# Induce deformation

**Topic ID**: 17446
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/induce-deformation/17446

---

## Post #1 by @Jakub_Mitura (2021-05-04 16:00 UTC)

<p>Hello I would like to induce some deformation and changes in an PET/CT  image preferably programmatically for example elastically deform aorta , add some gas bubbles, change size of the inflammatory infiltration … I want to use it for some  data augmentation.<br>
How best to approach this (for example what library to use, better in C+ or python - as far as i know there is/was limitad capability to load external libraries in python, some extension … ?)</p>
<p>Thank You for help !</p>

---

## Post #2 by @pieper (2021-05-04 16:53 UTC)

<p>Some of that can already be done with TorchIO, and maybe you can expand it to add some extra features.</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/fepegar/SlicerTorchIO" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://opengraph.githubassets.com/473821573f347f7712d338ef8aa0a1c0ef46857f323e4282c05af2c79de3364c/fepegar/SlicerTorchIO" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/fepegar/SlicerTorchIO" target="_blank" rel="noopener">fepegar/SlicerTorchIO</a></h3>


  <p><span class="label1">3D Slicer module for TorchIO. Contribute to fepegar/SlicerTorchIO development by creating an account on GitHub.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Jakub_Mitura (2021-05-04 16:59 UTC)

<p>Thank you! Yes I would like to contribute  in case you would have some clues where to start, you can let me know <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---

## Post #4 by @pieper (2021-05-04 17:01 UTC)

<p>I’m hoping <a class="mention" href="/u/fernando">@Fernando</a> can jump in with more details.</p>

---

## Post #5 by @Fernando (2021-05-04 17:08 UTC)

<p>Thanks, Steve.</p>
<p><a class="mention" href="/u/jakub_mitura">@Jakub_Mitura</a>, I suggest you use Python for data augmentation. As <a class="mention" href="/u/pieper">@pieper</a> said, TorchIO can be used for e.g. random elastic deformations. The transforms you’re after are quite level and problem-specific, so they would require some work. You can start by checking the <a href="https://github.com/fepegar/torchio/tree/master/notebooks" rel="noopener nofollow ugc">tutorials</a> that demonstrate how to use some of the transforms during training.</p>
<p>You can use Slicer to visualize your results or try the transforms parameters. If you have more questions that unrelated to Slicer, you can <a href="https://github.com/fepegar/torchio/discussions" rel="noopener nofollow ugc">open a discussion in the TorchIO repository</a>.</p>

---

## Post #6 by @Jakub_Mitura (2021-05-04 17:11 UTC)

<p>Ok thanks ! So i will dive into it slowly and when I will achieve sth i will share the results with you, in case i will get stuck i will post as you suggested, thanks!</p>

---
