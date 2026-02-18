# Segment-Meshing multiple segments

**Topic ID**: 13595
**Date**: 2020-09-21
**URL**: https://discourse.slicer.org/t/segment-meshing-multiple-segments/13595

---

## Post #1 by @Shajia_Ali (2020-09-21 20:56 UTC)

<p>Hi,</p>
<p>I discovered segment-mesher quite recently and my goal is to create a mesh of a nutshell and the vascular bundles within it. My attempt is to have two meshes. One for the shell (with holes) and one only for the vascular bundles. It works when I seperate the segments into different ‘segmentation-files’. If i have two regions in one segmentation, it will mesh beautifully and the regions are showed by different colours. But there is no way to export them for example, as one part, but with two regions (for example element sets). If I could export it like that, I would make sure that the nodes of both regions match perfectly. It would be also easier to work with the element-sets in abaqus, giving them different material-properties.</p>
<p>Can someone help me out on that?</p>

---

## Post #2 by @lassoan (2020-09-21 22:06 UTC)

<p>Cleaver provides a single mesh that contains multiple regions. Each element has an associated value that defines which region it belongs to.</p>
<p>How did you import the mesh into abaqus?</p>

---

## Post #3 by @Shajia_Ali (2020-09-22 00:13 UTC)

<p>I just save it as a vtk and then convert it to an inp. File with meshio. How can I see which element belongs to which region? It would simplify a lot. When I import it to abaqus, I only have ONE orphan mesh with ONE region.</p>

---

## Post #4 by @lassoan (2020-09-22 00:24 UTC)

<p>It seems that region information is lost during meshio conversion. Submit an issue in the meshio repository about this (include a link to an example vtk file) and see what the developers say.</p>

---

## Post #5 by @Shajia_Ali (2020-09-22 00:32 UTC)

<p>Is it even inside the vtk.file? If so, how do I check it? I opened it in paraview, it looked like ONE region to me, but I have never used paraview before, so that’s on me probably.</p>
<p>I do the following:</p>
<ol>
<li>Define regions</li>
<li>Mesh with segment mesher</li>
<li>Save the model of the coloured mesh as vtk. Maybe the saving process is wrong?</li>
</ol>

---

## Post #6 by @lassoan (2020-09-22 02:22 UTC)

<aside class="quote no-group" data-username="Shajia_Ali" data-post="5" data-topic="13595">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shajia_ali/48/3425_2.png" class="avatar"> Shajia_Ali:</div>
<blockquote>
<p>Is it even inside the vtk.file?</p>
</blockquote>
</aside>
<p>Yes, the region number is stored in cell data array called <code>label</code>.</p>
<p>In Slicer, it is listed in Models module / Display / Scalars / Active Scalar (and it is used by default to display each region with a different color).</p>
<p>In Paraview, it is shown in Information tab / Data Arrays (and you can use that to color the model by selecting it in Properties tab / Display / Coloring):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ac692f4418041b118e6de0d50936d88bbe89b64.png" data-download-href="/uploads/short-url/cX2pKfC7vUYgQW537lJqghwxIbO.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5ac692f4418041b118e6de0d50936d88bbe89b64_2_313x500.png" alt="image" data-base62-sha1="cX2pKfC7vUYgQW537lJqghwxIbO" width="313" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5ac692f4418041b118e6de0d50936d88bbe89b64_2_313x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5ac692f4418041b118e6de0d50936d88bbe89b64_2_469x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5ac692f4418041b118e6de0d50936d88bbe89b64_2_626x1000.png 2x" data-dominant-color="ECEDEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">891×1421 86.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Shajia_Ali (2020-09-22 07:48 UTC)

<p>Maybe the solution would be to split the submeshes, and merge them back in abaqus, after assigning the material properties.</p>
<p>I will look into the meshio thing as well.</p>
<p>Thanks a lot.</p>

---

## Post #8 by @Shajia_Ali (2020-09-29 19:23 UTC)

<p>A different question, I see the description about adjusting the cleaver mesh, There are three options: scale, multiplier and grading. What if I want to have a mesh which is coarser on simple structures and finer on complex ones? I feel like it gets finer or coarser everywhere when i only want to work with those three parameters. Is there a way to create a solid out of that generated mesh? Then I could adjust it outside of 3d slicer.</p>
<p>Kind regards</p>
<p>Shajia</p>

---

## Post #9 by @lassoan (2020-09-30 01:05 UTC)

<aside class="quote no-group" data-username="Shajia_Ali" data-post="8" data-topic="13595">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shajia_ali/48/3425_2.png" class="avatar"> Shajia_Ali:</div>
<blockquote>
<p>which is coarser on simple structures and finer on complex ones</p>
</blockquote>
</aside>
<p>This is how the Cleaver adaptive meshing works.</p>
<p>In addition, you can specify a sizing field (an image) that you can use to specify regions where you want to have finer/coarser resolution. You need to create and this sizing field image and specify as additional input to Cleaver.</p>

---

## Post #10 by @Shajia_Ali (2020-09-30 07:56 UTC)

<p>Yes I know, but I thought maybe I have more control over it. Where do I find the sizing field image thing? I will look into it by myself later this day. But maybe you can give me a hand in advance. Like is there a small example on that? Thank you a lot for the fast answers.</p>
<p>Kind regards</p>
<p>Shajia</p>

---

## Post #11 by @Shajia_Ali (2020-09-30 08:04 UTC)

<p>Or is it possible to mesh both of the meshes seperately and merge them and only adapt the coarser mesh to the finer mesh? Like somehow overlapping them without having holes in between (wishful thinking from my point of view).<br>
I have like one structure which doesn’t need to be fine, the other part needs to be really fine. So if I adjust with those three parameters either it’s too fine with the bigger structure or too coarse with the finer structure.</p>

---
