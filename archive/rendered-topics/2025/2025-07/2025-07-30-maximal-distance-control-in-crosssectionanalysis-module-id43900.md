---
topic_id: 43900
title: "Maximal Distance Control In Crosssectionanalysis Module"
date: 2025-07-30
url: https://discourse.slicer.org/t/43900
---

# Maximal distance control in CrossSectionAnalysis module

**Topic ID**: 43900
**Date**: 2025-07-30
**URL**: https://discourse.slicer.org/t/maximal-distance-control-in-crosssectionanalysis-module/43900

---

## Post #1 by @SANTIAGO_PENDON_MING (2025-07-30 08:27 UTC)

<p>Hi to everyone!</p>
<p>Today, working with the module CrossSectionAnalysis I found a particular behavior that maybe causes some troubles.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b9bab587f190e50f35b0dab89a4d8b1fcda493f.png" data-download-href="/uploads/short-url/flWBMd4y0tseZgviDWmyCAIYqNp.png?dl=1" title="Captura de pantalla 2025-07-30 101157" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b9bab587f190e50f35b0dab89a4d8b1fcda493f_2_690x487.png" alt="Captura de pantalla 2025-07-30 101157" data-base62-sha1="flWBMd4y0tseZgviDWmyCAIYqNp" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b9bab587f190e50f35b0dab89a4d8b1fcda493f_2_690x487.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b9bab587f190e50f35b0dab89a4d8b1fcda493f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b9bab587f190e50f35b0dab89a4d8b1fcda493f.png 2x" data-dominant-color="D4D0D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2025-07-30 101157</span><span class="informations">979×692 86.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The point in the box generates his CS area so far away, when it’s also obvious that this point is outside the geometry. As far as I understand about CSA module, the function will try to select the section closer to the point in case than more than one section intersects with the plane. But in this case only one section is computed, so the result here says that the vessel has a fake CS area.</p>
<p>My point of view: There is a way to limit/control the distance of selection CS, in order to avoid CS that are so far away the point where we are computing? For example, in the image, select only CS areas that are closer than the blue circle (radius = 5mm)</p>
<p>Thanks a lot!</p>

---

## Post #2 by @chir.set (2025-07-30 09:51 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="43900">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>The point in the box</p>
</blockquote>
</aside>
<p>But the point in the box is clearly outside of the segment. It’s this input that should be fixed. In general, If algorithms/workflows start accounting for corner conditions, there’ll be no end to their updates. CSA is indeed behaving as expected in this case too.</p>
<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="43900">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>There is a way to limit/control the distance of selection CS</p>
</blockquote>
</aside>
<p>Not really, because the surface is cut by vtkCutter which has as input an <em>infinite</em> plane. I was looking for a way to limit that too but did not find one. Even if there is such a way, it would be hard to define this limit for automation.</p>

---
