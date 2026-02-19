---
topic_id: 21643
title: "Exported Nrrd File Segmentation Misaligned With The Original"
date: 2022-01-26
url: https://discourse.slicer.org/t/21643
---

# Exported NRRD file (segmentation) misaligned with the original DICOM file (MRI).

**Topic ID**: 21643
**Date**: 2022-01-26
**URL**: https://discourse.slicer.org/t/exported-nrrd-file-segmentation-misaligned-with-the-original-dicom-file-mri/21643

---

## Post #1 by @luisfilipeap (2022-01-26 19:48 UTC)

<p>Hello all,</p>
<p>Using the following header I saved my segmentation volume stored in the variable ‘out’ in a NRRD file:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671d7157a9f0f32b6ff581fe3424a65778c6a49f.png" data-download-href="/uploads/short-url/eIcg8nsypODza3kxZiBm56NVOt9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/671d7157a9f0f32b6ff581fe3424a65778c6a49f_2_690x236.png" alt="image" data-base62-sha1="eIcg8nsypODza3kxZiBm56NVOt9" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/671d7157a9f0f32b6ff581fe3424a65778c6a49f_2_690x236.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671d7157a9f0f32b6ff581fe3424a65778c6a49f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/671d7157a9f0f32b6ff581fe3424a65778c6a49f.png 2x" data-dominant-color="F8FAF8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">962×330 27.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Loading both original MRI, and the segmented nrrd volume. We may check that the volume information of both structures are pretty close:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7ff9cd7fba39d74d3caa24ddee0a88a670673c51.png" data-download-href="/uploads/short-url/ig7PZGA65GUN0oVFXziAjAUew25.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7ff9cd7fba39d74d3caa24ddee0a88a670673c51.png" alt="image" data-base62-sha1="ig7PZGA65GUN0oVFXziAjAUew25" width="690" height="245" data-dominant-color="F4F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1302×464 22.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But some information is missing probably in the header file I saved since I couldn’t found a perfect position match between the NRRD and the original DICOM.</p>
<p>Here is how I see the 3D visualization of both volumes.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b5d2999b457fae345558d389d71440e1d097411.png" alt="image" data-base62-sha1="mapBFQ5u07YaYMhCyUuLZsV21Cp" width="475" height="353"></p>
<p>Would you have any idea what I can try next?</p>
<p>thanks a lot</p>

---

## Post #2 by @lassoan (2022-01-26 19:51 UTC)

<p>Slicer uses RAS coordinate system internally (for backward compatibility) but uses LPS in all files (for compatibility with DICOM and other software). You can convert between two coordinate systems by inverting the sign of the first two coordinate values.</p>

---
