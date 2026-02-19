---
topic_id: 28531
title: "Can We Rotate The Slice In Single Model Like In Mitk"
date: 2023-03-23
url: https://discourse.slicer.org/t/28531
---

# Can we rotate the slice in single model like in MITK

**Topic ID**: 28531
**Date**: 2023-03-23
**URL**: https://discourse.slicer.org/t/can-we-rotate-the-slice-in-single-model-like-in-mitk/28531

---

## Post #1 by @slicer365 (2023-03-23 00:08 UTC)

<p>Can we rotate the slice in single model like in MITK。</p>
<p>Anyway including python scripts, will be helpful !</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/babeb010cf9b312c0e94efe9d8d817e3e41562ec.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/babeb010cf9b312c0e94efe9d8d817e3e41562ec.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/babeb010cf9b312c0e94efe9d8d817e3e41562ec.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @jamesobutler (2023-03-23 01:41 UTC)

<p>There is not an interaction like that with interactive slice intersections, but you can try the “Reformat” widget which has controls to change the rotation of selected slice views from the module panel.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7fdaf4cd7989295d0d9b4d6612cc6c2d8e11cde6.jpeg" data-download-href="/uploads/short-url/if3KwqsT07WqAsJFUcqMiOInk9w.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fdaf4cd7989295d0d9b4d6612cc6c2d8e11cde6_2_690x370.jpeg" alt="image" data-base62-sha1="if3KwqsT07WqAsJFUcqMiOInk9w" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fdaf4cd7989295d0d9b4d6612cc6c2d8e11cde6_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fdaf4cd7989295d0d9b4d6612cc6c2d8e11cde6_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fdaf4cd7989295d0d9b4d6612cc6c2d8e11cde6_2_1380x740.jpeg 2x" data-dominant-color="717177"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>however,</p><aside class="quote quote-modified" data-post="2" data-topic="19377">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/orthogonal-reformat/19377/2">Orthogonal reformat</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    The reformat widget is not very powerful and I don’t think it supports suchorthogonality constraint. 
Instead, you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views" rel="noopener nofollow ugc">rotate slice views</a> by displaying slice intersections and then: 

use Ctrl + Alt + Left-click-and-drag using your mouse, or
pinch-and-rotate on touchscreen (on Windows) or on the touchpad (on macOS), or
or define the desired orientation using a transform and then use “Volume reslice driver” module in SlicerIGT extension to show orthogonal slices

There are specialized modules for…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2023-03-23 01:51 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="1" data-topic="28531">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>Can we rotate the slice in single model like in MITK。</p>
</blockquote>
</aside>
<p>Slice view intersection <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views">rotation using Ctrl+Alt+Left-click-and-drag</a> was implemented a few years ago. (0:00-0:09 in the video)</p>
<p>Interactive slice intersection feature was added more recently, maybe half year ago. There are still some glitches, so we haven’t advertised the feature much. (0:09-0:18 in the video)</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31d13b5461c795c96cd9849e312d290f83824ab2.mp4">
  </div><p></p>
<p>Do you miss the ability to rotate a single slice view?</p>
<p>In that case you can temporarily change the “view group” of a slice view in “View Controllers” module:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f3fd8179808c9a6ff4525e3a0742f5624c20abb.mp4">
  </div><p></p>
<p>What is your clinical use case?</p>

---

## Post #4 by @RafaelPalomar (2023-03-23 12:00 UTC)

<p>The development reported in <a href="https://discourse.slicer.org/t/interactive-slice-intersections/21677" class="inline-onebox">Interactive slice intersections</a> seems to be close to what you want, including rotations. I hope it helps.</p>

---
