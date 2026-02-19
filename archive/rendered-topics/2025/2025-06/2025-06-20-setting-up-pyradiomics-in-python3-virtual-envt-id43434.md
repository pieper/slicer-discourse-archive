---
topic_id: 43434
title: "Setting Up Pyradiomics In Python3 Virtual Envt"
date: 2025-06-20
url: https://discourse.slicer.org/t/43434
---

# setting up pyradiomics in python3 virtual env't

**Topic ID**: 43434
**Date**: 2025-06-20
**URL**: https://discourse.slicer.org/t/setting-up-pyradiomics-in-python3-virtual-envt/43434

---

## Post #1 by @tsc (2025-06-20 14:47 UTC)

<p>I am having some trouble with pyradiomics in my python3 virtual env’t on one particular server.  The issue may be that numpy 1.21.5 is present on the server and numpy 2.2.6 is present in the virtual env’t.   Pyradiomics and all dependencies are setup in the virtual env’t.</p>
<p>pip3 list from inside the virtual env’t shows the following:</p>
<blockquote>
<p>(mcs-virtual) tomcat@server03:/home/tomcat-tmp/mcs-virtual$ pip3 list<br>
Package          Version</p>
<hr>
<p>colorama         0.4.6<br>
contourpy        1.3.2<br>
cycler           0.12.1<br>
docopt           0.6.2<br>
fonttools        4.58.2<br>
imageio          2.37.0<br>
kiwisolver       1.4.8<br>
lazy_loader      0.4<br>
matplotlib       3.10.3<br>
networkx         3.4.2<br>
numpy            2.2.6<br>
opencv-python    4.11.0.86<br>
packaging        25.0<br>
pillow           11.2.1<br>
pip              22.0.2<br>
pydicom          3.0.1<br>
pykwalify        1.8.0<br>
pyparsing        3.2.3<br>
pyradiomics      3.0.1<br>
python-dateutil  2.9.0.post0<br>
PyWavelets       1.8.0<br>
ruamel.yaml      0.18.14<br>
ruamel.yaml.clib 0.2.12<br>
scikit-image     0.25.2<br>
scipy            1.15.3<br>
setuptools       80.9.0<br>
simpleitk        2.5.0<br>
six              1.17.0<br>
tifffile         2025.5.10</p>
</blockquote>
<p>Python in the virtual env’t:</p>
<blockquote>
<p>(mcs-virtual) tomcat@server03:/home/tomcat-tmp/mcs-virtual/$ which python<br>
/home/tomcat-tmp/mcs-virtual/bin/python</p>
</blockquote>
<p>radiomics is present under the site-packages folder in the virtual env:</p>
<blockquote>
<p>(mcs-virtual) tomcat@server03:/home/tomcat-tmp/mcs-virtual/lib/python3.10/site-packages/radiomics$ ls<br>
base.py					    featureextractor.py  glcm.py   glszm.py	       ngtdm.py     scripts	_version.py<br>
_cmatrices.cpython-310-x86_64-linux-gnu.so  firstorder.py	 gldm.py   imageoperations.py  <strong>pycache</strong>  shape2D.py<br>
_cshape.cpython-310-x86_64-linux-gnu.so     generalinfo.py	 glrlm.py  <strong>init</strong>.py	       schemas	    shape.py</p>
</blockquote>
<p>When I try to import radiomics, I see the following:</p>
<blockquote>
<p>(mcs-virtual) tomcat@server03:/home/tomcat-tmp/mcs-virtual/$ python</p>
<blockquote>
<blockquote>
<blockquote>
<p>import radiomics</p>
</blockquote>
</blockquote>
</blockquote>
<p>A module that was compiled using NumPy 1.x cannot be run in<br>
NumPy 2.2.6 as it may crash. To support both 1.x and 2.x<br>
versions of NumPy, modules must be compiled with NumPy 2.0.<br>
Some module may need to rebuild instead e.g. with ‘pybind11&gt;=2.12’.</p>
<p>If you are a user of the module, the easiest solution will be to<br>
downgrade to ‘numpy&lt;2’ or try to upgrade the affected module.<br>
We expect that some modules will need time to support NumPy 2.</p>
<p>Traceback (most recent call last):  File “”, line 1, in <br>
File “/home/tomcat-tmp/mcs-virtual/lib/python3.10/site-packages/radiomics/<strong>init</strong>.py”, line 286, in <br>
from radiomics import _cmatrices as cMatrices  # noqa: F401<br>
AttributeError: _ARRAY_API not found<br>
Error loading C extensions<br>
Traceback (most recent call last):<br>
File “/home/tomcat-tmp/mcs-virtual/lib/python3.10/site-packages/radiomics/<strong>init</strong>.py”, line 286, in <br>
from radiomics import _cmatrices as cMatrices  # noqa: F401<br>
ImportError: numpy.core.multiarray failed to import<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/tomcat-tmp/mcs-virtual/lib/python3.10/site-packages/radiomics/<strong>init</strong>.py”, line 297, in <br>
raise e<br>
File “/home/tomcat-tmp/mcs-virtual/lib/python3.10/site-packages/radiomics/<strong>init</strong>.py”, line 286, in <br>
from radiomics import _cmatrices as cMatrices  # noqa: F401<br>
ImportError: numpy.core.multiarray failed to import</p>
</blockquote>
<p>This is the path from inside the virtual env’t</p>
<blockquote>
<p>(mcs-virtual) tomcat@server03:/home/tomcat-tmp/mcs-virtual$ python</p>
<blockquote>
<blockquote>
<blockquote>
<p>import sys<br>
print(sys.path)<br>
[‘’, ‘/usr/lib/python310.zip’, ‘/usr/lib/python3.10’, ‘/usr/lib/python3.10/lib-dynload’, ‘/home/tomcat-tmp/mcs-virtual/lib/python3.10/site-packages’]</p>
</blockquote>
</blockquote>
</blockquote>
</blockquote>
<p>Numpy 1 is present on the server, but Numpy 2 is inside the virtual env’t.  Ideally, I do not want to downgrade from Numpy 2 in my virtual env’t.  This is a shared server and I do not want to upgrade from Numpy 1 on that server.  Given that I’m inside a python virtual env’t, I thought that it be an isolated env’t.  Any suggestions are appreciated.</p>
<p>Thanks!</p>

---
