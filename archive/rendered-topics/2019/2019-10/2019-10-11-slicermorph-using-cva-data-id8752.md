---
topic_id: 8752
title: "Slicermorph Using Cva Data"
date: 2019-10-11
url: https://discourse.slicer.org/t/8752
---

# SlicerMorph using CVA data?

**Topic ID**: 8752
**Date**: 2019-10-11
**URL**: https://discourse.slicer.org/t/slicermorph-using-cva-data/8752

---

## Post #1 by @sarah0501 (2019-10-11 23:31 UTC)

<p>Hello!</p>
<p>I recently learned how to morph the 3D model on SlicerMorph with PCA analysis available on the software. However, I mainly utilize CVAs for my projects. Is there a way to input my CVA values from another program (ie MorphoJ) and still utilize SlicerMorph functions? I would like to show the different morphologies represented on the opposite spectrums of the axes using the 3D model and create animation videos for presentation purposes.</p>
<p>Thank you!</p>
<p>Operating system: Mac OS High Sierra/Windows 10<br>
Slicer version: Slicer 4.11<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @muratmaga (2019-10-12 17:49 UTC)

<p>While you can do PCA decomposition, we currently do not have plans to implement CVA within SlicerMorph. We are thinking of developing a mechanisms to bring a set of arbitrary coefficients calculated external analytical packages and being able to visualize within SlicerMorph. It is the next thing we would like to tackle, but will take sometime to implement.</p>

---
