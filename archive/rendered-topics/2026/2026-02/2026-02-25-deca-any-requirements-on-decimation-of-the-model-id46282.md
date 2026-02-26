---
topic_id: 46282
title: "Deca Any Requirements On Decimation Of The Model"
date: 2026-02-25
url: https://discourse.slicer.org/t/46282
---

# DECA --> any requirements on decimation of the model?

**Topic ID**: 46282
**Date**: 2026-02-25
**URL**: https://discourse.slicer.org/t/deca-any-requirements-on-decimation-of-the-model/46282

---

## Post #1 by @MrMarkus (2026-02-25 14:35 UTC)

<p>Hi,</p>
<p>I am wondering if there are any recommandations for decimation of the 3D model<br>
of interest.</p>
<p>Working with CT data of mouse skull, the original 3D ply model is about 100 MB.<br>
After running “quadratic” decimation with 0.6% reduction the size is about 40 MB.</p>
<p>e.g:</p>
<ul>
<li>which decimation algorithm should be used in 3D Slicer?</li>
<li>should normals be re-computed?</li>
<li>what about minor smoothing after decimation?</li>
<li>and a kind of “repair” steps? should be also applied?</li>
<li>which coordiante system to store the reduced model?</li>
<li>which format for 3D models should be used toether with DECA?</li>
<li>is there a way to “evaluate” the quality of the resulting mesh after decimation?</li>
</ul>
<p>Are there any recommandations for CT data of mouse skull ? / biological samples?</p>
<p>Thanks in advance.</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2026-02-25 16:16 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="1" data-topic="46282">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<ul>
<li>which decimation algorithm should be used in 3D Slicer?</li>
<li>should normals be re-computed?</li>
<li>what about minor smoothing after decimation?</li>
<li>and a kind of “repair” steps? should be also applied?</li>
<li>which coordiante system to store the reduced model?</li>
<li>which format for 3D models should be used toether with DECA?</li>
<li>is there a way to “evaluate” the quality of the resulting mesh after decimation?</li>
</ul>
</blockquote>
</aside>
<p>I got these questions often in the workshops and courses I teach. The issue is there is no one size fits all answer to these. it is all about what you want to use the model for and what is acceptable for the analysis (is a high resolution scans of a single specimen that you would like to do detailed FEA on, or it is one of the thousands of specimens you can scanned you want to train a deep-learning algorithm to analyze shape variation). They have very different tolerances on what the model resolution (You can’t build DL model with thousands model each which has 100M vertices, and if you reduce 100M vertex model to 200K for FEA you probably are not going to get the detailed answer you are looking for).</p>
<p>I forgot the name of the most recent algorith used for decimation, but if you look at the forum you can find it youself, or search in the Slicer repository. In general you can probably decimate 90% of the vertices from a microCT scan for solid geometries. Skulls are difficult because there are many thin regions (like orbital walls, or zygomatic arches, or auditory bullae etc)  and if there are any gaps, decimation may enlarge those.</p>
<p>Ultimately this is something you probably need to experiment on by running a script with dozens of parameters and then decide them for yourself.</p>
<p>As for what formats to be used for DeCA, any 3D format that Slicer understands should be fine. We typically use PLY or OBJ.</p>

---
