---
topic_id: 18272
title: "Another Extensions Manager Problem"
date: 2021-06-22
url: https://discourse.slicer.org/t/18272
---

# Another Extensions Manager problem

**Topic ID**: 18272
**Date**: 2021-06-22
**URL**: https://discourse.slicer.org/t/another-extensions-manager-problem/18272

---

## Post #1 by @MikaelO (2021-06-22 14:36 UTC)

<p>Hi all,<br>
I have read through posts dealing with Extension Manager problems, but I can’t say I’ve found one with my particular problem (apologies if I’ve overlooked a previosly posted solution).<br>
When I open the extensions manager I get this window:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66840f91baafa08549bde4bd1ded0e141e088698.png" data-download-href="/uploads/short-url/eCTDJW09lWsFF7n5LeKclWR6qRW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66840f91baafa08549bde4bd1ded0e141e088698_2_690x418.png" alt="image" data-base62-sha1="eCTDJW09lWsFF7n5LeKclWR6qRW" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66840f91baafa08549bde4bd1ded0e141e088698_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66840f91baafa08549bde4bd1ded0e141e088698_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66840f91baafa08549bde4bd1ded0e141e088698_2_1380x836.png 2x" data-dominant-color="FCFDFE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1911×1158 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
No menus or other indications that it is loading. The progress bar at the bottom jumps straight to 100% but nothing happens. I’ve left it open for hours to check if it is just loading slowly from <a href="https://slicer.kitware.com/midas3/slicerappstore" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a> but with no result<br>
I have installed three extensions manually, but only the SurfaceWrapSolidify effect actually shows up in the effects box in Segment Editor.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76a4771a2532c848d603d153090b7d5fb0c42f4a.png" data-download-href="/uploads/short-url/gVyHOrkSeblUGBTlLzNksNenZOO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76a4771a2532c848d603d153090b7d5fb0c42f4a_2_690x118.png" alt="image" data-base62-sha1="gVyHOrkSeblUGBTlLzNksNenZOO" width="690" height="118" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76a4771a2532c848d603d153090b7d5fb0c42f4a_2_690x118.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76a4771a2532c848d603d153090b7d5fb0c42f4a_2_1035x177.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76a4771a2532c848d603d153090b7d5fb0c42f4a_2_1380x236.png 2x" data-dominant-color="F3F4FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1907×328 34.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/848a23ff80dac9cfde22be31318acffce73ee2f4.png" alt="image" data-base62-sha1="iUuZrqKg50QgrztsDdtpy3jI028" width="549" height="235"></p>
<p>I’m running Win10 ver.2004<br>
I’m running 3DSlicer 4.11.20210226 r29738 / 7a593c8 (running in administrator mode on my university laptop)</p>
<p>Any ideas would be extremely appreciated</p>
<p>Mikael</p>

---

## Post #2 by @lassoan (2021-06-22 23:56 UTC)

<p>What error messages do you see in the Python console? (Ctrl-3)</p>

---

## Post #3 by @MikaelO (2021-06-23 09:31 UTC)

<p>Hi Andras,<br>
Thanks for the reply</p>
<p>I cant see I’m getting any error message<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6fbe0f5ea52c40778bc5923a58409da4778f83c.png" data-download-href="/uploads/short-url/wXnsT4SMbjr0mdjkQ65Azh1TD6Q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6fbe0f5ea52c40778bc5923a58409da4778f83c_2_603x500.png" alt="image" data-base62-sha1="wXnsT4SMbjr0mdjkQ65Azh1TD6Q" width="603" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6fbe0f5ea52c40778bc5923a58409da4778f83c_2_603x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6fbe0f5ea52c40778bc5923a58409da4778f83c_2_904x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6fbe0f5ea52c40778bc5923a58409da4778f83c_2_1206x1000.png 2x" data-dominant-color="F8FAFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1217×1009 36.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @MikaelO (2021-06-23 11:33 UTC)

<p>Here with a DICOM loaded if that makes any difference</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d0395246bf792d4cad966e0ceed64c4868651be.png" data-download-href="/uploads/short-url/1R7SJnxMcrsVTGizgDBIll8dHm6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d0395246bf792d4cad966e0ceed64c4868651be_2_534x500.png" alt="image" data-base62-sha1="1R7SJnxMcrsVTGizgDBIll8dHm6" width="534" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d0395246bf792d4cad966e0ceed64c4868651be_2_534x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d0395246bf792d4cad966e0ceed64c4868651be_2_801x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d0395246bf792d4cad966e0ceed64c4868651be_2_1068x1000.png 2x" data-dominant-color="EEEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1142×1068 74.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2021-06-23 13:07 UTC)

<p>Do you use any third-party anti-virus software? That may delete some files from the downloaded extension. Or maybe you have run out of space or there were network errors when you installed the extension. Please try uninstalling and installing the extensions again.</p>

---

## Post #6 by @MikaelO (2021-06-24 20:34 UTC)

<p>Hi,<br>
No special anti-virus or anything like that. I have tried reinstalling the extensions but it didn’t help. I installed 3D Slicer on my stationary PC at home, and everything works perfectly.<br>
I’m wondering if the fact that it is running in administrator mode could cause it not to connect with the extensions for some reason. It is a work laptop from my university, so I’m stuck installing programs with administrator access.</p>

---

## Post #7 by @lassoan (2021-06-24 20:50 UTC)

<p>If you use current Slicer versions then you don’t need administrator access to install Slicer. Actually, you don’t even need to install it. You can just copy the entire Slicer folder to a USB stick (from the computer where Slicer is set up correctly) and run Slicer from the USB stick (or copy the files to any writable folder on your work laptop).</p>

---

## Post #8 by @MikaelO (2021-06-24 21:41 UTC)

<p>once installed I can only run Slicer.exe as admin, but I’ll try your idea of copying the slicer folder from the other computer tomorrow. Thanks for the tip</p>

---
