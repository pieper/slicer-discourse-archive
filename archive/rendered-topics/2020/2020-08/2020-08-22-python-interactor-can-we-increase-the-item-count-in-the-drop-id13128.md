---
topic_id: 13128
title: "Python Interactor Can We Increase The Item Count In The Drop"
date: 2020-08-22
url: https://discourse.slicer.org/t/13128
---

# Python interactor : can we increase the item count in the dropdown list?

**Topic ID**: 13128
**Date**: 2020-08-22
**URL**: https://discourse.slicer.org/t/python-interactor-can-we-increase-the-item-count-in-the-dropdown-list/13128

---

## Post #1 by @chir.set (2020-08-22 09:53 UTC)

<p>Currently, the dropdown list on TAB key press in the python interactor shows 7 items. Can one increase the number of items to, say, 16 ? By some python code in slicerrc.py ? Just for less scrolling.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2020-08-22 18:01 UTC)

<p>Good idea. I’ve added a new Python-accessible method to set this (available in Slicer Preview Release from tomorrow):</p>
<pre><code>slicer.app.pythonConsole().maxVisibleCompleterItems = 20</code></pre>

---

## Post #3 by @chir.set (2020-08-22 18:36 UTC)

<p>Great, I’ll rebuild tomorrow and drop this line in slicerrc.py.</p>
<p>[By the way, since the recent changes regarding dark mode, the python interactor does adopt the dark mode now, that’s less eye straining. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">]</p>
<p>Thanks.</p>

---
