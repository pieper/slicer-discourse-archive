# Non-rigid registration between DICOM volume and .stl alias volume

**Topic ID**: 3225
**Date**: 2018-06-19
**URL**: https://discourse.slicer.org/t/non-rigid-registration-between-dicom-volume-and-stl-alias-volume/3225

---

## Post #1 by @DavideBassano (2018-06-19 12:58 UTC)

<p>Hello,</p>
<p>I have a CT volume of a homerus and I have a alias generic humerus (.stl file) that I have to adapt to the CT volume.<br>
So I thought about doing a sort of non-rigid/elastic registration of my alias with the CT volume and then having this new deformed volume, that is very similar to the real homerus from CT data.</p>
<p>Does somebody know how I could do this kind of registration?</p>
<p>Thanks,<br>
Davide</p>

---

## Post #2 by @lassoan (2018-06-19 13:06 UTC)

<p>There are many ways of doing non-rigid warping in Slicer.</p>
<p>Simplest is landmark registration: you mark the same set of anatomical points on the CT and the STL model and use Fiducial registration wizard module in SlicerIGT extension to register the two (there is rigid and non-rigid option).</p>
<p>Another approach is to segment the humerus from the CT using Segment editor, import the model into segmentation node, and then register them automatically using Segment registration extension.</p>

---

## Post #3 by @DavideBassano (2018-06-19 14:10 UTC)

<p>Thanks for your answer Andras.</p>
<p>With Landmark registration I have a problem: I can’t upload my .stl file as a volume. But if I upload it as a model, it works (see figures). So when in Landmark registration module asks for “moving volume” I can’t select the .stl volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77e7c38a5dcc1f17738d6ce4abeea1b3bc6b103f.jpeg" data-download-href="/uploads/short-url/h6JmYY0KzzujEra2AUmTojAAW8D.jpg?dl=1" title="slicer1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77e7c38a5dcc1f17738d6ce4abeea1b3bc6b103f_2_690x387.jpg" alt="slicer1" data-base62-sha1="h6JmYY0KzzujEra2AUmTojAAW8D" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77e7c38a5dcc1f17738d6ce4abeea1b3bc6b103f_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77e7c38a5dcc1f17738d6ce4abeea1b3bc6b103f_2_1035x580.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77e7c38a5dcc1f17738d6ce4abeea1b3bc6b103f_2_1380x774.jpg 2x" data-dominant-color="93919A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer1</span><span class="informations">3258×1832 2.92 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/890cfbe2c435e575225f93b8d75df83852623dd5.jpeg" data-download-href="/uploads/short-url/jypelsWAcg54Shk0AiAETtD9A8d.jpg?dl=1" title="slicer2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/890cfbe2c435e575225f93b8d75df83852623dd5_2_281x500.jpg" alt="slicer2" data-base62-sha1="jypelsWAcg54Shk0AiAETtD9A8d" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/890cfbe2c435e575225f93b8d75df83852623dd5_2_281x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/890cfbe2c435e575225f93b8d75df83852623dd5_2_421x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/890cfbe2c435e575225f93b8d75df83852623dd5_2_562x1000.jpg 2x" data-dominant-color="9B9999"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer2</span><span class="informations">1832×3258 2.88 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/257553afe5bad4b597e7cfdfb45fdd3cb1f9e68e.jpeg" data-download-href="/uploads/short-url/5ln2mAYicj5pOei2RU9dxZUcPqS.jpg?dl=1" title="slicer3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/257553afe5bad4b597e7cfdfb45fdd3cb1f9e68e_2_690x387.jpg" alt="slicer3" data-base62-sha1="5ln2mAYicj5pOei2RU9dxZUcPqS" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/257553afe5bad4b597e7cfdfb45fdd3cb1f9e68e_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/257553afe5bad4b597e7cfdfb45fdd3cb1f9e68e_2_1035x580.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/257553afe5bad4b597e7cfdfb45fdd3cb1f9e68e_2_1380x774.jpg 2x" data-dominant-color="88858D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer3</span><span class="informations">3258×1832 2.76 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1ae47fc867827165e88aa2c6c049bd43f906e7fc.jpeg" data-download-href="/uploads/short-url/3PTYe5kkVDsR4P0M8li1aVgp9YU.jpg?dl=1" title="slicer4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ae47fc867827165e88aa2c6c049bd43f906e7fc_2_281x500.jpg" alt="slicer4" data-base62-sha1="3PTYe5kkVDsR4P0M8li1aVgp9YU" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ae47fc867827165e88aa2c6c049bd43f906e7fc_2_281x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ae47fc867827165e88aa2c6c049bd43f906e7fc_2_421x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ae47fc867827165e88aa2c6c049bd43f906e7fc_2_562x1000.jpg 2x" data-dominant-color="888788"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer4</span><span class="informations">1832×3258 2.83 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then I tried with Segment registration extension: I segmented both the dicom data and the .stl file and keep them in the same segmentation node; I’m not sure what “fixed image” and “moving image” are, but then I performed the registration.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfbac84ca4b89d24c4c7d24a47f3bdf256dd4fe9.jpeg" data-download-href="/uploads/short-url/tDF0Z0wDa5uv0IZDN1JF6HXqTax.jpg?dl=1" title="slicer5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfbac84ca4b89d24c4c7d24a47f3bdf256dd4fe9_2_281x500.jpg" alt="slicer5" data-base62-sha1="tDF0Z0wDa5uv0IZDN1JF6HXqTax" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfbac84ca4b89d24c4c7d24a47f3bdf256dd4fe9_2_281x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfbac84ca4b89d24c4c7d24a47f3bdf256dd4fe9_2_421x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cfbac84ca4b89d24c4c7d24a47f3bdf256dd4fe9_2_562x1000.jpg 2x" data-dominant-color="9B979A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer5</span><span class="informations">1832×3258 2.86 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efa521e6d9d0daa57dfd984a5af76123bbf55375.jpeg" data-download-href="/uploads/short-url/ybZUqaDNy2mctu7h2a5exxkAJ6d.jpg?dl=1" title="slicer6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efa521e6d9d0daa57dfd984a5af76123bbf55375_2_281x500.jpg" alt="slicer6" data-base62-sha1="ybZUqaDNy2mctu7h2a5exxkAJ6d" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efa521e6d9d0daa57dfd984a5af76123bbf55375_2_281x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efa521e6d9d0daa57dfd984a5af76123bbf55375_2_421x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efa521e6d9d0daa57dfd984a5af76123bbf55375_2_562x1000.jpg 2x" data-dominant-color="8F8C8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer6</span><span class="informations">1832×3258 2.76 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is it possible to export the new registrated and warped volume as a file (possibly a .stl)?</p>
<p>Thanks</p>
<p>Davide Bassano</p>

