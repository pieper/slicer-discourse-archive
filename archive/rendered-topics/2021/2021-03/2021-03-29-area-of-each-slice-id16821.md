---
topic_id: 16821
title: "Area Of Each Slice"
date: 2021-03-29
url: https://discourse.slicer.org/t/16821
---

# Area of each slice

**Topic ID**: 16821
**Date**: 2021-03-29
**URL**: https://discourse.slicer.org/t/area-of-each-slice/16821

---

## Post #1 by @Gonzalo_Rojas_Costa (2021-03-29 15:14 UTC)

<p>I made a 3D ROI with Segment Editor module in an MRI image… How can I get the area of each sagittal slice?</p>

---

## Post #2 by @mikebind (2021-03-29 20:19 UTC)

<p>To do this I would convert the segmentation to a labelmap, count the labeled voxels across the sagittal plane, and multiply by the voxel cross sectional area. Here is code which would do this for you:</p>
<pre><code>segmentationName= 'MySegmentation' # change this to whatever your segmentation is called
segmentationNode = getNode(segmentationName)
labelMapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode', segmentationNode.GetName()+'-label')
slicer.modules.segmentations.logic().ExportAllSegmentsToLabelmapNode(segmentationNode, labelMapVolumeNode , slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY)
labelMapNumpyArray = slicer.util.arrayFromVolume(labelMapVolumeNode )
voxelSizeMm = labelMapVolumeNode.GetSpacing()
</code></pre>
<p>Next, you can find the area by summing all the non-zero labeled voxels in each sagittal slice and multiplying by the voxel area in that slice plane.  For this, you need to know which IJK dimension corresponds to your sagittal plane because there can be an arbitrary relationship between the I, J, and K dimensions and the anatomical directions.  The relationship between the IJK directions and the RAS directions can be seen by examining the volume’s IJK to RAS directions matrix in the “Volumes” module, in the “Volume Information” section.  If you were to determine that the sagittal slice varies in the K direction (i.e. by seeing that the K direction vector points in the anatomical “Right” direction), then the following code would find the areas you want.</p>
<pre><code>mm2PerVoxel = voxelSizeMm[0] * voxelSizeMm[1] # the cross sectional area of the voxel in the IJ plane
# The numpy indexing is KJI rather than IJK, so to sum across the IJ plane, we need to sum across axis 1 and 2 rather than 0 and 1
areaInVoxels = np.sum(labelMapNumpyArray &gt; 0, axis=(1,2))
areaInMm2 = areaInVoxels * mm2PerVoxel
</code></pre>
<p>If you saw that your sagittal slice varied in the J dimension instead, then you would want to do this:</p>
<pre><code>mm2PerVoxel = voxelSizeMm[0] * voxelSizeMm[2] # the cross sectional area of the voxel in the IK plane
# The numpy indexing is KJI rather than IJK, so to sum across the IK plane, we need to sum across axis 2 and 0 rather than 0 and 2
areaInVoxels = np.sum(labelMapNumpyArray &gt; 0, axis=(0,2))
areaInMm2 = areaInVoxels * mm2PerVoxel
</code></pre>
<p>If you have multiple segments, you could do <code>np.sum(labelMapNumpyArray==segmentNumber)</code> for each segment number instead of the <code> &gt;0</code>, which will include all segments.</p>
<p>At the end of any of these, <code>areaInMm2</code> would be a numpy vector with as many values as there are sagittal slices.</p>

---

## Post #3 by @muratmaga (2021-03-29 20:35 UTC)

<aside class="quote no-group" data-username="Gonzalo_Rojas_Costa" data-post="1" data-topic="16821" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gonzalo_rojas_costa/48/5259_2.png" class="avatar"> Gonzalo_Rojas_Costa:</div>
<blockquote>
<p>I made a 3D ROI with Segment Editor module in an MRI image… How can I get the area of each sagittal slice?</p>
</blockquote>
</aside>
<p>You can use the <code>Segment Cross Section Area</code> module in <code>Sandbox</code> extension (listed under the Examples category in the Extension manager).</p>
<aside class="quote" data-post="1" data-topic="11293">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-for-measuring-cross-section-area-of-segments/11293">New module for measuring cross-section area of segments</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    A new module - “Segment cross-section area” - has been added to Slicer. It can compute cross-sectional area of segmented structures along a chosen axis direction. Results are available both as a table and can be shown in a plot, too. Short demo video: 

For now, the module is available by installing “Sandbox” extension in the extension manager in a recent 3D Slicer Preview Release. 
If you have any comments and suggestions then please post it here.
  </blockquote>
</aside>


---

## Post #4 by @coco (2024-07-22 15:56 UTC)

<aside class="quote no-group" data-username="New module for measuring cross-section area of segments" data-post="1" data-topic="11293">
<div class="title">
<div class="quote-controls"></div>
<a href="https://discourse.slicer.org/t/new-module-for-measuring-cross-section-area-of-segments/11293/1">New module for measuring cross-section area of segments</a></div>
<blockquote>
<p>Segment cross-section area</p>
</blockquote>
</aside>
<p>I like this but it is not clear which axis (axial, coronal or sagittal) is chosen or can be chosen. The video does not indicate it as well.<br>
After reviewing it seems “column” is for coronal,  row is for sagittal, and slice is axial, correct ?<br>
Many thanks</p>

---

## Post #5 by @lassoan (2024-07-22 16:13 UTC)

<p>You can choose IJK axis in <code>Volume axis</code> selector. It is not anatomical axis, but row, column, or slice. If you want to get cross-sections along an arbitrary axis direction (including any anatomical axis) then there are several other options. To summarize, if you need cross-section areas:</p>
<ul>
<li><strong>in axial slices:</strong> you can use the <code>Segment Cross-Section Area</code> module in <a href="https://github.com/PerkLab/SlicerSandbox">Sandbox</a> extension.</li>
<li><strong>along a line in arbitrary direction:</strong> you can use <code>SegmentGeometry</code> module in <a href="https://github.com/jmhuie/SlicerBiomech">SlicerBiomech</a> extension.</li>
<li><strong>along a curve:</strong> you can segment the region and use <code>Cross-section analysis</code> or <code>Stenosis measurement</code> modules in <a href="https://github.com/vmtk/SlicerExtension-VMTK">VMTK</a> extension.</li>
<li><strong>in a single slice (either axial oblique):</strong> you can use a closed curve markup (enable area measurement in <code>Measurements</code> section in <code>Markups</code> module).</li>
</ul>

---
