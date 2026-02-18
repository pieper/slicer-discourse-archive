# Approximate anatomical axis (curve) of long bone

**Topic ID**: 20600
**Date**: 2021-11-12
**URL**: https://discourse.slicer.org/t/approximate-anatomical-axis-curve-of-long-bone/20600

---

## Post #1 by @mau_igna_06 (2021-11-12 12:14 UTC)

<p>Hi devs.</p>
<p>I developed a script to parcelate a long bone. This parcells can then be used to calculate their centroids and with that points create the anatomical axis (curve).</p>
<p>Right now the script is missing somo thresholds and consideration of special cases to find the centroids of the parcelated pieces and create the curve from them.</p>
<p>Do you think I should finish it? or there is some limitations I’m not considering that would make this algorithm not work?</p>
<p>It searches the surface’s first principal component vector and uses it as normal of a plane with origin in the centroid of the bone to cut it and use that intersection as input for the geodesicDistanceFilter.</p>
<p>Here are some pictures:</p>
<ul>
<li>
<p>Big parcelations<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c59d124712aec85386fba16ae33393a98d83a2c8.png" data-download-href="/uploads/short-url/scaAj1yLgmS9LCcpOqgfWREMN6M.png?dl=1" title="fibulaParcelated" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c59d124712aec85386fba16ae33393a98d83a2c8_2_690x345.png" alt="fibulaParcelated" data-base62-sha1="scaAj1yLgmS9LCcpOqgfWREMN6M" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c59d124712aec85386fba16ae33393a98d83a2c8_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c59d124712aec85386fba16ae33393a98d83a2c8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c59d124712aec85386fba16ae33393a98d83a2c8.png 2x" data-dominant-color="9899CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fibulaParcelated</span><span class="informations">790×395 26.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f6eae10c9467740ea123b73c5366fbc6cef962a.png" data-download-href="/uploads/short-url/fTM83m6CSO9rLwxsTxo3c5PWfrA.png?dl=1" title="femurBigParcelations" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f6eae10c9467740ea123b73c5366fbc6cef962a_2_690x345.png" alt="femurBigParcelations" data-base62-sha1="fTM83m6CSO9rLwxsTxo3c5PWfrA" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f6eae10c9467740ea123b73c5366fbc6cef962a_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f6eae10c9467740ea123b73c5366fbc6cef962a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f6eae10c9467740ea123b73c5366fbc6cef962a.png 2x" data-dominant-color="9492C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">femurBigParcelations</span><span class="informations">790×395 72.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Small parcelations<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/935f0bde00bc626d89f626447601a698e6c9e84e.png" data-download-href="/uploads/short-url/l1HP5ADCo8fYBWrn8fDT4aBJ0K2.png?dl=1" title="femurSmallParcelations" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/935f0bde00bc626d89f626447601a698e6c9e84e_2_690x345.png" alt="femurSmallParcelations" data-base62-sha1="l1HP5ADCo8fYBWrn8fDT4aBJ0K2" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/935f0bde00bc626d89f626447601a698e6c9e84e_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/935f0bde00bc626d89f626447601a698e6c9e84e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/935f0bde00bc626d89f626447601a698e6c9e84e.png 2x" data-dominant-color="9295C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">femurSmallParcelations</span><span class="informations">790×395 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
<p>Here is the script:</p>
<pre><code class="lang-auto">
# find anatomical axis curve of bone

import numpy as np

model = getNode('mymodel')
parcelationLength = 9

numberOfSampledPointsOfModel = 2000
if model.GetPolyData().GetNumberOfPoints() &gt; numberOfSampledPointsOfModel:
  maskPointsFilter = vtk.vtkMaskPoints()
  maskPointsFilter.SetInputData(model.GetPolyData())
  # 
  ratio = round(model.GetPolyData().GetNumberOfPoints()/numberOfSampledPointsOfModel)
  # 
  # This works but the sampling could be biased spatially I think
  # If you have vtk9 you should use UNIFORM_SPATIAL_SURFACE option
  maskPointsFilter.SetOnRatio(ratio)
  maskPointsFilter.RandomModeOn()
  maskPointsFilter.Update()
  # 
  polydata = vtk.vtkPolyData()
  polydata.ShallowCopy(maskPointsFilter.GetOutput())
  # 
  # Calculate the SVD and mean
  from vtk.util.numpy_support import vtk_to_numpy
  modelPoints = vtk_to_numpy(polydata.GetPoints().GetData())
else:
  from vtk.util.numpy_support import vtk_to_numpy
  modelPoints = vtk_to_numpy(model.GetPolyData().GetPoints().GetData())


# Calculate the mean of the points, i.e. the 'center' of the cloud
modelPointsMean = modelPoints.mean(axis=0)

# Do an SVD on the mean-centered data.
uu, dd, rightSingularVectors = np.linalg.svd(modelPoints - modelPointsMean)

# Create a frame for the model
modelZ = np.zeros(3)
modelX = rightSingularVectors[0]


# Cut the bone at the half and find the centroid
plane = vtk.vtkPlane()
plane.SetOrigin(modelPointsMean)
plane.SetNormal(modelX)

cutter = vtk.vtkCutter()
cutter.SetInputData(model.GetPolyData())
cutter.SetCutFunction(plane)
cutter.Update()

