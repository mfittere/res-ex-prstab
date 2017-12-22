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
# only with random noise
opt0 = "2016injnocolc15o+19_6errb2uran/1/eps3.5/1_2e-3/p1e4t1e4s100weight"
# random noise + 7th pulsing
optsk = "2016injnocolc15o+19_6errb2ut7skran/1/eps3.5/h%se-8ran1_2e-3/p1e4t1e4s100weight"

# no excitation
t0 = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,opt0),plt_dir=plt_dir)

plt.close('all')
# losses
plt.figure("losses 2016, 3.5 um emittance")
plt.plot(t0.data['time'],t0.data['intensity'],'k-',label='0 nrad')
for amp,camp in zip(['1_2','2_4','4_8'],['b','r','g','m','orange','pink','cyan','indigo','lime']):
  t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%amp),plt_dir=plt_dir)
  pltlbl = amp.replace('_','')+' nrad'
  plt.plot(t.data['time'],t.data['intensity'],linestyle='-',color=camp,label=pltlbl)
plt.grid(b=True)
plt.xlabel('time [s]')
plt.ylabel('relative intensity')
leg = plt.legend(title='6 nrad random + 7th turn',ncol=2,fontsize=12)
plt.setp(leg.get_title(),fontsize=12)
plt.savefig(os.path.join(plt_dir,'2016injerrb2uran1_2e-3_7th_3_5um_intensity.png'),bbox_inches='tight')

# bunch length
plt.figure("bunch length 2016, 3.5 um emittance")
plt.plot(t0.data['time'],t0.data['sigm'],'k-',label='0 nrad')
for amp,camp in zip(['1_2','2_4','4_8'],['b','r','g','m','orange','pink','cyan','indigo','lime']):
  t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%amp),plt_dir=plt_dir)
  pltlbl = amp.replace('_','')+' nrad'
  plt.plot(t.data['time'],t.data['sigm'],linestyle='-',color=camp,label=pltlbl)
plt.grid(b=True)
plt.xlabel('time [s]')
plt.ylabel('bunch length [cm]')
leg = plt.legend(title='6 nrad random + 7th turn',ncol=2)
plt.setp(leg.get_title(),fontsize=12)
plt.savefig(os.path.join(plt_dir,'2016injerrb2uran1_2e-3_7th_3_5um_sigm.png'),bbox_inches='tight')

# emittance
for phv,p12 in zip(['hor.','vert.'],'12'):
  plt.figure("%s emit 2016, 3.5 um emittance"%(phv))
  plt.plot(t0.data['time'],t0.data['emit%s'%p12],'k-',label='0 nrad')
  for amp,camp in zip(['1_2','2_4','4_8'],['b','r','g','m','orange','pink','cyan','indigo','lime']):
    t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%amp),plt_dir=plt_dir)
    pltlbl = amp.replace('_','')+' nrad'
    plt.plot(t.data['time'],t.data['emit%s'%p12],linestyle='-',color=camp,label=pltlbl)
  plt.xlabel('time [s]')
  plt.ylabel('%s normalized emittance [$\mu$m]'%phv)
  plt.grid(b=True)
  leg = plt.legend(title='6 nrad random + 7th turn',ncol=2)
  plt.setp(leg.get_title(),fontsize=12)
  plt.savefig(os.path.join(plt_dir,'2016injerrb2uran1_2e-3_7th_3_5um_emit%s.png'%p12),bbox_inches='tight')

# relative emittance growth
for phv,p12 in zip(['hor.','vert.'],'12'):
  plt.figure("rel. %s emit 2016, 3.5 um emittance"%(phv))
  plt.plot(t0.data['time'],t0.data['emit%s'%p12]/t0.data['emit%s'%p12][0],'k-',label='0 nrad')
  for amp,camp in zip(['1_2','2_4','4_8'],['b','r','g','m','orange','pink','cyan','indigo','lime']):
    t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%amp),plt_dir=plt_dir)
    pltlbl = amp.replace('_','')+' nrad'
    plt.plot(t.data['time'],t.data['emit%s'%p12]/t.data['emit%s'%p12][0],linestyle='-',color=camp,label=pltlbl)
  plt.xlabel('time [s]')
  plt.ylabel('rel. %s normalized emittance [$\mu$m]'%phv)
  plt.grid(b=True)
  leg = plt.legend(title='6 nrad random + 7th turn',ncol=2)
  plt.setp(leg.get_title(),fontsize=12)
  plt.savefig(os.path.join(plt_dir,'2016injerrb2uran1_2e-3_7th_3_5um_emit%s.png'%p12),bbox_inches='tight')

plt.draw()
plt.show()

