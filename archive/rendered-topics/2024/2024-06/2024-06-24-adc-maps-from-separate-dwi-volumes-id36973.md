# ADC maps from separate DWI volumes?

**Topic ID**: 36973
**Date**: 2024-06-24
**URL**: https://discourse.slicer.org/t/adc-maps-from-separate-dwi-volumes/36973

---

## Post #1 by @hannaho (2024-06-24 10:54 UTC)

<p>Hi all. I have a couple DWI images (b = 0 and b = 1000) from which I would like to determine the ADC values in specific regions. Below is the area I have segmented which I would like to find the ADC value of.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ec4c07b95c2a40690db5800eb1226d144d42c35.jpeg" data-download-href="/uploads/short-url/mEwYIr6pIznBZEroejjzfSD9fSZ.jpeg?dl=1" title="Screenshot 2024-06-24 at 11.50.43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ec4c07b95c2a40690db5800eb1226d144d42c35_2_690x373.jpeg" alt="Screenshot 2024-06-24 at 11.50.43" data-base62-sha1="mEwYIr6pIznBZEroejjzfSD9fSZ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ec4c07b95c2a40690db5800eb1226d144d42c35_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ec4c07b95c2a40690db5800eb1226d144d42c35_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ec4c07b95c2a40690db5800eb1226d144d42c35_2_1380x746.jpeg 2x" data-dominant-color="393736"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-06-24 at 11.50.43</span><span class="informations">1438×778 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I previously followed the <a href="https://spujol.github.io/SlicerDiffusionMRITutorial/SlicerDiffusionMRITutorial_SoniaPujol.pdf" rel="noopener nofollow ugc">DTI tutorial</a> and procedure described by <a href="https://discourse.slicer.org/u/ihnorton">ihnorton</a> on <a href="https://discourse.slicer.org/t/adc-values-on-a-dwi-scan/1352/6">this thread</a>. However, I was unable to produce a mask as described, as the error message kept telling me there was no b0 information (even when I was using the b=0 volume to do this.</p>
<p>I wondered if this was because my DWI volumes are two separate ones? If that’s the cause of the error, is there a way I can combine them so they open as one volume and the mask can detect the b0 images?</p>
<p>The end goal is just to get the ADC value from the high intensity area on the b=1000 image.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2024-06-24 12:35 UTC)

<p>To calculated ADC you need not just B-value images but a full set of gradients too.  From there you can estimate the tensor and calculate the scalar maps.</p>

---

## Post #3 by @hannaho (2024-06-24 14:39 UTC)

<p>Thanks Steve,</p>
<p>And if I had these b-value and gradient images, if they all loaded as separate volumes could I use them somehow? It seems to have an issue with their all being separate image volumes. Is just two (b0 and b1000) DWI images enough to calculate ADC from, or are more b-values needed?</p>

---

## Post #4 by @pieper (2024-06-24 16:33 UTC)

<p>You would need to combine the DWI files like in the SlicerDMRI: <a href="https://dmri.slicer.org/docs/" class="inline-onebox">Documentation</a></p>
<p>Typically you will have a few B volumes and 20 or so diffusion gradient directions.  These are used to estimate tensors and ultimately scalars like ADC.</p>

---
