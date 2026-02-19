---
topic_id: 42615
title: "Add A Keyboard Shortcut To Close The Application"
date: 2025-04-18
url: https://discourse.slicer.org/t/42615
---

# Add a keyboard shortcut to close the application

**Topic ID**: 42615
**Date**: 2025-04-18
**URL**: https://discourse.slicer.org/t/add-a-keyboard-shortcut-to-close-the-application/42615

---

## Post #1 by @chir.set (2025-04-18 15:13 UTC)

<p>Many applications can be closed by the “CTRL + Q” keyboard shortcut. This combination does not seem to be used in Slicer. I am aware that custom keyboard shortcuts can be assigned, just wondering if it could be built-in.</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2025-04-18 18:02 UTC)

<p>On mac, Cmd-Q can be used to quit Slicer.</p>
<p>On windows, and I think on most if not all linux machines, you should be able to do Alt-F then x.  Alt-F brings up the file menu with the x underlined (this is a pretty general pattern for using menus on non-mac systems).  Adding Control-Q would be okay, but maybe redundant.</p>

---

## Post #3 by @chir.set (2025-04-18 18:39 UTC)

<p>ALT+F and x is simple enough on Linux, thank you <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=14" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2025-04-19 12:48 UTC)

<p>We use standard Qt shortcuts - <a href="https://doc.qt.io/qt-6/qkeysequence.html#standard-shortcuts" class="inline-onebox">QKeySequence Class | Qt GUI | Qt 6.9.0</a><br>
According to the table, Ctrl-Q should work on Linux (at least with KDE and Plasma). If you have a debug-mode build and installed Qt debug symbols then you can debug into why Ctrl-Q is not working or what other shortcut is assigned to the <code>Quit</code> action.</p>

---

## Post #5 by @chir.set (2025-04-19 18:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="42615">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>and installed Qt debug symbols</p>
</blockquote>
</aside>
<p>I’ll investigate that ASAP, thank you.</p>

---
