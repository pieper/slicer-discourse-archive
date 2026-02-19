---
topic_id: 18562
title: "Create A 3D Solid Model From Ct Scans"
date: 2021-07-07
url: https://discourse.slicer.org/t/18562
---

# Create a 3D solid model from CT scans

**Topic ID**: 18562
**Date**: 2021-07-07
**URL**: https://discourse.slicer.org/t/create-a-3d-solid-model-from-ct-scans/18562

---

## Post #1 by @Leelhan (2021-07-07 12:30 UTC)

<p>Hello,</p>
<p>I have CT scans of a vertebra and I’m trying to export a 3D solid model from Slicer so I can import in Abaqus. I have already segmented and created the model, but once on Abaqus I realised it was just a surface model and just a shell.<br>
How can I export a 3D solid model?<br>
I know that this can be fixed by creating a mesh, but I just want to export from Slicer the geometry.<br>
How can I do this?</p>

---

## Post #2 by @lassoan (2021-07-11 15:44 UTC)

<p>You can create a volumetric mesh (tetrahedral and wedge elements) using SegmentMesher extension.</p>

---

## Post #3 by @Leelhan (2021-07-12 08:09 UTC)

<p>Hi Andras, thank you for your reply. What if I don’t want to mesh it? I just need its solid geometry exported.</p>

---

## Post #4 by @lassoan (2021-07-12 15:56 UTC)

<p>“Don’t mesh it” is not an option. “Solid geometry” concept only exists in CAD software - it refers to parametric representation of a shape, obtained from combining simple parametric primitives and can be characterized with a few hundred or maybe a few thousand parameters. In contrast, in medical image computing you generate shapes from images, which consists of tens or hundreds of millions of voxels, so the resulting object cannot be practically stored with a parametric representation (you would need thousands of times faster CPU and thousands of times more RAM).</p>
<p>Image segmentation results therefore typically stored either as a 3D array of voxels or as a polygonal mesh. In rare cases, when the shape is very simple, you can reverse-engineer a parametric shape (“solid geometry”) from the segmented shape in your CAD software, but in general you need to use different tools to deal with these complex free-form shapes. For example, for finite-element analysis you generate a volumetric mesh; for Boolean operations, you need to use special algorithms that work on polygonal meshes (or use voxel array representation); …</p>

---

## Post #5 by @Leelhan (2021-07-12 17:32 UTC)

<p>Ok, I get it.</p>
<p>But a few years ago I had the model of a femur which I could mesh on Abaqus for example.<br>
If I do a volumetric mesh with slicer in order to create a 3d solid model, will I be able to mesh it again on Abaqus?</p>

---

## Post #6 by @lassoan (2021-07-12 20:10 UTC)

<p>It is up to what you want to do and what Abaqus can do. If Abaqus can import a surface mesh (from PLY, STL, OBJ, …) and create a solid model then it is great, but you can expect to run into difficulties if the surface mesh is complex or has many points.</p>

---

## Post #7 by @muratmaga (2021-07-12 20:12 UTC)

<p>I wonder if <a class="mention" href="/u/leelhan">@leelhan</a> simply wants a model that has no internal space (e.g., in femur). Wouldn’t WrapSurfaceSolidfy work for that?</p>

---

## Post #8 by @lassoan (2021-07-12 20:30 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="18562">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I wonder if <a class="mention" href="/u/leelhan">@leelhan</a> simply wants a model that has no internal space (e.g., in femur).</p>
</blockquote>
</aside>
<p>The first post suggests that the issue is the surface mesh, but maybe <a class="mention" href="/u/leelhan">@Leelhan</a> uses a different nomenclature. For reference here is <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#glossary">Slicer’s glossary of terms here</a>.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="18562">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Wouldn’t WrapSurfaceSolidfy work for that?</p>
</blockquote>
</aside>
<p>Wrap Solidify effect can fill internal holes in general, but since vertebrae have holes (spinal canal), surface wrapping cannot be used on them.</p>
<p>However, we worked out a very good protocol for spine segmentation at the last project week. See more information <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW35_2021_Virtual/Projects/SpineSegmentation/README.md#spine-segmentation-protocol-for-training-data-generation">here</a>.</p>

---

## Post #9 by @Leelhan (2021-07-14 11:06 UTC)

<p>I think I need to work the surface mesh into some kind of CAD software and create the solid from there and then import it on Abaqus.</p>
<p>I tried using SegmentMesher extension, but as I suspected it doesn’t create the geometry of the segmentation, which is what I need.</p>
<p>And yes, I need a 3D solid model, which is not hollow inside. And yes, I need to leave a hole where the spinal canal should be.</p>
<p>Thank you anyway for the suggestions.</p>

---

## Post #10 by @lassoan (2021-07-14 20:14 UTC)

<aside class="quote no-group" data-username="Leelhan" data-post="9" data-topic="18562">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/d26b3c/48.png" class="avatar"> Leelhan:</div>
<blockquote>
<p>I tried using SegmentMesher extension, but as I suspected it doesn’t create the geometry of the segmentation, which is what I need.</p>
</blockquote>
</aside>
<p>SegmentMesher creates a volumetric mesh of the segmentation, made up of tetrahedral and wedge elements, that can be used directly for finite-element analysis. Users reported to use these meshes successfully in FEBio and Abaqus.</p>
<aside class="quote no-group" data-username="Leelhan" data-post="9" data-topic="18562">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/d26b3c/48.png" class="avatar"> Leelhan:</div>
<blockquote>
<p>And yes, I need a 3D solid model, which is not hollow inside.</p>
</blockquote>
</aside>
<p>Anything that appears inside the segmentation will be inside the generated volumetric mesh, too. If you segment the vertebrae using simple thresholding then holes will appear inside the cortical regions of the spine, which you can fill using the Python code snippet I referred to above.</p>

---
