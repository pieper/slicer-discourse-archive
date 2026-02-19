---
topic_id: 984
title: "Slicer Python Packages Use And Install"
date: 2017-08-31
url: https://discourse.slicer.org/t/984
---

# Slicer-Python Packages Use and Install

**Topic ID**: 984
**Date**: 2017-08-31
**URL**: https://discourse.slicer.org/t/slicer-python-packages-use-and-install/984

---

## Post #1 by @ssyip (2017-08-31 21:27 UTC)

<p>Hi,</p>
<p>There are python packages (e.g. scipy) that I would like to use but not installed under<br>
"Slicer 4.6.2\lib\Python\Lib\site-packages".</p>
<ol>
<li>
<p>If I already have Python 2.7 and all packages I want installed on my computer, can I add path in Slicer so it knows where to find those packages?</p>
</li>
<li>
<p>I tried to copy and paste all the installed packages into the “Slicer 4.6.2\lib\Python\Lib\site-packages” folder, but Slicer ended up not running at all.</p>
</li>
<li>
<p>Does anyone know how to install packages through the python interactor? I tried to install pip, but keep getting errors.</p>
</li>
</ol>
<p>Thanks,<br>
Stephen</p>

---

## Post #2 by @jcfr (2017-08-31 21:46 UTC)

<aside class="quote no-group" data-username="ssyip" data-post="1" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3d9bf3/48.png" class="avatar"> ssyip:</div>
<blockquote>
<ol>
<li>
<p>If I already have Python 2.7 and all packages I want installed on my computer, can I add path in Slicer so it knows where to find those packages?</p>
</li>
<li>
<p>I tried to copy and paste all the installed packages into the “Slicer 4.6.2\lib\Python\Lib\site-packages” folder, but Slicer ended up not running at all.</p>
</li>
</ol>
</blockquote>
</aside>
<p>Since Slicer bundles its own <em>python</em>, it is generally <strong>NOT</strong> possible to simply copy python packages (especially the one including binaries) from your own <code>site-packages</code> into the one of Slicer.</p>
<p>That said, depending on the platform  there is way around it.</p>
<p>First, I suggest you download the latest nightly build of Slicer.</p>
<p>There are a lot of improvement regarding the python infrastructure. It for example includes an updated <code>setuptools</code> as well as <code>pip</code>.</p>
<p>Second, on linux (and most likely macOS), it is indeed <strong>possible to pip install official packages</strong> (even the including binaries like <code>scipy</code>, <code>tensorflow</code>, …).</p>
<p>On windows, it will currently work only for <em>pure</em> python wheels because the official package for python 2.7 are built with a compiler than the one used for the official wheels. Note that this will change as soon as we standardize on Visual Studio 2015 and switch to python &gt;= 3.5.</p>
<aside class="quote no-group" data-username="ssyip" data-post="1" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3d9bf3/48.png" class="avatar"> ssyip:</div>
<blockquote>
<ol start="3">
<li>Does anyone know how to install packages through the python interactor? I tried to install pip, but keep getting errors.</li>
</ol>
</blockquote>
</aside>
<p>As mentioned above, the good news is that <code>pip</code> is available in Slicer.</p>
<h4><a name="p-4054-build-tree-1" class="anchor" href="#p-4054-build-tree-1" aria-label="Heading link"></a>build tree</h4>
<p>From a build tree, you can do:</p>
<pre data-code-wrap="bash"><code class="lang-bash">./Slicer --launch ../python-install/bin/pip install scipy
</code></pre>
<p>or something like this on windows (only for pure python wheels)</p>
<pre data-code-wrap="bash"><code class="lang-bash">Slicer.exe --launch ..\python-install\bin\pip.exe install name-of-pure-python-wheel
</code></pre>
<h4><a name="p-4054-install-tree-or-python-interactor-2" class="anchor" href="#p-4054-install-tree-or-python-interactor-2" aria-label="Heading link"></a>install tree or python interactor</h4>
<p>Since we do not (yet) package the <code>pip</code> executable, you will have to use a different approach.</p>
<h5><a name="p-4054-from-the-terminal-3" class="anchor" href="#p-4054-from-the-terminal-3" aria-label="Heading link"></a>from the terminal</h5>
<pre data-code-wrap="bash"><code class="lang-bash">./Slicer --launch ./bin/python-real -c "import pip; pip.main(['install', 'scipy'])"
</code></pre>
<p>or something like this on windows</p>
<pre data-code-wrap="bash"><code class="lang-bash">Slicer.exe --launch bin\python-real.exe -c "import pip; pip.main(['install', 'scipy'])"
</code></pre>
<h5><a name="p-4054-from-python-interactor-4" class="anchor" href="#p-4054-from-python-interactor-4" aria-label="Heading link"></a>from python interactor</h5>
<pre data-code-wrap="python"><code class="lang-python">import pip
pip.main(['install', 'scipy'])
</code></pre>

---

## Post #4 by @ssyip (2017-09-01 16:13 UTC)

<p>Hi,</p>
<p>I downloaded and installed the 3D-Slicer nightly built on a window 64bit machine.</p>
<p>I tried to install the scipy whl using pip, but got a window error [Error 5] Access in denied: …Slicer 4.7.0\Lib\Python\Lib\site-packages\scipy</p>
<p>I also tried pip.main([‘install’,‘scipy’]), but got a failed building wheel for scipy feedback.<br>
Downloading the scipy wheel, then install doesn’t work either.</p>
<p>Does anyone know how to fix that?</p>
<p>Please also see attached</p>
<p>Thanks,<br>
Stephen</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/897958c561d0fb9ffd5b892c4ea5c0c33e67ef3a.JPG" data-download-href="/uploads/short-url/jC9oEIA9ktvXoe9MC93MGrb9CS6.JPG?dl=1" title="image1.JPG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/897958c561d0fb9ffd5b892c4ea5c0c33e67ef3a_2_666x500.JPG" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/897958c561d0fb9ffd5b892c4ea5c0c33e67ef3a_2_666x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/897958c561d0fb9ffd5b892c4ea5c0c33e67ef3a_2_999x750.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/897958c561d0fb9ffd5b892c4ea5c0c33e67ef3a_2_1332x1000.JPG 2x" data-dominant-color="757672"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image1.JPG</span><span class="informations">2851×2138 2.41 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @jcfr (2017-09-01 16:21 UTC)

<aside class="quote no-group quote-post-not-found" data-username="ssyip" data-post="3" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3d9bf3/48.png" class="avatar"> ssyip:</div>
<blockquote>
<p>I tried to install the scipy whl using pip, but got a window error [Error 5] Access in denied: …Slicer 4.7.0\Lib\Python\Lib\site-packages\scipy</p>
<p>Does anyone know how to fix that?</p>
</blockquote>
</aside>
<ol>
<li>
<p>Even if we manage to install the wheel, there is a chance it doesn’t work at all. Scipy is a binary wheel, it includes compiled code.</p>
</li>
<li>
<p>That said, since running pip install attempt to update packages located in <code>C:\Program Files\Slicer ...</code>, try to run Slicer as administrator.</p>
</li>
</ol>

---

## Post #6 by @ssyip (2017-09-01 16:38 UTC)

<p>I am sorry. How do I run Slicer as an administrator? Thanks!</p>

---

## Post #7 by @ssyip (2017-09-01 16:42 UTC)

