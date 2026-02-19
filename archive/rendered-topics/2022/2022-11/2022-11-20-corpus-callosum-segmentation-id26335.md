---
topic_id: 26335
title: "Corpus Callosum Segmentation"
date: 2022-11-20
url: https://discourse.slicer.org/t/26335
---

# Corpus callosum segmentation 

**Topic ID**: 26335
**Date**: 2022-11-20
**URL**: https://discourse.slicer.org/t/corpus-callosum-segmentation/26335

---

## Post #1 by @bnc0720 (2022-11-20 20:21 UTC)

<p>Hi Everyone,</p>
<p>I start a project in University and I need a little help. Our goal to segmentation corpus callosum and see the fractional anisotropy in these region. First I create the segmentation with hand draw tool in all slice, but I think it isn’t enough representative. After that I try threshold, but in DTI picture it isn’t useable.<br>
Anybody can suggest me how to do an easy corpus callosum segmentation?</p>

---

## Post #2 by @lassoan (2022-11-20 20:35 UTC)

<aside class="quote no-group" data-username="bnc0720" data-post="1" data-topic="26335">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/ce73a5/48.png" class="avatar"> bnc0720:</div>
<blockquote>
<p>create the segmentation with hand draw tool in all slice, but I think it isn’t enough representative</p>
</blockquote>
</aside>
<p>What do you mean by not enough representative? Not accurate enough? Why? Do you see some errors in your segmentation that you cannot fix?</p>
<p>The corpus callosum typically has a good contrast to surrounding structures in MRI, so you can quickly and accurately segment it using semi-automatic methods, such as “Grow from seeds”. There are many fully automatic brain segmentation tools, but if you only need to segment a single structure then it may not worth the time to set one up.</p>
<aside class="quote no-group" data-username="bnc0720" data-post="1" data-topic="26335">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/ce73a5/48.png" class="avatar"> bnc0720:</div>
<blockquote>
<p>After that I try threshold, but in DTI picture it isn’t useable.</p>
</blockquote>
</aside>
<p>How do you want to use it in a DTI image? What problem have you encountered?</p>

---

## Post #3 by @bnc0720 (2022-11-20 21:18 UTC)

<p>I asked the question very wrong, because I only provided little part of the information.<br>
So I want to segment the corpus callosum of 50 people, who suffered from multiple sclerosis. After that I want to measurement the fractional anisotropy of these corpus callosum segment and make fiber tracking.<br>
I followed the diffusion tutorial, so I can make succesfully the fractional anisotropy “map” , and use the segment statistics to see the data of the segment. Our dwi data is 128x128 so the contrast according to the surrounding structure is not the best, but it’s possible that I’m doing something wrong.<br>
So I only use the draw tool for make the segment, the other method didn’t work, and I search a better way to make the segmentation. If you have any suggestion how to make the segmentation, and help how to make it, I will be very grateful.</p>
<p>The data is from a 3T siemens MR.</p>

---
