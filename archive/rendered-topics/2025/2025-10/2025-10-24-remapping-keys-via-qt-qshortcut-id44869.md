# Remapping keys via qt.QShortcut()

**Topic ID**: 44869
**Date**: 2025-10-24
**URL**: https://discourse.slicer.org/t/remapping-keys-via-qt-qshortcut/44869

---

## Post #1 by @tas47 (2025-10-24 13:02 UTC)

<p>Hello all,<br>
I was wondering if there was anyway to remap shortcut keys that are already used:<br>
example say Ctrl+9 is already used for another shortcut or maybe not available: is there a way to free it up and  remap  to the a function?  Given function useHangingProtocolPetCT</p>
<pre data-code-wrap="shortcut"><code class="lang-shortcut">shortcut.setKey(qt.QKeySequence("Ctrl+9"))
shortcut.connect( "activated()", useHangingProtocolPetCt)```

Thank you,</code></pre>

---

## Post #2 by @lassoan (2025-10-25 14:54 UTC)

<p>This should not be hard to do, as Slicer exposes the full Qt API in Python. You can look up the Qt documentarion or ask chatbots about how to do it exactly, but it should be something like finding the shortcut or action object and then change the keyboard shortcut (and then you can add a new one) or add a new shortcut with a more specific context or install an event filter.</p>

---
