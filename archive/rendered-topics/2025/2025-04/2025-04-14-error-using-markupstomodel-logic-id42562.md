---
topic_id: 42562
title: "Error Using Markupstomodel Logic"
date: 2025-04-14
url: https://discourse.slicer.org/t/42562
---

# Error using MarkupsToModel Logic

**Topic ID**: 42562
**Date**: 2025-04-14
**URL**: https://discourse.slicer.org/t/error-using-markupstomodel-logic/42562

---

## Post #1 by @bloem1412 (2025-04-14 16:52 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.8.0<br>
I’m using the MarkupsToModel logic in my own module to make a closed surface model of a list of fiducials. My code has the desired effect, when I click the button in my module, a closed surface of the fiducials is created and visible.<br>
Even though it is functioning, I get an error in the console:<br>
[VTK] No output model node provided to UpdateOutputModel. No operation performed.<br>
I tried to define the output model node more explicitely, but to no effect.<br>
Is there a way to prevent this error or should I just ignore it since it doesn’t seem to affect the function?</p>
<p>My code:</p>
<pre data-code-wrap="python"><code class="lang-python"># Create a new model node for the output
outputModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode", outputModelName)
outputModelNode.CreateDefaultDisplayNodes()            
# Create a new MarkupsToModel node
markupsToModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsToModelNode")
# Set the input node (annotationNode)
         markupsToModelNode.SetAndObserveInputNodeID(self._parameterNode.annotationNode.GetID())
markupsToModelNode.SetAndObserveOutputModelNodeID(outputModelNode.GetID())
# Ensure the model is visible in 3D
outputModelNode.GetDisplayNode().SetVisibility(True)

markupsToModelLogic = slicer.modules.markupstomodel.logic()
         markupsToModelNode.SetModelType(slicer.vtkMRMLMarkupsToModelNode.ClosedSurface) 
markupsToModelNode.SetAutoUpdateOutput(False)  # Automatically update the model
            
# Trigger the model creation
markupsToModelLogic.UpdateOutputModel(markupsToModelNode)
</code></pre>

---
