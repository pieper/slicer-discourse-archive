---
topic_id: 27246
title: "Possibility To Export Multiple Labels In One Nifti File"
date: 2023-01-15
url: https://discourse.slicer.org/t/27246
---

# Possibility to export multiple labels in one nifti file?

**Topic ID**: 27246
**Date**: 2023-01-15
**URL**: https://discourse.slicer.org/t/possibility-to-export-multiple-labels-in-one-nifti-file/27246

---

## Post #1 by @a.mohseni (2023-01-15 10:39 UTC)

<p>Is it possible to export multiple labels in one nii.gz file? I’m cautious on trying this as I’m afraid the labels might go missing.</p>

---

## Post #2 by @lassoan (2023-01-17 05:55 UTC)

<p>The most common use case is to export all non-overlapping segments of an image into a single file. Therefore, you don’t need to worry about saving many labels into a single file.</p>
<p>However, NIFTI files have many issues, mostly due to that you can store the image geometry (origin, spacing, axis directions) in ambiguous ways. You may find that the labels that you write using one software cannot be read correctly by another software. Therefore, I would recommend using NRRD file format instead.</p>

---
