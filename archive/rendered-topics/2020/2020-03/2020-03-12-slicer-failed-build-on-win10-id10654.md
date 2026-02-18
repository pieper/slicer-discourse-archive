# Slicer failed build on win10

**Topic ID**: 10654
**Date**: 2020-03-12
**URL**: https://discourse.slicer.org/t/slicer-failed-build-on-win10/10654

---

## Post #1 by @Dyatsen (2020-03-12 07:31 UTC)

<p>Hello,</p>
<p>I followed the Build Instructions to build Slicer on Windows 10.<br>
CMake: 3.15.0<br>
Git: 2.25.1<br>
Qt: 5.10.0 64-bit (MSVC 2015)<br>
Visual Studio 2015<br>
After BUILD Slicer in Visual Studio, 42 errors occurred.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a99bcde55d1f386236b1cf18c65c8bfdd2f6f4ac.png" data-download-href="/uploads/short-url/ocqv6ivRwMOKtEbSJdGyOfbDz4g.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a99bcde55d1f386236b1cf18c65c8bfdd2f6f4ac.png" alt="image" data-base62-sha1="ocqv6ivRwMOKtEbSJdGyOfbDz4g" width="655" height="500" data-dominant-color="DCE0E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">942×719 52.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could someone tell me how to solve these errors? Thanks!</p>

---

## Post #2 by @Dyatsen (2020-03-12 11:37 UTC)

<p>In addition, this is the second time I build the same Slicer.sln in S4D folder. At the first time, I remember there were not so many errors (I don’t remember exactly), and I was able to run slicer.exe in slicer-build folder. But when I built the RUN_TESTS project, errors occurred. So I suppose I failed to build Slicer at the first time and built it for this second time. I don’t know whether this matters.</p>

---

## Post #3 by @Dyatsen (2020-03-12 16:10 UTC)

<p>It seems that I click the build button instead of the rebuild button to make so many errors. I just rebuilt the slicersln. Although there are not so many errors, there is still one:</p>
<p>C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets 171: error MSB6006: “cmd.exe” exited with code 1.</p>
<p>The executable Slicer.exe in Slicer-build was regenerated and it can run. But many files are failed to be loaded:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc36cbcffa52789b461607804e9d2ba542060c63.png" data-download-href="/uploads/short-url/vq6rvyfuIMO2hpFEDtuv1EIkQnx.png?dl=1" title="20200313000455" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc36cbcffa52789b461607804e9d2ba542060c63_2_202x500.png" alt="20200313000455" data-base62-sha1="vq6rvyfuIMO2hpFEDtuv1EIkQnx" width="202" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc36cbcffa52789b461607804e9d2ba542060c63_2_202x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc36cbcffa52789b461607804e9d2ba542060c63_2_303x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dc36cbcffa52789b461607804e9d2ba542060c63_2_404x1000.png 2x" data-dominant-color="1A1A1A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20200313000455</span><span class="informations">979×2418 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could someone tell me how to solve that error? Or does it mean that the build has been completed? Thanks!</p>

---

## Post #4 by @cpinter (2020-03-12 16:18 UTC)

<p>The build error you see may just mean that a resource file cannot be overwritten, so it might be harmless. I usually ignore these kind of errors as long as there are no other ones, and SlicerApp-real.exe is generated.</p>
<p>The errors you see on startup is due to a problem with a certain revision, and it has been fixed since then. Please update your Slicer source code, build, and it will work.</p>

---

## Post #5 by @kejuhn (2021-01-26 06:24 UTC)

<p>How to ignore these errors ?</p>

---

## Post #6 by @lassoan (2021-01-26 13:12 UTC)

<p>You can only ignore warnings (by simply not doing anything with them) but errors must be fixed because otherwise your build will be incomplete. Instead of reviving this old thread, I would recommend to create a new topic with whatever problem you have, unless it seems to be the same root cause of build error as this.</p>

---
