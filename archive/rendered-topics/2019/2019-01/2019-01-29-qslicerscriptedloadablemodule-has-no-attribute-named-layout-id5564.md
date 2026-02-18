# qSlicerScriptedLoadableModule has no attribute named 'layout'?

**Topic ID**: 5564
**Date**: 2019-01-29
**URL**: https://discourse.slicer.org/t/qslicerscriptedloadablemodule-has-no-attribute-named-layout/5564

---

## Post #1 by @timeanddoctor (2019-01-29 16:08 UTC)

<pre><code>def setup(self):
    ScriptedLoadableModuleWidget.setup(self)
    # Joint collapsible button
    jointcollapsibleButton = ctk.ctkCollapsibleButton()
    jointcollapsibleButton.text = "Joints"
    #jointcollapsibleButton.enabled = False
    self.layout.addWidget(jointcollapsibleButton)
</code></pre>
<p>I try to write a py module like upper code. But when I add to slicer. I get an error:<br>
Traceback (most recent call last):</p>
<p>File "D:\Program Files\Slicer 4.11.0-2018-12-16\bin\Python\slicer\ScriptedLoadableModule.py", line 87, in <strong>init</strong></p>
<p>self.layout = self.parent.layout()</p>
<p>AttributeError: qSlicerScriptedLoadableModule has no attribute named ‘layout’</p>

---

## Post #2 by @lassoan (2019-01-30 01:18 UTC)

<p>Can you find another error in the error log before this?<br>
Make sure you follow the latest extension module template (that works well).</p>

---
