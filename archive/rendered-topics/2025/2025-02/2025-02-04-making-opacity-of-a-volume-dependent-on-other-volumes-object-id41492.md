# Making opacity of a volume dependent on other volumes/objects

**Topic ID**: 41492
**Date**: 2025-02-04
**URL**: https://discourse.slicer.org/t/making-opacity-of-a-volume-dependent-on-other-volumes-objects/41492

---

## Post #1 by @Arber_Demi (2025-02-04 15:04 UTC)

<p>Hello everyone.</p>
<p>I’m trying to make a sort of “see-through” model/volume (i’ll call it volume C), which I want to use to look through a larger volume (volume A) and be able to see a smaller volume (volume B) inside volume A. However, I only want volume B to be visible when I’m looking at it through volume C, and hidden at all other times.</p>
<p>In these pictures, the yellow cube is volume A, the sphere inside the cube is volume B and the red cylinder is volume C.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/587ed1a86aefda01921cf960bc6616c7cd2e4cfd.png" data-download-href="/uploads/short-url/cCRIZZ6ELl6ZQ4y6ddvUK3cr0wR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/587ed1a86aefda01921cf960bc6616c7cd2e4cfd.png" alt="image" data-base62-sha1="cCRIZZ6ELl6ZQ4y6ddvUK3cr0wR" width="386" height="311"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">386×311 45.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b6711cfa8960cfa9d5632b21b8aa5fdaf16ceb7.png" data-download-href="/uploads/short-url/1CS4OL0y1XoimJSf5HFS8DxLwLt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b6711cfa8960cfa9d5632b21b8aa5fdaf16ceb7.png" alt="image" data-base62-sha1="1CS4OL0y1XoimJSf5HFS8DxLwLt" width="294" height="322"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">294×322 2.62 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The sphere should be hidden in the first image, and visible in the second image</p>
<p>I wasn’t able to find any opacity settings that connect their functionality to make it relative to other volumes, so I’m not sure if this is possible with existing functionality. In reality, the cube would be some MRI scan, and the sphere ultrasound results, with the cylinder being some 2D slice or a 3D model attached to a tracking tool.</p>
<p>I would appreciate any ideas :] (trying to do this hopefully without having to change code that touches rendering)</p>

---
