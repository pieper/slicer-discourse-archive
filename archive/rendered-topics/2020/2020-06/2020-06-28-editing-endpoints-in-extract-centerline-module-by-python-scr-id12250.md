# Editing endpoints in extract centerline module by Python scripting

**Topic ID**: 12250
**Date**: 2020-06-28
**URL**: https://discourse.slicer.org/t/editing-endpoints-in-extract-centerline-module-by-python-scripting/12250

---

## Post #1 by @Deepa (2020-06-28 05:19 UTC)

<p>Hello Everyone,<br>
Currently, the extract centerline module allows the removal of branches by clicking on the endpoints.<br>
I would like to know if it’s possible to do the same task using a set of input coordinates (coordinates of<br>
endpoints/free ends or junction points) specified by the user.</p>

---

## Post #2 by @lassoan (2020-06-28 13:13 UTC)

<p>Yes, you can get index of a control point based on its position and remove it by calling methods of the markups node.</p>

---

## Post #3 by @Deepa (2020-06-28 14:05 UTC)

<p>I have the indices of the position using <code>GetPointId</code>.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>remove it by calling methods of the markups node.</p>
</blockquote>
</aside>
<p>I am not sure how to do this. May I know if examples are available to understand how this can be done?</p>

---

## Post #4 by @lassoan (2020-06-28 14:22 UTC)

<p>These should be all fairly straightforward and it is hard to guess where you might have stuck. Please share the script that you are trying to use and indicate where it does not work as expected.</p>

---
