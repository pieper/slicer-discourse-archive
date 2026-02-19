---
topic_id: 38417
title: "How To Combine The Ct Packages Of Hip Knee And Ankle"
date: 2024-09-17
url: https://discourse.slicer.org/t/38417
---

# How to combine the CT packages of hip, knee and ankle

**Topic ID**: 38417
**Date**: 2024-09-17
**URL**: https://discourse.slicer.org/t/how-to-combine-the-ct-packages-of-hip-knee-and-ankle/38417

---

## Post #1 by @angelica_arrighetti (2024-09-17 21:57 UTC)

<p>Goodmorning,</p>
<p>Is it possible to know all the procedures to combine different CT packages of hip knee and anke to align them and so be able to do mesurements, and also how can i mesure angles like LDFA or MPTA or JLCA using tools like angles, lines and circles after the alignement is done?<br>
Is it mandatory to segment it or is there another option?</p>
<p>Thanks to all the people that’s gonna answer.</p>

---

## Post #2 by @pieper (2024-09-17 22:10 UTC)

<p>If the CTs of the different joints were obtained as different Series in the same Study, just with gaps for the long bones and the patient didn’t move much then you should be able merge them easily and make measurements.  If by “packages” you mean something different then it will be hard to combine them unless the scans happen to contain overlapping anatomy.</p>

---

## Post #3 by @angelica_arrighetti (2024-09-17 22:30 UTC)

<p>Yes by “packages” I mean that they are different series but in the same study.<br>
But I still don’t understand how to put them together with 3d slicer, if you or anyone else can help me I’d be so grateful.</p>

---

## Post #4 by @pieper (2024-09-18 14:56 UTC)

<p>You can load all three series as volumes in Slicer and assuming the dicom header data is correct (i.e. they all have the same “FrameOfReferenceUID” and correct positions and orientations) then you can use the markups tools to make measurements on all three scans.  It can be a bit awkward to work with as three volumes so you might use the <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">StitchVolumes</a> module or just the built-in CropVolumes module and AddScalarVolumes.  For the latter approach you would make an ROI big enough for all three volumes, crop on volume into it, and then add the other two volumes.</p>

---
