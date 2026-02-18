# How to get InformationPane from Models Module in Python

**Topic ID**: 10808
**Date**: 2020-03-24
**URL**: https://discourse.slicer.org/t/how-to-get-informationpane-from-models-module-in-python/10808

---

## Post #1 by @siaeleni (2020-03-24 00:16 UTC)

<p>Hello,</p>
<p>I would like to get some information from the “Information Panel” at the models module, like Volume or Surface Area for example. I know how to get info from the Display panel but I am not sure how to get from the Information panel.</p>
<p>Thanks,<br>
Eleni</p>

---

## Post #2 by @lassoan (2020-03-24 01:43 UTC)

<p>Model information is shown by a <code>qMRMLModelInfoWidget</code>. For example:</p>
<pre><code class="lang-python">w = slicer.qMRMLModelInfoWidget()
w.setMRMLModelNode(myModelNode)
w.show()
</code></pre>
<p>If you don’t need a widget just the numbers, then you can get it <a href="https://github.com/Slicer/Slicer/blob/9223190f0075b3bac400fe36dac4ba3a033b154f/Libs/MRML/Widgets/qMRMLModelInfoWidget.cxx#L151-L158">as it is done in the widget</a>.</p>

---
