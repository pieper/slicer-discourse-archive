# Binary segmentation mask to centerline polydata using a python script

**Topic ID**: 36523
**Date**: 2024-05-31
**URL**: https://discourse.slicer.org/t/binary-segmentation-mask-to-centerline-polydata-using-a-python-script/36523

---

## Post #1 by @RomanStriker (2024-05-31 16:46 UTC)

<p>Hi,</p>
<p>I am working on Ubuntu 20.04.6 LTS with the <a href="https://atm22.grand-challenge.org/" rel="noopener nofollow ugc">ATM’22</a> dataset. I have the CT volumes and the binary segmenatation mask of the pulmonary airway as nifty (.nii.gz) files. To get the centerline of the pulmonary airway, I use following steps:</p>
<ol>
<li>Load the image volume as normal volume and the segmentation volume as a segmenation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6728e980c6ddf8b64f76ea613d28db3ca9c7bd4e.png" data-download-href="/uploads/short-url/eIAPF5Z385VZrWDam4DaG1Jqffg.png?dl=1" title="ksnip_20240531-174014" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6728e980c6ddf8b64f76ea613d28db3ca9c7bd4e_2_690x411.png" alt="ksnip_20240531-174014" data-base62-sha1="eIAPF5Z385VZrWDam4DaG1Jqffg" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6728e980c6ddf8b64f76ea613d28db3ca9c7bd4e_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6728e980c6ddf8b64f76ea613d28db3ca9c7bd4e_2_1035x616.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6728e980c6ddf8b64f76ea613d28db3ca9c7bd4e_2_1380x822.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ksnip_20240531-174014</span><span class="informations">1494×892 61.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>Apply a growing operation on the segmentation mask using the segment editor.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34e342ad188be269d963090b6af7da8ed6fe7e54.jpeg" data-download-href="/uploads/short-url/7xRJmO6DVwZHp9fdqFh80fFL2kY.jpeg?dl=1" title="ksnip_20240531-174228" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e342ad188be269d963090b6af7da8ed6fe7e54_2_690x404.jpeg" alt="ksnip_20240531-174228" data-base62-sha1="7xRJmO6DVwZHp9fdqFh80fFL2kY" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e342ad188be269d963090b6af7da8ed6fe7e54_2_690x404.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e342ad188be269d963090b6af7da8ed6fe7e54_2_1035x606.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34e342ad188be269d963090b6af7da8ed6fe7e54_2_1380x808.jpeg 2x" data-dominant-color="BABFD6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ksnip_20240531-174228</span><span class="informations">1920×1126 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>Load the Extract Centerline module of the Vascular Modeling Toolkit (VMTK).<br>
3.1. Select the segmentation mask as my Surface and run Auto-detect for the endpoints.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19a18d19f8248fcadf52b5e8f20745ce9d033f7a.jpeg" data-download-href="/uploads/short-url/3EK3D78NGPIvj5Zk8COmzw0bVtE.jpeg?dl=1" title="ksnip_20240531-174613" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19a18d19f8248fcadf52b5e8f20745ce9d033f7a_2_690x375.jpeg" alt="ksnip_20240531-174613" data-base62-sha1="3EK3D78NGPIvj5Zk8COmzw0bVtE" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19a18d19f8248fcadf52b5e8f20745ce9d033f7a_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19a18d19f8248fcadf52b5e8f20745ce9d033f7a_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19a18d19f8248fcadf52b5e8f20745ce9d033f7a_2_1380x750.jpeg 2x" data-dominant-color="BBBDD8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ksnip_20240531-174613</span><span class="informations">1920×1045 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
3.2 Create a new network model and click apply to get the centerline.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e0d34ac9fb7b6518bfc4b00c410f64c1a4f5ebe.jpeg" data-download-href="/uploads/short-url/mybJtIVwmQ1lYRTbkbQkfIV3Cmq.jpeg?dl=1" title="ksnip_20240531-174915" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e0d34ac9fb7b6518bfc4b00c410f64c1a4f5ebe_2_690x358.jpeg" alt="ksnip_20240531-174915" data-base62-sha1="mybJtIVwmQ1lYRTbkbQkfIV3Cmq" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e0d34ac9fb7b6518bfc4b00c410f64c1a4f5ebe_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e0d34ac9fb7b6518bfc4b00c410f64c1a4f5ebe_2_1035x537.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e0d34ac9fb7b6518bfc4b00c410f64c1a4f5ebe_2_1380x716.jpeg 2x" data-dominant-color="BABCD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ksnip_20240531-174915</span><span class="informations">1920×997 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>Save the centerline network model as a vtk file.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f1d3a8248c5a74c24232b72143d041106047912.jpeg" data-download-href="/uploads/short-url/bhSlcP9EDOn3pNN21LCP2iAdwsO.jpeg?dl=1" title="ksnip_20240531-175307" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1d3a8248c5a74c24232b72143d041106047912_2_690x393.jpeg" alt="ksnip_20240531-175307" data-base62-sha1="bhSlcP9EDOn3pNN21LCP2iAdwsO" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1d3a8248c5a74c24232b72143d041106047912_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1d3a8248c5a74c24232b72143d041106047912_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f1d3a8248c5a74c24232b72143d041106047912_2_1380x786.jpeg 2x" data-dominant-color="BDBFD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ksnip_20240531-175307</span><span class="informations">1920×1095 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>I have to repeat the same steps for many files, and I would like to use a Python script to achieve this. So far I have the following:</p>
<pre><code class="lang-auto">import vtk
import slicer
import ExtractCenterline

