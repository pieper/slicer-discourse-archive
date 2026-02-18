# Interactions with the plane widget is problematic

**Topic ID**: 14174
**Date**: 2020-10-20
**URL**: https://discourse.slicer.org/t/interactions-with-the-plane-widget-is-problematic/14174

---

## Post #1 by @muratmaga (2020-10-20 21:11 UTC)

<p>I filled a bug for Planes, in which trying to use <a href="https://github.com/Slicer/Slicer/issues/5257#issue-725944150">interaction handles to drag the plane in a single axis causes a shift in its original position</a>).</p>
<p>For example, trying to drag the plane in direction of the yellow arrow would cause an initiation jump to the opposite side and then it moves correctly in the chosen direction.</p>
<p>Consistently happens with the latest stable on windows<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/cae7190eb2b6a4f03166d36183e718bf94067214.png" alt="image" data-base62-sha1="sWXzAhQhFALbjF5vz8ExZ3u16QI" width="285" height="478"></p>

---

## Post #2 by @lassoan (2020-10-21 00:05 UTC)

<p>Thanks for reporting, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> will have a look. Things that are very likely bugs and not expected to require discussion can be submitted directly as bug reports (without creating a forum topic).</p>

---
