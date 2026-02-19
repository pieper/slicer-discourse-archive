---
topic_id: 578
title: "Fetal Lung Volume Calculation"
date: 2017-06-27
url: https://discourse.slicer.org/t/578
---

# Fetal lung volume calculation

**Topic ID**: 578
**Date**: 2017-06-27
**URL**: https://discourse.slicer.org/t/fetal-lung-volume-calculation/578

---

## Post #1 by @Egor (2017-06-27 09:41 UTC)

<p>What module should I use to calculate the volume of the fetal lungs? Is there any guide for it? I want to measure it by subtracting mediastinal volume from total thoracic volume.</p>

---

## Post #2 by @lassoan (2017-06-27 11:22 UTC)

<p>Segment the structures using Segment editor and compute volumes using Segment statistics module.</p>

---

## Post #3 by @ihnorton (2017-06-27 12:00 UTC)

<p>See also</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://chestimagingplatform.org/profiles/openscholar/themes/hwpi_basetheme/favicon.png" class="site-icon" width="32" height="32">
      <a href="https://chestimagingplatform.org/" target="_blank">chestimagingplatform.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://chestimagingplatform.org/" target="_blank">Chest Imaging Platform (CIP)</a></h3>

<p>Chest Imaging Platform (CIP)</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Egor (2017-08-04 11:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dea550ce25f132620fe6f395b23779074e8ce04d.png" data-download-href="/uploads/short-url/vLCbvm9EOL1seAFya9RcRtNGY45.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dea550ce25f132620fe6f395b23779074e8ce04d_2_690x387.png" alt="image" data-base62-sha1="vLCbvm9EOL1seAFya9RcRtNGY45" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dea550ce25f132620fe6f395b23779074e8ce04d_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/dea550ce25f132620fe6f395b23779074e8ce04d_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dea550ce25f132620fe6f395b23779074e8ce04d.png 2x" data-dominant-color="C0C5D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 257 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How can I smooth the edges?</p>
<p>Which of the volumes is correct? LM? GS?</p>

---

## Post #5 by @lassoan (2017-08-04 13:08 UTC)

<p>The main problem with this segmentation is that it is created from a volume that has spacing between slices that is about 10x larger than pixel spacing within a slice. Use <code>Crop Volume</code> module to resample the volume with isotropic voxel size by checking <code>Isotropic spacing</code> checkbox and selecting <code>B-spline</code> interpolation. It is also advisable to set the region of interest to be just slightly larger than your region of interest (crop the rest of the volume to reduce memory need and processing time during segmentation).</p>
<p>After this, segment the lungs again. It seems that contrast between lungs and surrounding structures are quite good, so you may can segment very quickly and accurately using <code>Grow from seeds</code> effect or <code>Watershed</code> effect (to get <code>Watershed</code> effect, install <code>SegmentEditorExtraEffects</code> extension).</p>
<p>Difference between LM and GS volume is that GS only considers that region that is included in both the segment and the selected grayscale volume node. Usually the grayscale volume contains the whole segment and so the LM and GS volumes are the same.</p>

---

## Post #6 by @pieper (2017-08-04 13:31 UTC)

<p>Also it appears that the fetal lungs moved during the acquisition, leading to the stair-step appearance of the segmentation.  It’s possible that the volume calculation from the labelmap is fairly accurate even if the 3D reconstruction is not anatomically correct.</p>

---

## Post #7 by @lassoan (2017-08-04 15:26 UTC)

<p>Good point, Steve. At first look, it seemed to me that the staircase artifacts are due to large slice spacing, but maybe you are right that it’s due to motion. Either way, resampling to isotropic voxel size will not hurt.</p>
<p>You may reduce staircase artifacts by using <code>Smoothing</code> effect. Try different smoothing methods and parameters and browse through slices to check how well the smoothed segment matches the organ’s shape. If they are not good (not smooth enough or oversmoothed), then you can just undo the smoothing and try with different method or parameter setting.</p>

---

## Post #8 by @Egor (2017-08-07 07:10 UTC)

<p>Thank you very much!</p>

---
