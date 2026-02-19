---
topic_id: 15139
title: "Create Installer Package With Extension And Configuration"
date: 2020-12-19
url: https://discourse.slicer.org/t/15139
---

# Create installer package with extension and configuration

**Topic ID**: 15139
**Date**: 2020-12-19
**URL**: https://discourse.slicer.org/t/create-installer-package-with-extension-and-configuration/15139

---

## Post #1 by @Tesla2678 (2020-12-19 01:35 UTC)

<p>Hello Every one,</p>
<p>I have a question about how to create an installer package(With a created extension).</p>
<p>I have followed the tutorial in<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e35c681bed89db3ffa28e26ff11d036f16a2c03.png" data-download-href="/uploads/short-url/fIXJzwSCdkkkakFpS2Rw1tya9eb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e35c681bed89db3ffa28e26ff11d036f16a2c03_2_690x190.png" alt="image" data-base62-sha1="fIXJzwSCdkkkakFpS2Rw1tya9eb" width="690" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e35c681bed89db3ffa28e26ff11d036f16a2c03_2_690x190.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e35c681bed89db3ffa28e26ff11d036f16a2c03_2_1035x285.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e35c681bed89db3ffa28e26ff11d036f16a2c03.png 2x" data-dominant-color="F0F7EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1336×369 25.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I just follow the tutorial method, the installer package created does not include my extension.</p>
<p>So, How to configure and create an installer package with an extension( in folder “\Slicer-build\Modules\Scripted”)?</p>

---

## Post #2 by @lassoan (2020-12-19 02:34 UTC)

<p>Have you built Slicer?<br>
Did you get any error message?</p>

---

## Post #3 by @Tesla2678 (2020-12-19 06:11 UTC)

<p>Hello Iassoan,</p>
<p>Yes, I have built it, and successful without error.<br>
But after installing the Slicer from the “installer package”, The Module folder and Extensions disappeared.</p>
<p>##################################################<br>
77&gt;Qt5WebChannel.dll is up to date.<br>
77&gt;libGLESv2.dll is up to date.<br>
77&gt;libEGL.dll is up to date.<br>
77&gt;D3Dcompiler_47.dll is up to date.<br>
77&gt;opengl32sw.dll is up to date.<br>
77&gt;Creating C:\Slicer_new\Slicer-build_CPack_Packages\win-amd64\NSIS\Slicer-4.11.0-2020-07-04-win-amd64\bin\resources…<br>
77&gt;Updating icudtl.dat.<br>
77&gt;Updating qtwebengine_devtools_resources.pak.<br>
77&gt;Updating qtwebengine_resources.pak.<br>
77&gt;Updating qtwebengine_resources_100p.pak.<br>
77&gt;Updating qtwebengine_resources_200p.pak.<br>
77&gt;Creating C:\Slicer_new\Slicer-build_CPack_Packages\win-amd64\NSIS\Slicer-4.11.0-2020-07-04-win-amd64\bin\translations\qtwebengine_locales…<br>
77&gt;Updating en-US.pak.<br>
77&gt;CPack: Create package<br>
77&gt;CPack: - package: C:/Slicer_new/Slicer-build/Slicer-4.11.0-2020-07-04-win-amd64.exe generated.<br>
========== 生成: 成功 77 个，失败 0 个，最新 504 个，跳过 0 个 ==========</p>

---

## Post #4 by @lassoan (2020-12-19 06:14 UTC)

<p>If you want to bundle an extension in your custom install package then the recommend method is to use the <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">Slicer Custom Application Template</a>.</p>

---

## Post #5 by @Tesla2678 (2020-12-19 07:48 UTC)

<p>Hello Iassoan,</p>
<p>This really a good tools,</p>
<p>I am going to try it~</p>
<p>Thank you very much!</p>

---

## Post #6 by @Tesla2678 (2020-12-21 04:27 UTC)

