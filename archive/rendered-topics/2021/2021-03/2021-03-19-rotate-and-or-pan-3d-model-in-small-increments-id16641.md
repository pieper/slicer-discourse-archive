# Rotate and/or pan 3D model in small increments

**Topic ID**: 16641
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/rotate-and-or-pan-3d-model-in-small-increments/16641

---

## Post #1 by @quim (2021-03-19 15:25 UTC)

<p>Operating system: Linux Mint 19.3<br>
Slicer version: 4.11<br>
Expected behavior:<br>
I am trying to make a movie for publication of a 3D model while I rotate, pan and zoom it, to better display  details. To achieve this, I am using the modules sequences and screen capture. However, if I rotate/pan/zoom the model using the mouse, the final result is shaky and uneven. I would like to use the keyboard arrows to rotate and the shift-arrow to pan to have better control. However, in this case the rotation angles and pan steps are too big.<br>
Is there a way to reduce the rotation angles and pan displacements of the camera when using the arrows or shift-arrow?</p>

---

## Post #2 by @pieper (2021-03-19 18:08 UTC)

<p>If you are willing to dig in the code and maybe recompile Slicer I’m sure the increments can be changed.  I don’t recall the exact classes involved but I’m sure it can be found.  Perhaps it’s even configurable in python.</p>
<p>Or you might want the Animator from SlicerMorph.  It lets you make movies like this (it’s build on top of ScreenCapture):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="oGtvTOhIFtA" data-video-title="SlicerAnimator" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=oGtvTOhIFtA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/oGtvTOhIFtA/maxresdefault.jpg" title="SlicerAnimator" width="" height="">
  </a>
</div>

<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/15dd46139e815a85f145dcd6c510bd40ec831e51170f36f82081e1fe0894819d/SlicerMorph/SlicerMorph" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerMorph/SlicerMorph" target="_blank" rel="noopener">GitHub - SlicerMorph/SlicerMorph: Extensions to conduct 3D morphometrics in...</a></h3>

  <p>Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @quim (2021-03-19 19:44 UTC)

<p>Thank you for your suggestions. I looked into Animator, but it does not appear to support panning and it does not work with models, only with volumes. It would be great to be able to change the increments using Python, but I do not know how.</p>

---

## Post #4 by @pieper (2021-03-19 21:18 UTC)

<p>I’m not sure either, you’d need to look through the code.</p>
<p>Note that the animator has a plugin architecture, so you can define your on action classes in python, but that’s also a bit of work.</p>

---
