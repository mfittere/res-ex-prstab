
from pyoptics import *
from matplotlib.pyplot import *
from numpy import *
from beams import *

#simulation parameters
EGeV=7000
epsn0=2.5 # emittance in mum
eps0=beamparam.emitrms(epsn0,EGeV) # geometric emittance in mum
print eps0

I=5.0 # A

#calculate the energy spread
beam='b2'
fn = 'twiss_lhc%s_ref.tfs'%beam
opt=optics.open(fn) # ref for reference file
print 'optics file = %s'%(fn)
print 'beta_x/y(IP5)=%2.4f/%2.4f m'%(opt.betx[opt//'IP5'],opt.bety[opt//'IP5'])
print 'p_x/y(IP5)=%4.2f/%4.2f urad'%(opt.px[opt//'IP5']*1.e6,opt.py[opt//'IP5']*1.e6)

# plot optics, HEL is marked with hel1
opt4=opt.select('E.DS.L4.%s'%beam.upper(),'S.DS.R4.%s'%beam.upper(),shift=False)
hel_name='HEBC'
sip4=opt4.s[opt4//'IP4']

shebip4=opt4.s[opt4//hel_name]-sip4
close('all')
opt4.plotbeta()
plot(list((opt4.s[opt4//hel_name],)*2),[-30,30],'k--',label='HEL: %s m'%shebip4)
plot(sip4,0,marker='o',color='orange',label='IP4')
handles,labels=gca().get_legend_handles_labels()
legend(handles[-2:],labels[-2:])
savefig('opthelip4%s.png'%beam,bbox_inches='tight')

# calculate e-lens parameters
sigx=sqrt(eps0*1.e-6*opt4.betx[opt4//hel_name]) # m
sigy=sqrt(eps0*1.e-6*opt4.bety[opt4//hel_name]) # m
sig=max([sigx,sigy])
r1=4*sig # m
## parameters CERN gun
r1gun=6.75e-3 # m
r2gun=12.7e-3 # m
r2ovr1 = r2gun/r1gun # r2/r1, r2 = outer radius, r1 = inner radius
r2=r2ovr1*r1
l=3 # m
EkeV_e=10 # keV
thetaelens=elens.hel_thetamax(r2,I,l,EkeV_e,EGeV,'opposite')

# print e-lens summary
print 'I = %4.2f A, E= %4.2f keV, l=%4.2f m'%(I,EkeV_e,l)
print 'selens = %4.2f m'%shebip4
print 'thetamax = %4.8e rad'%(thetaelens)
print 'r2 = %4.6e cm'%(r2*1.e2)
print 'r2/r1 = %4.6f'%(r2ovr1)
print 'r1 = %4.6e cm'%(r1*1.e2)
print 'betx = %4.2f m'%(opt4.betx[opt4//hel_name])
print 'bety = %4.2f m'%(opt4.bety[opt4//hel_name])
print 'dx = %4.2f m'%(opt4.dx[opt4//hel_name])
print 'dy = %4.2f m'%(opt4.dy[opt4//hel_name])
print 'sigx(betatron) = %4.6e cm'%(sigx*1.e2)
print 'sigy(betatron) = %4.6e cm'%(sigy*1.e2)
print 'r2 = %4.6e sigmax'%(r2/sigx)
print 'r1 = %4.6e sigmax'%(r1/sigx)
print 'r2 = %4.6e sigmay'%(r2/sigy)
print 'r1 = %4.6e sigmay'%(r1/sigy)
print 'sigx(betatron)/sigy(betatron) = %4.2e'%(sigx/sigy)

draw()
show()




