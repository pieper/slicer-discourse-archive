---
topic_id: 22561
title: "Diameter Reduction Using Centerline"
date: 2022-03-17
url: https://discourse.slicer.org/t/22561
---

# Diameter reduction using Centerline

**Topic ID**: 22561
**Date**: 2022-03-17
**URL**: https://discourse.slicer.org/t/diameter-reduction-using-centerline/22561

---

## Post #1 by @Ismael_Aran (2022-03-17 11:57 UTC)

<p>Hi everyone! I do not know if this problem is possible to solve ussing Slicer 3D. But I would be glad if somebody knows about tools or python code that achieves this point.</p>
<p>My objective is to reduce the diameter of the semicircular canals of the inner ear obtained using a MRI. I determined the centerlines successfully as you can see in the .png. Now, I would like to reduce the diameter of these cilinders proportionally and respect to the centerline.</p>
<p>Thank you!<br>
Ismael.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0bae2119598a853781e51cccc79d620b3a9249c.png" data-download-href="/uploads/short-url/ruY4j55IW4wLcdGHicof1g8Ck0Y.png?dl=1" title="centerlines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0bae2119598a853781e51cccc79d620b3a9249c_2_690x499.png" alt="centerlines" data-base62-sha1="ruY4j55IW4wLcdGHicof1g8Ck0Y" width="690" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0bae2119598a853781e51cccc79d620b3a9249c_2_690x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0bae2119598a853781e51cccc79d620b3a9249c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0bae2119598a853781e51cccc79d620b3a9249c.png 2x" data-dominant-color="828BAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">centerlines</span><span class="informations">695×503 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2022-03-17 15:20 UTC)

<p>One easy approach would be to use the “Margin” tool in Segment Editor to shrink the exterior of the object by a given margin.  If your surface currently exists as a model rather than a segmentation, you can first import it to a segmentation using the “Segmentations” module.  I think this approach should do a reasonable job of preserving the centerlines, but to verify you could extract the centerlines of the reduced object and compare to the original centerlines.</p>

---

## Post #3 by @Ismael_Aran (2022-04-05 09:12 UTC)

<p>Hi Mike! Thank you for your advice. I tried to calculate and it works correctly. The problem now is that the Margin tool reduces the diameter by a fixed amount and not proportional to the semicircular canal.</p>
<p>This means that in certain regions it disappears and in others it remains too large as I show in figure. Do you know if it is possible to reduce it proportionally? Perhaps by modifying the code of the Margin tool itself.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e22b0971a4c27b2caea3cb12f8c0d0543cc84d28.jpeg" data-download-href="/uploads/short-url/wgM75SLhJ7xxj03doftzEK5Y4kg.jpeg?dl=1" title="reduction" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e22b0971a4c27b2caea3cb12f8c0d0543cc84d28.jpeg" alt="reduction" data-base62-sha1="wgM75SLhJ7xxj03doftzEK5Y4kg" width="690" height="492" data-dominant-color="9699B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">reduction</span><span class="informations">1076×768 39.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @mau_igna_06 (2022-04-06 00:36 UTC)

<p>May I ask why do you want to achieve this nonlinear shrinkage? What is the clinical problem you are trying to solve?</p>

---

## Post #5 by @Ismael_Aran (2022-04-06 11:58 UTC)

<p>Sure Mauro! My goal is not really a contraction. This type of medical imaging reveals only the bony labyrinth that functions as a cover for the membranous labyrinth that I intend to study. The latter has a smaller diameter (about 20%) and follows the geometry of the bony labyrinth, most of the time in contact with the outer side of the canal, as I show you in the following figure.</p>
<p>This reconstruction was obtained with a microtomography of a dead person that allows much greater precision. I am trying to get closer to living patients to provide personalized diagnosis and treatment. It is expected that in parts where the bony labyrinth has a smaller diameter, the membranous one will also reduce proportionally, so as a first approximation I look for this.</p>
<p>If you have any other ideas on how to get closer to reality, I appreciate it. Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c73d9d4fae7b7f646e552a8f192f64ee10053006.png" data-download-href="/uploads/short-url/sqz1yn19W3nccpZolIqILqpYe6G.png?dl=1" title="posterior_view" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c73d9d4fae7b7f646e552a8f192f64ee10053006_2_690x464.png" alt="posterior_view" data-base62-sha1="sqz1yn19W3nccpZolIqILqpYe6G" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c73d9d4fae7b7f646e552a8f192f64ee10053006_2_690x464.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c73d9d4fae7b7f646e552a8f192f64ee10053006.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c73d9d4fae7b7f646e552a8f192f64ee10053006.png 2x" data-dominant-color="756768"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">posterior_view</span><span class="informations">802×540 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2022-04-06 15:42 UTC)

<p>“Centerline” method can only extract a tree. Since you have rings in your topology you need to use the “network” method. It will give you a network of centerlines, and by applying a tube filter you can specify diameter for it. However, it won’t be very similar to the actual membranous labyrinth shape.</p>
<p>Instead of trying to reconstruct the labyrinth from centerlines, you will have much better results by warping an “atlas” to match image of a specific patient.</p>
<p>The “atlas” consists of an image of the bony labyrinth and the corresponding image or model of the membranous labyrinth. The atlas can be a single patient (you can use the cadaver image that you show above) or you can be constructed by averaging data from a number of similar patients.</p>
<p>You can warp the atlas to the patient fully automatically, by registering the bony labyrinth image of the patient to the bony labyrinth of the atlas (using SlicerElastix or SlicerANTs extension). The result is a warping transform. You can apply that warping transform to the membranous labyrinth model to get the patient-specific membranous labyrinth model (using Transforms module). It takes just a few clicks.</p>

---
