# Exporting decimated vtkPolyData

**Topic ID**: 12036
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/exporting-decimated-vtkpolydata/12036

---

## Post #1 by @Queen_Rei (2020-06-15 15:49 UTC)

<p>My current objective is to decimate a segmentation and export it. I have been looking around for the proper way to do this with vtkDecimatePro and the vtkSegmentationNode. I wanted to know how I may export this decimated data. Thank you for any and all advice!</p>
<pre><code>        # Decimate Closed Surface Representation
        decimate = vtk.vtkDecimatePro()
        decimate.SetInputData(segmentationNode.GetSegmentation().GetLayerDataObject(0))
        decimate.SetTargetReduction(.90)
        decimate.Update()

        decimated = vtk.vtkPolyData()
        decimated.ShallowCopy(decimate.GetOutput())

        # Send segment to output folder
        # TODO create text box for output folder
        segmentIDs = vtk.vtkStringArray()
        segmentIDs.InsertNextValue(segmentTypeID)
        slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles(outputFolder, segmentationNode, segmentIDs, "OBJ", True, 1.0, False)
</code></pre>
<p>Would using AddSegmentFromClosedSurfaceRepresentation() to add the decimated segmentation be a good approach or just redundant?</p>

---

## Post #2 by @Queen_Rei (2020-06-16 03:35 UTC)

<p>Ohh and I would like to export it as an OBJ. I don’t want to do go deep into a method that isn’t efficient. Looking for any guidance <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #3 by @lassoan (2020-06-16 04:01 UTC)

<p>You can export segments to models, run extra mesh simplification or smoothing steps using Surface toolbox module, then use File / Save to save the models as .obj files.</p>
<p>“Export to files” is a convenience feature to save you the extra step of exporting segments to models. But if you export segments to models anyway because you want to do further processing, then segmentation “Export to files” does not simplify things.</p>

---

## Post #4 by @Queen_Rei (2020-06-16 19:22 UTC)

<p>Thanks for the advice, always helps! I got this going, but when I try and do decimate.Update() it seems to crash my slicer.exe. I am investigating it now and when I look for .Update() for vtkOBJWriter, vtkDecimatePro, etc… I can’t seem to find it. I’ll keep looking around to see what I can find. This is what I made up so far.</p>
<pre><code>    # Export Segmentation to Model Node
    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "Segments")
    slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, exportFolderItemId)

    # Decimate Model
    surfaceMesh = segmentationNode.GetClosedSurfaceInternalRepresentation(segmentTypeID)
    decimate = vtk.vtkDecimatePro()
    decimate.SetTargetReduction(.90)
    decimate.SetInputData(surfaceMesh)
    decimate.Update()
    surfaceMesh = decimate.GetOutput()

    # Clean up Model
    cleaner = vtk.vtkCleanPolyData()
    cleaner.SetInputData(surfaceMesh)
    cleaner.Update()
    surfaceMesh = cleaner.GetOutput()

    # Write to OBJ File
    writer = vtk.vtkOBJWriter()
    writer.SetFileName(outputFileName)
    writer.SetInputData(surfaceMesh)
    writer.Update()
</code></pre>
<p>Ohh and with the vtkCleanPolyData(), how would I activate it like the manual button in the surface toolbox module.</p>

---

## Post #5 by @Queen_Rei (2020-06-16 21:41 UTC)

<p>Got it working with:</p>
<pre><code># Export Segmentation to Model Node
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "Segments")
slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, exportFolderItemId)

segmentID = segmentationNode.GetSegmentation().GetNthSegmentID(0)
surfaceMesh = segmentationNode.GetClosedSurfaceInternalRepresentation(segmentID)

# Decimate Model
decimator = vtk.vtkDecimatePro()
decimator.SplittingOff();
decimator.PreserveTopologyOn();
decimator.SetTargetReduction(0.95)
decimator.SetInputData(surfaceMesh)
decimator.Update()
surfaceMesh = decimator.GetOutput()

# Smooth the Model
smoother = vtk.vtkWindowedSincPolyDataFilter()
smoother.SetInputData(surfaceMesh);
smoother.SetNumberOfIterations(20);
smoother.SetPassBand(pow(10.0, -4.0 * 0.2));
smoother.BoundarySmoothingOff();
smoother.FeatureEdgeSmoothingOff();
smoother.NonManifoldSmoothingOn();
smoother.NormalizeCoordinatesOn();
smoother.Update();
surfaceMesh = smoother.GetOutput();

# Clean up Model
cleaner = vtk.vtkCleanPolyData()
cleaner.SetInputData(surfaceMesh)
cleaner.Update()
surfaceMesh = cleaner.GetOutput()

# Write to OBJ File
outputFileName = "Z:/GitHub/andrewxr.io/segmentation.obj"
writer = vtk.vtkOBJWriter()
writer.SetFileName(outputFileName)
writer.SetInputData(surfaceMesh)
writer.Update()</code></pre>

---
