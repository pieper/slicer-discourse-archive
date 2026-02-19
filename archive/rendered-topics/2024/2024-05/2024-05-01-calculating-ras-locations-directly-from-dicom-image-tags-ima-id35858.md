---
topic_id: 35858
title: "Calculating Ras Locations Directly From Dicom Image Tags Ima"
date: 2024-05-01
url: https://discourse.slicer.org/t/35858
---

# Calculating RAS locations directly from DICOM image tags (ImagePosition/ ImageOrientation)

**Topic ID**: 35858
**Date**: 2024-05-01
**URL**: https://discourse.slicer.org/t/calculating-ras-locations-directly-from-dicom-image-tags-imageposition-imageorientation/35858

---

## Post #1 by @Hesam (2024-05-01 19:45 UTC)

<p>Hello everyone,</p>
<p>I’m currently using 3D Slicer to identify microbleeds in brain MRIs, utilizing RAS coordinates provided in an accompanying Excel file. While manual identification works perfectly, automating the process with Python presents challenges. Specifically, the program inaccurately identifies slices due to discrepancies between the z-coordinate (SliceLocation or ImagePosition) in the DICOM files and the S coordinate from my Excel file.</p>
<p>Given a constant slice thickness of 4 mm, I attempted to correlate the S coordinate with ImagePosition without success. How can I accurately calculate RAS locations directly from ImagePosition or ImageOrientation in the DICOM metadata?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2024-05-01 19:52 UTC)

<p>See computations in the script repository: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-control-point-ras-coordinates" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>If you want to jump to positions defined in an excel file then probably the simplest is to save the positions into a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-control-points-table-file-format-csv-tsv"> Markups control points table CSV file</a>. You can drag-and-drop this file into Slicer and you can jump to a position in <code>Markups</code> module → <code>Control points</code> section. Set <code>Jump Slices</code> → <code>Centered</code> and then click on the point in the table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fd4fa20c9bc9e19656859c2d62d86871f542a84.png" data-download-href="/uploads/short-url/2g3sIXAKqGkbO83D2jlo2Sq4X9G.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd4fa20c9bc9e19656859c2d62d86871f542a84_2_641x500.png" alt="image" data-base62-sha1="2g3sIXAKqGkbO83D2jlo2Sq4X9G" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd4fa20c9bc9e19656859c2d62d86871f542a84_2_641x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd4fa20c9bc9e19656859c2d62d86871f542a84_2_961x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fd4fa20c9bc9e19656859c2d62d86871f542a84_2_1282x1000.png 2x" data-dominant-color="373D42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1848×1441 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Hesam (2024-05-01 21:13 UTC)

<p>Thank you very much for your response.</p>
<p>The suggestion to utilize the Markups module in 3D Slicer for jumping to positions defined in an Excel file is very helpful for manual identification.</p>
<p>However,<br>
when attempting to automatically spot microbleeds using Python scripts, the code prompts for RAS locations. Upon inserting the RAS locations, the code <strong>fails to correlate the S coordinate with the correct slice.</strong> Upon further investigation, I found that the <strong>inherent coordinates</strong> in the file metadata (such as ImagePosition and SliceLocation) <strong>differ</strong> from the S coordinate in my Excel file.</p>
<p>How can I effectively correlate the S coordinate with these metadata values? In other words, how can I teach the code to accurately locate the exact slice based on the entered RAS coordinates?</p>
<p>Your guidance would be greatly appreciated.</p>

---

## Post #4 by @pieper (2024-05-01 21:17 UTC)

<p>This entirely depends on who the S coordinate was calculated in your excel file.  I.e. what software created the file.  If these are MRI for example, if the ImageOrientationPatient vectors are not aligned with patient space the software will have needed to take this into account when calculating the RAS values.</p>

---

## Post #5 by @lassoan (2024-05-01 21:52 UTC)

<p>Only ImagePositionPatient and ImageOrientationPatient DICOM tags are allowed to be used when determining physical location of a pixel of an image slice. SliceLocation field is not relevant for this. In head CTs, it is common to have slices with normals that are not parallel to the IS axis. In such images there is no one-to-one correspondence between ImagePositionPatient and slice number (S coordinate varies within a slice; and one S coordinate appears in several slices).</p>
<p>If RAS positions in your Excel file look correct in Slicer then the problem is in those Python scripts that prompt for RAS locations and don’t find the correct Slice.</p>

---

## Post #7 by @Hesam (2024-05-02 12:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Thank you very much, gentlemen!</p>

---
