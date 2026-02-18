# How can i use 3DSlicer in a not local host container to do a brain segmentation of a Photon-Counting CT (totalsegmentor extension)?

**Topic ID**: 32785
**Date**: 2023-11-13
**URL**: https://discourse.slicer.org/t/how-can-i-use-3dslicer-in-a-not-local-host-container-to-do-a-brain-segmentation-of-a-photon-counting-ct-totalsegmentor-extension/32785

---

## Post #1 by @Carolina_Alves (2023-11-13 17:50 UTC)

<p>I do not know how to install the 3DSlicer in my not localhost container xc. I pretend to use the total segmentor extension in a jupyter notebook of my container. This is for my master thesis about segmentation a PCCT.</p>

---

## Post #2 by @pieper (2023-11-13 18:18 UTC)

<aside class="quote no-group" data-username="Carolina_Alves" data-post="1" data-topic="32785">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carolina_alves/48/68292_2.png" class="avatar"> Carolina_Alves:</div>
<blockquote>
<p>not localhost container xc</p>
</blockquote>
</aside>
<p>Can you clarify what you are refering to here?</p>

---

## Post #3 by @Carolina_Alves (2023-11-14 09:56 UTC)

<p>For my thesis project, my advisor has created an online container on his server for me to work on, but I can’t install 3DSlicer xc there (I think it has to be a terminal or script installation).</p>

---

## Post #4 by @pieper (2023-11-14 13:30 UTC)

<p>This sounds like something you’ll need to work out with your advisor.  Slicer is a desktop application that needs something like a windows desktop or an X session, ideally with GPU support for most operations.  You could research how Slicer is used in docker or on cloud virtual machines to better understand what your options are (there’s a lot of material you can get via a search engine query).</p>

---
