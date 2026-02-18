# Curved 3D MPR from input coordinates

**Topic ID**: 4080
**Date**: 2018-09-12
**URL**: https://discourse.slicer.org/t/curved-3d-mpr-from-input-coordinates/4080

---

## Post #1 by @LineM (2018-09-12 11:19 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.8.1</p>
<p>I’ve tried to find an answer to this question on the wiki pages, but haven’t been able to find it:<br>
Is it possible to use Slicer to generate a curved 3D multiplanar reconstruction (MPR) from a set of already-defined 3D coordinates? I have a text file containing 3D coordinates for a CT scan, and I would like to use these coordinates to make the MPR. Does anyone know how and if this can be done?</p>

---

## Post #2 by @pieper (2018-09-17 15:03 UTC)

<p>This video shows how to do that: <a href="https://www.youtube.com/watch?v=thExIlffL0I">https://www.youtube.com/watch?v=thExIlffL0I</a></p>

---

## Post #3 by @LineM (2018-09-18 07:43 UTC)

<p>Thank you for your reply - but this video does not do what I want.</p>
<p>They only perform the MPR in 2D (in one axial slice) and they define the coordinates manually. I have a file with already-defined 3D coordinates that I want to load into Slicer and use for the MPR. But I haven’t been able to find that functionality in Slicer</p>

---

## Post #4 by @lassoan (2018-09-18 19:36 UTC)

<aside class="quote no-group" data-username="LineM" data-post="3" data-topic="4080">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/c37758/48.png" class="avatar"> LineM:</div>
<blockquote>
<p>I have a file with already-defined 3D coordinates</p>
</blockquote>
</aside>
<p>Can you save the 3D coordinates in CSV files? Slicer can load markups from CSV files, just change the file extension from csv to fcsv.</p>
<p>In recent Slicer versions, you can also copy-paste markup point positions from Excel (column 1 is an ID, you can leave it empty; column 2, 3, 4 are the RAS coordinates of markups).</p>

---

## Post #5 by @LineM (2018-09-19 05:58 UTC)

<p>Yes, I can save them to .fcsv (adding an extra column) and load them in as markups. But then I’m not able to ‘import’ the markups to the ‘Endoscopy’ module and use them to generate the MPR</p>

---

## Post #6 by @lassoan (2018-09-19 20:02 UTC)

<p>Have you tried selecting the imported fiducial list as “Input fiducials” in Endoscopy module?</p>

---

## Post #7 by @LineM (2018-09-20 12:19 UTC)

<p>I can choose the points as Input fiducials, but when I press ‘Create path’ nothing happens. In the 3D view I can see the points as spheres, but there is no line connecting the points as in the video pieper linked to.</p>

---

## Post #8 by @lassoan (2018-09-20 15:03 UTC)

<p>It works well for me. Maybe something is wrong with the imported markups. Is any error logged? (menu: Help / Report a bug)</p>

---
