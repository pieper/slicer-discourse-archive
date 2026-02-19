---
topic_id: 24818
title: "How Can I Segment T1W Mri And Produce Its Image Mask"
date: 2022-08-18
url: https://discourse.slicer.org/t/24818
---

# How can I segment T1W MRI and produce its image mask?

**Topic ID**: 24818
**Date**: 2022-08-18
**URL**: https://discourse.slicer.org/t/how-can-i-segment-t1w-mri-and-produce-its-image-mask/24818

---

## Post #1 by @das (2022-08-18 11:40 UTC)

<p>I currently have a task at hand which has been challenging for me. I wish to produce a mask image (to be in .nii format) from a T1-weighted image (which is in .nii format and containing a glioma region). Before producing this image, I wish to segment the image into:</p>
<ol>
<li>White matter</li>
<li>Grey matter</li>
<li>CSF</li>
<li>Tumour (if possible, with peritumoral edema region)</li>
</ol>
<p>I would be very glad to get your recommendations and suggestions on the best way this task could be done with 3D slicer. I would not mind articles and lectures notes.</p>
<p>By the way, is it possible to also extract out only CSF regions and save as xxx.nii?</p>
<p>Many thanks in advance.</p>

---

## Post #2 by @pieper (2022-08-18 14:48 UTC)

<p>I don’t think there’s an off-the-shelf automated way of doing all of that currently, but if anybody knows of one I hope they will post here.</p>
<p>There are several pieces available and with a bit of manual work you can put together a nice segmentation.</p>
<p>For example the models trained on <a href="http://braintumorsegmentation.org/">BraTS</a> are getting very good at tumor and edema.  E.g. <a href="https://github.com/razeineldin/DeepSeg">this one has been made available for Slicer</a>.  Other tools like <a href="https://github.com/BBillot/SynthSeg">SynthSeg</a> are very good at non-tumor brain segmentation (including CSF).  You can manually combine the results of these and fix errors with the Segment Editor and extract CSF masks and other structures.</p>

---

## Post #3 by @ebrahim (2022-08-18 16:17 UTC)

<p>I don’t know what Slicer offers for this task directly, but here is an approach I have taken before using <a href="https://github.com/ANTsX/ANTsPy" rel="noopener nofollow ugc">antspy</a> <a href="https://antspy.readthedocs.io/en/latest/segmentation.html?highlight=prior_based_segmentation#ants.prior_based_segmentation" rel="noopener nofollow ugc">prior-based segmentation</a>. Below is a sketch of the code to give the idea; I haven’t tested this code directly.</p>
<pre data-code-wrap="py"><code class="lang-nohighlight">import ants

# This method of segmentation uses registration to
# an atlas that comes with a known segmentation
# I have used SRI24 in the past: https://www.nitrc.org/projects/sri24/

# Load atlas
atlas_img = ants.image_read(path_to_T1_atlas)
atlas_csf_img = ants.image_read(path_to_csf_segment_of_atlas)
atlas_gm_img = ants.image_read(path_to_gm_segment_of_atlas)
atlas_wm_img = ants.image_read(path_to_wm_segment_of_atlas)

# Load input image
img = ants.image_read(path_to_input_image)

# Run N4 bias correction
img_n4 = ants.n4_bias_field_correction(img)

# Register to atlas
img_reg = ants.registration(atlas_img, img_n4)

# create mask to restrict the segmentation inside this region
priors = [atlas_csf_img, atlas_gm_img, atlas_wm_img]
mask = priors[0].copy()
mask_view = mask.view()
for i in range(1, len(priors)):
    mask_view[priors[i].numpy() &gt; 0] = 1
mask_view[mask_view &gt; 0] = 1

# Do prior-based segmentation
seg = ants.prior_based_segmentation(img_reg, priors, mask)

# Take csf label
seg_img_view = seg['segmentation'].view()
csf_img = seg['segmentation'].copy()
csf_img_view = feature_img.view()
csf_img_view.fill(0)
csf_img_view[seg_img_view == 1] = 1  # 1 is the CSF label

# Write to nifti file
ants.image_write(csf_img, "csf_mask.nii.gz")
</code></pre>

---
