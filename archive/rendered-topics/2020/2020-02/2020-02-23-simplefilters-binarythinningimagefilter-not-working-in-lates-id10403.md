---
topic_id: 10403
title: "Simplefilters Binarythinningimagefilter Not Working In Lates"
date: 2020-02-23
url: https://discourse.slicer.org/t/10403
---

# SimpleFilters (BinaryThinningImageFilter) not working in latest MacOS build?

**Topic ID**: 10403
**Date**: 2020-02-23
**URL**: https://discourse.slicer.org/t/simplefilters-binarythinningimagefilter-not-working-in-latest-macos-build/10403

---

## Post #1 by @hherhold (2020-02-23 15:11 UTC)

<p>I’m trying to run BinaryThinningImageFilter on the CTACardio dataset. (Tried it on my own dataset and it didn’t work either, so I figured I’d try a sample dataset.)</p>
<ol>
<li>Load CTACardio</li>
<li>Select “Simple Filters”</li>
<li>Select “BinaryThinningImageFilter”</li>
<li>Select CTACardio as input</li>
<li>Select “Create new volume” as output</li>
<li>Hit “Apply”</li>
</ol>
<p>Filter never returns. Stays at zero percent, also UI is fully functional (step through slices, etc). No errors on console, only output is:</p>
<pre><code>myFilter = BinaryThinningImageFilter()
myFilter.SetDebug(False)
myFilter.SetNumberOfThreads(16)
</code></pre>
<p>I saw some posts a few days back on issues with SimpleFilters- is this related?</p>
<p>Thanks!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2020-02-23 15:25 UTC)

<p>Latest Slicer Preview Release should work. Progress reporting broke in the ITK release candidate that we are using, so it may look like ITK is not working, but most probably it does, you just need to wait. The new ITK release candidate that has just been tagged is supposed to contain a fix, so the problem is expected to be solved soon.</p>
<p>Try latest Slicer Preview Release, other filters, and on smaller data and let us know if they work.</p>

---

## Post #3 by @hherhold (2020-02-23 15:39 UTC)

<p>OK, other filters work fine. I know I’ve run this before, specifically for this workflow (below), but I feel like I’m doing something wrong… I will let it run but I’m pretty sure it did not take this long the last time I did this.</p>
<p>Thanks!</p>
<aside class="quote quote-modified" data-post="1" data-topic="2735">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-analyze-the-thickness-of-the-model/2735">How to analyze the thickness of the model</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Can I analyze the thickness of a stl model, and then get a color map. 
The distance between the two sides of an object. 
[2018-04-30_215013]
  </blockquote>
</aside>


---

## Post #4 by @jamesobutler (2020-02-23 16:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10403">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The new ITK release candidate that has just been tagged is supposed to contain a fix, so the problem is expected to be solved soon.</p>
</blockquote>
</aside>
<p>I have observed that the main Progress Reporting PR (<a href="https://github.com/InsightSoftwareConsortium/ITK/pull/1575" rel="noopener nofollow ugc">https://github.com/InsightSoftwareConsortium/ITK/pull/1575</a>) still hasn’t been merged and that the recently tagged ITK 5.1rc02 does not contain any of the commits from that PR. Maybe it will make it into ITK 5.1rc03 in a couple weeks.</p>

---

## Post #5 by @hherhold (2020-02-29 18:53 UTC)

<p>Is the lack of progress reporting back to slicer the issue?</p>

---

## Post #6 by @hherhold (2020-02-29 19:02 UTC)

<p>I really feel like I’m doing something wrong.</p>
<p>I have a segment that I’ve converted to a label map. I try to run this through the Binary Image Thinning Filter, creating a new label map volume. It never returns. I’ve run other filters and they seem to work.</p>
<p>Should this work?</p>

---

## Post #7 by @hherhold (2020-02-29 19:03 UTC)

<p>Also, for what it’s worth, I tried this on 4.10.2 and it did the same thing. I <em>know</em> I’ve done this before and it worked, because I opened the old scene file I had where it <em>did</em> work.</p>

---
