# Shrinkwrapping tool in 3dslicer

**Topic ID**: 17189
**Date**: 2021-04-19
**URL**: https://discourse.slicer.org/t/shrinkwrapping-tool-in-3dslicer/17189

---

## Post #1 by @Valentina_Mejia_Gall (2021-04-19 23:00 UTC)

<p>Hello!,<br>
i have a question, in 3dslicer is there a tool like a “Wraping tool” in the Remesher  that can be used to fill in the holes of the 3D model. This is an especially useful tool for FEA where holes can cause inaccurate results.<br>
In which i can set the parameters like: Gap closing distance  to determine the size of gaps that will be wrapped and the Smallest detail  that sets the size of the triangles of the newly created surface</p>

---

## Post #2 by @manjula (2021-04-20 03:15 UTC)

<p>Is this what you looking for ? It can be installed via extension manager and found in the segment editor.</p>
<aside class="quote quote-modified" data-post="1" data-topic="11248">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/fill-or-extract-cavities-in-segmentations-using-the-new-wrap-solidify-effect/11248">Fill or extract cavities in segmentations using the new "Wrap Solidify" effect</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Making a segment that has fractured, discontinuous boundary and holes inside to be a simple solid object is a quite common task for segmentation. For example it is needed for creating simple solid bone models from CT images, extracting skin surface, segment thin surfaces, such as orbital bone wall, measuring brain volume, or volumes of various cavities. 
Slicer now has a tool for all this: “Wrap Solidify” Segment Editor effect, provided by <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" rel="noopener nofollow ugc">SurfaceWrapSolidify extension</a> and contributed by Sebasti…
  </blockquote>
</aside>


---

## Post #3 by @Valentina_Mejia_Gall (2021-04-20 16:21 UTC)

<p>i’m not so sure, this wraping tool is to fill the cavities in the segmentation, am i correct?<br>
What i’m searching is a tool to fill the cavities for a 3d model using the parameters of the triangles of the volumetric mesh</p>

---

## Post #4 by @roozbehshams (2021-04-22 21:53 UTC)

<p>You could convert the 3d model to a segmentation and use the segment editor to wrap it and then convert it back to a 3d model.<br>
Or alternatively if you can achieve what you want to do with MeshLab, you can install pymeshlab in slicer’s interpreter and apply the same filters on your model in the scene.</p>

---

## Post #5 by @lassoan (2021-04-23 03:53 UTC)

<aside class="quote no-group" data-username="roozbehshams" data-post="4" data-topic="17189">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/roozbehshams/48/1544_2.png" class="avatar"> roozbehshams:</div>
<blockquote>
<p>You could convert the 3d model to a segmentation and use the segment editor to wrap it</p>
</blockquote>
</aside>
<p>Exactly. You can choose to export the result directly to model, that way you get even higher accuracy (it is especially useful if you still want to maintain thin surface cracks; might not be relevant for your use case).</p>
<aside class="quote no-group" data-username="roozbehshams" data-post="4" data-topic="17189">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/roozbehshams/48/1544_2.png" class="avatar"> roozbehshams:</div>
<blockquote>
<p>Or alternatively if you can achieve what you want to do with MeshLab, you can install pymeshlab in slicer’s interpreter and apply the same filters on your model in the scene.</p>
</blockquote>
</aside>
<p>Which filter do you mean? I haven’t found shrinkwrap filter in MeshLab.</p>

---

## Post #6 by @roozbehshams (2021-04-23 14:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="17189">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Which filter do you mean? I haven’t found shrinkwrap filter in MeshLab.</p>
</blockquote>
</aside>
<p>I don’t know of any filter that can specifically do that, but thought to mention it in case they had a way of achieving that in MeshLab.</p>

---

## Post #7 by @lassoan (2021-04-23 14:38 UTC)

<p>MeshLab can do many things, but I think it does not have shrinkwrap method or other similar methods that can reliably solidify a mesh.</p>

---
