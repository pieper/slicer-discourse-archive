# Collor map according Hounsfield unit

**Topic ID**: 35903
**Date**: 2024-05-03
**URL**: https://discourse.slicer.org/t/collor-map-according-hounsfield-unit/35903

---

## Post #1 by @Ricardo_Grillo (2024-05-03 22:02 UTC)

<p>Is there any 3D Slicer module that allows me to segment and create a 3D Skull with a color map based on the Hounsfield units from CT scan?</p>

---

## Post #2 by @muratmaga (2024-05-03 23:45 UTC)

<p>If your data is in HU, then you can do all of this.</p>

---

## Post #3 by @GeneRisi (2024-05-06 03:14 UTC)

<p>The approach I used was to filter the displayed 3d image such that mostly just bone was visible. That makes selecting the bone pretty straightforward. I then exported the selected area to a STL file, did a little editing and then 3d printed the model. Using this technique with a few sets of CT scans spaced out out in time, I created models of a bone flap undergoing aseptic resorption which I was able to bring to the surgeons’ offices when we discussed surgical repair options. One very nice benefit of this approach was to be able to feel the texture and thickness of the bone in different locations. You could also see new calcification of the dura occurring in one area.</p>

---
