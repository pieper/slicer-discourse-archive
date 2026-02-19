---
topic_id: 27910
title: "Processing Slows Down After Many Iterations"
date: 2023-02-17
url: https://discourse.slicer.org/t/27910
---

# Processing slows down after many iterations

**Topic ID**: 27910
**Date**: 2023-02-17
**URL**: https://discourse.slicer.org/t/processing-slows-down-after-many-iterations/27910

---

## Post #1 by @nrex45 (2023-02-17 22:51 UTC)

<p>Somewhat related question: I’m looping through the following code a couple of hundred times and after a while slicer starts to run slower and slower… based on experience this usually means I’m creating some kind of node (or maybe a widget in this case?) that accumulates and bogs Slicer down.</p>
<p>I’m removing all of the nodes I am creating (besides maybe the widget…) - is there anything I can do to prevent slowing of the program?</p>
<pre><code class="lang-auto">import vtkSegmentationCorePython as vtkSegmentationCore

def generate_subtracted_files(cwd, first_seg, second_seg,output_name,final_subtraction):
    
    ### load segmentations
    cwd = os.getcwd()
    vol = slicer.util.loadVolume(cwd+"/"+"fu0.nrrd")
    seg = slicer.util.loadSegmentation(cwd+"/"+first_seg)
    seg2 = slicer.util.loadSegmentation(cwd + "/" + second_seg)
    seg.SetReferenceImageGeometryParameterFromVolumeNode(vol)
    seg2.SetReferenceImageGeometryParameterFromVolumeNode(vol)
    
    
    ### create new segmentation, add loaded segmentations
    seg.CreateClosedSurfaceRepresentation()
    seg2.CreateClosedSurfaceRepresentation()
    csr1 = vtk.vtkPolyData()
    seg.GetClosedSurfaceRepresentation(seg.GetSegmentation().GetNthSegmentID(0), csr1)
    csr2 = vtk.vtkPolyData()
    seg2.GetClosedSurfaceRepresentation(seg2.GetSegmentation().GetNthSegmentID(0), csr2)
    segmentationNodeNew = slicer.vtkMRMLSegmentationNode()
    slicer.mrmlScene.AddNode(segmentationNodeNew)
    segmentationNodeNew.CreateDefaultDisplayNodes()
    segmentationNodeNew.SetReferenceImageGeometryParameterFromVolumeNode(vol)
    segmentationNodeNew.AddSegmentFromClosedSurfaceRepresentation(csr2,"first",[0,1,0])
    segmentationNodeNew.AddSegmentFromClosedSurfaceRepresentation(csr1,"second",[0,0,1])
    
    ### load segment editor widget
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    
    ### perform subtraction operations
    segmentEditorWidget.setSegmentationNode(segmentationNodeNew)
    segmentEditorWidget.setActiveEffectByName("Logical operators")
    effect = segmentEditorWidget.activeEffect()
    effect.self().scriptedEffect.setParameter("Operation","SUBTRACT")
    selectedSegmentID = effect.self().scriptedEffect.parameterSetNode().GetSelectedSegmentID()
    effect.self().scriptedEffect.setParameter("BypassMasking", 1)
    effect.self().scriptedEffect.setParameter("ModifierSegmentID",segmentationNodeNew.GetSegmentation().GetNthSegmentID(1))
    effect.self().onApply()
    segmentationNodeNew.RemoveSegment("second")
    
    myStorageNode = segmentationNodeNew.CreateDefaultStorageNode()
    myStorageNode.SetFileName(output_name)
    myStorageNode.WriteData(segmentationNodeNew)
    
    
    slicer.mrmlScene.RemoveNode(vol)
    slicer.mrmlScene.RemoveNode(segmentEditorNode)
    slicer.mrmlScene.RemoveNode(seg)
    slicer.mrmlScene.RemoveNode(seg2)
    slicer.mrmlScene.RemoveNode(segmentationNodeNew)
    slicer.mrmlScene.RemoveNode(myStorageNode)
    return(True)
</code></pre>

---

## Post #2 by @lassoan (2023-02-19 02:18 UTC)

<p>This is almost always due to memory leaks. You can confirm by monitoring the memory usage of the application. If memory usage is continuously increasing then it means your script causes a memory leak.</p>
<p>You can fix it by deleting all objects that you create. VTK and Python objects are all reference counted and so objects usually get automatically deleted once there are no more Python variable referencing them. However, you used factory methods (such as slicer.vtkMRMLSegmentationNode()) then you need to call <code>Unregister</code> to prevent leaks. See more information <a href="https://slicer.readthedocs.io/en/latest/developer_guide/advanced_topics.html#factory-methods">here</a>.</p>

---