<p>I tried this<br>
Slicer.exe --launch …\python-install\bin\pip.exe install name-of-pure-python-wheel<br>
Seems like Slicer started to load, but then nothing happened.<br>
Also, is the python-install/bin folder supposed to be inside the Slicer directory? I am not able to find it nor the pip.exe<br>
Thanks so much!<br>
Stephen</p>

---

## Post #8 by @jcfr (2017-09-01 17:00 UTC)

<p>To run as admin, you need to do right click -&gt; run as admin</p>
<p>Other since you installed Slicer, there is no pip exe.</p>

---

## Post #9 by @lassoan (2017-09-01 22:49 UTC)

<p>I’ve tried this on the latest nightly version and it all works well for me!</p>
<ol>
<li>
<p>Start Slicer as administrator: in the start menu, instead of left-click on the Slicer icon, use right-click, then select <code>More...</code> and <code>Run as Administrator</code>.</p>
</li>
<li>
<p>Install a package by using <code>pip</code>. For example, installing of <code>requests</code> package:</p>
</li>
</ol>
<p>Enter this into the Python interactor:</p>
<pre><code>import pip
pip.main(['install', 'requests'])
</code></pre>
<p>The package is successfully downloaded and installed:</p>
<pre><code>Collecting requests
  Downloading requests-2.18.4-py2.py3-none-any.whl (88kB)
Collecting idna&lt;2.7,&gt;=2.5 (from requests)
  Downloading idna-2.6-py2.py3-none-any.whl (56kB)
Collecting urllib3&lt;1.23,&gt;=1.21.1 (from requests)
  Downloading urllib3-1.22-py2.py3-none-any.whl (132kB)
Collecting certifi&gt;=2017.4.17 (from requests)
  Downloading certifi-2017.7.27.1-py2.py3-none-any.whl (349kB)
Collecting chardet&lt;3.1.0,&gt;=3.0.2 (from requests)
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133kB)
Installing collected packages: idna, urllib3, certifi, chardet, requests
  Found existing installation: chardet 2.3.0
    Uninstalling chardet-2.3.0:
      Successfully uninstalled chardet-2.3.0
Successfully installed certifi-2017.7.27.1 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22
0
</code></pre>
<p>Dependent packages are updated, therefore before using the installed <code>requests</code> package, you need to restart Slicer (you can use the <code>restart()</code> command in the Python console).</p>

---

## Post #10 by @jcfr (2017-09-01 23:05 UTC)

<p>Exactly. For pure python packages, that will work great.</p>

---

## Post #12 by @ssyip (2017-09-05 18:22 UTC)

<p>Hi,</p>
<p>Thank you very much for all the help!</p>
<p>While the installation worked well for some packages (e.g. PIL and matplotlib wheels), it still doesn’t work for “scipy”, “sckimage”, etc. Does anyone know what happened? Thank you!</p>
<ul>
<li>I did uninstall numpy and installed numpy+mkl since scipy complained numpy didn’t have mkl.</li>
</ul>
<p>In particular, I get the following error,</p>
<pre><code class="lang-auto">path=r"C:\Program Files\Slicer 4.7.0-2017-09-05\packages\scipy-0.19.1-cp27-cp27m-win_amd64.whl"
&gt;&gt;&gt; pip.main(['install',path])
Processing c:\program files\slicer 4.7.0-2017-09-05\packages\scipy-0.19.1-cp27-cp27m-win_amd64.whl
Requirement already satisfied: numpy&gt;=1.8.2 in c:\program files\slicer 4.7.0-2017-09-05\lib\python\lib\site-packages\numpy-1.13.1-py2.7-win-amd64.egg (from scipy==0.19.1)
Exception:
Traceback (most recent call last):
File "C:\Program Files\Slicer 4.7.0-2017-09-05\lib\Python\Lib\site-packages\pip\basecommand_.py", line 215, in main
status = self.run(options, args)
File "C:\Program Files\Slicer 4.7.0-2017-09-05\lib\Python\Lib\site-packages\pip\commands\install_.py", line 335, in run
wb.build(autobuilding=True)
File "C:\Program Files\Slicer 4.7.0-2017-09-05\lib\Python\Lib\site-packages\pip\wheel_.py", line 749, in build
self.requirement_set.prepare_files(self.finder)
File "C:\Program Files\Slicer 4.7.0-2017-09-05\lib\Python\Lib\site-packages\pip\req\req_set.py", line 380, in prepare_files
ignore_dependencies=self.ignore_dependencies))
File "C:\Program Files\Slicer 4.7.0-2017-09-05\lib\Python\Lib\site-packages\pip\req\req_set.py", line 666, in _prepare_file
check_dist_requires_python(dist)
File "C:\Program Files\Slicer 4.7.0-2017-09-05\lib\Python\Lib\site-packages\pip\utils\packaging_.py", line 48, in check_dist_requires_python
feed_parser.feed(metadata)
File "C:\Program Files\Slicer 4.7.0-2017-09-05\lib\Python\Lib\email\feedparser_.py", line 177, in feed
self._input.push(data)
File "C:\Program Files\Slicer 4.7.0-2017-09-05\lib\Python\Lib\email\feedparser_.py", line 99, in push
parts = data.splitlines(True)
AttributeError: 'NoneType' object has no attribute 'splitlines'
</code></pre>

---

## Post #13 by @codey (2017-09-26 23:38 UTC)

<p>I am trying to install scikit-image with</p>
<p>./Slicer --launch ./bin/python-real -c “import pip; pip.main([‘install’, ‘scikit-image’])”</p>
<p>In the install tree I get the error</p>
<pre><code>/usr/bin/gcc-4.6 -pthread -Wall -Wstrict-prototypes -fno-strict-aliasing -fwrapv -g -fPIC -I/Data-work/BuildDirs/Slicer-4.7.0-2017-09-24-linux-amd64/lib/Python/include/python2.7 -c _posixsubprocess.c -o build/temp.linux-x86_64-2.7/_posixsubprocess.o
_posixsubprocess.c:3:20: fatal error: Python.h: No such file or directory
compilation terminated.
error: command '/usr/bin/gcc-4.6' failed with exit status 1</code></pre>

---

## Post #14 by @lassoan (2017-09-27 00:29 UTC)

<p>Slicer’s pip does not yet support packages that need compilation. To get access to all Python packages, you have to build Slicer with your Python distribution. See some information here: <a href="https://www.slicer.org/wiki/Documentation/Labs/SlicerCondaIntegration">https://www.slicer.org/wiki/Documentation/Labs/SlicerCondaIntegration</a></p>

---

## Post #15 by @mcfly3001 (2018-07-12 09:52 UTC)

<p>Hi all,</p>
<p>a quick questions concerning this topic. I am developing with Slicer on Windows and was also trying to install a module with precompiled data, namely pywin32. After some try and error I figured out that pywin32 also uses precompiled data. Since Slicers Python is build with VS2013 but the module has precompiled with VS2008 I assume the runtimes collide here.<br>
My plan was now to build Slicer on my own such that I also have a Python.exe build with VS2013. Afterwards I would go to pywin32 gitlab page and build the module manually as well. Building pywin32 requires the Python.exe file, thats why I need to build Slicer as well.</p>
<p>Could this work?</p>
<p>Thanks!</p>

---

