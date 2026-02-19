---
topic_id: 31376
title: "Set Dynamic Modeler Attributes With Python"
date: 2023-08-26
url: https://discourse.slicer.org/t/31376
---

# Set Dynamic Modeler Attributes with python

**Topic ID**: 31376
**Date**: 2023-08-26
**URL**: https://discourse.slicer.org/t/set-dynamic-modeler-attributes-with-python/31376

---

## Post #1 by @Caetox (2023-08-26 10:47 UTC)

<p>I am using the Dynamic Modeler Module in my python script.<br>
For the ROI Cut Tool, I set the input model, input ROI and output model and so far this works perfectly.<br>
But I want the surface to be capped. In the Dynamic Modeler widget there is an option “Cap surface” with a checkbox. How can I set this attribute with python?<br>
I figured out how to set the attributes:</p>
<blockquote>
<p>dynamicModelerNode.SetAttribute(“ROICut.CapSurface”, _ )</p>
</blockquote>
<p>but what value do i need to put to make it work? It only takes a string.</p>
<p>I tried finding the attributes with their possible values like this:</p>
<blockquote>
<p>roiCutTool = slicer.vtkSlicerDynamicModelerROICutTool()<br>
for i in range(roiCutTool.GetNumberOfInputParameters()):<br>
print(roiCutTool.GetNthInputParameterAttributeName(i))<br>
print(roiCutTool.GetNthInputParameterName(i))<br>
print(roiCutTool.GetNthInputParameterPossibleValues(i))<br>
print(roiCutTool.GetNthInputParameterDescription(i))</p>
</blockquote>
<p>but for the possible values of ROICut.CapSurface, it returns None.</p>

---

## Post #2 by @cpinter (2023-08-28 09:34 UTC)

<p>This should work:</p>
<pre><code class="lang-auto">dynamicModelerNode.SetAttribute('ROICut.CapSurface', '1')
</code></pre>
<p>FYI the way I found it out was that I printed the content of the ROI cut parameter node. It gave me this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; print(dynamicModelerNode)
vtkMRMLDynamicModelerNode (0000026506838D10)
  ID: vtkMRMLDynamicModelerNode1
  ClassName: vtkMRMLDynamicModelerNode
  Name: ROI cut
  Debug: false
  MTime: 278225
  Description: (none)
  SingletonTag: (none)
  HideFromEditors: false
  Selectable: true
  Selected: false
  UndoEnabled: false
  Attributes:
    ROICut.CapSurface:1
  Node references:
    ROICut.InputModel: (none)
    ROICut.InputROI: (none)
    ROICut.OutputNegativeModel: (none)
    ROICut.OutputPositiveModel: (none)
  ToolName: ROI cut
  ContinuousUpdate: false
</code></pre>

---
