---
topic_id: 35885
title: "I Want To Count Number Of Voxel Pixel"
date: 2024-05-03
url: https://discourse.slicer.org/t/35885
---

# I want to count number of voxel/pixel

**Topic ID**: 35885
**Date**: 2024-05-03
**URL**: https://discourse.slicer.org/t/i-want-to-count-number-of-voxel-pixel/35885

---

## Post #1 by @Vikram (2024-05-03 08:05 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a9e5ed76a03380caab27cbe2e1d94dd388e120e.png" data-download-href="/uploads/short-url/aE6DG7vDKS29cRnIflPnQW7Ymom.png?dl=1" title="pixel" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a9e5ed76a03380caab27cbe2e1d94dd388e120e_2_690x352.png" alt="pixel" data-base62-sha1="aE6DG7vDKS29cRnIflPnQW7Ymom" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a9e5ed76a03380caab27cbe2e1d94dd388e120e_2_690x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a9e5ed76a03380caab27cbe2e1d94dd388e120e_2_1035x528.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a9e5ed76a03380caab27cbe2e1d94dd388e120e_2_1380x704.png 2x" data-dominant-color="D3D3EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pixel</span><span class="informations">1879×961 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
hi after segment i need to count number of pixel of hole and lattice when i click on segment statics there no any obsent to calculate volume and pixel</p>

---

## Post #2 by @rfenioux (2024-05-03 08:15 UTC)

<p>It looks like there is an error with the segment statistics module. It should not be empty. Are there any error messages in the python console?</p>

---

## Post #3 by @Vikram (2024-05-03 08:40 UTC)

<p>then what i can do any suggestion for me</p>

---

## Post #4 by @cpinter (2024-05-03 08:46 UTC)

<aside class="quote no-group" data-username="rfenioux" data-post="2" data-topic="35885">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rfenioux/48/70007_2.png" class="avatar"> rfenioux:</div>
<blockquote>
<p>Are there any error messages in the python console?</p>
</blockquote>
</aside>
<p>This is the next step. Please look in the Python console for red text. If you find it, copy paste it here.</p>

---

## Post #5 by @Vikram (2024-05-03 08:51 UTC)

<p>i am new user where i can find python console</p>

---

## Post #6 by @rfenioux (2024-05-03 08:57 UTC)

<p>You can use this button<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5957ebfe83ad4d78b5030fd78b0ce512b9d7b1a5.png" alt="image" data-base62-sha1="cKmRJ5QSS1k4RxUSiMYBHlYYHyZ" width="391" height="220"></p>
<p>Or this menu that does the same thing<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f06c284b34020348f138e97de33ca068655ee0d3.png" alt="image" data-base62-sha1="yiSjMtHr8XOTpA6j4ZiKSojitKr" width="375" height="241"></p>

---

## Post #7 by @Vikram (2024-05-03 10:38 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/467dfc6caea1b528b5e53641548d628a8ebc7dfe.png" data-download-href="/uploads/short-url/a3BluXl0TTGyDwiysAElsBOrfUa.png?dl=1" title="px" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/467dfc6caea1b528b5e53641548d628a8ebc7dfe_2_690x352.png" alt="px" data-base62-sha1="a3BluXl0TTGyDwiysAElsBOrfUa" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/467dfc6caea1b528b5e53641548d628a8ebc7dfe_2_690x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/467dfc6caea1b528b5e53641548d628a8ebc7dfe_2_1035x528.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/467dfc6caea1b528b5e53641548d628a8ebc7dfe_2_1380x704.png 2x" data-dominant-color="C0BCB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">px</span><span class="informations">1903×972 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
hello can any body help me to explain the parameter , which one is whole volume , i need volume of segmented structure and also overall volume, any body can help to explain these parameter</p>

---

## Post #8 by @muratmaga (2024-05-03 15:38 UTC)

<p>Please read the Segment Statistics module documentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">Segment statistics — 3D Slicer documentation</a></p>
<p>What is reported is the volume of the segmentation you generated. You need to define what “total volume” is (i.e., volume of the whole imaging grid, volume of the segmentation if the inside is filled etc)…</p>

---

## Post #9 by @Vikram (2024-05-06 01:56 UTC)

<p>i read actually I want to calculate volume and number of pixel of both lattice ( wall) in segmented and also hole(air) in segmented image<br>
i applied segment statics but result only gave lattice volume not air</p>

---

## Post #10 by @muratmaga (2024-05-06 03:09 UTC)

<aside class="quote no-group" data-username="Vikram" data-post="9" data-topic="35885">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/e47774/48.png" class="avatar"> Vikram:</div>
<blockquote>
<p>segment statics but result only gave lattice volume not air</p>
</blockquote>
</aside>
<p>Segment Statistics can only calculate statistics for the region you segmented. If you need the volume of air. You need to segment that as a separate structure.</p>

---

## Post #11 by @Vikram (2024-05-06 03:15 UTC)

<p>Yeah I tried to segment but I did not can any one help me to segment air to volume of air</p>

---

## Post #12 by @muratmaga (2024-05-06 04:17 UTC)

<p>It is very simple, you just need to lower your threshold that will pick air, and make sure you that you donot overwrite the voxels already assigned to lattice.</p>
<p>The main issue, there is no enclosing area to limit the extend of air around lattice, it is continuous with outside. I would probably create ROI that spans the limits of lattice, and then use the local threshold to threshold only within that ROI.</p>

---

## Post #13 by @Vikram (2024-05-06 08:26 UTC)

<p>i did get sir , what you mean</p>

---

## Post #14 by @Vikram (2024-05-07 04:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79c163db1be304175dbfd045c3b190ea8fcb657c.png" data-download-href="/uploads/short-url/hn66PGRiI6YEY9sx5pZySWFnDAg.png?dl=1" title="air" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c163db1be304175dbfd045c3b190ea8fcb657c_2_690x357.png" alt="air" data-base62-sha1="hn66PGRiI6YEY9sx5pZySWFnDAg" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c163db1be304175dbfd045c3b190ea8fcb657c_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c163db1be304175dbfd045c3b190ea8fcb657c_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79c163db1be304175dbfd045c3b190ea8fcb657c_2_1380x714.png 2x" data-dominant-color="C2CBD6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">air</span><span class="informations">1884×976 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
when i segment air from cubic , and also adjust threshold , but the segmented image of cubic like that i also attached , why segmentation of air include some parts of lattice ?<br>
what is the reason behind this can anyone please told me</p>

---

## Post #15 by @muratmaga (2024-05-07 04:47 UTC)

<p>You need to create a new segment and set the editable area to outside of.segment_1 (which should be the lattice)</p>

---

## Post #16 by @Vikram (2024-05-07 09:04 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/453a39b48a42110ee119f5ecace458203a02408c.png" data-download-href="/uploads/short-url/9SpGXewjvWph39YdkoCpSQPee4s.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453a39b48a42110ee119f5ecace458203a02408c_2_690x355.png" alt="image" data-base62-sha1="9SpGXewjvWph39YdkoCpSQPee4s" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453a39b48a42110ee119f5ecace458203a02408c_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453a39b48a42110ee119f5ecace458203a02408c_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/453a39b48a42110ee119f5ecace458203a02408c_2_1380x710.png 2x" data-dominant-color="CEC9BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1884×970 225 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
there is a lot of parameter  . i need overall volume of air(segment2)  and overall volume of lattice (segment1), which parameter i can take for volume in this data (volume LM) OR VOLUME CS.<br>
I read documentation but i did not get .<br>
can any one tell me please</p>

---
