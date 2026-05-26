---
topic_id: 46332
title: "DECA mean shape model: partly coarse surface"
date: 2026-02-27
url: https://discourse.slicer.org/t/46332
last_bumped: 2026-03-16T16:02:33.283Z
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

## Post #4 by @MrMarkus (2026-03-06 11:15 UTC)

<p>Hi,</p>
<p>I repeated the compuation of the mean shape. This time I used the mouse data of the DECA tutorial. <a href="https://github.com/SlicerMorph/Mouse_Models/tree/main" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/Mouse_Models · GitHub</a></p>
<p>Again one can notice kind of rough surface. I am wondering where does this come from?<br>
Mean shape of 60 skulls, I expect that there won´t be such edges / ripples generated.</p>
<p>Is this normal behaviour? I am wondering, such kind of “notch” is not visible in the skull data….</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38250a110cc3d131cf471386b30175466740277e.jpeg" data-download-href="/uploads/short-url/80G5S8k9dJNsYz5RpmGqZLKdqlE.jpeg?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38250a110cc3d131cf471386b30175466740277e_2_690x278.jpeg" alt="grafik" data-base62-sha1="80G5S8k9dJNsYz5RpmGqZLKdqlE" width="690" height="278" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38250a110cc3d131cf471386b30175466740277e_2_690x278.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38250a110cc3d131cf471386b30175466740277e_2_1035x417.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38250a110cc3d131cf471386b30175466740277e_2_1380x556.jpeg 2x" data-dominant-color="70705B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1501×605 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please comment on this mean shape outcome.</p>
<p>Thanks!</p>
<p>Best,<br>
Markus</p>

---

## Post #5 by @muratmaga (2026-03-09 00:32 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="4" data-topic="46332">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>Could you please comment on this mean shape outcome.</p>
</blockquote>
</aside>
<p>There shouldn’t be an artifact like that, unless one of the models have it. And I don’t think any of the models included in the sample data has a damage.</p>
<p>The other place it can possibly come is a mismatched landmarked that is warping the model incorrectly. Unfortunately as it is, DeCaL does not save the intermediate steps in the atlas creation. But DeCA does.</p>
<p>So use DeCa module to create the atlas from scratch one more time. Selections are very similar to DeCaL. Just make sure you enabled the “Create Output for Error checking” option. When you run DeCa this will create the folder errorChecking in the specified output folder where the warped models are saved. Load all of them into your scene, and see if there are any that appears warped incorrectly or have artifacts like that.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58eab8ac68569e47d4373ab19f8320e9ceecba62.png" data-download-href="/uploads/short-url/cGAU9gZPK2uTvnMFslH9CqDbuFA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58eab8ac68569e47d4373ab19f8320e9ceecba62.png" alt="image" data-base62-sha1="cGAU9gZPK2uTvnMFslH9CqDbuFA" width="381" height="500" data-dominant-color="E9E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">491×643 22.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @MrMarkus (2026-03-11 13:21 UTC)

<p>Hi,</p>
<p>the processing was repeated using DeCA and the available public data set ( <a href="https://github.com/SlicerMorph/Mouse_Models/tree/main" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/Mouse_Models · GitHub</a> )</p>
<p>The result was the same. None of the data sample showed such a kind of ripple/ notch in that specific anatomical location.</p>
<p>I assume that this is the “normal” behaviour of the algorithm. According to the publication (DOI:<a href="https://doi.org/10.1007/978-3-031-46914-5_21?urlappend=%3Futm_source%3Dresearchgate.net%26utm_medium%3Darticle" rel="noopener nofollow ugc">10.1007/978-3-031-46914-5_21</a>) the step of “mean template building” is described as:</p>
<p><em>“….Optionally, the mean templatemodel can ﬁrst be smoothed to remove unwanted local shape variation or decimated to reduce the number of point correspondences…”</em></p>
<p>Regarding mismatch of the landmarks:</p>
<ul>
<li>how to define “mismatch” in the situation of altered anatomical shape? → it is this shape difference which is of interest</li>
<li>alternative rigid registration approach –&gt; make use of the available “fast alignment” module?</li>
</ul>
<p>Besides smoothing the reference atlas, one “simple /fuzzy” option is to use GPA and select the resulting sample which is closest to the mean shape of the group.</p>
<p>I guess every user needs to find out which “approach” / “workflow” is best suited for the actual<br>
analysis. And the ripple/notch is introduced by the generation of the mean shape step.</p>
<p>I guess that´s how it is <img src="https://emoji.discourse-cdn.com/twitter/man_shrugging.png?v=15" title=":man_shrugging:" class="emoji" alt=":man_shrugging:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @muratmaga (2026-03-13 16:18 UTC)

