---
topic_id: 37139
title: "Malpaca On Several Species Issue"
date: 2024-07-02
url: https://discourse.slicer.org/t/37139
---

# MALPACA on several species - issue?

**Topic ID**: 37139
**Date**: 2024-07-02
**URL**: https://discourse.slicer.org/t/malpaca-on-several-species-issue/37139

---

## Post #1 by @MSAC (2024-07-02 02:13 UTC)

<p>Operating system: IOS<br>
Slicer version: 5.6.2</p>
<p>Hello Community!</p>
<p>I am new to slicer and ALPACA and I would like to apply a Multi-template (MALPACA) to my data for GMM analysis.<br>
<strong>Some context</strong>: I am working with 4 modern species and archaeological specimens. My objective is to create a template with modern specimens to test the phenotypic/taxonomic potential of the bone that I use and also to compare these modern specimens to archaeological ones. I decided to choose this automatic approach because of the good repeatability, avoid operator effect, open source AND especially because it is very complicated to find homologous landmarks on the bone that I use…!</p>
<p><strong>My issue</strong>:<br>
Firstly, I was trying to test MALPACA on my 4 modern species and I have some troubles applying multi-template.</p>
<p><em>Explanations</em>: I was trying to generate a “ kmeans_selected_templates” on a sample composed of all my specimens of the 4 species mixed together. The idea is to obtain the better representative template of these 4 species, to apply MALPACA on all these modern specimens, to observe the potential of a phenotype/taxonomical signal on modern specimens. The next objective is to apply and test these same (modern) templates on my archaeological specimens. The goal is to see how the both diversities (modern and archaeological) are interacting in statistical analysis.</p>
<p>BUT, I am stuck at the first step with the determination of the Kmeans samples… as I said before, I am not able to create a “ kmeans_selected_templates” when I am mixing all my modern specimens of the 4 species. The step 1 of “generetate reference Point cloud” never really works and I never had acces to the step 4 of “ Multi templates selection” etc…</p>
<p>SO, I made a test on 1 species only and it seems that in this case it works because step 1 and 2 works and I was able to obtain the “Generate Point clouds matched to reference”. So, I deduced that my 4 species are maybe too different to generate a multi template together?</p>
<p><em><strong>Consequently</strong></em>, I was thinking to generate a “kmeans_selected_templates” from each (4) species separately, and, after, groups all these templates together in a same file (one for landmarks points and one for ply models) in order to use them in the MALPACA batch processing “Method” and “Source landmarks” files. Like this, I will be able to obtain more “representative templates” for my modern and archaeological data.</p>
<p><strong>Nevertheless, I am not sure if this procedure is not “too much” and maybe artificial? Before to test, I would like to know</strong>,</p>
<ul>
<li>if someone already proceeds like this?</li>
<li>or have advice from colleagues who are more familiar with these tools. And/or, maybe suggest other procedures…</li>
</ul>
<p>I really thank you in advance for your help!</p>

---

## Post #2 by @chz31 (2024-07-02 04:32 UTC)

<p>I’m surprise that step 1 generating reference pcd did not work when you mix 4 species. All it does is pick up the first specimen in your folder by default and downsample it.</p>
<p>If you could proceed to step 2, did the text box print out any information? I think you are probably right that the 4 species are too different. If so, the text box should print out that there are many specimens have much less unique points sampled, thus very high error rates. See the tutorial: <a href="https://github.com/SlicerMorph/Tutorials/blob/main/MALPACA/K-means_templates_selection.md" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/MALPACA/K-means_templates_selection.md at main · SlicerMorph/Tutorials · GitHub</a>. The matched point clouds are also stored in your output finder,<br>
The multi-species sample we used was chimps, gorilla and orangs.</p>
<p>The generate correspondent point cloud step simply uses the reference point cloud to fetch closest points from other specimens after rigid registration. If specimens are too different, rigid registration won’t perform well (even morphometric analysis may not do well either).</p>
<p>In that case, it is better to do an ALPACA/MALPACA for the four species separately. MALPACA would use each template to landmark each specimen. If the templates from other species are too different, landmarking won’t be accurate. If only one template yields outliers, the impact might be small, since MALPACA would take the median output. MALPACA might still be able to pick up the optimal estimates in most cases (see our sample ape data). You might need to do a small pilot tests to see if MALPACA is able to pick up the better estimate.</p>
<p>Is it possible to know what these four species are and perhaps have some sample data?</p>

---

## Post #3 by @muratmaga (2024-07-02 05:22 UTC)

<aside class="quote no-group" data-username="MSAC" data-post="1" data-topic="37139">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/85e7bf/48.png" class="avatar"> MSAC:</div>
<blockquote>
<p>BUT, I am stuck at the first step with the determination of the Kmeans samples… as I said before, I am not able to create a “ kmeans_selected_templates” when I am mixing all my modern specimens of the 4 species. The step 1 of “generetate reference Point cloud” never really works and I never had acces to the step 4 of “ Multi templates selection” etc…</p>
</blockquote>
</aside>
<p>To answer some of these question, it really would help if you can share some of your data or at least screenshot of how different these four species are.</p>
<p>Are there any error messages when you try to run the kmeans template selection? You may need to open the log file (CTRL+0) and look into it.</p>

