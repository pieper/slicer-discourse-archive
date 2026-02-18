# Warnings Detected During Load

**Topic ID**: 18125
**Date**: 2021-06-14
**URL**: https://discourse.slicer.org/t/warnings-detected-during-load/18125

---

## Post #1 by @arif (2021-06-14 19:07 UTC)

<p>When I tried to load DICOM file, I am getting this warning below:</p>
<p>'<em>warnings detected during load. examine data in advanced mode for details. load anyway?</em><br>
<em>13: t2_tse_tra_512_p2 [Scalar Volume]: Multi-frame image. If slice orientation or spacing is non-uniform then the image may be displayed incorrectly. Use with caution.</em> ’</p>
<p>Any suggestion?</p>

---

## Post #2 by @pieper (2021-06-15 20:39 UTC)

<p>If the loaded data looks okay, then maybe you can ignore the warning.  It is telling you that the data you have is a multi-frame image, which isn’t very common and Slicer may not be handling any special cases.</p>
<p>If you have specific problems try the troubleshooting guide or follow up with specific questions.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---
