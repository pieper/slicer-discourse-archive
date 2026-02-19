---
topic_id: 12745
title: "Questions About Importing Labelmap Directly To Produce 3D Mo"
date: 2020-07-27
url: https://discourse.slicer.org/t/12745
---

# Questions about importing labelmap directly to produce 3D model

**Topic ID**: 12745
**Date**: 2020-07-27
**URL**: https://discourse.slicer.org/t/questions-about-importing-labelmap-directly-to-produce-3d-model/12745

---

## Post #1 by @KKad (2020-07-27 13:18 UTC)

<p>Hello Slicer Community! Very new user here,<br>
I have some annotated volumetric data (in the form of one 2D array per slice) where each pixel is labelled with a material and a volume index. The format is currently stored on matlab/python.</p>
<p>I want to use the model maker module to import this labelmap directly and create a 3D surface mesh of my model which I will use for biomechanical finite element analysis.</p>
<p>I’m having a bit of trouble understanding which file formats I need to provide, I understand that to normally get a label map i need to import images (DICOMS,pngs etc) and then segment the data. But in my case I already have the annotated data and I’m unsure of how to import it directly into slicer.</p>
<p>If anyone can guide me in the process that would be fantastic<br>
Thank you!</p>

---

## Post #2 by @lassoan (2020-07-27 13:31 UTC)

<p>You can save the labelmap file into nrrd format and then load it as segmentation by selecting “Segmentation” in Description column in “Add data” window.</p>
<p>You can then create a volumetric mesh using <a href="https://github.com/lassoan/SlicerSegmentMesher#segment-mesher-extension">SegmentMesher extension</a>.</p>

---
