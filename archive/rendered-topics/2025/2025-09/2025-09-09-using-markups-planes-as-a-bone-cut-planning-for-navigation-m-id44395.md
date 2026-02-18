# Using Markups planes as a bone cut planning for navigation machine

**Topic ID**: 44395
**Date**: 2025-09-09
**URL**: https://discourse.slicer.org/t/using-markups-planes-as-a-bone-cut-planning-for-navigation-machine/44395

---

## Post #1 by @Ben_Fong (2025-09-09 02:17 UTC)

<p>Hello,</p>
<p>I am working on bone tumour surgery planning. I created planes in Markups for the bone cuts, and would like to convert them to models and then save them as STLs to import to the navigation machine. I have two questions:</p>
<p>1.     I used the markuptomodel extension, selected the plane, the name of the plane appears in the model, but there is nothing inside. What have I missed?</p>
<p>2.     I would like to have the plane with thickness because real bone cut have thickness. Is there a way to covert the plane into one with thickness (effectively a rectangle)? Or should I use ROI? But then, how can I convert it to a model/stl?</p>
<p>Thanks</p>

---

## Post #2 by @mau_igna_06 (2025-09-09 02:29 UTC)

<p>When <a href="https://github.com/Slicer/SlicerSurfaceToolbox/pull/80" rel="noopener nofollow ugc">this PR</a> is merged you’ll be able to give thickness to markup planes by creating a narrow box 3D model</p>

---
