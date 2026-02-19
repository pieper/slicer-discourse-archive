---
topic_id: 22116
title: "Corrupted Slicer Registrationqa Tutorial Data"
date: 2022-02-22
url: https://discourse.slicer.org/t/22116
---

# Corrupted Slicer RegistrationQA tutorial data

**Topic ID**: 22116
**Date**: 2022-02-22
**URL**: https://discourse.slicer.org/t/corrupted-slicer-registrationqa-tutorial-data/22116

---

## Post #1 by @Young_Wang (2022-02-22 15:52 UTC)

<p>Hi 3Dslicer community, I’m going through the Slicer <a href="https://github.com/gsi-biomotion/SlicerRegistrationQA/blob/master/Documentation.md" rel="noopener nofollow ugc">RegistrationQA tutorial</a>.</p>
<p>However, I noticed that some Slicer RegistrationQA tutorial data is corrupted. I am not sure if this issue comes from my OS(mac os 12.2.1) or the uploaded data is actually corrupted. (i.e., I cannot load image2). Could someone confirm that?</p>

---

## Post #2 by @lassoan (2022-02-23 06:28 UTC)

<p>All the data sets load fine for me. Make sure you drag-and-drop the individual files and not the folder (if you load a folder then I think the file will attempted to be loaded as an image sequence).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de0f307d1dc97efc355c49195f88825762fdf3eb.jpeg" data-download-href="/uploads/short-url/vGqxzU7DCrPcuSc0fxDs89JiQZR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de0f307d1dc97efc355c49195f88825762fdf3eb_2_690x419.jpeg" alt="image" data-base62-sha1="vGqxzU7DCrPcuSc0fxDs89JiQZR" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de0f307d1dc97efc355c49195f88825762fdf3eb_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de0f307d1dc97efc355c49195f88825762fdf3eb_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de0f307d1dc97efc355c49195f88825762fdf3eb_2_1380x838.jpeg 2x" data-dominant-color="534E5B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1166 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Young_Wang (2022-02-23 13:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you for your speedy response, I really appreciate it. It works like a charm.<br>
I have a few follow-up questions that I’m not totally clear about.</p>
<ol>
<li>I am not entirely sure what units of those measures/metrics. I wonder if there is a way to report the fiducial pair distance in physical units such as mm?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e6df37b00acc7ad74f20d6b305761cb8affe485.png" data-download-href="/uploads/short-url/8UhaGkOuTulAhucr7RowdDVcqax.png?dl=1" title="Screen Shot 2022-02-23 at 9.35.37 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e6df37b00acc7ad74f20d6b305761cb8affe485_2_690x429.png" alt="Screen Shot 2022-02-23 at 9.35.37 AM" data-base62-sha1="8UhaGkOuTulAhucr7RowdDVcqax" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e6df37b00acc7ad74f20d6b305761cb8affe485_2_690x429.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e6df37b00acc7ad74f20d6b305761cb8affe485.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e6df37b00acc7ad74f20d6b305761cb8affe485.png 2x" data-dominant-color="1A1F23"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-23 at 9.35.37 AM</span><span class="informations">849×529 52.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>in the case where I use fiducial registration wizard to generate a transformation.<br>
how do I save the given transformation into a vector field, specifically what should I pick as the reference volume.</li>
<li>in the case where I use fiducial registration wizard and it gives an RMS error. What should I do to find the TRE in the physical unit given the RMS error is unitless</li>
</ol>
<p>Thank you so much for reading all those questions and your help.</p>

---

## Post #4 by @lassoan (2022-02-23 15:59 UTC)

<aside class="quote no-group" data-username="Young_Wang" data-post="3" data-topic="22116">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar"> Young_Wang:</div>
<blockquote>
<p>I am not entirely sure what units of those measures/metrics. I wonder if there is a way to report the fiducial pair distance in physical units such as mm?</p>
</blockquote>
</aside>
<p>All lengths and distances are reported in world coordinate system unit, which is millimeter by default.</p>
<aside class="quote no-group" data-username="Young_Wang" data-post="3" data-topic="22116">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar"> Young_Wang:</div>
<blockquote>
<p>I use fiducial registration wizard to generate a transformation.<br>
how do I save the given transformation into a vector field, specifically what should I pick as the reference volume</p>
</blockquote>
</aside>
<p>You can choose any volume as reference volume. You can make the region smaller, larger, or make the resolution finer or coarser by using Crop volume module.</p>
<aside class="quote no-group" data-username="Young_Wang" data-post="3" data-topic="22116">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar"> Young_Wang:</div>
<blockquote>
<p>in the case where I use fiducial registration wizard and it gives an RMS error. What should I do to find the TRE in the physical unit given the RMS error is unitless</p>
</blockquote>
</aside>
<p>Both TRE (target regitration error) and RMS (root mean square) are in millimeters. RMS just specifies how a single error value is computed from multiple samples, and so RMS can be used to characterize TRE. However, to compute TRE you need to know the ground truth target locations, which in practice is usually unavailable. So the RMS value that a landmark registration algorithm can give you is the FRE (fiducial registration error).</p>

