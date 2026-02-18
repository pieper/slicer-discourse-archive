# Issue with Generating Specific Isodose Surface using the Isodose Module in Python Interactor

**Topic ID**: 41826
**Date**: 2025-02-22
**URL**: https://discourse.slicer.org/t/issue-with-generating-specific-isodose-surface-using-the-isodose-module-in-python-interactor/41826

---

## Post #1 by @shahrokh (2025-02-22 13:20 UTC)

<p>Hello Dear Developers and Users</p>
<p>Sorry for asking my question again. In the question I asked titled “<a href="https://discourse.slicer.org/t/is-it-better-to-integrate-settings-from-module-b-into-module-a-for-improved-user-workflow-or-user-convenience/41189">Is it better to integrate settings from Module B into Module A for improved user workflow (or user convenience)</a>?” in the <strong>Development Category</strong>, I was trying to run the Isodose module through the Python Interactor in such a way that an Isodose surface for <strong>47.00 Gy</strong> would be generated. The commands are as follows:</p>
<pre><code class="lang-auto"># Get the dose volume node by class and name
doseVolumeNode = slicer.util.getFirstNodeByClassByName('vtkMRMLScalarVolumeNode', '2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1')

# Create a new Isodose node instance for displaying isodose surfaces
object_vtkMRMLIsodoseNode = slicer.vtkMRMLIsodoseNode().CreateNodeInstance()

# Set the scene for the isodose node to match the dose volume node's scene
object_vtkMRMLIsodoseNode.SetScene(doseVolumeNode.GetScene())

# Set the dose units to Gray (Gy)
object_vtkMRMLIsodoseNode.SetDoseUnits(slicer.vtkMRMLIsodoseNode.Gy)

# Set the reference dose value (in Gy) for isodose levels
object_vtkMRMLIsodoseNode.SetReferenceDoseValue(47.00)

# Observe the dose volume node to track its changes
object_vtkMRMLIsodoseNode.SetAndObserveDoseVolumeNode(doseVolumeNode)

# Setup the color table for the isodose node based on the dose volume
slicer.modules.isodose.logic().SetupColorTableNodeForDoseVolumeNode(doseVolumeNode)
#slicer.util.getModuleLogic('Isodose').SetupColorTableNodeForDoseVolumeNode(doseVolumeNode)

# Create isodose surfaces based on the configured isodose node
slicer.modules.isodose.logic().CreateIsodoseSurfaces(object_vtkMRMLIsodoseNode)
</code></pre>
<p>The result of running these commands can be seen in the image below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b810039b698cf072b21cc38fbf409846be67f0fe.png" data-download-href="/uploads/short-url/qgiacH0J9PVsXZs4c4cUiQMIVTE.png?dl=1" title="Screenshot from 2025-02-22 11-55-48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b810039b698cf072b21cc38fbf409846be67f0fe_2_690x394.png" alt="Screenshot from 2025-02-22 11-55-48" data-base62-sha1="qgiacH0J9PVsXZs4c4cUiQMIVTE" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b810039b698cf072b21cc38fbf409846be67f0fe_2_690x394.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b810039b698cf072b21cc38fbf409846be67f0fe_2_1035x591.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b810039b698cf072b21cc38fbf409846be67f0fe_2_1380x788.png 2x" data-dominant-color="E3E3EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-02-22 11-55-48</span><span class="informations">1844×1055 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As seen in this image, contrary to my expectation, where only the Isodose surface for the 47.00 Gy dose should have been generated, Isodose surfaces for the 5, 10, 15, 20, 25, and 30 Gy doses have also been generated.<br>
Please guide me on what mistake might be in my commands that caused the Isodose surface for the 47.00 Gy dose not to be generated.</p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #2 by @shahrokh (2025-04-07 11:35 UTC)

<p>I finally was able to generate specific isodose levels, like 30 and 47 Gy, using Python Interactor. For this, I executed the following commands:</p>
<pre><code class="lang-auto"># Get the dose volume node by class and name
doseVolumeNode = slicer.util.getFirstNodeByClassByName('vtkMRMLScalarVolumeNode', '2: RTDOSE: DOSIsoft:RTDOSE:Phase #1 Dosi Dosi 1: Beam setup 1 (GY) [11]: Beam setup 1')

# Create a new Isodose node instance for displaying isodose surfaces
object_vtkMRMLIsodoseNode = slicer.vtkMRMLIsodoseNode().CreateNodeInstance()

# Set the scene for the isodose node to match the dose volume node's scene
object_vtkMRMLIsodoseNode.SetScene(doseVolumeNode.GetScene())

# Set the dose units to Gray (Gy)
object_vtkMRMLIsodoseNode.SetDoseUnits(slicer.vtkMRMLIsodoseNode.Gy)

# Observe the dose volume node to track its changes
object_vtkMRMLIsodoseNode.SetAndObserveDoseVolumeNode(doseVolumeNode)

# Setup the color table for the dose volume node with two colors
slicer.modules.isodose.logic().SetupColorTableNodeForDoseVolumeNode(doseVolumeNode).SetNumberOfColors(2)

# Define the color for the first isodose surface (47 Gy)
slicer.modules.isodose.logic().SetupColorTableNodeForDoseVolumeNode(doseVolumeNode).SetColor(0, "47", 0.6, 0.9, 2.0, 0.6)

# Define the color for the second isodose surface (30 Gy)
slicer.modules.isodose.logic().SetupColorTableNodeForDoseVolumeNode(doseVolumeNode).SetColor(1, "30", 0.4, 0.2, 0.4, 0.4)

# Create isodose surfaces based on the defined settings
slicer.modules.isodose.logic().CreateIsodoseSurfaces(object_vtkMRMLIsodoseNode)
</code></pre>
<p>The result of these commands in 3DSlicer is shown in the figure below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6301d81a256479102950060db5508cff0dc89d26.png" data-download-href="/uploads/short-url/e7RdG9Yck7AKj20uewFZdVqAlb8.png?dl=1" title="Screenshot from 2025-04-07 15-04-10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6301d81a256479102950060db5508cff0dc89d26_2_690x393.png" alt="Screenshot from 2025-04-07 15-04-10" data-base62-sha1="e7RdG9Yck7AKj20uewFZdVqAlb8" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6301d81a256479102950060db5508cff0dc89d26_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6301d81a256479102950060db5508cff0dc89d26_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6301d81a256479102950060db5508cff0dc89d26_2_1380x786.png 2x" data-dominant-color="D2D3DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-04-07 15-04-10</span><span class="informations">1849×1054 387 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards.<br>
Shahrokh</p>

---
