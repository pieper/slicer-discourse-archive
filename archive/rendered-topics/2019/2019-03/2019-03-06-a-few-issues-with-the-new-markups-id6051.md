---
topic_id: 6051
title: "A Few Issues With The New Markups"
date: 2019-03-06
url: https://discourse.slicer.org/t/6051
---

# A few issues with the new Markups

**Topic ID**: 6051
**Date**: 2019-03-06
**URL**: https://discourse.slicer.org/t/a-few-issues-with-the-new-markups/6051

---

## Post #1 by @smrolfe (2019-03-06 22:24 UTC)

<p>I’ve been using the new Markups module and have run into a few issues. I’m testing on the most recent nightly build.</p>
<ol>
<li>Toggling the visibility of landmarks causes them to be permanently invisible.</li>
<li>The 2D projection option does not appear to be working.</li>
<li>The GetMarkupPoint() function in vtkMRMLMarkupsFiducialNode does not appear to be supported. Is this planned? I believe I can also use GetMarkupPointVector() to do the same thing.</li>
</ol>

---

## Post #2 by @smrolfe (2019-03-06 22:31 UTC)

<p>2D projection is not yet implemented, as noted in this thread:</p><aside class="quote" data-post="5" data-topic="6044">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/adding-points-to-open-curve/6044/5">Adding points to open curve</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    thanks for reporting. Fiducial projection is still not implemented. 
For reference here there are all the known reaming bugs and missing features: 
<a href="https://1drv.ms/x/s!Arm_AFxB9yqHtvxAsyBDU_3C1IxfGA" class="onebox" target="_blank" rel="noopener nofollow ugc">https://1drv.ms/x/s!Arm_AFxB9yqHtvxAsyBDU_3C1IxfGA</a>
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2019-03-07 00:03 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="1" data-topic="6051">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>Toggling the visibility of landmarks causes them to be permanently invisible.</p>
</blockquote>
</aside>
<p>Added an issue to the spreadsheet.</p>
<aside class="quote no-group" data-username="smrolfe" data-post="1" data-topic="6051">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>The GetMarkupPoint() function in vtkMRMLMarkupsFiducialNode does not appear to be supported. Is this planned? I believe I can also use GetMarkupPointVector() to do the same thing</p>
</blockquote>
</aside>
<p><code>GetNthControlPointPosition</code> method should be used instead. I’ll add a method (marking it as deprecated) to make transition to the updated API easier. The API was really messy, using “vector” and “world” suffixes and data types quite inconsistently. It is still not very clear, so we’ll improve it further (but keep old methods in place for a while).</p>

---

## Post #4 by @smrolfe (2019-03-07 02:29 UTC)

<p>Great, thanks <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---
