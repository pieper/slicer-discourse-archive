# Reorient MPR slice for 2d segmentation

**Topic ID**: 36724
**Date**: 2024-06-12
**URL**: https://discourse.slicer.org/t/reorient-mpr-slice-for-2d-segmentation/36724

---

## Post #1 by @rxl (2024-06-12 13:35 UTC)

<p>I was searching for a way to resample a volume in the orientation of multiplanar reformation (using 3d Slicer’s “interactive slice intersections” feature), with the goal of creating a 2d segmentation that lives in 1 slice in that space.</p>
<p>I previously found this solution for saving a single MPR slice, but didn’t know how to approach it to follow up with segmentation: <a href="https://discourse.slicer.org/t/export-single-mpr-slice-to-dicom/22853/14">Export single MPR slice to DICOM - Support - 3D Slicer Community</a></p>
<p>Any suggestions would be greatly appreciated.</p>

---

## Post #2 by @lassoan (2024-06-12 16:55 UTC)

<p>There are many ways to achieve this. What is your overall goal? Would you like to segment some 3D structures (vessels, bones, valves, etc.) slice by slice using some 2D segmentation model and then reconstruct a 3D volume from that?</p>

---

## Post #4 by @rxl (2024-06-13 14:47 UTC)

<p>Thanks for your reponse. For my purposes, I only need the 2D segmentations from this single slice in as streamlined of a fashion as possible; no 3D volume from multiple slices would be needed.</p>
<p>It seems necessary to resample in the multiplanar reformation’s axes to obtain a 2D mask. From this slice, I would segment a few ROIs that I’d like to save, then look at radiomic features.</p>

---

## Post #5 by @rxl (2024-06-13 17:49 UTC)

<p>Adding on: after segmenting, I’d like to save images and segmentations as .nrrd files to manipulate outside of Slicer</p>

---

## Post #6 by @lassoan (2024-06-13 19:17 UTC)

<p>Probably the easiest is to add a markup ROI, translate/rotate it to the desired location, and then use Crop volume module GUI to extract a slice (or a few slices).</p>

---

## Post #7 by @rxl (2024-06-18 14:02 UTC)

<p>Thank you for this. I’m having difficulty executing this; manual rotation is difficult to line up and I wasn’t able to find the . Cropping did make sense as well.</p>
<p>I also had a follow-up question from one of your prior responses:<br>
<a href="https://discourse.slicer.org/t/convert-closed-curve-to-segment-in-segment-editor/29805">Convert closed curve to segment in Segment Editor - Support - 3D Slicer Community</a></p>
<p>I wasn’t able to figure out from the UI or documentation how to use an existing closed curve to a segmentation using Surface cut (within segment editor, if there’s another way). Everything seemed to revolve around creating new fiducials rather than using the existing curve.</p>
<p>Sorry, I’ve only used Slicer in very limited capacity before (axial segmentations) and trying to take advantage  of so many new features at once is a bit overwhelming!</p>

---

## Post #8 by @lassoan (2024-06-18 17:21 UTC)

<aside class="quote no-group" data-username="rxl" data-post="7" data-topic="36724">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rxl/48/76926_2.png" class="avatar"> rxl:</div>
<blockquote>
<p>I’m having difficulty executing this; manual rotation is difficult to line up</p>
</blockquote>
</aside>
<p>There are many ways to achieve this, depending on what you exact needs are. But to make things really simple, I uploaded a simple script that you can use to extract an arbitrary slice from a volume designated by a markup plane. You can place a markup plane by a single click in any slice view and then copy-paste <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-slice-from-volume">this code snippet</a> into the Python console to extract that slice as a new volume.</p>
<blockquote>
<p>I also had a follow-up question from one of your prior responses</p>
</blockquote>
<p>Please keep this topic focused on the original question and post follow-up comments in that other topic or create a new topic for a new question. Thank you!</p>

---

## Post #9 by @rxl (2024-06-26 18:23 UTC)

<p>Thank you, the code snippet helped me extract the volume in the view of slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLScalarVolumeNode”)</p>
<p>This volume included voxels oriented in the original volume; would it be possible to resample the voxels in the new orientation so I could get a 2D cross section?</p>
<p>I tried resampling, which give the below image: however, using segment editor on the source volume “output volume (post-resampling)” still produces these angular annotations. Can I interpret this as that the resampled voxels are still in the same old orientation, despite what appears in the other views? If so, how can I resample to get an accurate 2d segmentation, for 2d shape properties?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/653ccdcfccede7ba064d2e4b06e75e827378c648.png" data-download-href="/uploads/short-url/erAuM5FXOs8RHDbaGq011NllLKw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/653ccdcfccede7ba064d2e4b06e75e827378c648_2_690x375.png" alt="image" data-base62-sha1="erAuM5FXOs8RHDbaGq011NllLKw" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/653ccdcfccede7ba064d2e4b06e75e827378c648_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/653ccdcfccede7ba064d2e4b06e75e827378c648_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/653ccdcfccede7ba064d2e4b06e75e827378c648.png 2x" data-dominant-color="4D4B52"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1269×691 94.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @rxl (2024-07-01 14:19 UTC)

<p>I’m having difficulty resampling the volume in the desired orientation, my original aim. Whether one slice or the whole volume doesn’t matter, but I’d like it to use the normal vectors from the orientation.</p>
<p>I made some headway with taking normal vectors from the reformat module for each r/g/y slice view and using them in a transformation matrix, but I’m still not achieving the goal and the workflow seems impractical.</p>
<p>From <a href="https://www.slicer.org/wiki/Documentation/4.6/FAQ#How_can_I_use_the_reformat_widget_view_to_resample_my_images.3F" rel="noopener nofollow ugc">FAQS from 4.6</a>, I did see this snippet “How can I use the reformat widget view to resample my images?” but wasn’t able to figure out how to yield new transforms or volumes with it.</p>

---
