---
topic_id: 46332
title: "Deca Mean Shape Model Partly Coarse Surface"
date: 2026-02-27
url: https://discourse.slicer.org/t/46332
---

# DECA mean shape model: partly coarse surface

**Topic ID**: 46332
**Date**: 2026-02-27
**URL**: https://discourse.slicer.org/t/deca-mean-shape-model-partly-coarse-surface/46332

---

## Post #1 by @MrMarkus (2026-02-27 14:47 UTC)

<p>Hi,</p>
<p>I am using DECA for some shape analysis. I am wondering why the resulting reference / atlas shape model appears to have partly coarse surface.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f9c50ceab191e78a281434662ac0b2cc7d5cec4.jpeg" data-download-href="/uploads/short-url/94IZ5NYc0EfSTcYh4nTXp7s2GLG.jpeg?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f9c50ceab191e78a281434662ac0b2cc7d5cec4.jpeg" alt="grafik" data-base62-sha1="94IZ5NYc0EfSTcYh4nTXp7s2GLG" width="231" height="490"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">231×490 20.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The workflow for comparing 2 groups looks like this:</p>
<ul>
<li>first: using DeCAL to increase the number of points –&gt; up to &gt; 200 from initially manually 20 LM place of both groups</li>
<li>second: use the LM_aligned_200points and model_alignes_200points of one group to create an atlas using DECA</li>
<li>third: use this resulting atlas for comparing the shape variance between the atlas and the indiviual samples of group 2 using DECA</li>
</ul>
<p>Maybe the initial number of manually placed LM is too less. Although I checked the initially aligned models based on the 20 LM –&gt; they are well aligned with the resulting first base / reference.</p>
<p>Any idea how to improve the mesh of the reference model?</p>
<p>THANKS!</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2026-02-27 16:35 UTC)

<p>Do you have damage or missing parts in your input models?</p>

---

## Post #3 by @MrMarkus (2026-02-27 17:22 UTC)

<p>Hi,</p>
<p>the models which are used are fine. No issues visible, size 40 MB after decimation, repair, normals recomputation and minor smoothing.</p>
<p>These data is used for generating the reference using DECA.</p>
<p>And the computed reference models are not similar affected showing more or less ripples.<br>
Infact several reference models are derived from different starting data.</p>
<p>In short: the starting data seems to be fine.</p>
<p>Best,<br>
Markus</p>

---
