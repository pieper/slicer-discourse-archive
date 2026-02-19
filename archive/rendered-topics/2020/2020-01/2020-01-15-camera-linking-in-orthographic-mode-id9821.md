---
topic_id: 9821
title: "Camera Linking In Orthographic Mode"
date: 2020-01-15
url: https://discourse.slicer.org/t/9821
---

# Camera linking in orthographic mode

**Topic ID**: 9821
**Date**: 2020-01-15
**URL**: https://discourse.slicer.org/t/camera-linking-in-orthographic-mode/9821

---

## Post #1 by @smrolfe (2020-01-15 04:31 UTC)

<p>I’m having a problem linking two 3D views when orthographic mode is enabled. Translate and rotate are working as intended, but the zoom isn’t linking.</p>
<p>I’m using the current Preview version. We ran into <a href="https://discourse.slicer.org/t/is-camera-linking-broken-in-4-10-1/5668">a similar issue</a> using perspective rendering in a previous nightly version, but it was corrected.</p>
<p>Is this a known issue?</p>

---

## Post #2 by @muratmaga (2020-01-15 16:23 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> We use linked 3D rendering a lot in SlicerMorph’s GPA module, it is quite an important feature for us…</p>

---

## Post #3 by @pieper (2020-01-15 21:06 UTC)

<p>I don’t think anyone had tested that mode - I put in a small fix that seems to work - let us know if it’s still broken in tomorrow’s build.</p>
<p><a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28731" class="onebox" target="_blank">http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28731</a></p>

---

## Post #4 by @smrolfe (2020-01-15 21:14 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, we’ll update you tomorrow.</p>

---

## Post #5 by @smrolfe (2020-01-16 16:32 UTC)

<p>The fix works well for me in the latest Mac package. Thanks <a class="mention" href="/u/pieper">@pieper</a>! It looks like there’s been no new Windows builds for a while, is this due to the recent server upgrade?</p>

---

## Post #6 by @pieper (2020-01-16 19:20 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="5" data-topic="9821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>It looks like there’s been no new Windows builds for a while, is this due to the recent server upgrade?</p>
</blockquote>
</aside>
<p>Yes, last I heard the windows factory machine upgrade could not complete (some mysterious hex code) so they were going to need to reinstall from scratch including all the build tools.  Hopefully it won’t take long.</p>

---