pointData = cutter.GetOutput().GetPoints().GetData()
from vtk.util.numpy_support import vtk_to_numpy
seedPoints = vtk_to_numpy(pointData)

meshLocator = vtk.vtkPointLocator()
meshLocator.SetDataSet(model.GetMesh())

seeds = vtk.vtkIdList()
for i in range(len(seedPoints)):
  pointIDOfClosestPoint = meshLocator.FindClosestPoint(seedPoints[i]);
  seeds.InsertNextId(pointIDOfClosestPoint);

geodesicDistance = slicer.vtkFastMarchingGeodesicDistance()
geodesicDistance.SetInputData(model.GetPolyData());
geodesicDistance.SetFieldDataName('GeodesicDistance')
geodesicDistance.SetSeeds(seeds)
geodesicDistance.Update()


parcelatedRegions = vtk.vtkPolyData()
parcelatedRegions.ShallowCopy(geodesicDistance.GetOutput())

pointScalars = parcelatedRegions.GetPointData()
distanceArray = pointScalars.GetArray("GeodesicDistance")

tempParcelationArray = vtk.vtkIntArray()
tempParcelationArray.SetName('TempParcelationArray')
numberOfPoints = parcelatedRegions.GetNumberOfPoints()
tempParcelationArray.SetNumberOfValues(numberOfPoints)
tempParcelationArray.Fill(0)

for i in range(parcelatedRegions.GetNumberOfPoints()):
  distance = distanceArray.GetTuple1(i)
  if distance &lt; (parcelationLength/2):
    parcellID = 0
  else: 
    parcellID = int((distance-parcelationLength/2) // parcelationLength) +1
  tempParcelationArray.SetTuple1(i,parcellID)

pointScalars.AddArray(tempParcelationArray)

model.SetAndObservePolyData(parcelatedRegions)

# Set up coloring by selection array
model.GetDisplayNode().SetActiveScalar("TempParcelationArray", vtk.vtkAssignAttribute.POINT_DATA)
model.GetDisplayNode().SetAndObserveColorNodeID("vtkMRMLProceduralColorNodeRandomIntegers")
scalarRange = model.GetDisplayNode().GetScalarRange()
model.GetDisplayNode().SetAutoScalarRange(False)
model.GetDisplayNode().SetScalarRange(-1,scalarRange[1])
model.GetDisplayNode().SetScalarVisibility(True)
</code></pre>
<p>I wonder how it would work with deformed bones because if it works well it could be used by researchers.</p>
<p>I was thinking that maybe the geodesic distance should be weighted by the inverse of the curvature (there is an option for this in the filter) but I’m not sure it would give me a usable result. I think the propagation speed may vary too much. What do you think?</p>

---

## Post #2 by @lassoan (2021-11-12 16:27 UTC)

<p>For long curved structures I would use <a href="https://github.com/vmtk/SlicerExtension-VMTK">VMTK</a> for simple geometry based or Voronoi diagram based centerline extraction. The resulting curve can be used to reslice and quantify the cross-sections using <a href="https://github.com/vmtk/SlicerExtension-VMTK/tree/master/CrossSectionAnalysis#readme">Cross-section analysis module</a>.</p>
<p>Maybe you could also discuss applications with <a class="mention" href="/u/jmhuie">@jmhuie</a> (developer of <a href="https://github.com/jmhuie/Slicer-SegmentGeometry">SegmentGeometry extension</a>), who so far worked with straight axes but might be interested in curved axes as well.</p>

---

## Post #3 by @jmhuie (2021-11-16 15:58 UTC)

<p>This seems like a neat feature.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe you could also discuss applications with <a class="mention" href="/u/jmhuie">@jmhuie</a> (developer of <a href="https://github.com/jmhuie/Slicer-SegmentGeometry" rel="noopener nofollow ugc">SegmentGeometry extension </a>), who so far worked with straight axes but might be interested in curved axes as well.</p>
</blockquote>
</aside>
<p>Ultimately, it could be cool to implement the ability to slice through a curve structure, while following the trajectory curvature. Although, I am not sure that this the way to do it. It could be used to measure the length of a curved structure for sure.</p>

---

## Post #4 by @lassoan (2021-11-16 22:54 UTC)

<aside class="quote no-group" data-username="jmhuie" data-post="3" data-topic="20600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jmhuie/48/7086_2.png" class="avatar"> jmhuie:</div>
<blockquote>
<p>Ultimately, it could be cool to implement the ability to slice through a curve structure, while following the trajectory curvature</p>
</blockquote>
</aside>
<p>You can already do this using <a href="https://github.com/vmtk/SlicerExtension-VMTK#readme">SlicerVMTK extension</a>. You can even straighten a curved structure (preserving length and cross-section shape) using Sandbox extension’s Curved Planar Reformat module.</p>

---

## Post #5 by @mikebind (2021-11-29 20:45 UTC)

<p>I was attempting to give this script a try, but I get an error that <code>slicer.vtkFastMarchingGeodesicDistance()</code> does not exist.  Might I be missing a needed extension?  If so, which one?</p>

---

## Post #6 by @mau_igna_06 (2021-11-29 22:08 UTC)

<p>You just need latest Slicer Preview Release.<br>
It’s the same filter used by DynamicModeler’s SelectByPoints tool</p>

---

## Post #7 by @mikebind (2021-11-30 16:57 UTC)

<p>OK, thanks, I have been using 2021-10-14, so I’ll update again.</p>

---
