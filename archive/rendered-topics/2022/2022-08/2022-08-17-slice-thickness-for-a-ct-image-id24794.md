# Slice thickness for a CT image

**Topic ID**: 24794
**Date**: 2022-08-17
**URL**: https://discourse.slicer.org/t/slice-thickness-for-a-ct-image/24794

---

## Post #1 by @Varsha (2022-08-17 06:14 UTC)

<p>Hi, I am currently in the process of examining various bony surface changes and correlating the same to the age of individuals using CT scans of the pelvis. I have some doubts which might seem pretty basic but I was wondering if anyone could guide me how to go about the following: How do I measure the slice thickness of a loaded CT image? I can find other relevant information while I load the data but i cant seem to find information pertaining to the slice thickness anywhere. Furthermore if I want to reduce the slice thickness, say from 1.0 mm to 0.6 mm, is it possible to do that using 3D Slicer? To what extent will the image quality be affected if I attempt to do this?</p>

---

## Post #2 by @pieper (2022-08-17 16:46 UTC)

<p>You can see the spacing between the slices in the Volumes module under Volume Information.  Thickness of CT slices is a related but independent parameter that also influences quantification so you can look that up in any book about CT.  If you need to see the thickness for a given CT you can look for it in the dicom metadata (right click on series in dicom browser).  If you want to resample the slice spacing you can use the CropVolume module the resample module.</p>

---