<p>Sorry for the late response it has been a busy week.</p>
<p>Your conclusion is correct you need to decide whether the produced template is correct and needs editing, smoothing is required.</p>
<p>Where the defects comes from:</p>
<ol>
<li>DeCA ultimately uses one of the models as a reference to calculate the final template. This changes based on the samples and landmark distribution.</li>
<li>It appears to me one of the samples (LP.ply) in that set of mouse models have a slight scanning artifact right in that area, and that sample ended up being chosen as to serve as the basis of the template. So the issue in the sample propagated to the template. That’s a common problem in the template based analyses. I am going to update that module UI log clearly specifies what samples are chosen for each step (there are two different steps for that), so that finding these kind of issues would be a bit easier.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a38054758863c5b92de1245307d54daebdd19aae.jpeg" data-download-href="/uploads/short-url/nkoLWqMBWUqpIFRVLMd7orxUpsi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a38054758863c5b92de1245307d54daebdd19aae_2_307x500.jpeg" alt="image" data-base62-sha1="nkoLWqMBWUqpIFRVLMd7orxUpsi" width="307" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a38054758863c5b92de1245307d54daebdd19aae_2_307x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a38054758863c5b92de1245307d54daebdd19aae_2_460x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a38054758863c5b92de1245307d54daebdd19aae_2_614x1000.jpeg 2x" data-dominant-color="A1A368"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">695×1130 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I didn’t look all samples very carefully, but there is another sample (PWD) with an unfused cranium</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/baeda6468dbe4fe3f781d6723a11982ef0a013ea.jpeg" data-download-href="/uploads/short-url/qFDYdrupAA86NLqjR4BxwWr4ZBM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baeda6468dbe4fe3f781d6723a11982ef0a013ea_2_296x499.jpeg" alt="image" data-base62-sha1="qFDYdrupAA86NLqjR4BxwWr4ZBM" width="296" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baeda6468dbe4fe3f781d6723a11982ef0a013ea_2_296x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baeda6468dbe4fe3f781d6723a11982ef0a013ea_2_444x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/baeda6468dbe4fe3f781d6723a11982ef0a013ea.jpeg 2x" data-dominant-color="A6A779"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">581×979 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>That would have been a bad sample to serve as a reference (it can, because that decision is based on the landmark coordinates, not the model itself).</p>
<p>So if you want you can take these two out, retry the pipeline and see if you can get a smoother atlas. But in the end, there will always be some sort of a template bias that you should be mindful of.</p>

---

## Post #8 by @MrMarkus (2026-03-16 10:24 UTC)

<p>Thank you very much for taking the time to look into this matter.</p>
<p>I removed the two samples. The reference looks little bit better now:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa9321b7e7ec313b210aa97d003335f5acaec5d.jpeg" data-download-href="/uploads/short-url/AtGfON2BFE4yjySgnUi0jBIiAmF.jpeg?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffa9321b7e7ec313b210aa97d003335f5acaec5d_2_268x500.jpeg" alt="grafik" data-base62-sha1="AtGfON2BFE4yjySgnUi0jBIiAmF" width="268" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffa9321b7e7ec313b210aa97d003335f5acaec5d_2_268x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffa9321b7e7ec313b210aa97d003335f5acaec5d_2_402x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa9321b7e7ec313b210aa97d003335f5acaec5d.jpeg 2x" data-dominant-color="565601"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">434×808 52.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best,<br>
Markus</p>

---

## Post #9 by @muratmaga (2026-03-16 16:02 UTC)

<p>If you update your DenseCorrespondence extension to the latest version, it now output the names of the samples selected for both initial rigid alignment and base mesh calculation. Most cases these would be the same, but it is not guaranteed to be the case. You can then check that specific sample and evaluate whether that’s a high quality model to serve as a template:</p>
<p>(This is displayed in the log Widget of both DeCAL and DeCA tabs)</p>
<p><strong>Sample selected for rigid alignment: B6C3F1</strong></p>
<p>Generating the average template</p>
<p><strong>Sample selected for base model calculation: B6C3F1_align</strong></p>
<p>Saving atlas model to /Users/amaga/Desktop/Mouse_Models/2/Mouse_Models/DeCaL_Out/2026_03-16_08_53_30/decaAtlasModel.ply</p>
<p>Saving atlas landmarks to /Users/amaga/Desktop/Mouse_Models/2/Mouse_Models/DeCaL_Out/2026_03-16_08_53_30/decaAtlasLM.mrk.json</p>

---
