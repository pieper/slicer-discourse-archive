# Unable to read the DICOM "scalar volume" 

**Topic ID**: 45830
**Date**: 2026-01-19
**URL**: https://discourse.slicer.org/t/unable-to-read-the-dicom-scalar-volume/45830

---

## Post #1 by @Samuel_Guigo (2026-01-19 16:45 UTC)

<p>I try to import some dice and the message is :</p>
<p>“Could not load: 8: CT TAP OS  1.5   Br59  4 as a Scalar Volume”</p>
<p>I can read the image folder in a standard image reader…</p>

---

## Post #2 by @lassoan (2026-01-19 18:54 UTC)

<p>You can enable detailed logging in menu: Edit / Application settings / DICOM. If you attempt to load the series again then you may find more information in the application log about what is wrong with the image.</p>

---