---

## Post #4 by @MSAC (2024-07-02 14:14 UTC)

<p>I thank you very much for your both answers. Maybe it is just me who do something wrong too.</p>
<p>I am working with complicated species, taxonomy is a big deal: the four south American camelids (lama, alpaca (ahah), guanaco and vicuna). Usually I use common landmarks/curves GMM, but i would like to try these automatic approach.</p>
<p>I am also working with a complicated bone: the first phalanges who can be mixed (fore/hind) in my samples. I know there is a lot of “difficulties” but I would like to be more closer as I can to the archaeological samples. To obtain commun tool for zooarchaeologists. But Maybe it is not possible.</p>
<p>I come back to you with my “error messages” and a samples of data.</p>

---

## Post #5 by @chz31 (2024-07-02 15:19 UTC)

<p>You can pick up two specimens from two species and use FastModelAlign to test registration. If they are registered well, then ALPACA/MALPACA should be fine: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/FastModelAlign" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/FastModelAlign at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #6 by @MSAC (2024-07-02 16:11 UTC)

<p>ah! maybe it is better to start with that indeed.<br>
I see " distinct sizes because no size reference was provided " in this example… I forgot to think about the scale… my data, indeed, came from several type of scanners… one part from a CT and other part from two Artec spiders… so maybe it is a problem of scale at the beginning. I try this " FastModelalign" and let you know.</p>
<p>Thank you very much!</p>

---

## Post #7 by @MSAC (2024-07-02 16:58 UTC)

<p>I think this is why it not working? when I am mixing specimens from two species here one (fore) phalange from a guanaco and one (hind) phalange of vicuna (my most different configuration possible) it seems that it is not possible to registered correctly. Moreover, my scan are bad quality (I’ve had a problem that I can no longer solve and I need to use this data). It certainly doesn’t help.<br>
I add some screens<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecbdb8124ae7e53841a365a9ee5d4ff3d3bea06a.png" data-download-href="/uploads/short-url/xMj9yDk9E9FUMjOjuRET7eg7UtY.png?dl=1" title="Capture d’écran 2024-07-02 à 18.45.34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecbdb8124ae7e53841a365a9ee5d4ff3d3bea06a_2_496x500.png" alt="Capture d’écran 2024-07-02 à 18.45.34" data-base62-sha1="xMj9yDk9E9FUMjOjuRET7eg7UtY" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecbdb8124ae7e53841a365a9ee5d4ff3d3bea06a_2_496x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecbdb8124ae7e53841a365a9ee5d4ff3d3bea06a_2_744x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ecbdb8124ae7e53841a365a9ee5d4ff3d3bea06a_2_992x1000.png 2x" data-dominant-color="9690AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-07-02 à 18.45.34</span><span class="informations">1444×1454 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d1d3f714ac0f8d261b3189c332ebea9a0e50059.png" data-download-href="/uploads/short-url/8IDMUpktdB2lZQ1lZIp2VaCtmPL.png?dl=1" title="Capture d’écran 2024-07-02 à 18.44.33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d1d3f714ac0f8d261b3189c332ebea9a0e50059_2_469x500.png" alt="Capture d’écran 2024-07-02 à 18.44.33" data-base62-sha1="8IDMUpktdB2lZQ1lZIp2VaCtmPL" width="469" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d1d3f714ac0f8d261b3189c332ebea9a0e50059_2_469x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d1d3f714ac0f8d261b3189c332ebea9a0e50059_2_703x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d1d3f714ac0f8d261b3189c332ebea9a0e50059_2_938x1000.png 2x" data-dominant-color="9E98BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-07-02 à 18.44.33</span><span class="informations">1410×1502 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f7fad45b7811d2947eb8287aea413179a26a9ee.png" data-download-href="/uploads/short-url/93JCSfL2XxgSVABboxuqwvR4m5g.png?dl=1" title="Capture d’écran 2024-07-02 à 18.44.14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f7fad45b7811d2947eb8287aea413179a26a9ee_2_690x436.png" alt="Capture d’écran 2024-07-02 à 18.44.14" data-base62-sha1="93JCSfL2XxgSVABboxuqwvR4m5g" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f7fad45b7811d2947eb8287aea413179a26a9ee_2_690x436.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f7fad45b7811d2947eb8287aea413179a26a9ee_2_1035x654.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f7fad45b7811d2947eb8287aea413179a26a9ee_2_1380x872.png 2x" data-dominant-color="C6C5D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-07-02 à 18.44.14</span><span class="informations">2740×1732 502 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @MSAC (2024-07-02 21:36 UTC)

