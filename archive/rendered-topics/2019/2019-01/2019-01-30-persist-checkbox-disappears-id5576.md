---
topic_id: 5576
title: "Persist Checkbox Disappears"
date: 2019-01-30
url: https://discourse.slicer.org/t/5576
---

# Persist checkbox disappears

**Topic ID**: 5576
**Date**: 2019-01-30
**URL**: https://discourse.slicer.org/t/persist-checkbox-disappears/5576

---

## Post #1 by @chir.set (2019-01-30 08:00 UTC)

<p>Please see the attached image. After selecting any of the three items in that toolbar list, the persistance checkbox will vanish. I noticed that many months ago and expected a discrete fix. Unfortunately, it’s still an unexpected behavior. Now it’s not a real problem, I just want to report it.</p>
<p>I’m using Slice built from git on Linux (KDE, Xorg), with the Python 2.7.15 as the only modification, instead of 2.7.13.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/559102a1b9394422bb63a1d3f5b4f1f59113d3af.png" alt="no_persist" data-base62-sha1="ccXgCv7OTBfJIpVE0uClwlUIs11" width="536" height="181"></p>

---

## Post #2 by @pieper (2019-01-30 08:22 UTC)

<p>Hi SET - thanks for the report. Does it happen with the stable or nightly builds from <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a>?  I tested 4.10.1 on debian and don’t have an issue.</p>

---

## Post #3 by @chir.set (2019-01-30 09:26 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="5576">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Does it happen with the stable or nightly builds from <a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a>?</p>
</blockquote>
</aside>
<p>Hi Steve,</p>
<p>It does not happen with 4.10.1 stable nor with 4.11.0 nightly 2019-01-27 from <a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a>. So it related to my build.</p>
<p>I should have checked before, sorry for having bothered you.</p>
<p>Anyway, it’s not a fundamental problem, and I don’t use the persist checkbox very often.</p>
<p>If relevant, I build on Arch Linux with GCC 8.x and Qt 5.12.</p>
<p>Thanks.</p>

---

## Post #4 by @lassoan (2019-01-31 00:32 UTC)

<p>It may have something to do with the Qt version (I think we use an earlier version for the nightly builds).</p>

---

## Post #5 by @chir.set (2019-03-24 15:04 UTC)

<p>Since 2019-03-09 build, the persist checkbox, well, just persists <img src="https://emoji.discourse-cdn.com/twitter/star_struck.png?v=9" title=":star_struck:" class="emoji" alt=":star_struck:"></p>

---

## Post #6 by @lassoan (2019-03-24 18:44 UTC)

<p>Do you mean the problem is solved?</p>

---

## Post #7 by @chir.set (2019-03-24 19:56 UTC)

<p>Yes, marking it as such.</p>

---