## Post #16 by @lassoan (2018-07-12 12:47 UTC)

<p>If you build Slicer according to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">build instructions</a> and you build the Python package using the same compiler and compiler settings then it should all work. If you need a Python.exe, you can use Slicer’s SlicerPython.exe.</p>
<p>Note that Slicer includes Qt library, which provides access to lots of Windows APIs (and Linux and macOS APIs), so you might be able to do without pywin32.</p>

---

## Post #17 by @mcfly3001 (2018-07-12 12:58 UTC)

<p>Thanks! I think you are right and I should use the Qt library. Haven’t thought about this. Anyways it’s good to know that it should work like this.</p>

---

## Post #18 by @ihnorton (2018-07-12 15:41 UTC)

<p>If the API is not available in Qt, or you need code to work outside the Slicer environment too, then you could also try <a href="http://pywincffi.readthedocs.io/en/0.4.0/">pywincffi</a>. That uses the CFFI module, which can construct calls at runtime via ctypes/libffi (in CPython), and avoid the need for dealing with compiled shim libraries.</p>

---

## Post #19 by @Saima (2018-09-05 09:29 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>stall tree or python interactor</p>
</blockquote>
</aside>
<p>WHy pip.main not working for me. I run as administrator even then its not working for me<br>
Python 2.7.13 (default, Aug 31 2018, 23:24:30) [MSC v.1900 64 bit (AMD64)] on win32<br>
AttributeError: ‘module’ object has no attribute ‘main’</p>

---

## Post #20 by @jamesobutler (2018-09-05 12:15 UTC)

<p>Details can be found <a href="https://discourse.slicer.org/t/pip-in-nightly-build-not-working/3325/5">Pip in nightly build not working</a></p>

---

## Post #21 by @Saima (2018-09-06 03:23 UTC)

<aside class="quote no-group" data-username="ssyip" data-post="12" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3d9bf3/48.png" class="avatar"> ssyip:</div>
<blockquote>
<p>ell for some packages (e.g. PIL and matplotlib wheel</p>
</blockquote>
</aside>
<p>how did you install matplotlib and other packages you mentioned.<br>
For me scipy is installed like this.<br>
from pip._internal import main as pipmain<br>
pipmain([‘install’,‘scipy’])</p>
<p>Collecting scipy</p>
<p>Downloading <a href="https://files.pythonhosted.org/packages/d2/a7/0d698589a3c6c44f81078a52518c8e64c4ed579a862105b2bff5a1f14ff4/scipy-1.1.0-cp27-none-win_amd64.whl" rel="noopener nofollow ugc">https://files.pythonhosted.org/packages/d2/a7/0d698589a3c6c44f81078a52518c8e64c4ed579a862105b2bff5a1f14ff4/scipy-1.1.0-cp27-none-win_amd64.whl</a> (31.5MB)</p>
<p>Requirement already satisfied: numpy&gt;=1.8.2 in d:\slicer 4.9.0-2018-08-31\lib\python\lib\site-packages\numpy-1.13.1-py2.7-win-amd64.egg (from scipy) (1.13.1)</p>
<p>Installing collected packages: scipy</p>
<p>Successfully installed scipy-1.1.0<br>
&gt;&gt;&gt; pipmain([‘install’,‘scipy’])</p>
<p>Collecting scipy</p>
<p>Downloading <a href="https://files.pythonhosted.org/packages/d2/a7/0d698589a3c6c44f81078a52518c8e64c4ed579a862105b2bff5a1f14ff4/scipy-1.1.0-cp27-none-win_amd64.whl" rel="noopener nofollow ugc">https://files.pythonhosted.org/packages/d2/a7/0d698589a3c6c44f81078a52518c8e64c4ed579a862105b2bff5a1f14ff4/scipy-1.1.0-cp27-none-win_amd64.whl</a> (31.5MB)</p>
<p>Requirement already satisfied: numpy&gt;=1.8.2 in d:\slicer 4.9.0-2018-08-31\lib\python\lib\site-packages\numpy-1.13.1-py2.7-win-amd64.egg (from scipy) (1.13.1)</p>
<p>Installing collected packages: scipy</p>
<p>Successfully installed scipy-1.1.0</p>
<p>&gt;&gt;&gt; pipmain([‘install’,‘scipy’])</p>
<p>Collecting scipy</p>
<p>Downloading <a href="https://files.pythonhosted.org/packages/d2/a7/0d698589a3c6c44f81078a52518c8e64c4ed579a862105b2bff5a1f14ff4/scipy-1.1.0-cp27-none-win_amd64.whl" rel="noopener nofollow ugc">https://files.pythonhosted.org/packages/d2/a7/0d698589a3c6c44f81078a52518c8e64c4ed579a862105b2bff5a1f14ff4/scipy-1.1.0-cp27-none-win_amd64.whl</a> (31.5MB)</p>
<p>Requirement already satisfied: numpy&gt;=1.8.2 in d:\slicer 4.9.0-2018-08-31\lib\python\lib\site-packages\numpy-1.13.1-py2.7-win-amd64.egg (from scipy) (1.13.1)</p>
<p>Installing collected packages: scipy</p>
<p>Successfully installed scipy-1.1.0</p>

---

## Post #22 by @Saima (2018-09-06 03:40 UTC)

<p>Why I cant install this package</p>
<p>pipmain([‘install’,‘scikit-fuzzy’])</p>
<p>Collecting scikit-fuzzy</p>
<p>Using cached <a href="https://files.pythonhosted.org/packages/fb/79/71a79d2663ed662d30461aca261baff4fc87ddfd23f3e9baeaee86917f6b/scikit-fuzzy-0.3.1.tar.gz" rel="nofollow noopener">https://files.pythonhosted.org/packages/fb/79/71a79d2663ed662d30461aca261baff4fc87ddfd23f3e9baeaee86917f6b/scikit-fuzzy-0.3.1.tar.gz</a></p>
<p>Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: ‘c:\users\22374464\appdata\local\temp\pip-req-tracker-v9vnky\6fa5e984c9f7c4180f5cbc9dc5bc4378cf0a090dcb740963746419f9’</p>

---

## Post #23 by @lassoan (2018-09-06 05:00 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Since Slicer bundles its own <em>python</em> , it is generally <strong>NOT</strong> possible to simply copy python packages (especially the one including binaries) from your own <code>site-packages</code> into the one of Slicer.</p>
</blockquote>
</aside>
<p>See more details in this post - see above.</p>

---

## Post #24 by @Saima (2018-09-07 06:07 UTC)

<p>Hi,<br>
I tried to install scikit-image but this is what I get</p>
<pre><code class="lang-auto">from pip._internal import main as pipmain

&amp;gt;&amp;gt;&amp;gt; pipmain(['install','scikit-image'])

Collecting scikit-image

Downloading https://files.pythonhosted.org/packages/0b/77/909865af5c9dd0fae58723e599747d204586096fd56199d51c6dcb0262e7/scikit_image-0.14.0-cp27-none-win_amd64.whl (24.7MB)

Collecting dask[array]&amp;gt;=0.9.0 (from scikit-image)

Downloading https://files.pythonhosted.org/packages/ea/e7/f01b2e72b4c235ee23c7730424b7bb0b36f1e93c90c129a8a14d7984ba5f/dask-0.19.1-py2.py3-none-any.whl (655kB)

Requirement already satisfied: six&amp;gt;=1.10.0 in d:\slicer 4.9.0-2018-08-31\lib\python\lib\site-packages (from scikit-image) (1.11.0)

Collecting pillow&amp;gt;=4.3.0 (from scikit-image)

Downloading https://files.pythonhosted.org/packages/48/91/f058672c494e186dc900bb6253e8cbde3307da17aed0a2d1ebcfb80ab766/Pillow-5.2.0-cp27-cp27m-win_amd64.whl (1.5MB)

Collecting PyWavelets&amp;gt;=0.4.0 (from scikit-image)

Downloading https://files.pythonhosted.org/packages/60/b4/d54dcf1c614ddf219fbb3612e6b0981706406ef54c1d2430be2efc5084cc/PyWavelets-1.0.0-cp27-none-win_amd64.whl (4.2MB)

Collecting networkx&amp;gt;=1.8 (from scikit-image)

Downloading https://files.pythonhosted.org/packages/11/42/f951cc6838a4dff6ce57211c4d7f8444809ccbe2134179950301e5c4c83c/networkx-2.1.zip (1.6MB)

Collecting cloudpickle&amp;gt;=0.2.1 (from scikit-image)

Downloading https://files.pythonhosted.org/packages/3e/41/cf788c011bff0ccf651fea2014450547213a03b3535a0f1bf813bf119aaf/cloudpickle-0.5.5-py2.py3-none-any.whl

Requirement already satisfied: numpy&amp;gt;=1.11.0; extra == &amp;quot;array&amp;quot; in d:\slicer 4.9.0-2018-08-31\lib\python\lib\site-packages\numpy-1.13.1-py2.7-win-amd64.egg (from dask[array]&amp;gt;=0.9.0-&amp;gt;scikit-image) (1.13.1)

Collecting toolz&amp;gt;=0.7.3; extra == &amp;quot;array&amp;quot; (from dask[array]&amp;gt;=0.9.0-&amp;gt;scikit-image)

Downloading https://files.pythonhosted.org/packages/14/d0/a73c15bbeda3d2e7b381a36afb0d9cd770a9f4adc5d1532691013ba881db/toolz-0.9.0.tar.gz (45kB)

Collecting decorator&amp;gt;=4.1.0 (from networkx&amp;gt;=1.8-&amp;gt;scikit-image)

Downloading https://files.pythonhosted.org/packages/bc/bb/a24838832ba35baf52f32ab1a49b906b5f82fb7c76b2f6a7e35e140bac30/decorator-4.3.0-py2.py3-none-any.whl

Building wheels for collected packages: networkx, toolz

Running setup.py bdist_wheel for networkx: started

Running setup.py bdist_wheel for networkx: finished with status 'done'

Stored in directory: C:\Users\22374464\AppData\Local\pip\Cache\wheels\44\c0\34\6f98693a554301bdb405f8d65d95bbcd3e50180cbfdd98a94e

Running setup.py bdist_wheel for toolz: started

Running setup.py bdist_wheel for toolz: finished with status 'done'

Stored in directory: C:\Users\22374464\AppData\Local\pip\Cache\wheels\f4\0c\f6\ce6b2d1aa459ee97cc3c0f82236302bd62d89c86c700219463

Successfully built networkx toolz

Installing collected packages: toolz, dask, pillow, PyWavelets, decorator, networkx, cloudpickle, scikit-image

**The script skivi.exe is installed in 'D:\Slicer 4.9.0-2018-08-31\lib\Python\Scripts' which is not on PATH.**

Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

Successfully installed PyWavelets-1.0.0 cloudpickle-0.5.5 dask-0.19.1 decorator-4.3.0 networkx-2.1 pillow-5.2.0 scikit-image-0.14.0 toolz-0.9.0

0

&amp;gt;&amp;gt;&amp;gt;
</code></pre>

---

## Post #25 by @Saima (2018-09-07 08:13 UTC)

<p>Hi,<br>
I was working on jupyter with scipy and suddenly it stoped working. What happened I dont know. it was importing before but not anymore</p>
<pre><code>]:

