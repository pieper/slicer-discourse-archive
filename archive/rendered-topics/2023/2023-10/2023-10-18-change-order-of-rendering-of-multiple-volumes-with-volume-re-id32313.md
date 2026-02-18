# Change 'order' of rendering of multiple volumes with Volume Rendering module

**Topic ID**: 32313
**Date**: 2023-10-18
**URL**: https://discourse.slicer.org/t/change-order-of-rendering-of-multiple-volumes-with-volume-rendering-module/32313

---

## Post #1 by @Hamburgerfinger (2023-10-18 20:21 UTC)

<p>Is it possible to change the ‘order’ of the rendering layers in the Volume Rendering module?</p>
<p>What I want to achieve:  CT maximum intensity projection (mostly transparent except for bones) overlaid on PET maximum intensity projection (fully opaque).</p>
<p>Problem:  CT has to be added to scene last to get the Volume Rendering visualization I want.  If I add the CT first, then it is ‘hidden’ behind any opaque regions of volumes added after it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/521ae9c8a80fd56690c0da4d7832b53f28ff38a2.jpeg" data-download-href="/uploads/short-url/bIkOsyvSwz5v9po6204KutOsCJ4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/521ae9c8a80fd56690c0da4d7832b53f28ff38a2_2_625x500.jpeg" alt="image" data-base62-sha1="bIkOsyvSwz5v9po6204KutOsCJ4" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/521ae9c8a80fd56690c0da4d7832b53f28ff38a2_2_625x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/521ae9c8a80fd56690c0da4d7832b53f28ff38a2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/521ae9c8a80fd56690c0da4d7832b53f28ff38a2.jpeg 2x" data-dominant-color="827996"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">870×695 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be appreciated!  Currently I am just using the Crop module to create a “new” CT volume at the end of my workflow, so it is the top layer of the render.  Thanks!</p>

---

## Post #2 by @pieper (2023-10-18 20:32 UTC)

<p>Hmm, you might be able to clone the CT and then delete the original.  Otherwise I don’t think we expose any way to control that ordering.</p>

---

## Post #3 by @cpinter (2023-10-19 08:35 UTC)

<p>I guess you use <code>VTK GPU Ray Casting</code> rendering mode. That one is designed to render a single volume, so indeed there is an order of rendering.</p>
<p>The volume renderer that can consider multiple volumes is the <code>VTK Multi-Volume (experimental)</code> option. However, some features that are exposed in the Volume Rendering module and applies to the default GPU renderer are not implemented in this one. You can try this mode and see if it covers your use case.</p>

---

## Post #4 by @Hamburgerfinger (2023-10-19 14:03 UTC)

<p>Thanks! This works and is faster than using the CropVolume module like I have been doing.</p>
<p>It might be nice if the renders are always ‘stacked’ in the order they are shown - i.e., clicking the ‘show’ toggle button for a volume moves it to the front.  Not sure if that would be easy for me to achieve with python…</p>

---

## Post #5 by @Hamburgerfinger (2023-10-19 14:07 UTC)

<p>Thanks, yes I was using GPU Ray Casting.  The VTK Multi-Volume option doesn’t work for me (nothing is displayed at all) with the “Maximum Intensity Projection” technique, which I usually need for nuc med images.  It works great with the 'Composite with Shading"  technique though.</p>

---
