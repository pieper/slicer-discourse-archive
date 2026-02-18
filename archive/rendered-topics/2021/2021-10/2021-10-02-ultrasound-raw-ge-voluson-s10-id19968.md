# Ultrasound .RAW GE Voluson S10

**Topic ID**: 19968
**Date**: 2021-10-02
**URL**: https://discourse.slicer.org/t/ultrasound-raw-ge-voluson-s10/19968

---

## Post #1 by @martinus (2021-10-02 11:20 UTC)

<p>Hi,</p>
<p>I’m trying to open a .raw file from a GE Voluson S10. However no luck so far. Any tips regarding the opening of these files or do I need the Dicom files?</p>
<p>kind regards, Martin</p>

---

## Post #2 by @martinus (2021-10-02 14:17 UTC)

<p>Good afternoon,</p>
<p>I’m trying to read the .raw files coming from a GE Voluson S10 Ultrasound Machine. Is that possible or should I really ask for the DICOM files? I don’t know if I can get my hands on them.</p>
<p>Kind Regards,</p>
<p>Martin</p>

---

## Post #3 by @lassoan (2021-10-02 14:22 UTC)

<p>I don’t know what .raw files a GE Voluson creates. If it is RF data (before envelope detection and scan conversion) then it would require quite a lot of proprietary information from GE to properly reconstruct an image from it. Loading 3D/4D ultrasound from DICOM is not a simple task either, but <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md">SlicerHeart extension’s ultrasound readers</a> or the <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess#slicerrawimageguess">RawImageGuess extension</a> may help.</p>

---
