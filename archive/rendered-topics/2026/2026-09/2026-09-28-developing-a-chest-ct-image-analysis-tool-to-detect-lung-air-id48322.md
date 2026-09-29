---
topic_id: 48322
title: "Developing a chest CT image analysis tool to detect lung airway obstruction"
date: 2026-09-28
url: https://discourse.slicer.org/t/48322
last_bumped: 2026-09-28T14:01:26.687Z
---

# Developing a chest CT image analysis tool to detect lung airway obstruction

**Topic ID**: 48322
**Date**: 2026-09-28
**URL**: https://discourse.slicer.org/t/developing-a-chest-ct-image-analysis-tool-to-detect-lung-airway-obstruction/48322

---

## Post #1 by @pspsps (2026-09-28 13:47 UTC)

<p>I am thinking of developing an chest CT image analysis tool to detect obstruction (narrowing) of central airways of the lung (trachea to lobar bronchii, perhaps also segmental bronchii). I will be thankful for any advice one may have regarding two strategies that I have thought of for doing so.</p>
<p>There are many causes for such obstructions, such as foreign bodies, but my interest is in cancer/tumor-associated obstruction. The cancer can arise within airways (intrinsic) or outside (extrinsic) or can be mixed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3504b33e5c6d62e9d8c71ff7f1bd59a993c84ac.jpeg" data-download-href="/uploads/short-url/wqUpGSwRlKBupYHnm9PXmG6dAmg.jpeg?dl=1" title="airway_tree" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3504b33e5c6d62e9d8c71ff7f1bd59a993c84ac_2_345x245.jpeg" alt="airway_tree" data-base62-sha1="wqUpGSwRlKBupYHnm9PXmG6dAmg" width="345" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3504b33e5c6d62e9d8c71ff7f1bd59a993c84ac_2_345x245.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3504b33e5c6d62e9d8c71ff7f1bd59a993c84ac_2_517x367.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3504b33e5c6d62e9d8c71ff7f1bd59a993c84ac_2_690x490.jpeg 2x" data-dominant-color="E0E0E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">airway_tree</span><span class="informations">800×570 95.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60b004a4be77ef7a3266830d36262977e9315c52.jpeg" data-download-href="/uploads/short-url/dNkXah7YAemB3l5wtXl7lKA7qwy.jpeg?dl=1" title="pictures" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60b004a4be77ef7a3266830d36262977e9315c52_2_518x500.jpeg" alt="pictures" data-base62-sha1="dNkXah7YAemB3l5wtXl7lKA7qwy" width="518" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60b004a4be77ef7a3266830d36262977e9315c52_2_518x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60b004a4be77ef7a3266830d36262977e9315c52_2_777x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60b004a4be77ef7a3266830d36262977e9315c52_2_1036x1000.jpeg 2x" data-dominant-color="BFB3AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pictures</span><span class="informations">1500×1447 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>One strategy</strong> is to use Slicer with TotalSegmenter to segment the airway tree. Since I am interested in only the proximal (large) airways, I expect the segmentation step to work well. Centerlines of the airway tree and airway cross-sectional areas along them will be derived and examined with some mathematical logic to identify possible locations of obstruction, such as a larger gradient in reduction of lumen area as one moves from distally along the airway tree.</p>
<p>The <strong>second strategy</strong> is to develop a neural network (NN) model. Airway lumens in 2D images (axial CT slices) covering trachea to lobar/segmental bronchi will be manually segmented for annotation as obstructed or not. Because of the airway segments’ orientations, the segmented areas may be oval, elliptical or tubular. A single CT scan series is expected to give 30-100 (depending on CT slice thickness) 2D images with airway lumens segmented only a fraction of which will be annotated as obstruction. The final set of a few thousand 2D images from 50-100 patients will be used to train an NN.</p>
<p>But I am not sure if this is the correct approach for training an NN model. Should some tissue surrounding obstructed airway segments be included in the segmentation along with the airway lumen? Should 3D and not 2D data be used for training? Also, is this problem even amenable to NN modeling?</p>

---

## Post #2 by @ebrahim (2026-09-28 14:01 UTC)

<p>The problem is definitely amenable to NN modeling, I think, if you have enough data and annotations.</p>
<p>I would expect TotalSegmentator to work well, but it is worth checking by trying it on some of your most pathological cases. ML models can handle the particular data domain they are trained on, and it is not certain whether the existence of tumors or other obstructions could cause issues with the segmentation. (Maybe someone else has an intuition for this.)</p>
<p>A 3D U-Net is going to be larger than a 2D one, but it will have more capacity for segmenting 3D images such as CT scans and doing so to produce consistent segmentations from slice-to-slice.</p>
<p>If you want to train your own, you could consider nnUNet: <a href="https://github.com/mic-dkfz/nnunet" class="inline-onebox">GitHub - MIC-DKFZ/nnUNet · GitHub</a></p>
<p>It has 2D (slice by slice) and 3D training configurations so it would not be hard to try both (with the same 3D input files being supplied regardless, which is convenient).</p>
<blockquote>
<p>Should some tissue surrounding obstructed airway segments be included in the segmentation along with the airway lumen?</p>
</blockquote>
<p>That IDK about but I think one advantage of training your own model is that you get to make these decisions based on what suits your needs. A deep U-Net is able to learn large scale features such as the possible shapes of airways while also taking into account finer image intensity and texture-like features as well to handle small details like obstructions – so my guess is that both approaches will work and it is up to what you want.</p>

---
