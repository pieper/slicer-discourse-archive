---
topic_id: 4401
title: "Scalar Subtraction"
date: 2018-10-15
url: https://discourse.slicer.org/t/4401
---

# Scalar subtraction

**Topic ID**: 4401
**Date**: 2018-10-15
**URL**: https://discourse.slicer.org/t/scalar-subtraction/4401

---

## Post #1 by @lemonade (2018-10-15 13:35 UTC)

<p>Hello. I am subtracting two images to track changes in contrast between them. I am interested in both the positive and negative change.</p>
<p>However I can’t seem to get any values below 0 after subtraction. Is there something I can do to get around this issue?</p>

---

## Post #2 by @ihnorton (2018-10-15 14:31 UTC)

<p>If you are using the <code>Subtract Scalar Volumes</code> module, then the issue is that the module sets the output type to match the type of the first input volume. If your first input has a unsigned type, then the output type will also be unsigned, and all negative values will be clamped to 0. The simplest fix is to use the <code>Cast Scalar Volumes</code> module to change the input type to something with sufficient range (<code>signed int</code> or <code>float</code> are typically a good choice, but you need to know your data).</p>
<p>Alternatively you could write a script in Python to do this for you, there are several relevant examples in the repository about doing math on image voxels:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a></p>

---

## Post #3 by @lemonade (2018-10-15 19:39 UTC)

<p>Thank you! I ran the Cast Scalar Volumes to change input to int, after that I got the results that I had expected :).</p>

---
