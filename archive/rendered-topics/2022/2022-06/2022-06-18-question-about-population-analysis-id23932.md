# Question about population Analysis

**Topic ID**: 23932
**Date**: 2022-06-18
**URL**: https://discourse.slicer.org/t/question-about-population-analysis/23932

---

## Post #1 by @yuanzhen_cui (2022-06-18 23:21 UTC)

<p>Operating system: MacOs<br>
Slicer version: slicer5.0.2</p>
<p>Hi everyone,</p>
<p>I have implemented population analysis on my dataset which consists of 8 muscles of the same type and I got the mean shape and principal components.</p>
<p>Obviously, I can change the slider according to the table(PCA projection table) to transform the shape (PCA exploration) into one of the muscles of the dataset.</p>
<p>And my question is If I have a new muscle, how can I get the corresponding weights for each component(like the PCA projection table) to convert the shape(PCA exploration) to the new muscle. This is the last step of my Group project <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thanks very much!<br>
Cui</p>

---

## Post #2 by @mau_igna_06 (2022-06-18 23:27 UTC)

<p>It appears you are adding a new muscle set to your data. That could mean one more degree of freedom. Or you could use the muscle components you have now (8) to describe each new muscle.<br>
One step involves making the pca again, the other using what you have with some registration algorithm</p>

---

## Post #3 by @yuanzhen_cui (2022-06-19 13:37 UTC)

<p>Hi Mr. Dominguez,</p>
<p>Sorry my problem description may not be clear enough.</p>
<p>Actually, the dataset consists of <strong>10</strong> muscles <strong>of the same type</strong>. And before the population analysis, I chose <strong>2 of the 10</strong> muscles to use as a <strong>validation set</strong> to evaluate the generalization of the result of population analysis(whether I can use the mean shape and principal components to fit the validation muscles). Then I implement the population analysis on  the remaining <strong>8</strong> muscles.</p>
<p>As shown below, I can get the mean shape(the purple 3D model) to fit any one of the 8 muscles(the yellow 3D model) by adjusting the sliders of pc1 and pc2 according the “PCA projection table”(Right side of picture).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4df63c16662c8c61ad9231655b47c423e1fcc62.jpeg" data-download-href="/uploads/short-url/wEHtlPRr45PVR3wboMK9rAFyhEK.jpeg?dl=1" title="Plot of Population Analysis" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4df63c16662c8c61ad9231655b47c423e1fcc62_2_517x322.jpeg" alt="Plot of Population Analysis" data-base62-sha1="wEHtlPRr45PVR3wboMK9rAFyhEK" width="517" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4df63c16662c8c61ad9231655b47c423e1fcc62_2_517x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4df63c16662c8c61ad9231655b47c423e1fcc62_2_775x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4df63c16662c8c61ad9231655b47c423e1fcc62_2_1034x644.jpeg 2x" data-dominant-color="C2C1DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Plot of Population Analysis</span><span class="informations">1920×1199 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Theoretically, I can indeed fit any muscles of the same type by adjusting the weight of the principal components. And My question is how to get the corresponding weights of components for <strong>muscles of the validation set</strong> just like the result “PCA projection table”.</p>
<p>Thanks very much for your attention!<br>
Cui</p>

---

## Post #4 by @mau_igna_06 (2022-06-19 13:57 UTC)

<p>I think you need to do an optimization of the pc parameters till the remaining muscles are matched to your dataset</p>

---
