---
topic_id: 961
title: "Qt5 Branch Macos Transparency Issue"
date: 2017-08-28
url: https://discourse.slicer.org/t/961
---

# Qt5 branch - MacOS transparency issue

**Topic ID**: 961
**Date**: 2017-08-28
**URL**: https://discourse.slicer.org/t/qt5-branch-macos-transparency-issue/961

---

## Post #1 by @hherhold (2017-08-28 17:43 UTC)

<p>Built MacOS 10.12.6 off fresh support-qt5-2017-08-11-r26241 branch. Built fine, runs fine (overall).</p>
<p>Graphics card is AMD Radeon R9 M370 on MacBook Pro Retina 15" on external thunderbolt display.</p>
<p>When displaying 3D model (from “Create surface”), there are transparency artifacts when displaying surfaces with 0.5 opacity. Should this be working properly with OpenGL 2 and VTK 8?</p>
<p>I can provide a video of the issue if needed.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2017-08-28 18:43 UTC)

<p>To get correct transparency, you need to enable depth peeling in menu: Edit / Application settings / Views / 3D viewer defaults / Use depth peeling - then restart Slicer.</p>

---

## Post #3 by @jcfr (2017-08-28 19:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="961">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Edit / Application settings / Views / 3D viewer defaults / Use depth peeling</p>
</blockquote>
</aside>
<p>While it can impact performances in some scenario, I wonder if we should enable <code>depth peeling</code> by default …</p>

---

## Post #4 by @lassoan (2017-08-28 20:27 UTC)

<p>Yes, we should enable it by default when we switch to the OpenGL2 backend.</p>
<p>The performance decrease with the OpenGL backend was significant and at some point the feature stopped working (at least on Windows), so it made no sense to enable it by default for the old backend.</p>

---

## Post #5 by @hherhold (2017-08-29 11:34 UTC)

<p>Issue still occurs with depth peeling activated. (Same as recent nightly build, incidentally.)</p>
<p>Is the Qt5 branch set to use OpenGL 2 by default? Slicer_VTK_RENDERING_BACKEND is set to OpenGL2, I’d been assuming that was all I needed to do. Qt version is 5.9.1.</p>
<p>Let me know if you want a video of the issue.</p>

---

## Post #6 by @lassoan (2017-08-30 03:18 UTC)

<p>I’ve just tried and for me, enabling depth peeling fixes transparent polygon rendering (Windows, OpenGL2 backend, Qt 5.6). Note that you have to rebuild VTK from scratch if you switch to another rendering backend - a forced rebuild may not be enough.</p>

---

## Post #7 by @jcfr (2017-08-31 21:17 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="5" data-topic="961">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>Is the Qt5 branch set to use OpenGL 2 by default?</p>
</blockquote>
</aside>
<p>The version of VTK will default to 8 if <code>Qt5_DIR</code> is used to configure Slicer.</p>
<p>That said, if you set <code>Qt5_DIR</code> in an already configured build tree … it will not force the version of VTK.</p>
<p><a href="https://github.com/Slicer/Slicer/blob/ee5c8703642cf8f42e9594bc780cb0801623b39d/CMakeLists.txt#L310-L319" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/ee5c8703642cf8f42e9594bc780cb0801623b39d/CMakeLists.txt#L310-L319</a></p>
<p><a href="https://github.com/Slicer/Slicer/blob/ee5c8703642cf8f42e9594bc780cb0801623b39d/CMakeLists.txt#L546-L553" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/ee5c8703642cf8f42e9594bc780cb0801623b39d/CMakeLists.txt#L546-L553</a></p>

---
