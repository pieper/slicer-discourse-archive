# How to use a widget in my module

**Topic ID**: 14756
**Date**: 2020-11-24
**URL**: https://discourse.slicer.org/t/how-to-use-a-widget-in-my-module/14756

---

## Post #1 by @ond12 (2020-11-24 14:18 UTC)

<p>Hello,</p>
<p>I added a “qMRMLVolumeThresholdWidget” in my module thanks to qt designer.<br>
But the slider is grey and i can’t modify the Threshold.</p>
<p>How can i interact with a widget this type ?</p>
<p>Thanks for your help</p>

---

## Post #2 by @jamesobutler (2020-11-24 21:18 UTC)

<p><a href="https://apidocs.slicer.org/master/classqMRMLVolumeThresholdWidget.html" rel="noopener nofollow ugc">qMRMLVolumeThresholdWidget</a> inherits from <a href="https://apidocs.slicer.org/master/classqMRMLVolumeWidget.html" rel="noopener nofollow ugc">qMRMLVolumeWidget</a> which requires a MRML volume to be set.</p>
<pre><code class="lang-python"># Get a node from SampleData that we will clone
import SampleData
volume_node = SampleData.SampleDataLogic().downloadMRHead()
volume_threshold_widget = slicer.qMRMLVolumeThresholdWidget()
volume_threshold_widget.setMRMLVolumeNode(volume_node)
volume_threshold_widget.show()
</code></pre>

---