<p>Hello,<br>
I was trying with a new subsamples of my data (four species)</p>
<ul>
<li>
<p>was able to do the two first steps but the generate point cloud seems strange (screen bellow):<br>
"The reference is mnhn_alp_1907_325_phal_courte_4_1<br>
The number of points in the downsampled reference pointcloud is 465. The error threshold for finding correspondent points is 1.0%<br>
<strong>{} unique points are sampled from each model to match the template pointcloud</strong> "</p>
</li>
<li>
<p>and the last step (kmeans) is not working yet there is this error (more a screen bellow):</p>
</li>
</ul>
<p>" Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ALPACA.py”, line 1153, in onkmeansTemplatesButton<br>
self.scores, self.LM = logic.pcdGPA(pcdFilePaths)<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ALPACA.py”, line 3225, in pcdGPA<br>
LM.lmOrig, landmarkTypeArray = GPAlogic.loadLandmarks(<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1827, in loadLandmarks<br>
import pandas<br>
ModuleNotFoundError: No module named ‘pandas’<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ALPACA.py”, line 1153, in onkmeansTemplatesButton<br>
self.scores, self.LM = logic.pcdGPA(pcdFilePaths)<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/ALPACA.py”, line 3225, in pcdGPA<br>
LM.lmOrig, landmarkTypeArray = GPAlogic.loadLandmarks(<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/SlicerMorph/lib/Slicer-5.6/qt-scripted-modules/GPA.py”, line 1827, in loadLandmarks<br>
import pandas<br>
ModuleNotFoundError: No module named ‘pandas’ "<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbe9888352e65176d47325f408284f5e58dd6b24.png" data-download-href="/uploads/short-url/vnqUl6JR8Xmw308k4gcarepAu0Y.png?dl=1" title="Capture d’écran 2024-07-02 à 22.47.55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbe9888352e65176d47325f408284f5e58dd6b24_2_690x362.png" alt="Capture d’écran 2024-07-02 à 22.47.55" data-base62-sha1="vnqUl6JR8Xmw308k4gcarepAu0Y" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbe9888352e65176d47325f408284f5e58dd6b24_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbe9888352e65176d47325f408284f5e58dd6b24_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbe9888352e65176d47325f408284f5e58dd6b24_2_1380x724.png 2x" data-dominant-color="E1E1E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-07-02 à 22.47.55</span><span class="informations">1644×863 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8059dd56e4105c9d296a710fb0a8ce3208117a6.png" data-download-href="/uploads/short-url/sxtwHA7w5ujDX0MpCITHYHayOhg.png?dl=1" title="Capture d’écran 2024-07-02 à 22.59.07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8059dd56e4105c9d296a710fb0a8ce3208117a6_2_690x332.png" alt="Capture d’écran 2024-07-02 à 22.59.07" data-base62-sha1="sxtwHA7w5ujDX0MpCITHYHayOhg" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8059dd56e4105c9d296a710fb0a8ce3208117a6_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8059dd56e4105c9d296a710fb0a8ce3208117a6_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8059dd56e4105c9d296a710fb0a8ce3208117a6_2_1380x664.png 2x" data-dominant-color="F0EFEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-07-02 à 22.59.07</span><span class="informations">1897×914 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eb63834a15ebdd3ac957f47214a93696826c9d7.png" data-download-href="/uploads/short-url/6FemLDOgtHQnj5ey9vtqL9OXUFx.png?dl=1" title="Capture d’écran 2024-07-02 à 23.36.00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eb63834a15ebdd3ac957f47214a93696826c9d7.png" alt="Capture d’écran 2024-07-02 à 23.36.00" data-base62-sha1="6FemLDOgtHQnj5ey9vtqL9OXUFx" width="690" height="440" data-dominant-color="A28AA9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2024-07-02 à 23.36.00</span><span class="informations">696×444 26.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @muratmaga (2024-07-03 04:58 UTC)

<p>In python console please type:<br>
<code>pip_install("pandas")</code><br>
and then retry.</p>
<p><a class="mention" href="/u/chz31">@chz31</a> kmeans is using GPA logic. GPA relies on pandas, which it installs in its first execution. If people try the kmean module without actually running the GPA ever before, it fails.</p>
<p>Can you add a logic in kmeans to see if pandas is available, and if not, install it.</p>

---

## Post #10 by @chz31 (2024-07-03 19:22 UTC)

<p>I did not realize it. Thanks for the reminder! I’ll add it.</p>
<p><a class="mention" href="/u/msac">@MSAC</a> It appears that based on registration, the bones from different species are indeed a bit too different. Perhaps running separate MALPACA/ALPACA can be a solution. It looks like the bones are different phalanges?</p>

---

## Post #11 by @MSAC (2024-07-08 15:28 UTC)

<p>Sorry for my delay of answer.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Many thanks! in adding this package in the consol as you suggested, I solve my first issue in the kmean steps! so now I am able to go at the end of the procedure.</p>
<p><a class="mention" href="/u/chz31">@chz31</a> no it is the same bone, but when I do a “Pseudo LM generator” followed by a single ALPACA between two specimens of two species my bones are correctly aligned.<br>
So I suppose as you suggested that I have to do kmeans by each species separately (with adjustment tests) in order to obtain 4 templates that I will secondly use with MALPACA on my whole sample. I am trying this process.</p>
<p>Thank you very much to both of you for your quick answers, it’s help a lot.</p>

---

## Post #12 by @muratmaga (2024-07-08 15:44 UTC)

<p>If you got the kmeans working, I would use those samples suggested as templates.</p>

---
