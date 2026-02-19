---
topic_id: 16695
title: "Create Roi From Pet Data"
date: 2021-03-22
url: https://discourse.slicer.org/t/16695
---

# Create ROI from PET data

**Topic ID**: 16695
**Date**: 2021-03-22
**URL**: https://discourse.slicer.org/t/create-roi-from-pet-data/16695

---

## Post #1 by @kykwon (2021-03-22 15:02 UTC)

<p>Dear experts,</p>
<p>I am trying to create ROI from dicom PET/CT data. I complete segmentation from the PET dicom data but I don’t know how can I create ROI from segmentation… is it possible or should I have to different way? please advice me…</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-03-23 05:53 UTC)

<p>What do you mean by ROI? In Slicer, by ROI we mean a box-shaped region of interest, but some people use ROI term for segmentation.</p>
<p>What is your overall goal?</p>

---

## Post #3 by @kykwon (2021-03-23 06:27 UTC)

<p>I’m newbie on this field. I want to simulate patient dose rate from the PET/CT DICOM file by FLUKA and it seems need ROIs for create RT Structure. I struggling hard for this last few weeks but still any gain.</p>
<p>First, I want to calculate absorbed dose of lesion from the PET image.<br>
Second, I want to simulate absorbed dose of lesion to voxelized source from the PET.<br>
where CT image will be use to voxel detector.</p>
<p>I can’t find information about this…</p>

---

## Post #4 by @kykwon (2021-03-24 04:28 UTC)

<p>I find solution, thank you for your kindness</p>
<p>Ciao</p>

---

## Post #5 by @lassoan (2021-03-24 16:07 UTC)

<p>Have you found a solution?</p>
<p>We don’t know what inputs FLUKA needs, but if you tell exactly what is required then we can tell you how to get it in Slicer.</p>

---

## Post #6 by @kykwon (2021-03-25 01:32 UTC)

<p>Dear lassoan</p>
<p>I didn’t know how do I mark up ROI on segmentation but now it’s okay.</p>
<p>additionally, I got error message while running Nvidia AI asistant like below</p>
<p>{{<br>
Traceback (most recent call last):<br>
File “/home/qwaj/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 492, in onClickAnnotation<br>
result_file = self.logic.dextr3d(in_file, session_id, model, pointSet)<br>
File “/home/qwaj/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1112, in dextr3d<br>
session_id=session_id,<br>
File “/home/qwaj/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/NvidiaAIAAClientAPI/client_api.py”, line 287, in dextr3d<br>
raise AIAAException(AIAAError.SERVER_ERROR, ‘Status: {}; Response: {}’.format(status, form))<br>
NvidiaAIAAClientAPI.client_api.AIAAException: (3, ‘Status: 500; Response: b’\n500 Internal Server Error\n</p><h1>Internal Server Error</h1>\n<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>\n’’)<br>
}}<p></p>
<p>what should I do?</p>
<p>thank you</p>

---
