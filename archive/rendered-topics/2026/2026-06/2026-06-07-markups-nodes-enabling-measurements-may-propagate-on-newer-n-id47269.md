---
topic_id: 47269
title: "Markups nodes: enabling measurements may propagate on newer nodes"
date: 2026-06-07
url: https://discourse.slicer.org/t/47269
last_bumped: 2026-06-07T19:24:12.206Z
---

# Markups nodes: enabling measurements may propagate on newer nodes

**Topic ID**: 47269
**Date**: 2026-06-07
**URL**: https://discourse.slicer.org/t/markups-nodes-enabling-measurements-may-propagate-on-newer-nodes/47269

---

## Post #1 by @chir.set (2026-06-07 11:45 UTC)

<p>I am seeing an unexpected behaviour regarding the display of measurements in markups nodes, in all versions of Slicer on Linux.</p>
<p>Start 5.10 stable for instance:</p>
<ul>
<li>draw a <code>Closed curve</code> node: no measurement is displayed</li>
<li>go to the <code>Markups module</code></li>
<li>enable <code>length</code> and <code>area</code>: the measurements are displayed</li>
<li>draw a new <code>Closed curve</code> node: the <code>length</code> and <code>area</code> measurements are displayed</li>
</ul>
<p>This can be reproduced with other markups nodes also, Slicer native or from ExtraMarkups.</p>
<p>While trying to reproduce this by code, the result is very inconsistent, sometimes expected and sometimes unexpected.</p>
<p>It would be of interest if someone could try to reproduce that in any environment.</p>
<p>Thanks.</p>

---

## Post #2 by @muratmaga (2026-06-07 15:45 UTC)

<p>I can reproduce on this MacOS with slight variations. As you describe I create a closed curve and then enable some of the measurements (length, curve, curvature, curvature max) and then drew another curve</p>
<p><strong>on 5.10.</strong></p>
<p>Second curve displayed the length only.</p>
<p><strong>on 5.11 from June 2nd</strong></p>
<p>Second curve displayed all three measurements.</p>
<p>I agree this a bit confusing, since I always thought to be property of individual markup object as opposed to default on and off (and if it is a global on/off, then one can argue it is in the wrong place in the UI).</p>

---

## Post #3 by @chir.set (2026-06-07 16:56 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="47269">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I can reproduce on this MacOS with slight variations.</p>
</blockquote>
</aside>
<p>Thank you for your reply. At least I know it’s not only me.</p>
<p>Measurement display should be a private property of each node IMO, like the colour of the node and its name.</p>

---

## Post #4 by @muratmaga (2026-06-07 18:49 UTC)

<p>You may want to open an issue for this to be tracked on the gh.</p>

---

## Post #5 by @chir.set (2026-06-07 19:24 UTC)

<p>Yep, done <a href="https://github.com/Slicer/Slicer/issues/9214" rel="noopener nofollow ugc">here</a>.</p>

---
