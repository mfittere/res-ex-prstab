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
# no pulsing
opt0 = "2016injnocolc15o+19_6errb2u/1/eps3.5/p1e4t1e4s100weight"
# with pulsing
optsk = "2016injnocolc15o+19_6errb2ut%ssk/1/eps3.5/hv9_6e-8/p1e4t1e4s100weight"
# random
optran8 = "2016injnocolc15o+19_6errb2uran/1/eps3.5/hv9_6e-8/p1e4t1e4s100weight"
optran9 = "2016injnocolc15o+19_6errb2uran/1/eps3.5/hv9_6e-9/p1e4t1e4s100weight"

# no excitation
t0 = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,opt0),plt_dir=plt_dir)

plt.close('all')
# losses
plt.figure("losses 2016, 3.5 um emittance")
plt.plot(t0.data['time'],t0.data['intensity'],'k-')
for sk,csk in zip(['2','3','4','6','8','9','10'],['b','r','g','pink','cyan','indigo','lime']):
#for sk,csk in zip(range(2,11),['b','r','g','m','orange','pink','cyan','indigo','lime']):
  t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%sk),plt_dir=plt_dir)
  if sk == '2':
    pltlbl = '2nd'
  elif sk == '3':
    pltlbl = '3rd'
  else:
    pltlbl = '%sth'%sk
  plt.plot(t.data['time'],t.data['intensity'],linestyle='-',color=csk,label=pltlbl)
plt.grid(b=True)
plt.xlabel('time [s]')
plt.ylabel('relative intensity')
leg = plt.legend(title='pulsing pattern',ncol=2,fontsize=12)
plt.setp(leg.get_title(),fontsize=12)
plt.savefig(os.path.join(plt_dir,'2016injerrb2u_pattern_3_5um_intensity.png'),bbox_inches='tight')

# bunch length
plt.figure("bunch length 2016, 3.5 um emittance")
plt.plot(t0.data['time'],t0.data['sigm'],'k-')
for sk,csk in zip(['2','3','4','6','8','9','10'],['b','r','g','pink','cyan','indigo','lime']):
#for sk,csk in zip(range(2,11),['b','r','g','m','orange','pink','cyan','indigo','lime']):
  t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%sk),plt_dir=plt_dir)
  if sk == '2':
    pltlbl = '2nd'
  elif sk == '3':
    pltlbl = '3rd'
  else:
    pltlbl = '%sth'%sk
  plt.plot(t.data['time'],t.data['sigm'],linestyle='-',color=csk,label=pltlbl)
plt.grid(b=True)
plt.xlabel('time [s]')
plt.ylabel('bunch length [cm]')
leg = plt.legend(title='pulsing pattern',ncol=2)
plt.setp(leg.get_title(),fontsize=12)
plt.savefig(os.path.join(plt_dir,'2016injerrb2u_pattern_3_5um_sigm.png'),bbox_inches='tight')

# emittance
for phv,p12 in zip(['hor.','vert.'],'12'):
  plt.figure("%s emit 2016, 3.5 um emittance"%(phv))
  plt.plot(t0.data['time'],t0.data['emit%s'%p12],'k-')
  for sk,csk in zip(['2','3','4','6','8','9','10'],['b','r','g','pink','cyan','indigo','lime']):
  #for sk,csk in zip(range(2,11),['b','r','g','m','orange','pink','cyan','indigo','lime']):
    t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%sk),plt_dir=plt_dir)
    if sk == '2':
      pltlbl = '2nd'
    elif sk == '3':
      pltlbl = '3rd'
    else:
      pltlbl = '%sth'%sk
    plt.plot(t.data['time'],t.data['emit%s'%p12],linestyle='-',color=csk,label=pltlbl)
  plt.xlabel('time [s]')
  plt.ylabel('%s normalized emittance [$\mu$m]'%phv)
  plt.grid(b=True)
  leg = plt.legend(title='pulsing pattern',ncol=2)
  plt.setp(leg.get_title(),fontsize=12)
  plt.savefig(os.path.join(plt_dir,'2016injerrb2u_pattern_3_5um_emit%s.png'%p12),bbox_inches='tight')

## bunch length
#plt.figure("long. sigm 2016, 3.5 um emittance")
#plt.plot(t0.data['time'],t0.data['sigm'],'k-')


plt.draw()
plt.show()

