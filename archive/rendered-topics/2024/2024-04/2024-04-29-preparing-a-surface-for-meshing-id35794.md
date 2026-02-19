---
topic_id: 35794
title: "Preparing A Surface For Meshing"
date: 2024-04-29
url: https://discourse.slicer.org/t/35794
---

# Preparing a surface for meshing

**Topic ID**: 35794
**Date**: 2024-04-29
**URL**: https://discourse.slicer.org/t/preparing-a-surface-for-meshing/35794

---

## Post #1 by @benzwick (2024-04-29 12:12 UTC)

<p>I am trying to prepare a surface mesh for use in a simulation. I need a surface with open ends that are perpendicular to the centerlines of the vessels.</p>
<p>I have a segmentation that looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96b010c798a1e3e0fba3010af32b022b9472cf89.jpeg" data-download-href="/uploads/short-url/lv2Q26We6bp54E8O8mX5ROwI8u5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96b010c798a1e3e0fba3010af32b022b9472cf89_2_690x418.jpeg" alt="image" data-base62-sha1="lv2Q26We6bp54E8O8mX5ROwI8u5" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96b010c798a1e3e0fba3010af32b022b9472cf89_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96b010c798a1e3e0fba3010af32b022b9472cf89_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96b010c798a1e3e0fba3010af32b022b9472cf89.jpeg 2x" data-dominant-color="877FA9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×708 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would like to cut the ends normal to the centrelines to obtain a model with open ends similar to this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96d04918b64fea8009d01d22d55a7e14a75aefc2.jpeg" data-download-href="/uploads/short-url/lw9RXinDyl2No3CiLHHrNsDIZai.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96d04918b64fea8009d01d22d55a7e14a75aefc2_2_690x418.jpeg" alt="image" data-base62-sha1="lw9RXinDyl2No3CiLHHrNsDIZai" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96d04918b64fea8009d01d22d55a7e14a75aefc2_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96d04918b64fea8009d01d22d55a7e14a75aefc2_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96d04918b64fea8009d01d22d55a7e14a75aefc2.jpeg 2x" data-dominant-color="918CBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×708 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is it possible to do this using VMTK within 3D Slicer?</p>

---

## Post #2 by @mikebind (2024-04-29 19:12 UTC)

<p>Sounds like this might be helpful: <a href="https://discourse.slicer.org/t/vmtk-surface-clipping-contribution/30456/1" class="inline-onebox">Vmtk surface clipping contribution</a></p>

---

## Post #3 by @benzwick (2024-04-30 05:34 UTC)

<p>Thank you, this is exactly what I was looking for. I can get it to work when the vessels attached to the aneurysm are relatively long.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f11710c380fd48183e1049a9319bf21b52f87922.png" data-download-href="/uploads/short-url/yoMufFF48HZce3dMsoN8bpwgPC2.png?dl=1" title="clip-vessel-long" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f11710c380fd48183e1049a9319bf21b52f87922_2_690x372.png" alt="clip-vessel-long" data-base62-sha1="yoMufFF48HZce3dMsoN8bpwgPC2" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f11710c380fd48183e1049a9319bf21b52f87922_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f11710c380fd48183e1049a9319bf21b52f87922_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f11710c380fd48183e1049a9319bf21b52f87922_2_1380x744.png 2x" data-dominant-color="BEC1D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clip-vessel-long</span><span class="informations">1920×1036 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, if I try to shorten the segments as required for our analysis the top of the aneurysm gets clipped as well. Is there any way to avoid this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b274d857a7c82ec8cd48fd8d25adcb74dbc4b14b.png" data-download-href="/uploads/short-url/psHkpo5M7GzZTMHMJUAVbXTpLt1.png?dl=1" title="clip-vessel-short" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b274d857a7c82ec8cd48fd8d25adcb74dbc4b14b_2_690x372.png" alt="clip-vessel-short" data-base62-sha1="psHkpo5M7GzZTMHMJUAVbXTpLt1" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b274d857a7c82ec8cd48fd8d25adcb74dbc4b14b_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b274d857a7c82ec8cd48fd8d25adcb74dbc4b14b_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b274d857a7c82ec8cd48fd8d25adcb74dbc4b14b_2_1380x744.png 2x" data-dominant-color="C1C4DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clip-vessel-short</span><span class="informations">1920×1036 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @DavidM (2024-04-30 13:23 UTC)

<p>The issue here is that there is no centerline associated with the aneurysm so the logic does not recognize it as a separate region and hence exclude it from the clipping. It may work if you are able to add a centerline to the tip of the aneurysm. Otherwise I think you will have to clip it above the aneurysm.</p>

---

## Post #5 by @benzwick (2024-04-30 16:23 UTC)

<p>Thanks <a class="mention" href="/u/davidm">@DavidM</a> I got it to work by adding a few centerlines within the aneurysm.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b3a2389b3e90affccb8bd10e7486b3e96406687.png" data-download-href="/uploads/short-url/fizEn9GlYjLkBt4jTSuZ7M8wxhB.png?dl=1" title="clip-vessel-short-more-centerlines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b3a2389b3e90affccb8bd10e7486b3e96406687_2_690x392.png" alt="clip-vessel-short-more-centerlines" data-base62-sha1="fizEn9GlYjLkBt4jTSuZ7M8wxhB" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b3a2389b3e90affccb8bd10e7486b3e96406687_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b3a2389b3e90affccb8bd10e7486b3e96406687_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b3a2389b3e90affccb8bd10e7486b3e96406687_2_1380x784.png 2x" data-dominant-color="BABFD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clip-vessel-short-more-centerlines</span><span class="informations">2050×1166 450 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @benzwick (2024-05-01 06:07 UTC)

<p>Are there any examples for how to use VMTK scripts from within 3D Slicer?</p>
<p>For example, I would like to do the following after I clip the geometry:</p>
<pre data-code-wrap="bash"><code class="lang-bash">vmtksurfacenormals -ifile "../processed NRRDs/artery_cut_remesh_clip.stl" -ofile "artery_cut_remesh_clip_vmtksurfacenormals.stl" \
  --pipe vmtksurfaceremeshing -elementsizemode edgelength -edgelength 0.3 -ofile "artery_cut_remesh_clip_vmtksurfacenormals_remesh.stl"
</code></pre>
<p>The reason for computing the surface normals is that the normals on the extrusions were in the opposite direction to those on the artery and aneurysm wall which causes problems when trying to create a volume mesh.</p>

---

## Post #7 by @mikebind (2024-05-02 16:53 UTC)

<p>The VMTK extension for Slicer (<a href="https://github.com/vmtk/SlicerExtension-VMTK" rel="noopener nofollow ugc">https://github.com/vmtk/SlicerExtension-VMTK</a>) has several examples of using VMTK features from python.  For example, <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py" rel="noopener nofollow ugc">https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py</a> shows how to extract a centerline using VMTK and is a python module. It will take a little work to unpack the code there, but it and the other modules of the VMTK Slicer extension are definitely working examples you could start from.  Perhaps there are other more straightforward resources that others could point you to.</p>

---
