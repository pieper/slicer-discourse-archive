---
topic_id: 4355
title: "Copy Model Display Node"
date: 2018-10-11
url: https://discourse.slicer.org/t/4355
---

# Copy model display node

**Topic ID**: 4355
**Date**: 2018-10-11
**URL**: https://discourse.slicer.org/t/copy-model-display-node/4355

---

## Post #1 by @Niels (2018-10-11 08:28 UTC)

<p>I have a generated a new model derived from a source model. I want the new display properties (including selected scalars) of the target model to be the same as the source model. I tried various Copy functions with no success.</p>
<pre><code>modelDisplayNode = modelNode.GetDisplayNode()
    
newModel1 = slicer.vtkMRMLModelNode()
newModel1.SetAndObservePolyData(surfaceFilter1.GetOutput())

newDisplayNode1 = slicer.vtkMRMLModelDisplayNode()
newDisplayNode1.CopyWithScene(modelDisplayNode)
slicer.mrmlScene.AddNode(newDisplayNode1)
    
newModel1.SetAndObserveDisplayNodeID(newDisplayNode1.GetID())
slicer.mrmlScene.AddNode(newModel1)</code></pre>

---

## Post #2 by @lassoan (2018-10-11 12:52 UTC)

<p>Simple <code>Copy</code> of the display node should work:</p>
<pre><code>newModel1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
newModel1.SetAndObservePolyData(surfaceFilter1.GetOutput()))
newModel1.CreateDefaultDisplayNodes()
newModel1.GetDisplayNode().Copy(modelNode.GetDisplayNode())
</code></pre>
<p>A more generic option is to use Subject Hierarchy module’s clone function, which can clone any node. See this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Clone_a_node">example</a>.</p>

---
