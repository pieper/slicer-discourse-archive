# No extensions for latest nightly

**Topic ID**: 865
**Date**: 2017-08-14
**URL**: https://discourse.slicer.org/t/no-extensions-for-latest-nightly/865

---

## Post #1 by @lassoan (2017-08-14 12:09 UTC)

<p>There are no extensions available for latest nightly version (due to “Variable Slicer_QT_VERSION_MAJOR is not defined” error) and there are also some new failed tests.</p>
<p>As about half of the users download the latest nightly version, so we must keep the nightly versions fully functional.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Could you please remove the latest nightly build from MIDAS?</p>
<p><strong>Workaround:</strong> Users who come across this problem can download an earlier version (built 3 days ago) by using this link: <a href="http://download.slicer.org/?offset=-3">http://download.slicer.org/?offset=-3</a></p>

---

## Post #2 by @stevenagl12 (2017-08-14 13:20 UTC)

<p>I’m having the same issue with the Nightly version you put up for the workaround where it’s saying there are no extensions.</p>

---

## Post #3 by @moselhy (2017-08-14 13:25 UTC)

<p><a href="http://download.slicer.org/?offset=-1" rel="nofollow noopener">http://download.slicer.org/?offset=-1</a> works for me</p>

---

## Post #4 by @jcfr (2017-08-14 13:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="865">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you please remove the latest nightly build from MIDAS?</p>
</blockquote>
</aside>
<p>All set. After the internal database associated with <a href="http://download.slicer.org">download.slicer.org</a> is updated, we should be good.</p>

---

## Post #5 by @ihnorton (2018-08-08 13:46 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/no-extensions-in-extension-manager/3705/2">No extensions in extension manager</a></p>

---

## Post #6 by @kamrul079 (2018-08-13 03:24 UTC)

<p>I face the same problem. I had built slicer 4.8.1 from the source by myself.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/982db91dd3ac43a5b31e115ca86bd89eb4d261ce.png" data-download-href="/uploads/short-url/lIexhxQLEkJs6194UQVcmlQPTL8.png?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/982db91dd3ac43a5b31e115ca86bd89eb4d261ce_2_607x500.png" alt="slicer" data-base62-sha1="lIexhxQLEkJs6194UQVcmlQPTL8" width="607" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/982db91dd3ac43a5b31e115ca86bd89eb4d261ce_2_607x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/982db91dd3ac43a5b31e115ca86bd89eb4d261ce.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/982db91dd3ac43a5b31e115ca86bd89eb4d261ce.png 2x" data-dominant-color="FBFBFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">845×695 16.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @jcfr (2018-08-13 03:39 UTC)

<aside class="quote no-group" data-username="kamrul079" data-post="6" data-topic="865">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kamrul079/48/2059_2.png" class="avatar"> kamrul079:</div>
<blockquote>
<p>I had built slicer 4.8.1 from the source by myself.</p>
</blockquote>
</aside>
<p>Since the extensions associated with the latest release are already built, could you clarify why you had to rebuild Slicer 4.8.1 yourself ? Which problem were you trying to solve ?</p>

---

## Post #8 by @kamrul079 (2018-08-13 04:16 UTC)

<p>Our current project involves the revival of a project previously developed in 2015 in our lab with updates in syntax and logic for QT (VS2012 to VS2017), updates in code from C++ ’98 to C++ ’11, new versions of OpenCV (2.4.9 to 3.4.1), 3D Slicer (4.4.0 to 4.9.0), and ArUco (1.2.5 to 3.0.11). And thats why we are building the older version.</p>

---

## Post #9 by @kamrul079 (2018-08-13 04:38 UTC)

<p>Actually We were trying to upgrade from older to newer version. But before that we were trying to build older version of slicer. We will build a new module for Augmented reality application</p>

---

## Post #11 by @cpinter (2018-08-13 18:39 UTC)

<p>Have you added the binary folders to the Additional modules list in the Application settings? For example:<br>
[path_to_module_bin]\lib\Slicer-4.9\qt-loadable-modules\Release<br>
[path_to_module_bin]\lib\Slicer-4.9\qt-scripted-modules<br>
[path_to_module_bin]\lib\Slicer-4.9\cli-modules\Release<br>
Please note the Release/Debug folder for CLIs and loadable modules. These are only needed on Windows.</p>

---

## Post #12 by @kamrul079 (2018-08-13 18:41 UTC)

<p>I had added the qt binary file only because I will make the qt loadable module only</p>
<p><strong>[path_to_module_bin]\lib\Slicer-4.9\qt-loadable-modules</strong></p>
<p>not the<br>
[path_to_module_bin]\lib\Slicer-4.9\qt-loadable-modules\Release</p>

---

## Post #13 by @cpinter (2018-08-13 18:53 UTC)

<p>So when you open Slicer, then the Application Settings contains the correct path, but your module does not show up?</p>
<p>If so, can you send us the log? You can find it in About / Report a problem</p>
<p>Also, this may be a basic question but did you check it in the category that is set in the module? Can you find it by search?</p>

---

## Post #14 by @kamrul079 (2018-08-13 18:58 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f52b914a004dbefb4449df524e631f607d23de10.png" data-download-href="/uploads/short-url/yYSk2FhAwTOJxmMkrVFUXmtBMI0.png?dl=1" title="log" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f52b914a004dbefb4449df524e631f607d23de10.png" alt="log" data-base62-sha1="yYSk2FhAwTOJxmMkrVFUXmtBMI0" width="690" height="83" data-dominant-color="EAE9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">log</span><span class="informations">1902×230 12.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I had added the path but in the module finding,it does not show up.  I did not check it in the category. How to do that?</p>

---

## Post #15 by @cpinter (2018-08-13 19:11 UTC)

<p>There is neither “Release” nor “Debug” at the end of your module path</p>

---

## Post #16 by @kamrul079 (2018-08-13 19:31 UTC)

<p>I tried to use the Release path at the end but when i did that it showed an error message that: can not find the module</p>

---

## Post #17 by @kamrul079 (2018-08-13 20:02 UTC)

<p>Its working now. I didn’t add the module path in the “slicerLaunchSettings.ini” files. Now its working.<br>
Thanks a lot for your support</p>

---
