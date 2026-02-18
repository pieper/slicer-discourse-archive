# Trouble importing DICOM files

**Topic ID**: 11017
**Date**: 2020-04-06
**URL**: https://discourse.slicer.org/t/trouble-importing-dicom-files/11017

---

## Post #1 by @alebarone (2020-04-06 16:48 UTC)

<p>Dear all,</p>
<p>I have been trying to import a DICOM folder with more than 1K frames of the heart. In particular, I’d like to import a series of frames with the three different orientations so that once I open them in 3DSlicer, I can see the three views at the same time (as done in the video tutorial on Youtube about heart segmentation). However, I can only see one group at the time, the software does not see the frames as a unique database. I already tried what suggested in other topics, such as drag and drop in the main window, import as any data, deselect “single file” and so on, but I didn’t succeed. Thus, when I try to segment it, I can only select one volume at the time.<br>
Could anyone help me with this? I’d really appreciate any suggestions.</p>
<p>Thank you,<br>
Alessandro</p>

---

## Post #2 by @lassoan (2020-04-06 16:50 UTC)

<p>What is the image modality (CT, US, or MRI) and dimensionality (2D+time, 3D, 3D+time)? How did you create the DICOM files?</p>

---

## Post #3 by @alebarone (2020-04-06 17:03 UTC)

<p>Thank you for your reply.<br>
They are images from MRI in 2D, with some including time. I was given the files, I didn’t create them.</p>

---

## Post #4 by @lassoan (2020-04-06 17:46 UTC)

<p>If you have 2D slices in 3 different orientations then you need to load all of them and then show a different image in each slice view (click the pushpin icon in the top-left corner of the slice view to see the image selector widget). You may also want to rotate the view to match the slice orientation, by clicking the small double-arrow button in the slice view controller, and then pressing the “Rotate to volume plane” button. See details here: <a href="https://discourse.slicer.org/t/read-prostate-mr-image-failed/3423/2" class="inline-onebox">Read Prostate MR image failed</a></p>

---

## Post #5 by @alebarone (2020-04-06 18:00 UTC)

<p>Yes, I managed to do that. However, as I am trying to do the same that was performed in the youtube video “Whole heart segmentation from cardiac CT in 10 minutes”, when I go to crop volume, I can’t select all the three views together. As input volume in IO, I can only select one slice view at the time . I suppose the volumes are not merged together, but can’t figure out how to do that. Would you have any suggestions? Or am I missing something?</p>
<p>Thanks for your help,<br>
Alessandro</p>

---

## Post #6 by @lassoan (2020-04-06 18:08 UTC)

<p>Would you like to segment 3 orthogonal slices? To segment 3D structures, you would need a 3D volume.</p>

---

## Post #7 by @alebarone (2020-04-06 18:17 UTC)

<p>Yes, that is what I want to do. I understand now.<br>
And is there any way to combine the different segmentations from the 2D slices to increase accuracy? Because if I use one view at the time, the 3D model looks pretty bad. I would like to somehow combine the informations coming from the different orientations to get a better final results.<br>
Thanks,<br>
A</p>

---

## Post #8 by @lassoan (2020-04-06 18:33 UTC)

<p>This is a fairly common issue with MRI acquisitions. See discussions here: <a href="https://discourse.slicer.org/t/3d-model-from-dicoms/5478/2" class="inline-onebox">3D model from dicoms</a></p>

---
