---
topic_id: 37285
title: "Batch Processing Stl Files Into Binary Images For Radiomics"
date: 2024-07-09
url: https://discourse.slicer.org/t/37285
---

# Batch Processing Stl files into binary images for Radiomics

**Topic ID**: 37285
**Date**: 2024-07-09
**URL**: https://discourse.slicer.org/t/batch-processing-stl-files-into-binary-images-for-radiomics/37285

---

## Post #1 by @Steven_A (2024-07-09 15:02 UTC)

<p>Hi, is there a way to batch process the discretization of stl files into binary images to be loaded into either slicerradiomics or into pyradiomics for feature extraction? Or maybe there is a way to simply load in the stl file with trimesh or numpy-stl and discretize it in order to use pyradiomics?</p>

---

## Post #2 by @pieper (2024-07-09 15:17 UTC)

<p>Yes, you can do that with a small python script.  See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">these examples</a></p>

---

## Post #3 by @Steven_A (2024-07-09 15:25 UTC)

<p>How do you go about batch importing files into a MRML scene and then accessing each node in order to use the example code you provided?</p>

---

## Post #4 by @pieper (2024-07-09 15:53 UTC)

<p>Generally you probably want to load each one, convert it, save it, and delete it.  Just do that in a loop over all your file names.  I don’t think we have a canned example of that but it’s something a chatbot should be good at generating for you.</p>

---
