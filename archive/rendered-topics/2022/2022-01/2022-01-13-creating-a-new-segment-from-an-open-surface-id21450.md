# Creating a new segment from an open surface

**Topic ID**: 21450
**Date**: 2022-01-13
**URL**: https://discourse.slicer.org/t/creating-a-new-segment-from-an-open-surface/21450

---

## Post #1 by @perecanals (2022-01-13 17:02 UTC)

<p>Hi,</p>
<p>I am trying to get a new segment from a part of a (closed) surface model (obtained from a segment in the Segment Editor) via Python scripting. I am working with a large closed surface, onto which I identify a part of the points and cells (mesh triangles) that fulfill a given set of conditions (see first image).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c948ee3f2b86d1d1d294b6f1442552cd7dc8de48.jpeg" data-download-href="/uploads/short-url/sIEdVYEWy5qIugukqR6WdC5mKik.jpeg?dl=1" title="sense nom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c948ee3f2b86d1d1d294b6f1442552cd7dc8de48_2_290x500.jpeg" alt="sense nom" data-base62-sha1="sIEdVYEWy5qIugukqR6WdC5mKik" width="290" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c948ee3f2b86d1d1d294b6f1442552cd7dc8de48_2_290x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c948ee3f2b86d1d1d294b6f1442552cd7dc8de48_2_435x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c948ee3f2b86d1d1d294b6f1442552cd7dc8de48_2_580x1000.jpeg 2x" data-dominant-color="4B4A57"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sense nom</span><span class="informations">752×1294 65.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I can generate a new surface isolating these points from the rest and creating a new vtkPolyData object, but I am left with open ends of the surface (image 2).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3872f36564936cbfd1c847824c759474934b7aa4.jpeg" data-download-href="/uploads/short-url/83n1bTUeCzh51BdmfY5jZy08LYw.jpeg?dl=1" title="sense nom 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3872f36564936cbfd1c847824c759474934b7aa4_2_690x492.jpeg" alt="sense nom 2" data-base62-sha1="83n1bTUeCzh51BdmfY5jZy08LYw" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3872f36564936cbfd1c847824c759474934b7aa4_2_690x492.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3872f36564936cbfd1c847824c759474934b7aa4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3872f36564936cbfd1c847824c759474934b7aa4.jpeg 2x" data-dominant-color="605F60"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sense nom 2</span><span class="informations">700×500 22.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My goal is to generate a new segment from this open surface, but I understand that I need a closed surface to do so. If that is the case, what is the best way to close these open ends? I have tried to use vtkClipClosedSurface, but I haven’t found an automatic way to detect the clipping planes.</p>
<p>Thank you!</p>

---

## Post #2 by @mau_igna_06 (2022-01-13 20:10 UTC)

<p>Maybe you could try using this:</p>
<pre><code class="lang-auto">edges = vtk.vtkFeatureEdges()
edges.BoundaryEdgesOn()
</code></pre>
<p>And the get all disconnected regions with vtkConnectivityFilter. Maybe you can use this data to initialize your algorithms.</p>
<p><a href="https://discourse.vtk.org/t/polydata-surface-border-as-polyline/5451">This</a> maybe a little bit related</p>

---

## Post #3 by @perecanals (2022-01-14 07:56 UTC)

<p>Thank you <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> for your reply. Following your advise, I have tried to get the boundary edges using the following code:</p>
<pre><code class="lang-auto">edges = vtk.vtkFeatureEdges()
edges.BoundaryEdgesOn()
edges.FeatureEdgesOff()
edges.ManifoldEdgesOff()
edges.SetInputData(circularSegment)
edges.Update()
output = edges.GetOutput()
</code></pre>
<p>In this example, the object <code>circular segment</code> is a the vtkPolyData containing the input surface from the original post. From here, I would expect that <code>output</code> would be a vtkPolyData containing two cells (vtkPolyLines?) corresponding to the two boundaries of the surface. Instead, I get all other edges of the original surface. In the image below you can see one of the open ends of the surface. On the left, the blue wireframe corresponds to the <code>output</code> object, while on the right I superposed the wireframe representation of the original surface in white.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19137ecd33b76cd52985a5bc4b41de29747fee7e.jpeg" data-download-href="/uploads/short-url/3zPHJ83MvDALYJAOgn7VFodKzMO.jpeg?dl=1" title="sense nom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19137ecd33b76cd52985a5bc4b41de29747fee7e_2_690x251.jpeg" alt="sense nom" data-base62-sha1="3zPHJ83MvDALYJAOgn7VFodKzMO" width="690" height="251" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19137ecd33b76cd52985a5bc4b41de29747fee7e_2_690x251.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19137ecd33b76cd52985a5bc4b41de29747fee7e_2_1035x376.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19137ecd33b76cd52985a5bc4b41de29747fee7e_2_1380x502.jpeg 2x" data-dominant-color="090911"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sense nom</span><span class="informations">1824×664 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is this expected behavior? Do you think there is something wrong with my original vtkPolyData? Also, I noticed that if I also introduce this:</p>
<pre><code class="lang-auto">edges.NonManifoldEdgesOff()
</code></pre>
<p>I get an empty object in return, which seems incorrect. Any ideas?</p>

