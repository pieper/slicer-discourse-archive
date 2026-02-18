# Dynamic 3D Object Manipulation for surgery simulation

**Topic ID**: 22508
**Date**: 2022-03-15
**URL**: https://discourse.slicer.org/t/dynamic-3d-object-manipulation-for-surgery-simulation/22508

---

## Post #1 by @Eserval (2022-03-15 00:29 UTC)

<p>Hello everyone,</p>
<p>Does anyone have experience with the manipulation of 3D objects?<br>
After I made my 3D model I’.m looking for a way to manipulate it, for example, retracting the lung parenchyma to expose the vessels.<br>
There is a great paper where collegues from Japan are using it: <a href="https://www.jtcvs.org/article/S0022-5223(19)31769-6/pdf" class="inline-onebox" rel="noopener nofollow ugc">DEFINE_ME</a>.</p>
<p>Here a video to here is a video from the paper to explain better:</p>
<p><a href="https://www.jtcvs.org/cms/10.1016/j.jtcvs.2019.07.136/attachment/a42f502d-05f0-4e22-a978-b1d3434674dd/mmc1.mp4" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.jtcvs.org/cms/10.1016/j.jtcvs.2019.07.136/attachment/a42f502d-05f0-4e22-a978-b1d3434674dd/mmc1.mp4</a></p>
<p>Best regards</p>

---

## Post #2 by @lassoan (2022-03-15 03:31 UTC)

<p>If you need approximate deformation, then you can simply use a thin-plate-spline transform driven by control points in Slicer. It can warp not just models (meshes) but volumetric images and all other nodes as well. Here is a short tutorial how to set up something like this for a more complicated case (deform soft tissue with constraints of nearby bones; modify an image, not just mesh):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="GfDDQykH1iY" data-video-title="Soft tissue deformation simulation" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=GfDDQykH1iY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/GfDDQykH1iY/maxresdefault.jpg" title="Soft tissue deformation simulation" width="" height="">
  </a>
</div>

<p>If you need physically realistic deformations then I would recommend to have a look at <a href="https://www.imstk.org/">IMSTK</a>. <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> can give more details about how that works in Slicer.</p>
<div class="vimeo-onebox lazy-video-container" data-video-id="299972259" data-video-title="KBVTrainer" data-provider-name="vimeo">
  <a href="https://vimeo.com/299972259" target="_blank" rel="noopener">
    <img class="vimeo-thumbnail" src="https://vumbnail.com/299972259.jpg" title="KBVTrainer" width="" height="">
  </a>
</div>


---