# 1. load volume and segmentation

volume = slicer.util.loadVolume("volume.nii.gz")
seg = slicer.util.loadSegmentation("segmentation.nii.gz")
segmentation = seg.GetSegmentation()
# This creates the 3D view
seg.CreateClosedSurfaceRepresentation()
segmentID = segmentation.GetSegmentIdBySegmentName('Segment_1')
# create empty vtkPolyData object
segmentVtkPolyData = vtk.vtkPolyData()
# Get vtkPolyData representation of segment surface into segmentVtkPolyData variable
seg.GetClosedSurfaceRepresentation(segmentID, segmentVtkPolyData)

# 2. Apply a growing operation
#I am not sure how to do this

# 3.1. Auto-detect the endpoints
# Here I think the code from onAutoDetectEndPoints() should be used, is that correct?
[onAutoDetectEndPoints()](https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L323)

end_pts = []

# 3.2. Extract the centerline
# Here I think the code from onApply() should be used, but I found the following code at 
# (https://discourse.slicer.org/t/vmtk-extract-centerline-with-python-console/31596/8)
# should I use this or the code from onApply()?
[onApply()](https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L230)

# get the centerline logic object
extractLogic = ExtractCenterline.ExtractCenterlineLogic()
# preprocess the polydata
inputSurfacePolyData = extractLogic.polyDataFromNode(seg, segmentID)
preprocessEnabled = True
targetNumberOfPoints = 5000.0
decimationAggressiveness = 4.0
subdivideInputSurface = False
preprocessedPolyData = extractLogic.preprocess(
    inputSurfacePolyData,
    targetNumberOfPoints,
    decimationAggressiveness,
    subdivideInputSurface,
)
centerlineCurveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode", "Centerline curve")
centerlinePolyData, voronoiDiagramPolyData = extractLogic.extractCenterline(
        preprocessedPolyData, end_pts, curveSamplingDistance=0.001)

# 4. Save the centerline
# Again, I don't know how to export the centerlinePolyData as a .vtk file
</code></pre>
<p>I would also like to know how to run a .py file in slicer? Do I need to create a new module, and use the .py file that it generates. Ideally I would like to be able to debug the file using Pycharm. I managed to attached Pycharm’s remote debugger to 3D Slicer’s Python console using the instructions <a href="https://github.com/SlicerRt/SlicerDebuggingTools#instructions-for-pycharm" rel="noopener nofollow ugc">here</a>, but the instructions at one point say</p>
<blockquote>
<p>Load your .py file and add breakpoints (menu: <code>Run</code> / <code>Toggle Line Breakpoint</code>) where you want your execution to stop for debugging.</p>
</blockquote>
<p>but does not explain how to actually run the python script.</p>
<p>I would appreciate any help with this.</p>

---

## Post #2 by @chir.set (2024-05-31 18:33 UTC)

<aside class="quote no-group" data-username="RomanStriker" data-post="1" data-topic="36523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/c37758/48.png" class="avatar"> RomanStriker:</div>
<blockquote>
<pre><code class="lang-auto"># 2. Apply a growing operation
#I am not sure how to do this
</code></pre>
</blockquote>
</aside>
<p><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/e9aa8e7e532299c10cfae5746e9c7ef06a4314b1/ArterialCalcificationPreProcessor/ArterialCalcificationPreProcessor.py#L271" rel="noopener nofollow ugc">This code</a> may be an adequate example for a growing operation with the ‘Segment editor’.</p>

---

## Post #3 by @RomanStriker (2024-06-03 18:22 UTC)

<p>Thanks. I have managed to get the centerline using the following code.</p>
<pre data-code-wrap="py"><code class="lang-py"># Reference: https://discourse.slicer.org/t/vmtk-extract-centerline-with-python-console/31596/8
# 1. load volume and segmentation
print("Loading volume and segmentation:", volume)
vol = slicer.util.loadVolume(vol_path)
seg = slicer.util.loadSegmentation(seg_path)
seg.CreateClosedSurfaceRepresentation()  # This creates the 3D view

