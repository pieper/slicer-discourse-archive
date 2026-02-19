---
topic_id: 33924
title: "Run Python Code In Each Subfolder Automatically"
date: 2024-01-23
url: https://discourse.slicer.org/t/33924
---

# Run Python code in each subfolder automatically

**Topic ID**: 33924
**Date**: 2024-01-23
**URL**: https://discourse.slicer.org/t/run-python-code-in-each-subfolder-automatically/33924

---

## Post #1 by @paleomariomm (2024-01-23 09:42 UTC)

<p>I have this file structure:</p>
<ol>
<li>
<p>Main Folder: <code>W001-W100</code>.</p>
<ul>
<li>
<p>Subfolder: <code>W001</code></p>
<ul>
<li>Around 500 DICOM files (I am working with CT data).</li>
</ul>
</li>
<li>
<p>Subfolder: <code>W002</code></p>
<ul>
<li>Around 500 DICOM files (I am working with CT data).</li>
</ul>
</li>
<li>
<p>Subfolder: <code>...</code></p>
</li>
<li>
<p>Subfolder: <code>W100</code></p>
<ul>
<li>Around 500 DICOM files (I am working with CT data).</li>
</ul>
</li>
</ul>
</li>
</ol>
<p><a href="https://i.stack.imgur.com/g9gtV.png" rel="noopener nofollow ugc"><img src="https://i.stack.imgur.com/g9gtV.png" alt="enter image description here" width="690" height="376"></a></p>
<p>I am using Slicer software and Python to automate the process of getting surface meshes automatically.</p>
<p>This is the Python script I wrote that needs to be run in each subfolder (please, don’t take into account the code itself)</p>
<p>As you can see, there are two lines with the location of the subfolder:</p>
<ul>
<li>Second line, specifying the location of the subfolder</li>
<li>Almost the last line, indicating where to save the <code>.ply</code> file.</li>
</ul>
<p>As I have around 1000 subfolders, I don’t want to run the script changing those lines. In other words, I wan to automate the process.</p>
<p>I am much more familiar with R than with Python. So:</p>
<ul>
<li>could please indicate me how can I automate the process in detail by using Python?</li>
<li>could you please edit the code to adapt to my needs?</li>
<li>could you please show me a step-by-step process?</li>
</ul>
<pre><code class="lang-auto"># Load DICOM files
dicomDataDir = "C:/Users/mario.modesto/Desktop/DICOM/W001"  # input folder with DICOM files
import os 
baboon_skull  = os.path.basename(dicomDataDir)
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))

# Display volume rendering
logic = slicer.modules.volumerendering.logic()
volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
displayNode = logic.CreateVolumeRenderingDisplayNode()
displayNode.UnRegister(logic)
slicer.mrmlScene.AddNode(displayNode)
volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)

# find the files NodeID
volumeNode = getNode('2: Facial Bones  0.75  H70h')

#create a blank Markup ROI
roiNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")

#set the new markup ROI to the dimensions of the volume
cropVolumeParameters = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLCropVolumeParametersNode")
cropVolumeParameters.SetInputVolumeNodeID(volumeNode.GetID())
cropVolumeParameters.SetROINodeID(roiNode.GetID())
slicer.modules.cropvolume.logic().SnapROIToVoxelGrid(cropVolumeParameters)  # optional (rotates the ROI to match the volume axis directions)
slicer.modules.cropvolume.logic().FitROIToInputVolume(cropVolumeParameters)
slicer.mrmlScene.RemoveNode(cropVolumeParameters)

#set the cropping parameters
cropVolumeLogic = slicer.modules.cropvolume.logic()
cropVolumeParameterNode = slicer.vtkMRMLCropVolumeParametersNode()
cropVolumeParameterNode.SetIsotropicResampling(True)

#set the output resolution to 2 millimeters. units in slicer is always in mm. 
cropVolumeParameterNode.SetSpacingScalingConst(2)
cropVolumeParameterNode.SetROINodeID(roiNode.GetID())
cropVolumeParameterNode.SetInputVolumeNodeID(volumeNode.GetID())

#do the cropping
cropVolumeLogic.Apply(cropVolumeParameterNode)

