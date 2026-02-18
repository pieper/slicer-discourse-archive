# ELF load command address/offset not properly aligned

**Topic ID**: 18039
**Date**: 2021-06-09
**URL**: https://discourse.slicer.org/t/elf-load-command-address-offset-not-properly-aligned/18039

---

## Post #1 by @muratmaga (2021-06-09 12:53 UTC)

<p>This is not a slicer issue per se, but perhaps someone on the forum might suggest what this errors means.</p>
<p>This happens inside a docker instance of SlicerMorph. So some sort of a missing library might be at play, but not exactly sure how to find out more about it:</p>
<p>It is helpful, the host is centos 7.x, and the docker container is ubuntu 20.04.2.LTS</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/docker/slicer/NA-MIC/Extensions-29738/Auto3dgm/lib/Slicer-4.11/qt-scripted-modules/Auto3dgm.py", line 198, in onLoad
    self.Auto3dgmData.datasetCollection=Auto3dgmLogic.createDataset(self.meshFolder)
  File "/home/docker/slicer/NA-MIC/Extensions-29738/Auto3dgm/lib/Slicer-4.11/qt-scripted-modules/Auto3dgm.py", line 485, in createDataset
    from auto3dgm_nazar.dataset.datasetfactory import DatasetFactory
  File "/home/docker/slicer/NA-MIC/Extensions-29738/Auto3dgm/lib/Slicer-4.11/qt-scripted-modules/auto3dgm_nazar/dataset/datasetfactory.py", line 5, in &lt;module&gt;
    from auto3dgm_nazar.mesh.subsample import Subsample 
  File "/home/docker/slicer/NA-MIC/Extensions-29738/Auto3dgm/lib/Slicer-4.11/qt-scripted-modules/auto3dgm_nazar/mesh/subsample.py", line 27, in &lt;module&gt;
    from scipy.spatial.distance import cdist
  File "/home/docker/slicer/lib/Python/lib/python3.6/site-packages/scipy/spatial/__init__.py", line 101, in &lt;module&gt;
    from ._procrustes import procrustes
  File "/home/docker/slicer/lib/Python/lib/python3.6/site-packages/scipy/spatial/_procrustes.py", line 9, in &lt;module&gt;
    from scipy.linalg import orthogonal_procrustes
  File "/home/docker/slicer/lib/Python/lib/python3.6/site-packages/scipy/linalg/__init__.py", line 194, in &lt;module&gt;
    from .misc import *
  File "/home/docker/slicer/lib/Python/lib/python3.6/site-packages/scipy/linalg/misc.py", line 3, in &lt;module&gt;
    from .blas import get_blas_funcs
  File "/home/docker/slicer/lib/Python/lib/python3.6/site-packages/scipy/linalg/blas.py", line 213, in &lt;module&gt;
    from scipy.linalg import _fblas
ImportError: /home/docker/slicer/lib/Python/lib/python3.6/site-packages/scipy/linalg/_fblas.cpython-36m-x86_64-linux-gnu.so: ELF load command address/offset not properly aligned
</code></pre>

---

## Post #2 by @hherhold (2021-06-09 12:57 UTC)

<p>From a quick search online- this looks like maybe a packaging issue where a library that’s depended on by something else has been improperly stripped?</p>

---

## Post #3 by @muratmaga (2021-06-09 13:10 UTC)

<p>Thanks, pip_uninstall(‘scipy’) followed by pip_install(‘scipy’) fixed the issue.</p>

---
