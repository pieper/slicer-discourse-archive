# Is there a way to have all vertices on a vtk model be markups/landmarks?

**Topic ID**: 28752
**Date**: 2023-04-04
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-have-all-vertices-on-a-vtk-model-be-markups-landmarks/28752

---

## Post #1 by @Gening_Dong (2023-04-04 20:54 UTC)

<p>Hi,</p>
<p>I’m trying to match the node IDs between two vtk models. I was thinking if it’s possible to have all vertices on a vtk model be markups, so that I can directly use the vertices on the surface of the source model as its landmarks and perform ALPACA in the SlicerMorph module.</p>
<p>Thanks,<br>
Gening</p>

---

## Post #2 by @muratmaga (2023-04-04 22:28 UTC)

<p>You can look at the script repository and to probably work that out.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups</a><br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#models" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#models</a></p>
<p>What is your goal with ALPACA? To register these two vtk models, or to transfer your landmarks from one model to the other?</p>

---

## Post #3 by @Gening_Dong (2023-04-04 22:38 UTC)

<p>Thanks for the reply!</p>
<p>I’d like to match points 1:1 on two vtk models. My plan is to register two vtk models using ALPACA first and then match the points between the TPS warped model and the target model by finding nearest neighbors of points.</p>
<p>Would it be possible to directly transfer landmarks from one model to the other using SlicerMorph? I saw the ProjectSemiLM utility modules, but could it project those landmarks to the vertices of the target model?</p>
<p>Best,</p>
<p>Gening</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13228e9e732d507c72b00e023276e1da7fbb4a5c.png" data-download-href="/uploads/short-url/2Jh6PAzukHbJEafq2farcG87BSI.png?dl=1" title="A7CF354468834AF2A6902E7B6C953F14.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13228e9e732d507c72b00e023276e1da7fbb4a5c.png" alt="A7CF354468834AF2A6902E7B6C953F14.png" data-base62-sha1="2Jh6PAzukHbJEafq2farcG87BSI" width="690" height="1" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">A7CF354468834AF2A6902E7B6C953F14.png</span><span class="informations">709×2 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2023-04-04 22:48 UTC)

<aside class="quote no-group" data-username="Gening_Dong" data-post="3" data-topic="28752">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gening_dong/48/14706_2.png" class="avatar"> Gening_Dong:</div>
<blockquote>
<p>Would it be possible to directly transfer landmarks from one model to the other using SlicerMorph? I saw the ProjectSemiLM utility modules, but could it project those landmarks to the vertices of the target model?</p>
</blockquote>
</aside>
<p>ALPACA will transfer points on one (source) model to the target model for you.</p>
<p>ALPACA is a point-cloud registration. We often work with 3D models with hundreds of thousands (or more) vertices, but our anatomical landmarks on them are far sparser (from tens to thousands range). To improve the speed, we turn the models into downsampled pointclouds, do the registration as point clouds, and then apply the resultant transformation to the models. This seem to perform sufficiently well, and rather fast, for our use cases. I am not sure how well your LMs will be transferred if you use every single vertex as a landmark. We never tried such approach.</p>
<p>TPS deformation is very slow when you have large number of points. Also projectSemiLM module requires existence of manually annotated landmarks on source and target models (see <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ProjectSemiLM">https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ProjectSemiLM</a>). I don’t think it will work for your case.</p>

---

## Post #5 by @Chuan (2023-11-16 08:52 UTC)

<p>Hi Gening,</p>
<p>Recently I have a similar task with yours. Could you tell me which way did you finally choose then to extract all nodes as landmarks and transfer those landmarks to other target models?</p>
<p>Best regards,<br>
Chuan</p>

---
