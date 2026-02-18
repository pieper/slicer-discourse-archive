# Help needed for segmenting an atrophic maxilla in 3D Slicer (for 3D printing)

**Topic ID**: 43922
**Date**: 2025-08-01
**URL**: https://discourse.slicer.org/t/help-needed-for-segmenting-an-atrophic-maxilla-in-3d-slicer-for-3d-printing/43922

---

## Post #1 by @piero_perez (2025-08-01 06:58 UTC)

<p>I’m a dental student currently learning how to use 3D Slicer.</p>
<p>My father, who is an implantologist, asked me to 3D print an atrophic maxilla based on a CT scan.</p>
<p>I’m using the Segment Editor module. I’ve already tried applying thresholds around 300 HU and even lower, but the bone still appears incomplete or hollow, especially around the alveolar ridge and other thin cortical areas.</p>
<p>I’ve also tried manual painting, using smoothing, and adjusting the editable area, but I still can’t get a clean, solid segmentation suitable for 3D printing.</p>
<p>I’m attaching some images to show exactly what’s going wrong.</p>
<p>Has anyone here successfully segmented severely atrophic maxillae? I’d really appreciate any advice or workflow suggestions.</p>
<p>Saludos from Lima, Peru and thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61bb7fe86c719f5c0f9c242ea1eb20b9cfd033b1.jpeg" data-download-href="/uploads/short-url/dWA1UeZE0R2AMi58NcWCkwfeTdL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61bb7fe86c719f5c0f9c242ea1eb20b9cfd033b1_2_375x500.jpeg" alt="image" data-base62-sha1="dWA1UeZE0R2AMi58NcWCkwfeTdL" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61bb7fe86c719f5c0f9c242ea1eb20b9cfd033b1_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61bb7fe86c719f5c0f9c242ea1eb20b9cfd033b1_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61bb7fe86c719f5c0f9c242ea1eb20b9cfd033b1_2_750x1000.jpeg 2x" data-dominant-color="737F78"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×2560 902 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>—Piero</p>

---

## Post #2 by @GeneRisi (2025-08-03 19:26 UTC)

<p>My experience is very limited - I printed a series based on a temporal bone flap that underwent aseptic resorption, and this reminds me of what I saw, with the exception that there still was a single bone flap portion. My approach would be to ask myself what is holding those seemingly discrete sections of bone in position? If the resorption is so severe that soft tissue is what is holding the maxillary remnants in place, you won’t be able to print it as a single structure (but perhaps could print it as more than one STL file with the files properly registered). You can create a notch filter for the CT data that would eliminate the HU range associated with bone and might be able to segment whatever is apparently holding the pieces in place. Is that helpful?</p>

---
