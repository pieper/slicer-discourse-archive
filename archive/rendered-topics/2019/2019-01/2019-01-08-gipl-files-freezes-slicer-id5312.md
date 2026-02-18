# Gipl files freezes slicer

**Topic ID**: 5312
**Date**: 2019-01-08
**URL**: https://discourse.slicer.org/t/gipl-files-freezes-slicer/5312

---

## Post #1 by @muratmaga (2019-01-08 20:18 UTC)

<p>I was given two volumes in gipl format (image and labelmap), that I can open with ITKsnap without any problem. When I drag and drop them into Slicer, first it suggests to load them as ‘Scalar Overlay’ as oppose to ‘Volume’.  Regardless of what’s chosen, Slicer stalls. This happens with both stable 4.10 and r27623 on windows 10.</p>
<p>Same volumes exported as NRRD from ITK-Snap loads fine.</p>

---

## Post #2 by @lassoan (2019-01-08 20:38 UTC)

<p>Gipl image loading works fine for me on Windows10 with Slicer-4.10. Can you share one of the images that you had problem with?</p>
<p>I haven’t encountered images in gipl formats in recent years. Where did the data sets come from?</p>

---

## Post #3 by @muratmaga (2019-01-08 21:53 UTC)

<p>It is a recycled data from an older publication. Here is the link:<br>
<a href="https://app.box.com/s/bdtx5ys12un4e1bp5ccee6yl2c2d5589" class="onebox" target="_blank" rel="nofollow noopener">https://app.box.com/s/bdtx5ys12un4e1bp5ccee6yl2c2d5589</a></p>

---

## Post #4 by @lassoan (2019-01-09 02:00 UTC)

<p>Since DICOM files can have any file extensions, when Slicer loads a file, it checks if it can be interpreted as a DICOM file, by calling <code>GDCMImageIO::CanReadFile(const char *filename)</code>. For the attached file, this check takes several minutes, as hundreds of errors are logged. After the check is completed and GDCM library finally realizes that it is not a DICOM file and the file is loaded correctly.</p>
<p>I’ll report this error to ITK: <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/388" rel="nofollow noopener">https://github.com/InsightSoftwareConsortium/ITK/issues/388</a></p>
<p>Until it gets fixed, I would recommend not to use gipl file format. In general, it is probably better to use more common file formats (nrrd, mha, maybe nifti).</p>

---

## Post #5 by @muratmaga (2019-01-09 19:58 UTC)

<p>OK. Thanks. It worked fine with 4.8.1.</p>

---
