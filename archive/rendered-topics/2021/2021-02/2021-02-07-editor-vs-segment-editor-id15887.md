---
topic_id: 15887
title: "Editor Vs Segment Editor"
date: 2021-02-07
url: https://discourse.slicer.org/t/15887
---

# Editor vs Segment Editor

**Topic ID**: 15887
**Date**: 2021-02-07
**URL**: https://discourse.slicer.org/t/editor-vs-segment-editor/15887

---

## Post #1 by @vidyakar555 (2021-02-07 19:16 UTC)

<p>Windows 10<br>
3D Slicer 4.10.1</p>
<p>I’m a novice to the world of 3D Slicer. I would like to segment images and save the label maps in nii. format. <strong>How are Editor tool and the Segment Editor tool different from one another?</strong> Also can a label map previously created on Editor be further modified on Segment Editor tool?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-02-07 19:18 UTC)

<p>Editor module was deprecated several years ago and will soon be removed from Slicer. You can continue editing all previously created labelmaps using Segment Editor module.</p>

---

## Post #3 by @Mehran (2021-02-14 13:22 UTC)

<p>you can use “import” option in Segment Editor to import the label maps already exist. Later also you can export it as volumetric label map. Segment Editor has more options though their functionalities are a little different. e.g., if you only want to threshold an image and save the label, probably Editor is faster way. Anyway, I suggest to use Segment Editor to learn more.</p>

---

## Post #4 by @vidyakar555 (2021-02-14 16:10 UTC)

<p>Can a segmentation done on Segment Editor be saved in .mha file format?</p>
<p>While I was able to save a label in mha format while working with Editor tool, Segment Editor only allows saving in .nrrd format.</p>

---

## Post #5 by @Mehran (2021-02-14 16:27 UTC)

<p>Yes, you can. You need to click “segmentation” button, then scroll to find Export button. Once you click it, a volumetric label map will be created. If you go to save option, you will see a new file named Segmentation-label.nrrd. You can save this file in other formats.</p>

---

## Post #6 by @lassoan (2021-02-15 03:28 UTC)

<p>I would just add that although nrrd and mha file formats are almost the same, we promote usage of nrrdfor two reasons:</p>
<ol>
<li>nrrd allows storing overlapping segments as a 4D volume in a clean way (in nrrd files you can specify meaning of each axis)</li>
<li>anatomical image orientation is clearly defined in nrrd files (while in mha files <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/1017">AnatomicalOrientaition field is not used by most software</a>).</li>
</ol>

---
