---
topic_id: 23671
title: "Importing Pc Scores In 3D Slicer"
date: 2022-06-01
url: https://discourse.slicer.org/t/23671
---

# Importing PC scores in 3D slicer

**Topic ID**: 23671
**Date**: 2022-06-01
**URL**: https://discourse.slicer.org/t/importing-pc-scores-in-3d-slicer/23671

---

## Post #1 by @NoemiH (2022-06-01 11:29 UTC)

<p>Hi,</p>
<p>I have run a PCA in MorphoJ and exported the PC scores for each individual. Is it possible to import the PC scores in 3D slicer to visualise 3D shape changes along the PC axes?</p>
<p>I know that 3D slicer can now perform PCA but since I have my landmark data in a different format and also the PCA results, it would be more convenient for me to just export these PC scores in 3D slicer if possible.</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2022-06-01 15:32 UTC)

<p>Short answer is no. You cannot. Even if you import the eigenvectors from MorphoJ, the rotations are specific to the GPA. You should run your data with SlicerMorph.</p>

---

## Post #3 by @NoemiH (2022-06-01 15:46 UTC)

<p>OK, thanks for your answer!</p>

---
