---
topic_id: 46621
title: "Screen Capture And Screenshot Export Issues"
date: 2026-03-31
url: https://discourse.slicer.org/t/46621
---

# Screen Capture and Screenshot export issues

**Topic ID**: 46621
**Date**: 2026-03-31
**URL**: https://discourse.slicer.org/t/screen-capture-and-screenshot-export-issues/46621

---

## Post #1 by @Atticus (2026-03-31 14:30 UTC)

<p>Hi community!</p>
<p>I am trying to export images from 3D renders (transparent PNGs). Currently running 3DSlicer 5.10 on Win11.</p>
<ul>
<li>Issue 1: When using the Screen Capture module, if the default output file name is changed, the export task fails:</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c601fc2405ab4b295d336a424a96bd669a71006f.png" data-download-href="/uploads/short-url/sfEN5NlCpcdkoePWDtshGjrs1Jl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c601fc2405ab4b295d336a424a96bd669a71006f.png" alt="image" data-base62-sha1="sfEN5NlCpcdkoePWDtshGjrs1Jl" width="600" height="466"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">600×466 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/593b7b3c193d3edf4fda848192967faee95188a3.png" data-download-href="/uploads/short-url/cJnVR24CajQNi8kVTtRhnjxZilZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/593b7b3c193d3edf4fda848192967faee95188a3.png" alt="image" data-base62-sha1="cJnVR24CajQNi8kVTtRhnjxZilZ" width="600" height="466"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">600×466 19.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Issue 2: When using the Screenshot scaling option, to get a larger image, the result of the scaled image is broken and random. Happens for any factor beyond 1.0 X</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea1320c7d42b8407c702072a4c6f13b57609e51b.png" data-download-href="/uploads/short-url/xoII0feUr2uHhBBbwRXYwIIi9yb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea1320c7d42b8407c702072a4c6f13b57609e51b.png" alt="image" data-base62-sha1="xoII0feUr2uHhBBbwRXYwIIi9yb" width="655" height="367"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">655×367 64.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f51a83f437cc0b8adeaeb644657582e685d9382c.png" data-download-href="/uploads/short-url/yYhMWdGdyfsKJzrjAAZCgNPboxm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f51a83f437cc0b8adeaeb644657582e685d9382c.png" alt="image" data-base62-sha1="yYhMWdGdyfsKJzrjAAZCgNPboxm" width="661" height="374"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">661×374 62 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9eb35c73b85993d8f96c51bff06ac75ba1c5113.png" data-download-href="/uploads/short-url/xnlbwtBPPjfxn9HBFWJCj9Qhw55.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9eb35c73b85993d8f96c51bff06ac75ba1c5113.png" alt="image" data-base62-sha1="xnlbwtBPPjfxn9HBFWJCj9Qhw55" width="663" height="364"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">663×364 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tested both things in the previous 3DSlicer release and a different computer and both issues where there too.</p>
<p>Any help is appreciated!</p>

---

## Post #2 by @Deep_Learning (2026-03-31 15:27 UTC)

<p>Having similar issues that with Capture mode == single frame.   If I remove the integer “%05d” . It fails “Error:not all arguments converted during string formatting” v5.9.0</p>

---

## Post #3 by @mikebind (2026-03-31 17:29 UTC)

<p>I ran into the first issue a few weeks ago <a href="https://github.com/Slicer/Slicer/issues/9077" class="inline-onebox" rel="noopener nofollow ugc">ScreenCapture module does not save an output file in Single Frame mode. · Issue #9077 · Slicer/Slicer · GitHub</a></p>
<p>I submitted a PR with a possible solution here: <a href="https://github.com/Slicer/Slicer/pull/9078" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix ScreenCapture single frame saving by mikebind · Pull Request #9078 · Slicer/Slicer · GitHub</a></p>
<p>In the discussion there, <a class="mention" href="/u/lassoan">@lassoan</a> argued that the current behavior is not broken, but just not intuitive for the way I was thinking about it.  You might weigh in there with your thoughts on how the single frame screen capture should work.</p>
<p>I’m not sure what’s going on with the scaled screenshot.  It looks like a tiled image is just being assembled in the wrong order.  Do you have multiple monitors?  What operating system are you using?  This feature was definitely working in the past.</p>

---

## Post #4 by @muratmaga (2026-03-31 20:18 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="3" data-topic="46621">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I’m not sure what’s going on with the scaled screenshot. It looks like a tiled image is just being assembled in the wrong order. Do you have multiple monitors? What operating system are you using? This feature was definitely working in the past.</p>
</blockquote>
</aside>
<p>This has been broken for sometime. The solution is to switch to a 3D only layout in the application, then choose the full layout. It will achieve the same thing as 3D rendering.</p>
<p>The main issue though, this 2.0 scaling is simply interpolation of the image inside the 3D viewer. Plus it doesnt give the option to adjust the 3D view to fit your data axes easily. If you want both, you will better of using the HiResScreenCapture in SlicerMorph, which does off-screen rendering. The way is to use it is to undock the 3D view, adjust all the visual properties (such as the ratio of window), and then capture it at the specified magnification. There is a short tutorial here.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/HiResScreenCapture">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/HiResScreenCapture" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/HiResScreenCapture" target="_blank" rel="noopener nofollow ugc">Tutorials/HiResScreenCapture at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