<p>Hello Iassoan,</p>
<p>Thank you for your instruction and recommend this method to me.( <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">Slicer Custom Application Template</a>)</p>
<p>I have followed the method below.</p>
<ol>
<li><a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/#step1" rel="noopener nofollow ugc">Generate the application framework from the template repository</a></li>
<li><a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/#step2" rel="noopener nofollow ugc">Customize the Slicer configuration using CMake (optional)</a></li>
<li><a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/#step5" rel="noopener nofollow ugc">Add new custom modules (optional)</a></li>
<li><a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/#step6" rel="noopener nofollow ugc">Build the custom app</a></li>
</ol>
<p>If I don’t execute the 3ed step “3. <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/#step5" rel="noopener nofollow ugc">Add new custom modules (optional)</a>”, everything goes okay, And I can build and get an example executable file. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bef12652daeb65c256031c523e6c328ac8d5b1fa.png" alt="image" data-base62-sha1="rf9nzDuwtl9a0mw14NgvzgpaSaS" width="176" height="30"></p>
<p>But After I added my custom module “Reader” in CMakeLists.txt by this config(followed step 3):</p>
<p>set(Slicer_EXTENSION_SOURCE_DIRS<br>
${AB_SOURCE_DIR}/Modules/Scripted/Reader<br>
)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abf376bc5c85ec46b21399da8bcdbb3df73afaf9.png" alt="image" data-base62-sha1="ox9gvuDPvfeUMQSCrdUtqFWiw2d" width="582" height="249"></p>
<p>Then I can’t even build a project.</p>
<p>I suspect the reason maybe comes from my python modules, I imported some new modules in my custom module “Reader” such as PyTorch.</p>
<p>Then I added all needed python modules in “C:\ABB\python-install\Lib\site-packages”<br>
and then I can access it in python Interactor:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39730600fdb0a511693a57840bcdbe044b30a91d.png" data-download-href="/uploads/short-url/8cdErVrYzgrNEEPcUWb4U2pPKI5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39730600fdb0a511693a57840bcdbe044b30a91d_2_690x462.png" alt="image" data-base62-sha1="8cdErVrYzgrNEEPcUWb4U2pPKI5" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39730600fdb0a511693a57840bcdbe044b30a91d_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39730600fdb0a511693a57840bcdbe044b30a91d_2_1035x693.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39730600fdb0a511693a57840bcdbe044b30a91d_2_1380x924.png 2x" data-dominant-color="8F969C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1559×1045 66.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I can’t rebuild it successfully. so, Can I get any to add a new module (with a new python package) in CMakeList?</p>

---

## Post #7 by @Tesla2678 (2020-12-22 03:28 UTC)

<p>I have solved this problem.</p>
<p>There are some problems with my custom modules.</p>
<p>Now It works,</p>
<p>Thank you!</p>

---

## Post #8 by @Tesla2678 (2020-12-28 00:31 UTC)

<p>Hello Iassoan,</p>
<p>Thank you for your help these days. My work nearly finishes, just 2 problems left.<br>
I have built the custom project partly successful (include some new python packages like PyQt5 and Matplotlib).<br>
While I met 2 problems. One is about the custom building, the other one is about the build-installer-package.</p>
<p><strong>1、Problem about custom building.</strong><br>
I followed the step in <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a></p>
<p>The building process is successful. I got an “AB.exe” file in the “Slicer-build” folder.</p>
<p>When I open it(AB.exe), I found some of my custom configs( such as rename the title from ‘AB’ to ‘Reader’) in my extension module (I set it as the default startup module) work well at the beginning. And then my custom configs(the title “Reader”) were replaced by system original configs(“AB”) rapidly. So most of my custom configs were failed. (this problem just affect outlook, so I can still work on it)</p>
<p><strong>2、Problem about the “build-installer-package”</strong><br>
When I start to build installer-package as the follow instruct. even though the installer-package was built successfully, but after I install and open it some problems will happen.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b1c550eafce3a2c11289d80985f3e9ccb05b667.png" data-download-href="/uploads/short-url/d009nVZZuyEKymZNJrMZzFnIC2z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b1c550eafce3a2c11289d80985f3e9ccb05b667_2_690x178.png" alt="image" data-base62-sha1="d009nVZZuyEKymZNJrMZzFnIC2z" width="690" height="178" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b1c550eafce3a2c11289d80985f3e9ccb05b667_2_690x178.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b1c550eafce3a2c11289d80985f3e9ccb05b667_2_1035x267.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b1c550eafce3a2c11289d80985f3e9ccb05b667.png 2x" data-dominant-color="F0F6EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1336×345 26 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On one of my computers, it can’t be started.<br>
On another computer, I started, but some bugs about the Python package raised. Shows below.</p>
<blockquote>
<pre><code>Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "D:\Program Files\AB 0.1.0-0000-00-00\lib\Python\Lib\imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "D:/Program Files/AB 0.1.0-0000-00-00/bin/../lib/AB-4.13/qt-scripted-modules/Reader.py", line 22, in &lt;module&gt;
    from PyQt5 import QtCore,Qt,QtGui
ImportError: DLL load failed: The specified module could not be found.
</code></pre>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80151bb77a7519aeae461ceefb4d7a227194d561.png" data-download-href="/uploads/short-url/ih4l6MtM2qnPKm1dqXiR0k4VVkJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80151bb77a7519aeae461ceefb4d7a227194d561_2_690x339.png" alt="image" data-base62-sha1="ih4l6MtM2qnPKm1dqXiR0k4VVkJ" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80151bb77a7519aeae461ceefb4d7a227194d561_2_690x339.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80151bb77a7519aeae461ceefb4d7a227194d561_2_1035x508.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80151bb77a7519aeae461ceefb4d7a227194d561_2_1380x678.png 2x" data-dominant-color="D1CED1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×945 73.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So, for Problem 1, I guess it may about the starting sequence.<br>
for Problem 2, I have no idea. It might about the method of built installer_package. I want to assure, I have a new module in slicer, then the create install_package process show start by “Slicer.exe --VisualStudioProject” is it right? maybe something wrong in here?<br>
It is not only the problem with the PyQt5 package. (I have tried to move code “from PyQt5 import QtCore,Qt,QtGui” to back of other code, another package got a problem)</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “D:\Program Files\AB 0.1.0-0000-00-00\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “D:/Program Files/AB 0.1.0-0000-00-00/bin/…/lib/AB-4.13/qt-scripted-modules/Reader.py”, line 45, in <br>
from matplotlib import pyplot as pp<br>
File “D:\Program Files\AB 0.1.0-0000-00-00\lib\Python\Lib\site-packages\matplotlib\pyplot.py”, line 115, in <br>
_backend_mod, new_figure_manager, draw_if_interactive, <em>show = pylab_setup()<br>
File "D:\Program Files\AB 0.1.0-0000-00-00\lib\Python\Lib\site-packages\matplotlib\backends_<em>init</em></em>.py", line 62, in pylab_setup<br>
[backend_name], 0)<br>
File “D:\Program Files\AB 0.1.0-0000-00-00\lib\Python\Lib\site-packages\matplotlib\backends\backend_tkagg.py”, line 4, in <br>
from . import tkagg  # Paint image to Tk photo blitter extension.<br>
File “D:\Program Files\AB 0.1.0-0000-00-00\lib\Python\Lib\site-packages\matplotlib\backends\tkagg.py”, line 5, in <br>
from six.moves import tkinter as Tk<br>
File “D:\Program Files\AB 0.1.0-0000-00-00\lib\Python\Lib\site-packages\six.py”, line 92, in <strong>get</strong><br>
result = self._resolve()<br>
File “D:\Program Files\AB 0.1.0-0000-00-00\lib\Python\Lib\site-packages\six.py”, line 115, in _resolve<br>
return _import_module(self.mod)<br>
File “D:\Program Files\AB 0.1.0-0000-00-00\lib\Python\Lib\site-packages\six.py”, line 82, in <em>import_module<br>
<strong>import</strong>(name)<br>
File "D:\Program Files\AB 0.1.0-0000-00-00\lib\Python\Lib\tkinter_<em>init</em></em>.py", line 36, in <br>
import _tkinter # If this fails your Python may not be configured for Tk<br>
ModuleNotFoundError: No module named ‘_tkinter’</p>
</blockquote>
<p>Could you give me some advice to solve these problems?</p>
<p>Thanks again~</p>

---