---

## Post #4 by @mau_igna_06 (2022-01-14 09:41 UTC)

<p>Do you calculated the normals of the model before processing it? if not try that</p>
<p>Try to know how many non-manifold edges your mesh has by using the corresponding option on and all the other off in the edges filter. If the mesh has lot of non manifold edges that can be a problem.</p>
<p>Try cleaning your mesh with vtkCleanPolyData before processing, that may help</p>
<p>Hope these ideas can help</p>
<p>Mauro</p>

---

## Post #5 by @perecanals (2022-01-14 11:49 UTC)

<p>I now introduced the normals computation, which didn’t have any noticeable effect in the edges computation. Then, I was experimenting a bit to see how many cells were computed for each of the 4 options (boundary, feature, manifold and non-manifold) and something strange is happening, at least if what I understand is correct. I have 0 boundary and feature edges, 53 manifold edges (these are the ones in the boundary!) and the rest (29537) are non-manifold… In the image I superposed the manifold edges form one of the open ends in red to the non-manifold in blue that we saw before.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19faa74339d9f18a8c7f2b5795f422f19328d190.jpeg" data-download-href="/uploads/short-url/3HOXsTevQrRixYXYdXiw9UjMayY.jpeg?dl=1" title="sense nom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19faa74339d9f18a8c7f2b5795f422f19328d190_2_329x250.jpeg" alt="sense nom" data-base62-sha1="3HOXsTevQrRixYXYdXiw9UjMayY" width="329" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19faa74339d9f18a8c7f2b5795f422f19328d190_2_329x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19faa74339d9f18a8c7f2b5795f422f19328d190_2_493x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/19faa74339d9f18a8c7f2b5795f422f19328d190_2_658x500.jpeg 2x" data-dominant-color="050309"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sense nom</span><span class="informations">994×754 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>At least I can continue to implement some filter to close those open ends, but it would be nice to have the expected behavior instead of this. If any ideas come up feel free to reply!</p>
<p>Thank you Mauro!</p>

---

## Post #6 by @mau_igna_06 (2022-01-14 13:10 UTC)

<p>You are welcome.</p>
<p>I think to deep further into this you should ask <a href="https://discourse.vtk.org/">here</a></p>
<p>Mauro</p>

---

## Post #7 by @perecanals (2022-01-17 13:52 UTC)

<p>Hi again,</p>
<p>In the end, I repeated the process computing the normals and passing the <code>vtkCleanPolyData</code> filter and everything works as expected now, I am not sure of what I was doing wrong before. In the end, the code looks something like this (I paste here from the <code>vtkPolyData</code> definition onwards):</p>
<pre><code class="lang-auto"># Define vtkPolyData from selected points (vtkPoints object) and polys (vtkCellArray object)
circularSegment = vtk.vtkPolyData()
circularSegment.SetPoints(pointsCircularSegmentModel)
circularSegment.SetPolys(cellArrayCircularSegmentModel)

# We can to compute the normals for all mesh triangles
normals = vtk.vtkPolyDataNormals()
normals.SetInputData(circularSegment)
normals.SetFeatureAngle(80)
normals.AutoOrientNormalsOn()
normals.UpdateInformation()
normals.Update()
circularSegment = normals.GetOutput()

# Clean the vtkPolyData. Without this, normal edges are seen as non-manifold and boundary edges as manifold. Normals have to be computed prior to this
cleanPolyData = vtk.vtkCleanPolyData()
cleanPolyData.SetInputData(circularSegment)
cleanPolyData.Update()
circularSegment = cleanPolyData.GetOutput()

# Now we can extract the boundary edges with the vtkFeatureEdges filter
edgesFilter = vtk.vtkFeatureEdges()
edgesFilter.BoundaryEdgesOn()
edgesFilter.FeatureEdgesOff()
edgesFilter.ManifoldEdgesOff()
edgesFilter.NonManifoldEdgesOff()
edgesFilter.SetInputData(circularSegment)
edgesFilter.Update()
boundaryEdges = edgesFilter.GetOutput()

