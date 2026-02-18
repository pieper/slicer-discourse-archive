# Prism rendering

**Topic ID**: 16609
**Date**: 2021-03-18
**URL**: https://discourse.slicer.org/t/prism-rendering/16609

---

## Post #1 by @mohammed_alshakhas (2021-03-18 07:48 UTC)

<p>is it posiible to apply Prism rendering on the rendered volume in "volume rendering module " ?</p>
<p>like applying a sphere carving on the render</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8335146aae34a479ed226198e69d0ebb09de56e.jpeg" data-download-href="/uploads/short-url/zpGmjmh61iXB5ddxo0WYsTtmZpI.jpeg?dl=1" title="Screen Shot 2021-03-18 at 10.48.10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8335146aae34a479ed226198e69d0ebb09de56e_2_690x388.jpeg" alt="Screen Shot 2021-03-18 at 10.48.10" data-base62-sha1="zpGmjmh61iXB5ddxo0WYsTtmZpI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8335146aae34a479ed226198e69d0ebb09de56e_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8335146aae34a479ed226198e69d0ebb09de56e_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8335146aae34a479ed226198e69d0ebb09de56e_2_1380x776.jpeg 2x" data-dominant-color="96989C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-18 at 10.48.10</span><span class="informations">1920×1080 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>i thought i would be  able to save the rendering in prism in volume property like into rendering module and use multi volume ray casting .</p>

---

## Post #2 by @pieper (2021-03-19 00:20 UTC)

<p>SlicerPrismRendering is not really integrated with the Volume Rendering module, it’s more of an alternative way to define the rendering setup.</p>

---

## Post #3 by @lassoan (2021-03-19 05:51 UTC)

<p>I’ve found that Volume rendering module and PRISM works quite nicely together on the same nodes (they both edit the same Volume Rendering and Volume Property nodes). PRISM provides a convenient GUI to specify custom shaders and their parameters, while Volume Rendering module allows editing transfer functions, lighting, and a few other parameters.</p>
<p>There seems to be a limitation in PRISM module GUI that prevents recognizing volume rendering nodes created by Volume Rendering module, so for now you need to create the volume rendering nodes in PRISM (by clicking the “Volume rendering” checkbox). It should be easy to fix this, if you send a bug report to the PRISM issue tracker then eventually they will take care of this (or you can give it a try yourself).</p>
<p>I don’t think PRISM is prepared to work with the relatively new multivolume renderer, so this may be another feature request for PRISM (or you can dive in and implement it).</p>

---

## Post #4 by @mohammed_alshakhas (2021-03-19 06:04 UTC)

<p>i stumbled on  the " volume rendering special effects" module and it does  recognize node from volume rendering module . it has a wedge and sphere carving.</p>
<p>however the prism rendering is better and has more functionality .</p>
<p>ill try to submit the issue on GitHub</p>

---

## Post #5 by @mohammed_alshakhas (2021-03-19 06:05 UTC)

<p>well , thats  a downer . i don’t think it makes sense to be in slicer and not be able to interact with the core volume rendering module</p>

---

## Post #6 by @lassoan (2021-03-19 06:11 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="5" data-topic="16609" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>well , thats a downer . i don’t think it makes sense to be in slicer and not be able to interact with the core volume rendering module</p>
</blockquote>
</aside>
<p>This is not the case. Just for now (until the PRISM module GUI is fixed), you need to create the volume rendering nodes in PRISM. You can then use Volume Rendering module to edit those settings.</p>
<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="4" data-topic="16609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>i stumbled on the " volume rendering special effects" module and it does recognize node from volume rendering module . it has a wedge and sphere carving.</p>
</blockquote>
</aside>
<p>This module is an earlier version of PRISM. PRISM should work the same way, there is just that small bug in its GUI it that it expects a vtkMRMLShaderPropertyNode to be associated with the volume rendering node and the Volume Rendering module does not create such a node; but PRISM could easily create it instead of just throwing an error message.</p>

---

## Post #7 by @mohammed_alshakhas (2021-03-19 06:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="16609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is not the case. Just for now (until the PRISM module GUI is fixed), you need to create the volume rendering nodes in PRISM. You can then use Volume Rendering module to edit those settings</p>
</blockquote>
</aside>
<p>i failed to see that before , i just tried it now and it works . however . i still would love to do to the other way around . use volume rendering module then prism . will be waiting for the fix</p>
<p>is there any volume rendering extension / module offering more possibilities ?<br>
just wondering since im getting such amazing results learning using these two modules</p>

---

## Post #8 by @pieper (2021-03-19 12:01 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="7" data-topic="16609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>im getting such amazing results learning using these two modules</p>
</blockquote>
</aside>
<p>Yes, there are many possibilities and the programming infrastructure is very powerful.  it’s taken many years of development by uniquely talented people to turn these into the usable GUIs that exist today, but much more is possible if someone is able to invest the time and effort.  This could be accomplished through sponsorship, if someone wants to pay to have it developed, or through mentorship, if a student or volunteer wants to dive in.</p>

---
