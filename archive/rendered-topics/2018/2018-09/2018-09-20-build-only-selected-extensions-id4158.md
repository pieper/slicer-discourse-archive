# Build only selected extensions

**Topic ID**: 4158
**Date**: 2018-09-20
**URL**: https://discourse.slicer.org/t/build-only-selected-extensions/4158

---

## Post #1 by @torquil (2018-09-20 18:03 UTC)

<p>Hi!</p>
<p>I’m building Slicer Git Master myself, and therefore also the Extensions. However, since it takes a long time, I would like to only build a few selected extensions. Is there a more elegant way of doing it than deleting all the *.s4ext files that are not wanted from the local ExtensionsIndex git repository?</p>
<p>Best regards<br>
Torquil Sørensen</p>

---

## Post #2 by @lassoan (2018-09-20 18:18 UTC)

<p>It seems elegant enough for me, but if you want to make this a bit more reproducible then you can fork ExtensionIndex repository and in your fork keep only those s4ext files that you are interested in.</p>

---

## Post #3 by @ihnorton (2018-09-20 18:30 UTC)

<aside class="quote no-group" data-username="torquil" data-post="1" data-topic="4158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e79b87/48.png" class="avatar"> torquil:</div>
<blockquote>
<p>Is there a more elegant way of doing it than deleting all the *.s4ext files that are not wanted from the local ExtensionsIndex git repository?</p>
</blockquote>
</aside>
<p>Copy them to another folder with a simple script, rather than delete?</p>

---
