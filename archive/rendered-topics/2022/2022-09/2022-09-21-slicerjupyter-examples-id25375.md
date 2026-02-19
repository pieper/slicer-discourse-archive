---
topic_id: 25375
title: "Slicerjupyter Examples"
date: 2022-09-21
url: https://discourse.slicer.org/t/25375
---

# SlicerJupyter examples

**Topic ID**: 25375
**Date**: 2022-09-21
**URL**: https://discourse.slicer.org/t/slicerjupyter-examples/25375

---

## Post #1 by @PaoloZaffino (2022-09-21 13:56 UTC)

<p>Hi all,<br>
I installed all the required stuff to get SlicerJupyter working, but if I run this code nothing happens in Jupyter:</p>
<pre><code class="lang-python">import SampleData
SampleData.SampleDataLogic().DownloadCTACardio ()
display()
</code></pre>
<p>Slicer downloads the dataset and show it in Slicer (so the bridge works), but not in Jupyter.</p>
<p>Any idea?</p>
<p>Just to familiarize with SlicerJupyter, is there a repository where I can find educational notebooks?</p>
<p>Thanks a lot,<br>
Paolo</p>

---

## Post #2 by @lassoan (2022-09-21 15:33 UTC)

<p>There are lots of display functions for displaying or interacting with data loaded into Slicer in a notebook. I would recommend to go through these examples:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/SlicerNotebooks/">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/SlicerNotebooks/" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/ace2b97f60a5cf8514005dbf8aa706f590734ef0ee42f8baf79b3a822831b635/Slicer/SlicerNotebooks" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/SlicerNotebooks/" target="_blank" rel="noopener">GitHub - Slicer/SlicerNotebooks: Examples that illustrate how to use 3D...</a></h3>

  <p>Examples that illustrate how to use 3D Slicer via Jupyter notebooks in Python - GitHub - Slicer/SlicerNotebooks: Examples that illustrate how to use 3D Slicer via Jupyter notebooks in Python</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @PaoloZaffino (2022-09-22 08:53 UTC)

<p>Thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a> … that’s exactly what I looked for!</p>
<p>Best,<br>
Paolo</p>

---
