---
topic_id: 34668
title: "Calling Surfacetoolbox Logic Programatically"
date: 2024-03-03
url: https://discourse.slicer.org/t/34668
---

# Calling SurfaceToolBox Logic Programatically

**Topic ID**: 34668
**Date**: 2024-03-03
**URL**: https://discourse.slicer.org/t/calling-surfacetoolbox-logic-programatically/34668

---

## Post #1 by @oothomas (2024-03-03 03:18 UTC)

<p>Hello everyone,</p>
<p>I’ve been working on automating the cleaning of polygon models derived from segmentations and encountered a stumbling block. Specifically, I’m having trouble utilizing the logic from the SurfaceToolbox module within my script. To verify the functionality of my script, I directly integrated the logic portion of the SurfaceToolbox, after which everything worked as expected. This indicates that the rest of my script is operational.</p>
<p>However, when I attempt to call the SurfaceToolbox module’s logic in the same manner as I successfully do with other modules, it doesn’t seem to work. Here’s a snippet of how I’m trying to access the logic:</p>
<p>pythonCopy code</p>
<pre><code class="lang-auto">surfaceToolboxLogic = slicer.modules.surfacetoolbox.logic()
</code></pre>
<p>I’m curious if there’s a known issue or a particular nuance in accessing the logic of the SurfaceToolbox module that I might be missing. Has anyone else experienced similar issues or can provide insights into what might be going wrong?</p>
<p>Thank you in advance for your time and assistance. I’m looking forward to any suggestions or guidance you can offer.</p>
<p>Best regards,</p>
<p>Oshane O. Thomas</p>
<pre><code class="lang-auto">    def cleanAndRemeshModel(inputModelNode, desiredNumberOfTriangles):
        """
        Cleans the input model node and applies remeshing to achieve a specific number of triangles.
        Automatically creates and returns an output model node based on the input model node.

        Args:
            inputModelNode (vtkMRMLModelNode): The input model node to process.
            desiredNumberOfTriangles (int): The desired number of triangles in the remeshed model.

        Returns:
            vtkMRMLModelNode: The output model node containing the cleaned and remeshed model.
        """
        if not inputModelNode:
            raise ValueError("An input model node must be provided")

        # Ensure the pyacvd package is installed for remeshing
        if not SurfaceToolboxLogic.installRemeshPrerequisites(force=True):
            raise ImportError("Required 'pyacvd' package could not be installed.")

        # Create a new model node for the output
        outputModelNode = slicer.vtkMRMLModelNode()
        outputModelNode.SetName(inputModelNode.GetName() + "_cleanedRemeshed")
        slicer.mrmlScene.AddNode(outputModelNode)

        # Copy the display properties from the input model to the output model
        outputModelDisplay = slicer.vtkMRMLModelDisplayNode()
        slicer.mrmlScene.AddNode(outputModelDisplay)
        outputModelNode.SetAndObserveDisplayNodeID(outputModelDisplay.GetID())
        if inputModelNode.GetDisplayNode():
            outputModelDisplay.Copy(inputModelNode.GetDisplayNode())

        # Clean the input model
        logging.info("Cleaning the model...")

        surfaceToolboxLogic = slicer.modules.surfacetoolbox.logic()

        SurfaceToolboxLogic.clean(inputModelNode, outputModelNode)

        # Calculate the clusters value for the desired number of triangles.
        # The number of clusters (points) in pyacvd is roughly half the number of triangles desired.
        clusters = desiredNumberOfTriangles // 2

        # Apply remeshing
        logging.info("Remeshing the model to approximately {} triangles...".format(desiredNumberOfTriangles))
        SurfaceToolboxLogic.remesh(outputModelNode, outputModelNode, clusters=clusters)

        print("Model cleaning and remeshing completed.")

        return outputModelNode
</code></pre>

---

## Post #2 by @chir.set (2024-03-03 06:58 UTC)

<p>For Python modules:</p>
<pre><code class="lang-auto">import SurfaceToolbox
surfaceToolboxLogic = SurfaceToolbox.SurfaceToolboxLogic()
</code></pre>
<p>N.B. - It’s written <em>SurfaceToolbox</em> and not <em>SurfaceToolBox</em>.</p>

---
