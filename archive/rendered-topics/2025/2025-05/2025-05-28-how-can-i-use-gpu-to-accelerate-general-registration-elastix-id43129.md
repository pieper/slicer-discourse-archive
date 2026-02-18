# How can I use GPU to accelerate General Registration (Elastix) module?

**Topic ID**: 43129
**Date**: 2025-05-28
**URL**: https://discourse.slicer.org/t/how-can-i-use-gpu-to-accelerate-general-registration-elastix-module/43129

---

## Post #1 by @LanceDuan (2025-05-28 07:52 UTC)

<p>Hi all,<br>
I’m using General Registration (Elastix) to align two different time DICOM CT of one patient, and it works very well!<br>
However it takes such a long time, about 5min. I checked the CPU and GPU usage status. As you can see in the figures, memory is consumed 84% while GPU is only about 14%. How can I use more GPU to process this module?<br>
Info of my computer is:</p>
<ol>
<li>CPU: 13th Gen Intel(R) Core™ i7-13650HX 2.60GHz</li>
<li>RAM: 16.0GB</li>
<li>GPU: NVIDIA GeForce RTX 4060 Laptop 8GB</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b852497d3ad1f4aa9ca2c0fc18e28220081df5b9.png" data-download-href="/uploads/short-url/qiA9xaEJXapJKb0MjkFK3dUoXNf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b852497d3ad1f4aa9ca2c0fc18e28220081df5b9_2_626x500.png" alt="image" data-base62-sha1="qiA9xaEJXapJKb0MjkFK3dUoXNf" width="626" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b852497d3ad1f4aa9ca2c0fc18e28220081df5b9_2_626x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b852497d3ad1f4aa9ca2c0fc18e28220081df5b9_2_939x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b852497d3ad1f4aa9ca2c0fc18e28220081df5b9_2_1252x1000.png 2x" data-dominant-color="ECF5F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1432×1143 82.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f832ceb2a01db74beb6b898963cd7d5f1a201e9e.png" data-download-href="/uploads/short-url/zpFgyxWS8EbhFLiB7Aq4RAzNQCO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f832ceb2a01db74beb6b898963cd7d5f1a201e9e_2_637x500.png" alt="image" data-base62-sha1="zpFgyxWS8EbhFLiB7Aq4RAzNQCO" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f832ceb2a01db74beb6b898963cd7d5f1a201e9e_2_637x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f832ceb2a01db74beb6b898963cd7d5f1a201e9e_2_955x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f832ceb2a01db74beb6b898963cd7d5f1a201e9e_2_1274x1000.png 2x" data-dominant-color="E2EEFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1430×1122 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @LanceDuan (2025-05-28 08:17 UTC)

<p>It seems like only using Memory to process the computation. And I’ve checked the CUDA in Slicer’s Python Console.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bed9103078a42381e709c90b79c68e19f7115a3.png" data-download-href="/uploads/short-url/3Z3Shlc1duKk3oOcPNtJaV5DXft.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bed9103078a42381e709c90b79c68e19f7115a3_2_690x415.png" alt="image" data-base62-sha1="3Z3Shlc1duKk3oOcPNtJaV5DXft" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bed9103078a42381e709c90b79c68e19f7115a3_2_690x415.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bed9103078a42381e709c90b79c68e19f7115a3_2_1035x622.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bed9103078a42381e709c90b79c68e19f7115a3_2_1380x830.png 2x" data-dominant-color="CED2D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1541 465 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1eb21d9459c3b8641fef1f714258a72e6ca3c8b0.png" data-download-href="/uploads/short-url/4nxVXMRq0dKnPIfDCXC9bkNkRI4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1eb21d9459c3b8641fef1f714258a72e6ca3c8b0_2_690x190.png" alt="image" data-base62-sha1="4nxVXMRq0dKnPIfDCXC9bkNkRI4" width="690" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1eb21d9459c3b8641fef1f714258a72e6ca3c8b0_2_690x190.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1eb21d9459c3b8641fef1f714258a72e6ca3c8b0_2_1035x285.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1eb21d9459c3b8641fef1f714258a72e6ca3c8b0_2_1380x380.png 2x" data-dominant-color="212121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1803×498 10.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
