# Nifti data from the HCP import via DWI Convert Module

**Topic ID**: 12913
**Date**: 2020-08-09
**URL**: https://discourse.slicer.org/t/nifti-data-from-the-hcp-import-via-dwi-convert-module/12913

---

## Post #1 by @hercp (2020-08-09 02:23 UTC)

<p>I’m using 3D Slicer 4.10.2 on a Windows 10 system.  I’m trying to convert DTI Nifti data from the HCP import via DWI Convert Module (the data come from <a href="http://www.humanconnectomeproject.org/" rel="nofollow noopener">http://www.humanconnectomeproject.org/</a>)</p>
<p>I receive the following errors:</p>
<p><em>Diffusion-weighted DICOM Import (DWIConvert) standard error:</em></p>
<p><em>E: DcmElement: Unknown Tag &amp; Data (2035,3031) larger (824193072) than remaining bytes in file</em></p>
<p><em>W: DcmItem: Length of element (2d20,2e30) is odd</em></p>
<p><em>E: DcmElement: Unknown Tag &amp; Data (2d20,2e30) larger (925906485) than remaining bytes in file</em></p>
<p><em>W: DcmItem: Dataset not in ascending tag order, at element (0000,0000)</em></p>
<p><em>W: DcmItem: Element (0000,0000) found twice in one data set or item, ignoring second entry</em><br>
<em>…</em></p>

---

## Post #2 by @pieper (2020-08-10 15:58 UTC)

<p>Hi -</p>
<p>That tool is for dicom.  You probably want to use these tools instead: <a href="https://github.com/pnlbwh/conversion">https://github.com/pnlbwh/conversion</a></p>
<p>Also get the latest Slicer nightly preview 4.11</p>

---
