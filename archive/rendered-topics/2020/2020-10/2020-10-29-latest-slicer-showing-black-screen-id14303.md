# Latest Slicer showing black screen

**Topic ID**: 14303
**Date**: 2020-10-29
**URL**: https://discourse.slicer.org/t/latest-slicer-showing-black-screen/14303

---

## Post #1 by @drvarunagarwal (2020-10-29 11:04 UTC)

<p>Hi,</p>
<p>I am  using slicer version 4.11.20200930 on windows 10 Pro version 2004 - 64 bit</p>
<p>with latest drivers running on macbook pro intel core i5-4288U @ 2.60GHz, 8.00 GB ram, Intel  Iris graphics 5100 (driver date 15-05-2020 and version 20.19.15.5144)</p>
<p>Monitor is LED TV (not routine computer monitor as the display of this laptop is spoilt)</p>
<p>I am just getting a black screen after launching slicer.</p>
<p>on random clicks some functions work.</p>
<p>Earlier version with older driver was working fine. However since I update my driver and slicer I am getting this problem.</p>
<p>I can’t get this solved based on other similar problems on forum with earlier versions of slicer.</p>
<p>Please guide and advise</p>
<p>many thanks</p>

---

## Post #2 by @lassoan (2020-10-30 04:43 UTC)

<p>We need to balance between supporting old hardware and have good performance on modern hardware. We aim for having Slicer running on computers released in the past 5 years. See some more information about system requirements here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements</a></p>
<p>Since i5-4288U was released in 2013, we don’t actively support this hardware anymore, which means we cannot spend time trying to investigate and resolve compatibility issues.</p>

---

## Post #3 by @drvarunagarwal (2020-11-02 08:05 UTC)

<p>Hi,</p>
<p>Actually my system is dual boot.<br>
On the same hardware slicer is working fine on Mac OS.</p>
<p>However when I boot into windows 10 it doesn’t work.<br>
I get only black screen.</p>
<p>Please advise</p>
<p>many thanks</p>

---

## Post #4 by @jamesobutler (2020-11-02 13:07 UTC)

<p>Can you provide a full screenshot of it not working on Windows 10?</p>

---

## Post #5 by @lassoan (2020-11-02 14:12 UTC)

<aside class="quote no-group" data-username="drvarunagarwal" data-post="3" data-topic="14303">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drvarunagarwal/48/8914_2.png" class="avatar"> drvarunagarwal:</div>
<blockquote>
<p>On the same hardware slicer is working fine on Mac OS.</p>
</blockquote>
</aside>
<p>Things break not because the hardware suddenly stops working but because of driver incompatibilities, which are different for each operating system.</p>
<p>4th Gen Intel (Haswell) chipset support in VTK (Slicer’s rendering engine) was a topic of discussion about 3-4 years ago (<a href="https://vtkusers.public.kitware.narkive.com/yDHSNMOZ/is-dvtk-rendering-backend-opengl-needed-for-haswell-with-7-0-0">1</a>, <a href="https://groups.google.com/g/vmtk-users/c/-Ttcmf2ffJg">2</a>). Incompatibilities already started to show up then, but one could ask developers for help because those systems were just a couple of years old. Since now only a very small fraction of VTK users have computers with 4th Gen Intel chipsets, you cannot rely on mainstream free support, but you would need to pay for custom support (e.g., to Kitware). Probably even just the investigation of the problem would cost $2000-3000 and you might need to pay a lot more for a fix, and it may take time to develop that fix and get it into Slicer.</p>
<p>It is of course possible that the issue is something that can be fixed at Slicer level or with some configuration/driver tuning and based on his comment above, maybe <a class="mention" href="/u/jamesobutler">@jamesobutler</a> is willing to spend some time with figuring it out. But overall, it is probably much faster and less expensive to upgrade your hardware than spending time/money with this investigation.</p>

---

## Post #6 by @drvarunagarwal (2020-11-03 06:19 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dfe6048f041c20c66f4758b7d9341ebb7000090.jpeg" data-download-href="/uploads/short-url/4hkQnZByzuFlD1rP8CPkAtJf636.jpeg?dl=1" title="IMG_0276" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dfe6048f041c20c66f4758b7d9341ebb7000090_2_666x500.jpeg" alt="IMG_0276" data-base62-sha1="4hkQnZByzuFlD1rP8CPkAtJf636" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dfe6048f041c20c66f4758b7d9341ebb7000090_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dfe6048f041c20c66f4758b7d9341ebb7000090_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dfe6048f041c20c66f4758b7d9341ebb7000090_2_1332x1000.jpeg 2x" data-dominant-color="124387"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_0276</span><span class="informations">4032×3024 1.96 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e38bfe8c7b47e05974f9a8a4e01431484f7516c9.jpeg" data-download-href="/uploads/short-url/wsYjYMi3jqtcyD9ANsGPbhQeYg9.jpeg?dl=1" title="IMG_0277" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e38bfe8c7b47e05974f9a8a4e01431484f7516c9_2_666x500.jpeg" alt="IMG_0277" data-base62-sha1="wsYjYMi3jqtcyD9ANsGPbhQeYg9" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e38bfe8c7b47e05974f9a8a4e01431484f7516c9_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e38bfe8c7b47e05974f9a8a4e01431484f7516c9_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e38bfe8c7b47e05974f9a8a4e01431484f7516c9_2_1332x1000.jpeg 2x" data-dominant-color="235E97"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_0277</span><span class="informations">4032×3024 2.9 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Please see the attached files<br>
I get a black screen<br>
and<br>
On random clicks sometimes I get menus like these.</p>
<p>I am using a LED TV rather than a regular monitor.<br>
Can it be because of that?</p>
<p>Please guide</p>

---
