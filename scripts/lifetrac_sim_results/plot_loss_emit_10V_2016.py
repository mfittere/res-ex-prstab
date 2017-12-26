from LifeDesk import *

import os
import matplotlib as mpl
import matplotlib.pyplot as plt

# plot settings
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
mpl.rcParams['axes.labelsize']  = 14
mpl.rcParams['legend.fontsize']  = 12
mpl.rcParams['legend.fontsize']  = 12

# directory with simulation results
basedir = "/home/mfittere/work/MDs/mdelens/simulations/lifetrac"
# plot directory for paper
plt_dir = "plots"

# 2016 optics
# no noise
opt0 = "2016injnocolc15o+19_6errb2u/1/eps3.5/p1e4t1e4s100weight"
# only with random noise
opt0ran = "2016injnocolc15o+19_6errb2uran/1/eps3.5/1_2e-3/p1e4t1e4s100weight"
# random noise + 10th V pulsing
optskran = "2016injnocolc15o+19_6errb2ut10skran/1/eps3.5/v%se-8ran1_2e-3/p1e4t1e4s100weight"
# 10th V pulsing
optsk    = "2016injnocolc15o+19_6errb2ut10sk/1/eps3.5/v%se-8/p1e4t1e4s100weight"

# no 10th turn pulsing
t0 = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,opt0),plt_dir=plt_dir)
t0ran = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,opt0ran),plt_dir=plt_dir)

plt.close('all')
# losses
# open file to dump loss rates [%/h]
f = open(os.path.join(basedir,'2016injnocolc15o+19_6errb2ut10skran/1/eps3.5/','losses_ran_10V'), 'w+')
f.write("# amplitude [nrad] loss rate [%/h]\n")
plt.figure("losses 2016, 3.5 um emittance")
plt.plot(t0.data['time'],t0.data['intensity'],'k-',label='0 nrad')
plt.plot(t0ran.data['time'],t0ran.data['intensity'],'k:',label='0 nrad')
lossrate = -(t0ran.data['intensity'][-1]-t0ran.data['intensity'][0])/(t0ran.data['time'][-1]-t0ran.data['time'][0])*60*60*100
f.write("0 %4.8e\n"%(lossrate))
for amp,camp in zip(['4_8','9_6'],['b','r','g','m','orange','pink','cyan','indigo','lime']):
  t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%amp),plt_dir=plt_dir)
  tran = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optskran%amp),plt_dir=plt_dir)
  pltlbl = amp.replace('_','')+' nrad'
  plt.plot(t.data['time'],t.data['intensity'],linestyle='-',color=camp,label=pltlbl)
  plt.plot(tran.data['time'],tran.data['intensity'],linestyle=':',color=camp,label=pltlbl)
  # dump the loss rates into the file 2016injnocolc15o+19_6errb2ut10skran/1/eps3.5/losses_10V
  lossrate = -(t.data['intensity'][-1]-t.data['intensity'][0])/(t.data['time'][-1]-t.data['time'][0])*60*60*100
  f.write("%s %4.8e\n"%(amp.replace('_',''),lossrate))
plt.grid(b=True)
plt.xlabel('time [s]')
plt.ylabel('relative intensity')
f.close()

