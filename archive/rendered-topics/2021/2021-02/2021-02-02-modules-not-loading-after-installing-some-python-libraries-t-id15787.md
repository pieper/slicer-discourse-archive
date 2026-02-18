# Modules not loading after installing some python libraries through the python console

**Topic ID**: 15787
**Date**: 2021-02-02
**URL**: https://discourse.slicer.org/t/modules-not-loading-after-installing-some-python-libraries-through-the-python-console/15787

---

## Post #1 by @Atabak (2021-02-02 04:51 UTC)

<p>Hi everyone,</p>
<p>I installed a couple of Python libraries (ctk, cv2,…) and my slicer stopped working like before after I restarted it. The errors that I get when I launch the software are the following:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘getSlicerRCFileName’ is not defined<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\D\S4R\python-install\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/D/S4R/Slicer-build/lib/Slicer-4.13/qt-scripted-modules/AddManyMarkupsFiducialTest.py”, line 5, in </p>
</blockquote>
<p>Operating system:Windows10<br>
Slicer version:4.13.0</p>
<p>I would appreciate some help on this.<br>
Thanks,<br>
Atabak</p>

---

## Post #2 by @lassoan (2021-02-02 04:58 UTC)

<p>We already use the ctk namespace for CTK (<a href="https://commontk.org/">https://commontk.org/</a>). Fortunately, <a href="https://pypi.org/project/ctk/">ctk Python package</a> does not seem to be a useful package, so you should just make sure that you or other packages don’t accidentally install it.</p>
<p>OpenCV is a huge collection of random stuff and there are many ways of making it out to be a Python package. It is entirely possible that some distributions can break Slicer.</p>
<p>If you find indispensable Python packages that seem to break Slicer then let us know and we can have a look.</p>

---

## Post #3 by @Atabak (2021-02-02 05:41 UTC)

<p>Hi Andras,</p>
<p>Thank you for your response. Here are the packages that I intended to install: “cv2, scipy, sitkUtils, SimpleITK, vtk, qt, ctk” . Some of them were already installed but some weren’t.</p>
<p>So how do I uninstall ctk Python package that I just installed?</p>
<p>I’m trying to use</p>
<blockquote>
<p>slicer.util.<code> </code>pip_uninstall` ( <em>requirements</em> )</p>
</blockquote>
<p>But, I’m getting the following error:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘slicer’ is not defined</p>
</blockquote>
<p>Thanks</p>

---

## Post #4 by @lassoan (2021-02-02 13:54 UTC)

<aside class="quote no-group" data-username="Atabak" data-post="3" data-topic="15787">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/atabak/48/7940_2.png" class="avatar"> Atabak:</div>
<blockquote>
<p>cv2, scipy, sitkUtils, SimpleITK, vtk, qt, ctk</p>
</blockquote>
</aside>
<p>These packages are already bundled with Slicer, do not try to reinstall them: scipy, sitkUtils, SimpleITK, vtk, qt, ctk (by the way, ctk is not a Python package from PyPI but a namespace where <a href="https://github.com/commontk/CTK">CTK library</a> classes are imported into).</p>
<aside class="quote no-group" data-username="Atabak" data-post="3" data-topic="15787">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/atabak/48/7940_2.png" class="avatar"> Atabak:</div>
<blockquote>
<p>So how do I uninstall ctk Python package that I just installed?</p>
</blockquote>
</aside>
<p>If you cannot uninstall it using <code>pip_uninstall</code> then you probably need to delete the entire application folder and reinstall Slicer, extensions, and Python packages from scratch.</p>
<p>OpenCV is a huge beast, it can break anything, depending on which variant you import. Which OpenCV packages have you tried to install?</p>
<p>What are you trying to achieve? Run Python scripts without showing the application GUI?</p>

---
