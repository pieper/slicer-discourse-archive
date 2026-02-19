---
topic_id: 37684
title: "Vmtk Mapping And Patching Error"
date: 2024-08-03
url: https://discourse.slicer.org/t/37684
---

# VMTK Mapping and Patching Error

**Topic ID**: 37684
**Date**: 2024-08-03
**URL**: https://discourse.slicer.org/t/vmtk-mapping-and-patching-error/37684

---

## Post #1 by @Michael_C (2024-08-03 15:13 UTC)

<p>Dear all,</p>
<p>I am trying to map the surface of an aortic arch (in a .vtp format, as acquired from a SimVascular Simulation) onto the same parametric space, using <a href="http://www.vmtk.org/tutorials/MappingAndPatching.html" rel="noopener nofollow ugc">VMTK’s Mapping and Patching</a>.</p>
<p>The splitting and grouping seems to be correct. However when i proceed to the Metric mapping, the results differ from the ones shown in the website.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6b83b6dbcf2bf690d7bbd5c62d82540e0bc84dd.jpeg" data-download-href="/uploads/short-url/zcAaK4JObFE0rTwu5VhpgQvMZit.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6b83b6dbcf2bf690d7bbd5c62d82540e0bc84dd_2_251x250.jpeg" alt="image" data-base62-sha1="zcAaK4JObFE0rTwu5VhpgQvMZit" width="251" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6b83b6dbcf2bf690d7bbd5c62d82540e0bc84dd_2_251x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6b83b6dbcf2bf690d7bbd5c62d82540e0bc84dd_2_376x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6b83b6dbcf2bf690d7bbd5c62d82540e0bc84dd_2_502x500.jpeg 2x" data-dominant-color="565770"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">627×623 24.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As shown below, at Case 1, the Harmonic Mapping takes place in only one branch/group instead of every single one (Example) and subsequently, the vmtkbranchpatching script leads to an error.</p>
<div class="d-image-grid">
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c95e10c3961762055be57a657d63a3492c19b24.png" data-download-href="/uploads/short-url/k3FXxxty2D9DFqyNUqd7fdAZUu8.png?dl=1" title="Case 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c95e10c3961762055be57a657d63a3492c19b24_2_250x250.png" alt="Case 1" data-base62-sha1="k3FXxxty2D9DFqyNUqd7fdAZUu8" width="250" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c95e10c3961762055be57a657d63a3492c19b24_2_250x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c95e10c3961762055be57a657d63a3492c19b24_2_375x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c95e10c3961762055be57a657d63a3492c19b24_2_500x500.png 2x" data-dominant-color="484E71"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Case 1</span><span class="informations">522×522 59.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0fe1f6bf35be21269011bf2b6b0673aa9f5ae2d.jpeg" data-download-href="/uploads/short-url/rxi82U2yxRMCUbUSj4rX7zvlvDn.jpeg?dl=1" title="Example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0fe1f6bf35be21269011bf2b6b0673aa9f5ae2d_2_93x250.jpeg" alt="Example" data-base62-sha1="rxi82U2yxRMCUbUSj4rX7zvlvDn" width="93" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0fe1f6bf35be21269011bf2b6b0673aa9f5ae2d_2_93x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0fe1f6bf35be21269011bf2b6b0673aa9f5ae2d_2_139x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0fe1f6bf35be21269011bf2b6b0673aa9f5ae2d_2_186x500.jpeg 2x" data-dominant-color="E2DFE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Example</span><span class="informations">285×766 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</div>
<p>I tried smoothing the surfaces and cap any possible gaps but it didn’t work.</p>
<p>Any ideas and suggestions are welcome. Thank you in advance.</p>
<p>Best,<br>
Michael</p>

---
