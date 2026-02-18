# nrrd segmentation file error

**Topic ID**: 43292
**Date**: 2025-06-10
**URL**: https://discourse.slicer.org/t/nrrd-segmentation-file-error/43292

---

## Post #1 by @SDV (2025-06-10 16:42 UTC)

<p>Version 5.8.0</p>
<p>Slicer crashed while using paint brush in a segmentation, and now the nrrd segmentation file seems corrupt and I can’t seem to load it in any way. Any help please?</p>
<p>The message detail is:<br>
Exception thrown in event: C:\D\S\S-0-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx:771:<br>
ITK ERROR: NrrdImageIO(000001A6262E3420): Read: Error reading MYLOCATION\Segmentation.seg.nrrd:</p>
<p>[nrrd] nrrdLoad: trouble reading “MYLOCATION/Segmentation.seg.nrrd”</p>
<p>[nrrd] nrrdRead: trouble</p>
<p>[nrrd] _nrrdRead: trouble reading NRRD file</p>
<p>[nrrd] _nrrdFormatNRRD_read:</p>
<p>[nrrd] _nrrdEncodingGzip_read: expected 36502868255 bytes but received 32668896932</p>

---
