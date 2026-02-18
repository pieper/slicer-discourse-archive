# Workflow for (Manual, Ground Truth) Segmentations in VFSS

**Topic ID**: 34535
**Date**: 2024-02-26
**URL**: https://discourse.slicer.org/t/workflow-for-manual-ground-truth-segmentations-in-vfss/34535

---

## Post #1 by @Constantine_Zakkarof (2024-02-26 03:37 UTC)

<p>Say, I’d like to create a manual segmentation of a rigid object (hyoid bone) in a videofluorosopic swallowing study (VFSS), which is a 2D time series. This object moves about (with a swallow) and the images are sometimes nosy/blurry.</p>
<p>I’d imagine the optimal workflow starting with creating a segmentation in one frame, copying it as it is to the next frame, then moving/dragging it to the right place, then copying it from the current into the next frame, and so on.</p>
<p>I did search for posts related to copying and transforming segmentations, but the solutions seem to involve quite a lot of interactions for duplicating segments and then interacting with them in 3D view — it would be a painstaking manual process, instead of just copy-to-next, drag, copy-to-next, drag, etc.</p>
<p>Is there anything of this sort that 3D Slicer or any extension can offer?</p>

---

## Post #2 by @lassoan (2024-02-26 03:39 UTC)

<p>See this post about tools used for segmenting 2D time series (ultrasound image sequences):</p>
<aside class="quote quote-modified" data-post="3" data-topic="34526">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/3d-slicer-for-us-segmentation/34526/3">3D slicer for US segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I think segmentation itself is best done outside of Slicer. I used to install TensorFlow and PyTorch in Slicer’s python environment and run segmentation in Slicer, but then it seemed better to run segmentation in everyone’s favorite AI environment, and communicate with Slicer via OpenIGTLink. You can stream the ultrasound images from Slicer or PLUS to an Anaconda environment and receive the segmentations back in Slicer (or whatever your application is) nearly real time. 
I still use Slicer for m…
  </blockquote>
</aside>


---
