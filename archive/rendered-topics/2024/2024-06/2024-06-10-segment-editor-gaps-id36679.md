---
topic_id: 36679
title: "Segment Editor Gaps"
date: 2024-06-10
url: https://discourse.slicer.org/t/36679
---

# Segment Editor Gaps

**Topic ID**: 36679
**Date**: 2024-06-10
**URL**: https://discourse.slicer.org/t/segment-editor-gaps/36679

---

## Post #1 by @jahong (2024-06-10 11:38 UTC)

<p>Hello,</p>
<p>The segmentation I have been working on has been giving me these weird gaps in a sort of pattern as you can see below. These images were registered in 3d slicer as well, if anyone knows what could be causing this please let me know.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b31b7ab74f8fb5db51c721c9a1e16f472c58f2ec.jpeg" data-download-href="/uploads/short-url/pyslaB6abYQMXefNa0SiqnrCYsk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b31b7ab74f8fb5db51c721c9a1e16f472c58f2ec_2_480x500.jpeg" alt="image" data-base62-sha1="pyslaB6abYQMXefNa0SiqnrCYsk" width="480" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b31b7ab74f8fb5db51c721c9a1e16f472c58f2ec_2_480x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b31b7ab74f8fb5db51c721c9a1e16f472c58f2ec_2_720x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b31b7ab74f8fb5db51c721c9a1e16f472c58f2ec_2_960x1000.jpeg 2x" data-dominant-color="6E746F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1288×1340 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d966ee52c73c4e8d86bd977c775fcee5769e670.jpeg" data-download-href="/uploads/short-url/mu5goD0bShXSH2tU6NRedp51YWc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d966ee52c73c4e8d86bd977c775fcee5769e670_2_522x500.jpeg" alt="image" data-base62-sha1="mu5goD0bShXSH2tU6NRedp51YWc" width="522" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d966ee52c73c4e8d86bd977c775fcee5769e670_2_522x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d966ee52c73c4e8d86bd977c775fcee5769e670_2_783x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d966ee52c73c4e8d86bd977c775fcee5769e670_2_1044x1000.jpeg 2x" data-dominant-color="797A72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1282×1226 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f1f108a1a3aa63103d6fa5cedef2818f072b414.jpeg" data-download-href="/uploads/short-url/bhWh660edch6PTVyKuUw2BIP9Zy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1f108a1a3aa63103d6fa5cedef2818f072b414_2_462x499.jpeg" alt="image" data-base62-sha1="bhWh660edch6PTVyKuUw2BIP9Zy" width="462" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1f108a1a3aa63103d6fa5cedef2818f072b414_2_462x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1f108a1a3aa63103d6fa5cedef2818f072b414_2_693x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1f108a1a3aa63103d6fa5cedef2818f072b414_2_924x998.jpeg 2x" data-dominant-color="63615A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1288×1392 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-10 13:02 UTC)

<p>This is expected when segmenting on oblique slices. See details in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#paint-affects-neighbor-slices-or-stripes-appear-in-painted-segments">documentation</a>.</p>

---

## Post #3 by @jahong (2024-06-16 22:02 UTC)

<p>Hello,</p>
<p>When I segmented these I switched the axis to match to resolve the gaps in the oblique slices, however, now it still seems like the axis may be off, but the axis button is no longer available on the segment editor. Is there another reason this could be/do the axis revert?</p>
<p>There are also some segmentations in this mrml that are associated with different volumes that are like this, and some that have no gaps/separation over slices.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f85be5c624b8a88020c4cf645a26bf112342617.png" data-download-href="/uploads/short-url/2djHNn1AyOnVtI47AqJ1U97TMy3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f85be5c624b8a88020c4cf645a26bf112342617_2_641x500.png" alt="image" data-base62-sha1="2djHNn1AyOnVtI47AqJ1U97TMy3" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f85be5c624b8a88020c4cf645a26bf112342617_2_641x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f85be5c624b8a88020c4cf645a26bf112342617.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f85be5c624b8a88020c4cf645a26bf112342617.png 2x" data-dominant-color="8F98BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">644×502 59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af41d57222c80cb568ac252af63c0a7c68121e74.jpeg" alt="image" data-base62-sha1="p0oBxGgDsNliEb3PVCcthnxztWs" width="624" height="478"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b7b84068544102d6267f864323008be93c1c153.png" data-download-href="/uploads/short-url/6cFa4s2JRtzxIaBUdDKm1g9FAKn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b7b84068544102d6267f864323008be93c1c153_2_681x500.png" alt="image" data-base62-sha1="6cFa4s2JRtzxIaBUdDKm1g9FAKn" width="681" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b7b84068544102d6267f864323008be93c1c153_2_681x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b7b84068544102d6267f864323008be93c1c153_2_1021x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b7b84068544102d6267f864323008be93c1c153.png 2x" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1200×880 81.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2024-06-18 01:42 UTC)

<p>Your image looks highly anisotropic, i.e., distance between slices is huge compared to the size of pixels within a slice. Most likely you have 3 image series like this in the study, in axial, sagittal, coronal orientations.</p>
<p>These kind of studies are barely usable for 3D analysis, but with some effort you may still get out the information you need. You can learn more about this topic here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="5478">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/3d-model-from-dicoms/5478/2">3D model from dicoms</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    First of all, what would you like to segment? Simple thresholding works well in cases when structures of interest have highly distinctive intensity value on the image (bone on CT, contrasted vessels, etc.). If you want to segment bone on MRI then you need to use more sophisticated tools than thresholding. 
Another problem is that, quite often 3 anisotropic MRI images are acquired (high resolution along two axes, very low resolution along a third axis) to reduce time spent in the MRI scanner. How…
  </blockquote>
</aside>


---