# 2. Apply a growing operation
# Reference: https://discourse.slicer.org/t/include-a-manual-segment-editor-effect-in-a-module/17464
# Reference: https://github.com/vmtk/SlicerExtension-VMTK/blob/e9aa8e7e532299c10cfae5746e9c7ef06a4314b1/ArterialCalcificationPreProcessor/ArterialCalcificationPreProcessor.py#L271
print("Applying growing operation")
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(seg)
segmentEditorWidget.setSourceVolumeNode(vol)

# Grow by margin within intensity range.
segmentEditorWidget.setActiveEffectByName("Margin")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("ApplyToAllVisibleSegments", str(0))
effect.setParameter("MarginSizeMm", str(0.83))
effect.self().onApply()

# 3.1. Auto-detect the endpoints and extract the centerline
extractCenterlineWidget = ExtractCenterline.ExtractCenterlineWidget()
# get segment ID
segmentation = seg.GetSegmentation()
segmentID = segmentation.GetSegmentIdBySegmentName('Segment_1')
# Set the parameters
extractCenterlineWidget._parameterNode.SetNodeReferenceID("InputSurface", seg.GetID())
extractCenterlineWidget._parameterNode.SetParameter("InputSegmentID", segmentID)
extractCenterlineWidget._parameterNode.SetParameter("TargetNumberOfPoints", str(5000.0))
extractCenterlineWidget._parameterNode.SetParameter("DecimationAggressiveness", str(4.0))
extractCenterlineWidget._parameterNode.SetParameter("CurveSamplingDistance", str(0.001))
extractCenterlineWidget._parameterNode.SetParameter("PreprocessInputSurface", "true")
extractCenterlineWidget._parameterNode.SetParameter("SubdivideInputSurface", "true")

extractCenterlineWidget.onAutoDetectEndPoints()
endPointsMarkupsNode = extractCenterlineWidget._parameterNode.GetNodeReference("EndPoints")

# 3.2. Extract the centerline
# Setting network nodes
# For extracting the network model
networkModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode",
                                                          slicer.mrmlScene.GetUniqueNameByString("Network model"))
networkModelNode.CreateDefaultDisplayNodes()
extractCenterlineWidget._parameterNode.SetNodeReferenceID("NetworkModel", networkModelNode.GetID())
# For extracting the network curve
networkCurveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode",
                                                      slicer.mrmlScene.GetUniqueNameByString("Network curve"))
networkCurveNode.CreateDefaultDisplayNodes()
extractCenterlineWidget._parameterNode.SetNodeReferenceID("NetworkCurve", networkCurveNode.GetID())
# For extracting the network properties
networkPropertiesNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode",
                                                      slicer.mrmlScene.GetUniqueNameByString("Network properties"))
extractCenterlineWidget._parameterNode.SetNodeReferenceID("NetworkProperties", networkPropertiesNode.GetID())

extractCenterlineWidget.onApplyButton()
</code></pre>
<p>In Slicer GUI there is an option to export the network curve as a Markups JSON file with options to include children and retain hierarchy. How can I do this using the python script? I would also like to export the network model as a VTK file and the end points as a JSON file, How can I do that?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/056a11934bf8cd0c049e28037604db43138e78b2.jpeg" data-download-href="/uploads/short-url/LTDzZoNcAisRVKA9zlNTBIVyr8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/056a11934bf8cd0c049e28037604db43138e78b2_2_690x344.jpeg" alt="image" data-base62-sha1="LTDzZoNcAisRVKA9zlNTBIVyr8" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/056a11934bf8cd0c049e28037604db43138e78b2_2_690x344.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/056a11934bf8cd0c049e28037604db43138e78b2_2_1035x516.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/056a11934bf8cd0c049e28037604db43138e78b2_2_1380x688.jpeg 2x" data-dominant-color="DBDBE4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×959 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @RomanStriker (2024-06-04 09:03 UTC)

<p>I can save the nodes as follows.</p>
<pre><code class="lang-auto"># Create network model storage node
networkModelStorageNode = networkModelNode.CreateDefaultStorageNode()
networkModelStorageNode.SetFileName(os.path.join(network_save_path, file_name + ".vtk"))
networkModelStorageNode.WriteData(networkModelNode)
</code></pre>
<p>but I still cannot figure out how to save the network curve in heirachical folder structure as possible in GUI. Any help would be appreciated.</p>

---

## Post #5 by @RomanStriker (2024-06-04 10:53 UTC)

<p>The code for saving the network curve with required folder structure is linked <a href="https://discourse.slicer.org/t/save-a-tree-of-centerline-curves-to-json-files-using-python/36574/2">here</a>.</p>

---
