# Why is nightly build looking for local config?

**Topic ID**: 154
**Date**: 2017-04-20
**URL**: https://discourse.slicer.org/t/why-is-nightly-build-looking-for-local-config/154

---

## Post #1 by @tdiprima (2017-04-20 19:38 UTC)

<p>I compiled our extension, SlicerPathology, on Linux.  The Linux <a href="http://download.slicer.org/bitstream/624156" rel="nofollow noopener">nightly build</a>, when you use the  SlicerPathology extension, gives the following error message in the Python Interactor:</p>
<pre><code>[GCC 4.6.4] on linux2
&gt;&gt;&gt; Current SlicerOpenCVSelfTest.py path = 
/home/superbear/.config/NA-MIC/Extensions-25933/SlicerOpenCV/lib/Slicer-4.7/qt-scripted-modules
Trying to import cv2
Trying to import from file
Full path not found:  /home/superbear/.config/NA-MIC/Extensions-25933/OpenCV-build/lib/cv2.so
Loading cv2 from  cv2.so
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/superbear/.config/NA-MIC/Extensions-25933/SlicerOpenCV/lib/Slicer-4.7/qt-scripted-modules/SlicerOpenCVSelfTest.py", line 36, in &lt;module&gt;
    cv2 = imp.load_dynamic('cv2', cv2File)
ImportError: ./cv2.so: cannot open shared object file: No such file or directory
</code></pre>
<p>ok, that’s embarrassing.  Why is it looking for this .config directory in my local home directory?  How do I fix it?</p>

---

## Post #2 by @lassoan (2017-04-20 20:02 UTC)

<p>Extensions are installed in your local home directory, so normally they are loaded from there. Don’t you have <a href="http://SlicerOpenCVSelfTest.py">SlicerOpenCVSelfTest.py</a> in your local home directory?</p>
<p>While you are developing the extension you should be able to load it from your build tree. Try specifying --launcher-additional-settings (.ini file in your build tree) when you start Slicer.</p>

---

## Post #3 by @ihnorton (2017-04-20 20:06 UTC)

<aside class="quote no-group" data-username="tdiprima" data-post="1" data-topic="154">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tdiprima/48/9469_2.png" class="avatar"> tdiprima:</div>
<blockquote>
<p>Why is it looking for this .config directory in my local home directory?  How do I fix it?</p>
</blockquote>
</aside>
<p>On Linux (and Windows) the extension install directory is under HOME because it needs to be writable by the user, whereas the Slicer install directory is often read-only (e.g. <code>C:\Program Files</code>).</p>
<p>From a quick look at the package, it appears that there are some hard-coded loader paths which would need to be adjusted. <code>imp.load_dynamic('cv2', SO_PATH)</code> succeeds on my linux vm (where SO_PATH is the full path to <code>cv2.so</code>).</p>

---

## Post #4 by @fedorov (2017-04-20 20:20 UTC)

<p>This error comes from exposing of OpenCV functionality into Python. This was added by Nicole Aucoin, who is no longer working on this project. I remember she was saying that this error message is harmless.</p>

---

## Post #5 by @tdiprima (2017-04-20 20:36 UTC)

<p>Hi Andrey,</p>
<p>Thanks.  I was wondering how it got there.  It’s harmless but if anybody besides us downloads this, and if they’re reading carefully, there’re gonna wonder who the heck user ‘superbear’ is.  So… I have to ask… does anybody else there know about the opencv integration, or how to get around the hard-coding that was implemented?</p>
<p>Thanks,<br>
Tammy</p>

---

## Post #6 by @fedorov (2017-04-20 20:58 UTC)

<p>Tammy,</p>
<p>“superbear” must be the user name on your platform.</p>
<p>The reason it refers to <em>your</em> config file is because when you install an extension, that extension is installed on your computer in a specific location, and config file must be updated to point to that directory.</p>
<p>There is no hard-coded reference to “superbear” anywhere in the code, see <a href="https://github.com/sbu-bmi/SlicerOpenCV">https://github.com/sbu-bmi/SlicerOpenCV</a>.</p>
<p>I do agree however that the error message is misleading. Perhaps we should remove indications that Python integration of OpenCV is working, since it has never been verified by anyone.</p>
<p>This error message should not affect your work, since you use SlicerOpenCV from C++, not from Python.</p>

---

## Post #7 by @fedorov (2017-04-20 21:11 UTC)

<p>I disabled Python-OpenCV test to get rid of this misleading error message:</p>
<p><a href="https://github.com/SBU-BMI/SlicerOpenCV/commit/8b71734d0580b2d197ea1b91707760c219e26bf6" class="onebox" target="_blank">https://github.com/SBU-BMI/SlicerOpenCV/commit/8b71734d0580b2d197ea1b91707760c219e26bf6</a></p>

---

## Post #8 by @jcfr (2017-04-20 22:19 UTC)

<p>If OpenCV + python is needed, the new changes to support SlicerRadiomics should help. Let me know if it become an issue again.</p>

---
