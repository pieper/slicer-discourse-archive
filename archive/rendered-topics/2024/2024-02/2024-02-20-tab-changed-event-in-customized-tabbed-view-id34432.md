# Tab changed event in customized tabbed view

**Topic ID**: 34432
**Date**: 2024-02-20
**URL**: https://discourse.slicer.org/t/tab-changed-event-in-customized-tabbed-view/34432

---

## Post #1 by @bzhu (2024-02-20 18:45 UTC)

<p>With a customized tab view, I have several tabs in a layout.<br>
(See <a href="https://discourse.slicer.org/t/customized-tabbed-view/24375">Customized tabbed view</a><br>
Within each tab, there are a group of views. I need to place some action code when the active tab is changed. Help to capture this tab changed event is appreciated.</p>
<p>Bing from UCLA</p>

---

## Post #2 by @lassoan (2024-02-20 20:09 UTC)

<p>You can look up the child widget using <code>slicer.util.findChildren</code> function and connect your callback function to the relevant signal.</p>

---

## Post #3 by @bzhu (2024-02-20 23:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="34432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.util.findChildren</p>
</blockquote>
</aside>
<p>Yes, the tab widget is found by this method. Thanks.</p>

---