import scipy

x

1

import scipy

Out[22]:

Traceback (most recent call last): File "&amp;lt;string&amp;gt;", line 1, in &amp;lt;module&amp;gt; File "D:\Slicer 4.9.0-2018-08-31\lib\Python\Lib\site-packages\scipy\__init__.py", line 77, in &amp;lt;module&amp;gt; from . import _distributor_init ImportError: cannot import name _distributor_init</code></pre>

---

## Post #26 by @Saima (2018-09-07 09:51 UTC)

<aside class="quote no-group" data-username="Saima" data-post="21" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>rom pip._internal import main as pipmain</p>
</blockquote>
</aside>
<p>I successfully installed scipy used it once but now its not working:</p>
<pre><code>from pip._internal import main as pipmain

&amp;gt;&amp;gt;&amp;gt; pipmain(['install','scipy'])

Requirement already satisfied: scipy in d:\slicer 4.9.0-2018-08-31\lib\python\lib\site-packages (1.1.0)

Requirement already satisfied: numpy&amp;gt;=1.8.2 in d:\slicer 4.9.0-2018-08-31\lib\python\lib\site-packages\numpy-1.13.1-py2.7-win-amd64.egg (from scipy) (1.13.1)

0

&amp;gt;&amp;gt;&amp;gt; import scipy

Traceback (most recent call last):

File &amp;quot;&amp;lt;console&amp;gt;&amp;quot;, line 1, in &amp;lt;module&amp;gt;

File &amp;quot;D:\Slicer 4.9.0-2018-08-31\lib\Python\Lib\site-packages\scipy\__init__.py&amp;quot;, line 77, in &amp;lt;module&amp;gt;

from . import _distributor_init

ImportError: cannot import name _distributor_init
</code></pre>

---

## Post #27 by @lassoan (2018-09-07 12:37 UTC)

<p>Currently, you cannot import scipy into Slicer’s embedded Python interpreter. You have access to many Python libraries, you can use numpy, you can run a Jupyter kernel in Slicer’s Python interpreter, import native Python libraries, etc. but not import entire scipy.</p>
<p>Probably we can make Slicer’s Python interpreter compatible with all Python packages, including scipy, within 4-6 months.</p>

---

## Post #28 by @Saima (2018-09-26 04:02 UTC)

<p>Hi,<br>
I need official packages of python. If I switch to ubuntu. will I be able to install any official package? is there anything I cant do in slicer on linux as compared to widows.</p>
<p>I am not sure of switching but without official packages (scipy, scikit-image, skfuzzy etc) I am unable to proceed with my work. Any option if I stay in windows and can still install official packages.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #29 by @lassoan (2018-09-26 05:47 UTC)

<p>Thanks to recent developments, you can already use all these official packages on Windows. You need to implement your processing in Python CLI modules. Slicer writes all input data to files, launches your module with the active Python interpreter (it can be any Python on your computer), and when processing is completed read all the outputs. Process data in CLI module is useful anyway, as processing can run in the background, without blocking the user interface.</p>
<p>See <a href="https://github.com/SlicerDMRI/SlicerWMA">White Matter Analysis extension</a> as an example, which uses scipy, multiprocessing, xlrd, cython, joblib, … packages.</p>
<p>Within about 6 months, we plan to migrate Slicer to Python 3 and then we’ll be able to load any binary Python packages directly in Slicer’s interpreter. However, it’ll be still advisable to do most of the processing in Python CLI modules so that they can run in the background, easily interrupted, etc.</p>

