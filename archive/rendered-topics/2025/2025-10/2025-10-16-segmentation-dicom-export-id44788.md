# Segmentation DICOM export

**Topic ID**: 44788
**Date**: 2025-10-16
**URL**: https://discourse.slicer.org/t/segmentation-dicom-export/44788

---

## Post #1 by @CSalt (2025-10-16 22:33 UTC)

<p>I am working in slicer 5.9.0 (though I have also used 5.8.0) and I am trying to export PET Segmentations to DICOM. I did not have luck using CLI to export segmentations or the PET labelmap. I have the SlicerRT extension, but I seem to be missing the DICOMSegmentationPlugin. When I try to use the DICOM Export feature, the only export type options I see are Scalar Volume, RT, and Slicer data bundle, not SEG. If anyone is able to advise me in this matter I would greatly appreciate it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ade2c53b3fff876f098c19d9bdc6a0a45a2d22ac.png" data-download-href="/uploads/short-url/oOgsg70JS7FdZrwxjOlbacu7NMw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ade2c53b3fff876f098c19d9bdc6a0a45a2d22ac.png" alt="image" data-base62-sha1="oOgsg70JS7FdZrwxjOlbacu7NMw" width="569" height="322"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">569×322 7.11 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-10-17 08:01 UTC)

<p>The DICOM Segmentation Object support is in the Quantitative Reporting extension. Please install that and try again.</p>

---
