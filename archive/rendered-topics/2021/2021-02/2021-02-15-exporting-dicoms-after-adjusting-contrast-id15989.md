# Exporting DICOMS after adjusting contrast

**Topic ID**: 15989
**Date**: 2021-02-15
**URL**: https://discourse.slicer.org/t/exporting-dicoms-after-adjusting-contrast/15989

---

## Post #1 by @kandrade (2021-02-15 03:04 UTC)

<p>Hello, I’ve been having some  difficulty exporting a DICOM series after I’ve adjusted contrast of my  MRI scans.  I’m able to export the DICOM  series  by right clicking on the subject and selecting  export to file server. However, once I open the exported files onto server to  make  sure the image is clear, it reverts back to the highly contrasted image. Is there a way to save these changes?  Also If I just select Export to DICOM after right clicking on  the node/loaded data window, I receive an error message that says  "Empty  modality  for series “…” " Any suggestions?</p>

---

## Post #2 by @lassoan (2021-02-15 03:13 UTC)

<aside class="quote no-group" data-username="kandrade" data-post="1" data-topic="15989">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/ecccb3/48.png" class="avatar"> kandrade:</div>
<blockquote>
<p>I’m able to export the DICOM series by right clicking on the subject and selecting export to file server. However, once I open the exported files onto server to make sure the image is clear, it reverts back to the highly contrasted image.</p>
</blockquote>
</aside>
<p>Recent Slicer Preview Release saves the recommended brightness/contrast in DICOM fields (0028,1050) and (0028,1051). If your DICOM viewer interprets these values correctly then the image should appear with the same brightness/contrast as in Slicer by default. This is just a default visualization option, though, so you don’t need to worry too much about it (user is allowed to adjust it).</p>
<aside class="quote no-group" data-username="kandrade" data-post="1" data-topic="15989">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/ecccb3/48.png" class="avatar"> kandrade:</div>
<blockquote>
<p>If I just select Export to DICOM after right clicking on the node/loaded data window, I receive an error message that says "Empty modality for series “…”</p>
</blockquote>
</aside>
<p>If you use a recent Slicer Preview Release, then in “Edit DICOM tags” section set the correct value in “Modality” field.</p>

---
