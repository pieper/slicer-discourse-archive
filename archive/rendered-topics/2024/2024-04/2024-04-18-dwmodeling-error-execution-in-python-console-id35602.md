---
topic_id: 35602
title: "Dwmodeling Error Execution In Python Console"
date: 2024-04-18
url: https://discourse.slicer.org/t/35602
---

# DWModeling error execution in Python console

**Topic ID**: 35602
**Date**: 2024-04-18
**URL**: https://discourse.slicer.org/t/dwmodeling-error-execution-in-python-console/35602

---

## Post #1 by @smati_wissem (2024-04-18 14:32 UTC)

<p>Hello everyone,</p>
<p>I’ve created this code to execute DWModeling in the Python console, but it appears that I’m encountering an issue assigning parameters to the model. Could someone please help me?</p>
<p>Thank you.<br>
def runDWModeling(inputVolumeNode):<br>
“”“Run diffusion weighting modeling from an input volume node.”“”<br>
# Check if the inputVolumeNode is valid<br>
if inputVolumeNode is None:<br>
raise ValueError(“The input volume node is None. Please check the node ID.”)</p>
<pre><code># Set parameters
parameters = {}
parameters["Input image"] = inputVolumeNode.GetID()  # Adjusted parameter name
if not parameters["Input image"]:
    raise ValueError("Failed to get a valid ID from the input volume node. Check if the node is correct.")

outputModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")
parameters["MonoExp diffusion map"] = outputModelNode
parameters["modelName"] = "MonoExponential"

# Setup the CLI module
dwModelingLogic = slicer.modules.dwmodeling

# Execute the CLI module
cliNode = slicer.cli.runSync(slicer.modules.dwmodeling, None, parameters)

# Process results
if cliNode.GetStatus() &amp; cliNode.ErrorsMask:
    # Handle errors
    errorText = cliNode.GetErrorText()
    slicer.mrmlScene.RemoveNode(cliNode)
    raise ValueError("CLI execution failed: " + errorText)

# Success, cleanup
slicer.mrmlScene.RemoveNode(cliNode)
print("Modeling completed successfully.")
return cliNode
</code></pre>
<h1><a name="p-109812-usage-1" class="anchor" href="#p-109812-usage-1" aria-label="Heading link"></a>usage:</h1>
<p>try:<br>
inputVolumeNode = slicer.util.getNode(‘vtkMRMLMultiVolumeNode1’)<br>
if not inputVolumeNode:<br>
raise Exception(“Node not found. Please check the node ID.”)<br>
modelNode = runDWModeling(inputVolumeNode)</p>
<p>except Exception as e:<br>
print(str(e))</p>
<p>Thank you.</p>

---
