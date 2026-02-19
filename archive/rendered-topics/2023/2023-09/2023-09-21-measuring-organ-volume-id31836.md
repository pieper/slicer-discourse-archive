---
topic_id: 31836
title: "Measuring Organ Volume"
date: 2023-09-21
url: https://discourse.slicer.org/t/31836
---

# Measuring Organ Volume

**Topic ID**: 31836
**Date**: 2023-09-21
**URL**: https://discourse.slicer.org/t/measuring-organ-volume/31836

---

## Post #1 by @Hannah_Osland (2023-09-21 20:21 UTC)

<p>I have a bunch of .tif files of the entire body of an organism. I want to measure the volume of an organ in the animal. What steps should I take?</p>

---

## Post #2 by @muratmaga (2023-09-21 21:13 UTC)

<ol>
<li>You need to import your tiff files into slicer. You can use the <code>ImageStacks</code> in SlicerMorph to do that</li>
<li>You can then use the <code>Segment Editor</code> to segment the individual organs</li>
<li>Then you can use the <code>Segment Statistics</code> module to calculate the volumes of individual organs.</li>
</ol>
<p>If you are new to Slicer, you may want to review SlicerMorph tutorials, which explains these steps:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerMorph/Tutorials">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/dc9aa94a34f45b2e623efc7f274ceb185bab2b67f303b313507b44d892b90079/SlicerMorph/Tutorials" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerMorph/Tutorials" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a></h3>

  <p>SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
