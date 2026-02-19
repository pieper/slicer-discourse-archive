---
topic_id: 11848
title: "Rendering Bug With Non Simple Polygons"
date: 2020-06-03
url: https://discourse.slicer.org/t/11848
---

# Rendering bug with non-simple polygons

**Topic ID**: 11848
**Date**: 2020-06-03
**URL**: https://discourse.slicer.org/t/rendering-bug-with-non-simple-polygons/11848

---

## Post #1 by @gcsharp (2020-06-03 16:34 UTC)

<p>I’ve noticed this before, but never had time to investigate.  Anyway when an RTSTRUCT has non-simple (self-intersecting) polygons, it does not render correctly in slice view.  Should I file a bug report?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd3e7daa8d6322ddd5ae9e5e34758d2469c33c0d.png" alt="2020-06-03_12-27" data-base62-sha1="vzdpeMby5V1GNPfITCNgVVM5zzf" width="442" height="365"></p>

---

## Post #2 by @lassoan (2020-06-03 17:44 UTC)

<p>We’ll push a fix soon - <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is working on it (see <a href="https://github.com/Slicer/Slicer/issues/4959">https://github.com/Slicer/Slicer/issues/4959</a>).</p>
<p>As a workaround, go to Segmentations module’s Representations section and click “Create” in “binary labelmap”. This will allow using binary labelmap representation for slice intersection display, which works robustly regardless of the complexity of the input.</p>

---

## Post #3 by @gcsharp (2020-06-03 18:16 UTC)

<p>Cool.  Thanks <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> !!</p>

---
