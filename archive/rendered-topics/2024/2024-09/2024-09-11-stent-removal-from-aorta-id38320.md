---
topic_id: 38320
title: "Stent Removal From Aorta"
date: 2024-09-11
url: https://discourse.slicer.org/t/38320
---

# Stent removal from aorta

**Topic ID**: 38320
**Date**: 2024-09-11
**URL**: https://discourse.slicer.org/t/stent-removal-from-aorta/38320

---

## Post #1 by @Ngodachongan (2024-09-11 00:56 UTC)

<p>Hi all,<br>
I’m trying to remove the stent from the aorta using CTA DICOM data. The aim is to build a 3D model of only the aortic lumen (without stent).<br>
Is there any quick way to achieve this?<br>
Thanks and have a good day!<br>
An Ngo</p>

---

## Post #2 by @chir.set (2024-09-11 09:07 UTC)

<aside class="quote no-group" data-username="Ngodachongan" data-post="1" data-topic="38320">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ngodachongan/48/66421_2.png" class="avatar"> Ngodachongan:</div>
<blockquote>
<p>build a 3D model of only the aortic lumen (without stent)</p>
</blockquote>
</aside>
<p>This is a tough exercise since there are artefacts and the lumen is heterogeneous even with contrast. Your required precision will determine if the method below fits in your research.</p>
<p>The module ‘Guided vein segmentation’ can segment the lumen inside the stent as shown below. You must install SlicerVMTK from the extensions manager. Segment each branch inside the stent if it’s bifurcated, then merge them using the ‘Logical operators’ effect of the ‘Segment editor’.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d16e4ded740c0dfd5a78316d64fef28a8a8bc283.gif" alt="aorta_endo_00" data-base62-sha1="tSI7hmBMlZSVDybqA1MUXFu4K9Z" width="308" height="499" class="animated"></p>
<p>The final result will include some metallic surroundings and some calcifications. You may further slightly shrink the merged segment, still there will be some overlaps.</p>
<p>It doesn’t really ‘remove’ a stent, but make a best good looking segmentation. If you remove the metallic parts by thresholding the image data itself or in a segmentation, what should be put in place? It’s generally a single intensity value and the resulting volume is full of ‘holes’. Try that with the ‘Threshold scalar volume’ module.</p>

---

## Post #4 by @Ngodachongan (2024-09-12 06:58 UTC)

<p>Thank you so much for your reply.</p>
<p>Do you have any guide for using the Guided Vein Segmentation?<br>
I’m trying to figure out but it doesn’t work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33e117cce4c0d81b90ce587781f83468277ddd3a.jpeg" data-download-href="/uploads/short-url/7oWBQB4VvyM0CcEshIxDfoxZv9E.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33e117cce4c0d81b90ce587781f83468277ddd3a_2_690x371.jpeg" alt="image" data-base62-sha1="7oWBQB4VvyM0CcEshIxDfoxZv9E" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33e117cce4c0d81b90ce587781f83468277ddd3a_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33e117cce4c0d81b90ce587781f83468277ddd3a_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33e117cce4c0d81b90ce587781f83468277ddd3a_2_1380x742.jpeg 2x" data-dominant-color="6C6D6C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1035 83.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best wishes,<br>
An Ngo</p>

---

## Post #5 by @chir.set (2024-09-12 07:09 UTC)

<aside class="quote no-group" data-username="Ngodachongan" data-post="4" data-topic="38320">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ngodachongan/48/66421_2.png" class="avatar"> Ngodachongan:</div>
<blockquote>
<p>any guide</p>
</blockquote>
</aside>
<p>For any module in Slicer, there is a ‘Help and acknowledgement’ collapsible button where developers point to the online project page.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb08ec5ff80933a79c14e4ddd9ff090984e81f27.png" alt="help_button" data-base62-sha1="sY82LHxe8a1As3i3Q8lp1yYpTbF" width="548" height="166"></p>
<p>For <a href="https://github.com/vmtk/SlicerExtension-VMTK/" rel="noopener nofollow ugc">this</a> module, you must draw an open curve inside the lumen of your stent and provide it as input.</p>

---

## Post #6 by @Ngodachongan (2024-09-12 08:10 UTC)

<p>Thanks a lot for your help. I finally made it. It really time saving since I have more than 150 cases to segment for CFD run.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad6c88811912d142149b677eb175d77efe19a6bb.png" data-download-href="/uploads/short-url/oKb8i5IduRh2ImR9kLTlK7Z8s6D.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad6c88811912d142149b677eb175d77efe19a6bb_2_252x500.png" alt="image" data-base62-sha1="oKb8i5IduRh2ImR9kLTlK7Z8s6D" width="252" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad6c88811912d142149b677eb175d77efe19a6bb_2_252x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad6c88811912d142149b677eb175d77efe19a6bb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad6c88811912d142149b677eb175d77efe19a6bb.png 2x" data-dominant-color="A6A8A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">281×556 38.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Have a nice day!</p>

---
