---
topic_id: 35733
title: "Conversion To Binary Labelmap Freezes Slicer"
date: 2024-04-25
url: https://discourse.slicer.org/t/35733
---

# Conversion to binary labelmap freezes Slicer

**Topic ID**: 35733
**Date**: 2024-04-25
**URL**: https://discourse.slicer.org/t/conversion-to-binary-labelmap-freezes-slicer/35733

---

## Post #1 by @koenterheegde (2024-04-25 14:43 UTC)

<p>Hey everyone,</p>
<p>I have been using Slicer a lot to generate a .STL from a segmentation. The nice thing in here was that I could apply smoothing very easily. I’m doing the segmentation myself now, and generate a .STL from it (own program). However, I can’t manage to smooth it and wanted to see if Slicer could do it for me. I import the .STL and set the geometry to that of the .STL. I then want to smooth it, but Slicer asks me to change the source representation to a binary labelmap. When I click ‘Yes’, Slicer completely freezes. I looked at this issue: <a href="https://discourse.slicer.org/t/retrieving-statistics-from-rtstruct-and-scalar-volume-binary-labelmap-representation-computation-is-very-slow/28100" class="inline-onebox">Retrieving statistics from RTSTRUCT and scalar volume - binary labelmap representation computation is very slow</a>, but for me there is no option to select the “Planar contour → Ribbon model → Binary labelmap” path to create the binary labelmap. What is the issue here?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d3a34427a655296a7c7d3622261f47238279079.png" data-download-href="/uploads/short-url/k9m1yAqbrwPsy9fuL9sfRpA6vX3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d3a34427a655296a7c7d3622261f47238279079.png" alt="image" data-base62-sha1="k9m1yAqbrwPsy9fuL9sfRpA6vX3" width="285" height="500" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">310×543 7.85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-04-25 14:46 UTC)

<p>Did you try the smoothing in Surface toolbox? That does not require changing the representation to segmentation.</p>

---

## Post #3 by @koenterheegde (2024-04-25 14:56 UTC)

<p>I just did, but it doesn’t lead to the result I want. In the Surface Toolbox, the only options are Taubin and Laplacian Smoothing. The smoothing used in the segment editor is Median Smoothing if I understood correctly. This is the result after applying Laplacian smoothing with 500 iterations and relaxation factor of 0.5:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/771d64022f8b755f33f71884a74e5d904dfa719c.png" data-download-href="/uploads/short-url/gZJMRL105EjGeAlAFJkQBV6LKAA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/771d64022f8b755f33f71884a74e5d904dfa719c_2_504x500.png" alt="image" data-base62-sha1="gZJMRL105EjGeAlAFJkQBV6LKAA" width="504" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/771d64022f8b755f33f71884a74e5d904dfa719c_2_504x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/771d64022f8b755f33f71884a74e5d904dfa719c_2_756x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/771d64022f8b755f33f71884a74e5d904dfa719c.png 2x" data-dominant-color="979BC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">796×789 97.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And I want to get something like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e42d2b087a34e141cebd2927bd828119c023c9aa.jpeg" data-download-href="/uploads/short-url/wyxDoJp2ajNIG6zEXdMXVBoOv0u.jpeg?dl=1" title="Schermafbeelding 2024-03-13 123413 (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e42d2b087a34e141cebd2927bd828119c023c9aa_2_690x360.jpeg" alt="Schermafbeelding 2024-03-13 123413 (1)" data-base62-sha1="wyxDoJp2ajNIG6zEXdMXVBoOv0u" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e42d2b087a34e141cebd2927bd828119c023c9aa_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e42d2b087a34e141cebd2927bd828119c023c9aa_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e42d2b087a34e141cebd2927bd828119c023c9aa_2_1380x720.jpeg 2x" data-dominant-color="F8F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermafbeelding 2024-03-13 123413 (1)</span><span class="informations">1920×1004 53.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Important difference is to know that the in the first picture I did the segmentation in my own program and in the second picture it was done in Slicer.</p>

---

## Post #4 by @muratmaga (2024-04-25 19:18 UTC)

<p>What happens when you drag and drop the STL into slicer scene, and as opposed to loading it as Model, choose Segmentation in the options?</p>

---

## Post #5 by @koenterheegde (2024-04-26 07:18 UTC)

<p>I’ve now loaded it in using ‘Add data’ and then select the .STL. Haven’t converted it into a model and then I can make it a binary labelmap in the ‘Segmentations’ module using just the standard ‘Create’ option, so not even using the advanced option. However, I still need a model in order to smooth it in the segment editor and I don’t have a model now.</p>

---
