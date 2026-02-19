---
topic_id: 44475
title: "Visible Segment In 3D May Have A None Representation Name"
date: 2025-09-14
url: https://discourse.slicer.org/t/44475
---

# Visible segment in 3D may have a None representation name

**Topic ID**: 44475
**Date**: 2025-09-14
**URL**: https://discourse.slicer.org/t/visible-segment-in-3d-may-have-a-none-representation-name/44475

---

## Post #1 by @chir.set (2025-09-14 20:31 UTC)

<p>Please consider these steps:</p>
<ul>
<li>add a volume in a new scene</li>
<li>in the segment editor, paint anything in a slice view</li>
<li>in the python console
<ul>
<li><code>seg = getNode("Segmentation")</code></li>
<li><code>seg.GetDisplayNode().GetPreferredDisplayRepresentationName3D() == None # True</code></li>
<li><code>seg.CreateClosedSurfaceRepresentation()</code>
<ul>
<li>the segment becomes visible in 3D</li>
<li>the Show 3D button gets enabled, but</li>
<li><code>seg.GetDisplayNode().GetPreferredDisplayRepresentationName3D() == None # still True</code></li>
</ul>
</li>
<li>Uncheck/check the 3D button
<ul>
<li><code>seg.GetDisplayNode().GetPreferredDisplayRepresentationName3D() == None # False</code></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The same is observed with <code>CreateBinaryLabelMapRepresentation()</code>, except that the segment does not become visible in 3D (which is logical).</p>
<p>One would expect that <code>GetPreferredDisplayRepresentationName3D()</code> would not be <code>None</code> if there is a 3D display.</p>
<p>What are your views about that ?</p>

---

## Post #2 by @cpinter (2025-09-15 14:21 UTC)

<p>As far as I can tell (probably I implemented this but more than 5 years ago), this member is to override the default representation that is shown in a certain type of view. I think <code>None</code> is an acceptable value, and it means that the default representation is shown.</p>
<p>Does this cause any issue for you?</p>

---

## Post #3 by @chir.set (2025-09-15 14:39 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="44475">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Does this cause any issue for you?</p>
</blockquote>
</aside>
<p>Well, I discovered this unexpected state after observing a minor issue that can be easily fixed. There is no need to touch the core of Segmentation, I just wanted to collect a few point of views.</p>
<p>Thank you for yours.</p>

---

## Post #4 by @cpinter (2025-09-16 10:51 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="44475">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I discovered this unexpected state</p>
</blockquote>
</aside>
<p>What I don’t agree with is that this would be an unexpected state. A <code>None</code> value in an option indicating that the default is used does not seem unexpected to me at all.</p>

---

## Post #5 by @chir.set (2025-09-16 13:38 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="44475">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>A <code>None</code> value in an option indicating that the default is used</p>
</blockquote>
</aside>
<p>Good tho know it’s a guideline in Slicer, thank you for the hint.</p>

---
