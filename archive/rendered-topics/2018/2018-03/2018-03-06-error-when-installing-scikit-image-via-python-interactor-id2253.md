# Error when installing scikit-image via Python Interactor

**Topic ID**: 2253
**Date**: 2018-03-06
**URL**: https://discourse.slicer.org/t/error-when-installing-scikit-image-via-python-interactor/2253

---

## Post #1 by @ckuzi001 (2018-03-06 22:13 UTC)

<p>Hello Everyone,</p>
<p>I am attempting to install the scikit-image package via the Slicer Python Interactor using the command:</p>
<blockquote>
<blockquote>
<blockquote>
<p>pip.main([‘install’, ‘scikit-image’])</p>
</blockquote>
</blockquote>
</blockquote>
<p>However, this throws an error.  As a test, I tried the same command using other packages, including scikit-learn.</p>
<blockquote>
<blockquote>
<blockquote>
<p>pip.main([‘install’, ‘scikit-learn’])</p>
</blockquote>
</blockquote>
</blockquote>
<p>This worked without any errors. The version I am running is 3D Slicer 4.8.1/Python 2.7 on Ubuntu. Any assistance resolving this issue would be greatly appreciated.</p>
<p>Thank you,</p>
<p>~ Carrie</p>
<p>PS – I’ve copied and pasted the output below.</p>
<pre><code class="lang-auto">----------------------------------------------------------------------------------------------------

Collecting scikit-image
  Using cached scikit_image-0.13.1-cp27-cp27m-manylinux1_x86_64.whl
Collecting matplotlib&gt;=1.3.1 (from scikit-image)
  Using cached matplotlib-2.2.0-cp27-cp27m-manylinux1_x86_64.whl
Requirement already up-to-date: six&gt;=1.7.3 in ./lib/Python/lib/python2.7/site-packages (from scikit-image)
Collecting networkx&gt;=1.8 (from scikit-image)
  Using cached networkx-2.1.zip
Collecting pillow&gt;=2.1.0 (from scikit-image)
  Using cached Pillow-5.0.0-cp27-cp27m-manylinux1_x86_64.whl
Collecting PyWavelets&gt;=0.4.0 (from scikit-image)
  Using cached PyWavelets-0.5.2-cp27-cp27m-manylinux1_x86_64.whl
Requirement already up-to-date: scipy&gt;=0.17.0 in ./lib/Python/lib/python2.7/site-packages (from scikit-image)
Requirement already up-to-date: python-dateutil&gt;=2.1 in ./lib/Python/lib/python2.7/site-packages (from matplotlib&gt;=1.3.1-&gt;scikit-image)
Requirement already up-to-date: cycler&gt;=0.10 in ./lib/Python/lib/python2.7/site-packages (from matplotlib&gt;=1.3.1-&gt;scikit-image)
Collecting subprocess32 (from matplotlib&gt;=1.3.1-&gt;scikit-image)
  Using cached subprocess32-3.2.7.tar.gz
Collecting pytz (from matplotlib&gt;=1.3.1-&gt;scikit-image)
  Using cached pytz-2018.3-py2.py3-none-any.whl
Collecting backports.functools-lru-cache (from matplotlib&gt;=1.3.1-&gt;scikit-image)
  Using cached backports.functools_lru_cache-1.5-py2.py3-none-any.whl
Requirement already up-to-date: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,&gt;=2.0.1 in ./lib/Python/lib/python2.7/site-packages (from matplotlib&gt;=1.3.1-&gt;scikit-image)
Collecting numpy&gt;=1.7.1 (from matplotlib&gt;=1.3.1-&gt;scikit-image)
  Using cached numpy-1.14.1-cp27-cp27m-manylinux1_x86_64.whl
Collecting kiwisolver&gt;=1.0.1 (from matplotlib&gt;=1.3.1-&gt;scikit-image)
  Using cached kiwisolver-1.0.1-cp27-cp27m-manylinux1_x86_64.whl
Collecting decorator&gt;=4.1.0 (from networkx&gt;=1.8-&gt;scikit-image)
  Using cached decorator-4.2.1-py2.py3-none-any.whl
