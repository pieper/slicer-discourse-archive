---
topic_id: 5491
title: "Build Errors Nightly Version"
date: 2019-01-24
url: https://discourse.slicer.org/t/5491
---

# Build errors nightly version

**Topic ID**: 5491
**Date**: 2019-01-24
**URL**: https://discourse.slicer.org/t/build-errors-nightly-version/5491

---

## Post #1 by @siaeleni (2019-01-24 00:47 UTC)

<p>Hello,</p>
<p>I am trying to build Slicer at my laptop, Win 10 while I follow nightly instructions from slicer documentation for Release mode. But I got the following errors:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78e6a5fba3512e90b64f3e40175661a705610d14.png" data-download-href="/uploads/short-url/hfxspK0i8odDytk0J454m9M4mPy.png?dl=1" title="errors" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78e6a5fba3512e90b64f3e40175661a705610d14_2_690x359.png" alt="errors" data-base62-sha1="hfxspK0i8odDytk0J454m9M4mPy" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78e6a5fba3512e90b64f3e40175661a705610d14_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78e6a5fba3512e90b64f3e40175661a705610d14_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78e6a5fba3512e90b64f3e40175661a705610d14_2_1380x718.png 2x" data-dominant-color="C2C7CD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">errors</span><span class="informations">3771×1967 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Do you have any idea how can I solve that issue?<br>
Thanks</p>

---

## Post #2 by @jamesobutler (2019-01-24 01:07 UTC)

<p>I see in your Visual Studio window that the configuration is currently specified as “Release”, but your build tree is called “C:/S4D/…” which seems to indicate that you want a “Debug” configuration. Did you previously start a build as debug and are now doing a release build?</p>
<p>According to the Slicer build instructions <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows_2" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows_2</a> you cannot use the same build tree for both release and debug builds.</p>
<p>Otherwise I suggest making sure you have fetched and pulled all the latest commits from Github for Slicer’s master branch. If all else fails, clearing out your S4D directory and trying again should fix it.</p>

---

## Post #3 by @siaeleni (2019-01-24 01:42 UTC)

<p>Thanks for the response.<br>
No, I didn’t start to build in debug, only at release.<br>
Sure, I am going to try again and let you know if I will have the same issue.</p>

---

## Post #4 by @jcfr (2019-01-24 04:55 UTC)

<p>I suggest you first close Visual Studio (currently open with the top-level solution) and instead open the solution file <code>C:\s4d\Slilcer-build\Slicer.sln</code>, then you wlll be able to build again, this should report a more informative message.</p>

---

## Post #5 by @siaeleni (2019-01-24 14:42 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>  I built that sln and I got the follwoing:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59e945835204c3a8ba0bfdaa78094d65e5b8cb1b.png" data-download-href="/uploads/short-url/cPoha83EgDaBlbSyOncoxO1XXF9.png?dl=1" title="imgs" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59e945835204c3a8ba0bfdaa78094d65e5b8cb1b_2_690x362.png" alt="imgs" data-base62-sha1="cPoha83EgDaBlbSyOncoxO1XXF9" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59e945835204c3a8ba0bfdaa78094d65e5b8cb1b_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59e945835204c3a8ba0bfdaa78094d65e5b8cb1b_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59e945835204c3a8ba0bfdaa78094d65e5b8cb1b_2_1380x724.png 2x" data-dominant-color="B3B8BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imgs</span><span class="informations">3788×1989 374 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @pieper (2019-01-24 14:58 UTC)

<p>Also interesting is that <a class="mention" href="/u/siaeleni">@siaeleni</a> told me that her slicer build does run (using Slicer-build\Slicer.exe), but those build errors at the top level persist.</p>

---

## Post #7 by @siaeleni (2019-01-24 15:08 UTC)

<p>I tried to build again the top level sln after a lot of tries and got it finally.<br>
I don’t know why, but seems that has no errors now.  Note, that I didn’t change any setting at my laptop.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/939dd383fb233112697c5287ad9df3fd2cefcb11.png" data-download-href="/uploads/short-url/l3SkpPo6L7rOkKk2ZYkXNgt4Mwx.png?dl=1" title="imgfinal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/939dd383fb233112697c5287ad9df3fd2cefcb11_2_690x349.png" alt="imgfinal" data-base62-sha1="l3SkpPo6L7rOkKk2ZYkXNgt4Mwx" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/939dd383fb233112697c5287ad9df3fd2cefcb11_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/939dd383fb233112697c5287ad9df3fd2cefcb11_2_1035x523.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/939dd383fb233112697c5287ad9df3fd2cefcb11_2_1380x698.png 2x" data-dominant-color="B7BCC2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imgfinal</span><span class="informations">3784×1918 350 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @pieper (2019-01-24 16:48 UTC)

<p>That’s good news anyway <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=6" title=":+1:" class="emoji" alt=":+1:"></p>
<p>I still suspect it’s an antivirus or similar issue that locks some of the files at random.</p>

---

## Post #9 by @lassoan (2019-01-24 21:23 UTC)

<p>I usually get errors similar to those top-level errors (launcher icon cannot be updated, etc.) when I have a Slicer instance running.</p>

---
