# Build arm 32 OpenSSL

**Topic ID**: 31204
**Date**: 2023-08-17
**URL**: https://discourse.slicer.org/t/build-arm-32-openssl/31204

---

## Post #1 by @Kening_Zhang (2023-08-17 21:27 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed9c6c83c890cbcc7bad7bd1cb735ac4fb621fc1.png" data-download-href="/uploads/short-url/xU0iq9v8jJVML4TQi97RQGeu4uZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed9c6c83c890cbcc7bad7bd1cb735ac4fb621fc1_2_690x329.png" alt="image" data-base62-sha1="xU0iq9v8jJVML4TQi97RQGeu4uZ" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed9c6c83c890cbcc7bad7bd1cb735ac4fb621fc1_2_690x329.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed9c6c83c890cbcc7bad7bd1cb735ac4fb621fc1_2_1035x493.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed9c6c83c890cbcc7bad7bd1cb735ac4fb621fc1_2_1380x658.png 2x" data-dominant-color="F3F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1836×876 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I try this step, error happens:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbc3f6ec37b582ea4fc59bd87fea5314b0c070db.png" data-download-href="/uploads/short-url/qN38CzX1Q0auoSLYjjKX9p6yaMz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbc3f6ec37b582ea4fc59bd87fea5314b0c070db_2_690x310.png" alt="image" data-base62-sha1="qN38CzX1Q0auoSLYjjKX9p6yaMz" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbc3f6ec37b582ea4fc59bd87fea5314b0c070db_2_690x310.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbc3f6ec37b582ea4fc59bd87fea5314b0c070db_2_1035x465.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbc3f6ec37b582ea4fc59bd87fea5314b0c070db.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1124×506 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The error message indicates that the linker could not find some symbol (function, variable, etc.) when trying to build. But I dont know how to solve.<br>
Best wishes,<br>
Joshua</p>

---

## Post #2 by @pieper (2023-08-17 22:16 UTC)

<p>Thanks for reporting.  Something must have changed either with the mac build tools or something in OpenSSL source.   I just re-ran that those commands on the same M2 mac where they worked before and now I get the same link error that you reported.</p>

---

## Post #3 by @Kening_Zhang (2023-08-18 05:28 UTC)

<p>Thanks so much. So I may not build Slicer on my mac now right?</p>

---

## Post #4 by @pieper (2023-08-18 12:43 UTC)

<aside class="quote no-group" data-username="Kening_Zhang" data-post="3" data-topic="31204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kening_zhang/48/65641_2.png" class="avatar"> Kening_Zhang:</div>
<blockquote>
<p>So I may not build Slicer on my mac now right?</p>
</blockquote>
</aside>
<p>Not without some extra work.  You could investigate why this link error occurs by looking at any changes in OpenSSL since the time late last year when it worked vs the current version.  Maybe checking out an older version would build correctly and if so maybe a patch could be developed to make a newer version work.  It’s also possible that other people have noticed this issue and a fix is in the works (to know you would need to check the OpenSSL issue tracker).  Since this failure is on a straightforward build of the library on a fairly popular OS I suspect it will eventually be fixed, but maybe you can help speed up the process with some research.</p>

---

## Post #5 by @jcfr (2023-08-18 13:37 UTC)

<p><a class="mention" href="/u/kening_zhang">@Kening_Zhang</a>  Thanks for following up with additional details <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=12" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"></p>
<p>To help organize the effort, I just updated our “meta” issue adding links to issue reports and relevant discourse posts:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/issues/6811" class="inline-onebox">Support for building/testing/packaging Slicer on Apple arm64 · Issue #6811 · Slicer/Slicer · GitHub</a></li>
</ul>
<p><a class="mention" href="/u/kening_zhang">@Kening_Zhang</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Could you add a summary of your latest finding regarding building OpenSSL on arm to the following issue report:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/issues/5944" class="inline-onebox">Unable to build from source on Apple silicon · Issue #5944 · Slicer/Slicer · GitHub</a></li>
</ul>

---

## Post #6 by @Kening_Zhang (2023-08-18 17:47 UTC)

<p>OK, I am working on it.</p>

---
