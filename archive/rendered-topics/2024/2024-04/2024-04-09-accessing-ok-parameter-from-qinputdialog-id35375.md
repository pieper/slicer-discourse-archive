# Accessing 'ok' parameter from QInputDialog

**Topic ID**: 35375
**Date**: 2024-04-09
**URL**: https://discourse.slicer.org/t/accessing-ok-parameter-from-qinputdialog/35375

---

## Post #1 by @bruce (2024-04-09 02:00 UTC)

<p>Hello,<br>
I’m using a simple input dialog to get a user choice from a list but need to determine if the Cancel button has been pushed. I understand slicer uses PythonQt and it looks like PythonQt provides a BoolResult type to do this. However, I haven’t been able to get this working. The following code just causes slicer to crash.</p>
<pre data-code-wrap="python"><code class="lang-python">result = PythonQt.BoolResult()
item = qt.QInputDialog().getItem(None, "MyTitle", "Enter text", ['Choice1', 'Choice2'], ok=result)
</code></pre>
<p>Any help would be appreciated.</p>

---

## Post #2 by @lassoan (2024-04-09 03:33 UTC)

<p>It was quite close. This works:</p>
<pre data-code-wrap="python"><code class="lang-python">import PythonQt
selectionSuccess = PythonQt.BoolResult()
selectedItem = PythonQt.QtGui.QInputDialog().getItem(None, "MyTitle", "Label", ['Choice1', 'Choice2'], 1, True, selectionSuccess)
</code></pre>
<p>Note that popup windows are generally very annoying for users and should only be used in exceptional cases. I would recommend to add these widgets to your module’s GUI panel instead (by using Qt Designer).</p>

---

## Post #3 by @bruce (2024-04-11 03:03 UTC)

<p>Perfect. Thank you.<br>
Yes, popup window is only to cater for low traffic pathway through the workflow (trying to avoid cluttering the module pane).</p>

---