---

## Post #30 by @Saima (2018-10-24 10:39 UTC)

<p>Hi Andras,<br>
I could no understand white matter analysis extension. is there a simple example for python cli modules. or do you recommend any workshop which can help me to learn how to develop cli extensions within slicer.</p>
<p>regards,<br>
Saima Safdar</p>

---

## Post #31 by @lassoan (2018-10-25 04:20 UTC)

<p>A simpler example is PyCLIModule4Test example:</p>
<ul>
<li>Module parameters/GUI specification: <a href="https://github.com/Slicer/Slicer/blob/master/Base/QTCLI/Testing/PyCLIModule4Test.xml">https://github.com/Slicer/Slicer/blob/master/Base/QTCLI/Testing/PyCLIModule4Test.xml</a>
</li>
<li>Executed python script:<br>
<a href="https://github.com/Slicer/Slicer/blob/master/Base/QTCLI/Testing/PyCLIModule4Test.py">https://github.com/Slicer/Slicer/blob/master/Base/QTCLI/Testing/PyCLIModule4Test.py</a>
</li>
</ul>
<p>In the executed Python script you can launch an external Python interpreter (Python3, anaconda, etc.), similarly to how it is done here: <a href="https://discourse.slicer.org/t/subprocess-call-in-python-interpreter-results-in-memory-corruption/919/11?u=lassoan">Subprocess call in Python interpreter results in memory corruption</a></p>

---

## Post #32 by @Saima (2018-10-26 07:02 UTC)

<p>Hi Andras,<br>
Is there any video on how to develop cli modules. I have searched for step by step guide but couldnt found. I am unable to establish links between different files. How to run these files?<br>
I have seen videos for how to make scripted modules in slicer and how to use the build in cli modules.<br>
I am unable to understand the connections between files.<br>
When I create a cli module in slicer is gives me .xml and .cxx files. Do i need to create the .py and place it in this folder.<br>
How to run this module in slicer? as with scripted it appears in the modules section but cli do not appear in the modules section.</p>
<p>Please help</p>
<p>Regards,<br>
Saima</p>

---

## Post #33 by @Felipe_Cabrera (2018-11-30 21:23 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, and about using TensorFlow with Slicer in a Windows 10, is it possible now?<br>
What are the steps that i need to take to make it work?</p>
<p>Thanks</p>

---

## Post #34 by @lassoan (2018-11-30 23:22 UTC)

<p>Yes, it works. You can run any Python script in any environment that you have set up on your system as described in my post above.</p>

---

## Post #35 by @DAVID_GARCIA_MATO (2018-12-10 15:21 UTC)

<p>Hi Andras,</p>
<p>I would like to use the function <strong>scipy.optimize.minimize</strong> from <strong>scipy</strong>.</p>
<p>I have tried to install scipy using pip in Slicer 4.8.1 and 4.10.0, but I am not able to install it properly. I get the following error:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5860825b6b63ec8f9fd7be698f096785f137fbb7.png" alt="image" data-base62-sha1="cBOMOQUQWPyz4xFUVzzYxzZkTwb" width="500" height="291"></p>
<p>I am doing the installation like this:</p>
<p>from pip._internal import main as pipmain<br>
pipmain([‘install’,‘scipy’])</p>
<p>Is there any way I can use scipy.optimize.minimize function is my 3D Slicer module? What about using this function from a Python CLI module?</p>
<p>Thanks for your time,</p>
<p>Best,</p>
<p>David</p>

---

## Post #36 by @jcfr (2018-12-10 16:05 UTC)

<p>Hi David,</p>
<p>We will shortly distribute scipy along with Slicer, this should happen by the end of the week.</p>
<p>Thanks for your patience,<br>
Jc</p>

---

## Post #37 by @lassoan (2018-12-10 16:12 UTC)

<p>This will be great! Is it going to be included in Slicer-4.10.1? If it is not risky/complicated then it probably should.</p>

---

## Post #38 by @DAVID_GARCIA_MATO (2018-12-10 16:31 UTC)

<p>That’s great JC! Thanks for the info!</p>
<p>I will check it at the end of the week. It would be great if it was included in the nightly build or the stable version.</p>

---

## Post #39 by @DAVID_GARCIA_MATO (2018-12-20 11:57 UTC)

<p>Hi JC,</p>
<p>Is Scipy already available?</p>
<p>Thanks!</p>
<p>David</p>

---

## Post #40 by @jcfr (2018-12-20 12:10 UTC)

<p>Hi David,</p>
<p>Not yet, I have to tackle a more urgent deadline first. I will resume work on scipy integration afterward.</p>
<p>Jc</p>

---

## Post #41 by @brhoom (2018-12-20 12:20 UTC)

<p>In my case, I tried to add scipy via slicer python interactor (as I did with 4.8.1) but it didn’t work. I added scipy to slicer-4.10 by copy/paste scipy folder from 4.8.1 and it works. e.g.</p>
<pre><code>cp -r  Slicer-4.8.1/lib/Python/lib/python2.7/site-packages/scipy   Slicer-4.10.0/lib/Python/lib/python2.7/site-packages</code></pre>

---

## Post #42 by @lassoan (2018-12-20 12:54 UTC)

<p>Python binaries are ABI compatible with Slicer’s bundled Python in Linux but not in Windows. If you use Windows, you need to wait for Jc.</p>

---

## Post #43 by @ZiyunLiang (2019-03-08 04:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Start Slicer as administrator: in the start menu, instead of left-click on the Slicer icon, use right-click, then select <code>More...</code> and <code>Run as Administrator</code> .</p>
</blockquote>
</aside>
<p>Hi, I’m  having the same problem when I try to install packages to my computer. I tried the pip way as you described but it did not work  for me. No matter what package I try to install, it always report to  following  errors:<br>
Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: ‘/private/var/folders/4m/3zz84kjj0rb8r7twkxksmplw0000gn/T/pip-req-tracker-dVJBGY/39e3ab1dfb11346e7d530d2e1ee1ef3dc8bbf9578e5f497994026cda’<br>
and some times like  this: Could not install packages due to an EnvironmentError: [Errno 30] Read-only file system: ‘/Volumes/Slicer-4.10.0-macosx-amd64/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/python_dateutil-2.8.0.dist-info’<br>
I was wondering  if this is because I didn’t run slicer as an administrator. I’m using mac  and when I right click on the icon, I didn’t see more and run as administrator. Does anyone know to run slicer on mac as an administrator? And does anyone know how to fix this error?<br>
Please help.</p>
<p>Thanks,<br>
Andrea</p>

---

## Post #44 by @pieper (2019-03-08 12:05 UTC)

<p>Hi - it looks like you didn’t drag the application to a writable location.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/Installation#Mac" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/Installation#Mac</a></p>

---

## Post #45 by @ZiyunLiang (2019-03-09 02:20 UTC)

