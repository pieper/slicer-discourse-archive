---
topic_id: 31541
title: "How To Get The Convexhull Of A Segment"
date: 2023-09-04
url: https://discourse.slicer.org/t/31541
---

# How to get the convexHull of a segment

**Topic ID**: 31541
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/how-to-get-the-convexhull-of-a-segment/31541

---

## Post #1 by @Matteboo (2023-09-04 10:10 UTC)

<p>Hello,<br>
I want to obtain the convex hull of a segment. (I don’t know how to upload an nrrd file but I can give it necessary)<br>
I saw <a href="https://discourse.slicer.org/t/fill-holes-in-3d-model/13508">this</a> conversation but I can’t figure out what node I should get.<br>
I want to use this snippet of code</p>
<pre><code class="lang-auto">modelNode = getNode('mySurface')

convexHull = vtk.vtkDelaunay3D()
convexHull.SetInputData(modelNode.GetPolyData())
outerSurface = vtk.vtkGeometryFilter()
outerSurface.SetInputConnection(convexHull.GetOutputPort())
outerSurface.Update()
modelNode.SetAndObservePolyData(outerSurface.GetOutput())
</code></pre>
<p>But I don’t know what I should put in ‘mysurface’<br>
From my understanding I should put the name of an vtkMRMLModelNode so that I can call GetPolyData()</p>
<p>However when I do getNode(‘mysegmentation’) I get a vtkMRMLSegmentationNode</p>
<p>I don’t know how to get the vtkMRMLModelNode could you help me with that ?<br>
Or if you have another way to get the convec hull that works too</p>

---

## Post #2 by @pieper (2023-09-04 13:49 UTC)

<p>Probably you want one of these methods:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/4a668bea6ebd183d9d0b70a510e87ea38164fd33/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L140-L152">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/4a668bea6ebd183d9d0b70a510e87ea38164fd33/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L140-L152" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4a668bea6ebd183d9d0b70a510e87ea38164fd33/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L140-L152" target="_blank" rel="noopener">Slicer/Slicer/blob/4a668bea6ebd183d9d0b70a510e87ea38164fd33/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L140-L152</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="140" style="counter-reset: li-counter 139 ;">
          <li>/// Export segment to representation MRML node.</li>
          <li>/// 1. If representation node is a labelmap node, then the binary labelmap representation of the</li>
          <li>///    segment is copied</li>
          <li>/// 2. If representation node is a model node, then the closed surface representation is copied</li>
          <li>/// Otherwise return with failure.</li>
          <li>static bool ExportSegmentToRepresentationNode(vtkSegment* segment, vtkMRMLNode* representationNode);</li>
          <li></li>
          <li>/// Export multiple segments into a folder, a model node from each segment</li>
          <li>/// \param segmentationNode Segmentation node from which the the segments are exported</li>
          <li>/// \param segmentIds List of segment IDs to export</li>
          <li>/// \param folderItemId Subject hierarchy folder item ID to export the segments to</li>
          <li>static bool ExportSegmentsToModels(vtkMRMLSegmentationNode* segmentationNode,</li>
          <li>  const std::vector&lt;std::string&gt;&amp; segmentIDs, vtkIdType folderItemId);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Matteboo (2023-09-20 13:52 UTC)

<p>Thanks you I managed to make it work  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
