# Multi-phase segmentation of a rock core

**Topic ID**: 41620
**Date**: 2025-02-11
**URL**: https://discourse.slicer.org/t/multi-phase-segmentation-of-a-rock-core/41620

---

## Post #1 by @jddorellanao (2025-02-11 03:34 UTC)

<p>I am currently working with microCT images of rocks, more specifically cores (like the following image)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a76ddc75bdc8ebf0359f8c8d6ef23a5405e9085.jpeg" data-download-href="/uploads/short-url/1uzrz9aWGzgVlWSLZUecWB8LZYx.jpeg?dl=1" title="IMG_4963" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a76ddc75bdc8ebf0359f8c8d6ef23a5405e9085_2_281x375.jpeg" alt="IMG_4963" data-base62-sha1="1uzrz9aWGzgVlWSLZUecWB8LZYx" width="281" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a76ddc75bdc8ebf0359f8c8d6ef23a5405e9085_2_281x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a76ddc75bdc8ebf0359f8c8d6ef23a5405e9085_2_421x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a76ddc75bdc8ebf0359f8c8d6ef23a5405e9085_2_562x750.jpeg 2x" data-dominant-color="7F7B77"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_4963</span><span class="informations">1512×2016 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Since the acquisition is done by the lab operator, the images he gives me have some problems</p>
<ul>
<li>
<p>When the CT was acquired the core was tilted, so the first image and the last image do not match:<br>
The top image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e9d4c3bdac691e687c9e162c06f3da2390bbe69.jpeg" data-download-href="/uploads/short-url/i45aynthAt0GCF5uj8VEJnURcgx.jpeg?dl=1" title="LUMIR-187-2024_.am0268" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e9d4c3bdac691e687c9e162c06f3da2390bbe69_2_363x375.jpeg" alt="LUMIR-187-2024_.am0268" data-base62-sha1="i45aynthAt0GCF5uj8VEJnURcgx" width="363" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e9d4c3bdac691e687c9e162c06f3da2390bbe69_2_363x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e9d4c3bdac691e687c9e162c06f3da2390bbe69_2_544x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e9d4c3bdac691e687c9e162c06f3da2390bbe69_2_726x750.jpeg 2x" data-dominant-color="3D3D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LUMIR-187-2024_.am0268</span><span class="informations">994×1024 47 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The base image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2474ac3c7b5c76e5e55a43dfb876046c531412e3.jpeg" data-download-href="/uploads/short-url/5cv9SaoutHMBd5yL2cxfBjiPkDV.jpeg?dl=1" title="LUMIR-187-2024_.am2029" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2474ac3c7b5c76e5e55a43dfb876046c531412e3_2_363x375.jpeg" alt="LUMIR-187-2024_.am2029" data-base62-sha1="5cv9SaoutHMBd5yL2cxfBjiPkDV" width="363" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2474ac3c7b5c76e5e55a43dfb876046c531412e3_2_363x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2474ac3c7b5c76e5e55a43dfb876046c531412e3_2_544x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2474ac3c7b5c76e5e55a43dfb876046c531412e3_2_726x750.jpeg 2x" data-dominant-color="373737"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LUMIR-187-2024_.am2029</span><span class="informations">994×1024 40.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>The segmentation consists of a multiphase discriminator: the pore space, the rock matrix, and one or more minerals, when trying to segment the pore space with threshold, the space outside the core is included:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6aa581ef28156558f0fbc1f37627dd9fd120eb77.jpeg" data-download-href="/uploads/short-url/fdrd1TmgKpYN8mC9i8Y4NOtPign.jpeg?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aa581ef28156558f0fbc1f37627dd9fd120eb77_2_690x370.jpeg" alt="imagen" data-base62-sha1="fdrd1TmgKpYN8mC9i8Y4NOtPign" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aa581ef28156558f0fbc1f37627dd9fd120eb77_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aa581ef28156558f0fbc1f37627dd9fd120eb77_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aa581ef28156558f0fbc1f37627dd9fd120eb77_2_1380x740.jpeg 2x" data-dominant-color="616571"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1920×1032 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
<p>Which is not wrong, but it is not the desire. I tried with scissors, but since the core is inclined, I can’t do it.</p>
<p>I would be grateful if you could guide me.</p>

---

## Post #2 by @pieper (2025-02-11 14:17 UTC)

<p>You should be able to threshold the air outside the rock first, then when you do the inside of the rock don’t let it overwrite the air.</p>

---
