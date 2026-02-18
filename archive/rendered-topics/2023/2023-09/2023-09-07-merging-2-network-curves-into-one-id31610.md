# Merging 2 Network Curves into One

**Topic ID**: 31610
**Date**: 2023-09-07
**URL**: https://discourse.slicer.org/t/merging-2-network-curves-into-one/31610

---

## Post #1 by @sthaker (2023-09-07 19:24 UTC)

<p>Hello,</p>
<p>I have been having this issue (using ExtractCenterline Module) when I am trying to extract the centerlines of a stl model of an aorta where there is a random branch (one not bounded by an endpoint) that is added. I delete the random branch, but I do not know how to merge the other two network curves into one curve so that I can resample the combined curve with 50 points in the Markups Module. Could someone please help me with this issue?</p>

---

## Post #2 by @lassoan (2023-09-08 04:07 UTC)

<p>You can copy the control points in Markups module’s Control points section, copy and paste (or prgrammatically using Python scripting).</p>
<aside class="quote no-group" data-username="sthaker" data-post="1" data-topic="31610">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/8dc957/48.png" class="avatar"> sthaker:</div>
<blockquote>
<p>I am trying to extract the centerlines of a stl model of an aorta where there is a random branch (one not bounded by an endpoint) that is added</p>
</blockquote>
</aside>
<p>If you use “Centerline extraction” then curve will be drawn only between endpoints that you specify.</p>

---

## Post #3 by @sthaker (2023-09-09 17:56 UTC)

<p>Thanks so much for your help!</p>

---
