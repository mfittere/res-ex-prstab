from LifeDesk import *
import os
from matplotlib.pyplot import *

# directory with simulation results
#basedir = "/home/mfittere/work/MDs/mdelens/simulations/lifetrac"
basedir = "/home/fitterma/work/Fermilab/work/MDs/mdelens/simulations/lifetrac"
# plot directory for paper
plt_dir = "plots"

## use weighted Gaussian (p1e4t1e2s100weight) or not (p1e4t1e2s100)
weighted = False
# pulsing pattern H+V
#sk = 't7sk'
#ylimresdiff = [-7,7]
sk='t10sk'
ylimresdiff = [-3.1,3.1]
#sk='ran'
#ylimresdiff = [-3.1,3.1]

if weighted:
# weighted Gaussian
  opt = '2016injnocolc15o+19_6erra2b2u%s/1/eps3.5/hv9_6e-8/p1e4t1e2s100weight'%sk
else:
# normal Gaussian
  opt = '2016injnocolc15o+19_6erra2b2u%s/1/eps3.5/hv9_6e-8/p1e4t1e2s100'%sk

close('all')
t=LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,opt),plt_dir=plt_dir)
t.get_hist()
t.plot_hist_xyz(title=sk,ylimhist=[1.e-4,1.1],ylimresdiff=ylimresdiff,ylimresrat=[0.1,10])
for p in 'xyz':
  figure('%s %s'%(sk,p))
  if weighted:
    savefig('%s/2016injerra2b2u_%shv_3_5um_hist_weighted_%s.png'%(plt_dir,sk,p),bbox_inches='tight')
  else:
    savefig('%s/2016injerra2b2u_%shv_3_5um_hist_%s.png'%(plt_dir,sk,p),bbox_inches='tight')

## no excitation
#if weighted:
## weighted Gaussian
#  opt = '2016injnocolc15o+19_6erra2b2u/1/eps3.5/p1e4t1e2s100weight'
#else:
## normal Gaussian
#  opt = '2016injnocolc15o+19_6erra2b2u/1/eps3.5/p1e4t1e2s100'
#close('all')
#print(os.path.join(basedir,opt))
#t=LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,opt),plt_dir=plt_dir)
#t.get_hist()
#t.plot_hist_xyz(title='no excitation',ylimhist=[1.e-4,1.1],ylimresdiff=ylimresdiff,ylimresrat=[0.1,10])
#for p in 'xyz':
#  figure('no excitation %s'%(p))
#  if weighted:
#    savefig('%s/2016injerra2b2u_3_5um_hist_weighted_%s.png'%(plt_dir,p),bbox_inches='tight')
#  else:
#    savefig('%s/2016injerra2b2u_3_5um_hist_%s.png'%(plt_dir,p),bbox_inches='tight')

draw()
show()

