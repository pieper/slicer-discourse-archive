---
topic_id: 19190
title: "Changing Cursor During Long Running Script"
date: 2021-08-14
url: https://discourse.slicer.org/t/19190
---

# Changing cursor during long running script

**Topic ID**: 19190
**Date**: 2021-08-14
**URL**: https://discourse.slicer.org/t/changing-cursor-during-long-running-script/19190

---

## Post #1 by @ezgimercan (2021-08-14 00:38 UTC)

<p>Is there a way to change the cursor to spinning pinwheel when a long running function is called after a button is pressed in a scripted module? Right now the UI freezes until the function returns but no visual feedback to the user. Thanks.</p>

---

## Post #2 by @mau_igna_06 (2021-08-14 09:15 UTC)

<p>I think this should work:</p>
<pre><code class="lang-auto">qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)
myFunctionThatTakesLongToExecute()
qt.QApplication.restoreOverrideCursor()
</code></pre>

---