## bunch length
#plt.figure("bunch length 2016, 3.5 um emittance")
#plt.plot(t0.data['time'],t0.data['sigm'],'k-',label='0 nrad')
#plt.plot(t0ran.data['time'],t0ran.data['sigm'],'k:',label='0 nrad')
#for amp,camp in zip(['4_8','9_6'],['b','r','g','m','orange','pink','cyan','indigo','lime']):
#  t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%amp),plt_dir=plt_dir)
#  tran = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optskran%amp),plt_dir=plt_dir)
#  pltlbl = amp.replace('_','')+' nrad'
#  plt.plot(t.data['time'],t.data['sigm'],linestyle='-',color=camp,label=pltlbl)
#  plt.plot(tran.data['time'],tran.data['sigm'],linestyle=':',color=camp,label=pltlbl)
#plt.grid(b=True)
#plt.xlabel('time [s]')
#plt.ylabel('bunch length [cm]')
#
## emittance
#for phv,p12 in zip(['hor.','vert.'],'12'):
#  plt.figure("%s emit 2016, 3.5 um emittance"%(phv))
#  plt.plot(t0.data['time'],t0.data['emit%s'%p12],'k-',label='0 nrad')
#  plt.plot(t0ran.data['time'],t0ran.data['emit%s'%p12],'k:',label='0 nrad')
#  for amp,camp in zip(['4_8','9_6'],['b','r','g','m','orange','pink','cyan','indigo','lime']):
#    t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%amp),plt_dir=plt_dir)
#    tran = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optskran%amp),plt_dir=plt_dir)
#    pltlbl = amp.replace('_','')+' nrad'
#    plt.plot(t.data['time'],t.data['emit%s'%p12],linestyle='-',color=camp,label=pltlbl)
#    plt.plot(tran.data['time'],tran.data['emit%s'%p12],linestyle=':',color=camp,label=pltlbl)
#  plt.xlabel('time [s]')
#  plt.ylabel('%s normalized emittance [$\mu$m]'%phv)
#  plt.grid(b=True)
#
## relative emittance growth
#for phv,p12 in zip(['hor.','vert.'],'12'):
#  plt.figure("rel. %s emit 2016, 3.5 um emittance"%(phv))
#  plt.plot(t0.data['time'],t0.data['emit%s'%p12]/t0.data['emit%s'%p12][0],'k-',label='0 nrad')
#  plt.plot(t0ran.data['time'],t0ran.data['emit%s'%p12]/t0.data['emit%s'%p12][0],'k:',label='0 nrad')
#  for amp,camp in zip(['4_8','9_6'],['b','r','g','m','orange','pink','cyan','indigo','lime']):
#    t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%amp),plt_dir=plt_dir)
#    tran = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optskran%amp),plt_dir=plt_dir)
#    pltlbl = amp.replace('_','')+' nrad'
#    plt.plot(t.data['time'],t.data['emit%s'%p12]/t.data['emit%s'%p12][0],linestyle='-',color=camp,label=pltlbl)
#    plt.plot(tran.data['time'],tran.data['emit%s'%p12]/tran.data['emit%s'%p12][0],linestyle=':',color=camp,label=pltlbl)
#  plt.xlabel('time [s]')
#  plt.ylabel('rel. %s normalized emittance [$\mu$m]'%phv)
#  plt.grid(b=True)
#
## now do the legends for all plots
#paramsfig = ['losses','bunch length','hor. emit','vert. emit','rel. hor. emit','rel. vert. emit']
#params    = ['intensity','sig','emit1','emit2','emit1_rel','emit2_rel'] 
#for param,paramfig in zip(params,paramsfig):
#  plt.figure("%s 2016, 3.5 um emittance"%paramfig)
#  handles,labels = plt.gca().get_legend_handles_labels()
#  if param in ['intensity','sig']:
#    loc1 = 'lower left'
#    loc2 = 'center left'
#  else:
#    loc1 = 'center left'
#    loc2 = 'upper left'
#  leg1 = plt.legend(title='excitation\n10th turn V',ncol=1,fontsize=12,
#                   handles=handles[::2],labels=labels[::2],loc=loc1)
#  leg2 = plt.legend(title='excitation\nrandom H+V',ncol=1,fontsize=12,
#                   handles=handles[:2],labels=['0 nrad','6 nrad'],loc=loc2)
#  plt.gca().add_artist(leg1)
#  plt.setp(leg1.get_title(),fontsize=12)
#  plt.setp(leg2.get_title(),fontsize=12)
#  plt.savefig(os.path.join(plt_dir,'2016injerrb2uran1_2e-3_10thV_3_5um_%s.png'%param),bbox_inches='tight')

plt.draw()
plt.show()

