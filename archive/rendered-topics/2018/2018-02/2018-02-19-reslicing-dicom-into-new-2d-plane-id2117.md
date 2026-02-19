---
topic_id: 2117
title: "Reslicing Dicom Into New 2D Plane"
date: 2018-02-19
url: https://discourse.slicer.org/t/2117
---

# Reslicing DICOM into new 2D plane

**Topic ID**: 2117
**Date**: 2018-02-19
**URL**: https://discourse.slicer.org/t/reslicing-dicom-into-new-2d-plane/2117

---

## Post #1 by @etesta (2018-02-19 16:01 UTC)

<p>Hello,  looking to use Slicer to take 2D dicom CT images, convert to a 3D model, and reslice in a different plane (I.e. plane of scapula) . Does anyone know if this sort of feature is supported by Slicer?<br>
Thank you</p>

---

## Post #2 by @ihnorton (2018-02-19 16:05 UTC)

<blockquote>
<p>convert to a 3D model, and reslice in a different plane</p>
</blockquote>
<p>I’m not sure about reslicing a 3D model (ie a mesh), but Slicer can reslice a 3D <strong>volume</strong> in an arbitrary plane. I’m not sure where this is in the documentation so I took a screenshot of the widget:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46b2cd636b0c8ade3923ca16d75fa9d5fb1390fb.png" data-download-href="/uploads/short-url/a5qvjyM2LY6B77Yy6oMrWrD4HdV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46b2cd636b0c8ade3923ca16d75fa9d5fb1390fb_2_666x500.png" alt="image" data-base62-sha1="a5qvjyM2LY6B77Yy6oMrWrD4HdV" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46b2cd636b0c8ade3923ca16d75fa9d5fb1390fb_2_666x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46b2cd636b0c8ade3923ca16d75fa9d5fb1390fb_2_999x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46b2cd636b0c8ade3923ca16d75fa9d5fb1390fb.png 2x" data-dominant-color="A09ECC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1034×776 33.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2018-02-19 17:45 UTC)

<p>You can reslice a model by showing slice intersections in the slice view (you can show model slice intersection in Models module Display section).</p>

---

## Post #4 by @etesta (2018-02-19 19:52 UTC)

<p>Thank you both.</p>
<p>Once I use the widget, I can drag it in the 3D model to alter slices. Instead, is there a way to alter the planes in my 2D images, such as a reformat widget for each plane in the 2D model.</p>
<p>As you can see in my attachment, I have the slice intersections set. I’d like to ideally drag each color in axial, sag, or coronal to set my desired planes.Any help would be greatly appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fbe40aae0aaa12f9fef708b8b0b6824a40cf107.jpeg" data-download-href="/uploads/short-url/95TH5sK2hKF5dgPVbpWcdAGUVLx.jpg?dl=1" title="example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fbe40aae0aaa12f9fef708b8b0b6824a40cf107_2_690x436.jpg" alt="example" data-base62-sha1="95TH5sK2hKF5dgPVbpWcdAGUVLx" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fbe40aae0aaa12f9fef708b8b0b6824a40cf107_2_690x436.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fbe40aae0aaa12f9fef708b8b0b6824a40cf107_2_1035x654.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3fbe40aae0aaa12f9fef708b8b0b6824a40cf107_2_1380x872.jpg 2x" data-dominant-color="7B7C9E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">example</span><span class="informations">1455×921 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2018-02-19 21:23 UTC)

<p>You can move slices in the 2D or 3D views by holding down Shift key while moving the mouse. You can show the cursor position in all views by clicking on crosshair icon the toolbar.</p>

---

## Post #6 by @Steve_Yang (2019-12-19 14:01 UTC)

<p>Excuse me , I need you help .</p>
<p>I got new slice successfully by used your method , but I want to export to DICOM from these new slice .</p>
<p>How can I save these Slice of new 2D plane ?</p>

---

## Post #7 by @lassoan (2019-12-19 14:30 UTC)

<aside class="quote no-group" data-username="Steve_Yang" data-post="6" data-topic="2117">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/steve_yang/48/4231_2.png" class="avatar"> Steve_Yang:</div>
<blockquote>
<p>I got new slice successfully by used your method , but I want to export to DICOM from these new slice .</p>
</blockquote>
</aside>
<p>This can be done, but it should not be needed (DICOM viewers do it themselves, research software can read standard research image file formats). Why would you like to save a reformatted slice to DICOM?</p>

---

## Post #8 by @Steve_Yang (2019-12-20 04:16 UTC)

<p>Thank you for your kind response.<br>
It will be used for data augmentation in deep learning.<br>
That is why I need to save it as a new DICOM set with different tilt/altitude angle.</p>

---

## Post #9 by @lassoan (2019-12-20 15:36 UTC)

<p>You don’t need to use DICOM as input for deep learning. You can export the DICOM directly into formats that can be read much more efficiently.</p>

---

## Post #10 by @BobbyZhang26 (2020-11-21 07:15 UTC)

<p>Hi, could you tell me the name of this widget? I am using Slicer version 4.11 and i cannot find this icon. Are there any extensions I should install? Many thanks</p>

---
