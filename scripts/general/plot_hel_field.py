from beams import *
from pyoptics import *
from numpy import *
from matplotlib.pyplot import *
import matplotlib.patches as patches

# plot optics
# optics HLLHCV1.0, 6m beta* (v10beta0_600c3o0nobb_noerr)
opt=optics.open('../optics_hel/twiss_lhcb1.tfs')
opt4=opt.select('E.DS.L4.B1','S.DS.R4.B1',shift=False)

sip4=opt4.s[opt4//'IP4']
shebip4=opt4.s[opt4//'HEBC']-sip4
close('all')
opt4.plotbeta()
plot(list((opt4.s[opt4//'HEBC'],)*2),[-30,30],'k--',label='HEL: %4.1f m'%shebip4)
plot(sip4,0,marker='o',color='orange',label='IP4')
handles,labels=gca().get_legend_handles_labels()
legend(handles[-2:],labels[-2:])
savefig('opthelip4b1.png',bbox_inches='tight')


# HEL parameters
EGeV=7000
epsn0=2.5 # emittance in mum
eps0=beamparam.emitrms(epsn0,EGeV) # geometric emittance in mum

# parameters CERN gun
I=5.0 # A
EkeV_e=10 # keV
r1gun=6.75e-3 # m
r2gun=12.7e-3 # m
r2ovr1 = r2gun/r1gun # r2/r1, r2 = outer radius, r1 = inner radius

# parameters HEL
l=3 # m

# calculate e-lens parameters
sigx_betatron=sqrt(eps0*1.e-6*opt4.betx[opt4//'HEBC']) # m
sigy_betatron=sqrt(eps0*1.e-6*opt4.bety[opt4//'HEBC']) # m
sig=max([sigx_betatron,sigy_betatron])
nsig=4 #HEL inner radius [sigma]
r1=nsig*sig # m
r2=r2ovr1*r1
thetaelens=float(elens.hel_thetamax(r2,I,l,EkeV_e,EGeV,'opposite'))

# collimator settings in units of [sigma] for epsn0
nsigcol=5.7
epscol=3.5
nsigcol_beam=nsigcol*sqrt(epscol/epsn0)

close('all')
figure(figsize=(5,4))
ax1=gca()
ax2=ax1.twinx()
# current density
width=nsig*(r2ovr1-1)
ax1.add_patch(patches.Rectangle((nsig,0),width,thetaelens,facecolor='b',alpha=0.6))
ax1.add_patch(patches.Rectangle((-nsig,0),-width,thetaelens,facecolor='b',alpha=0.6))
# collimator
ax1.add_patch(patches.Rectangle((nsigcol_beam,0),10,thetaelens*2,color='Gray',alpha=0.5,edgecolor='k',hatch='\\\\',fill=True))
ax1.add_patch(patches.Rectangle((-nsigcol_beam,0),-10,thetaelens*2,color='Gray',alpha=0.5,edgecolor='k',hatch='//',fill=True))
#ax1.grid(b=True,axis='both',which='major')
ax1.xaxis.set_tick_params(labelsize=16,labelcolor='k',color='k')
ax1.yaxis.set_tick_params(labelsize=16,labelcolor='b',color='b')
ax1.set_xlabel('horizontal position [$\sigma_p$]',fontsize=16)
ax1.set_ylabel(r'current density [arb. units]',fontsize=16,color='b')
r=arange(-12*sig,12*sig,0.01*sig)
# electric field
ax2.plot(r/sig,elens.hel_kick(r,r1,r2,thetaelens),'r-',lw=4)
ax2.set_ylabel(r'em-field strength [arb. units]',fontsize=16,color='r')
ax2.yaxis.set_tick_params(labelsize=16,labelcolor='r',color='r')
for ax in ax1,ax2:
  ax.set_yticklabels([])
  ax.set_ylim(0,thetaelens*1.1)
  ax.set_xlim(-10,10)
tight_layout()

text(8.2,2.e-7,'collimator',rotation=90,fontsize=20)
text(-9.5,2.e-7,'collimator',rotation=90,fontsize=20)
savefig('kick_hel_lhc_no_grid.pdf',bbox_inches='tight')
savefig('kick_hel_lhc_no_grid.png',bbox_inches='tight')

draw()
show()





