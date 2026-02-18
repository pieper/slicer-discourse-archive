# Creat a circular ROI and extract count in PET image

**Topic ID**: 28501
**Date**: 2023-03-21
**URL**: https://discourse.slicer.org/t/creat-a-circular-roi-and-extract-count-in-pet-image/28501

---

## Post #1 by @Shearson (2023-03-21 18:03 UTC)

<p>Dear members, I have a series of PET images of the same phantom. Now I’m trying to create a fixed size (like diameter=10mm) circular ROI in the same position of each series and extract the count or SUV. Is it possible or convenient to use 3D Slicer for this? I used to finish this work on GE Xeleris workstation and found it really time-consuming…</p>

---

## Post #2 by @cpinter (2023-03-21 19:28 UTC)

<p>The only idea I have for circular ROI is to use the Mask Volume effect in Segment Editor to zero out the values outside the sphere. The problem will be that without doing this programmatically, the ROI will not be exactly at the same place, because you will have to place the sphere each time manually. If you have a bit of experience in Python I could imagine a script that combines a <code>vtkSphereSource</code>, which can be converted into a Segmentation node, and then use the Mask Volume effect from code as well. Let me know if you are interested, happy to help with the script.</p>
<p>In the meantime, maybe others have a simpler idea…</p>

---

## Post #3 by @chir.set (2023-03-21 20:17 UTC)

<p>Do you mean a circular ROI in slice views or 3D views?<br>
Do all series have the same centre and the same XY(Z) resolutions?<br>
Would centering the series be acceptable?<br>
Can you post an image with a sketchy circle and point to what you want to count?<br>
Can you provide an anonymized such series ?</p>

---
