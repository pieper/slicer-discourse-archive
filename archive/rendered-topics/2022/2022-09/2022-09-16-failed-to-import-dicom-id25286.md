---
topic_id: 25286
title: "Failed To Import Dicom"
date: 2022-09-16
url: https://discourse.slicer.org/t/25286
---

# Failed to import dicom

**Topic ID**: 25286
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/failed-to-import-dicom/25286

---

## Post #1 by @nnzzll (2022-09-16 01:59 UTC)

<p>I’m using  DICOM module to import dicom but failed.<br>
The procedure was like: import dicom files → choose folder → patient imported to dicom database → examine series → load.<br>
Everything work fine before <em>load</em>. When I clicked the <em>load</em> button, Slicer returned errors below:</p>
<pre><code class="lang-auto">Imported a DICOM directory, checking for extensions
Loading with imageIOName: GDCM
Could not read scalar volume using GDCM approach.  Error is: FileFormatError
Loading with imageIOName: DCMTK
Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
Could not load: 102001: Unnamed Series as a Scalar Volume
</code></pre>
<p>Here is the screenshot.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1d231fce4d9d3af3773b57712667c5742290987.png" data-download-href="/uploads/short-url/yvfpwpkzTCQVvsDIMceBqLx9nKv.png?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d231fce4d9d3af3773b57712667c5742290987_2_690x355.png" alt="screenshot" data-base62-sha1="yvfpwpkzTCQVvsDIMceBqLx9nKv" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d231fce4d9d3af3773b57712667c5742290987_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d231fce4d9d3af3773b57712667c5742290987_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d231fce4d9d3af3773b57712667c5742290987_2_1380x710.png 2x" data-dominant-color="F2F4F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">1929×994 68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to import single dicom file by the <em>DATA</em> button and it works fine, I don’t know what happens to the DICOM module since I can load the whole directory using other DICOM viewer like RadiAnt</p>
<p>Slicer version: 4.13.0 2021-11-20</p>

---

## Post #2 by @lassoan (2022-09-16 03:57 UTC)

<p>Please use the latest Slicer stable version and follow the instructions provided in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#i-try-to-import-a-directory-of-dicom-files-but-nothing-shows-up-in-the-browser">DICOM module documentation</a>.</p>

---
