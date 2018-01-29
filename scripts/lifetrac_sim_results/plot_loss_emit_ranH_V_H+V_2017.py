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

# 2017 optics
# only with random noise
opt0 = "2017injnocolc15o+19_6erra2b2u/1/eps3.5/p1e4t1e4s100weight"
# random noise + 7th pulsing
optsk = "2017injnocolc15o+19_6erra2b2uranadt/1/eps3.5/%s%se-8/p1e4t1e4s100weight"

# no excitation
t0 = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,opt0),plt_dir=plt_dir)

grid_flag = False

plt.close('all')
# losses
plt.figure("losses 2017, 3.5 um emittance")
plt.clf()
plt.plot(t0.data['time'],t0.data['intensity'],'k-',label='0 nrad')
for plane,cplane in zip(['h','v','h+v'],['b','r','g']):
  for amp,lamp in zip(['1_2','2_4'],['--',':']):
    t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%(plane.replace('+',''),amp)),plt_dir=plt_dir)
    pltlbl = plane.upper()+' '+amp.replace('_','')+' nrad'
    plt.plot(t.data['time'],t.data['intensity'],linestyle=lamp,color=cplane,label=pltlbl)
plt.grid(b=grid_flag)
plt.xlabel('time [s]')
plt.ylabel('relative intensity')
plt.ylim(0.9997,0.999825)
leg = plt.legend(title='random\nexcitation',ncol=1,fontsize=12)
plt.setp(leg.get_title(),fontsize=12)
plt.savefig(os.path.join(plt_dir,'2017injerra2b2u_ranadt_3_5um_intensity.png'),bbox_inches='tight')

# bunch length
plt.figure("bunch length 2016, 3.5 um emittance")
plt.plot(t0.data['time'],t0.data['sigm'],'k-',label='0 nrad')
for plane,cplane in zip(['h','v','h+v'],['b','r','g']):
  for amp,lamp in zip(['1_2','2_4'],['--',':']):
    t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%(plane.replace('+',''),amp)),plt_dir=plt_dir)
    pltlbl = plane.upper()+' '+amp.replace('_','')+' nrad'
    plt.plot(t.data['time'],t.data['sigm'],linestyle=lamp,color=cplane,label=pltlbl)
plt.grid(b=grid_flag)
plt.xlabel('time [s]')
plt.ylabel('bunch length [cm]')
plt.ylim(9.1905,9.1927)
leg = plt.legend(title='random\nexcitation',ncol=1,fontsize=12)
plt.setp(leg.get_title(),fontsize=12)
plt.savefig(os.path.join(plt_dir,'2017injerra2b2u_ranadt_3_5um_sigm.png'),bbox_inches='tight')

# emittance
for phv,p12 in zip(['hor.','vert.'],'12'):
  plt.figure("%s emit 2016, 3.5 um emittance"%(phv))
  plt.plot(t0.data['time'],t0.data['emit%s'%p12],'k-',label='0 nrad')
  for plane,cplane in zip(['h','v','h+v'],['b','r','g']):
    for amp,lamp in zip(['1_2','2_4'],['--',':']):
      t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%(plane.replace('+',''),amp)),plt_dir=plt_dir)
      pltlbl = plane.upper()+' '+amp.replace('_','')+' nrad'
      plt.plot(t.data['time'],t.data['emit%s'%p12],linestyle=lamp,color=cplane,label=pltlbl)
  plt.grid(b=grid_flag)
  plt.xlabel('time [s]')
  plt.ylabel('%s normalized emittance [$\mu$m]'%phv)
  plt.ylim(3.48,4.35)
  leg = plt.legend(title='random\nexcitation',ncol=1,fontsize=12)
  plt.setp(leg.get_title(),fontsize=12)
  plt.savefig(os.path.join(plt_dir,'2017injerra2b2u_ranadt_3_5um_emit%s.png'%p12),bbox_inches='tight')

# relative emittance growth
for phv,p12 in zip(['hor.','vert.'],'12'):
  plt.figure("rel. %s emit 2016, 3.5 um emittance"%(phv))
  plt.plot(t0.data['time'],t0.data['emit%s'%p12]/t0.data['emit%s'%p12][0],'k-',label='0 nrad')
  for plane,cplane in zip(['h','v','h+v'],['b','r','g']):
    for amp,lamp in zip(['1_2','2_4'],['--',':']):
      t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%(plane.replace('+',''),amp)),plt_dir=plt_dir)
      pltlbl = plane.upper()+' '+amp.replace('_','')+' nrad'
      plt.plot(t.data['time'],t.data['emit%s'%p12]/t.data['emit%s'%p12][0],linestyle=lamp,color=cplane,label=pltlbl)
  plt.grid(b=grid_flag)
  plt.xlabel('time [s]')
  plt.ylabel('rel. %s normalized emittance [$\mu$m]'%phv)
  leg = plt.legend(title='random\nexcitation',ncol=1,fontsize=12)
  plt.setp(leg.get_title(),fontsize=12)
  plt.savefig(os.path.join(plt_dir,'2017injerra2b2u_ranadt_3_5um_rel_emit%s.png'%p12),bbox_inches='tight')

plt.draw()
plt.show()

