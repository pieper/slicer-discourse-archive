---
topic_id: 14760
title: "Loading In Huge Data"
date: 2020-11-24
url: https://discourse.slicer.org/t/14760
---

# Loading in huge data

**Topic ID**: 14760
**Date**: 2020-11-24
**URL**: https://discourse.slicer.org/t/loading-in-huge-data/14760

---

## Post #1 by @NoobForSlicer (2020-11-24 23:05 UTC)

<p>So one man from here called Alex_Vergara helped me process huge batches of .png images.</p>
<p>He made an incredibly well script module but I have some questions concerning Slicer in general.</p>
<p>I noticed once a batch of PNG images is being loaded in, it is not the disk speed that matters. I got NVMe from a friend Samsung 980 PRO PCIe 4.0 (up to 7,000 MB/s)</p>
<p>7000 MB/s and our boss upgraded machines to over 60GB of ram.<br>
because what he had me working with some months ago was idk… very horrible.</p>
<p>With this new hardware NVMe I supposed loading in should be faster. But it isn’t. Or at least I don’t notice any change.</p>
<p>The speed is supposably more than 20 times faster than the old SSD.</p>
<p>Well… Why?</p>
<p>I assume there is somet recalculation that the CPU has to do and so disk speed isn’t even important that much because bottle neck is made by the CPU processing speed?</p>

---

## Post #2 by @timeanddoctor (2020-11-25 05:59 UTC)

<p>The script code maybe edit by python which will be blocked by the GIL：<a href="https://realpython.com/python-gil/" rel="noopener nofollow ugc">https://realpython.com/python-gil/</a></p>
<p>So the speed will not improve significantly after the update of computer if you donnot recode the script.</p>

---

## Post #3 by @muratmaga (2020-11-25 06:55 UTC)

<p>Because reading and writing thousands of files individually has a lot of overhead. See this</p><aside class="quote" data-post="6" data-topic="9240">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/can-slicer-utilise-multiple-cores-on-linux/9240/6">Can Slicer utilise multiple cores on linux?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Out of curiosity, I made a rough test. 
Reading a sequence of 2200 PNG images that resulted in a 10GB volume took 3’ 25" on a 32GB laptop with a nvme drive (Using ImageStack from <a class="mention" href="/u/pieper">@pieper</a>). Saving same volume as nrrd without compression took about 4 seconds. Flushing the cache and reloading the uncompressed 10GB NRRD into a fresh instance of Slicer took 26 seconds.
  </blockquote>
</aside>


---

## Post #4 by @NoobForSlicer (2020-11-25 15:05 UTC)

<p>incredible post, I became interested because yesterday they gave me over 60 GB of png sequence.</p>
<p>with 60gb ram and 1000 GB NVMe available for virtual ram memory and storing images,</p>
<p>it worked fine and everything is okay.</p>

---
