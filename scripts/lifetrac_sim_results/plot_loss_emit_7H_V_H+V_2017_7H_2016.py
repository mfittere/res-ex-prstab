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
opt0_16 = "2016injnocolc15o+19_6erra2b2uran/1/eps3.5/1_2e-3/p1e4t1e4s100weight"
# random noise + 7th pulsing H
optsk_16 = "2016injnocolc15o+19_6erra2b2ut7skran/1/eps3.5/h%se-8ran1_2e-3/p1e4t1e4s100weight"

# 2017 optics
# only with random noise
opt0 = "2017injnocolc15o+19_6erra2b2uran/1/eps3.5/1_2e-3/p1e4t1e4s100weight"
# random noise + 7th pulsing
optsk = "2017injnocolc15o+19_6erra2b2ut7skran/1/eps3.5/%s%se-8ran1_2e-3/p1e4t1e4s100weight"

# no excitation
t0 = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,opt0),plt_dir=plt_dir)
t0_16 = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,opt0_16),plt_dir=plt_dir)

plt.close('all')
# losses
plt.figure("losses, 3.5 um emittance")
plt.clf()
# 2017
plt.plot(t0.data['time'],t0.data['intensity'],'k-',label='0 nrad')
for plane,cplane in zip(['h','v','h+v'],['b','r','g']):
  for amp,lamp in zip(['2_4','4_8'],['--',':']):
    t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%(plane.replace('+',''),amp)),plt_dir=plt_dir)
    pltlbl = plane.upper()+' '+amp.replace('_','')+' nrad'
    plt.plot(t.data['time'],t.data['intensity'],linestyle=lamp,color=cplane,label=pltlbl)
# 2016
plt.plot(t0_16.data['time'],t0_16.data['intensity'],linestyle='-',color='grey',label='0 nrad')
for amp,lamp in zip(['2_4','4_8'],['--',':']):
  t_16 = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk_16%(amp)),plt_dir=plt_dir)
  pltlbl = 'H '+amp.replace('_','')+' nrad'
  plt.plot(t_16.data['time'],t_16.data['intensity'],linestyle=lamp,color='orange',label=pltlbl)
plt.grid(b=True)
plt.xlabel('time [s]')
plt.ylabel('relative intensity')
handles,labels = plt.gca().get_legend_handles_labels()
leg1 = plt.legend(title='(2017)\n7th turn pulsing',ncol=1,fontsize=12,handles=handles[:-2],labels=labels[:-2],loc='lower left')
leg2 = plt.legend(title='(2016)\n7th turn pulsing',ncol=1,fontsize=12,handles=handles[-3:],labels=labels[-3:],loc='lower center')
plt.gca().add_artist(leg1)
plt.setp(leg1.get_title(),fontsize=12)
plt.setp(leg2.get_title(),fontsize=12)
plt.savefig(os.path.join(plt_dir,'2016+2017injerra2b2uran1_2e-3_7th_3_5um_intensity.png'),bbox_inches='tight')

# bunch length
plt.figure("bunch length, 3.5 um emittance")
plt.plot(t0.data['time'],t0.data['sigm'],'k-',label='0 nrad')
for plane,cplane in zip(['h','v','h+v'],['b','r','g']):
  for amp,lamp in zip(['2_4','4_8'],['--',':']):
    t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%(plane.replace('+',''),amp)),plt_dir=plt_dir)
    pltlbl = plane.upper()+' '+amp.replace('_','')+' nrad'
    plt.plot(t.data['time'],t.data['sigm'],linestyle=lamp,color=cplane,label=pltlbl)
# 2016
plt.plot(t0_16.data['time'],t0_16.data['sigm'],linestyle='-',color='grey',label='0 nrad')
for amp,lamp in zip(['2_4','4_8'],['--',':']):
  t_16 = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk_16%(amp)),plt_dir=plt_dir)
  pltlbl = 'H '+amp.replace('_','')+' nrad'
  plt.plot(t_16.data['time'],t_16.data['sigm'],linestyle=lamp,color='orange',label=pltlbl)
plt.grid(b=True)
plt.xlabel('time [s]')
plt.ylabel('bunch length [cm]')
handles,labels = plt.gca().get_legend_handles_labels()
leg1 = plt.legend(title='(2017)\n7th turn pulsing',ncol=1,fontsize=12,handles=handles[:-2],labels=labels[:-2],loc='lower left')
leg2 = plt.legend(title='(2016)\n7th turn pulsing',ncol=1,fontsize=12,handles=handles[-3:],labels=labels[-3:],loc='lower center')
plt.gca().add_artist(leg1)
plt.setp(leg1.get_title(),fontsize=12)
plt.setp(leg2.get_title(),fontsize=12)
plt.savefig(os.path.join(plt_dir,'2016+2017injerra2b2uran1_2e-3_7th_3_5um_sigm.png'),bbox_inches='tight')

