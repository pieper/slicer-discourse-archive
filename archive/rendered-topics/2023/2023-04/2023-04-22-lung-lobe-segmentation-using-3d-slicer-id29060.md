# Lung lobe segmentation using 3D slicer

**Topic ID**: 29060
**Date**: 2023-04-22
**URL**: https://discourse.slicer.org/t/lung-lobe-segmentation-using-3d-slicer/29060

---

## Post #1 by @Rajesh_Ds (2023-04-22 15:25 UTC)

<p>How can I get lung lobe segmentation (into RUL, RML, RLL, LUL and LLL) given a CT volume ? Which is the best method in slicer ? Please let me know.</p>
<p>I want something like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2db470c82b26da376e5da39a3823e62a17044b28.jpeg" data-download-href="/uploads/short-url/6wk4QT6rXIKg2ezzXiTStuZf652.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2db470c82b26da376e5da39a3823e62a17044b28_2_690x406.jpeg" alt="image" data-base62-sha1="6wk4QT6rXIKg2ezzXiTStuZf652" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2db470c82b26da376e5da39a3823e62a17044b28_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2db470c82b26da376e5da39a3823e62a17044b28_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2db470c82b26da376e5da39a3823e62a17044b28_2_1380x812.jpeg 2x" data-dominant-color="C4C3C8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1480×871 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have tried interactive lobe segmentation but it didn’t work.</p>

---

## Post #2 by @pieper (2023-04-22 16:11 UTC)

<aside class="quote quote-modified" data-post="1" data-topic="26710">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-extension-fully-automatic-whole-body-ct-segmentation-in-2-minutes-using-totalsegmentator/26710">New extension: Fully automatic whole-body CT segmentation in 2 minutes using TotalSegmentator</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The <a href="https://github.com/lassoan/SlicerTotalSegmentator#totalsegmentator">TotalSegmentator AI model is now available as an extension for 3D Slicer</a> version 5.2 and above (see installation instructions <a href="https://github.com/lassoan/SlicerTotalSegmentator#setup">here</a>). 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7de17ed588712331572fcd5de59f85ae9f2c9d1.jpeg" data-download-href="/uploads/short-url/uNEukuqDrXUWbSpuiA6BDwYo6Ln.jpeg?dl=1" title="image">[image]</a> 
A large number of AI segmentation models have been developed over the past few years, but <a href="https://github.com/wasserth/TotalSegmentator">TotalSegmentator</a> stands out in several aspects: 


it can segment many structures: 104 anatomical structures (all abdominal organs, bones, larger vessels, muscles)

it is very robust: it can segment any whole-body, abdominal, chest CT images, regardless of image…
  </blockquote>
</aside>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/wasserth/TotalSegmentator">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/wasserth/TotalSegmentator" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/1c4376d4f3fc7d97efd874fde8d335f403a3901c85ddfa9077a23b3f71f0a266/wasserth/TotalSegmentator" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/wasserth/TotalSegmentator" target="_blank" rel="noopener">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of &gt;100...</a></h3>

  <p>Tool for robust segmentation of &gt;100 important anatomical structures in CT images - GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of &gt;100 important anatomical structures in...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @rbumm (2023-04-22 18:06 UTC)

<p>You can use the Lung CT Segmenter, part of Lung CT Analyzer extension, where the TotalSegmentator AI call is implemented for the lobes.</p>

---

## Post #4 by @diazandr3s (2023-04-28 11:10 UTC)

<p>Great answers already.</p>
<p>You could also use the whole-body CT segmentation model available for MONAI Label: <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation" class="inline-onebox" rel="noopener nofollow ugc">model-zoo/models/wholeBody_ct_segmentation at dev · Project-MONAI/model-zoo · GitHub</a></p>
<p>Here are more instructions for using the MONAI Bundle: <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/monaibundle#how-to-use-the-app" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/sample-apps/monaibundle at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>If needed, you could fine-tune the model to your dataset.</p>
<p>Hope this helps,</p>

---
