---
topic_id: 16772
title: "Voila With Slicerjupyter"
date: 2021-03-26
url: https://discourse.slicer.org/t/16772
---

# Voila with slicerJupyter

**Topic ID**: 16772
**Date**: 2021-03-26
**URL**: https://discourse.slicer.org/t/voila-with-slicerjupyter/16772

---

## Post #1 by @fpsiddiqui91 (2021-03-26 10:13 UTC)

<p>Hi all,</p>
<p>Sorry, I am asking this question again as a new topic. I am trying to use Jupyter slicer to visualize my results and share it to some non-technical users. For this, I am planning to use Viola with a jupyter notebook.</p>
<p>First I have developed my Jupyter notebook (following <a class="mention" href="/u/lassoan">@lassoan</a> notebook : <a href="https://github.com/Slicer/SlicerNotebooks.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerNotebooks: Examples that illustrate how to use 3D Slicer via Jupyter notebooks in Python</a>) which visualizes my results. It worked well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b527fa88ec1291a44c2ba8dff41396a419496cc2.jpeg" data-download-href="/uploads/short-url/pQA4Id8qY7k2kJ7Vl3rsnLImyKC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b527fa88ec1291a44c2ba8dff41396a419496cc2_2_662x500.jpeg" alt="image" data-base62-sha1="pQA4Id8qY7k2kJ7Vl3rsnLImyKC" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b527fa88ec1291a44c2ba8dff41396a419496cc2_2_662x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b527fa88ec1291a44c2ba8dff41396a419496cc2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b527fa88ec1291a44c2ba8dff41396a419496cc2.jpeg 2x" data-dominant-color="C7C5C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">976×737 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now I want to remove the code blocks from my notebook, so a user can directly interact with the results. For this I am trying to integrate voila with binder as follows:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/108b4af3dc3fe933aed32a76a2c42c7fc82a8067.png" alt="image" data-base62-sha1="2mm4wnwBaRCSHZurGMtpigL6Uw7" width="690" height="293"></p>
<p>but I am getting this error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de87dedc70c08ecdb7248259ccaa612cb37c01f4.png" data-download-href="/uploads/short-url/vKB6brVJEwWJMQJUBkwFuNjWXEo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de87dedc70c08ecdb7248259ccaa612cb37c01f4.png" alt="image" data-base62-sha1="vKB6brVJEwWJMQJUBkwFuNjWXEo" width="690" height="220" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">715×228 8.79 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think I am making some mistakes with the docker file or something. Can you please help me with this?</p>
<p>For your reference, my repository is:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/FaizanSiddiqui91/slicer_notebook_test">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/FaizanSiddiqui91/slicer_notebook_test" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/8b0068f90dd03116c5a95d6307874b0ba6da5511bd749d4ed544225a131ef23e/FaizanSiddiqui91/slicer_notebook_test" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/FaizanSiddiqui91/slicer_notebook_test" target="_blank" rel="noopener nofollow ugc">GitHub - FaizanSiddiqui91/slicer_notebook_test</a></h3>

  <p>Contribute to FaizanSiddiqui91/slicer_notebook_test development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @fpsiddiqui91 (2021-03-30 13:54 UTC)

<p>Hi,</p>
<p>I am still stuck in this problem,. I have been reading several articles, e.g:<br>
<a href="https://blog.jupyter.org/slicerjupyter-a-3d-slicer-kernel-for-interactive-publications-6f2ad829f635" class="onebox" target="_blank" rel="noopener nofollow ugc">https://blog.jupyter.org/slicerjupyter-a-3d-slicer-kernel-for-interactive-publications-6f2ad829f635</a></p>
<p>it seems fairly easy to deploy your app with Voila, however I could not manage to do it yet. Has anyone tried this? Can anyone share any example?<br>
For reference, the link of my repo is attached in my last message…</p>
<p>Thanks.</p>

---

## Post #5 by @fpsiddiqui91 (2021-03-31 14:15 UTC)

<p>Hello, I have been trying other options. I came across with a Jupyer appmode: (<a href="https://github.com/oschuett/appmode" class="inline-onebox" rel="noopener nofollow ugc">GitHub - oschuett/appmode: A Jupyter extensions that turns notebooks into web applications.</a>). The app mode is similar to what we have in voila, however, using appmode I could not be able to run Slicer Kernel. There are some problems with the Docker I think.</p>
<p>Can anyone help me with this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/552f43f0ff9d71e29a4db72bbd54c3a0e0e29b31.png" data-download-href="/uploads/short-url/c9zQJPufKtOIisRQ1aulwX5uRVf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/552f43f0ff9d71e29a4db72bbd54c3a0e0e29b31_2_690x327.png" alt="image" data-base62-sha1="c9zQJPufKtOIisRQ1aulwX5uRVf" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/552f43f0ff9d71e29a4db72bbd54c3a0e0e29b31_2_690x327.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/552f43f0ff9d71e29a4db72bbd54c3a0e0e29b31_2_1035x490.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/552f43f0ff9d71e29a4db72bbd54c3a0e0e29b31.png 2x" data-dominant-color="F5F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1318×625 52.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the notebook could not find slicer Kernel.</p>
<p>Here is my repos for reference.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/FaizanSiddiqui91/Slicer_binder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/FaizanSiddiqui91/Slicer_binder" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/168efe2d2799cdfec85773b18cf614870eccd855a4417499d9b49499d021a2e4/FaizanSiddiqui91/Slicer_binder" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/FaizanSiddiqui91/Slicer_binder" target="_blank" rel="noopener nofollow ugc">GitHub - FaizanSiddiqui91/Slicer_binder</a></h3>

  <p>Contribute to FaizanSiddiqui91/Slicer_binder development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks you.</p>

---

## Post #7 by @fpsiddiqui91 (2021-04-05 21:47 UTC)

<p>Hi developers, Sorry for asking this question again…<br>
Since it mentioned here, it seems a bit straightforward, however, I could not manage to deploy slicer jupyter with Voila…</p>
<p><a href="https://blog.jupyter.org/slicerjupyter-a-3d-slicer-kernel-for-interactive-publications-6f2ad829f635" class="onebox" target="_blank" rel="noopener nofollow ugc">https://blog.jupyter.org/slicerjupyter-a-3d-slicer-kernel-for-interactive-publications-6f2ad829f635</a></p>
<p>Please let me know if that’s even possible?</p>

---

## Post #8 by @pieper (2021-04-05 22:20 UTC)

<p>Let’s put this first on the list or tomorrow’s developer hangout.</p>

---

## Post #9 by @fpsiddiqui91 (2021-04-06 07:37 UTC)

<p>Thanks alot. I will discuss what I am up to and what options do I have. I seek your guidance and suggestions.</p>
<p>Thank you.</p>

---

## Post #10 by @tayran-mila (2023-01-24 14:15 UTC)

<p>Hi all!</p>
<p>I have the same problem here. I am trying to run Voila inside the 3D Slicer docker instance, but it returns a  “404: Not Found” error.</p>
<p>I installed Voila via <code>pip install voila</code>. When I tried to install it directly from the extension manager, it returned an error about Node.js and npm.</p>
<p>Were you able to run Voila inside the 3D Slicer docker instance?</p>

---
