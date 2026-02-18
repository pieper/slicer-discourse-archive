# Installing FEniCS Python package inside Slicer

**Topic ID**: 12322
**Date**: 2020-07-01
**URL**: https://discourse.slicer.org/t/installing-fenics-python-package-inside-slicer/12322

---

## Post #1 by @benzwick (2020-07-01 14:13 UTC)

<p>Hi,</p>
<p>I need some help with installing the <code>fenics</code> Python package inside Slicer. I tried using <code>pip_install('fenics')</code> in the latest Slicer preview (4.11.0-2020-06-30 r29196 / 07bc921):</p>
<pre><code>Python 3.6.7 (default, Jul  1 2020, 03:07:22) 
[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux2
&gt;&gt;&gt; pip_install('fenics')
Collecting fenics
  Using cached fenics-2019.1.0-py3-none-any.whl (1.5 kB)
Collecting fenics-ffc&lt;2019.2,&gt;=2019.1.0
  Using cached fenics_ffc-2019.1.0.post0-py3-none-any.whl (362 kB)
Collecting fenics-dijitso&lt;2019.2,&gt;=2019.1.0
  Using cached fenics_dijitso-2019.1.0-py3-none-any.whl (46 kB)
Collecting fenics-ufl&lt;2019.2,&gt;=2019.1.0
  Using cached fenics_ufl-2019.1.0-py3-none-any.whl (282 kB)
Collecting fenics-fiat&lt;2019.2,&gt;=2019.1.0
  Using cached fenics_fiat-2019.1.0-py3-none-any.whl (112 kB)
Requirement already satisfied: numpy in ./Slicer-4.11.0-2020-06-30-linux-amd64/lib/Python/lib/python3.6/site-packages (from fenics-ffc&lt;2019.2,&gt;=2019.1.0-&gt;fenics) (1.18.1)
Collecting sympy
  Using cached sympy-1.6-py3-none-any.whl (5.8 MB)
Processing /home/ben/.cache/pip/wheels/63/9d/8e/37c3f6506ed3f152733a699e92d8e0c9f5e5f01dea262f80ad/mpmath-1.1.0-cp36-none-any.whl
Installing collected packages: fenics-dijitso, fenics-ufl, mpmath, sympy, fenics-fiat, fenics-ffc, fenics
  WARNING: The script dijitso is installed in '/opt/slicer/Slicer-4.11.0-2020-06-30-linux-amd64/lib/Python/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script isympy is installed in '/opt/slicer/Slicer-4.11.0-2020-06-30-linux-amd64/lib/Python/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts ffc and ffc-3 are installed in '/opt/slicer/Slicer-4.11.0-2020-06-30-linux-amd64/lib/Python/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed fenics-2019.1.0 fenics-dijitso-2019.1.0 fenics-ffc-2019.1.0.post0 fenics-fiat-2019.1.0 fenics-ufl-2019.1.0 mpmath-1.1.0 sympy-1.6
WARNING: You are using pip version 20.1; however, version 20.1.1 is available.
You should consider upgrading via the '/opt/slicer/Slicer-4.11.0-2020-06-30-linux-amd64/bin/./python-real -m pip install --upgrade pip' command.
&gt;&gt;&gt; import dolfin
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
ModuleNotFoundError: No module named 'dolfin'
&gt;&gt;&gt; import fenics
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
ModuleNotFoundError: No module named 'fenics'
&gt;&gt;&gt; import ffc
&gt;&gt;&gt; import dijitso
</code></pre>
<p>It appears that the installation is successful, but I cannot import the <code>fenics</code> or <code>dolfin</code> modules (although the related <code>ffc</code> and <code>dijitso</code> modules can be loaded).</p>
<p>I am using Ubuntu 18.04 and have FEniCS installed using PPA. In other words the non-Python components are available on my system path.</p>

---

## Post #2 by @lassoan (2020-07-01 14:49 UTC)

<p>Slicer FEniCS extension should help: <a href="https://discourse.slicer.org/t/slicer-fenics-extension/7407" class="inline-onebox">Slicer FEniCS extension</a></p>
<p>Let us know if you find it useful, we would then consider making it available directly in the Extension manager.</p>

---

## Post #3 by @lassoan (2020-07-01 14:53 UTC)

<p>I’ve just realized that you are the person who develops Slicer FEniCS extension…</p>

---

## Post #4 by @lassoan (2020-07-01 15:00 UTC)

<p>If you have a <code>fenics</code> folder in your <code>lib/Python/Lib</code> folder and it has a <code>__init__.py</code> file then the module should be found. You can edit the init file or other Python files to add logs to figure out where things break down.</p>

---

## Post #5 by @benzwick (2020-07-01 15:01 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, that is the extension that I developed <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> I am trying to extend it for a different problem and also to simplify the installation. I have lost my previous development environment and it was quite difficult to install back then. I was hoping there may be a better way to install the Python modules. Last time I did it like this:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://projectweek.na-mic.org/PW31_2019_Boston/Projects/SlicerFEniCS/slicer-fenics-install.html" target="_blank" rel="nofollow noopener">ProjectWeek</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="20" height="20">

<h3><a href="https://projectweek.na-mic.org/PW31_2019_Boston/Projects/SlicerFEniCS/slicer-fenics-install.html" target="_blank" rel="nofollow noopener">Slicer FEniCS Installation</a></h3>

<p>Website for NA-MIC Project Weeks</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>However, I have now installed FEniCS binaries instead of from source. I would like to just install the Python modules inside Slicer so I can import <code>fenics</code> or <code>dolfin</code> inside my extension module.</p>
<p>Here is the <code>fenics</code> package on pypi:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.6a76275d.ico" class="site-icon" width="16" height="16">
      <a href="https://pypi.org/project/fenics/" target="_blank" rel="nofollow noopener">PyPI</a>
  </header>
  <article class="onebox-body">
    <img src="https://pypi.org/static/images/twitter.90915068.jpg" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://pypi.org/project/fenics/" target="_blank" rel="nofollow noopener">fenics</a></h3>

<p>The FEniCS Project Python Metapackage</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @benzwick (2020-07-01 15:11 UTC)

<p>I had a look and this is what I have in <code>/opt/slicer/Slicer-4.11.0-2020-06-30-linux-amd64/lib/Python/lib/python3.6/site-packages/</code>:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90e6106756090ddedec2db5af96b51e24cba3b9e.png" alt="image" data-base62-sha1="kFPFhagNTRGFYZwkxUimPTDyYH4" width="325" height="241"></p>
<p>This is all the other files I could find:</p>
<pre><code class="lang-auto">$ pwd
/opt/slicer/Slicer-4.11.0-2020-06-30-linux-amd64
$ find . -iname fenics*
./lib/Python/lib/python3.6/site-packages/fenics_dijitso-2019.1.0.dist-info
./lib/Python/lib/python3.6/site-packages/fenics_ufl-2019.1.0.dist-info
./lib/Python/lib/python3.6/site-packages/fenics_fiat-2019.1.0.dist-info
./lib/Python/lib/python3.6/site-packages/fenics_ffc-2019.1.0.post0.dist-info
./lib/Python/lib/python3.6/site-packages/fenics-2019.1.0.dist-info
$ find . -iname dolfin*
./lib/Python/lib/python3.6/site-packages/ffc/backends/dolfin
</code></pre>
<p>This is where the system installed dolfin module is:</p>
<pre><code class="lang-auto">In [1]: import dolfin

In [2]: dolfin.__file__
Out[2]: '/usr/lib/python3/dist-packages/dolfin/__init__.py'

In [3]: 
</code></pre>
<p>So the one in Slicer should have a similar name I guess but with a different path.</p>

---

## Post #7 by @lassoan (2020-07-01 15:28 UTC)

<p>This seems to be a common issue and troubleshooting tips are available here: <a href="https://stackoverflow.com/questions/50585246/pip-install-creates-only-the-dist-info-not-the-package">https://stackoverflow.com/questions/50585246/pip-install-creates-only-the-dist-info-not-the-package</a></p>

---

## Post #8 by @benzwick (2020-07-01 15:42 UTC)

<p>Thanks, I will try that. What is the best/recommended way to run pip to install/uninstall packages in Slicer? I have looked on the forum, wiki, documentation and there appear to be a few different ways to run pip. Do you have a link to the most up to date documentation for this?<br>
Currently I am using this: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_run_pip_.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_run_pip_.3F</a></p>

---

## Post #9 by @benzwick (2020-07-01 16:19 UTC)

<p>I tried troubleshooting. I realised that the DOLFIN Python component needs to be built separately to link with the DOLFIN C++ libraries.</p>
<p>I got it working now using a “hybrid” approach:</p>
<ol>
<li>
<p>Install FEniCS 2019.1.0 using Ubuntu PPA<br>
(see: <a href="https://fenics.readthedocs.io/en/latest/installation.html#ubuntu-ppa" rel="nofollow noopener">https://fenics.readthedocs.io/en/latest/installation.html#ubuntu-ppa</a>)</p>
</li>
<li>
<p>Install <code>fenics</code> Python-only components in Slicer using <code>pip</code>:</p>
<pre><code> {MY_SLICER_DIR}/bin/PythonSlicer -m pip install fenics
</code></pre>
</li>
<li>
<p>Download and install Python header files in Slicer:</p>
<pre><code> wget -P ${MY_SLICER_DIR}/lib/Python/include/python3.6m/ https://github.com/python/cpython/archive/v3.6.7.tar.gz
 cd ${MY_SLICER_DIR}/lib/Python/include/python3.6m/
 tar --strip-components=2 -zxf v3.6.7.tar.gz cpython-3.6.7/Include
</code></pre>
</li>
<li>
<p>Install Python interface of DOLFIN:</p>
<pre><code> ${MY_SLICER_DIR}/bin/PythonSlicer -m pip install ${MY_FENICS_SRC}/dolfin/python
</code></pre>
</li>
</ol>
<p>Step 3 was suggested by <a class="mention" href="/u/jcfr">@jcfr</a> when I was developing Slicer FEniCS in Boston. Maybe it would be worthwhile to include these headers within the Slicer distribution. It is the only complicated step in the installation process here.</p>

---

## Post #10 by @benzwick (2020-07-09 16:33 UTC)

<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/2637" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/2637" target="_blank" rel="nofollow noopener">Include all Python header files with nightly binary build</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="23:48:55" data-timezone="UTC">11:48PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-20" data-time="15:37:25" data-timezone="UTC">03:37PM - 20 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="nofollow noopener">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #11 by @Saima (2021-02-10 08:42 UTC)

<p>Hi Andras,<br>
I have fenics in the 3d slicer. when I use interpreter I can import the fenics<br>
but how can i import from within a module it says</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/home/saima/Downloads/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 674, in exec_module<br>
File “”, line 781, in get_code<br>
File “”, line 741, in source_to_code<br>
File “”, line 219, in _call_with_frames_removed<br>
File “/home/saima/Downloads/Slicer-4.11.20200930-linux-amd64/VoxelizeMesh/crwateMesh/crwateMesh.py”, line 317<br>
def process(self, inputVolume, outputVolume, imageThreshold, invert=False, showResult=True):<br>
^<br>
SyntaxError: import * only allowed at module level</p>
<p>from fenics import * is not allowed how can I fix it?</p>
<p>thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #12 by @benzwick (2021-02-10 11:28 UTC)

<p>You can have a look in this file to see how to use FEniCS DOLFIN inside a 3D Slicer module:</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/benzwick/slicer-fenics/blob/master/FEniCS_demo/FEniCS_demo_module/FEniCS_demo_module.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/benzwick/slicer-fenics/blob/master/FEniCS_demo/FEniCS_demo_module/FEniCS_demo_module.py" target="_blank" rel="noopener nofollow ugc">benzwick/slicer-fenics/blob/master/FEniCS_demo/FEniCS_demo_module/FEniCS_demo_module.py</a></h4>
<pre><code class="lang-py">import vtk
import qt
import ctk
import slicer
from slicer.ScriptedLoadableModule import (
    ScriptedLoadableModule,
    ScriptedLoadableModuleLogic,
    ScriptedLoadableModuleTest,
    ScriptedLoadableModuleWidget,
)
import logging

import dolfin


#
# FEniCS_demo_module
#
class FEniCS_demo_module(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
</code></pre>

  This file has been truncated. <a href="https://github.com/benzwick/slicer-fenics/blob/master/FEniCS_demo/FEniCS_demo_module/FEniCS_demo_module.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
