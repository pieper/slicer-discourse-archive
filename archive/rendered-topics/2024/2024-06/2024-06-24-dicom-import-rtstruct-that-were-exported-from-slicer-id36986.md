---
topic_id: 36986
title: "Dicom Import Rtstruct That Were Exported From Slicer"
date: 2024-06-24
url: https://discourse.slicer.org/t/36986
---

# Dicom import RTSTRUCT that were exported from slicer

**Topic ID**: 36986
**Date**: 2024-06-24
**URL**: https://discourse.slicer.org/t/dicom-import-rtstruct-that-were-exported-from-slicer/36986

---

## Post #1 by @gleesoi (2024-06-24 18:00 UTC)

<p>Hi, new to slicer and working on a dicom workflow. I notice that importing my dicom ct and segments look fine in dicom apart from a body rind and couch roi.</p>
<p>I then export the ct and contours in dicom to file.</p>
<p>I then load them and many contours look different/wrong and cut in all views. When i try to edit the contours or change 2d visibility to binary label, the computer seems to struggle and freeze… help please thanks!</p>
<p>if its just a visual thing thats fine but if someone needs to edit etc it freezes/crashes which seems bad. might be similar to topic <a href="https://discourse.slicer.org/t/loading-dicom-ct-rt-structure-is-incomplete/21696">Loading DICOM CT+RT Structure is incomplete - Support - 3D Slicer Community</a> but is there anything else i am missing? thanks<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ee2dcc075ccdf11df74f304df7d06a425c5c675.png" alt="imported original ct rois" data-base62-sha1="fOWzsO8I1kVJm9QO9temb9iieJD" width="602" height="262"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a22383b38b3aa32ae4161016961a2cf9814e91f6.png" alt="re imported ct rois exported from slicer" data-base62-sha1="n8lrfMl6T0H5O1YI3Tt4DPsY1rE" width="602" height="257"></p>

---

## Post #2 by @gleesoi (2024-06-24 18:51 UTC)

<p>I now see I need to set binary label before Dicom export which looks better upon re import ! My follow up question is if anyone know how to set source (yellow star) to be binary label via script? I can see command for create but not set source? This would be useful to automate this step for me thanks</p>

---

## Post #4 by @gleesoi (2024-06-24 20:15 UTC)

<p>segmentationNode.SetSourceRepresentationToBinaryLabelmap()</p>

---
