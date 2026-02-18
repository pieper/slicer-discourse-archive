# What is the method to draw Structure of Slicer Rt?

**Topic ID**: 9585
**Date**: 2019-12-23
**URL**: https://discourse.slicer.org/t/what-is-the-method-to-draw-structure-of-slicer-rt/9585

---

## Post #1 by @11131 (2019-12-23 02:42 UTC)

<p>Hi, I am working with MR DICOM files and RT Structure.</p>
<p>I want to see DICOM and RT Structure in Python.<br>
I’m trying to implement pydicom, not the Slicer module, but the value of Image Orientation Patient in MR data that I have is not (1,0,0,0,1,0), have (0.99, -0.04,0.01,0.043,0.99, -0.01) .</p>
<p>The following formula is used to convert RT Structure points from 3D to 2D.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a094fe44a621f879b7a5ad1b99ccfa998ad506d.png" data-download-href="/uploads/short-url/cQuVfrPacUXKtM5kQlitLN6HYyp.png?dl=1" title="캡처" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a094fe44a621f879b7a5ad1b99ccfa998ad506d.png" alt="캡처" data-base62-sha1="cQuVfrPacUXKtM5kQlitLN6HYyp" width="345" height="154" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">캡처</span><span class="informations">699×313 8.77 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As a result, the structure is off the target in Python as compared to the slicer as shown in the picture on the right.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9631917fd66497e321f2e5d87f19779648b6f0f3.png" alt="캡처1" data-base62-sha1="lqFORadF8nk2OHMlnhZsSbCdsH1" width="491" height="143"></p>
<p>I want to match a structure like the algorithm used by Slicer RT.<br>
Thank you for your help.</p>

---

## Post #2 by @lassoan (2019-12-23 03:06 UTC)

<p>DICOM RT structure set import/export is already implemented in SlicerRT extension.</p>
<p>No need to reimplement this in Python, since everything is already available in Python (the C++ classes are Python-wrapped). In fact, the DICOM import plugin infrastructure is implemented in Python.</p>
<p>If an RTSTRUCT importer that does all the sophisticated and robust processing as SlicerRT (preserves original contour points but interpolates between them smoothly, while supporting keyholes, branching, and provides smooth end-capping) was implemented in Python natively, it would be probably way too slow anyway.</p>

---

## Post #3 by @11131 (2019-12-23 03:32 UTC)

<p>Thank you for your reply.</p>
<p>In fact, what I want is a similar implementation using pydicom in python like Slicer RT.</p>
<p>So I wanted to know how to match the coordinates of the structure used in Slicer RT algorithm.</p>
<p>But if this is difficult, as you replied, I would like to use Slicer RT in python. Are there any pages for reference?</p>

---

## Post #4 by @lassoan (2019-12-23 03:44 UTC)

<p>This topic should help: <a href="https://discourse.slicer.org/t/does-slicer-support-the-batch-processing/2529" class="inline-onebox">Does Slicer support the batch processing?</a>. If you have any remaining questions then let us know.</p>

---
