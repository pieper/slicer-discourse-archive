---
topic_id: 32650
title: "Keyboard Shortcut Assigned To A Push Button"
date: 2023-11-07
url: https://discourse.slicer.org/t/32650
---

# Keyboard shortcut assigned to a push button

**Topic ID**: 32650
**Date**: 2023-11-07
**URL**: https://discourse.slicer.org/t/keyboard-shortcut-assigned-to-a-push-button/32650

---

## Post #1 by @laurentletg (2023-11-07 20:50 UTC)

<p>Hello,</p>
<p>I’ve seen examples of how to assign keyboard shortcuts in the forum and the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts" rel="noopener nofollow ugc">script repository.</a> I was wondering if there is a quick way to simply assign a keyboard shortcut to an existing push button (without necessarily calling a function). The idea is to use the shortcut as an alternative to clicking the push button.</p>
<p>For example, in Qt for Python it is possible to assign a shortcut to a button using button.setShortcut(). Unless I made an error somewhere, I was not able to replicate this in a custom slicer module.</p>
<pre><code class="lang-auto"># Example with PySide6
from PySide6.QtGui import QKeySequence

###...other lines here...
# Set the shortcut to Ctrl+B (for example)
self.button.setShortcut(QKeySequence("Ctrl+B"))
</code></pre>
<p>Thanks!</p>

---
