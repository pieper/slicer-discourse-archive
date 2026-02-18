# Multiple choice dialog

**Topic ID**: 13006
**Date**: 2020-08-14
**URL**: https://discourse.slicer.org/t/multiple-choice-dialog/13006

---

## Post #1 by @rohan_n (2020-08-14 20:20 UTC)

<p>Does slicer have any method that’s very similar to the<br>
<code>slicer.util.</code> <code>confirmYesNoDisplay</code><br>
but instead of being just Yes or No, you can add custom number of buttons and give the buttons any labels you want? If so, syntax and example of how it’s used would be really helpful.<br>
Thanks,<br>
Rohan Nadkarni</p>

---

## Post #2 by @pieper (2020-08-14 20:35 UTC)

<p>If Slicer doesn’t have exactly what you need, then usually it’s easy to make something custom with QDialog.  If you think there’s a general purpose feature that would be good to add to slicer.util a PR would be welcome.</p>
<p><a href="https://doc.qt.io/qt-5/qdialog.html" class="onebox" target="_blank">https://doc.qt.io/qt-5/qdialog.html</a></p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/e4557d1f5ebeb96e5577f46d8ad89cce3601ace2/Base/Python/slicer/util.py#L1966-L1974" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/e4557d1f5ebeb96e5577f46d8ad89cce3601ace2/Base/Python/slicer/util.py#L1966-L1974" target="_blank" rel="noopener">Slicer/Slicer/blob/e4557d1f5ebeb96e5577f46d8ad89cce3601ace2/Base/Python/slicer/util.py#L1966-L1974</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="1966" style="counter-reset: li-counter 1965 ;">
<li>def confirmYesNoDisplay(text, windowTitle=None, parent=None, **kwargs):</li>
<li>  """Display an confirmation popup. Return if confirmed with Yes.</li>
<li>  """</li>
<li>  import qt, slicer</li>
<li>  if not windowTitle:</li>
<li>    windowTitle = slicer.app.applicationName + " confirmation"</li>
<li>  result = messageBox(text, parent=parent, windowTitle=windowTitle, icon=qt.QMessageBox.Question,</li>
<li>                       standardButtons=qt.QMessageBox.Yes | qt.QMessageBox.No, **kwargs)</li>
<li>  return result == qt.QMessageBox.Yes</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @rohan_n (2020-08-14 20:42 UTC)

<p>Ok, I’ll try that out</p>

---

## Post #4 by @lassoan (2020-08-15 03:51 UTC)

<p><a href="https://doc.qt.io/qt-5/qmessagebox.html">QMessageBox</a> has many options, you can define custom buttons, too. You can search for QMessageBox and ctkMessageBox in .py files in Slicer source code to see examples.</p>

---
