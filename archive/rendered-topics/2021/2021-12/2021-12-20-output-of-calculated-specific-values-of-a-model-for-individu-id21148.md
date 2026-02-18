# Output of calculated specific values of a model for individual ROIs

**Topic ID**: 21148
**Date**: 2021-12-20
**URL**: https://discourse.slicer.org/t/output-of-calculated-specific-values-of-a-model-for-individual-rois/21148

---

## Post #1 by @MaKe (2021-12-20 14:57 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11</p>
<p>Hi everyone,</p>
<p>I am currently working with 3D Slicer and would like to output specific values within different ROIs of a calculated model as a mean value. For this I have read in a DICOM dataset (CT images) and created a model using a segmentation. This model contains a calculation of different specific values and results in a 3D color model based on the calculations. Within the calculated model I would like to define individual ROIs and output the specific mean values of the calculated model for these ROIs.</p>
<p>Currently, the output of individual mean values within the ROIs using the Segment Statistics module refers to the original DICOM file. However, my goal is to have the calculated model to be the basis for the output of the individual mean values of an ROI. Is there any way to solve this problem?</p>
<p>Many thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0f520e92d905ca47d68717c9a28126887aef171.png" data-download-href="/uploads/short-url/w648BUkrTsHeQlH1cR4IvcaGjiV.png?dl=1" title="Issue_3DSlicer_Forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0f520e92d905ca47d68717c9a28126887aef171_2_517x279.png" alt="Issue_3DSlicer_Forum" data-base62-sha1="w648BUkrTsHeQlH1cR4IvcaGjiV" width="517" height="279" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0f520e92d905ca47d68717c9a28126887aef171_2_517x279.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0f520e92d905ca47d68717c9a28126887aef171_2_775x418.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0f520e92d905ca47d68717c9a28126887aef171.png 2x" data-dominant-color="CACECC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Issue_3DSlicer_Forum</span><span class="informations">831×449 56.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-12-21 05:20 UTC)

<p>In Segment Statistics module, intensity statistics are computed from voxels of the <code>Scalar volume</code>. You can choose any volume as <code>Scalar volume</code>, it does not have to be the image that was segmented.</p>

---

## Post #3 by @MaKe (2021-12-21 13:22 UTC)

<p>Thank you very much for the quick reply. Is there any way to convert my calculated model into a volume? The information about the calculated specific values (scalars) of the model should be kept when converting to a volume so that it can be output for the individual ROIs.</p>

---

## Post #4 by @lassoan (2021-12-27 13:07 UTC)

<p>You can convert a model into volume by in Data module: right-click on the model and choose to convert to segmentation, then right-click on the segmentation to export to volume.</p>

---

## Post #5 by @MaKe (2022-01-06 16:10 UTC)

<p>Thank you very much Andras. It worked and I was able to convert my model into a volume.</p>

---
