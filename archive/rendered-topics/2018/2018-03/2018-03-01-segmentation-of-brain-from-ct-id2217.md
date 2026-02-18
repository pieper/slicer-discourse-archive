# segmentation of brain from CT 

**Topic ID**: 2217
**Date**: 2018-03-01
**URL**: https://discourse.slicer.org/t/segmentation-of-brain-from-ct/2217

---

## Post #1 by @iplneuro (2018-03-01 13:56 UTC)

<p>Hi,<br>
I am just trying to segment brain from CT. Is there a way to segment brain from CT data or it is possible to segment brain from only MRI. Anyone can help me with this issue.</p>
<p>Thanks in advance,<br>
Suba</p>

---

## Post #2 by @lassoan (2018-03-01 14:19 UTC)

<p>Do you mean you would like to remove the skull? <a href="https://github.com/lorensen/SwissSkullStripperExtension">Swiss Skull Stripper extension</a> should be able to do that completely automatically. The built-in atlas is optimal for MRI, but if you segment a CT manually then you can use that as atlas and may get better results.</p>
<p>See for example the result it gave for the CTBrain sample data set:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/474074be252056ba018d75067b8ea72102ab5770.jpeg" data-download-href="/uploads/short-url/aajZNHI68zyS6GQIiF8mxI2nqso.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/474074be252056ba018d75067b8ea72102ab5770_2_690x373.jpg" alt="image" data-base62-sha1="aajZNHI68zyS6GQIiF8mxI2nqso" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/474074be252056ba018d75067b8ea72102ab5770_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/474074be252056ba018d75067b8ea72102ab5770_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/474074be252056ba018d75067b8ea72102ab5770_2_1380x746.jpg 2x" data-dominant-color="797C86"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 368 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @iplneurosurgery (2018-03-03 05:47 UTC)

<p>Hi,</p>
<p>Thank you for your valuable reply.</p>
<p>I have attached the screen shot of the brain segmented from MRI. Will I be able to segment the brain with those grooves and more detail from CT data.</p>
<p>Thanks and regards,</p>
<p>Suba</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e51a488de3ec88631d3470c4463886453e7f5130.png" data-download-href="/uploads/short-url/wGJEsWhB438Z8pMsnPCQXGiH43u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e51a488de3ec88631d3470c4463886453e7f5130_2_454x500.png" alt="image" data-base62-sha1="wGJEsWhB438Z8pMsnPCQXGiH43u" width="454" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e51a488de3ec88631d3470c4463886453e7f5130_2_454x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e51a488de3ec88631d3470c4463886453e7f5130.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e51a488de3ec88631d3470c4463886453e7f5130.png 2x" data-dominant-color="928575"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">500×550 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2018-03-03 13:17 UTC)

<p>You will not get the same level of detail from CT as from MRI - see below MRI and CT image of the same patient, showing the same image slice:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbe94b7ed37102896dbacb7e2646e74efa575626.jpeg" data-download-href="/uploads/short-url/t5SL1Mo2KjzCeo4GD156tNPuy9g.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbe94b7ed37102896dbacb7e2646e74efa575626_2_690x382.jpg" alt="image" data-base62-sha1="t5SL1Mo2KjzCeo4GD156tNPuy9g" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbe94b7ed37102896dbacb7e2646e74efa575626_2_690x382.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbe94b7ed37102896dbacb7e2646e74efa575626_2_1035x573.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbe94b7ed37102896dbacb7e2646e74efa575626_2_1380x764.jpg 2x" data-dominant-color="4E4E4E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2997×1661 529 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Saima (2019-09-09 04:52 UTC)

<p>Hi andras,<br>
Is it possible to get the brain portion automatically without the cerebellum part of the brain(the back lower brain portion)</p>
<p>thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #6 by @lassoan (2019-09-09 17:41 UTC)

<p>Contrast between cerebellum and other parts of the brain is not very good but you can try to modify the atlas that the skull stripper module uses and see if it can provide the region you need.</p>

---

## Post #7 by @Saima (2019-09-16 14:47 UTC)

<p>How can i modify the atlas. I do not understand this. Could you please tell me how can I change it.</p>

---

## Post #8 by @lassoan (2019-09-17 00:25 UTC)

<p>You can import the atlas labelmap volume node into a segmentation node using Segmentations module, then edit it using Segment Editor module, finally export the segmentation to a labelmap volume node. See segmentation tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">here</a>.</p>

---

## Post #9 by @AbnerxzHe (2019-11-02 02:34 UTC)

<p>Hello,<br>
have you realized the brain extraction on CT? If you can, can you introduce how you do it?<br>
Thank you</p>

---

## Post #10 by @lassoan (2019-11-03 05:04 UTC)

<p>What do you mean by extraction of brain on CT? Would you like to remove the skin and skull from the image?</p>

---

## Post #11 by @AbnerxzHe (2019-11-03 06:56 UTC)

<p>Hello,<br>
Yes, when I do brain CT, I can remove the bone, but I don’t  know how to remove the soft tissue and skin .if you have any good way to  deal with it?<br>
Thank you</p>

---

## Post #12 by @lassoan (2019-11-04 00:05 UTC)

<aside class="quote no-group" data-username="AbnerxzHe" data-post="11" data-topic="2217">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/439d5e/48.png" class="avatar"> AbnerxzHe:</div>
<blockquote>
<p>I can remove the bone, but I don’t know how to remove the soft tissue and skin</p>
</blockquote>
</aside>
<p>Yes, this should be quite straightforward by segmenting the brain by thresholding then separating other soft tissues by margin shrinking, island removal, and margin growing.<br>
See step-by-step instructions in CT skull stripping segmentation recipe here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/" class="inline-onebox">Segmentation recipes for 3D Slicer | 3D Slicer segmentation recipes</a></p>
<p>You can find more segmentation tutorials here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" class="inline-onebox">Documentation/Nightly/Training - Slicer Wiki</a></p>

---

## Post #13 by @AbnerxzHe (2019-11-04 12:51 UTC)

<p>Thank you very much for your help!</p>

---

## Post #14 by @KateDelb (2022-07-08 12:10 UTC)

<p>Dear Andras,</p>
<p>The recipe for CT skull stripping is very helpful, I was wondering if this is implemented in python code as well?</p>

---

## Post #15 by @lassoan (2022-07-09 16:05 UTC)

<p>I’ve implemented the procedure in Python, but then the <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify</a> extension was developed, which does a much better job. Both the old and new method is made available by SlicerMorph extension developers in their <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/SegmentEndocranium/SegmentEndocranium.py">Segment Endocranium module</a>.</p>

---
