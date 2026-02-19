---
topic_id: 37604
title: "Get Segment Node Contour By Drr Metrix"
date: 2024-07-29
url: https://discourse.slicer.org/t/37604
---

# Get Segment Node contour by DRR metrix

**Topic ID**: 37604
**Date**: 2024-07-29
**URL**: https://discourse.slicer.org/t/get-segment-node-contour-by-drr-metrix/37604

---

## Post #1 by @fqzhice (2024-07-29 08:45 UTC)

<p>I segment bone and vessel, then run DRR registration and get matrix. Later I just want  get bone contour in DRR projected plane and chagned it by manually, such as mouse move, rotation, how can i do this?</p>

---

## Post #2 by @lassoan (2024-07-29 09:29 UTC)

<aside class="quote no-group" data-username="fqzhice" data-post="1" data-topic="37604">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/7bcc69/48.png" class="avatar"> fqzhice:</div>
<blockquote>
<p>then run DRR registration</p>
</blockquote>
</aside>
<p>What is “DRR registration” registration of 3D CT to a 2D x-ray image? Do you perform it in Slicer or in some other software?</p>
<p>If you want to get the contour of the projection of the bones then you can use the 3D view for that: render the bones without shading (either as a segmented model; or directly the CT volume using volume rendering) and set the view background to black.</p>

---

## Post #3 by @fqzhice (2024-07-29 10:32 UTC)

<p>I generated drr image by drrgenerator in Slicer to make registration of 3D CT to DSA.<br>
Then want to render bone contour in DRR projected/DSA plane. Doctors will rotate or move the vr image slightlly by mouse if necessary. Also bone contour will also re-projected again<br>
I will try according your suggestion<br>
Thanks very much!</p>

---

## Post #4 by @lassoan (2024-07-29 11:48 UTC)

<p>If you use volume rendering then you can edit the opacity transfer function to emphasize bone edges.</p>

---

## Post #5 by @fqzhice (2024-07-30 03:36 UTC)

<p>Yea!<br>
I convert bone segment node to labelmap and render in volume rendering module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3ba64cd81703313360f45b09e579c859ecf387b6.png" data-download-href="/uploads/short-url/8vGsY2ym9cRTmVi8DnInLvWAs9U.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba64cd81703313360f45b09e579c859ecf387b6_2_690x327.png" alt="image" data-base62-sha1="8vGsY2ym9cRTmVi8DnInLvWAs9U" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba64cd81703313360f45b09e579c859ecf387b6_2_690x327.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba64cd81703313360f45b09e579c859ecf387b6_2_1035x490.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3ba64cd81703313360f45b09e579c859ecf387b6_2_1380x654.png 2x" data-dominant-color="51524B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1840×872 44.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This maybe can fulfill our requirement.  but i cant do it segment module now<br>
The slicer main version is 5.4</p>
<p>This is philips product and i think is more better<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b94d5c1a1fcd1d458816d4083a9ecd31ed7552d0.jpeg" data-download-href="/uploads/short-url/qrg4CHnkNrFikLKe6O1a0GEvoBO.jpeg?dl=1" title="1722310697050" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b94d5c1a1fcd1d458816d4083a9ecd31ed7552d0.jpeg" alt="1722310697050" data-base62-sha1="qrg4CHnkNrFikLKe6O1a0GEvoBO" width="690" height="421" data-dominant-color="54443E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1722310697050</span><span class="informations">969×592 58.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @fqzhice (2024-07-30 05:30 UTC)

<p>Thanks for your help  <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
