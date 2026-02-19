---
topic_id: 39872
title: "Warning Detection 3D Slicer"
date: 2024-10-26
url: https://discourse.slicer.org/t/39872
---

# Warning detection 3d slicer

**Topic ID**: 39872
**Date**: 2024-10-26
**URL**: https://discourse.slicer.org/t/warning-detection-3d-slicer/39872

---

## Post #1 by @Swarna_Yerebairapura (2024-10-26 13:38 UTC)

<p>I face a problem when I import DICOM files of CBCT with Mandibular canal segmentations into 3D Slicer. The mandibular canal tracings were done in the In Vivo software. A window pops up as shown below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92d2e5618b862fe38aafdf90dfa8f13de59af51f.png" data-download-href="/uploads/short-url/kWRyiYyLZT0rhhVrCTkWC8XcXXp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d2e5618b862fe38aafdf90dfa8f13de59af51f_2_690x318.png" alt="image" data-base62-sha1="kWRyiYyLZT0rhhVrCTkWC8XcXXp" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d2e5618b862fe38aafdf90dfa8f13de59af51f_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d2e5618b862fe38aafdf90dfa8f13de59af51f_2_1035x477.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92d2e5618b862fe38aafdf90dfa8f13de59af51f_2_1380x636.png 2x" data-dominant-color="DBE4EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1894×874 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-10-26 13:45 UTC)

<p>These warnings are not a problem for secondary capture images (essentially screenshots) that you don’t want to visualize or process in 3D. Just make sure you don’t use such images.</p>
<p>However, if this happens for CT images or segmentations that you want to use then most likely the In Vivo software creates the DICOM files incorrectly. Please report the issue to the software developers. In the meantime, you can go to <code>Volumes</code> module and in <code>Volume information</code> section make sure the <code>Image spacing</code> values are correct (edit them as needed).</p>

---
