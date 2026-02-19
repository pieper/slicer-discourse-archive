---
topic_id: 37682
title: "Seek Advice On Merge Surfaces"
date: 2024-08-03
url: https://discourse.slicer.org/t/37682
---

# Seek advice on merge surfaces

**Topic ID**: 37682
**Date**: 2024-08-03
**URL**: https://discourse.slicer.org/t/seek-advice-on-merge-surfaces/37682

---

## Post #1 by @Lulu (2024-08-03 11:08 UTC)

<p>I’m working on a project to reconstruct the surface of the bronchi.<br>
My idea is to generate tubes to compensate for the end loss of the model after smoothing.<br>
I generated tubes of different sizes through the centerline. And I want to merge it with the original bronchi surface.Do you have any good suggestions？<br>
This is the current generated surface and the original surface<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/844fbffac3069aea0e8a4c6c7df06a82c2743245.jpeg" data-download-href="/uploads/short-url/iStT9ikJNo7J5JojceaWRGIvYmV.jpeg?dl=1" title="6a5ced1a045ed049bc198693cce603b" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/844fbffac3069aea0e8a4c6c7df06a82c2743245_2_382x500.jpeg" alt="6a5ced1a045ed049bc198693cce603b" data-base62-sha1="iStT9ikJNo7J5JojceaWRGIvYmV" width="382" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/844fbffac3069aea0e8a4c6c7df06a82c2743245_2_382x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/844fbffac3069aea0e8a4c6c7df06a82c2743245_2_573x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/844fbffac3069aea0e8a4c6c7df06a82c2743245.jpeg 2x" data-dominant-color="F3E4E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6a5ced1a045ed049bc198693cce603b</span><span class="informations">729×952 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This is a similar effect I want to achieve.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a5f197d4779cecb3575829215dc4d17a484623d.png" data-download-href="/uploads/short-url/3LiaaRt3NggbrwwOG6O0Ymj0xu5.png?dl=1" title="a4d2e340866f06ce816f7b5bb50d839" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a5f197d4779cecb3575829215dc4d17a484623d_2_323x500.png" alt="a4d2e340866f06ce816f7b5bb50d839" data-base62-sha1="3LiaaRt3NggbrwwOG6O0Ymj0xu5" width="323" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a5f197d4779cecb3575829215dc4d17a484623d_2_323x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a5f197d4779cecb3575829215dc4d17a484623d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a5f197d4779cecb3575829215dc4d17a484623d.png 2x" data-dominant-color="F5F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a4d2e340866f06ce816f7b5bb50d839</span><span class="informations">433×669 96.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mau_igna_06 (2024-08-03 19:53 UTC)

<p>If I understood well you need to use “union” operation of CombineModels module from Sandbox extension.</p>
<p>HIH</p>

---

## Post #3 by @lassoan (2024-08-03 21:21 UTC)

<p>There are vessel surface reconstruction filters in VMTK that do exactly this. There is no GUI for this reconstruction but you can use the filters in Slicer’s Python console.</p>

---

## Post #4 by @Santiago_Cutiller (2024-08-04 04:09 UTC)

<p>Hi!<br>
How did you generate tubes of different sizes through the centerline?</p>

---

## Post #6 by @Lulu (2024-08-06 02:03 UTC)

<p>Thank you for your advice.<br>
I’m sorry to reply so late.I tried your suggestion, but it didn’t work.I guess because both models are mesh.I don’t know if this is the right guess</p>

---

## Post #7 by @Lulu (2024-08-06 02:11 UTC)

<p>hi,<br>
I am glad to receive your suggestion and apologize for the late response.<br>
I’m not very good with VMTK.Can you tell me how to use this filers？The code would be even better，because I want to integrate it into my code，Automate the entire process.<br>
Thank you again</p>

---

## Post #8 by @Lulu (2024-08-06 02:13 UTC)

<p>hi，<br>
I used slicer to extract the centerline of the trachea, then exported the file and read the data through VTK.And then rebuild by vtk example TubesWithVaryingRadiusAndColors.</p>

---