# emittance
for phv,p12 in zip(['hor.','vert.'],'12'):
  plt.figure("%s emit, 3.5 um emittance"%(phv))
  plt.plot(t0.data['time'],t0.data['emit%s'%p12],'k-',label='0 nrad')
  for plane,cplane in zip(['h','v','h+v'],['b','r','g']):
    for amp,lamp in zip(['2_4','4_8'],['--',':']):
      t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%(plane.replace('+',''),amp)),plt_dir=plt_dir)
      pltlbl = plane.upper()+' '+amp.replace('_','')+' nrad'
      plt.plot(t.data['time'],t.data['emit%s'%p12],linestyle=lamp,color=cplane,label=pltlbl)
  # 2016
  plt.plot(t0_16.data['time'],t0_16.data['emit%s'%p12],linestyle='-',color='grey',label='0 nrad')
  for amp,lamp in zip(['2_4','4_8'],['--',':']):
    t_16 = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk_16%(amp)),plt_dir=plt_dir)
    pltlbl = 'H '+amp.replace('_','')+' nrad'
    plt.plot(t_16.data['time'],t_16.data['emit%s'%p12],linestyle=lamp,color='orange',label=pltlbl)
  plt.grid(b=True)
  plt.xlabel('time [s]')
  plt.ylabel('%s normalized emittance [$\mu$m]'%phv)
  handles,labels = plt.gca().get_legend_handles_labels()
  leg1 = plt.legend(title='(2017)\n7th turn pulsing',ncol=1,fontsize=12,handles=handles[:-2],labels=labels[:-2],loc='upper left')
  leg2 = plt.legend(title='(2016)\n7th turn pulsing',ncol=1,fontsize=12,handles=handles[-3:],labels=labels[-3:],loc='upper center')
  plt.gca().add_artist(leg1)
  plt.setp(leg1.get_title(),fontsize=12)
  plt.setp(leg2.get_title(),fontsize=12)
  plt.savefig(os.path.join(plt_dir,'2016+2017injerra2b2uran1_2e-3_7th_3_5um_emit%s.png'%p12),bbox_inches='tight')

# relative emittance growth
for phv,p12 in zip(['hor.','vert.'],'12'):
  plt.figure("rel. %s emit, 3.5 um emittance"%(phv))
  plt.plot(t0.data['time'],t0.data['emit%s'%p12]/t0.data['emit%s'%p12][0],'k-',label='0 nrad')
  for plane,cplane in zip(['h','v','h+v'],['b','r','g']):
    for amp,lamp in zip(['2_4','4_8'],['--',':']):
      t = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk%(plane.replace('+',''),amp)),plt_dir=plt_dir)
      pltlbl = plane.upper()+' '+amp.replace('_','')+' nrad'
      plt.plot(t.data['time'],t.data['emit%s'%p12]/t.data['emit%s'%p12][0],linestyle=lamp,color=cplane,label=pltlbl)
  # 2016
  plt.plot(t0_16.data['time'],t0_16.data['emit%s'%p12]/t0_16.data['emit%s'%p12][0],linestyle='-',color='grey',label='0 nrad')
  for amp,lamp in zip(['2_4','4_8'],['--',':']):
    t_16 = LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,optsk_16%(amp)),plt_dir=plt_dir)
    pltlbl = 'H '+amp.replace('_','')+' nrad'
    plt.plot(t_16.data['time'],t_16.data['emit%s'%p12]/t_16.data['emit%s'%p12][0],linestyle=lamp,color='orange',label=pltlbl)
  plt.grid(b=True)
  plt.xlabel('time [s]')
  plt.ylabel('rel. %s normalized emittance [$\mu$m]'%phv)
  handles,labels = plt.gca().get_legend_handles_labels()
  leg1 = plt.legend(title='(2017)\n7th turn pulsing',ncol=1,fontsize=12,handles=handles[:-2],labels=labels[:-2],loc='upper left')
  leg2 = plt.legend(title='(2016)\n7th turn pulsing',ncol=1,fontsize=12,handles=handles[-3:],labels=labels[-3:],loc='upper center')
  plt.gca().add_artist(leg1)
  plt.setp(leg1.get_title(),fontsize=12)
  plt.setp(leg2.get_title(),fontsize=12)
  plt.savefig(os.path.join(plt_dir,'2016+2017injerra2b2uran1_2e-3_7th_3_5um_rel_emit%s.png'%p12),bbox_inches='tight')

plt.draw()
plt.show()

