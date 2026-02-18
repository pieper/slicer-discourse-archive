# Creating smooth flow extensions

**Topic ID**: 23197
**Date**: 2022-04-29
**URL**: https://discourse.slicer.org/t/creating-smooth-flow-extensions/23197

---

## Post #1 by @JuliaW (2022-04-29 16:28 UTC)

<p>Dear vmtk community,</p>
<p>Currently, I am preparing a segmented aorta for flow analysis.<br>
Using vmtk I have cut open the surface and added flow extensions.<br>
However, at opening of the aorta, the transition between the flow extension and the segmented surface is not smooth (see the attached image).<br>
Is there a way to smooth out the edges?<br>
Maybe I could refine the mesh of the flow extensions, but I wouldn’t know how.</p>
<p>Thank you for your reply!</p>
<p>Kind regards,</p>
<p>Julia</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/643d0df0db75dca52c0300f29996adcebd88cda3.jpeg" data-download-href="/uploads/short-url/eiKyrMvdnwRmVWGeURTi6oQNq03.jpeg?dl=1" title="Flow_extension aorta_arrows" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/643d0df0db75dca52c0300f29996adcebd88cda3.jpeg" alt="Flow_extension aorta_arrows" data-base62-sha1="eiKyrMvdnwRmVWGeURTi6oQNq03" width="605" height="500" data-dominant-color="666979"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Flow_extension aorta_arrows</span><span class="informations">911×752 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-04-29 16:38 UTC)

<p>Probably the simplest is to edit the mesh locally to smooth out that edge in Meshmixer (BubbleSmooth brush) or 3D Slicer (Segment Editor, Smoothing effect, use the brush in slice or 3D views).</p>

---
