# How to convert a segmentation back into a stack of images 

**Topic ID**: 24085
**Date**: 2022-06-28
**URL**: https://discourse.slicer.org/t/how-to-convert-a-segmentation-back-into-a-stack-of-images/24085

---

## Post #1 by @sam.seq (2022-06-28 16:03 UTC)

<p>How do you convert a segmentation that has been edited back into a stack of images?</p>

---

## Post #2 by @lassoan (2022-06-28 16:19 UTC)

<p>A segmentation (the binary labelmap representation) is already a stack of image slices. You can definitely write out each slice into a separate image file, but it should not be necessary and by storing each slice as a separate png file you would lose essential information about image geometry.</p>
<p>What is your end goal? Why would you like to save the 3D image as separate 2D images?</p>

---

## Post #3 by @sam.seq (2022-06-28 16:34 UTC)

<p>How do you save each slice as a separate image file? I have a coronary artery that I segmented using contrast and the spherical brush to create a 3D rendering but I want to take measurements of each slice in a different program, so I would need each slice as an individual image file.</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2022-06-29 02:14 UTC)

<p>What measurements would you like to make (vessel diameters, Cardiac Agatston score, …)? In which program? How do you ensure that physical sizes in the exported 2D image are correct (how that other program gets the pixel size)? Are you sure that doing measurements on parallel slices is optimal (e.g., if you want to measure cross-sections then instead of parallel slices you must use curved planar reformatting that follows the normal of the vessel centerline).</p>
<p>Sorry for asking all the questions, but I would not like to mislead you or spend time with guiding you through some process that produces incorrect or suboptimal results.</p>

---

## Post #5 by @sam.seq (2022-06-29 03:09 UTC)

<p>I am looking to find the inner and outer radius from the center point, I want to analyze it in MatLab, slice by slice using a loop. I am planning to check the measurements are correct and then use a conversion factor to fix it.</p>

---

## Post #6 by @lassoan (2022-06-29 04:46 UTC)

<p>You can get radius measurements fully automatically from <a href="https://github.com/vmtk/SlicerExtension-VMTK/">VMTK extension</a>. No exporting of the data needed, no programming is needed, no extensive validation is needed (as the method has been validated in many projects throughout the years). You just run centerline extraction and get a csv file with the radius values along the vasculature. The results are more accurate than by computing radius on parallel planes (because the parallel planes are not always exactly orthogonal to the vessel’s centerline).</p>

---
