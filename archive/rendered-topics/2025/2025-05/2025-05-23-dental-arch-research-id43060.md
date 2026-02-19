---
topic_id: 43060
title: "Dental Arch Research"
date: 2025-05-23
url: https://discourse.slicer.org/t/43060
---

# Dental Arch Research

**Topic ID**: 43060
**Date**: 2025-05-23
**URL**: https://discourse.slicer.org/t/dental-arch-research/43060

---

## Post #1 by @cekrebs (2025-05-23 11:08 UTC)

<p>Hi everyone! I am currently trying to compare two scans of lower teeth (one scan of a plastic typodont, one scan of a 3D printed version of the typodont). The STL files of the models after being scanned are almost identical with minor differences from the 3D printing process.</p>
<p>I was able to upload the two STL files. Now I am hoping to align/superimpose the two dental arches, then quantify the differences between the two in mm. For example, where the 3D printer made the teeth too big, too small, etc.</p>
<p>Let me know if anyone would know how to do this.</p>

---

## Post #2 by @cekrebs (2025-05-23 20:40 UTC)

<p>Ok I was able to overlay the two STL file of the two dental arches. I would love help with how to compute the differences between the two now! Example - places between the two arches that are different and differences in mm.</p>

---

## Post #3 by @chir.set (2025-05-23 21:05 UTC)

<aside class="quote no-group" data-username="cekrebs" data-post="2" data-topic="43060">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/73ab20/48.png" class="avatar"> cekrebs:</div>
<blockquote>
<p>I was able to overlay</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="cekrebs" data-post="2" data-topic="43060">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/73ab20/48.png" class="avatar"> cekrebs:</div>
<blockquote>
<p>compute the differences between the two</p>
</blockquote>
</aside>
<p>Try the <code>Combine models</code> module in the <code>Sandbox</code> extension.</p>

---
