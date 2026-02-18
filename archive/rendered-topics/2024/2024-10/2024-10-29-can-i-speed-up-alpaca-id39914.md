# Can I speed up ALPACA?

**Topic ID**: 39914
**Date**: 2024-10-29
**URL**: https://discourse.slicer.org/t/can-i-speed-up-alpaca/39914

---

## Post #1 by @Chuan (2024-10-29 12:20 UTC)

<p>Hi,</p>
<p>I have around 7500 landmarks, and now I would like to use ALPACA to get other subjects’ landmarks. I have in total of 50 subjects, but the current problem is the processing is very slow and takes so long time for even one subject.<br>
Kindly ask here if anyone know there are methods to speed up the ALPACA process?</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #2 by @muratmaga (2024-10-29 15:23 UTC)

<p>You can disable the projection which sometimes slows down things.</p>
<p>ALPACA is already fairly optimized. You can use the Bayesian coherent drift implementation to speed up the deformable registration, but unless you are on windows, it needs to be built from the source. See the instructions on how to get bcpd from the repo and once you have it built, enable it in alpaca (check acceleration option and locate where the executable is):</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/ohirose/bcpd">
  <header class="source">

      <a href="https://github.com/ohirose/bcpd" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/73142b2df1f737092adbff7559ffd3d4/ohirose/bcpd" class="thumbnail">

  <h3><a href="https://github.com/ohirose/bcpd" target="_blank" rel="noopener nofollow ugc">GitHub - ohirose/bcpd: Bayesian Coherent Point Drift...</a></h3>

    <p><span class="github-repo-description">Bayesian Coherent Point Drift (BCPD/BCPD++/GBCPD/GBCPD++)</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73fa36ede44823f703fd51a2bd7e7c459fd1dc56.png" data-download-href="/uploads/short-url/gxYZsI4RPHuA3nnOr75Nt9a8YGW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73fa36ede44823f703fd51a2bd7e7c459fd1dc56_2_664x500.png" alt="image" data-base62-sha1="gxYZsI4RPHuA3nnOr75Nt9a8YGW" width="664" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73fa36ede44823f703fd51a2bd7e7c459fd1dc56_2_664x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73fa36ede44823f703fd51a2bd7e7c459fd1dc56.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73fa36ede44823f703fd51a2bd7e7c459fd1dc56.png 2x" data-dominant-color="F3F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">948×713 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Having said that 7500 landmark is very large. Even loading and interacting with them in 3D Slicer as is will be slow. Also more importantly, when we extract point clouds in ALPACA to do the point cloud registration, we typically aim for 5000-8000 points (see our paper). So make sure your point cloud densities are not less than the landmarks you are trying to register.</p>
<p>If your goal is to establish dense point clouds of semi landmarks, instead of trying to speed up ALPACA, take a look at our DeCa tool: <a href="https://github.com/smrolfe/DeCa" class="inline-onebox" rel="noopener nofollow ugc">GitHub - smrolfe/DeCA: Dense Correspondence Analysis (DeCA) toolkit</a>. It is not finished yet, and finess, but functional. You need a handful of landmarks (10-12) to align the models rigidly, then you can extract as many points as you like from the template, and then use the DeCaL module to transfer them to the samples. Here is the paper.</p>
<p><a href="https://www.researchgate.net/publication/375111739_DeCA_A_Dense_Correspondence_Analysis_Toolkit_for_Shape_Analysis" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.researchgate.net/publication/375111739_DeCA_A_Dense_Correspondence_Analysis_Toolkit_for_Shape_Analysis</a></p>

---

## Post #3 by @Chuan (2024-10-30 09:13 UTC)

<p>Hi,</p>
<p>Thank you very much for your reply, especially for the point cloud density. I am using bactch processing, and there is no info showing the point density. Does it mean it uses the default setting?</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #4 by @Chuan (2024-10-30 09:54 UTC)

<p>Hi Muratmaga,</p>
<p>Just have a random thought suddenly, but I’m not sure if it’s right. What do you think if I use the bottom-layer python of ALPACA directly instead of using GUI for batch process? Do you think it will be more faster because now it always shows the GUI has no response and stuck.</p>
<p>I assume it will be easy to use python for batch process of ALPACA, because there are only four parameters I need to fill in the GUI.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b74e14e38cc6b7703ccddbca7137f9033abb1646.png" data-download-href="/uploads/short-url/q9AFiEpzRbHQDm70YgRa6luGxlY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b74e14e38cc6b7703ccddbca7137f9033abb1646.png" alt="image" data-base62-sha1="q9AFiEpzRbHQDm70YgRa6luGxlY" width="690" height="427" data-dominant-color="F4F0EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1095×679 23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6361e08e4109b838c12f9b0246818af6b447b1f.png" data-download-href="/uploads/short-url/shsu4g5t6DEA8DgNr3U9TF4LeZV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6361e08e4109b838c12f9b0246818af6b447b1f_2_690x470.png" alt="image" data-base62-sha1="shsu4g5t6DEA8DgNr3U9TF4LeZV" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6361e08e4109b838c12f9b0246818af6b447b1f_2_690x470.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6361e08e4109b838c12f9b0246818af6b447b1f_2_1035x705.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6361e08e4109b838c12f9b0246818af6b447b1f.png 2x" data-dominant-color="F7F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1046×714 58.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards,<br>
Chuan</p>

---

## Post #5 by @muratmaga (2024-10-30 22:30 UTC)

<aside class="quote no-group" data-username="Chuan" data-post="4" data-topic="39914">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/4da419/48.png" class="avatar"> Chuan:</div>
<blockquote>
<p>Just have a random thought suddenly, but I’m not sure if it’s right. What do you think if I use the bottom-layer python of ALPACA directly instead of using GUI for batch process? Do you think it will be more faster because now it always shows the GUI has no response and stuck.</p>
</blockquote>
</aside>
<p>If you have more than one sample, you should definitely use the Batch mode. But if you have only one pair of samples, it probably wouldn’t save you too much time, but you can definitely try.</p>

---

## Post #6 by @SamuelKing (2024-11-19 13:01 UTC)

<p>Thank you, you saved my time.</p>

---
