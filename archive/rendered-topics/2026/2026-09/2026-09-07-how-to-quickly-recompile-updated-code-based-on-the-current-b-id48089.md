---
topic_id: 48089
title: "How to quickly recompile updated code based on the current build version"
date: 2026-09-07
url: https://discourse.slicer.org/t/48089
last_bumped: 2026-09-07T14:23:19.906Z
---

# How to quickly recompile updated code based on the current build version

**Topic ID**: 48089
**Date**: 2026-09-07
**URL**: https://discourse.slicer.org/t/how-to-quickly-recompile-updated-code-based-on-the-current-build-version/48089

---

## Post #1 by @zhuofalin (2026-09-07 09:13 UTC)

<p>Hello, I am very happy to be back in the Slicer community.<img src="https://emoji.discourse-cdn.com/twitter/grinning_face.png?v=15" title=":grinning_face:" class="emoji" alt=":grinning_face:" loading="lazy" width="20" height="20"></p>
<hr>
<p>I typically use an older version of the slicer for development, but thanks to the efforts of the developers, new features are constantly being added—and I find myself using some or all of these updates.</p>
<p>Now, what I want to ask is:</p>
<p><strong>How to quickly recompile updated code based on the current build version?</strong></p>
<p>Because I don’t want to run commands like <code>cmake build</code> and compile everything step-by-step to get a new version every time I perform a <code>git pull</code>.</p>

---

## Post #2 by @mau_igna_06 (2026-09-07 14:23 UTC)

<p>Enter on <code>SlicerRelease/Slicer-build</code> folder using <code>cd</code> and execute the build command there, that way you’ll only rebuild Slicer code and not the dependencies</p>

---
