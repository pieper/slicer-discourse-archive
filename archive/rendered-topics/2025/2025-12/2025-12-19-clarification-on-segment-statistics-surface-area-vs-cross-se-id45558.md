# Clarification on Segment Statistics: Surface Area vs. Cross-Sectional Area (CSA) for Muscle Analysis

**Topic ID**: 45558
**Date**: 2025-12-19
**URL**: https://discourse.slicer.org/t/clarification-on-segment-statistics-surface-area-vs-cross-sectional-area-csa-for-muscle-analysis/45558

---

## Post #1 by @GaetanoGazze (2025-12-19 12:48 UTC)

<p>Hi everyone,</p>
<p>I am performing a quantitative body composition analysis on single-slice CT scans (at the D10 level) using the <strong>Segment Statistics</strong> module in 3D Slicer. I would like to clarify a methodological doubt to ensure the accuracy of my data:</p>
<ol>
<li>
<p><strong>Surface Area vs. CSA:</strong> Can you confirm that the <strong>‘Surface Area’ (mm²)</strong> metric provided by the module refers to the total 3D surface area of the generated mesh (the “envelope” or “shell” of the segment)? In my single-slice analysis, this value is significantly higher than the expected planar area. Is it correct to assume that ‘Surface Area’ should <strong>not</strong> be used as a proxy for the <strong>Cross-Sectional Area (CSA)</strong> or <strong>Skeletal Muscle Area (SMA)</strong>?</p>
</li>
<li>
<p><strong>SMA Calculation:</strong> To derive the <strong>Skeletal Muscle Area (SMA)</strong> in $cm^2$, I am currently taking the <strong>‘Volume’ (mm³)</strong> of the segment and dividing it by the slice thickness (e.g., 1 mm). Is this “Volume / Thickness” conversion considered a standard and reliable method in Slicer to obtain the 2D planar area from a single-slice segmentation?</p>
</li>
</ol>
<p>I want to make sure I am not misinterpreting the geometric outputs of the software, as using the wrong metric would lead to incorrect Skeletal Muscle Index (SMI) calculations.</p>
<p>Thank you in advance for your help!</p>

---
