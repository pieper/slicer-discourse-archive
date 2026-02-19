---
topic_id: 20868
title: "Surface Mesh With Multiple Scalar Data"
date: 2021-12-01
url: https://discourse.slicer.org/t/20868
---

# Surface mesh with multiple scalar data

**Topic ID**: 20868
**Date**: 2021-12-01
**URL**: https://discourse.slicer.org/t/surface-mesh-with-multiple-scalar-data/20868

---

## Post #1 by @gerroba (2021-12-01 18:35 UTC)

<p>Hello Slicer community,<br>
I am trying to load a Polydata vtk file that I created using Matlab that contains a surface mesh with multiple scalar variables associated. I am able to load the file (test1.vtk) in Paraview and play with the scalar values using the “Find data” option but I can not load it in Slicer because it gives me the following error:</p>
<p>“Failed to load model from VTK file […] test1.vtk as it does not contain polydata nor unstructured grid. The file might be loadable as a volume”.</p>
<p>I can not load it as a volume and I have also tried to create a different VTK file that contains the scalar values but displays the anatomy in a rare fashion in Slicer (test2.vtk).</p>
<p>Here are the files:<br>
test1.vtk: <a href="https://drive.google.com/file/d/1agI0Fxfp7oaztQ8kQulg5IziYzt4py4m/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">test1.vtk - Google Drive</a><br>
test2.vtk: <a href="https://drive.google.com/file/d/1agNL2vAzJAlnUYIxuy7Swz6W7Wu3qwnA/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">test2.vtk - Google Drive</a></p>
<p>Any help would be appreciated!</p>
<p>Thanks in advance,</p>
<p>Gerard</p>

---

## Post #2 by @lassoan (2021-12-02 17:46 UTC)

<p>Slicer supports loading of surface meshes (polydata) and volumetric meshes (unstructured grid).</p>
<p>The data set that you get from from the EP mapping system is just a point cloud (earlier CartoEP versions were also able to export the reconstructed surface but more recent ones just provide the points).</p>
<p>The simplest way to store a point cloud is to use a POLYDATA. You can fix test1.vtk by replacing</p>
<pre><code class="lang-auto">DATASET STRUCTURED_GRID
DIMENSIONS 49328 1 1 
</code></pre>
<p>by</p>
<pre><code class="lang-auto">DATASET POLYDATA 
</code></pre>
<p>You can load this file into Slicer and visualize by applying a vtkGlyph3D filter - by copy-pasting this into the Python console:</p>
<pre data-code-wrap="python"><code class="lang-python">pointsModelNode = getNode('test1')
glypher = vtk.vtkGlyph3D()
glypher.SetInputConnection(pointsModelNode.GetPolyDataConnection())
glyph = vtk.vtkSphereSource()
glypher.SetSourceConnection(glyph.GetOutputPort())
glypher.SetScaleModeToDataScalingOff()
glypher.Update()
glyphedModel = slicer.modules.models.logic().AddModel(glypher.GetOutputPort())
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab85c317a1d0fed7b980ca32aa31b03a7a841684.jpeg" data-download-href="/uploads/short-url/otmelqlMuVOCswaLbCsbSOjsR2A.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab85c317a1d0fed7b980ca32aa31b03a7a841684_2_656x500.jpeg" alt="image" data-base62-sha1="otmelqlMuVOCswaLbCsbSOjsR2A" width="656" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab85c317a1d0fed7b980ca32aa31b03a7a841684_2_656x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab85c317a1d0fed7b980ca32aa31b03a7a841684_2_984x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab85c317a1d0fed7b980ca32aa31b03a7a841684_2_1312x1000.jpeg 2x" data-dominant-color="7674A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1564×1192 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can also reconstruct a surface:</p>
<pre data-code-wrap="python"><code class="lang-python">pointsModelNode = getNode('test1')
numberOfSamples = 256.0
normalSamplingFactor = 5e-5

polyData = pointsModelNode.GetPolyData()

sampleSize = max(polyData.GetNumberOfPoints() * normalSamplingFactor, 10)
normals = vtk.vtkPCANormalEstimation()
normals.SetInputData(polyData)
normals.SetSampleSize(sampleSize)
normals.SetNormalOrientationToGraphTraversal()
normals.FlipNormalsOff()

distance = vtk.vtkSignedDistance()
distance.SetInputConnection(normals.GetOutputPort())

boundingBox = vtk.vtkBoundingBox()
boundingBox.SetBounds(polyData.GetBounds())

radius = boundingBox.GetMaxLength() / numberOfSamples * 4.0  # about 4 voxels
distance.SetRadius(radius)
boundingBox.Inflate(boundingBox.GetLength(0) * .1, boundingBox.GetLength(1) * .1, boundingBox.GetLength(2) * .1)
distance.SetDimensions(int(numberOfSamples), int(numberOfSamples), int(numberOfSamples))
bounds = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
boundingBox.GetBounds(bounds)
distance.SetBounds(bounds)

surface = vtk.vtkExtractSurface()
surface.SetInputConnection(distance.GetOutputPort())
surface.SetRadius(radius * .99)
surfaceModel = slicer.modules.models.logic().AddModel(surface.GetOutputPort())
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/949d931974111992d020df8af6d10bb7bbade37c.png" alt="image" data-base62-sha1="lcIgAU7EnAcLqEcGS8VF5HN19F2" width="460" height="364"></p>
<p>We also have a small <a href="https://github.com/stephan1312/SlicerEAMapReader">Slicer extension that can import EP maps</a> that you might find useful. They could be improved to reconstruct the surface, etc. as has been discussed <a href="https://discourse.slicer.org/t/import-carto-electroanatomic-maps-to-slicer/19316/6">here</a>, so you might do without Matlab and just do all your analysis and visualization in Python.</p>
<p>What kind of visualization and analysis would you like to do?</p>

---

## Post #3 by @gerroba (2021-12-03 13:05 UTC)

<p>Dear Andras,<br>
Thanks for your help and suggestions. I will definitely take a look at the SlicerEAMapReader extension as I am sure it will simplify my workflow.<br>
In our project we have LA infarcted pigs with EP maps and histology studies. I am using Slicer to segment the fibrosis of the histology sections and to merge this information with the EP maps. I want to correlate the regions of fibrosis to the values of bipolar voltage, etc.<br>
Thanks again!</p>

---

## Post #4 by @lassoan (2021-12-05 01:51 UTC)

<p>What do you mean by “correlate the regions of fibrosis”?</p>
<p>Do you want to just visualize the regions or you need quantitative analysis, too?</p>
<p>How do you plan to align the histology sections? Do you have some landmarks that are visible in both of them that you can use for registration?</p>

---

## Post #5 by @gerroba (2021-12-21 14:47 UTC)

<p>I would like to visualize and also perform a quantitative analysis (if I can).<br>
I am aligning the histology sections with the tool of TrakEM2 of Image J. I am now segmenting the histology sections to create two 3D volumes, one with the scar and one with the healthy regions. My plan is to use visual landmarks in both techniques for registration.<br>
Once this is done I want to study the bipolar values inside and outside the areas of fibrosis.</p>

---
