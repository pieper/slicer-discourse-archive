# Option to disable "minimum bounding box" cropping feature for segmentations

**Topic ID**: 10221
**Date**: 2020-02-12
**URL**: https://discourse.slicer.org/t/option-to-disable-minimum-bounding-box-cropping-feature-for-segmentations/10221

---

## Post #1 by @eyjolfur (2020-02-12 16:51 UTC)

<p>Hello,</p>
<p>First of all, thanks to everyone who has worked on the development of Slicer, it is proving immensely useful in my work. This post is regarding the underlying “minimum bounding box” cropping feature of segmentations in Slicer.</p>
<p>In brief, I would propose having the option of disabling the “minimum bounding box” cropping of segmentations when loading and editing segmentations in Slicer. I am aware that the most recent preview versions of Slicer are now providing the option of disabling this feature when saving segmentations, which is great, but I would prefer also having the option to disable it when loading and processing segmentations.</p>
<p>I’m currently working on the segmentations of fibrotic lungs on CT scans. My current workflow is as follows:</p>
<ol>
<li>Load in the CT scan into Slicer as a .nii.gz file.</li>
<li>Load in an initial lung segmentation labelmap (created using external software) into Slicer as a .seg.nii.gz file. This .seg.nii.gz volume is initially of the same dimensions as the CT scan.</li>
<li>Create a new segmentation using the Segmentations module in Slicer. To do this, I select the “reference volume” to be the CT scan from step 1, and import the labelmap from step 2.</li>
<li>I would like to now correct the initial lung segmentation from step 2. As part of this, I will potentially be adding regions that are outside of the “minimum bounding box” of the initial segmentation.</li>
</ol>
<p>Steps 1-3 work fine. It is at step 4 where I run into the issue of being unable to add regions outside the minimum bounding box of the initial segmentation, seemingly due to the automatic cropping of the segmentation volume by Slicer.</p>
<p>I have read previous posts on this topic on this forum (e.g., <a href="https://discourse.slicer.org/t/cannot-edit-outside-a-segmentation-bounding-box/2451/7" class="inline-onebox">Cannot edit outside a segmentation bounding box</a>), and I have tried the proposed solutions: e.g., setting the reference volume as the CT scan from step 1, and using the “Crop Volume” module to extend the volume of the segmentation – unfortunately, after hours of trying to get it to work, neither solution seems to solve the issue completely for me.</p>
<p>In the end, to bypass this issue, I’ve inserted segmentation voxels at opposite corners of the top and bottom slices in my initial segmentation, so that the minimum bounding box covers the whole scan. However, this is not exactly a perfect solution due to the following reasons:</p>
<p>a) It creates an arbitrary step of inserting “ghost” segmentation voxels into my initial segmentation that I have to make sure to ignore in subsequent processing of the corrected segmentations (e.g., development of segmentation models, etc.).<br>
b) I would like to use the “Fill between slices” feature of the Segmentations module when working on the corrected segmentation. The voxels at the top and bottom slices of the segmentation interfere with this process. If I delete these voxels before filling between slices, Slicer seems to crop the segmentation volume “on the fly” and I again lose my ability to edit regions outside the new minimum bounding box.</p>
<p>In summary, having the option to disable all minimum bounding box cropping of segmentations, whether when loading segmentations or editing them, would be immensely useful for me. I understand the reasoning behind it of saving memory and disk space, and it may not be causing issues in most cases, but in my case it would save me a lot of headache just to have the option to disable it altogether.</p>
<p>I hope the above explanation has been sufficiently thorough and I welcome any thoughts on this feature request. Let me know if I’ve missed anything.</p>
<p>All the best,<br>
Eyjólfur</p>

---
