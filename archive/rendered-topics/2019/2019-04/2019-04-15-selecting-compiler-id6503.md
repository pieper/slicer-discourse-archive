---
topic_id: 6503
title: "Selecting Compiler"
date: 2019-04-15
url: https://discourse.slicer.org/t/6503
---

# Selecting Compiler

**Topic ID**: 6503
**Date**: 2019-04-15
**URL**: https://discourse.slicer.org/t/selecting-compiler/6503

---

## Post #1 by @marcmclean (2019-04-15 14:01 UTC)

<p>I’m attempting to compile Slicer from source.<br>
The Slicer documentation states to not configure until after selecting your compiler.<br>
In CMake GUI, the only way I see to specify the compiler is to click the Configure button first<br>
and enter the compiler information. Is this the correct method?</p>
<p>Thank you,<br>
Marc McLean</p>

---

## Post #2 by @lassoan (2019-04-15 15:13 UTC)

<p>You can add CMake variables before you configure by clicking <code>Add Entry</code>. I’ve updated the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Configure#Windows" rel="nofollow noopener">build instructions</a> to make this more clear.</p>

---
