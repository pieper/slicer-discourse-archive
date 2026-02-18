# Refinement of 3D models

**Topic ID**: 12258
**Date**: 2020-06-28
**URL**: https://discourse.slicer.org/t/refinement-of-3d-models/12258

---

## Post #1 by @IanH (2020-06-28 19:36 UTC)

<p>I’ve been using 3Dslicer to segment different tissue types in soybean nodules and am looking to make 3D models for papers that are going to be published. I am the second person to work on this project, and the person who worked before me was able to generate 3D models as well as measure surface area and length of the different tissue types. This information was not shared with me and I’ve been having a bit of trouble generating my own models. I have been able to export .mrb files to .obj files that I have then put into Blender, but this seems to keep the model in slices instead of a full 3D structure. I have use the fill between slices and grow from seeds functions to fill out the segmentation and I am not sure what I am missing. Any help would be appreciated, attached images show what I am seeing. Thank you.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52591cf1d5be2e6634fce9323531c1dfcf6935aa.jpeg" data-download-href="/uploads/short-url/bKu4JPnMO6P0i84D4sTM9pZpNUK.jpeg?dl=1" title="Slicer View.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52591cf1d5be2e6634fce9323531c1dfcf6935aa_2_690x316.jpeg" alt="Slicer View.PNG" data-base62-sha1="bKu4JPnMO6P0i84D4sTM9pZpNUK" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52591cf1d5be2e6634fce9323531c1dfcf6935aa_2_690x316.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52591cf1d5be2e6634fce9323531c1dfcf6935aa_2_1035x474.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52591cf1d5be2e6634fce9323531c1dfcf6935aa_2_1380x632.jpeg 2x" data-dominant-color="9C9FA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer View.PNG</span><span class="informations">1920×881 339 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2020-06-29 04:16 UTC)

<aside class="quote no-group" data-username="IanH" data-post="1" data-topic="12258">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/71c47a/48.png" class="avatar"> IanH:</div>
<blockquote>
<p>I’ve been having a bit of trouble generating my own models. I have been able to export .mrb files to .obj files that I have then put into Blender, but this seems to keep the model in slices instead of a full 3D structure.</p>
</blockquote>
</aside>
<p>MRB file is a packaged scene. If this is something handed over to you from an existing work, it probably contains many different data types, and you are probably not exporting the right data.</p>
<p>In the MRB scene, do you see the whole structure segmented correctly after your fill between slices and grow from the seed effects, if you click the ‘Show 3D’ button? If not, perhaps those tasks didn’t complete correctly.</p>
<p>Process usually goes CT scan → Segmentation → 3D models, of all which can be done in Slicer, including obtaining measurements. Perhaps going through some tutorials with sample data to understand the workflow better before you jump into your data.</p>

---

## Post #3 by @lassoan (2020-07-01 01:31 UTC)

<p>I’ve just noticed on this image that what you exported is the segmentation seed region only. On the Slicer screen I can also see the grown region.</p>
<p>If you have multiple segmentations in the scene, open each of them in Segment Editor module and click Show 3D.</p>
<p>If you have only one segmentation then maybe the “Grow from seeds” effect is in preview mode. Go to Segment Editor module, select “Grow from seeds” effect, and click “Apply” to finalize the segmentation (create the complete segmentation from seeds).</p>
<p>I would recommend this page to get familiar with image segmentation in 3D Slicer: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>

---
