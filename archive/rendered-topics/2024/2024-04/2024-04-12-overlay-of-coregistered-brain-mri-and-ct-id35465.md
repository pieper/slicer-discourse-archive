# Overlay of coregistered brain MRI and CT

**Topic ID**: 35465
**Date**: 2024-04-12
**URL**: https://discourse.slicer.org/t/overlay-of-coregistered-brain-mri-and-ct/35465

---

## Post #1 by @Kerezoudis (2024-04-12 22:09 UTC)

<p>Operating system: MacOs Sonoma 14.4.1<br>
Slicer version: 5.6.1<br>
Expected behavior: I would like to overlay preoperative brain MRI with postoperative CT (after electrode placement)<br>
Actual behavior: images are not aligned.</p>
<p>Plase see screenshow below. I would like to overlay preoperative T1 MRI (top left) with postoperative CT (top right). Images have already been co-registered in SPM, and alignment looks great in MRICrogl (bottom left). For some reason, the two images look completely out of place with each other in 3D slicer (I tried cropping out unnecessary volume too, but with no sucsess). Any help would be greatly appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/868e1e542ebb7c552efeb57fa48d1b1baf95ea9e.jpeg" data-download-href="/uploads/short-url/jckt2LEUKYKYvEXrSk4chSxAgF0.jpeg?dl=1" title="3DSlicer_q" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/868e1e542ebb7c552efeb57fa48d1b1baf95ea9e_2_635x500.jpeg" alt="3DSlicer_q" data-base62-sha1="jckt2LEUKYKYvEXrSk4chSxAgF0" width="635" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/868e1e542ebb7c552efeb57fa48d1b1baf95ea9e_2_635x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/868e1e542ebb7c552efeb57fa48d1b1baf95ea9e_2_952x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/868e1e542ebb7c552efeb57fa48d1b1baf95ea9e_2_1270x1000.jpeg 2x" data-dominant-color="525251"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3DSlicer_q</span><span class="informations">2640×2076 476 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-04-12 22:32 UTC)

<p>Describe what step you used to register the images.  In Slicer you should just be able to right click on one in the Data module, pick Register this and then right click to select the  other and then click apply.</p>

---
