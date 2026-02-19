---
topic_id: 45559
title: "Clarification On Segment Statistics Surface Area Vs Cross Se"
date: 2025-12-19
url: https://discourse.slicer.org/t/45559
---

# Clarification on Segment Statistics: Surface Area vs. Cross-Sectional Area (CSA) for Muscle Analysis

**Topic ID**: 45559
**Date**: 2025-12-19
**URL**: https://discourse.slicer.org/t/clarification-on-segment-statistics-surface-area-vs-cross-sectional-area-csa-for-muscle-analysis/45559

---

## Post #1 by @GaetanoGazze (2025-12-19 12:49 UTC)

<p>Hi everyone,</p>
<p>I am performing a quantitative body composition analysis on single-slice CT scans (at the D10 level) using the <strong>Segment Statistics</strong> module in 3D Slicer. I would like to clarify a methodological doubt to ensure the accuracy of my data:</p>
<ol>
<li>
<p><strong>Surface Area vs. CSA:</strong> Can you confirm that the <strong>‘Surface Area’ (mm²)</strong> metric provided by the module refers to the total 3D surface area of the generated mesh (the “envelope” or “shell” of the segment)? In my single-slice analysis, this value is significantly higher than the expected planar area. Is it correct to assume that ‘Surface Area’ should <strong>not</strong> be used as a proxy for the <strong>Cross-Sectional Area (CSA)</strong> or <strong>Skeletal Muscle Area (SMA)</strong>?</p>
</li>
<li>
<p><strong>SMA Calculation:</strong> To derive the <strong>Skeletal Muscle Area (SMA)</strong> in cm^2, I am currently taking the <strong>‘Volume’ (mm³)</strong> of the segment and dividing it by the slice thickness (e.g., 1 mm). Is this “Volume / Thickness” conversion considered a standard and reliable method in Slicer to obtain the 2D planar area from a single-slice segmentation?</p>
</li>
</ol>
<p>I want to make sure I am not misinterpreting the geometric outputs of the software, as using the wrong metric would lead to incorrect Skeletal Muscle Index (SMI) calculations.</p>
<p>Thank you in advance for your help!</p>

---

## Post #2 by @mikebind (2025-12-19 23:16 UTC)

<p>You are correct that Segment Statistics returns the 3D surface area of the generated mesh, the sum of the areas of all the triangles which make up the surface. To your second question, no, you can’t derive cross sectional areas by dividing the total surface area by a slice thickness.  Such a calculation would give you an average volume per slice, but would not tell you about the CSA.  To get a series of CSA values, you should cut across the muscle perpendicular to the axis you want to measure relative to (presumably the long axis of the muscle or perhaps a centerline of the muscle), and measure the enclosed area.  This discussion will likely be helpful for you: <a href="https://discourse.slicer.org/t/extracting-muscle-cross-sectional-area-and-its-centroid-locatation-from-mri-ct-scans/12575" class="inline-onebox">Extracting muscle cross-sectional area and its centroid locatation from MRI/CT scans</a></p>

---

## Post #3 by @GaetanoGazze (2025-12-28 23:16 UTC)

<p>Hello, thank you for your prompt and valuable feedback.</p>
<p>First of all, I would like to wish you and the entire community a Merry Christmas and happy holidays!</p>
<p>I realized I missed an important detail in my previous message: I am not loading full CT volumes into 3D Slicer. Instead, I am working with <strong>single-slice CT images</strong> that have been pre-selected and re-sliced at the level of the inferior border of the D10 vertebral body, oriented along the vertebral endplate. The slice thickness is exactly 1 mm.</p>
<p>My goal is not to calculate the CSA of a single muscle, but the total <strong>Skeletal Muscle Area (SMA)</strong> for the entire slice (including all muscle groups present).</p>
<p>Given that I am working with these specific single-slice exports where the geometry is already “flattened” to the plane of interest, would the <strong>“Volume / Thickness”</strong> approach be considered valid and numerically reliable in this case? Or is there a more direct way within the <strong>Segment Statistics</strong> module to extract the 2D planar area (based on voxel count) in cm^2 to avoid potential 3D mesh interpolation errors?</p>
<p>Thank you in advance for your help!</p>

---

## Post #4 by @mikebind (2025-12-30 18:41 UTC)

<p>Merry Christmas and a happy holiday season to you as well!</p>
<p>Yes, for the specific use case you are working with, single-slice images, the CSA can be easily calculated by multiplying the CSA of a voxel by the count of voxels.  In this view, the thickness of the slice can be neglected, and the voxels considered as 2D pixels instead.  Segment Statistics can give you the count of these pixels, and you can multiply by the area of each pixel (the product of the non-thickness voxel dimensions).   Alternatively, since you know the slice thickness is 1 mm in your case, you can take the calculated labelmap-based volume from Segment Statistics as the CSA (since the labelmap-based volume is voxel count * voxel volume, and you know that the voxel volume equals the voxel area because the thickness is 1). Both of those methods should produce identical CSA values.  Note that the surface-based volume calculated by Segment Statistics should be similar to the labelmap-based volume, but will typically not be identical because of the smoothing which is usually applied when generating the surface representation from the segment labelmap.</p>
<p>The Segment Statistics surface area for a surface should be a bit greater than double the CSA you would calculate via the suggested method above.  This is because the top surface of the enclosed segment should be approximately the CSA, the bottom surface should be approximately the CSA, and then the side surface will also be added (which should be approximately the slice thickness times the perimeter of the segment).  Because surface smoothing will muck with the exact values and because different perimeter sizes will introduce different errors for different muscle cross-section sizes and shapes, this is not a good method to estimate the CSA.</p>

---
