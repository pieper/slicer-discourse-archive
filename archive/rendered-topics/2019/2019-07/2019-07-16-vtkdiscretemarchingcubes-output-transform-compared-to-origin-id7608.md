---
topic_id: 7608
title: "Vtkdiscretemarchingcubes Output Transform Compared To Origin"
date: 2019-07-16
url: https://discourse.slicer.org/t/7608
---

# vtkDiscreteMarchingCubes Output Transform compared to original vtkOrientedImageData

**Topic ID**: 7608
**Date**: 2019-07-16
**URL**: https://discourse.slicer.org/t/vtkdiscretemarchingcubes-output-transform-compared-to-original-vtkorientedimagedata/7608

---

## Post #1 by @basti (2019-07-16 15:05 UTC)

<p>Dear forum,<br>
I’m trying to create a vtkPolyData out of a vtkOrientedImageData. Given a segmentation ‘Segmentation’ with a segment with id ‘Segment_1’, the output model is strangely transformed to the input oriented imagedata:</p>
<pre><code>seg = slicer.util.getNode('Segmentation')
segID = 'Segment_1'

import vtkSegmentationCorePython
modelsLogic = slicer.modules.models.logic()

orImg = vtkSegmentationCorePython.vtkOrientedImageData()
slicer.vtkSlicerSegmentationsModuleLogic.GetSegmentBinaryLabelmapRepresentation(seg, segID, orImg)

inputDiscreteCubes = vtk.vtkDiscreteMarchingCubes()
inputDiscreteCubes.SetInputData(orImg)
inputDiscreteCubes.GenerateValues(1,0,0)
inputDiscreteCubes.Update()

modelNode = modelsLogic.AddModel(inputDiscreteCubes.GetOutput())
</code></pre>
<p>It is possible to solve this by first removing the ImageToWorld transform of the oriented imagedata and applying this transform to the model later again:</p>
<pre><code>seg = slicer.util.getNode('Segmentation')
segID = 'Segment_1'

import vtkSegmentationCorePython
modelsLogic = slicer.modules.models.logic()

orImg = vtkSegmentationCorePython.vtkOrientedImageData()
slicer.vtkSlicerSegmentationsModuleLogic.GetSegmentBinaryLabelmapRepresentation(seg, segID, orImg)

mat = vtk.vtkMatrix4x4()
orImg.GetImageToWorldMatrix(mat)
orImg.SetImageToWorldMatrix(vtk.vtkMatrix4x4())

inputDiscreteCubes = vtk.vtkDiscreteMarchingCubes()
inputDiscreteCubes.SetInputData(orImg)
inputDiscreteCubes.GenerateValues(1,0,0)
inputDiscreteCubes.Update()

transform = vtk.vtkTransform()
transform.SetMatrix(mat)
transformFilter=vtk.vtkTransformPolyDataFilter()
transformFilter.SetTransform(transform)
transformFilter.SetInputData(inputDiscreteCubes.GetOutput())
transformFilter.Update()

modelNode = modelsLogic.AddModel(transformFilter.GetOutput())
</code></pre>
<p>But why does it not work in the first place without removing and reapplying the transform? And which transform has to be applied to the resulting model without removing the matrix from the oriented imagedata?</p>
<p>Thank you, Sebastian</p>

---

## Post #2 by @cpinter (2019-07-16 16:05 UTC)

<p>Instead of reimplementing existing features, I would strongly suggest using what is already available and tested:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L209" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L209" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L209</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="199" style="counter-reset: li-counter 198 ;">
<li>/// \param insertBeforeSegmentId New segments will be inserted before this segment.</li>
<li>static bool ImportLabelmapToSegmentationNode(vtkMRMLLabelMapVolumeNode* labelmapNode,</li>
<li>  vtkMRMLSegmentationNode* segmentationNode, std::string insertBeforeSegmentId="");</li>
<li>
</li>
<li>/// Import all labels from a labelmap image to a segmentation node, each label to a separate segment</li>
<li>/// The colors of the new segments are randomly generated, unless terminology context is specified, in which case the terminology</li>
<li>///   entries are attempted to be mapped to the imported labels</li>
<li>/// LabelmapImage is defined in the segmentation node's coordinate system</li>
<li>/// (parent transform of the segmentation node is not used during import).</li>
<li>/// \param baseSegmentName Prefix for the names of the new segments. Empty by default, in which case the prefix will be "Label"</li>
<li class="selected">static bool ImportLabelmapToSegmentationNode(vtkOrientedImageData* labelmapImage,</li>
<li>  vtkMRMLSegmentationNode* segmentationNode, std::string baseSegmentName="", std::string insertBeforeSegmentId="") ;</li>
<li>
</li>
<li>/// Update segmentation from segments in a labelmap node.</li>
<li>/// \param updatedSegmentIDs Defines how label values 1..N are mapped to segment IDs (0..N-1).</li>
<li>static bool ImportLabelmapToSegmentationNode(vtkMRMLLabelMapVolumeNode* labelmapNode,</li>
<li>  vtkMRMLSegmentationNode* segmentationNode, vtkStringArray* updatedSegmentIDs);</li>
<li>
</li>
<li>/// Update segmentation from segments in a labelmap node.</li>
<li>/// \param updatedSegmentIDs Defines how label values 1..N are mapped to segment IDs (0..N-1).</li>
<li>static bool ImportLabelmapToSegmentationNode(vtkOrientedImageData* labelmapImage,</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L149" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L149" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L149</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="139" style="counter-reset: li-counter 138 ;">
<li>/// 1. If representation node is a labelmap node, then the binary labelmap representation of the</li>
<li>///    segment is copied</li>
<li>/// 2. If representation node is a model node, then the closed surface representation is copied</li>
<li>/// Otherwise return with failure.</li>
<li>static bool ExportSegmentToRepresentationNode(vtkSegment* segment, vtkMRMLNode* representationNode);</li>
<li>
</li>
<li>/// Export multiple segments into a model hierarchy, a model node from each segment</li>
<li>/// \param segmentationNode Segmentation node from which the the segments are exported</li>
<li>/// \param segmentIds List of segment IDs to export</li>
<li>/// \param modelHierarchyNode Model hierarchy to export the segments to</li>
<li class="selected">static bool ExportSegmentsToModelHierarchy(vtkMRMLSegmentationNode* segmentationNode,</li>
<li>  std::vector&lt;std::string&gt;&amp; segmentIDs, vtkMRMLModelHierarchyNode* modelHierarchyNode);</li>
<li>
</li>
<li>/// Export multiple segments into a model hierarchy, a model node from each segment</li>
<li>/// \param segmentationNode Segmentation node from which the the segments are exported</li>
<li>/// \param segmentIds List of segment IDs to export</li>
<li>/// \param modelHierarchyNode Model hierarchy to export the segments to</li>
<li>static bool ExportSegmentsToModelHierarchy(vtkMRMLSegmentationNode* segmentationNode,</li>
<li>  vtkStringArray* segmentIds, vtkMRMLModelHierarchyNode* modelHierarchyNode);</li>
<li>
</li>
<li>/// Export visible segments into a model hierarchy, a model node from each segment</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2019-07-16 16:17 UTC)

<p>I fully agree, just use these existing methods for that. You can find examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_nodes_from_segmentation_node" rel="nofollow noopener">script repository</a>.</p>
<p>We plan to retire vtkOrientedImageData in Slicer5 by this fall (as image orientation is now part of <a href="https://vtk.org/doc/nightly/html/classvtkImageData.html#a14849687420465eedec8290c1d7f88a9" rel="nofollow noopener">vtkImageData</a>) and that will make things much simpler.</p>

---
