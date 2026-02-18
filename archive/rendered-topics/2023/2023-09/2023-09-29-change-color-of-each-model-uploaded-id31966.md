# Change color of each model uploaded

**Topic ID**: 31966
**Date**: 2023-09-29
**URL**: https://discourse.slicer.org/t/change-color-of-each-model-uploaded/31966

---

## Post #1 by @CharNamIII (2023-09-29 15:04 UTC)

<p>Hi,</p>
<p>Is there a way to give each model a unique color when uploaded to 3DSlicer? They all come out the same color if I upload them all at once and changing them one by one takes a long time!</p>

---

## Post #2 by @muratmaga (2023-09-30 01:23 UTC)

<p>This is easy to do via scripting, and I don’t think there is a way through UI. Interestingly enough, I couldn’t find an example of changing a color of a model node in script repository. But ChatGPT has quite helpful with the question:<br>
<code>how can I change the color of a model node in 3D slicer with python?</code></p>
<p>It gave me this non-functional (with extraneous stuff in it) example.</p>
<pre><code class="lang-auto">import slicer
import vtk

# Get the model node by name
model_node = slicer.util.getNodeByName("YourModelNodeName")

# Create a color table node
color_table_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLColorTableNode")

# Define the color (e.g., red)
color = vtk.vtkUnsignedCharArray()
color.SetNumberOfComponents(3)
color.InsertNextTuple3(255, 0, 0)

# Set the color of the model node
model_node.GetDisplayNode().SetColor(color_table_node.GetColorIndex(color))

# Update the 3D view
slicer.util.resetFiducialsMarkersColor()
</code></pre>
<p>But it has enough pointers. So it was easy change it into this, in which the model node is called A.</p>
<pre><code class="lang-auto">import slicer

# Get the model node by name
model_node = slicer.util.getNode("A")

# Set the color of the model node
model_node.GetDisplayNode().SetColor(255,255,0)
</code></pre>
<p>you can then modify this example with your models and change their colors as you which by specifying their RGB codes.</p>

---

## Post #3 by @CharNamIII (2023-09-30 10:46 UTC)

<p>Hi,</p>
<p>Thanks for this! Interesting way of using ChatGPT!</p>

---
