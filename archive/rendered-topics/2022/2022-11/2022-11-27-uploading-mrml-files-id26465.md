# Uploading MRML Files

**Topic ID**: 26465
**Date**: 2022-11-27
**URL**: https://discourse.slicer.org/t/uploading-mrml-files/26465

---

## Post #1 by @ThymusTheTrain (2022-11-27 19:39 UTC)

<p>I’ve received the MRML, .nii.gz, .nrrd files for a segmentation and am trying to upload them to generate a 3D segmentation.</p>
<p>Which file(s) do I upload to 3D Slicer and what next module or steps do I select so I can see the 2D segmentation overlaid the MRI images and see the 3D segmentation? I’m hoping to export the 3D Segmentation.</p>
<p>To my understanding, I should just be able to upload the MRML file to get what I want, but when I switch between the Segment Editor modules I don’t see anything displayed.</p>
<p>Any help will be much appreciated. Thanks!</p>

---

## Post #2 by @lassoan (2022-11-27 20:21 UTC)

<p>If you open the MRML scene file (.mrml) then it should show everything (MRI, segmentation, etc) as it was shown when the scene was saved.</p>
<p>If this fails for some reason (e.g., not all the files were saved or provided to you) then you can open the image and segmentation files that you have by drag-and-dropping them to the application window. If non-standard file extension was used for saving the segmentation then you may need to choose “Segmentation” in the Description column in the “Add data” window.</p>

---
