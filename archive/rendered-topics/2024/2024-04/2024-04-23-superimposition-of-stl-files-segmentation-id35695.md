---
topic_id: 35695
title: "Superimposition Of Stl Files Segmentation"
date: 2024-04-23
url: https://discourse.slicer.org/t/35695
---

# Superimposition of STL files / segmentation

**Topic ID**: 35695
**Date**: 2024-04-23
**URL**: https://discourse.slicer.org/t/superimposition-of-stl-files-segmentation/35695

---

## Post #1 by @constance_sid (2024-04-23 20:07 UTC)

<p>hello !</p>
<p>I’m writing a thesis for my end of studies. It’s about dental mouvements with orthodontics appliance. I have 2 intra oral scans that I need to analyse and compare.<br>
those scans are 3D stl files.<br>
i figured out that I need to superimpose them and then compare them. But if I want to evaluate the movement done for each teeth I need to do a segment of each teeth? can I do that with stl files?<br>
I read the forum and watched tutorial videos but I cannot seem to find how to segment my file.<br>
can anyone help me? thank you very much</p>

---

## Post #2 by @lassoan (2024-04-25 03:10 UTC)

<p>Yes, you can superimpose STL files and segmentations. You can register them based on matching landmark points, using <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">Fiducial Registration Wizard module</a>.</p>
<p>You can quantify motion by exporting the segmentation to model and then use ModelToModelDistance extension to compute surface distances.</p>

---

## Post #3 by @constance_sid (2024-04-25 18:11 UTC)

<p>thank you very much for you answer. I 'm so sorry but it seems that every time I download on the software the stl files, they automatically misaligned and I can’t succed to realigned them.<br>
one of the scan is hiding part or all of the other scan. is there something I can do about this ?</p>

---

## Post #4 by @lassoan (2024-04-25 18:31 UTC)

<p>Intraoral scans are not aligned with CBCT scans, because they are not in the same coordinate system. If you align the surface scan with the CBCT and save the scene then if you later load that scene, the registration is preserved.</p>

---

## Post #5 by @muratmaga (2024-04-25 19:21 UTC)

<aside class="quote no-group" data-username="constance_sid" data-post="3" data-topic="35695">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/constance_sid/48/70167_2.png" class="avatar"> constance_sid:</div>
<blockquote>
<p>one of the scan is hiding part or all of the other scan. is there something I can do about this ?</p>
</blockquote>
</aside>
<p>This is not important for registration. But if you do want to see them separately, turn off their visibility, switch to Dual 3D layout, and then drag and drop the STL objects into separate 3D viewers one by one.</p>
<p>Also, give FastModelAlign in SlicerMorph a try. It does rigid registration of models.</p>

---

## Post #6 by @constance_sid (2024-05-09 16:35 UTC)

<p>ok thank you so much ! I managed to register them. this is where I am .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10ecbb2c9000e026356188c71cb11ca929e2008f.jpeg" data-download-href="/uploads/short-url/2pIPGDTy1MNFXMVD6Zwd3OcTLAj.jpeg?dl=1" title="Capture d’écran 2024-05-09 à 18.13.26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ecbb2c9000e026356188c71cb11ca929e2008f_2_690x392.jpeg" alt="Capture d’écran 2024-05-09 à 18.13.26" data-base62-sha1="2pIPGDTy1MNFXMVD6Zwd3OcTLAj" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ecbb2c9000e026356188c71cb11ca929e2008f_2_690x392.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ecbb2c9000e026356188c71cb11ca929e2008f_2_1035x588.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10ecbb2c9000e026356188c71cb11ca929e2008f_2_1380x784.jpeg 2x" data-dominant-color="BBBFD6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-05-09 à 18.13.26</span><span class="informations">1920×1092 95.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but I want to evaluate the movement done by each teeth from the first STL file to the other.How can I choose or create reference axis in order to compare properly ?</p>
<p>I know I can export my transformation nodes to excel to have every data. do you think I need to isolate each and every tooth ?</p>
<p>thank you so much</p>

---

## Post #7 by @muratmaga (2024-05-09 17:57 UTC)

<p>Yes, if you need to get the information on per tooth basis, you will need to isolate them i imagine.</p>

---