Collecting setuptools (from kiwisolver&gt;=1.0.1-&gt;matplotlib&gt;=1.3.1-&gt;scikit-image)
  Using cached setuptools-38.5.2-py2.py3-none-any.whl
Building wheels for collected packages: networkx, subprocess32
  Running setup.py bdist_wheel for networkx: started
  Running setup.py bdist_wheel for networkx: finished with status 'error'
  Complete output from command "/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-eE_lIS/networkx/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpbIzR__pip-wheel- --python-tag cp27:
  usage:  [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or:  --help [cmd1 cmd2 ...]
     or:  --help-commands
     or:  cmd --help
  
  error: option -u not recognized
  
  ----------------------------------------
  Failed building wheel for networkx
  Running setup.py clean for networkx
  Complete output from command "/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-eE_lIS/networkx/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" clean --all:
  usage:  [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or:  --help [cmd1 cmd2 ...]
     or:  --help-commands
     or:  cmd --help
  
  error: option -u not recognized
  
  ----------------------------------------
  Failed cleaning build dir for networkx
  Running setup.py bdist_wheel for subprocess32: started
  Running setup.py bdist_wheel for subprocess32: finished with status 'error'
  Complete output from command "/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-eE_lIS/subprocess32/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpYZu52jpip-wheel- --python-tag cp27:
  usage:  [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or:  --help [cmd1 cmd2 ...]
     or:  --help-commands
     or:  cmd --help
  
  error: option -u not recognized
  
  ----------------------------------------
  Failed building wheel for subprocess32
  Running setup.py clean for subprocess32
  Complete output from command "/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-eE_lIS/subprocess32/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" clean --all:
  usage:  [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or:  --help [cmd1 cmd2 ...]
     or:  --help-commands
     or:  cmd --help
  
  error: option -u not recognized
  
  ----------------------------------------
  Failed cleaning build dir for subprocess32
Failed to build networkx subprocess32
Installing collected packages: subprocess32, pytz, backports.functools-lru-cache, numpy, setuptools, kiwisolver, matplotlib, decorator, networkx, pillow, PyWavelets, scikit-image
  Running setup.py install for subprocess32: started
    Running setup.py install for subprocess32: finished with status 'error'
    Complete output from command "/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-eE_lIS/subprocess32/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-f8oqVV-record/install-record.txt --single-version-externally-managed --compile:
    usage:  [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
       or:  --help [cmd1 cmd2 ...]
       or:  --help-commands
       or:  cmd --help
    
    error: option -u not recognized
    
    ----------------------------------------
Command ""/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-eE_lIS/subprocess32/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-f8oqVV-record/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /tmp/pip-build-eE_lIS/subprocess32/
1
&gt;&gt;&gt; pip.main(['install', 'numpy'])
Requirement already satisfied: numpy in ./lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-linux-x86_64.egg
0
&gt;&gt;&gt; pip.main(['install', 'skimage'])
Collecting skimage
  Downloading skimage-0.0.tar.gz
    Complete output from command python setup.py egg_info:
    
    *** Please install the `scikit-image` package (instead of `skimage`) ***
    
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-PINFjC/skimage/
1
&gt;&gt;&gt; pip.main(['install', 'scikit-image'])
Collecting scikit-image
  Using cached scikit_image-0.13.1-cp27-cp27m-manylinux1_x86_64.whl
Collecting matplotlib&gt;=1.3.1 (from scikit-image)
  Using cached matplotlib-2.2.0-cp27-cp27m-manylinux1_x86_64.whl
Requirement already satisfied: six&gt;=1.7.3 in ./lib/Python/lib/python2.7/site-packages (from scikit-image)
Collecting networkx&gt;=1.8 (from scikit-image)
  Using cached networkx-2.1.zip
Collecting pillow&gt;=2.1.0 (from scikit-image)
  Using cached Pillow-5.0.0-cp27-cp27m-manylinux1_x86_64.whl
Collecting PyWavelets&gt;=0.4.0 (from scikit-image)
  Using cached PyWavelets-0.5.2-cp27-cp27m-manylinux1_x86_64.whl
Requirement already satisfied: scipy&gt;=0.17.0 in ./lib/Python/lib/python2.7/site-packages (from scikit-image)
Requirement already satisfied: python-dateutil&gt;=2.1 in ./lib/Python/lib/python2.7/site-packages (from matplotlib&gt;=1.3.1-&gt;scikit-image)
Requirement already satisfied: cycler&gt;=0.10 in ./lib/Python/lib/python2.7/site-packages (from matplotlib&gt;=1.3.1-&gt;scikit-image)
Collecting subprocess32 (from matplotlib&gt;=1.3.1-&gt;scikit-image)
  Using cached subprocess32-3.2.7.tar.gz
Collecting pytz (from matplotlib&gt;=1.3.1-&gt;scikit-image)
  Using cached pytz-2018.3-py2.py3-none-any.whl
Collecting backports.functools-lru-cache (from matplotlib&gt;=1.3.1-&gt;scikit-image)
  Using cached backports.functools_lru_cache-1.5-py2.py3-none-any.whl
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,&gt;=2.0.1 in ./lib/Python/lib/python2.7/site-packages (from matplotlib&gt;=1.3.1-&gt;scikit-image)
Requirement already satisfied: numpy&gt;=1.7.1 in ./lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-linux-x86_64.egg (from matplotlib&gt;=1.3.1-&gt;scikit-image)
Collecting kiwisolver&gt;=1.0.1 (from matplotlib&gt;=1.3.1-&gt;scikit-image)
  Using cached kiwisolver-1.0.1-cp27-cp27m-manylinux1_x86_64.whl
Collecting decorator&gt;=4.1.0 (from networkx&gt;=1.8-&gt;scikit-image)
  Using cached decorator-4.2.1-py2.py3-none-any.whl
Requirement already satisfied: setuptools in ./lib/Python/lib/python2.7/site-packages/setuptools-36.6.0.post20171220-py2.7.egg (from kiwisolver&gt;=1.0.1-&gt;matplotlib&gt;=1.3.1-&gt;scikit-image)
Building wheels for collected packages: networkx, subprocess32
  Running setup.py bdist_wheel for networkx: started
  Running setup.py bdist_wheel for networkx: finished with status 'error'
  Complete output from command "/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-yeDhnL/networkx/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpon3uEHpip-wheel- --python-tag cp27:
  usage:  [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or:  --help [cmd1 cmd2 ...]
     or:  --help-commands
     or:  cmd --help
  
  error: option -u not recognized
  
  ----------------------------------------
  Failed building wheel for networkx
  Running setup.py clean for networkx
  Complete output from command "/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-yeDhnL/networkx/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" clean --all:
  usage:  [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or:  --help [cmd1 cmd2 ...]
     or:  --help-commands
     or:  cmd --help
  
  error: option -u not recognized
  
  ----------------------------------------
  Failed cleaning build dir for networkx
  Running setup.py bdist_wheel for subprocess32: started
  Running setup.py bdist_wheel for subprocess32: finished with status 'error'
  Complete output from command "/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-yeDhnL/subprocess32/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpfOfMjBpip-wheel- --python-tag cp27:
  usage:  [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or:  --help [cmd1 cmd2 ...]
     or:  --help-commands
     or:  cmd --help
  
  error: option -u not recognized
  
  ----------------------------------------
  Failed building wheel for subprocess32
  Running setup.py clean for subprocess32
  Complete output from command "/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-yeDhnL/subprocess32/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" clean --all:
  usage:  [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or:  --help [cmd1 cmd2 ...]
     or:  --help-commands
     or:  cmd --help
  
  error: option -u not recognized
  
  ----------------------------------------
  Failed cleaning build dir for subprocess32
Failed to build networkx subprocess32
Installing collected packages: subprocess32, pytz, backports.functools-lru-cache, kiwisolver, matplotlib, decorator, networkx, pillow, PyWavelets, scikit-image
  Running setup.py install for subprocess32: started
    Running setup.py install for subprocess32: finished with status 'error'
    Complete output from command "/home/carrie/Workspace/3D Slicer/Slicer-4.8.1-linux-amd64/bin/SlicerApp-real" -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-yeDhnL/subprocess32/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-Kt5oiI-record/install-record.txt --single-version-externally-managed --compile:
    usage:  [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
       or:  --help [cmd1 cmd2 ...]
       or:  --help-commands
       or:  cmd --help
    
    error: option -u not recognized
</code></pre>

---

## Post #2 by @jcfr (2018-03-07 00:17 UTC)

<p>When there are issues using Slicer application as the <em>python interpreter</em>, I suggest to fallback to using a the plain python interpreter also bundled in the Slicer package.</p>
<p>The following could be done:</p>
<h3>Step 1</h3>
<p>Open a terminal</p>
<h3>Step 2</h3>
<p>Source the Slicer environment</p>
<pre><code class="lang-auto">$ eval $(./Slicer  --launcher-show-set-environment-commands)
</code></pre>
<h3>Step 3</h3>
<p>Install the package</p>
<p><em>Note that the name of the interpreter bundled with Slicer is <code>python-real</code> and not <code>python</code></em></p>
<pre><code class="lang-auto">$ python-real -m "pip" install scikit-image
Collecting scikit-image
  Downloading scikit_image-0.13.1-cp27-cp27m-manylinux1_x86_64.whl (35.2MB)
  ...
Collecting matplotlib&gt;=1.3.1 (from scikit-image)
  Downloading matplotlib-2.2.0-cp27-cp27m-manylinux1_x86_64.whl (12.5MB)
  ....
Collecting networkx&gt;=1.8 (from scikit-image)
  Downloading networkx-2.1.zip (1.6MB)

[...]

Building wheels for collected packages: networkx, subprocess32

[...]
Running setup.py bdist_wheel for subprocess32 ... error
  Complete output from command /home/jcfr/Downloads/Slicer-4.8.1-linux-amd64/bin/python-real -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-vTIc2o/subprocess32/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpKY4kdZpip-wheel- --python-tag cp27:
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.linux-x86_64-2.7
  copying subprocess32.py -&gt; build/lib.linux-x86_64-2.7
  running build_ext
  building '_posixsubprocess' extension
  creating build/temp.linux-x86_64-2.7
  /usr/bin/gcc-4.6 -pthread -Wall -Wstrict-prototypes -fno-strict-aliasing -fwrapv -g -fPIC -I/home/jcfr/Downloads/Slicer-4.8.1-linux-amd64/lib/Python/include/python2.7 -c _posixsubprocess.c -o build/temp.linux-x86_64-2.7/_posixsubprocess.o
  unable to execute '/usr/bin/gcc-4.6': No such file or directory
  error: command '/usr/bin/gcc-4.6' failed with exit status 1
  
  ----------------------------------------
  Failed building wheel for subprocess32
  Running setup.py clean for subprocess32

[...]
</code></pre>
<h3>issue</h3>
<p>While there are python 2.7 wheels for most of the dependencies (scikit_image itself, matplotlib, etc …), there are no per-built binaries for <code>subprocess32</code> for linux for python 2.7. See <a href="https://pypi.python.org/pypi/subprocess32/3.5.0rc1">https://pypi.python.org/pypi/subprocess32/3.5.0rc1</a> and <a href="https://pypi.python.org/pypi/subprocess32/3.2.7">https://pypi.python.org/pypi/subprocess32/3.2.7</a></p>
<p>On linux, the expectation is that user of the package is expected to build from source.</p>
<p>Few approaches:</p>
<ul>
<li>
<p>Fix the build system of <a href="https://github.com/google/python-subprocess32">https://github.com/google/python-subprocess32</a> so that they use <a href="http://scikit-build.readthedocs.io/en/latest/">scikit-build</a> to compile their code and generate while for python 2.7.</p>
<ul>
<li>I can provide guidance, this should be only few lines and the use of the <a href="https://github.com/dockcross/dockcross#cross-compilers">dockcross/manylinux-x64</a> docker image to have package working on a broad set of linux distribution.</li>
<li>Once a wheel is generated locally, you could install it first and then install scikit-image.</li>
</ul>
</li>
<li>
<p>Use ITK python. Running <code>pip install itk</code> is expected to work. See <a href="http://itkpythonpackage.readthedocs.io/en/latest/">http://itkpythonpackage.readthedocs.io/en/latest/</a></p>
</li>
</ul>

---
