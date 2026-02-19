---
topic_id: 23152
title: "Combine Two Volumes Into One Using Python"
date: 2022-04-27
url: https://discourse.slicer.org/t/23152
---

# combine two volumes into one using python

**Topic ID**: 23152
**Date**: 2022-04-27
**URL**: https://discourse.slicer.org/t/combine-two-volumes-into-one-using-python/23152

---

## Post #1 by @Katya_Stansfield (2022-04-27 15:05 UTC)

<p>Hi, I need to automate combining two volumes into one. I have DICOM files of whole body CT scans of a body, split into parts. The parts overlap slightly. My aim is to be able to quickly merge the torso and legs to obtain one volume for segmentation. Manually, slicer provides a chance to ‘add’ two volumes arithmetically, as long as one of the volumes has been extended to include the size of the other.</p>
<p>Following this logic, I need to script:</p>
<p>a. ‘cropping’ the torso volume to a larger region of interest so that it includes legs,<br>
b. cropping the leg volume to the lowest point of the Z coordinates in the torso volume to avoid overlap,<br>
c. adding two cropped volumes to make one,<br>
d. pushing the new volume to the slicer.</p>
<p>Thanks to discussions here and to previously published code, the problem does not seem impossible to solve. However, I cannot see an answer for defining XYZ boundaries of my regions of interest. Can you help, please?</p>

---

## Post #2 by @lassoan (2022-04-27 15:18 UTC)

<p>You can use Crop volume module to create an ROI that fits the volume, adjust it manually so that it includes the entire region that you are interested in, then created the “cropped” output (it will be actually larger than the input volume). You can then use image "Resample Scalar/Vector/DWI Volume<code>module with the "cropped" output volume chosen as</code>Reference volume` to get all the images in the same voxel coordinate space.</p>

---

## Post #3 by @Katya_Stansfield (2022-04-27 15:59 UTC)

<p>Hi, thanks for the reply but I need to avoid manual adjustment. It needs to be precise, based on coordinates of the volumes’ top and bottom. Can it be done programmatically?</p>

---

## Post #4 by @pieper (2022-04-28 12:08 UTC)

<p>Yes, this can certainly be done by scripting.  Look at the code in CropVolume and you’ll see how to get the bounds of volumes in RAS space and how ROIs are manipulated.  Make a new volume big enough for all the parts and copy or add the data into it.  You can decide how to deal with any overlaps, maybe crop on side to fit the other.  This problem doesn’t come up that often so there’s no module for it, but if you come up with some code please post to help the next person.</p>

---

## Post #5 by @mikebind (2022-04-28 16:41 UTC)

<p>Here is a link to a module I created to do this: <a href="https://github.com/mikebind/SlicerStitchImageVolumes" class="inline-onebox">GitHub - mikebind/SlicerStitchImageVolumes: A 3D Slicer (slicer.org) module for stitching together multiple image volumes into a single larger image volume.</a>  The ROI still needs to be created manually because for my workflows it was helpful to be able to cut out large regions of non-patient present in the full scans, but I think this will do everything else you want.</p>
<p>Let me know if you run into problems.  It was created a while back, so it initially was set up to use the legacy AnnotationROI objects for the ROI, but I believe it has been updated to work equally well with the newer MarkupsROI objects.</p>

---

## Post #6 by @lassoan (2022-04-28 16:55 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> The module looks very useful. The image stitching has come up a number of times on the forum, so it could make sense to make it available for users via the extension manager. You could consider <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#distribute-an-extension">submitting the extension to the extensions index</a> but if you find that too much work or looks like too big of a commitment to provide and support an extension, then you can add the module to the <a href="https://github.com/PerkLab/SlicerSandbox#slicersandbox">Sandbox extension</a>. It contains many experimental modules that are already useful but still incomplete or may need a bit of more polishing.</p>

---

## Post #7 by @mikebind (2022-04-28 17:43 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, I will try to add it to the Sandbox extension soon.  I think it isn’t really polished enough for a standalone extension (it should be more configurable), but it is also useful as is, so that sounds like a good place for it to end up.</p>

---

## Post #8 by @Katya_Stansfield (2022-04-28 18:10 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> – thank you for the code, really appreciated!</p>

---

## Post #9 by @Katya_Stansfield (2022-04-29 08:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, may I return please to the markup ROI? I am playing with this option and it is great in Slicer. However, when trying the script (’ Fit markups ROI to volume’ from script repository) through a Jupiter notebook, the ROI is created but fitting fails. Why so?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eae6f91da2e1db9e28375fb96783bf0368b8f82.jpeg" data-download-href="/uploads/short-url/kmdwIWZpimsRsMg57zYkAAu3rIC.jpeg?dl=1" title="Screenshot 2022-04-29 091615" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8eae6f91da2e1db9e28375fb96783bf0368b8f82_2_471x500.jpeg" alt="Screenshot 2022-04-29 091615" data-base62-sha1="kmdwIWZpimsRsMg57zYkAAu3rIC" width="471" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8eae6f91da2e1db9e28375fb96783bf0368b8f82_2_471x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8eae6f91da2e1db9e28375fb96783bf0368b8f82_2_706x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eae6f91da2e1db9e28375fb96783bf0368b8f82.jpeg 2x" data-dominant-color="F3F2F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-04-29 091615</span><span class="informations">743×788 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