<p>Hi, Thank you for the advice! I checked and I think Slicer is at a writable location right now. And I also tried to open it as an administrator by command <em>Applications andrealiang$ sudo open Slicer.app</em> at the terminal. But I still get the following error:<br>
<em>Requirement already satisfied: pandas in ./Slicer.app/Contents/lib/Python/lib/python2.7/site-packages (0.24.1)</em></p>
<p><em>Requirement already satisfied: python-dateutil&gt;=2.5.0 in ./Slicer.app/Contents/lib/Python/lib/python2.7/site-packages (from pandas) (2.8.0)</em></p>
<p><em>Requirement already satisfied: numpy&gt;=1.12.0 in ./Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.9-x86_64.egg (from pandas) (1.13.1)</em></p>
<p><em>Requirement already satisfied: pytz&gt;=2011k in ./Slicer.app/Contents/lib/Python/lib/python2.7/site-packages (from pandas) (2018.9)</em></p>
<p><em>Requirement already satisfied: six&gt;=1.5 in ./Slicer.app/Contents/lib/Python/lib/python2.7/site-packages (from python-dateutil&gt;=2.5.0-&gt;pandas) (1.11.0)</em></p>
<p><em>Collecting importlib</em></p>
<p><em>Using cached <a href="https://files.pythonhosted.org/packages/31/77/3781f65cafe55480b56914def99022a5d2965a4bb269655c89ef2f1de3cd/importlib-1.0.4.zip" rel="nofollow noopener">https://files.pythonhosted.org/packages/31/77/3781f65cafe55480b56914def99022a5d2965a4bb269655c89ef2f1de3cd/importlib-1.0.4.zip</a></em></p>
<p><em>Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: ‘/private/var/folders/4m/3zz84kjj0rb8r7twkxksmplw0000gn/T/pip-req-tracker-rEfQlE/20483040384e67f98bad799531b988be6a42bb897823a965fb554d64’</em></p>
<p>It looks like it has already installed the package pandas, but is having trouble with the second package. Does anyone know how to fix this bug?</p>
<p>Thanks!<br>
Andrea</p>

---

## Post #46 by @ZiyunLiang (2019-03-11 02:42 UTC)

<p>Hi everyone, after days of trying, my problem is solved in two ways. And I’d like to share my solutions with you.</p>
<ol>
<li>As for me, I’m using mac, and to successfully install the packages, mac users need to put the software in the directory Users/<em>yourname</em>/Applications rather than /Applications. Or if your software is in the directory /Applications, you can open it by option+open</li>
<li>you can use multithreading, which is <em>to run Python script using a non-Slicer Python environment</em> as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_run_Python_script_using_a_non-Slicer_Python_environment" rel="nofollow noopener">here</a>.</li>
</ol>

---

## Post #47 by @Alex_Vergara (2019-03-13 14:21 UTC)

<aside class="quote no-group" data-username="ZiyunLiang" data-post="46" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/5daacb/48.png" class="avatar"> ZiyunLiang:</div>
<blockquote>
<p>you can use multithreading, which is <em>to run Python script using a non-Slicer Python environment</em> as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_run_Python_script_using_a_non-Slicer_Python_environment" rel="noopener nofollow ugc">here </a>.</p>
</blockquote>
</aside>
<p>I don’t get your point, no matter what I am not able to run multithreading, all packages run in a single processor even if they split threads. I have tried with multiprocessing, cython, numba, ipyparallel, joblib, handythreads. Everything has same behaviour, yes they can be installed but multithreading is just not working. Using an external python for this is not efficient since you have to pass big arrays (files). Can you elaborate more this point please?</p>

---

## Post #48 by @lassoan (2019-03-13 14:28 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="47" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Using an external python for this is not efficient since you have to pass big arrays (files)</p>
</blockquote>
</aside>
<p>Have you actually measured the time to pass large arrays through files? My experience is that if you don’t use compression then it works extremely fast. I guess that pickling of numpy arrays is quite well optimized, too. If you find that data transfer is the performance bottleneck then you can go lower level and use shared memory transfer.</p>

---

## Post #50 by @roberta (2019-04-02 11:00 UTC)

<p>Hi!! i have 4.11 slicer version. I’d like to know if there is a way to display the spect / ct on slicer</p>

---

## Post #53 by @Alex_Vergara (2019-04-04 15:02 UTC)

<p><a class="mention" href="/u/roberta">@roberta</a> Please create a new thread with your question and please gives us more information on what you want to do so we can help you.</p>

---

## Post #54 by @fpsiddiqui91 (2019-07-22 09:53 UTC)

<p>Hello Developers,</p>
<p>I am trying to install python packages from Python interactor but it gives error.</p>
<p>I am using Slicer 4.10 in Linux Centos 7 OS</p>
<p>I am trying like this:</p>
<pre><code>import pip 
pip.main(['install', 'scipy'])
</code></pre>
<p>but it gives this error:</p>
<p>AttributeError: ‘module’ object has no attribute ‘main’</p>
<p>I have also tried with build tree but it gives the same error.  Can you please help me with installing Python packages.</p>
<p>thank you so much for all your support.</p>

---

## Post #55 by @jamesobutler (2019-07-22 11:40 UTC)

<p>For Slicer 4.10 I would probably suggest opening a terminal window to the location of PythonSlicer and doing <code>PythonSlicer.exe -m pip install scipy</code>. The error you are getting is because the “pip” package was updated and “main” was moved out. You could try some work around as was suggested earlier in this discussion such as</p>
<pre><code class="lang-auto">from pip._internal import main as pipmain
pipmain(['install','scipy'])
</code></pre>
<p>If using Slicer 4.11, Slicer is now using Python3. You could also use a helper function within Slicer’s python interactor. Try <code>slicer.util.pip_install('scipy')</code>.<br>
Reference: <a href="https://discourse.slicer.org/t/use-full-power-of-python-in-slicer/7162" class="inline-onebox">Use full power of Python in Slicer</a></p>
<p>Note: If you install scipy in Slicer 4.10, which is using python2, you will <strong>not</strong> be using the latest version of scipy (1.3.0). Scipy 1.3.0 is only available for Python3.</p>

---

## Post #56 by @fpsiddiqui91 (2019-07-22 13:08 UTC)

<p>Thank you so much for your response. it worked. I am also going to update Slicer to 4.11.</p>
<p>Thank you again</p>

---

## Post #57 by @Saima (2019-07-23 08:35 UTC)

<aside class="quote no-group" data-username="Saima" data-post="21" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>pipmain([‘install’,‘scipy’])</p>
</blockquote>
</aside>
<p>pipmain([‘install’,‘pynrrd’])</p>
<p>Collecting pynrrd</p>
<p>Using cached <a href="https://files.pythonhosted.org/packages/75/db/d0b421a9cbf84ce2af6f95e433f472b6a49e27e9355c027c8680ca9163af/pynrrd-0.4.0-py2.py3-none-any.whl" rel="noopener nofollow ugc">https://files.pythonhosted.org/packages/75/db/d0b421a9cbf84ce2af6f95e433f472b6a49e27e9355c027c8680ca9163af/pynrrd-0.4.0-py2.py3-none-any.whl</a></p>
<p>Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: ‘C:\Users\22374464\AppData\Local\Temp\pip-req-tracker-de0bnyq2\038c22fe9d64f3b52795137322e50c0d971005e9da8841928046b4a7’</p>
<p>Any idea of how to install pynrrd</p>

---

## Post #58 by @jamesobutler (2019-07-23 09:53 UTC)

