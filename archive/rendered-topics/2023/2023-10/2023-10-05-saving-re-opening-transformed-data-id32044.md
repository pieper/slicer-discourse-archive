---
topic_id: 32044
title: "Saving Re Opening Transformed Data"
date: 2023-10-05
url: https://discourse.slicer.org/t/32044
---

# Saving/re-opening transformed data

**Topic ID**: 32044
**Date**: 2023-10-05
**URL**: https://discourse.slicer.org/t/saving-re-opening-transformed-data/32044

---

## Post #1 by @tybone2323 (2023-10-05 02:32 UTC)

<p>When I transform my data and harden the transform, the next time I load the data it is no longer oriented in the way I switched it to. Does anyone know what is happening?<br>
(I’m on Windows)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2d89657f12f1c7a22236a7354b17e0be3cbfb5b.jpeg" data-download-href="/uploads/short-url/yEjAcIKa2LqbuKRyx0xN56MxFEf.jpeg?dl=1" title="IMG-3428" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2d89657f12f1c7a22236a7354b17e0be3cbfb5b_2_690x425.jpeg" alt="IMG-3428" data-base62-sha1="yEjAcIKa2LqbuKRyx0xN56MxFEf" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2d89657f12f1c7a22236a7354b17e0be3cbfb5b_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2d89657f12f1c7a22236a7354b17e0be3cbfb5b_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2d89657f12f1c7a22236a7354b17e0be3cbfb5b_2_1380x850.jpeg 2x" data-dominant-color="89868B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG-3428</span><span class="informations">1920×1183 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/030f3ab4e09eb097ba6039a5342a75f9525dc249.jpeg" data-download-href="/uploads/short-url/r43MO5wsGjrsUytpZTK8bdYgyZ.jpeg?dl=1" title="IMG-3429" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/030f3ab4e09eb097ba6039a5342a75f9525dc249_2_690x411.jpeg" alt="IMG-3429" data-base62-sha1="r43MO5wsGjrsUytpZTK8bdYgyZ" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/030f3ab4e09eb097ba6039a5342a75f9525dc249_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/030f3ab4e09eb097ba6039a5342a75f9525dc249_2_1035x616.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/030f3ab4e09eb097ba6039a5342a75f9525dc249_2_1380x822.jpeg 2x" data-dominant-color="8B888C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG-3429</span><span class="informations">1920×1144 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2023-10-05 17:54 UTC)

<p>I suspect that what may be happening is that you are reloading the data from DICOM, using the DICOM Browser?  When you load an image from the DICOM browser, you are, from that point on, working with an imported copy of that image data, and any modifications you make are to that copy, not to the original data.   When you save, using the Save dialog box, you are saving that modified copy, but not saving it back to the DICOM database, instead you are saving it to a different format (.nrrd by default) and in a different location.  If you load the saved scene file (.mrml file extension), you will see that the loaded version is as it was when you saved it (transformed).  If you load from the DICOM browser, you will be reloading the original (un-transformed) image data.</p>
<p>I understand why this might seem confusing.  DICOM is intended to be an archival, non-modifiable format.  If you load an image from DICOM and then make a change, then according to the DICOM standard, you shouldn’t save it back to the same files because it is not the same data and at least some of the associated metadata is no longer correct (at minimum, all new data should have unique UIDs).</p>

---

## Post #3 by @ebrahim (2023-10-05 17:55 UTC)

<p>The view that’s being used in red/green/yellow slice views might not be what you expect. Check the view described in this dropdown:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/857960c417e3fa5e409eaaa2153d48eeba86210e.png" alt="image" data-base62-sha1="j2LyokXKVp6ZaGvPKjrfuhTbqvI" width="455" height="115"></p>
<p>So the image transformation may be there no problem, and it’s just the default view directions re-aligning after you re-load the data</p>

---
