# Export my own Slicer

**Topic ID**: 22691
**Date**: 2022-03-25
**URL**: https://discourse.slicer.org/t/export-my-own-slicer/22691

---

## Post #1 by @Chicago_Girl (2022-03-25 22:37 UTC)

<p>I’ve made some extensions and installed them on Slicer.<br>
They are not easy to install. Is there any way that I can make an export of my current version of Slicer?</p>
<p>So, when I give them others and they install it, the extensions will be there.</p>

---

## Post #2 by @lassoan (2022-03-26 03:03 UTC)

<p>I would recommend to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#distribute-an-extension">submit your extension to the extensions index</a>. That will make the extension available for users by a few clicks, in current and future Slicer versions, on all platforms.</p>
<p>Slicer is portable - it does not require installation but can run from anywhere (even from a USB stick). Therefore, if the extension private then you can distribute it by simply copying the Slicer install tree to the user’s computer.</p>

---

## Post #3 by @dsa934 (2023-01-17 02:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22691">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer is portable - it does not require installation but can run from anywhere (even from a USB stick). Therefore, if the extension private then you can distribute it by simply copying the Slicer install tree to the user’s computer.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>What’s is the Slicer’s install tree?</p>
<p>Where can I find related information?</p>

---

## Post #4 by @lassoan (2023-01-17 05:38 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="3" data-topic="22691">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>What’s is the Slicer’s install tree?</p>
</blockquote>
</aside>
<p>The directory tree where Slicer application is installed into. We use this term to differentiate from the “build tree”, which is the directory tree where Slicer is built in.</p>
<aside class="quote no-group" data-username="dsa934" data-post="3" data-topic="22691">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>Where can I find related information?</p>
</blockquote>
</aside>
<p>You can search in the <a href="https://slicer.readthedocs.io/en/latest/index.html">documentation</a>, but probably it is even simpler to just use web search, as all Slicer documentation, discussion, examples, and code are indexed by all major search engines. If you don’t find an answer you can ask here.</p>

---
