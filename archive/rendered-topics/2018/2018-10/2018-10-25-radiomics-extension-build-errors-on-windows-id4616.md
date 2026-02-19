---
topic_id: 4616
title: "Radiomics Extension Build Errors On Windows"
date: 2018-10-25
url: https://discourse.slicer.org/t/4616
---

# Radiomics extension build errors on Windows

**Topic ID**: 4616
**Date**: 2018-10-25
**URL**: https://discourse.slicer.org/t/radiomics-extension-build-errors-on-windows/4616

---

## Post #1 by @pieper (2018-10-25 15:49 UTC)

<aside class="quote no-group" data-username="TingtingYu" data-post="5" data-topic="4496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/b38774/48.png" class="avatar"><a href="https://discourse.slicer.org/t/radiomics-extension-and-butterworth-filter/4496/5">Radiomics Extension and Butterworth Filter</a></div>
<blockquote>
<p>Thank you. I tried both stable-release and nightly-build version. None of them have “Radiomics” extension.</p>
</blockquote>
</aside>
<p>It’s available for linux 4.10, but there is a build error on windows.  <a class="mention" href="/u/joostjm">@JoostJM</a> or <a class="mention" href="/u/jcfr">@jcfr</a> any ideas about this one?</p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1410882" class="onebox" target="_blank" rel="noopener">http://slicer.cdash.org/viewBuildError.php?buildid=1410882</a></p>

---

## Post #2 by @TingtingYu (2018-10-26 07:04 UTC)

<p>Got it, thank you for your reply.</p>

---

## Post #3 by @fedorov (2018-10-26 15:10 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="7" data-topic="4496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/radiomics-extension-and-butterworth-filter/4496/7">Radiomics Extension and Butterworth Filter</a></div>
<blockquote>
<p>It’s available for linux 4.10, but there is a build error on windows. <a class="mention" href="/u/joostjm">@JoostJM</a> or <a class="mention" href="/u/jcfr">@jcfr</a> any ideas about this one?</p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1410882">http://slicer.cdash.org/viewBuildError.php?buildid=1410882 </a></p>
</blockquote>
</aside>
<p>This is the first time build started to fail with those errors (<a href="http://b5386721e8162d5a3c07575d3335359039a4a38d">r27508</a>): <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-10-20&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=radiomics" class="inline-onebox">CDash</a></p>
<p>No changes in SlicerRadiomics. There were <a href="https://github.com/Radiomics/pyradiomics/compare/9d992fe96a0876cb5bc4307c7c558727c22918bd...9f4eb6377a524b27a137988e9fe3e023fb889ef3">changes in pyradiomics</a>, but looks like the problem is from a dependency of pyradiomics, which doesn’t look like changed.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> these are the commits in Slicer that might have caused the problem:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3e94f9a6704a658c7f0eee3cb086acd7e210566.png" data-download-href="/uploads/short-url/yNJThMHl6uK47OosAw6RBOzejVc.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3e94f9a6704a658c7f0eee3cb086acd7e210566_2_479x500.png" alt="image" data-base62-sha1="yNJThMHl6uK47OosAw6RBOzejVc" width="479" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3e94f9a6704a658c7f0eee3cb086acd7e210566_2_479x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3e94f9a6704a658c7f0eee3cb086acd7e210566.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3e94f9a6704a658c7f0eee3cb086acd7e210566.png 2x" data-dominant-color="F7F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">705×735 80.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @fedorov (2018-11-05 03:32 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> trying to ping you again - do you have any hints as to what might be wrong here?</p>

---

## Post #5 by @JoostJM (2018-11-05 09:14 UTC)

<p>Hi All,</p>
<p>I haven’t fixed the error yet, but I think I found the cause. Downside is that this resides in a package PyRadiomics depends on (PyWavelets). Follow <a href="https://github.com/Radiomics/SlicerRadiomics/issues/50" rel="nofollow noopener">this issue</a> on the SlicerRadiomics github for updates.</p>

---

## Post #6 by @fedorov (2018-11-05 19:33 UTC)

<p>I think it would be good to know whether this failure is due to any changes in Slicer or configuration of the dashboard. When I looked into this earlier, I did not notice any changes as to how pywavelets or its use from pyradiomics changed in the commits that separated successful builds from failure on the Slicer dashboard. I understand pywavelets is failing, but I do not understand why it started happening.</p>

---

## Post #7 by @fedorov (2018-11-13 15:05 UTC)

<p>Today’s update is that extension build is failing on all platforms: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=radiomics" class="inline-onebox">CDash</a></p>
<p>Response from <a class="mention" href="/u/jcfr">@jcfr</a> in <a href="https://github.com/Radiomics/SlicerRadiomics/issues/50#issuecomment-438296942:" class="inline-onebox">I couldn't find the Radiomics in the 3D Slicer extensions manager · Issue #50 · AIM-Harvard/SlicerRadiomics · GitHub</a></p>
<blockquote>
<p>I am out at a conference today and we will have a look later.</p>
<p>It seems the extensions server is getting overloaded and it will be time to<br>
plan for transitioning away to the new Girder based system.</p>
<p>Note that the backend is ready and we still need to finalize the frontend.</p>
</blockquote>

---

## Post #8 by @lassoan (2018-11-13 16:49 UTC)

<p>All errors seem to happen in package upload step, so it seems that build errors have been resolved!</p>
<p>The extension manager responds, but it is really slow (took several minutes to load the <a href="http://slicer.kitware.com/midas3/slicerappstore/">main page</a>).</p>

---

## Post #9 by @JoostJM (2018-11-14 09:13 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>, I think the error is caused by changes made in the PyWavelets’ source code. As <a class="mention" href="/u/lassoan">@lassoan</a> mentioned, it is a quite complex extension build. I now force the version to &gt; 0.4, &lt;= 1.0.0, which now resolves the build error. Therefore I think some changes were made to the extensions or the build process that didn’t agree with the slicer build platform.</p>

---

## Post #10 by @jcfr (2018-11-14 14:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="4616">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>extension manager responds, but it is really slow</p>
</blockquote>
</aside>
<p>As a temporary fix, we increased the memory allocated to the extension server.</p>

---

## Post #11 by @fedorov (2018-11-14 15:32 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> !</p>
<p><a class="mention" href="/u/tingtingyu">@TingtingYu</a> the Radiomics extension  should now be available for all platforms:</p>
<p><a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=radiomics" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=radiomics</a></p>

---

## Post #12 by @TingtingYu (2018-11-16 06:44 UTC)

<p>Hi Andrey,</p>
<p>Thank you! Great to hear that.</p>
<p>Best,<br>
Tingting</p>

---
