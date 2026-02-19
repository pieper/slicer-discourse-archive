---
topic_id: 7093
title: "Image Sets Keep Losing Relationship On 3D Model Generation"
date: 2019-06-08
url: https://discourse.slicer.org/t/7093
---

# Image sets keep losing relationship on 3d model generation

**Topic ID**: 7093
**Date**: 2019-06-08
**URL**: https://discourse.slicer.org/t/image-sets-keep-losing-relationship-on-3d-model-generation/7093

---

## Post #1 by @logan74k (2019-06-08 23:53 UTC)

<p>Apologies as I’m new to the program, trying to generate a good resolution brain model.  I have 3 image sets which import with incorrect background selections IE Axial Sagittal Coronal all come in with COR SE T1 + GAD, so Coronal view looks good, but Axial and Sagittal are both very low res, almost previews.</p>
<p>I can correct this in the Axial and Sagittal views by Unlinking slice controls across the viewers, and changing to the AX SE T1 + GAD and SAG SE T1 + GAD, respectively, which makes all three sets appear in high resolution as expected.  I can then create threshold masks from which to create a model.</p>
<p>However, on switching to the model creation module, or even just ‘Apply’ in the threshold menu, it defaults all three image sets back, locking them all to the same background selection I.E.  AX SE T1 + GAD, which distorts two of the views, and reinterprets the threshold masks and therefore the model based on those low res versions.  Hoping this is an easy fix and just a setting I have no knowledge of, vs a basic flaw in the dataset.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abd30c4da7cd713e6254e482a8b9489b24f20845.jpeg" data-download-href="/uploads/short-url/ow1OA35lk9XT17TGHnwswVkon6l.jpeg?dl=1" title="before" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abd30c4da7cd713e6254e482a8b9489b24f20845_2_690x388.jpeg" alt="before" data-base62-sha1="ow1OA35lk9XT17TGHnwswVkon6l" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abd30c4da7cd713e6254e482a8b9489b24f20845_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abd30c4da7cd713e6254e482a8b9489b24f20845_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abd30c4da7cd713e6254e482a8b9489b24f20845_2_1380x776.jpeg 2x" data-dominant-color="8E8E94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">before</span><span class="informations">1920×1080 380 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eec449ab85a642be1fe7f896ac06e24523ac705.jpeg" data-download-href="/uploads/short-url/fPgIRq3HjRHrGrS5daQ4lt7swKN.jpeg?dl=1" title="after" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6eec449ab85a642be1fe7f896ac06e24523ac705_2_690x388.jpeg" alt="after" data-base62-sha1="fPgIRq3HjRHrGrS5daQ4lt7swKN" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6eec449ab85a642be1fe7f896ac06e24523ac705_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6eec449ab85a642be1fe7f896ac06e24523ac705_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6eec449ab85a642be1fe7f896ac06e24523ac705_2_1380x776.jpeg 2x" data-dominant-color="87888E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">after</span><span class="informations">1920×1080 357 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, I get this warning on input of the 3 image sets, which doesn’t mean much to me but may be a clue as to the problem.  Thanks a lot for any help!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/101af1e48d33d50b740232e7d1a869e5a492d0bd.jpeg" data-download-href="/uploads/short-url/2itmRguuXSc8lm7hoHlrBEYa1at.jpeg?dl=1" title="warning" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/101af1e48d33d50b740232e7d1a869e5a492d0bd_2_690x86.jpeg" alt="warning" data-base62-sha1="2itmRguuXSc8lm7hoHlrBEYa1at" width="690" height="86" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/101af1e48d33d50b740232e7d1a869e5a492d0bd_2_690x86.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/101af1e48d33d50b740232e7d1a869e5a492d0bd_2_1035x129.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/101af1e48d33d50b740232e7d1a869e5a492d0bd_2_1380x172.jpeg 2x" data-dominant-color="EFEFE9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">warning</span><span class="informations">1424×178 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-06-09 02:34 UTC)

<p>You cannot directly utilize information in these 3 sparse volumes. See details and explanation <a href="https://discourse.slicer.org/t/3d-model-from-dicoms/5478/2">here</a>.</p>
<p>In theory, it may be possible to reconstruct a single higher-quality volume from multiple anisotropic volumes (see for example <a href="https://ieeexplore.ieee.org/document/7829267" rel="nofollow noopener">this paper</a>) but I’m not aware of any implementation that we may use.</p>
<p>The warning looks harmless (very little variation in slice spacing).</p>

---