---

## Post #4 by @lassoan (2018-06-19 14:16 UTC)

<aside class="quote no-group" data-username="DavideBassano" data-post="3" data-topic="3225">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/57b2e6/48.png" class="avatar"> DavideBassano:</div>
<blockquote>
<p>Landmark registration module asks for “moving volume”</p>
</blockquote>
</aside>
<p>As I wrote above, for landmark-based registration of a volume and model, use Fiducial registration wizard module in SlicerIGT extension.</p>

---

## Post #5 by @DavideBassano (2018-06-21 12:47 UTC)

<p>Segment registration asks for “volumes” but I don’t have any volumes from my segmentations, I only have models and segmentations. What can I do?</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2018-06-21 15:06 UTC)

<p>Segment registration requires segmentations as input. You can import any model into a segmentation using Segmentations module.</p>

---

## Post #7 by @DavideBassano (2018-06-22 07:21 UTC)

<p>What does “segment registration” give as output after you “perform registration”?<br>
Does it modify the moving segmentation or create a new segmentation?</p>
<p>Thanks</p>

---

## Post #8 by @DavideBassano (2018-06-22 08:07 UTC)

<p>I downloaded SlicerElastix extension. Would it be useful for what I have to do?</p>

---

## Post #9 by @lassoan (2018-06-22 23:56 UTC)

<aside class="quote no-group" data-username="DavideBassano" data-post="7" data-topic="3225">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/57b2e6/48.png" class="avatar"> DavideBassano:</div>
<blockquote>
<p>What does “segment registration” give as output after you “perform registration”?</p>
</blockquote>
</aside>
<p>It computes a transform, which aligns/warps the moving segment to the fixed segment. It does not modify the segment, just puts the moving segment under that transform to show the effect of the transformation. You can then decide to harden that transform (permanently modify the segmentation using that transform), or apply it to other volumes, models, point sets, etc.</p>
<aside class="quote no-group" data-username="DavideBassano" data-post="8" data-topic="3225" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/57b2e6/48.png" class="avatar"> DavideBassano:</div>
<blockquote>
<p>I downloaded SlicerElastix extension. Would it be useful for what I have to do?</p>
</blockquote>
</aside>
<p>SlicerElastix extension is set up to perform intensity-based image registration. I don’t think there is a preset that would work for binary images (that’s how segments are represented as images).</p>

---
