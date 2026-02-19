---
topic_id: 27171
title: "Mesh Generation Using Cleaver Method"
date: 2023-01-10
url: https://discourse.slicer.org/t/27171
---

# Mesh generation using Cleaver method

**Topic ID**: 27171
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/mesh-generation-using-cleaver-method/27171

---

## Post #1 by @ZSoltani (2023-01-10 16:37 UTC)

<p>HI ALL,</p>
<p>I’m trying to use Cleaver for meshing a vertebra in Segment Mesher. The output contains regions with different mesh resolutions and the volume elements looks bizarre too (below images). I appreciate any comment on what can be the potential reasons and how they might be fixed.</p>
<p>Thanks,</p>
<p>Zahra</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aae56359eb7a3dc83450d79ba2060a9806d42f82.jpeg" data-download-href="/uploads/short-url/onODaervo1hn9Pl5fQwwZusy0Cu.jpeg?dl=1" title="Screenshot from 2023-01-10 06-25-22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aae56359eb7a3dc83450d79ba2060a9806d42f82_2_637x500.jpeg" alt="Screenshot from 2023-01-10 06-25-22" data-base62-sha1="onODaervo1hn9Pl5fQwwZusy0Cu" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aae56359eb7a3dc83450d79ba2060a9806d42f82_2_637x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aae56359eb7a3dc83450d79ba2060a9806d42f82_2_955x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aae56359eb7a3dc83450d79ba2060a9806d42f82.jpeg 2x" data-dominant-color="837D86"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-01-10 06-25-22</span><span class="informations">1120×878 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99d8c366626be7113dc67cbd61fc94bf54492e56.jpeg" data-download-href="/uploads/short-url/lWZsTWvIFvtfY8wIdDxuJ078C1g.jpeg?dl=1" title="Screenshot from 2023-01-10 06-25-42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99d8c366626be7113dc67cbd61fc94bf54492e56_2_637x500.jpeg" alt="Screenshot from 2023-01-10 06-25-42" data-base62-sha1="lWZsTWvIFvtfY8wIdDxuJ078C1g" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99d8c366626be7113dc67cbd61fc94bf54492e56_2_637x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99d8c366626be7113dc67cbd61fc94bf54492e56_2_955x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99d8c366626be7113dc67cbd61fc94bf54492e56.jpeg 2x" data-dominant-color="807C88"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-01-10 06-25-42</span><span class="informations">1120×878 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mau_igna_06 (2023-01-10 17:11 UTC)

<p>Those darker areas look like triangles with flipped normals on my opinion</p>
<p>Please check if <a href="https://vtk.org/doc/nightly/html/classvtkPolyDataNormals.html" rel="noopener nofollow ugc">vtkPolyDataNormals</a> works for you</p>
<p>Hope it helps</p>

---

## Post #3 by @ZSoltani (2023-01-10 17:19 UTC)

<p>Thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> for your reply. Perhaps below image can show the darker area better.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a860319cc5405cba68ad120ca8d5f3808b5bab04.jpeg" data-download-href="/uploads/short-url/o1wjaWmIQgorNbxnA32HSZQh0Rm.jpeg?dl=1" title="Screenshot from 2023-01-10 07-20-06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a860319cc5405cba68ad120ca8d5f3808b5bab04_2_637x500.jpeg" alt="Screenshot from 2023-01-10 07-20-06" data-base62-sha1="o1wjaWmIQgorNbxnA32HSZQh0Rm" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a860319cc5405cba68ad120ca8d5f3808b5bab04_2_637x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a860319cc5405cba68ad120ca8d5f3808b5bab04_2_955x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a860319cc5405cba68ad120ca8d5f3808b5bab04.jpeg 2x" data-dominant-color="7E7776"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-01-10 07-20-06</span><span class="informations">1120×878 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