<p>Since you had issues using pipmain and I’m assuming you are using Slicer 4.10, then you should try <code>PythonSlicer.exe -m pip install pynrrd</code> to install this pure python package. Don’t use pipmain if you’re using Slicer 4.11 nightly.</p>
<p>If you’re using Slicer 4.11 nightly, you can easily use <code>slicer.util.pip_install('pynrrd')</code>as stayed above.</p>

---

## Post #59 by @Saima (2019-07-23 09:58 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="58" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>slicer.util.pip_install(‘pynrrd’)</p>
</blockquote>
</aside>
<p>i am using slicer 4.11.0 nightly</p>
<p>I followed and got<br>
slicer.util.pip_install(‘pynrrd’)<br>
Collecting pynrrd<br>
Using cached <a href="https://files.pythonhosted.org/packages/75/db/d0b421a9cbf84ce2af6f95e433f472b6a49e27e9355c027c8680ca9163af/pynrrd-0.4.0-py2.py3-none-any.whl" rel="noopener nofollow ugc">https://files.pythonhosted.org/packages/75/db/d0b421a9cbf84ce2af6f95e433f472b6a49e27e9355c027c8680ca9163af/pynrrd-0.4.0-py2.py3-none-any.whl</a><br>
Could not install packages due to an EnvironmentError: [Errno 2] No such file or directory: ‘C:\Users\22374464\AppData\Local\Temp\pip-req-tracker-de0bnyq2\038c22fe9d64f3b52795137322e50c0d971005e9da8841928046b4a7’</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\22374464\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-06\bin\Python\slicer\util.py”, line 2002, in pip_install<br>
logProcessOutput(proc)<br>
File “C:\Users\22374464\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-06\bin\Python\slicer\util.py”, line 1955, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/22374464/AppData/Local/NA-MIC/Slicer 4.11.0-2019-07-06/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pynrrd’]’ returned non-zero exit status 1.</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>

---

## Post #60 by @Alex_Vergara (2019-07-23 10:00 UTC)

<p>I see you are using windows, therefore you have installed Slicer into Programs files folder without writing permissions for slicer. You shall uninstall Slicer and reinstall in a writable folder like Documents, etc. This will solve your problems.</p>

---

## Post #61 by @lassoan (2019-07-23 13:30 UTC)

<p>It seems that it is a recent Slicer Preview version, which installs itself to a writeable location by default, so write access should not be an issue.</p>
<p><code>pynnrd</code> does not seem to be available on PyPI:</p>
<pre><code class="lang-nohighlight">&gt;&gt;&gt; pip_install('pynnrd')
Loading Slicer RC file [C:/Users/andra/.slicerrc.py]
Collecting pynnrd
  Could not find a version that satisfies the requirement pynnrd (from versions: )
No matching distribution found for pynnrd
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-15\bin\Python\slicer\util.py", line 2002, in pip_install
    logProcessOutput(proc)
  File "C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-15\bin\Python\slicer\util.py", line 1955, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/andra/AppData/Local/NA-MIC/Slicer 4.11.0-2019-07-15/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'pynnrd']' returned non-zero exit status 1.
</code></pre>
<p>On your computer, there seem to be some cached pynrrd package, which is probably not compatible.</p>
<p>You should not need to import basic functionalities such as nrrd file reading from python.</p>
<p>You can read a nrrd file using <code>vol=slicer.util.loadVolume('something.nrrd')</code>, if you want to access it as a numpy array, call <code>a=slicer.util.arrayFromVolume(vol)</code>. This approach has the advantage that you can directly manipulate the voxels that Slicer displays.</p>

---

## Post #62 by @jamesobutler (2019-07-23 14:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> The output error you posted happened because you tried to install <code>pynnrd</code> instead <code>pynrrd</code>. Just a simple typo.</p>
<p>I was able to successfully install this <code>pynrrd</code> package using <code>slicer.util.pip_install('pynrrd')</code>.  I do think the previous errors have been due to some messed up cache of the download. Deleting that cache and then retrying should work.</p>

---

## Post #63 by @lassoan (2019-07-23 16:12 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="62" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The output error you posted happened because you tried to install <code>pynnrd</code> instead <code>pynrrd</code> . Just a simple typo.</p>
</blockquote>
</aside>
<p>Good catch, thank you!</p>

---

## Post #64 by @Saima (2019-07-29 06:40 UTC)

<p>thankyou so much yes it was a typo</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a2b6f84929cebe9793f8fa5a6d0b21d389052e3.png" data-download-href="/uploads/short-url/lZQAD90qktZZGNODRaH53saQHir.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a2b6f84929cebe9793f8fa5a6d0b21d389052e3_2_625x500.png" alt="image" data-base62-sha1="lZQAD90qktZZGNODRaH53saQHir" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a2b6f84929cebe9793f8fa5a6d0b21d389052e3_2_625x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a2b6f84929cebe9793f8fa5a6d0b21d389052e3_2_937x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a2b6f84929cebe9793f8fa5a6d0b21d389052e3.png 2x" data-dominant-color="D1D2D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1082×865 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #65 by @Saima (2019-08-27 01:40 UTC)

<p>Hi Andras,<br>
gmsh-api is I need it within slicer. its succesfully installed but there is problem in using it within slicer. could you please help  how to resolve the issue:</p>
<blockquote>
<blockquote>
<blockquote>
<p>pip_install(“gmsh-api”)</p>
</blockquote>
</blockquote>
</blockquote>
<p>Requirement already satisfied: gmsh-api in c:\users\22374464\appdata\local\na-mic\slicer 4.11.0-2019-07-06\lib\python\lib\site-packages (0.1.5)</p>
<p>Requirement already satisfied: pandas in c:\users\22374464\appdata\local\na-mic\slicer 4.11.0-2019-07-06\lib\python\lib\site-packages (from gmsh-api) (0.25.1)</p>
<p>Requirement already satisfied: numpy in c:\users\22374464\appdata\local\na-mic\slicer 4.11.0-2019-07-06\lib\python\lib\site-packages\numpy-1.16.2-py3.6-win-amd64.egg (from gmsh-api) (1.16.2)</p>
<p>Requirement already satisfied: python-dateutil&gt;=2.6.1 in c:\users\22374464\appdata\local\na-mic\slicer 4.11.0-2019-07-06\lib\python\lib\site-packages (from pandas-&gt;gmsh-api) (2.8.0)</p>
<p>Requirement already satisfied: pytz&gt;=2017.2 in c:\users\22374464\appdata\local\na-mic\slicer 4.11.0-2019-07-06\lib\python\lib\site-packages (from pandas-&gt;gmsh-api) (2019.2)</p>
<p>Requirement already satisfied: six&gt;=1.5 in c:\users\22374464\appdata\local\na-mic\slicer 4.11.0-2019-07-06\lib\python\lib\site-packages (from python-dateutil&gt;=2.6.1-&gt;pandas-&gt;gmsh-api) (1.12.0)</p>
<p>but when I import the gmsh and try to run a script it gives me error. I am posting error below: The api works well on anaconda. I have used it before.<br>
File “C:/Users/22374464/AppData/Local/NA-MIC/Slicer 4.11.0-2019-07-06/Mesher/MeshCreator/MeshCreator.py”, line 165, in run<br>
import gmsh_api.gmsh as gmsh<br>
File “C:\Users\22374464\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-06\lib\Python\Lib\site-packages\gmsh_api\gmsh.py”, line 39, in <br>
lib = CDLL(libpath)<br>
File “C:\Users\22374464\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-06\lib\Python\Lib\ctypes_<em>init</em>_.py”, line 348, in <strong>init</strong><br>
self._handle = _dlopen(self._name, mode)<br>
TypeError: LoadLibrary() argument 1 must be str, not None</p>

