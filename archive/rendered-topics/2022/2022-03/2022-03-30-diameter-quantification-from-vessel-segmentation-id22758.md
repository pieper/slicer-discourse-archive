# Diameter quantification From vessel segmentation

**Topic ID**: 22758
**Date**: 2022-03-30
**URL**: https://discourse.slicer.org/t/diameter-quantification-from-vessel-segmentation/22758

---

## Post #1 by @Adela_Garcia (2022-03-30 09:20 UTC)

<p>I have already segmented vessel and bone, an d get a segment with only the vessel, now I would like to quantify the <strong>diameters</strong> of the vessels in this segment. Do you known how I can to get it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/574f7441b12cf297125234efd7f55b99658237d3.jpeg" data-download-href="/uploads/short-url/csnLIo3UkeMQkROByViUPaluvPt.jpeg?dl=1" title="SUM_Segmentation.seg-labeled-skeletons" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/574f7441b12cf297125234efd7f55b99658237d3_2_251x500.jpeg" alt="SUM_Segmentation.seg-labeled-skeletons" data-base62-sha1="csnLIo3UkeMQkROByViUPaluvPt" width="251" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/574f7441b12cf297125234efd7f55b99658237d3_2_251x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/574f7441b12cf297125234efd7f55b99658237d3_2_376x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/574f7441b12cf297125234efd7f55b99658237d3.jpeg 2x" data-dominant-color="0A0A0A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SUM_Segmentation.seg-labeled-skeletons</span><span class="informations">404×803 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @chir.set (2022-03-30 10:25 UTC)

<p>You can use ‘Extract centerline’ module followed by ‘Cross-section analysis’ in SlicerVMTK extension for this kind of task.</p>
<p>However, your segmentation is highly complex. It’s advisable to analyse targeted small portions of your segmentation, within reach of reasoning on the results.</p>

---