#obtain the nodeID of the cropped volume 
croppedVolume = slicer.mrmlScene.GetNodeByID(cropVolumeParameterNode.GetOutputVolumeNodeID())

# Segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(croppedVolume)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skull")

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(croppedVolume)

# Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","115")
effect.setParameter("MaximumThreshold","3071")
effect.self().onApply()

# Clean up
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

# Make segmentation results visible in 3D
segmentationNode.CreateClosedSurfaceRepresentation()

# Creatint surface mesh and saving

surfaceMesh = segmentationNode.GetClosedSurfaceInternalRepresentation(addedSegmentID)
writer = vtk.vtkPLYWriter()
writer.SetInputData(surfaceMesh)
writer.SetFileName("C:/Users/mario.modesto/Desktop/DICOM/"+baboon_skull+"_surfaceMesh.ply")
writer.Update()

</code></pre>
<p>I would really appreciate your help.</p>
<h1><a name="p-105861-update-1" class="anchor" href="#p-105861-update-1" aria-label="Heading link"></a>UPDATE</h1>
<p>I tried this code:</p>
<pre><code class="lang-auto">from DICOMLib import DICOMUtils
import os
from pathlib import Path
import shutil

for root, dirnames, _ in os.walk("C:/Users/mario.modesto/Desktop/DICOM/"):
    root_path = Path(root)
    for dirname in dirnames:
        dir_path = root_path / dirname
        dicomDataDir = dirname  # input folder with DICOM files
        baboon_skull  = os.path.basename(dicomDataDir)
        loadedNodeIDs = []  # this list will contain the list of all loaded node IDs
        
        with DICOMUtils.TemporaryDICOMDatabase() as db:
          DICOMUtils.importDicom(dicomDataDir, db)
          patientUIDs = db.patients()
          for patientUID in patientUIDs:
            loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
        
        # Display volume rendering
        # https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#display-volume-using-volume-rendering
        logic = slicer.modules.volumerendering.logic()
        volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
        displayNode = logic.CreateVolumeRenderingDisplayNode()
        displayNode.UnRegister(logic)
        slicer.mrmlScene.AddNode(displayNode)
        volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
        logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)
</code></pre>
<p>I inserted some code to load DICOM files and to show volume rendering in the <code>for</code> loop. However, now I see this error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 27, in &lt;module&gt;
AttributeError: 'NoneType' object has no attribute 'AddAndObserveDisplayNodeID'

However, when I tried the original code with only one folder, it works. Any idea?
</code></pre>

---

## Post #2 by @paleomariomm (2024-01-23 12:52 UTC)

<p>I solved this by using this code (<a href="https://stackoverflow.com/questions/77865010/run-python-script-in-each-subfolder-automatically/77865473#77865473" rel="noopener nofollow ugc">answered in SO</a>):</p>
<pre><code class="lang-auto">import os
from DICOMLib import DICOMUtils

yourpath = r"&lt;enter your path&gt;/W001-W100"

#walk through DICOM directory
for dir in os.scandir(yourpath):
    # Load DICOM files
    dicomDataDir = dir.path  # path to input folder with DICOM files
    baboon_skull  = dir.name
    loadedNodeIDs = []  # this list will contain the list of all loaded node IDs

    with DICOMUtils.TemporaryDICOMDatabase() as db:
        DICOMUtils.importDicom(dicomDataDir, db)
        patientUIDs = db.patients()
        for patientUID in patientUIDs:
            loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))


    &lt; rest of your code &gt;

    writer.SetFileName(fr"{dicomDataDir}_surfaceMesh.ply")
    writer.Update()
</code></pre>

---

## Post #3 by @muratmaga (2024-01-23 15:59 UTC)

<p>Looking great.</p>
<p>By the way, if you do not need the metada contents of DICOM files, you can convert the DICOMs to NRRD outside of Slicer using a tool like DCM2NIIX (there is even a slicer extension). Often clinical research needs those DICOM fields for their project, but I don’t think that’s probably the case for those baboon scans. That may simplify your code and workflow.</p>
<p>But regardless you are almost there I think.</p>

---