# The vtkConnectivityFilter allows for separation of both boundaries (in my case I only have two groups, so I use first and final cell seeds for separation)
connectivityFilter = vtk.vtkConnectivityFilter()
connectivityFilter.SetExtractionModeToCellSeededRegions()
connectivityFilter.AddInputData(boundaryEdges)
connectivityFilter.AddSeed(0)
connectivityFilter.Update()
proximalBorder = connectivityFilter.GetOutput()

connectivityFilter2 = vtk.vtkConnectivityFilter()
connectivityFilter2.SetExtractionModeToCellSeededRegions()
connectivityFilter2.AddInputData(boundaryEdges)
connectivityFilter2.AddSeed(boundaryEdges.GetCell(boundaryEdges.GetNumberOfPoints() - 1).GetPointId(0))
connectivityFilter2.Update()
distalBorder = connectivityFilter2.GetOutput()
</code></pre>
<p>Now I continued the code introducing the <code>vtkClipClosedSurface</code> filter to close the surface at the edges (criteria for plane definition are a bit too adapted at my example, just want it to work altogether):</p>
<pre><code class="lang-auto"># We have to define planes for the vtkClipClosedSurface filter. First pool all points from both groups
proximalBorderPoints = np.ndarray([proximalBorder.GetNumberOfPoints(), 3])
distalBorderPoints = np.ndarray([distalBorder.GetNumberOfPoints(), 3])

for idx in range(proximalBorder.GetNumberOfPoints()):
    proximalBorderPoints[idx] = proximalBorder.GetPoints().GetPoint(idx)  
for idx in range(distalBorder.GetNumberOfPoints()):
    distalBorderPoints[idx] = distalBorder.GetPoints().GetPoint(idx)
    
# Get point with maximal z coordinate in proximal boundary and minimum z coordinate in distal boundary
proximalBorderZMax = np.amax(proximalBorderPoints[:, 2])
distalBorderZMin = np.amin(distalBorderPoints[:, 2])

# Cutting planes definition
proximalPlane = vtk.vtkPlane()
proximalPlane.SetNormal(0, 0, 1)
proximalPlane.SetOrigin(0, 0, proximalBorderZMax)
distalPlane = vtk.vtkPlane()
distalPlane.SetNormal(0, 0, -1)
distalPlane.SetOrigin(0, 0, distalBorderZMin)
clippingPlanes = vtk.vtkPlaneCollection()
clippingPlanes.AddItem(proximalPlane)
clippingPlanes.AddItem(distalPlane)

# Application of the vtkClipClosedSurface filter
clip = vtk.vtkClipClosedSurface()
clip.AddInputData(circularSegment)
clip.SetClippingPlanes(clippingPlanes)
clip.Update()
clippedCircularSegment = clip.GetOutput()
</code></pre>
<p>Now the object looks all right:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89b5d01afdc99c3c7f8202047112cbcc44875775.jpeg" data-download-href="/uploads/short-url/jEeWDJ4pvkNb6ua74gYJnUY3LQV.jpeg?dl=1" title="sense nom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89b5d01afdc99c3c7f8202047112cbcc44875775_2_494x375.jpeg" alt="sense nom" data-base62-sha1="jEeWDJ4pvkNb6ua74gYJnUY3LQV" width="494" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89b5d01afdc99c3c7f8202047112cbcc44875775_2_494x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89b5d01afdc99c3c7f8202047112cbcc44875775_2_741x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89b5d01afdc99c3c7f8202047112cbcc44875775_2_988x750.jpeg 2x" data-dominant-color="616061"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sense nom</span><span class="informations">994×754 49.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am doing all of this in a Slicer context, and now I am trying to store it as a new segment in a vtkMRMLSegmentationNode. I am using the following line:</p>
<pre><code class="lang-auto">segmentationNode.AddSegmentFromClosedSurfaceRepresentation(clippedCircularSegment)
</code></pre>
<p>But this is not working (it returns an empty string). I have been able to define a new vtkMRMLModelNode and visualize the object in Slicer:</p>
<pre><code class="lang-auto">circularSegmentModelNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode")
circularSegmentModelNode.SetAndObservePolyData(clippedCircularSegment)
</code></pre>
<p>But I cannot add it as a new segment in the vtkMRMLSegmentationNode, which is what I would like to do, and I don’t really understand why… Any help with this?</p>

---
