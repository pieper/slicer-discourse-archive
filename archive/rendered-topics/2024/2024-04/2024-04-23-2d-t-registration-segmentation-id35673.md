# 2D+t registration/segmentation

**Topic ID**: 35673
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/2d-t-registration-segmentation/35673

---

## Post #1 by @ffournier13 (2024-04-23 10:01 UTC)

<p>Hi,</p>
<p>I’m trying to segment/register a 2D+t MRI of the stomach to study the peristalsis propagation waves. I’ve followed this video tutorial for 3D+t images: <a href="https://www.youtube.com/watch?v=qVgXdXEEVFU&amp;t=66s" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=qVgXdXEEVFU&amp;t=66s</a>. I’ve tried to make it work, but I’m not having any luck.</p>
<p>Any advice would be greatly appreciated!<br>
I’ve found some examples of people using FSLeyes and changing the t dimension as a z dimension to segment the same way they would with classical 2D MRI with multiple slices, but I do prefer the slicer 3D environment which I am getting used to. Is there any way to do the same process in 3D slicer (with an automatic or semi-automatic segmentation)? I’d love to have similar results to the video above, but with only two dimensions. It would be great to have a surface changing in function of time, or even a surface with an x/y plane and a time axis instead of the z one.</p>
<p>Thank you in advance for your help!</p>
<p>Here is a few screenshot to give you an idea of the data I have :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9adac8b41102f5ea9736c749ab1b725043d4bb1c.jpeg" alt="image" data-base62-sha1="m5UgVq41UhjcFdQ4bbPTJkdfSji" width="574" height="434"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4920db11e6cd77526cb0c4661aee5bcf7f2dfaff.jpeg" alt="image" data-base62-sha1="aqVfp1rfcuSud9j1dZGCiKSnMbJ" width="597" height="467"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42833707e7582430af8bbc907b86619c9ff7bb89.jpeg" data-download-href="/uploads/short-url/9uoDFrDPOX5IdVnSq6dG61dDLfP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42833707e7582430af8bbc907b86619c9ff7bb89.jpeg" alt="image" data-base62-sha1="9uoDFrDPOX5IdVnSq6dG61dDLfP" width="577" height="500" data-dominant-color="626662"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">599×519 40.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-04-23 20:13 UTC)

<p>Did you try loading them as a volume and using the 3D tools?</p>

---

## Post #3 by @ffournier13 (2024-04-24 07:40 UTC)

<p>Thank you for your answer !<br>
Yes, I tried to edit the prefered multivolume format (that was in default (volume sequence) ). i tried the three options with the same result. By the way, I didin’t precised it but I am using Slicer 5.6.1.<br>
My data look like this when I examin them in the dicom browser :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae21ebb7263ff88efac97a025fe08b8ce40e5a42.png" alt="image" data-base62-sha1="oQrKNi5vNqIyWzy5CwnV0zvXBei" width="470" height="105"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd4131f850a1ccc4a8ec9b65e882ab7d46d349fc.png" alt="image" data-base62-sha1="A8otLrKiOVk0mCm78cVDcyeD5VO" width="467" height="102"></p>
<p>With 317 frames in scalar volume (that load separetly if i load them instead of the multivolume).<br>
Do you have any idea on how to solve this issue ?<br>
Thank you very much for your help !</p>

---

## Post #4 by @pieper (2024-04-24 12:48 UTC)

<p>I was thinking you could try the ScalarVolume option and get the time series to load as a single volume that perhaps could be segmented as if it were 3D.  If that’s not working with the data as-is you may need to develop some tricks or workarounds since your data is not the kind that Slicer’s been programmed to handle.  You might try the DICOM Patcher or it’s possible you’ll need a small script to convert the data headers to make it work.</p>

---
