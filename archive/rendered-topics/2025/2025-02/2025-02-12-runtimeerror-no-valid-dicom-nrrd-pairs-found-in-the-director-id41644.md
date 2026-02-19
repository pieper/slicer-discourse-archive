---
topic_id: 41644
title: "Runtimeerror No Valid Dicom Nrrd Pairs Found In The Director"
date: 2025-02-12
url: https://discourse.slicer.org/t/41644
---

# RuntimeError: No valid DICOM-NRRD pairs found in the directories

**Topic ID**: 41644
**Date**: 2025-02-12
**URL**: https://discourse.slicer.org/t/runtimeerror-no-valid-dicom-nrrd-pairs-found-in-the-directories/41644

---

## Post #1 by @kwonheokju (2025-02-12 11:42 UTC)

<p>Hi, I’m trying to do machine learning using raw data in dicom format and mask data in nrrd format.<br>
However, the number of dicom files and the number of slices of nrd are not the same.<br>
When I open dicom and nrrd together using slicer, it’s matching, what’s the problem?</p>

---

## Post #2 by @lassoan (2025-02-13 04:26 UTC)

<p>Reconstruction of a 3D volume from 2D slices is a very complex task. Most likely there is no problem, there can be several valid reasons for the input slices not matching the dimensions of the reconstructed volume. Tell us more about your data.</p>

---

## Post #3 by @kwonheokju (2025-02-13 04:47 UTC)

<p>No, I’m not trying to reconstruct 2D into 3D.<br>
In slicer, the number of dcm and nrd is the same, but the number of indexes is not the same when imported from python.</p>

---
