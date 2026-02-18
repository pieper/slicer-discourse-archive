# GetDisplayNode returns 'NoneType' after I create manually a Node

**Topic ID**: 11863
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/getdisplaynode-returns-nonetype-after-i-create-manually-a-node/11863

---

## Post #1 by @siaeleni (2020-06-04 16:40 UTC)

<p>Hi All,</p>
<p>I create a qMRMLNodeComboBox using following code:</p>
<blockquote>
<pre><code>self.outputSelector = slicer.qMRMLNodeComboBox()
self.outputSelector.nodeTypes = ["vtkMRMLModelNode"]
self.outputSelector.selectNodeUponCreation = True
self.outputSelector.addEnabled = True
self.outputSelector.removeEnabled = True
self.outputSelector.noneEnabled = True
self.outputSelector.renameEnabled = True
self.outputSelector.showHidden = False
self.outputSelector.showChildNodeTypes = False
self.outputSelector.setMRMLScene(slicer.mrmlScene)
</code></pre>
</blockquote>
<p>After creating manually a new Model from UI, I try to make the model visible by using:</p>
<blockquote>
<p>node = slicer.util.getNode(‘Model’)<br>
d = node.GetDisplayNode()</p>
</blockquote>
<p>but type(d) = NoneType</p>
<p>I am not sure how can I make it visible.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-06-04 17:02 UTC)

<p>After you add a data node to the scene and set its content, you need to add display node to show it in views. The simplest is to call <code>CreateDefaultDisplayNodes()</code>.</p>

---
