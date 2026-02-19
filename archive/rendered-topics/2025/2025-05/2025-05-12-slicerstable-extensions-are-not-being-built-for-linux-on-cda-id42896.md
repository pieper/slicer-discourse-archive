---
topic_id: 42896
title: "Slicerstable Extensions Are Not Being Built For Linux On Cda"
date: 2025-05-12
url: https://discourse.slicer.org/t/42896
---

# SlicerStable - extensions are not being built for Linux on cdash

**Topic ID**: 42896
**Date**: 2025-05-12
**URL**: https://discourse.slicer.org/t/slicerstable-extensions-are-not-being-built-for-linux-on-cdash/42896

---

## Post #1 by @chir.set (2025-05-12 20:22 UTC)

<p>No extension is being built for Linux on cdash since a few weeks, there is simply no line for Linux.</p>
<p>I just want to highlight it in case it went unnoticed. Or may be there are known reasons.</p>

---

## Post #2 by @muratmaga (2025-05-15 15:57 UTC)

<p>This is still true as of this morning.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a>  an update please?</p>

---

## Post #3 by @chir.set (2025-05-28 19:09 UTC)

<p>Still true today. Has Linux platform been abandoned for Slicer stable?</p>

---

## Post #4 by @muratmaga (2025-05-28 22:34 UTC)

<p>I don’t think it is abandoned, but I agree it doesn’t look good that we have not updated the stable extensions for over two weeks now.</p>
<p>At some point there were some hardware issues with the build factory at Kitware, but I thought it was resolved.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> ?</p>

---

## Post #5 by @lassoan (2025-05-29 15:01 UTC)

<p>Definitely not abandoned, but no extension update since May 1 is getting way too long. Hopefully <a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> will comment here but if not then we’ll raise this question at the next weekly developer meeting on Tuesday.</p>

---

## Post #6 by @jcfr (2025-05-29 16:10 UTC)

<p>After looking into this, it turns out that the Stable build tree for the latest <code>5.8.1</code> release was inadvertently removed.</p>
<p>A new one is being re-generated. See  <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-05-29&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex">here</a></p>

---

## Post #7 by @chir.set (2025-05-30 12:40 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="42896">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>A new one is being re-generated.</p>
</blockquote>
</aside>
<p>Yes, up-to-date extensions are now available for Slicer stable on Linux, thanks.</p>

---
