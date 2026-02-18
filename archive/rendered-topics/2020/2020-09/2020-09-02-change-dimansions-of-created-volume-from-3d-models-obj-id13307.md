# Change dimansions of created volume from 3d models (obj)

**Topic ID**: 13307
**Date**: 2020-09-02
**URL**: https://discourse.slicer.org/t/change-dimansions-of-created-volume-from-3d-models-obj/13307

---

## Post #1 by @Nina (2020-09-02 21:10 UTC)

<p>Hello;</p>
<p>I have created volume from .obj file (bunny model) as explained here:<br>
<a href="https://discourse.slicer.org/t/create-volumes-from-3d-model-obj-file/5463">volume from obj file</a></p>
<p>However the dimensions of the models look very small (see attached figure). how can change the dimension of segmentation and spacing ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc4ad57f3c73f6f2fa25754c6e024e9606789636.png" data-download-href="/uploads/short-url/t9fJzpxz0DGtaoscTiPP7S9FEs6.png?dl=1" title="bunny" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc4ad57f3c73f6f2fa25754c6e024e9606789636_2_690x312.png" alt="bunny" data-base62-sha1="t9fJzpxz0DGtaoscTiPP7S9FEs6" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc4ad57f3c73f6f2fa25754c6e024e9606789636_2_690x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc4ad57f3c73f6f2fa25754c6e024e9606789636_2_1035x468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc4ad57f3c73f6f2fa25754c6e024e9606789636_2_1380x624.png 2x" data-dominant-color="86869C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bunny</span><span class="informations">1822×826 63.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2020-09-02 23:01 UTC)

<p>You can use Surface Toolbox or Transforms module to scale your model. I guess your bunny model uses meters as unit, so you need to scale up by 1000.0 (but it might use inches, centimeters,…).</p>

---
