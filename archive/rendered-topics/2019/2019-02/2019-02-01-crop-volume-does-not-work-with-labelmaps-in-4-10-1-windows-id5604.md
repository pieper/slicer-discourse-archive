---
topic_id: 5604
title: "Crop Volume Does Not Work With Labelmaps In 4 10 1 Windows"
date: 2019-02-01
url: https://discourse.slicer.org/t/5604
---

# Crop Volume does not work with labelmaps in 4.10.1 (windows)

**Topic ID**: 5604
**Date**: 2019-02-01
**URL**: https://discourse.slicer.org/t/crop-volume-does-not-work-with-labelmaps-in-4-10-1-windows/5604

---

## Post #1 by @muratmaga (2019-02-01 06:36 UTC)

<p>If the input volume is of labelmap type, and user chooses to “create a new volume as” Crop Volume does not work (see error below). As a work around, it is possible to clone the original label map, and specify it as the output volume. Then it works.</p>
<p>CropVolume: output volume (vtkMRMLScalarVolumeNode) is not compatible with input volume (vtkMRMLLabelMapVolumeNode)</p>

---

## Post #2 by @lassoan (2019-02-02 02:21 UTC)

<p>You can leave the default option (“Create new volume”) - then a compatible output volume is automatically created when you click apply. There are “Create new Volume” and “Create new Volume as…” options available near the bottom - those create simple Volume nodes (not labelmap volumes) - I understand that these may be confusing.</p>
<p>We could add options to create labelmap volume, but there are several other volume types. Some of them are defined in extensions so we cannot even add those, and the full list of nodes would be quite long anyway.</p>
<p>Do you have any suggestion how to make the GUI and behavior more intuitive?</p>

---

## Post #3 by @muratmaga (2019-02-02 04:49 UTC)

<p>I see. Yes, I was using the “Create New Volume As…” to rename the output file prior to cropping. I like the convenience of being able to name the volume at the function of choice, but if the drop-down list is too long, then it gets confusing.<br>
I am not sure if I have a good suggestion to improve the behavior. It is more about making it more consistent among different modules. Perhaps remove all 'create something new as" option from all modules, and have users create blank nodes (with whatever name they want) of correct type using the data module…</p>

---
