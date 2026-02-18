# Discrepancy between image coordinates and seed points centerline extraction

**Topic ID**: 31504
**Date**: 2023-09-01
**URL**: https://discourse.slicer.org/t/discrepancy-between-image-coordinates-and-seed-points-centerline-extraction/31504

---

## Post #1 by @IlvaHou55 (2023-09-01 11:59 UTC)

<p>Hello,</p>
<p>I am using VMTK to extract the hepatic arteries from contrast-enhanced CT scans. After centerline extraction I need to make the connection between the outlets of the centerlines and the original image. While I was working on this, I found out there is a discepancy between the coordinates used in the centerline extraction and the coordinates of the image. Hopefully it is my own mistake, but I cannot seem to find where the problem lies.<br>
As I am not able to share my own data, I am using some open-source CT data and walk you through it. (In this example I am using the vertebra instead of vessels, but it only serves the goal of showing the discepancy):</p>
<p>When using the centerline extractor, I use the point picker to select some landmarks on the generated surface.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdad576cf8658f3f8f9035c2f4cbbc4910060c80.png" alt="Landmarks_on_surface" data-base62-sha1="Ac8bju7nL7hG7dRYFQ75irTC5va" width="598" height="302"></p>
<p>I made sure that vmtkcenterlines.py prints out the pickPositions (line 161) in physical (xyz) coordinates.<br>
The positions were: [[406, 393, 1563],[362, 390, 1562],[412, 391, 1537],[357, 387, 1538]].</p>
<p>I transform these positions to image (ijk) coordinates by transforming to ras coordinates first, following by transforming to ijk coordinates by the following transformation matrices:<br>
XyzToRasMatrixCoefficients = [-1.0, 0.0, 0.0, 382.00000000000017, 0.0, -1.0, 0.0, 222.00000000000009, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]<br>
RasToIjkMatrixCoefficients = [-1.2864321608040201, -0.0, 0.0, 245.70854271356794, -0.0, -1.2864321608040201, -0.0, 142.79396984924628, 0.0, -0.0, 0.5, -747.5, -0.0, 0.0, -0.0, 1.0]</p>
<p>The resulting image (ijk) coordinates are: [[276, 362, 34],[219, 358, 33],[284, 360, 21],[213, 355, 21]].</p>
<p>I looked up these coordinates in the original image using the vmtk image viewer and the crosshair:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9674eb0f157e39365b8e186dc50b1702b933ec28.png" alt="Landmark_1" data-base62-sha1="lt07epJFjUZqINaCfJ3AW7aMdSw" width="590" height="316"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1b9a7b55d9c571d080fdcdacba98027c0f6ce97.png" alt="Landmark_2" data-base62-sha1="rDLUNftw3eCEZJtnr1fvQ6y1GS3" width="580" height="346"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf3f1e82eec1c1e59e53f70da21ce991d48f3bb.png" alt="Landmark_3" data-base62-sha1="sXp67iHBOQ68f4EiSKXfEzHDL9V" width="600" height="356"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a5a0bd0051e2f62762c3db3801fbf01be504e1d.png" alt="Landmark_4" data-base62-sha1="62EYyya9pRZqEDXg0ftJAtr862V" width="597" height="358"></p>
<p>Although not far, they are obviously off.</p>
<p>I cross-checked the transformation from xyz to ijk by setting the ContinuousCursor to true in the image viewer and found the same result. Therefore, I assume the transformation from physical coordinates to image coordinates is not the problem.</p>
<p>Could anyone help my indicate why this goes wrong and what to do to overcome this issue?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2023-09-01 12:01 UTC)

<p>I would recommend to cross-check with results you get in 3D Slicer - install VMTK extension and exteact centerline using “Extract centerline” module.</p>

---

## Post #3 by @IlvaHou55 (2023-09-01 13:07 UTC)

<p>Thank you for your fast suggestion <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>In 3D slicer I have done something similar and found that the EndPointPositions in the Centerline Quantification table match the positions of the markups I have placed, after transforming them from xyz to ijk coordinates.</p>
<p>This would suggest that the issue lies somewhere in the vmtk point seed selector that works differently from the placement of the markups in 3D slicer.</p>
<p>Unfortunately, I cannot use 3D slicer for my purpose, so the question still remains why there is a discrepancy in vmtk point seed selector and the original image.</p>

---

## Post #4 by @lassoan (2023-09-01 13:54 UTC)

<p>I don’t think many people use VMTK’s GUI components, so you may need to investigate and fix any issues in them yourself.</p>
<p>I’m just curious, is there anything specific that prevents you from using Slicer?</p>

---

## Post #5 by @IlvaHou55 (2023-09-04 07:59 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> that is a pity. The reason I posted this is because I seem to be unable to find and fix the issue myself… Do you know if there are developers of the VMTK GUI components active on this platform?</p>
<p>The reason I am not using Slicer is because we might want to incorporate part of it in our own software in a later stage.</p>

---

## Post #6 by @pieper (2023-09-04 14:11 UTC)

<p>I don’t know of anyone actively developing VMTK GUI, but if you use it please do contribute to that project to keep it healthy.  As you’ve seen it’s very complicated to keep all these pieces working.</p>

---
