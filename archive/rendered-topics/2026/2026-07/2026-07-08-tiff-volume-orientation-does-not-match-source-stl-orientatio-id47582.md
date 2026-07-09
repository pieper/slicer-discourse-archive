---
topic_id: 47582
title: "TIFF volume orientation does not match source STL orientation"
date: 2026-07-08
url: https://discourse.slicer.org/t/47582
last_bumped: 2026-07-08T21:40:53.508Z
---

# TIFF volume orientation does not match source STL orientation

**Topic ID**: 47582
**Date**: 2026-07-08
**URL**: https://discourse.slicer.org/t/tiff-volume-orientation-does-not-match-source-stl-orientation/47582

---

## Post #1 by @tbugajski (2026-07-08 21:40 UTC)

<p>Hi SAM team,</p>
<p>We have been successfully using SAM to create partial volumes from CT segmentations, track these volumes, and apply the resulting transformations to AUT models in MATLAB to visualize motion.</p>
<p>We are now trying to repeat the same workflow using STL implant models instead of CT segmentations. Our workflow in 3D Slicer (version 5.10.0) is:</p>
<ol>
<li>Load the implant STL model into 3D Slicer.</li>
<li>Convert the model to a segmentation node.</li>
<li>Export the segmentation node as a binary labelmap volume.</li>
<li>In the SAM pre-processing module, set the <strong>Volume Node</strong> to the binary labelmap and the <strong>Segmentation Node</strong> to the STL-derived segmentation.</li>
</ol>
<p>The AUT models, volumes, and transforms are exported successfully. However, after tracking the generated TIFF volumes, applying the resulting transformation matrices to the AUT models produces an incorrect implant orientation.</p>
<p>While investigating, we noticed that the exported TIFF volumes appear to have a different orientation from the original STL model (specifically, a 180° rotation about the Y-axis). In contrast, the TIFF volumes generated from our CT segmentations retain the orientation of the source CT data. The images below show the STL (left) and CT (right) derived models and their associated TIFF volumes from the pre-processing module. Note: the TIFF volumes have been scaled back to match the same dimensions as the models.</p>
<div class="d-image-grid">
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72d59b1e3a8902d80ace2fe406a6e5cf32535ae8.jpeg" data-download-href="/uploads/short-url/gnS4YnZYEYixHyYnkCjMB7bnEF2.jpeg?dl=1" title="STL Model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72d59b1e3a8902d80ace2fe406a6e5cf32535ae8.jpeg" alt="STL Model" data-base62-sha1="gnS4YnZYEYixHyYnkCjMB7bnEF2" width="420" height="485"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">STL Model</span><span class="informations">420×485 30.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ad5b7d297d9cbd287a030f8c726834dfca735d3.jpeg" data-download-href="/uploads/short-url/cXyRojZvLg2LeuWEr4X98Oo9bpx.jpeg?dl=1" title="CT-derived bone model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ad5b7d297d9cbd287a030f8c726834dfca735d3.jpeg" alt="CT-derived bone model" data-base62-sha1="cXyRojZvLg2LeuWEr4X98Oo9bpx" width="512" height="478"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CT-derived bone model</span><span class="informations">512×478 31.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</div>
<p>Could this orientation mismatch be responsible for the incorrect tracking results? If so, is there a recommended workflow for using STL models with SAM that preserves the correct orientation, or an alternative approach that would avoid this issue?</p>
<p>Any guidance would be greatly appreciated.</p>
<p>Thank you,</p>
<p>Tomasz</p>

---
