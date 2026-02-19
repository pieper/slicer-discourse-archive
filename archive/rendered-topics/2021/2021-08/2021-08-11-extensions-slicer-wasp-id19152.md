---
topic_id: 19152
title: "Extensions Slicer Wasp"
date: 2021-08-11
url: https://discourse.slicer.org/t/19152
---

# Extensions--Slicer-Wasp

**Topic ID**: 19152
**Date**: 2021-08-11
**URL**: https://discourse.slicer.org/t/extensions-slicer-wasp/19152

---

## Post #1 by @skyhsu (2021-08-11 09:09 UTC)

<p>Hi ,<br>
I am search for some tool that can do simple segmentation job,<br>
I found the extension Slicer-Wasp and install it,<br>
but it can’t  run normally,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6d3c9c306464742ac9ecc3b2ca916648da40360.png" alt="wasp" data-base62-sha1="wVZzttmYgB7pC8PbDxFNrxss9WM" width="574" height="386"><br>
Are there any steps to fix?</p>
<p>Thanks<br>
Sky</p>

---

## Post #2 by @pieper (2021-08-11 12:32 UTC)

<p>That extension is for a much older version of Slicer and probably it hasn’t been updated.  You could look in the error log and report an issue on the project’s issue tracker.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Tomnl/Slicer-Wasp">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Tomnl/Slicer-Wasp" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/159b2a5e012f13c94f38ab398c47ddc89b8a4b482975cd342ecd12934595c11e/Tomnl/Slicer-Wasp" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Tomnl/Slicer-Wasp" target="_blank" rel="noopener">GitHub - Tomnl/Slicer-Wasp: Watershed Annotation and Segmentation Plugin for...</a></h3>

  <p>Watershed Annotation and Segmentation Plugin for 3D Slicer - GitHub - Tomnl/Slicer-Wasp: Watershed Annotation and Segmentation Plugin for 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @skyhsu (2021-08-12 00:39 UTC)

<p>HI pieper,<br>
OK, I will report this issue on the project’s issue tracker.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2021-08-12 04:29 UTC)

<p>These watershed segmentations look cool in demos, but I’ve found them useless in practice, especially in 3D. See some more details <a href="https://discourse.slicer.org/t/watershed-paint-mode/7655/2">here</a>.</p>
<p>So, I would not bother with trying to revive Slicer-WASP, but I would recommend to use methods that gives you better control of the segmentation process, such as “Grow from seeds” (you can specify very rough initial seeds, and then add more inputs until the segmentation becomes acceptable).</p>
<p>If you want to get a feeling of limitation of watershed methods then you try “Watershed” effect (provided by SegmentEditorExtraEffects), which generates same kind of partitioning into small cells as Slicer-WASP, but does not show you the small cell boundaries, just the result that you get after recoloring based on the seed segments. You can see how the “object scale” value influences the sizes of cells (and see that most often there is no single value that works well over the entire image); and also experience how the watershed cannot fully take into account your inputs (a seed region that you paint with a certain color may end up assigned to another color in the segmentation result).</p>

---
