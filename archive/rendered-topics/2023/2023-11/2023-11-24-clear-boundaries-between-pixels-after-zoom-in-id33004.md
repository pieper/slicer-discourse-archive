---
topic_id: 33004
title: "Clear Boundaries Between Pixels After Zoom In"
date: 2023-11-24
url: https://discourse.slicer.org/t/33004
---

# Clear boundaries between pixels after zoom in

**Topic ID**: 33004
**Date**: 2023-11-24
**URL**: https://discourse.slicer.org/t/clear-boundaries-between-pixels-after-zoom-in/33004

---

## Post #1 by @AdiSoag (2023-11-24 13:20 UTC)

<p>Dear all,<br>
When I zoom in CT slice, the boundaries between pixels become blurring(1st picture), is there any settings that could show boundaries clearly like ImageJ(2nd picture)?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99662cefd258ec789c8582f8ee127c6bbb1be31e.jpeg" data-download-href="/uploads/short-url/lT1XHY8Z6zAS1n3oum4SIu0JgBg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99662cefd258ec789c8582f8ee127c6bbb1be31e_2_473x500.jpeg" alt="image" data-base62-sha1="lT1XHY8Z6zAS1n3oum4SIu0JgBg" width="473" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99662cefd258ec789c8582f8ee127c6bbb1be31e_2_473x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99662cefd258ec789c8582f8ee127c6bbb1be31e_2_709x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99662cefd258ec789c8582f8ee127c6bbb1be31e.jpeg 2x" data-dominant-color="9C9C9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×964 79.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/167c4afdfb8d5c0459e67fc63fda7ad5046eca43.png" data-download-href="/uploads/short-url/3cUNE34UQ9GeOfKAUidLIEcLSM3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/167c4afdfb8d5c0459e67fc63fda7ad5046eca43.png" alt="image" data-base62-sha1="3cUNE34UQ9GeOfKAUidLIEcLSM3" width="475" height="500" data-dominant-color="959595"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">796×837 6.38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-11-24 14:17 UTC)

<p>You can use the button marked “interpolation” for this.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view</a></p>

---

## Post #3 by @lassoan (2023-11-24 14:29 UTC)

<p>What you refer to “blurring” is a low-pass filter and dense resampling that reconstructs the original continuous signal from discrete samples (voxel values). Performing this interpolation is not a user preference but the right thing to do. If you just display the raw sample values then you will see edges that were not present in the original signal (harsh, visible boundaries of each voxel) that may make it harder to see real changes in the signal.</p>
<p>I know that some imaging software disable it by default (ImageJ, ITK-Snap), probably because long time ago the additional computation slowed down the image display; and the artifacts are not as complex because these software mostly just show 2D image slices - they cannot work on arbitrarily positioned and oriented slices in a 3D volume. However, in 3D Slicer each slice view position can be freely positioned and oriented in the volume, so if you just display the closest sample value instead of showing the reconstructed signal then you may get very confusing artifacts like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/657133774b3589725b31f717750150bb07158fdb.jpeg" data-download-href="/uploads/short-url/etoKUsqB7Dp4jmzXp6ozezAGDnt.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/657133774b3589725b31f717750150bb07158fdb.jpeg" alt="image" data-base62-sha1="etoKUsqB7Dp4jmzXp6ozezAGDnt" width="526" height="500" data-dominant-color="595959"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">746×709 42.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Some users wants to disable interpolation because they segment low-resolution images and it matters where where the exact pixel boundaries are. However, this means that you are trying to represent a signal with less samples than it would be required, which would lead to most processing algorithm working incorrectly and reconstructed 3D surface would lose details or contain step artifacts. One solution to this is to resample the input image (for example, using <code>Crop volume</code> module) to have higher resolution before starting the segmentation.</p>
<p>If you just want to see the pixel boundaries for software debugging then disabling interpolation is again not a good approach. The problem is that you can only make those pixel boundaries visible where value of the neighbors are sufficiently different. Even if you artificially increase the contrast to see more of the pixel boundaries, you will never be able to visualize boundaries between voxels that have exactly the same value. For this kind of debugging tasks, you can copy past <a href="https://discourse.slicer.org/t/volume-display-interpolate-turned-off-by-default-in-newest-stable/13918/10">this code snippet</a> into the Python console, which displays the voxel grid (replace the <code>volumeNode = ...</code> line by <code>volumeNode = getNode("MyVolumeName")</code> where <code>MyVolumeName</code> is the name of the image you want to see the voxel boundaries of).</p>
<p>You can find further related discussions in these topics:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/image-processing-reslicing-a-dicom-series-generates-artifacts/25841" class="inline-onebox">Image Processing: reslicing a DICOM series generates artifacts</a></li>
<li><a href="https://discourse.slicer.org/t/volume-display-interpolate-turned-off-by-default-in-newest-stable/13918" class="inline-onebox">Volume display - Interpolate turned off by default in newest stable?</a></li>
<li><a href="https://discourse.slicer.org/t/turn-off-all-smoothing-in-segmentation/1933" class="inline-onebox">Turn off all smoothing in segmentation</a></li>
</ul>

---

## Post #4 by @AdiSoag (2023-11-27 13:12 UTC)

<p>Thank you for your replies!<br>
I am writing an script to find corresponding voxels in CT slces from RT-Structure points coordinates, therefore clear boundaries are important for me to check whether my script is correct.<br>
Click “interpolation” button is useful for me.<br>
Thanks again!</p>

---
