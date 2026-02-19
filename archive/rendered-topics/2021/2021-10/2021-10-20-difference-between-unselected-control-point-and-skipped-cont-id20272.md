---
topic_id: 20272
title: "Difference Between Unselected Control Point And Skipped Cont"
date: 2021-10-20
url: https://discourse.slicer.org/t/20272
---

# Difference between unselected control point and skipped control point

**Topic ID**: 20272
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/difference-between-unselected-control-point-and-skipped-control-point/20272

---

## Post #1 by @jamesobutler (2021-10-20 19:15 UTC)

<p>What’s the difference in usage between setting a markups control point as being “Unselected” versus having a position status that is “Skip placement”?</p>
<p>The markups control point table appears to indicate the Selected/Unselected state is for marking control points to be used or not used by CLI modules. The “Skip placement” appears to also be used to allow control points to be in the list, but marked in a way to not be used (to have a position undefined). Are both used to allow a control point to be in the list, but then marked to be ignored? Are both necessary? Could their functionality be combined in some way?</p>
<p>Would I have a control point that is marked as “Unselected”, but then a point defined (row 3)? Or a control point marked as “Selected”, but then marked as “Skip placement” with no position defined (row 5)?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c96e81924e8f741ffb06e56f0d39a710a87358f9.png" alt="image" data-base62-sha1="sJWJfCAliJQaBDQfU6B3kxITNZ7" width="509" height="187"></p>

---

## Post #2 by @smrolfe (2021-10-20 21:04 UTC)

<p>The “missing” flag is used when placing landmarks from a template on a group of specimens, some of which may be missing features. It indicates that the point is complete (will never become active when placement mode is entered) but has no position recorded.</p>
<p>Using the select/unselect field to indicate missing landmarks would break its use for other tasks that require selecting a persistent subset of control points. For example, SlicerMorph has a module that allows a group of points to be selected and operated on by drawing a curve around them. I believe this property is used similarly in other modules.</p>

---

## Post #3 by @jamesobutler (2021-10-20 21:24 UTC)

<p>If I want to have a row in the control point list to be ignored by various processing on it should I mark it as “Unselected” like some CLI are doing? Or mark it as “Skip placement”, where the position is undefined?</p>

---

## Post #4 by @smrolfe (2021-10-20 21:35 UTC)

<p>In this case you would mark it “Unselected” to ignore during processing of “Selected” points. “Skip placement” is intended to prevent only point placement, not deleting, copy/paste to a new node, etc.</p>

---

## Post #5 by @lassoan (2021-10-22 18:04 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="20272">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If I want to have a row in the control point list to be ignored by various processing on it should I mark it as “Unselected” like some CLI are doing?</p>
</blockquote>
</aside>
<p>It is up to the user and modules to decide how to use the selected flag. For example, it is used in Fiducial registration module to exclude points, while it is used for differentiating inflow/outflow points in Extract centerline module.</p>
<p>Since point status is a new feature, I don’t think any CLI modules use the feature and only those loadable modules use them that are recently modified.</p>

---
