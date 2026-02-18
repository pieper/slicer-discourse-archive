# Changing the Hounsfield unit in a DICOM CT image

**Topic ID**: 42370
**Date**: 2025-03-30
**URL**: https://discourse.slicer.org/t/changing-the-hounsfield-unit-in-a-dicom-ct-image/42370

---

## Post #1 by @azam (2025-03-30 08:05 UTC)

<p>Hi everyone<br>
I have a CT image in DICOM format that I exported it from Brachytherapy treatment planning system. I want to remove the Brachy applicators from the CT image. In other words, I want to change its Hounsfield unit  to a desired value of zero. I have no idea about this. Can you guide me?<br>
Thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d12674bd377bd84456442d89fef4a86d54973d95.png" data-download-href="/uploads/short-url/tQeblg7jsgoNqskDYbG4KWRsIhn.png?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d12674bd377bd84456442d89fef4a86d54973d95_2_517x199.png" alt="Screenshot_1" data-base62-sha1="tQeblg7jsgoNqskDYbG4KWRsIhn" width="517" height="199" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d12674bd377bd84456442d89fef4a86d54973d95_2_517x199.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d12674bd377bd84456442d89fef4a86d54973d95_2_775x298.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d12674bd377bd84456442d89fef4a86d54973d95_2_1034x398.png 2x" data-dominant-color="5B5A59"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1404×542 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-03-30 14:08 UTC)

<p>You can use the Masking effect in the Segment Editor for that.</p>

---

## Post #3 by @Eka_Mulyani (2025-05-15 03:52 UTC)

<p>Hi, I am a beginner using 3DSlicer. I worked on the nrrd file to dicom, after I checked in TPS, the HU value is still 0 and 1. How do I set the HU so that the value obtained is around 200</p>

---