---

## Post #5 by @Young_Wang (2022-02-23 16:13 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks once again for your speedy and in-depth answers. I truly appreciate that. If I recall correctly from one of the slicer tutorials, the RMS error could be used to quantify TRE, but RMS is a mixture of unknown precision and accuracy.</p>
<p>The issue I’m trying into when saving transformation and visualizing is that the visualized transformation doesn’t seem to be on the correct plane.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8c628e68a07023d72ac8f428492c8422fa5da00.jpeg" data-download-href="/uploads/short-url/sE8341y6DyCavxC1hGap9LTKp32.jpeg?dl=1" title="Screen Shot 2022-02-23 at 12.09.14 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8c628e68a07023d72ac8f428492c8422fa5da00_2_599x500.jpeg" alt="Screen Shot 2022-02-23 at 12.09.14 PM" data-base62-sha1="sE8341y6DyCavxC1hGap9LTKp32" width="599" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8c628e68a07023d72ac8f428492c8422fa5da00_2_599x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8c628e68a07023d72ac8f428492c8422fa5da00_2_898x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8c628e68a07023d72ac8f428492c8422fa5da00_2_1198x1000.jpeg 2x" data-dominant-color="676672"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-23 at 12.09.14 PM</span><span class="informations">1920×1602 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I also wonder, in the case where landmarks registration is used, what is the preferred approach for quantifying the accuracy? i.e step (1) visual confirmation of overlays step(2) calculation of the RMS ?</p>

---

## Post #6 by @lassoan (2022-02-24 05:26 UTC)

<p>If the transform contains a large rigid translation&amp;rotation component then the visualization using a grid is not that helpful. For fiducial registration result visualization it may be more informative if you use <code>Glyph</code> visualization mode and in Advanced → Source Points you select the point list that the transform should move to the correct position (but don’t apply the transform to the point list; if you want to visualize the transformed positions as well then clone the point list and apply the transform to the clone).</p>

---

## Post #7 by @Young_Wang (2022-02-24 15:23 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thank you so much for your advice again. However, I still have trouble with visualizing the transformation shown <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" rel="noopener nofollow ugc">here</a><br>
Here is what I did,<br>
step 1: clone From points<br>
step 2: generate a transform from Fiducial registration wizard<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84f419675473b73ae94c13967008120e35e8e9c7.png" data-download-href="/uploads/short-url/iYa0oc0BswGjXeVqjtleYabExkX.png?dl=1" title="Screen Shot 2022-02-24 at 11.20.10 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f419675473b73ae94c13967008120e35e8e9c7_2_524x500.png" alt="Screen Shot 2022-02-24 at 11.20.10 AM" data-base62-sha1="iYa0oc0BswGjXeVqjtleYabExkX" width="524" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f419675473b73ae94c13967008120e35e8e9c7_2_524x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f419675473b73ae94c13967008120e35e8e9c7_2_786x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f419675473b73ae94c13967008120e35e8e9c7_2_1048x1000.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-24 at 11.20.10 AM</span><span class="informations">1316×1254 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
step 3: select <code>Glyph</code> visualization mode and in Advanced → Source Points you select the point list that the transform<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd52f593a0f854075d36d567b9e6d06ede42c3e4.png" data-download-href="/uploads/short-url/tinCuH0yf5slVz2n1ZkWYE91Qzi.png?dl=1" title="Screen Shot 2022-02-24 at 11.20.37 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd52f593a0f854075d36d567b9e6d06ede42c3e4_2_578x499.png" alt="Screen Shot 2022-02-24 at 11.20.37 AM" data-base62-sha1="tinCuH0yf5slVz2n1ZkWYE91Qzi" width="578" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd52f593a0f854075d36d567b9e6d06ede42c3e4_2_578x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd52f593a0f854075d36d567b9e6d06ede42c3e4_2_867x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd52f593a0f854075d36d567b9e6d06ede42c3e4_2_1156x998.png 2x" data-dominant-color="F0F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-24 at 11.20.37 AM</span><span class="informations">1304×1128 90.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
step 4: apply the transform on the cloned lists</p>
<p>Results:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9af52efa29ce3b922f7090318a3287238d40aee7.jpeg" data-download-href="/uploads/short-url/m6OPGGxMGJMKv251p8iYU5wLGCz.jpeg?dl=1" title="Screen Shot 2022-02-24 at 11.21.48 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9af52efa29ce3b922f7090318a3287238d40aee7_2_647x500.jpeg" alt="Screen Shot 2022-02-24 at 11.21.48 AM" data-base62-sha1="m6OPGGxMGJMKv251p8iYU5wLGCz" width="647" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9af52efa29ce3b922f7090318a3287238d40aee7_2_647x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9af52efa29ce3b922f7090318a3287238d40aee7_2_970x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9af52efa29ce3b922f7090318a3287238d40aee7_2_1294x1000.jpeg 2x" data-dominant-color="3E3E4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-02-24 at 11.21.48 AM</span><span class="informations">1960×1514 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can see the cloned list moved to desired locations but I can’t see the arrows indicating the transformation</p>

---
