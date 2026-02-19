---
topic_id: 44207
title: "Check Surface Meshes Generated With The Surface Toolbox"
date: 2025-08-26
url: https://discourse.slicer.org/t/44207
---

# Check surface meshes generated with the surface toolbox

**Topic ID**: 44207
**Date**: 2025-08-26
**URL**: https://discourse.slicer.org/t/check-surface-meshes-generated-with-the-surface-toolbox/44207

---

## Post #1 by @DaSt (2025-08-26 15:53 UTC)

<p>Dear All,</p>
<p>I’m using the Surface Toolbox, specifically Uniform Remesh, via the Python API to generate STL surface meshes with a target edge length. Occasionally the resulting STL is not watertight (e.g., open boundaries / non-manifold elements).</p>
<p>I wanted to ask if there is a slicer inbuild solution to check for watertightness or fix falsely stl files/surface meshes?</p>
<p>Context:</p>
<ul>
<li>Slicer Version 5.8.1</li>
<li>OS: Windows 11</li>
</ul>
<p>Thanks in advance and best,</p>
<p>Daniel</p>

---

## Post #2 by @pieper (2025-08-26 17:19 UTC)

<p>This discussion might help: <a href="https://discourse.vtk.org/t/is-there-any-way-to-check-mesh-is-watertight/3169" class="inline-onebox">is there any way to check mesh is watertight? - Support - VTK</a></p>
<p>VTK classes like this are available in the Slicer python environment.</p>

---

## Post #3 by @DaSt (2025-08-27 14:59 UTC)

<p>Thanks Steve!</p>
<p>I’ll have a look at it, I also stumbled across trimesh which seems to also have the capability of repairing STLs</p>

---

## Post #4 by @Przemek_Czuma (2025-08-29 04:54 UTC)

<p>Hi,<br>
If it helps: I’m sealing the mesh in Blender after exporting it to STL from 3D Slicer. There are dedicated tools for this (the 3D Print add-on – quite effective). I also wrote my own add-on that checks for watertightness (in Polish it’s that tricky word: “wodoszczelna” <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> at the top of addon) and allows automating the available there mesh optimization methods, as well as performing a remesh to make the mesh less chaotic than the raw one from 3D Slicer (as in the illustration), smoothing it, reducing size etc. – basically preparing it for 3D printing.</p>
<p>If you don’t feel like using Blender, a good, simple, and effective tool is the Windows mesh repair service, for example through Bambu Studio.</p>
<p>Best regards <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>BEFORE REMESH:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee062fcb0cc325999090be7ac7d1ea06cc72023a.jpeg" data-download-href="/uploads/short-url/xXETmhvCHGENZIzs3teDUNA9EhA.jpeg?dl=1" title="Zrzut ekranu 2025-08-29 063816" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee062fcb0cc325999090be7ac7d1ea06cc72023a_2_690x374.jpeg" alt="Zrzut ekranu 2025-08-29 063816" data-base62-sha1="xXETmhvCHGENZIzs3teDUNA9EhA" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee062fcb0cc325999090be7ac7d1ea06cc72023a_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee062fcb0cc325999090be7ac7d1ea06cc72023a_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee062fcb0cc325999090be7ac7d1ea06cc72023a_2_1380x748.jpeg 2x" data-dominant-color="795936"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Zrzut ekranu 2025-08-29 063816</span><span class="informations">1572×854 312 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>AFTER REMESH:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a16865808ef04ec01a2f403bc8284581094d8d2f.jpeg" data-download-href="/uploads/short-url/n1SxymlpNyIing8X3JMj8LvTyAn.jpeg?dl=1" title="Zrzut ekranu 2025-08-29 064259" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a16865808ef04ec01a2f403bc8284581094d8d2f_2_690x370.jpeg" alt="Zrzut ekranu 2025-08-29 064259" data-base62-sha1="n1SxymlpNyIing8X3JMj8LvTyAn" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a16865808ef04ec01a2f403bc8284581094d8d2f_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a16865808ef04ec01a2f403bc8284581094d8d2f_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a16865808ef04ec01a2f403bc8284581094d8d2f_2_1380x740.jpeg 2x" data-dominant-color="594A3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Zrzut ekranu 2025-08-29 064259</span><span class="informations">1580×849 298 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
