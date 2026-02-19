---
topic_id: 22648
title: "Cortical Bone Thickness Measurement"
date: 2022-03-23
url: https://discourse.slicer.org/t/22648
---

# Cortical bone thickness measurement

**Topic ID**: 22648
**Date**: 2022-03-23
**URL**: https://discourse.slicer.org/t/cortical-bone-thickness-measurement/22648

---

## Post #1 by @TommyTurner (2022-03-23 09:55 UTC)

<p>Hello everyone !<br>
I am currently working on cortical bone fissuration and to do so, i have to extract the volume of cortical bone from the femoral diaphysis to conduct finite element analysis.<br>
As geometry of the bone plays a big part on its mechanical properties, i am trying several segmentation methods to analyse the geometrical variation of the models in function of the segmentations parameters.       I have now three STL files segmented with different methods, with different visible thicknesses and i would like to compute precisely the thickness variation between  those models.<br>
I tried several approach to conduct thickness mapping compuration such as bone thickness mapping, DanielsonDistanceMap, Binarythinning or Probe Volume With Model but all those did not work on my computer.<br>
As my need is, i think, really basic, do you know how could I proceed it ?</p>
<p>Here to image wath are the geoometrycal variations, a picture of two models superimposed with the thicker in red in transaprency and the thinner in yellow :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5b425905afb260d6e403a0dc621af1d0c34acce.png" data-download-href="/uploads/short-url/uuvF9ERds1bSIZCQRooGpI1bUei.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5b425905afb260d6e403a0dc621af1d0c34acce_2_525x499.png" alt="1" data-base62-sha1="uuvF9ERds1bSIZCQRooGpI1bUei" width="525" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5b425905afb260d6e403a0dc621af1d0c34acce_2_525x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5b425905afb260d6e403a0dc621af1d0c34acce_2_787x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5b425905afb260d6e403a0dc621af1d0c34acce.png 2x" data-dominant-color="72644E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">945×899 367 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/903d5d167bf0510cff8c1f98d8c34fea56d973d0.png" data-download-href="/uploads/short-url/kA0e3rMpPYfVBNpAde7ObB127iU.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/903d5d167bf0510cff8c1f98d8c34fea56d973d0_2_158x500.png" alt="2" data-base62-sha1="kA0e3rMpPYfVBNpAde7ObB127iU" width="158" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/903d5d167bf0510cff8c1f98d8c34fea56d973d0_2_158x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/903d5d167bf0510cff8c1f98d8c34fea56d973d0_2_237x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/903d5d167bf0510cff8c1f98d8c34fea56d973d0.png 2x" data-dominant-color="958A7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">268×848 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you in advance for your help !</p>

---
