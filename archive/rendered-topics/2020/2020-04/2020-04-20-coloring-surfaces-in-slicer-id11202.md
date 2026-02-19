---
topic_id: 11202
title: "Coloring Surfaces In Slicer"
date: 2020-04-20
url: https://discourse.slicer.org/t/11202
---

# Coloring surfaces in slicer

**Topic ID**: 11202
**Date**: 2020-04-20
**URL**: https://discourse.slicer.org/t/coloring-surfaces-in-slicer/11202

---

## Post #1 by @hcmidt (2020-04-20 13:47 UTC)

<p>Hello together,</p>
<p>I have written a couple of python scripts to analyze CT scan images and would like to depict the results in slicer.<br>
My script returns a 3d array that assigns a thickness to each point on a surface (let’s say the thickness is represented as an integer in [0,255], if that is important). The first thing I want to achieve is to depict the colored surface.</p>
<p>For the sake of simplicity let’s assume the surface is a sphere and one half of it should be colored in one color and the other in another color, according to some color-mapping. Here is an example that creates the array.</p>
<pre><code class="lang-auto">import numpy as np
from skimage.morphology import ball

b1 = ball(100)
b2 = ball(99)
b = np.copy(b1)
b[1:-1, 1:-1, 1:-1] -= b2
b[0:100][b[0:100] != 0] = 100
b[100:][b[100:] != 0] = 250
</code></pre>
<p>I want the half that is assigned the values <code>100</code> as one color and the other half that is assigned the values <code>250</code> in another color.</p>
<p>For now I am just storing this data in nrrd format and load it into slicer.</p>
<pre><code class="lang-auto">import itk
image = itk.GetImageFromArray(b)
itk.imwrite(image, '~/image.nrrd')
</code></pre>
<p>I have <em>tried</em> to use the <code>Probe volume with model</code> module (like suggested in <a href="https://discourse.slicer.org/t/how-to-analyze-the-thickness-of-the-model/2735/2" class="inline-onebox">How to analyze the thickness of the model</a>) as follows:</p>
<ol>
<li>Load the nrrd-file in slicer
<ul>
<li>This creates the <code>image</code> volume as expected</li>
</ul>
</li>
<li>Create a model from the <code>image</code> volume
<ul>
<li>The only way I found to achieve this was the <code>Grayscale model maker</code> module (with threshold set to 10 for the above example)</li>
<li>This returns a nice sphere surface, as expected, let’s call it <code>sphere_model</code>
</li>
</ul>
</li>
<li>Use the resulting <code>sphere_model</code> model and the <code>image</code> volume in the <code>Probe volume with model</code> module
<ul>
<li>this returns a model, let’s call it <code>probed_model</code>
</li>
<li>The <code>probed_model</code> appears as a green sphere. All the surface is uniformly covered with green color.</li>
</ul>
</li>
<li>Work the results with the <code>models</code> module
<ul>
<li>I tried to adjust things in the <code>Scalars</code> section of the module, but it has no effect on the depicted model.</li>
</ul>
</li>
</ol>
<p>What I am expecting to see is a <code>probed_model</code> that is colored `half-half’ with two different colors. I am new to slicer and I suppose I went wrong somewhere (and or did not yet find the right module).</p>
<p>I am running slicer on a MacBook (late 2013) with macOS Catalania 10.15.4 and I am using slicer version 4.10.2</p>
<p>Thanks for your help</p>

---

## Post #2 by @lassoan (2020-04-20 14:32 UTC)

<aside class="quote no-group" data-username="hcmidt" data-post="1" data-topic="11202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/59ef9b/48.png" class="avatar"> hcmidt:</div>
<blockquote>
<p>Create a model from the <code>image</code> volume</p>
</blockquote>
</aside>
<p>For trivial segmentation tasks (e.g., bone segmentation from CT), simple thresholding works, so “Grayscale model maker” module is usable. For most other cases, you can use Segment Editor module.</p>
<aside class="quote no-group" data-username="hcmidt" data-post="1" data-topic="11202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/59ef9b/48.png" class="avatar"> hcmidt:</div>
<blockquote>
<p>The <code>probed_model</code> appears as a green sphere. All the surface is uniformly covered with green color.</p>
</blockquote>
</aside>
<p>Probing with model adds a new scalar array to a model. You can use Models module’s Scalars section to make an array colorize the surface. If you have trouble setting this up then upload an example model somewhere (the result of probing) and post the link here.</p>

---

## Post #3 by @pieper (2020-04-20 14:50 UTC)

<p>Here’s an example that may help.  The purpose is to show a way to use C++ and python together, but it also illustrates all the mechanism needed to manipulate model scalar arrays from numpy arrays and manage the color mapping.</p>
<div class="lazyYT" data-youtube-id="xcQKj4yp2nw" data-youtube-title="SlicerCPPYY 2020 04 09" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/pieper/f9da3e0a73c70981b48d0747132526d5" target="_blank">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/pieper/f9da3e0a73c70981b48d0747132526d5" target="_blank">https://gist.github.com/pieper/f9da3e0a73c70981b48d0747132526d5</a></h4>
<h5>guide.py</h5>
<pre><code class="Python">
# Copyright Steve Pieper
# https://github.com/Slicer/Slicer/blob/master/License.txt
# Demo video: https://youtu.be/xcQKj4yp2nw

"""

exec(open('/Users/pieper/slicer/latest/SlicerTMSGuide/guide.py', 'r').read())

"""</code></pre>
This file has been truncated. <a href="https://gist.github.com/pieper/f9da3e0a73c70981b48d0747132526d5" target="_blank">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @hcmidt (2020-04-20 17:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="11202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For trivial segmentation tasks (e.g., bone segmentation from CT), simple thresholding works, so “Grayscale model maker” module is usable. For most other cases, you can use Segment Editor module.</p>
</blockquote>
</aside>
<p>Yes, indeed. The segmentation is not the problem I think. The problem is the coloring of the resulting surfaces. The sphere example I provided is just an instructive example to reproduce the issues I am facing with a simpler example.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="11202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probing with model adds a new scalar array to a model. You can use Models module’s Scalars section to make an array colorize the surface. If you have trouble setting this up then upload an example model somewhere (the result of probing) and post the link here.</p>
</blockquote>
</aside>
<p>Here is a link with the dataset that results on my machine, following the steps I described above: <a href="https://drive.google.com/open?id=1MN9jkQvmC0Ihu_MWEvcrCunLGFjcGTPe" class="inline-onebox" rel="noopener nofollow ugc">probed_model.vtk - Google Drive</a></p>

---

## Post #5 by @lassoan (2020-04-20 18:23 UTC)

<p>All the values in the scalar are set to the value of 10, which means that probably the generated volume was not right. Could you also upload the volume that you created?</p>

---

## Post #6 by @hcmidt (2020-04-20 18:24 UTC)

<p>This looks indeed helpful for what I have in mind. However, for the moment seems a bit overkill in order to understand the issue at hand for me. So I have tried to take a step back and just extract the scalar values. The result is insightful in some sense.</p>
<p>Running</p>
<pre><code class="lang-auto">modelNode = getNode('probed_model')
modelPointValues = modelNode.GetPolyData().GetPointData().GetArray("Normals")
</code></pre>
<p>in the slicer python prompt returns <code>None</code>. Running the same with the <code>sperical_model</code> returns a vtkFloatArray object that I can inspect.</p>
<p>So I suppose something might go wrong during the probing stage?</p>
<p>Thanks!</p>

---

## Post #7 by @hcmidt (2020-04-20 18:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="11202" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>All the values in the scalar are set to the value of 10, which means that probably the generated volume was not right. Could you also upload the volume that you created?</p>
</blockquote>
</aside>
<p>Yes, here it is: <a href="https://drive.google.com/open?id=1AcxCfIc9wHuoVL2Q4yWQyDINp0LZR4o3" class="inline-onebox" rel="noopener nofollow ugc">VolumeProperty.vp - Google Drive</a></p>

---

## Post #8 by @lassoan (2020-04-20 18:28 UTC)

<aside class="quote no-group" data-username="hcmidt" data-post="6" data-topic="11202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/59ef9b/48.png" class="avatar"> hcmidt:</div>
<blockquote>
<p>in the slicer python prompt returns <code>None</code> . Running the same with the <code>sperical_model</code> returns a vtkFloatArray object that I can inspect.</p>
<p>So I suppose something might go wrong during the probing stage?</p>
</blockquote>
</aside>
<p>Not, this is all looks good. Mesh processing modules may or may not add surface normals to the output. If you need surface normals and the modules that you used did not happen to provide them then you can apply vtkPolyDataNormals to the output (or if you want to use GUI, then use Surface Toolbox module).</p>

---

## Post #9 by @lassoan (2020-04-20 18:30 UTC)

<p>What you uploaded was the volume rendering property node. If you are not sure which file is which then you can click on the package icon and save the entire scene as a single .mrb file.</p>

---

## Post #10 by @hcmidt (2020-04-20 18:40 UTC)

<p>Perfect, here is the whole package: <a href="https://drive.google.com/open?id=1OsToo4BLIQldFbSPRsOtUhPuqoM1vpX3" rel="nofollow noopener">https://drive.google.com/open?id=1OsToo4BLIQldFbSPRsOtUhPuqoM1vpX3</a></p>

---

## Post #11 by @lassoan (2020-04-20 18:59 UTC)

<p>The scene file shows that you probed the same volume that you contoured! I have done this a few times before but of course this can never work, as per definition, the isosurface that you extract from a volume will have the same scalar value at all the surface points (the exact value that you specified for isosurface extraction). Since you have created your model by extracting the iso-value of 10, all the probed point scalars have the value of 10, which means both iso-surface extraction and probing worked perfectly.</p>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_simple_surface_mesh_as_a_model_node">this example</a> how to create a surface mesh using a VTK source. You can use a <code>vtkSphereSource</code> to create a sphere model.</p>

---

## Post #12 by @hcmidt (2020-04-20 19:37 UTC)

<p>All right, thanks! I thought that by applying the <code>Probe volume with model</code> module, the surface values would change according to the values of the volume. But I clearly misunderstood.</p>
<p>Then back to the original problem: how can I achieve what I want to do in slicer? If we stick to the example I gave. How do I extract the surface model and then color this surface model according to the entries in the array that defines the surface?</p>

---

## Post #13 by @lassoan (2020-04-21 00:17 UTC)

<aside class="quote no-group" data-username="hcmidt" data-post="12" data-topic="11202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/59ef9b/48.png" class="avatar"> hcmidt:</div>
<blockquote>
<p><code>Probe volume with model</code> module, the surface values would change according to the values of the volume</p>
</blockquote>
</aside>
<p>You carefuly built your mesh so that each point lies in positions that all have the exact same scalar value. So, probing will always give you that same scalar value for each point.</p>
<aside class="quote no-group" data-username="hcmidt" data-post="12" data-topic="11202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/59ef9b/48.png" class="avatar"> hcmidt:</div>
<blockquote>
<p>Then back to the original problem: how can I achieve what I want to do in slicer? If we stick to the example I gave. How do I extract the surface model and then color this surface model according to the entries in the array that defines the surface?</p>
</blockquote>
</aside>
<p>You did it well. Just don’t create your model by iso-surfacing the same volume that you use for coloring.</p>
<aside class="quote no-group" data-username="hcmidt" data-post="12" data-topic="11202">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/59ef9b/48.png" class="avatar"> hcmidt:</div>
<blockquote>
<p>Then back to the original problem: how can I achieve what I want to do in slicer?</p>
</blockquote>
</aside>
<p>Extracting a medial surface from a volume is not a trivial operation. If during your skeletonization operation you have not built a data structure that preserved your original topology then you need to reconstruct the surface from point cloud in the end. VTK has many tools for this. For example, you can <a href="https://vtk.org/doc/nightly/html/classvtkImageToPoints.html">convert voxel data to points</a>, remove zero-valued points using <a href="https://vtk.org/doc/nightly/html/classvtkThreshold.html">thresholding</a>, then create a surface using one of the <a href="https://lorensen.github.io/VTKExamples/site/Cxx/Points/PoissonExtractSurface/">surface reconstruction filters</a>. These all should not be more than 10-20 lines of Python code in total.</p>

---

## Post #14 by @hcmidt (2020-04-21 11:13 UTC)

<p>Ok, great. I am not familiar with vtk, but it seems there are some good resources. I’ll try to learn about it and give an update once I have made some progress.</p>
<p>Thank you!</p>

---

## Post #15 by @hcmidt (2020-04-24 14:07 UTC)

<p>Hello together,</p>
<p>I have had my try on some vtk. I manage to do what I intended to do in vtk now, but I am failing to incorporate it properly in slicer.</p>
<p>Here is a minimalistic example of my code that should run from within slicer (after installing scipy, which I did as described in the forum):</p>
<pre><code class="lang-auto">import numpy as np
from scipy.ndimage.filters import maximum_filter
from vtk.util.numpy_support import vtk_to_numpy
from vtk.util.numpy_support import numpy_to_vtk


def ball(radius, dtype=np.uint8):
    n = 2 * radius + 1
    Z, Y, X = np.mgrid[-radius:radius:n * 1j,
                       -radius:radius:n * 1j,
                       -radius:radius:n * 1j]
    s = X ** 2 + Y ** 2 + Z ** 2
    return np.array(s &lt;= radius * radius, dtype=dtype)


def get_colored_model(index=0):
	segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
	referenceVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
	labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
	# extract mask
	slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, referenceVolumeNode)
	# apply marching cubes
	contour = vtk.vtkDiscreteMarchingCubes()
	contour.SetInputData(labelmapVolumeNode.GetImageData())
	contour.ComputeScalarsOn()
	contour.SetValue(0, index)
	contour.Update()
	# smoothen mesh
	smoother = vtk.vtkWindowedSincPolyDataFilter()
	smoother.SetInputConnection(contour.GetOutputPort())
	smoother.SetNumberOfIterations(30) 
	smoother.NonManifoldSmoothingOn()
	smoother.NormalizeCoordinatesOn()
	smoother.Update()
	smoothedMesh = smoother.GetOutput()
	# cell normals
	triangleCellNormals = vtk.vtkPolyDataNormals()
	triangleCellNormals.SetInputData(smoothedMesh)
	triangleCellNormals.ComputeCellNormalsOn()
	triangleCellNormals.ComputePointNormalsOff()
	triangleCellNormals.ConsistencyOn()
	triangleCellNormals.AutoOrientNormalsOn()
	triangleCellNormals.Update()
	# get mask from segmentation
	labelmapArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
	# extract volume
	referenceVolumeArray = slicer.util.arrayFromVolume(referenceVolumeNode)
	# mask original volume
	# maskedVolumeArray = np.copy(labelmapArray*referenceVolumeArray)
	maskedVolumeArray = labelmapArray * referenceVolumeArray
	maskedVolumeArray = maskedVolumeArray.transpose(2,1,0)
	# map volume values to surface
	coords = vtk_to_numpy(triangleCellNormals.GetOutput().GetPoints().GetData())
	voi_array = maximum_filter(maskedVolumeArray, footprint=ball(5))
	mn = voi_array[voi_array &gt; 0].min()
	mx = voi_array[voi_array &gt; 0].max()
	voi_array = (voi_array-mn) / (mx-mn)
	vals = voi_array[tuple(coords.astype(np.int).T)]
	vtk_data_array = numpy_to_vtk(vals)
	triangleCellNormals.GetOutput().GetPointData().SetScalars(vtk_data_array)
	# for mesh model
	myNode = slicer.modules.models.logic().AddModel(triangleCellNormals.GetOutputPort())
	# Show scalar values at surface of a model
	myNode.GetDisplayNode().ScalarVisibilityOn()
</code></pre>
<p>And here is the example data:<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1MoxMcTeA0RqUW67VGNldHtLc1qyZmTRL/view?usp=drive_open" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1MoxMcTeA0RqUW67VGNldHtLc1qyZmTRL/view?usp=drive_open" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1MoxMcTeA0RqUW67VGNldHtLc1qyZmTRL/view?usp=drive_open" target="_blank" rel="nofollow noopener">example.nrrd</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The workflow would be the following:</p>
<ol>
<li>load <code>example.nrrd</code> in slicer</li>
<li>open the segment editor and extract the segment by applying the threshold operation.</li>
<li>run the <code>get_colored_model</code> function from the python interactor within slicer</li>
<li>The result is a correctly colored mesh as I intended</li>
</ol>
<p>I am doing things without really understanding the slicer api and I am not very happy with my solution for the following reasons:<br>
a) The model appears as an independent model, not linked to the original volume/segment (in the 3D viewer it appears as a kind of mirror-version, next to the original volume/segment).<br>
For the moment this is fine, but it would be nicer to have the model be linked to the rest. I am planing to write a small extension to slicer that can automatically apply the algorithm.<br>
b) I cannot interact with the colors of the resulting model in the <code>Models module</code>. When I try to change the color table or anything else, the depiction breaks and suddenly depicts nonsense. Ideally I would like to be able to change the color table from within slicer.</p>
<p>Is it possible to adapt the code to incorporate the last points?<br>
Thanks in advance!</p>

---

## Post #16 by @hcmidt (2020-04-24 20:07 UTC)

<p>I resolved (b). There was a problem with the color mapping and also a bug because I got too used to Python3 (however it did not play a role for the specific example above).<br>
<code>voi_array = (voi_array-mn) / (mx-mn)</code> should be replaced by<br>
<code>voi_array = (voi_array-mn) / float(mx-mn) * 255</code> to resolve the coloring issues.</p>
<p>I’ll try to work out (a) next.</p>

---

## Post #17 by @lassoan (2020-04-24 20:26 UTC)

<p>If you enable “Show 3D” option in the Segment Editor then you can see a 3D representation synchronized with the labelmap representation (internally quite similarly as you did it).</p>
<p>If you need the result as models (surface meshes) then Segment editor can create them you, just right-click on the segmentation node in Data module and choose export to model node.</p>

---

## Post #18 by @hcmidt (2020-04-24 21:54 UTC)

<p>Thanks! I was looking for this functionality before but did not manage to find it.<br>
Could you tell me how I can do that on the python level?</p>

---

## Post #19 by @lassoan (2020-04-24 22:48 UTC)

<p>You can find Python examples for all commonly needed operations and complete workflow examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations">script repository</a>.</p>

---

## Post #20 by @hcmidt (2020-04-25 02:14 UTC)

<p>Thanks. I have been looking at the repository and I am managing to extract the modelNode like so:</p>
<pre><code class="lang-auto">modelHierarchyNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelHierarchyNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToModelHierarchy(segmentationNode, modelHierarchyNode)
modelNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLModelNode")
</code></pre>
<p>However, I <em>don’t manage to project the volume values onto the scalar values of the model like I did in my example</em>.</p>
<p>In case this is informative: the coordinates returned by<br>
<code>vtk_to_numpy(modelNode.GetPolyData().GetPoints().GetData())</code> are only four points</p>
<pre><code class="lang-auto">[[  54.22350311, -200.5       ,  100.        ],
 [-254.22349548, -200.5       ,  100.        ],
 [  54.22350311,    0.5       ,  100.        ],
 [-254.22349548,    0.5       ,  100.        ]]
</code></pre>
<p>which I found a bit strange.</p>
<p>I could not find anything in the script repository to help. I suppose I am doing sth wrong somewhere.</p>
<p>Edit: I have also tried to apply again the <code>Probe Volume With Model</code> module, but it does not resolve the issue. It gives me a proper array of coordinates, but since they are in a different coordinate system it still does not allow to apply my mapping for the Scalar Values.<br>
Sorry, I am a bit lost in between different slicer-objects :&gt;</p>

---

## Post #21 by @lassoan (2020-04-25 03:02 UTC)

<p>You can get model point positions as numpy array using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPoints">arrayFromModelPoints</a> and point scalars (if you have added point scalar array) using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromModelPointData">arrayFromModelPointData</a>, but it would be much slower and more complicated to process the meshes using numpy.</p>
<p>Instead, you can extract non-zero voxels from your volume using <a href="https://vtk.org/doc/nightly/html/classvtkThreshold.html">vtkThreshold</a> then interpolate values onto the isosurface using <a href="https://vtk.org/doc/nightly/html/classvtkPointInterpolator.html">vtkPointInterpolator</a>.</p>

---
