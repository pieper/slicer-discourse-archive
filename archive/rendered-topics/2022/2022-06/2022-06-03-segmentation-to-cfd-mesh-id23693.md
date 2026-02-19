---
topic_id: 23693
title: "Segmentation To Cfd Mesh"
date: 2022-06-03
url: https://discourse.slicer.org/t/23693
---

# Segmentation to CFD Mesh

**Topic ID**: 23693
**Date**: 2022-06-03
**URL**: https://discourse.slicer.org/t/segmentation-to-cfd-mesh/23693

---

## Post #1 by @Elias_Karabelas (2022-06-03 16:32 UTC)

<p>Hey there,</p>
<p>I have a question concerning the transition from segmentation to meshing. I managed to segment some coronary arteries with the aorta and also have the centerline in there (see my slicer screenshot)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c97603bd95ebbbd3245568f9fb48b98a0b978a.jpeg" data-download-href="/uploads/short-url/7o7YHYKZH8ApE45K8mQJW3eliXw.jpeg?dl=1" title="slicer_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c97603bd95ebbbd3245568f9fb48b98a0b978a_2_690x287.jpeg" alt="slicer_1" data-base62-sha1="7o7YHYKZH8ApE45K8mQJW3eliXw" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c97603bd95ebbbd3245568f9fb48b98a0b978a_2_690x287.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c97603bd95ebbbd3245568f9fb48b98a0b978a_2_1035x430.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33c97603bd95ebbbd3245568f9fb48b98a0b978a_2_1380x574.jpeg 2x" data-dominant-color="6D738B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_1</span><span class="informations">1920×800 92.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In a next step I extracted the surfaces of the segmentation and visualized them in ParaView<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b563f8ee8112544d56fa31a7d483bc439564096.jpeg" data-download-href="/uploads/short-url/1Ci2n29LCrnJV6Ef0e2X7jmGNsq.jpeg?dl=1" title="paraview" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b563f8ee8112544d56fa31a7d483bc439564096_2_690x287.jpeg" alt="paraview" data-base62-sha1="1Ci2n29LCrnJV6Ef0e2X7jmGNsq" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b563f8ee8112544d56fa31a7d483bc439564096_2_690x287.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b563f8ee8112544d56fa31a7d483bc439564096_2_1035x430.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b563f8ee8112544d56fa31a7d483bc439564096_2_1380x574.jpeg 2x" data-dominant-color="DEDEDE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">paraview</span><span class="informations">1920×800 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So my question regards this extracted surface: I want to do some CFD simulations in the coronaries and the aorta and for generating a suitable mesh I would need to have some sharp boundaries capping of the outlets of coronaries in the aorta and coronaries. Is there any way to achieve this in slicer directly? It was somewhat possible in vmtk as far as I remember (vtmksurfaceclipper cutted normal to the centerline)</p>
<p>Thanks<br>
Elias</p>

---

## Post #2 by @mau_igna_06 (2022-06-03 17:14 UTC)

<p>If I understand yiur question right you would need to use to use the dynamic modeler plane cut tool with cap option on</p>

---

## Post #3 by @researchtomliu (2022-06-05 14:06 UTC)

<p>You might input the stl model to the “Materialise 3-matic 12.0 (x64)” and regenerate the hollow model with you needed.</p>

---

## Post #4 by @mau_igna_06 (2022-06-05 18:47 UTC)

<p>You can also use hollow tool of Slicer to achieve the same. Use plamar cut without capping option to get your empty on the inside model</p>
<p>Thank you for asking</p>

---

## Post #5 by @Elias_Karabelas (2022-06-20 14:26 UTC)

<p>Hey Mauro, thanks!<br>
So I tried the Dynamic modeller but it is very fuzzy to use it. I have Slicer 4.13 and it seems I cannot make planes with more than one point for spanning a normal, every time I try it adds a new plane. So is there some way to use dynamic modeler and prescribe a point and a normal spanning the plane?</p>

---

## Post #6 by @mau_igna_06 (2022-06-20 14:44 UTC)

<p>Now that’s the default behavior. You need to go to the markups module and set the plane mode to be 3 points</p>

---
