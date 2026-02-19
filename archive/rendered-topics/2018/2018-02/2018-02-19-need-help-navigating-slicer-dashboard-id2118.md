---
topic_id: 2118
title: "Need Help Navigating Slicer Dashboard"
date: 2018-02-19
url: https://discourse.slicer.org/t/2118
---

# Need help navigating Slicer dashboard

**Topic ID**: 2118
**Date**: 2018-02-19
**URL**: https://discourse.slicer.org/t/need-help-navigating-slicer-dashboard/2118

---

## Post #1 by @fedorov (2018-02-19 18:21 UTC)

<p>I no longer see nightly builds at the location they used to be: <a href="http://slicer.cdash.org/index.php?project=Slicer4">http://slicer.cdash.org/index.php?project=Slicer4</a>, the only category is Extensions-4.8-Nightly. The download page shows Slicer was build last night, but I can’t find where it was build, and I would also like to see the 4.9 extensions status. Where can I find those?</p>

---

## Post #2 by @ihnorton (2018-02-19 18:35 UTC)

<p><a href="http://slicer.cdash.org">slicer.cdash.org</a> then click SlicerPreview. See:</p>
<aside class="quote" data-post="10" data-topic="2091">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/different-dashboard-for-master-and-stable-builds/2091/10">Different dashboard for master and stable builds</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Updates: 


Dashboard will be <a href="http://slicer.cdash.org/index.php?project=SlicerPreview">SlicerPreview</a> 


Slicer has been updated accordingly - see <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26928">r26928</a> 


New <a href="https://github.com/mhalle/slicer4-download/pull/13">PR mhalle/slicer4-download#13</a> was just submitted to update <a href="http://download.slicer.org/">http://download.slicer.org/</a> and use the term Preview Release instead of Nightly Build
  </blockquote>
</aside>


---

## Post #3 by @fedorov (2018-02-19 18:47 UTC)

<p>Thank you Isaiah! I actually did look at that one, but didn’t notice that the Slicer packages are at the bottom of the page, and not on top as they used to be.</p>

---

## Post #4 by @jcfr (2018-02-19 19:03 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="3" data-topic="2118">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>didn’t notice that the Slicer packages are at the bottom of the page</p>
</blockquote>
</aside>
<p>Thanks for reporting this. Order of the groups has just been updated. Let us know if you observe something else.</p>

---

## Post #5 by @lassoan (2018-02-19 23:10 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> The dashboard separation is great! It loads faster and easier to find what I need (stable or preview extensions).</p>

---
