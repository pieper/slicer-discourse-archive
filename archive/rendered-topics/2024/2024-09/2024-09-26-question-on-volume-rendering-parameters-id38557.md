---
topic_id: 38557
title: "Question On Volume Rendering Parameters"
date: 2024-09-26
url: https://discourse.slicer.org/t/38557
---

# Question on volume rendering parameters

**Topic ID**: 38557
**Date**: 2024-09-26
**URL**: https://discourse.slicer.org/t/question-on-volume-rendering-parameters/38557

---

## Post #1 by @alientex (2024-09-26 12:12 UTC)

<p>Hello,</p>
<p>Below are the parameters of the volume rendering module:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67e4c68f3e05d11751e6f77a0499889a698adb3f.png" data-download-href="/uploads/short-url/eP5koynVct8MGXs1qk8wCi6YGbJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67e4c68f3e05d11751e6f77a0499889a698adb3f_2_271x250.png" alt="image" data-base62-sha1="eP5koynVct8MGXs1qk8wCi6YGbJ" width="271" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67e4c68f3e05d11751e6f77a0499889a698adb3f_2_271x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67e4c68f3e05d11751e6f77a0499889a698adb3f_2_406x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67e4c68f3e05d11751e6f77a0499889a698adb3f_2_542x500.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">561×517 11 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I  want to use the parameters specifically the Rendering, Quality, and Interactive Speed for the 3D view of segmentations instead of volume rendering. I have managed to retrieve the Auto-release resources parameter from the code below; however, I am unable to fetch the other parameters:<br>
<code><br>
viewNode = slicer.app.layoutManager().threeDWidget(0).mrmlViewNode()<br>
autoRelease = viewNode.GetAutoReleaseGraphicsResources()<br>
</code></p>
<p>Can anyone help me with this?</p>

---

## Post #2 by @alientex (2024-09-27 04:08 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>Is it possible to use Ray Casting, Quality or Interactive speed for the 3d visualization happens for segmentations in 3d view?</p>

---

## Post #3 by @muratmaga (2024-09-27 05:53 UTC)

<p>3D view of segmentations are based on surface rendering of polydata. It is a totally different mechanisms from the volume rendering. Those parameters do not apply?</p>
<p>Is your 3D rendering of segmentations slow?</p>

---

## Post #4 by @cpinter (2024-09-27 09:56 UTC)

<p>Segmentations are shown in 3D using the closed surface mesh representation, but it (typically) also has a binary labelmap, which is used for editing and 2D visualization. In theory, you could export the segmentation labelmap to a volume node (Segmentations module Import/Export section, or Data module right-click), and show it with volume rendering with the Colorize volumes module. The problem is that currently multi-volume rendering does not really work well (this is why it says “experimental” in the option in the Volume rendering module). What this means is that if you use multi-volume rendering showing the CT and the segmentation at the same time, you won’t have access to features like cropping, rendering quality settings, lighting, etc, and if you use the default GPU ray casting then the rendering of the two volumes will not consider depth information, so one will always appear “on top of” the other.</p>

---
