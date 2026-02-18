# Contrast Control in DRR Generation Module

**Topic ID**: 26527
**Date**: 2022-12-01
**URL**: https://discourse.slicer.org/t/contrast-control-in-drr-generation-module/26527

---

## Post #1 by @fieldr4 (2022-12-01 04:01 UTC)

<p>I am attempting to create clinical-quality simulated XRs of the lumbar spine using the <code>DRR Generation</code> module. Unfortunately, my application prevents me from using the volume renderer for DRR generation.</p>
<p>I have selected realistic SID, SAD, and imager values, but the resulting images have very poor contrast. Here are two examples. I exported them from Slicer as .mha files and then converted them to .png files using ImageJ.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a57a8b278b1761ea6967faaa89895041bb72f421.jpeg" data-download-href="/uploads/short-url/nBTkwqvsc4DBsRsIVDFpXMzxk1H.jpeg?dl=1" title="563_DRR_Coronal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a57a8b278b1761ea6967faaa89895041bb72f421_2_500x500.jpeg" alt="563_DRR_Coronal" data-base62-sha1="nBTkwqvsc4DBsRsIVDFpXMzxk1H" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a57a8b278b1761ea6967faaa89895041bb72f421_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a57a8b278b1761ea6967faaa89895041bb72f421_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a57a8b278b1761ea6967faaa89895041bb72f421_2_1000x1000.jpeg 2x" data-dominant-color="AEAEAE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">563_DRR_Coronal</span><span class="informations">1920×1920 80.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a8dfd886fdf81885e7e84654aec1bd8e31e0bb1.jpeg" data-download-href="/uploads/short-url/cV5bufSLG3cyVl0LOBkoWo1M9ix.jpeg?dl=1" title="563_DRR_Sagittal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a8dfd886fdf81885e7e84654aec1bd8e31e0bb1_2_500x500.jpeg" alt="563_DRR_Sagittal" data-base62-sha1="cV5bufSLG3cyVl0LOBkoWo1M9ix" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a8dfd886fdf81885e7e84654aec1bd8e31e0bb1_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a8dfd886fdf81885e7e84654aec1bd8e31e0bb1_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a8dfd886fdf81885e7e84654aec1bd8e31e0bb1_2_1000x1000.jpeg 2x" data-dominant-color="CBCBCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">563_DRR_Sagittal</span><span class="informations">1920×1920 47.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Does anyone have any recommendations?</p>
<p>I am unable to crop the CT volume to remove some of the soft tissues because the coordinates of the CT are not in LPS (thanks <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/mik">@Mik</a> for helping me figure that out). I can fix the original CT’s coordinate reference frame, but when I create a new cropped volume from it the resulting volume’s coordinate reference frame is not correct for the <code>DRR Generation</code> module.</p>
<p>Is there a way to threshold the original CT volume without creating a new volume?</p>

---
