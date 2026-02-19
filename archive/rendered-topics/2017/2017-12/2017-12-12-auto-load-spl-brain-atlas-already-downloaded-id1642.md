---
topic_id: 1642
title: "Auto Load Spl Brain Atlas Already Downloaded"
date: 2017-12-12
url: https://discourse.slicer.org/t/1642
---

# Auto-load SPL brain atlas? (already downloaded)

**Topic ID**: 1642
**Date**: 2017-12-12
**URL**: https://discourse.slicer.org/t/auto-load-spl-brain-atlas-already-downloaded/1642

---

## Post #1 by @aNonprofessional (2017-12-12 05:18 UTC)

<p>Hello, I’ve been lurking here for a number of years, not really using Slicer much, my interest is not professional but is rather a long-term/sometimes &amp; only marginally successful desire to learn brain anatomy.  I recently had to reload Slicer (4.8.0) after a computer glitch, and was glad to also find &amp; download a new version of SPL Brain Atlas, January 2017.<br>
<a href="http://www.spl.harvard.edu/publications/item/view/2037" class="onebox" target="_blank" rel="nofollow noopener">http://www.spl.harvard.edu/publications/item/view/2037</a></p>
<p>I wonder if there is some way to auto-load the already downloaded SPL brain atlas when Slicer executes?</p>
<p>(I have an older version of Slicer that still does auto-load it, but I can’t see how it was accomplished.)</p>
<p>Thanks,<br>
Dan</p>

---

## Post #2 by @lassoan (2017-12-12 14:10 UTC)

<p>The easiest is to double-click on the atlas .mrb file - it should open the file in Slicer.</p>
<p>Alternatively, you can add a line to your application startup script (you can find its location in menu: Edit / Application settings / General / Application startup script) that loads the scene using <code>slicer.util.loadScene('some-scene-to-load.mrb')</code>.</p>

---

## Post #3 by @aNonprofessional (2017-12-12 22:24 UTC)

<p>Oh, too simple! Thanks!  Perhaps all my questions to come may be that simple.</p>
<p>Dan</p>

---
