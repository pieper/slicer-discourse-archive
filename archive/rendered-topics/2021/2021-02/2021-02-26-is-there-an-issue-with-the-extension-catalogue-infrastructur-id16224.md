# Is there an issue with the extension catalogue infrastructure?

**Topic ID**: 16224
**Date**: 2021-02-26
**URL**: https://discourse.slicer.org/t/is-there-an-issue-with-the-extension-catalogue-infrastructure/16224

---

## Post #1 by @muratmaga (2021-02-26 00:24 UTC)

<p>throughout the day it was very slow or unresponsive at times (like right now).</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #2 by @lassoan (2021-02-26 13:50 UTC)

<p>The Extensions Manager server is often overloaded because it needs to manage more packages and requests as it has been designed for. It will be replaced soon.</p>
<p>Also, until very recently there has been a problem with Slicer unnecessarily flooding the server with requests when starting the Extensions Manager, which led to slower response and timeouts. I’ve implemented request caching in recent Slicer Preview Releases, which reduced unnecessary requests and drastically improved the performance and robustness.</p>
<p>When we roll out a new stable release (expected within a week or so) and upgrade the server (maybe in 1-2 months) then speed and reliability of browsing and installing extensions are expected to be magnitudes better.</p>

---
