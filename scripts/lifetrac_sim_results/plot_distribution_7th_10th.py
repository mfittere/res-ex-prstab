from LifeDesk import *
import os
from matplotlib.pyplot import *

# directory with simulation results
basedir = "/home/mfittere/work/MDs/mdelens/simulations/lifetrac"
# plot directory for paper
plt_dir = "plots"

close('all')
for sk in ['7','10']:
  opt = '2016injnocolc15o+19_6errb2ut%ssk/1/eps3.5/hv9_6e-8/p1e4t1e2s100weight'%sk
  t=LifeDeskDB.getdata(ltr_dir=os.path.join(basedir,opt),plt_dir=plt_dir)
  t.get_hist()
  t.plot_hist_xyz(title=sk)
  for p in 'xyz':
    figure('%s %s'%(sk,p))
    savefig('%s/2016injerra2b2u_%sthhv_3_5um_hist_%s.png'%(plt_dir,sk,p),bbox_inches='tight')

draw()
show()

