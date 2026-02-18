# MarkupsToModel : build fails with VTK9

**Topic ID**: 13839
**Date**: 2020-10-03
**URL**: https://discourse.slicer.org/t/markupstomodel-build-fails-with-vtk9/13839

---

## Post #1 by @chir.set (2020-10-03 16:30 UTC)

<p>Slicer builds nicely with VTK9 on Arch Linux with gcc 10.2.</p>
<p>MarkupsToModel fails to build on VTK_OVERRIDE and VTK_DELETE_FUNCTION. If all occurrences of these macros are removed, the build process completes. Can’t know if it’s the right fix.</p>
<p>Thank you for looking into it.</p>

---

## Post #2 by @lassoan (2020-10-04 15:21 UTC)

<p>Could you send a pull request that replaces these macros with their meaning (<code>override</code> and <code>= delete</code>)? Thank you!</p>

---

## Post #3 by @chir.set (2020-10-04 17:05 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>with their meaning</p>
</blockquote>
</aside>
<p>I removed these macros in 3 header files. It was not a replacement by some other non-empty values. In particular, there is no VTK version testing. I can send the pull request as such, and just want to confirm that it’s what you expect.</p>

---

## Post #4 by @chir.set (2020-10-04 17:22 UTC)

<p>Just understood better what you mean.</p>
<p>Replace VTK_OVERRIDE by override, and VTK_DELETE_FUNCTION by =delete.</p>
<p>I’ll send the PR.</p>

---