---

## Post #66 by @lassoan (2019-08-27 02:52 UTC)

<p>Python wrapping of gmsh is quite messy. There are many python wrappers, they all work slightly differently and a few of those that I tried fail in various ways.</p>
<p><a href="https://pypi.org/project/pygmsh/" rel="nofollow noopener">pygmsh</a> is a quite simple one, which uses an installed gmsh executable and it seems to work for me. For example, this generates a mesh:</p>
<pre><code class="lang-python">import pygmsh

geom = pygmsh.opencascade.Geometry(
  characteristic_length_min=0.1,
  characteristic_length_max=0.1,
  )

rectangle = geom.add_rectangle([-1.0, -1.0, 0.0], 2.0, 2.0)
disk1 = geom.add_disk([-1.2, 0.0, 0.0], 0.5)
disk2 = geom.add_disk([+1.2, 0.0, 0.0], 0.5)
union = geom.boolean_union([rectangle, disk1, disk2])

disk3 = geom.add_disk([0.0, -0.9, 0.0], 0.5)
disk4 = geom.add_disk([0.0, +0.9, 0.0], 0.5)
flat = geom.boolean_difference([union], [disk3, disk4])

geom.extrude(flat, [0, 0, 0.3])

mesh = pygmsh.generate_mesh(geom, gmsh_path="c:/Users/andra/util/gmsh/gmsh.exe", msh_filename="c:/Users/andra/tmp/test.vtk", mesh_file_type="vtk")
</code></pre>

---

## Post #67 by @Saima (2019-08-30 03:16 UTC)

<p>Hi Andras,<br>
Sorry for asking a question about pygmsh. What if you want to load a geometry from file and not create it using the opencascade. I searched much in the google but couldnt find anything on this? Could you guide me please. any related documentation which can help me.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #68 by @lassoan (2019-08-30 19:41 UTC)

<p>Simplest is probably to write the model to file and run gmsh on that. Then read the output file to Slicer.</p>

---

## Post #69 by @Saima (2020-03-10 05:38 UTC)

<p>Hi andras,<br>
I am getting the error for installing<br>
import pip</p>
<blockquote>
<blockquote>
<blockquote>
<p>pip.main([‘install’, ‘numpy-stl’])</p>
</blockquote>
</blockquote>
</blockquote>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>AttributeError: module ‘pip’ has no attribute ‘main’</p>
<p>what am i missing???</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #70 by @Saima (2020-03-10 05:41 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="62" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>slicer.util.pip_install(‘pynrrd’)</p>
</blockquote>
</aside>
<p>resolved I used this.<br>
slicer.util.pip_install(‘numpy-stl’)</p>
<p>Didnt understand why main not worked.</p>

---

## Post #71 by @lassoan (2020-03-10 12:47 UTC)

<aside class="quote no-group" data-username="Saima" data-post="69" data-topic="984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>AttributeError: module ‘pip’ has no attribute ‘main’</p>
<p>what am i missing???</p>
</blockquote>
</aside>
<p><code>pip</code> has not been exposing <code>main</code> for a really long time (since pip 9.x; while current pip version is 19.x). You can use the current pip API or the slicer.util helper function that you have found.</p>
<p>By the way, you should not need numpy-stl for loading/saving models. You can use <code>slicer.util.loadModel('something.stl')</code> and <code>slicer.util.saveNode('something2.stl')</code> instead.</p>

---

## Post #72 by @WilliamLambert1205 (2023-03-31 12:39 UTC)

<p>Hi everyone,<br>
I tried to install matplotlib in slicer 5.3.0 and 5.1.0, returns a lot error like this, too long to paste</p>
<blockquote>
<blockquote>
<blockquote>
<p>import pip<br>
pip.main([‘install’, ‘matplotlib’])<br>
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.<br>
Please see <a href="https://github.com/pypa/pip/issues/5599" rel="noopener nofollow ugc">https://github.com/pypa/pip/issues/5599</a> for advice on fixing the underlying issue.<br>
To avoid this problem you can invoke Python with ‘-m pip’ instead of running pip directly.<br>
— Logging error —<br>
Traceback (most recent call last):<br>
File “”, line 60, in emit<br>
KeyError: 15<br>
Call stack:<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\code.py”, line 258, in push<br>
more = self.runsource(source, self.filename)<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\code.py”, line 74, in runsource<br>
self.runcode(code)<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\code.py”, line 90, in runcode<br>
exec(code, self.locals)<br>
File “”, line 1, in <br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\site-packages\pip_<em>init</em>_.py”, line 13, in main<br>
return <em>wrapper(args)<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\site-packages\pip_internal\utils\entrypoints.py”, line 43, in <em>wrapper<br>
return main(args)<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\site-packages\pip_internal\cli\main.py”, line 55, in main<br>
cmd_name, cmd_args = parse_command(args)<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\site-packages\pip_internal\cli\main_parser.py”, line 79, in parse_command<br>
general_options, args_else = parser.parse_args(args)<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\optparse.py”, line 1371, in parse_args<br>
values = self.get_default_values()<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\site-packages\pip_internal\cli\parser.py”, line 279, in get_default_values<br>
self.config.load()<br>
…<br>
…<br>
packages\pip_internal\cli\base_command.py", line 216, in <em>main<br>
self.handle_pip_version_check(options)<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\site-packages\pip_internal\cli\req_command.py”, line 190, in handle_pip_version_check<br>
pip_self_version_check(session, options)<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\site-packages\pip_internal\self_outdated_check.py”, line 238, in pip_self_version_check<br>
logger.warning(“There was an error checking the latest version of pip.”)<br>
File "D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\logging_<em>init</em></em>.py", line 1458, in warning<br>
self.<em>log(WARNING, msg, args, **kwargs)<br>
File "D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\logging_<em>init</em></em>.py", line 1589, in <em>log<br>
self.handle(record)<br>
File "D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\logging_<em>init</em></em>.py", line 1599, in handle<br>
self.callHandlers(record)<br>
File "D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\logging_<em>init</em></em>.py", line 1661, in callHandlers<br>
hdlr.handle(record)<br>
File "D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\logging_<em>init</em></em>.py", line 952, in handle<br>
self.emit(record)<br>
File “D:\Slicer 5.3.0-2022-12-16\lib\Python\Lib\site-packages\pip_internal\utils\logging.py”, line 179, in emit<br>
self.handleError(record)<br>
Message: ‘There was an error checking the latest version of pip.’<br>
Arguments: ()<br>
1</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #73 by @Sam_Horvath (2023-03-31 15:17 UTC)

<p>Please try using the <code>slicer.util</code> helper function, i.e.</p>
<pre><code class="lang-auto">slicer.util.pip_install('matplotlib')
</code></pre>

---

## Post #74 by @lassoan (2023-05-08 05:18 UTC)

<p>2 posts were split to a new topic: <a href="/t/cannot-import-gmsh-python-package/29344">Cannot import gmsh Python package</a></p>

---
