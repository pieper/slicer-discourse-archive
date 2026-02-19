---
topic_id: 43650
title: "How To Manually Edit Part Of A Curve After Automatic Generat"
date: 2025-07-08
url: https://discourse.slicer.org/t/43650
---

# how to manually edit part of a curve after automatic generation in 3d slicer?

**Topic ID**: 43650
**Date**: 2025-07-08
**URL**: https://discourse.slicer.org/t/how-to-manually-edit-part-of-a-curve-after-automatic-generation-in-3d-slicer/43650

---

## Post #1 by @LJW (2025-07-08 12:46 UTC)

<p>Hi, I’m currently doing research and not very familiar with 3D Slicer, so I’m posting my question here.</p>
<p>I generated a curve using the following settings:</p>
<ul>
<li><strong>Curve Type</strong>: Shortest distance on surface</li>
<li><strong>Model Node</strong>: Model</li>
<li><strong>Cost function</strong>: Inverse squared</li>
<li><strong>Weighting</strong>: Distance / Curvature</li>
</ul>
<p>Now I want to manually modify part of this curve. However, when I try to add points to adjust the shape, the curve becomes distorted in an unexpected way.</p>
<p>Is there a way to <strong>generate the whole curve with these settings first</strong>, and then <strong>disable those automatic constraints</strong> so I can manually fine-tune or modify certain parts of the curve?</p>

---

## Post #2 by @cpinter (2025-07-08 14:39 UTC)

<p>First of all, I don’t think there is a way currently to add points between any two already defined points, it will always be placed to the end. Make sure you place all control points you need, which later you may move around as you want.</p>
<p>Second, you can turn the surface constraint on and off as you want in the Markups module’s Curve Settings section.</p>
<p>If I misunderstand what you say, some screenshots or a video about that “unexpected distortion” would help.</p>
<p>UPDATE: I see that you posted three questions with images, then removed them, then posted them again with less information. I suggest you re-add those images to facilitate the conversation.</p>

---

## Post #3 by @LJW (2025-07-11 16:12 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ed016830b42f038c13a13269174d465e611e534.png" data-download-href="/uploads/short-url/fOilA5BA3JOSfWR3H2DdHZwCU7O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ed016830b42f038c13a13269174d465e611e534.png" alt="image" data-base62-sha1="fOilA5BA3JOSfWR3H2DdHZwCU7O" width="624" height="189"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">624×189 2.47 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8187a2f9ecfe176074dc7a2f288b47158afb98d5.jpeg" data-download-href="/uploads/short-url/itSc12vdtmZqX1CLaTOIpYBq5Df.jpeg?dl=1" title="스크린샷 2025-07-07 150059" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8187a2f9ecfe176074dc7a2f288b47158afb98d5_2_690x405.jpeg" alt="스크린샷 2025-07-07 150059" data-base62-sha1="itSc12vdtmZqX1CLaTOIpYBq5Df" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8187a2f9ecfe176074dc7a2f288b47158afb98d5_2_690x405.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8187a2f9ecfe176074dc7a2f288b47158afb98d5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8187a2f9ecfe176074dc7a2f288b47158afb98d5.jpeg 2x" data-dominant-color="206F70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2025-07-07 150059</span><span class="informations">902×530 79 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f37395184a7f1e092284d53f7ae061d188d55fad.jpeg" data-download-href="/uploads/short-url/yJFET0UmbBXelXLIrIB7PhSS2EB.jpeg?dl=1" title="스크린샷 2025-07-07 145948" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f37395184a7f1e092284d53f7ae061d188d55fad_2_690x427.jpeg" alt="스크린샷 2025-07-07 145948" data-base62-sha1="yJFET0UmbBXelXLIrIB7PhSS2EB" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f37395184a7f1e092284d53f7ae061d188d55fad_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f37395184a7f1e092284d53f7ae061d188d55fad.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f37395184a7f1e092284d53f7ae061d188d55fad.jpeg 2x" data-dominant-color="216E70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2025-07-07 145948</span><span class="informations">750×465 59.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for your reply. I’m leaving this comment along with the attached image to help clarify the situation.</p>
<p>I’m not trying to turn off the surface constraint entirely. As shown in the screenshot, I configured the Curve Settings using “Shortest distance on surface” and constrained the curve to a model. However, when I try to add a control point to make fine adjustments, the curve becomes distorted, as shown in the image.</p>
<p>Is there a way to preserve the shape of the curve created under these settings, even if I later turn off these settings?</p>
<p>Additionally, I’ve noticed that some of my previous posts were uploaded immediately without going through a pending review process, but those particular posts didn’t seem visible to others — their view counts didn’t increase, and they received no replies. I deleted them thinking there might be a bug. Could you explain the difference between posts that go through a pending review and those that don’t?</p>

---
