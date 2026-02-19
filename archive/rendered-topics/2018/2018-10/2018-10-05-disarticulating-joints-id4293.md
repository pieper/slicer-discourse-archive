---
topic_id: 4293
title: "Disarticulating Joints"
date: 2018-10-05
url: https://discourse.slicer.org/t/4293
---

# Disarticulating Joints

**Topic ID**: 4293
**Date**: 2018-10-05
**URL**: https://discourse.slicer.org/t/disarticulating-joints/4293

---

## Post #1 by @vahemat (2018-10-05 01:43 UTC)

<p>Hey all,</p>
<p>I’m completely new to this. I was hoping someone could refer me to a good tutorial that I can use make make a model of a disarticulated joint. Specifically, I want to be able to make a model of a joint, however, I want to print each bone involved in the joint separately. For example, if I wanted to make the ankle joint I would start with a DICOM file from a CT scan and be able to print the tibia, fibula and talus individually. Much appreciate the help.</p>

---

## Post #2 by @lassoan (2018-10-05 02:58 UTC)

<p>You need to import the CT scan, segment the image using <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">Segment Editor module</a> (see tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">here</a>), creating a separate segment for each piece that you would like to print separately, then <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428">export to STL file</a>.</p>

---

## Post #3 by @vahemat (2018-10-08 22:50 UTC)

<p>Thanks a lot. That video helped a lot.</p>

---
