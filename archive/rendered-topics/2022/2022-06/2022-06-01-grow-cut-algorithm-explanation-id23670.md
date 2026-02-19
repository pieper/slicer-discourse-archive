---
topic_id: 23670
title: "Grow Cut Algorithm Explanation"
date: 2022-06-01
url: https://discourse.slicer.org/t/23670
---

# Grow-cut algorithm explanation

**Topic ID**: 23670
**Date**: 2022-06-01
**URL**: https://discourse.slicer.org/t/grow-cut-algorithm-explanation/23670

---

## Post #1 by @bserrano (2022-06-01 10:23 UTC)

<p>Hi all,</p>
<p>I have been working lately with the grow-cut algorithm of local threshold. I find it very useful but I can’t figure out how the algorithm works on a code basis, is there any documentation on this?</p>
<p>Thanks,</p>
<p>Belén</p>

---

## Post #2 by @pieper (2022-06-01 12:47 UTC)

<p>Yes, GrowCut is a really useful algorithm.  It’s actually a very simple idea that works well.</p>
<aside class="onebox pdf" data-onebox-src="https://www.graphicon.ru/oldgr/en/publications/text/gc2005vk.pdf">
  <header class="source">

      <a href="https://www.graphicon.ru/oldgr/en/publications/text/gc2005vk.pdf" target="_blank" rel="noopener">graphicon.ru</a>
  </header>

  <article class="onebox-body">
    <a href="https://www.graphicon.ru/oldgr/en/publications/text/gc2005vk.pdf" target="_blank" rel="noopener"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://www.graphicon.ru/oldgr/en/publications/text/gc2005vk.pdf" target="_blank" rel="noopener">gc2005vk.pdf</a></h3>

  <p class="filesize">873.15 KB</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @rbumm (2022-06-01 13:40 UTC)

<p>Interesting link and the algorithm is really working well. Is there a way to involve background seeds (as shown in the paper) in the grow-cut implementation of local threshold?  Would make it even more precise …</p>

---

## Post #4 by @pieper (2022-06-01 13:56 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="3" data-topic="23670">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>background seeds (as shown in the paper)</p>
</blockquote>
</aside>
<p>Do you mean parameters T1 and T2 from section 2.2 of the paper?  I don’t think we have tried those, but they would be possible to add.</p>

---

## Post #5 by @rbumm (2022-06-01 14:57 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="23670">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Do you mean parameters T1 and T2</p>
</blockquote>
</aside>
<p>I actually meant the red/blue seeds in figure 4 section 3.1. In 3D Slicer, the grow-cut process in local threshold is started by the CTRL-left click (one seed/markup) on the area that you want to grow.</p>

---

## Post #6 by @pieper (2022-06-01 18:28 UTC)

<p>Yes, LocalThreshold (from segment editor extra effects extension) is a bit different.  But the regular GrowFromSeeds should be just like what’s shown in figure 4 and it’s the way I typically use the algorithm.  I start by painting some seeds for whatever I want to segment and some rejection class seeds outside and then initialize the preview mode.  From there it can auto update the algorithm as you paint or erase the input (use any tool - paint, draw, scissors…).  For some kinds of data this can converge very quickly to a nice result.  Then remember to go back to GrowFromSeeds and click apply when the preview looks the way you want it.  If you don’t like the result you can undo back to the seeds and redo the grow from seeds part.</p>

---

## Post #7 by @lassoan (2022-06-01 18:49 UTC)

<p>In Local threshold effect, the background seed region is generated automatically by inverting the foreground seed region and shrinking it a bit.</p>

---
