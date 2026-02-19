---
topic_id: 30760
title: "Color Scale For Segmentations"
date: 2023-07-24
url: https://discourse.slicer.org/t/30760
---

# Color scale for segmentations

**Topic ID**: 30760
**Date**: 2023-07-24
**URL**: https://discourse.slicer.org/t/color-scale-for-segmentations/30760

---

## Post #1 by @lvdw (2023-07-24 12:35 UTC)

<p>Operating system: MacOS<br>
Slicer version: 5.2.2</p>
<p>I originally had two DICOM series of a CT head: one is the original scan and the second is a processed series that shows some kind of map of hypodensities. I could not make a direct overlay in Slicer with the DICOM on DICOM so I used dicom2nifty in a python script and made the overlay by importing it as a segmentation. Now I have 3 questions:</p>
<ol>
<li>Is there a way to make an overlay in Slicer from DICOMs directly?</li>
<li>Each time it picks default colors for the loaded segmentations, but it should actually be a blue to red colorscale. I only found the colorscale option for volumes but not segmentations. Is there a way I can do this with segmentations? And can I do this each time I import a .nii file as segmentation if it has a certain amount of layers?</li>
<li>I’m not interested in adding parts to the segmentation, but mostly in removing artefacts. Is there an easy way to use the segmentation tools, e.g. the erase tool, on all segmentations at once?</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c4d821684cc52b621901d387e95b95fbe1cdacd.jpeg" data-download-href="/uploads/short-url/k1aUbTMwYdWFqOd1Eg0ITe9B0Xr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c4d821684cc52b621901d387e95b95fbe1cdacd_2_690x386.jpeg" alt="image" data-base62-sha1="k1aUbTMwYdWFqOd1Eg0ITe9B0Xr" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c4d821684cc52b621901d387e95b95fbe1cdacd_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c4d821684cc52b621901d387e95b95fbe1cdacd_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c4d821684cc52b621901d387e95b95fbe1cdacd_2_1380x772.jpeg 2x" data-dominant-color="272725"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1906×1069 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-07-24 15:45 UTC)

<p>It seems that your image is not a segmentation but a scalar overlay. You can load that as a “Volume”, choose a nice colormap for its display in Volumes module, and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#overlay-two-volumes">set it as Foreground volume</a> to show it above the brain image.</p>

---

## Post #3 by @lvdw (2023-07-25 07:21 UTC)

<p>Thank you, but now it’s not possible to edit the volume as I could do with segmentations. E.g. the part within the ventricle is not what I am looking for so I would like to be able to manually remove artefacts from the volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f1c17158559bb9fa74032afad6fcffb1f8a275e.jpeg" data-download-href="/uploads/short-url/90igl6qcOV95DIo2ieyPuEuRrMq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f1c17158559bb9fa74032afad6fcffb1f8a275e_2_690x386.jpeg" alt="image" data-base62-sha1="90igl6qcOV95DIo2ieyPuEuRrMq" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f1c17158559bb9fa74032afad6fcffb1f8a275e_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f1c17158559bb9fa74032afad6fcffb1f8a275e_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f1c17158559bb9fa74032afad6fcffb1f8a275e_2_1380x772.jpeg 2x" data-dominant-color="1D2142"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1906×1069 87 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is that possible?</p>
<p>The background is now always coloured as well, which is not needed. Wouldn’t it be better to work with it as a segmentation?</p>

---

## Post #4 by @lvdw (2023-07-25 09:40 UTC)

<p>In the end the goal with these maps will be to remove artefacts en then use the automatically contoured area as ‘the lesion’, so therefore I think a segmentation would be more ideal?</p>

---
