---
topic_id: 34842
title: "Generate A 3D Model Point Cloud From Ct Scan Of Abdomen"
date: 2024-03-12
url: https://discourse.slicer.org/t/34842
---

# Generate a 3d model/point cloud from CT scan of abdomen

**Topic ID**: 34842
**Date**: 2024-03-12
**URL**: https://discourse.slicer.org/t/generate-a-3d-model-point-cloud-from-ct-scan-of-abdomen/34842

---

## Post #1 by @Pratima (2024-03-12 06:21 UTC)

<p>Hello,<br>
I want to know step-by-step process on how to convert and download a segmented CT scan model (visible in Slicer) into Point Cloud/STL format. I am a beginner in 3D slicing. Any help is highly appreciated.</p>

---

## Post #2 by @muratmaga (2024-03-12 16:52 UTC)

<p>That’s done through segmentation. Please read the Segmentation and Segment Editor sections of the Slicer user manual at <a href="https://slicer.readthedocs.io">https://slicer.readthedocs.io</a></p>

---

## Post #3 by @drnoorfatima (2026-02-17 08:37 UTC)

<p>Hi! Yes this is definitely possible and you’re on the right track.<br>
The export process itself isn’t too complicated once your segmentation is properly set up, but for beginners the confusing part is usually what happens before the export , making sure the model is actually clean and ready, otherwise the STL or point cloud comes out unusable.<br>
Are you working with a specific type of scan (head, chest, bone, soft tissue)? And is this for 3D printing, analysis, or something else? That would help point you in the right direction since the steps differ a bit depending on the goal.</p>

---
