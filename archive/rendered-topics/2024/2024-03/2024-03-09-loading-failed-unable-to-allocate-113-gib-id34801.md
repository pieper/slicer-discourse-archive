---
topic_id: 34801
title: "Loading Failed Unable To Allocate 113 Gib"
date: 2024-03-09
url: https://discourse.slicer.org/t/34801
---

# loading failed: Unable to allocate 113 GiB

**Topic ID**: 34801
**Date**: 2024-03-09
**URL**: https://discourse.slicer.org/t/loading-failed-unable-to-allocate-113-gib/34801

---

## Post #1 by @aochaoyu (2024-03-09 17:19 UTC)

<p>I use the Image Stacks module, and a Slicer error window pops up. The content is “loading failed: Unable to allocate 113 GiB for an array with shape (206,19200,30720) and data type uint8”. I would like to ask the seniors if there is a suitable solution. I’m trying to find the settings for importing images, hoping to use an ssd to process the images instead. Thanks!</p>

---

## Post #2 by @pieper (2024-03-09 17:39 UTC)

<p>That means you don’t have enough memory.  See the docs for info on reducing the size:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener">//github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you really need to operate at the full volume you’ll need to find a bigger computer (5x or more memory than the size of the volume).  One option is to rent a big memory cloud VM.</p>

---

## Post #3 by @muratmaga (2024-03-09 22:41 UTC)

<p>Based on the numbers you reported, you have more than 30,000 slices! The other dimensions are also very awkward 206x19200.</p>
<p>What is this dataset of? Given the number of slices, I would suggest using the skip slice option ImageStacks, and perhaps use every other or every third slice. But again, dimensions are very unusual…</p>

---
