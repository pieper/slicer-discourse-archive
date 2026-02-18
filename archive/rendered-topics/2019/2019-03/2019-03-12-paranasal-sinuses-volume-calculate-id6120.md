# Paranasal Sinuses Volume Calculate

**Topic ID**: 6120
**Date**: 2019-03-12
**URL**: https://discourse.slicer.org/t/paranasal-sinuses-volume-calculate/6120

---

## Post #1 by @hozermd (2019-03-12 17:41 UTC)

<p>Hi,<br>
I want to measure the volume of each paranasal sinuses. Each one separately; Left, Right; sphenoid, ethmoid, maxillary, frontal sinus and total nasal cavity volume. I’ve tried many methods, extensions and programs. For example; ImageJ, ITKSnap and in Slicer automated segmentation extensions. ITKsnap and some slicer extensions is good but not so simple. What is your advice?</p>

---

## Post #2 by @gcsharp (2019-03-12 18:38 UTC)

<p>The paranasal sinuses contain a mixture of air, bone, and phlegm, and therefore don’t lend themselves to thresholding or other simple methods.  I suggest you contour them manually.  In Slicer, you can contour every other slice and interpolate.</p>

---
