# "failed to set suffix" error following DICOM anonymization 

**Topic ID**: 5404
**Date**: 2019-01-17
**URL**: https://discourse.slicer.org/t/failed-to-set-suffix-error-following-dicom-anonymization/5404

---

## Post #1 by @chloe (2019-01-17 17:41 UTC)

<p>Hi,</p>
<p>I have some anonymized DICOM files that I am trying to load into Slicer. I can load the studies into the DICOM browser. However, when I try to display them, I get the following error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ec5eec6c8c2a7168408c156ae36fda1c00db566.png" data-download-href="/uploads/short-url/dwoWY6EFJN08zv1VLU4gnxJdZH0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ec5eec6c8c2a7168408c156ae36fda1c00db566_2_439x500.png" alt="image" data-base62-sha1="dwoWY6EFJN08zv1VLU4gnxJdZH0" width="439" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ec5eec6c8c2a7168408c156ae36fda1c00db566_2_439x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ec5eec6c8c2a7168408c156ae36fda1c00db566.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ec5eec6c8c2a7168408c156ae36fda1c00db566.png 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">570×648 48.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>More details on how I’m anonymizing the data:</p>
<ul>
<li>Instead of deleting/replacing PHI, I create a new DICOM file and only copy/replace what I need to. This is very similar to what’s done <a href="https://github.com/16-Bit-Inc/dicom-anonymizer" rel="noopener nofollow ugc">here</a></li>
<li>I have verified that I am including all of the required DICOM fields, as specified <a href="https://www.pclviewer.com/help/required_dicom_tags.htm" rel="noopener nofollow ugc">here</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" rel="noopener nofollow ugc">here</a></li>
<li>I have tried different DICOM readers (DCMTK vs GDCM), but both lead to the same error.</li>
</ul>
<p>I am using <strong>Slicer 4.8.1</strong>.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2019-01-17 18:36 UTC)

<p>You might have better luck with the latest release or nightly version, but probably there’s something incorrectly formatted in the anonymized data.  I’d suggest using <a href="http://www.dclunie.com/pixelmed/software/webstart/DicomCleanerUsage.html" rel="nofollow noopener">DicomCleaner</a>.  At least use that for debugging your script.</p>

---
