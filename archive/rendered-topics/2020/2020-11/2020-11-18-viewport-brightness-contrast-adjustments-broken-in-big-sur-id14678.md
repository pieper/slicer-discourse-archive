# Viewport brightness/contrast adjustments broken in Big Sur?

**Topic ID**: 14678
**Date**: 2020-11-18
**URL**: https://discourse.slicer.org/t/viewport-brightness-contrast-adjustments-broken-in-big-sur/14678

---

## Post #1 by @pll_llq (2020-11-18 20:36 UTC)

<p>Hi there,</p>
<p>After the Big Sur update on my Mac I noticed that clicking and dragging over viewport windows with slices does not change the image brightness/contrast as it used to.</p>
<p>Is this a bug or did I miss a migration of this feature to the Volumes tab?</p>

---

## Post #2 by @muratmaga (2020-11-18 20:40 UTC)

<p>Did you also upgrade your Slicer version too? For a while now you need to use the window/level mode mouse mode (see below).</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#mouse-modes" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#mouse-modes" target="_blank" rel="noopener nofollow ugc">User Interface — 3D Slicer  documentation</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @pll_llq (2020-11-18 21:06 UTC)

<p>Hi, thanks for the link.<br>
My Slicer version is 4.11.20200930<br>
With the mouse mode selected<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1b435c6aa3503417e8d316e69798c3c281f7033.jpeg" data-download-href="/uploads/short-url/yudasjCPIBjHrnxepe8NSO9mTnB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1b435c6aa3503417e8d316e69798c3c281f7033_2_560x499.jpeg" alt="image" data-base62-sha1="yudasjCPIBjHrnxepe8NSO9mTnB" width="560" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1b435c6aa3503417e8d316e69798c3c281f7033_2_560x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1b435c6aa3503417e8d316e69798c3c281f7033_2_840x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1b435c6aa3503417e8d316e69798c3c281f7033.jpeg 2x" data-dominant-color="4D4B4A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1024×914 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Ctrl+click’n’drag zooms the image and Cmd+click’n’drag and simple click’n’drag do nothing</p>

---

## Post #4 by @lassoan (2020-11-18 21:10 UTC)

<p>You need to click “Adjust window/level” button on the toolbar - see <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#adjusting-image-window-level">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#adjusting-image-window-level</a></p>

---

## Post #5 by @pll_llq (2020-11-18 21:12 UTC)

<p>Thanks! I definitely missed that.<br>
It used to be on by default</p>

---
