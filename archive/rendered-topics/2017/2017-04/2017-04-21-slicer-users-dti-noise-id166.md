---
topic_id: 166
title: "Slicer Users Dti Noise"
date: 2017-04-21
url: https://discourse.slicer.org/t/166
---

# [slicer-users] dti noise

**Topic ID**: 166
**Date**: 2017-04-21
**URL**: https://discourse.slicer.org/t/slicer-users-dti-noise/166

---

## Post #1 by @ihnorton (2017-04-21 15:41 UTC)

<p><code>from gabriele pasqua on slicer-users</code></p>
<p>Hi,<br>
I have computed the DTI images starting from the DWI image, but it seems to be too noisy. What can I do to improve the image quality?</p>
<p>I attached both the DWI image and the DTI computed.</p>
<p>thanks in advance<br>
Gabriel</p>
<details>
<summary>
DWI</summary>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfb23802bce43af97bc9ff0d9613860e95098aef.jpeg" data-download-href="/uploads/short-url/vUUj5BHrjFOrtAQZ4pmlrnN5sKj.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb23802bce43af97bc9ff0d9613860e95098aef_2_547x499.jpeg" alt="image" data-base62-sha1="vUUj5BHrjFOrtAQZ4pmlrnN5sKj" width="547" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb23802bce43af97bc9ff0d9613860e95098aef_2_547x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dfb23802bce43af97bc9ff0d9613860e95098aef_2_820x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfb23802bce43af97bc9ff0d9613860e95098aef.jpeg 2x" data-dominant-color="383838"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1093×998 79 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</details>
<p>[details=DTI]<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa180739da8556089484b9a3262e6837a721f969.jpeg" data-download-href="/uploads/short-url/zGqQz8qZOBBHJlCCZb8cxjyIpL3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa180739da8556089484b9a3262e6837a721f969_2_547x499.jpeg" alt="image" data-base62-sha1="zGqQz8qZOBBHJlCCZb8cxjyIpL3" width="547" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa180739da8556089484b9a3262e6837a721f969_2_547x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa180739da8556089484b9a3262e6837a721f969_2_820x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa180739da8556089484b9a3262e6837a721f969.jpeg 2x" data-dominant-color="050707"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1093×998 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>[/details]</p>

---

## Post #2 by @ihnorton (2017-04-21 15:41 UTC)

<p>Hi Gabriele,<br>
This is very dependent on your scanner and protocol details. You may need to contact a local MR expert to investigate. As a first pass, you could manually inspect each of the gradient directions in the Volumes module to see if there is any consistent pattern of signal dropout or speckle (which could be caused by RF interference, for example).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/0bd8ca74c2f02b15679a91665072b8b6d70e2c77.png" width="557" height="156"></p>

---
