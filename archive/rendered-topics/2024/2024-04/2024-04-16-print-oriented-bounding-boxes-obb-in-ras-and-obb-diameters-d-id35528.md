# Print oriented bounding boxes(OBB in ras) and obb diameters data for 600 patients

**Topic ID**: 35528
**Date**: 2024-04-16
**URL**: https://discourse.slicer.org/t/print-oriented-bounding-boxes-obb-in-ras-and-obb-diameters-data-for-600-patients/35528

---

## Post #1 by @hk_y (2024-04-16 12:22 UTC)

<p>Operating system: mac os python 3.12<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
I’ve labeled and converted over 600 patients’ labels into NRRD files. I want to apply the “obb in ras” and “obb diameter” for label (only one segmentation in each patient) using the “Segment Statistics” tool from “Quantification” in 3D Slicer. However, applying this operation to each patient individually would be too time-consuming. Do you have any suggestions?<br>
Actual behavior: I try tp apply this operation to each patient individually but it’s too time-consuming. Do you have any suggestions?</p>

---

## Post #2 by @mikebind (2024-04-17 01:55 UTC)

<p>You can do this fairly easily with a python script.  You might also take a look at Slicer Case Iterator (<a href="https://github.com/JoostJM/SlicerCaseIterator" class="inline-onebox" rel="noopener nofollow ugc">GitHub - JoostJM/SlicerCaseIterator: Simple Scripted Module to batch process patients in 3D Slicer</a>), which is oriented around looping over cases.  The Slicer script repository will also be very helpful for you, here is a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi" rel="noopener nofollow ugc">link to an example script</a> which gathers obb data using the Segment Statistics module from python.  Combining those two pieces (looping over cases and finding obb data on each) should get you everything you need.</p>

---

## Post #3 by @hk_y (2024-04-18 10:24 UTC)

<p>Thank you so much! I have solved my problem.</p>

---
