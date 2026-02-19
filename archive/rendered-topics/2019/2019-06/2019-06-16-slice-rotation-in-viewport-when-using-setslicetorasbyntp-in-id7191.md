---
topic_id: 7191
title: "Slice Rotation In Viewport When Using Setslicetorasbyntp In"
date: 2019-06-16
url: https://discourse.slicer.org/t/7191
---

# Slice rotation in viewport when using SetSliceToRASByNTP in python

**Topic ID**: 7191
**Date**: 2019-06-16
**URL**: https://discourse.slicer.org/t/slice-rotation-in-viewport-when-using-setslicetorasbyntp-in-python/7191

---

## Post #1 by @talmazov (2019-06-16 22:17 UTC)

<p>hey guys,<br>
I have been trying to debug this issue to no avail and I’m hoping someone could help me out or point me in some direction. Please refer to my stackoverflow post, feel free to answer here or there. If solution or discussion occurs here I can post it in stackoverflow.</p>
<aside class="onebox stackexchange">
  <header class="source">
      <a href="https://stackoverflow.com/questions/56622542/3d-slicer-viewport-rotation-on-model-path-in-python" target="_blank" rel="nofollow noopener">stackoverflow.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/455343/mayotic" target="_blank" rel="nofollow noopener">
    <img alt="mayotic" src="https://lh3.googleusercontent.com/-2vyDkVE5u-Y/AAAAAAAAAAI/AAAAAAAAAAs/SzAZsudJjgI/photo.jpg?sz=128" class="thumbnail onebox-avatar" width="128" height="128">
  </a>
<h4>
  <a href="https://stackoverflow.com/questions/56622542/3d-slicer-viewport-rotation-on-model-path-in-python" target="_blank" rel="nofollow noopener">3D Slicer viewport rotation on model path in python</a>
</h4>

<div class="tags">
  <strong>python, 3d, medical</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/455343/mayotic" target="_blank" rel="nofollow noopener">
    mayotic
  </a>
  on <a href="https://stackoverflow.com/questions/56622542/3d-slicer-viewport-rotation-on-model-path-in-python" target="_blank" rel="nofollow noopener">08:50PM - 16 Jun 19 UTC</a>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-06-17 04:09 UTC)

<p>Determining a smoothly changing curve normal direction is not a trivial task. In recent Slicer versions, we introduced curve node, which can provide curve tangent and normal using <a href="https://lorensen.github.io/VTKExamples/site/Cxx/Remote/FrenetSerretFrame/">Frenet-Serret frame</a>.</p>
<p>Here is a complete example of computing a panoramic X-ray from a cone-beam dental CT. Just a demonstration of how an image can be resampled along a curve - the code is not optimized for performance or quality and distance along curve is not scaled (we simply used all point indices instead of retrieving point indices based on desired distance along curve).</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07">
  <header class="source">

      <a href="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07" target="_blank" rel="noopener">https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07</a></h4>

  <h5>CurvedPlanarReformatting.py</h5>
  <pre><code class="Python"># Get a dental CT scan
import SampleData
volumeNode = SampleData.SampleDataLogic().downloadDentalSurgery()[1]

# Define curve
curveNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsCurveNode')
curveNode.CreateDefaultDisplayNodes()
curveNode.GetCurveGenerator().SetNumberOfPointsPerInterpolatingSegment(25) # add more curve points between control points than the default 10
curveNode.AddControlPoint(vtk.vtkVector3d(-45.85526315789473,	-104.59210526315789,	74.67105263157896))
curveNode.AddControlPoint(vtk.vtkVector3d(-50.9078947368421,	-90.06578947368418,	66.4605263157895))</code></pre>
    This file has been truncated. <a href="https://gist.github.com/lassoan/b445c734f118a5fb7643f3fb05f98b07" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Computed panoramic X-ray:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37fbf16c15fdbd71230b7b9dcf22a6b9c85a067a.jpeg" data-download-href="/uploads/short-url/7Zg2Si33dDIFDMTHnOQqIuVqCRc.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37fbf16c15fdbd71230b7b9dcf22a6b9c85a067a_2_690x163.jpeg" alt="image" data-base62-sha1="7Zg2Si33dDIFDMTHnOQqIuVqCRc" width="690" height="163" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37fbf16c15fdbd71230b7b9dcf22a6b9c85a067a_2_690x163.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37fbf16c15fdbd71230b7b9dcf22a6b9c85a067a_2_1035x244.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37fbf16c15fdbd71230b7b9dcf22a6b9c85a067a.jpeg 2x" data-dominant-color="545454"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1145×271 38.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @talmazov (2019-06-26 22:27 UTC)

<p>Hey,<br>
Really cool algorithm. I am trying to implement it but I am running into this error</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/talmazovg/SlicerDev/SlicerPano/SlicerPano/SlicerPano/SlicerPano.py”, line 234, in onCreatePathButtonClicked<br>
test.construct_pano(self.path)<br>
File “C:/Users/talmazovg/SlicerDev/SlicerPano/SlicerPano/SlicerPano/SlicerPano.py”, line 604, in construct_pano<br>
curveNode.CreateDefaultDisplayNodes()<br>
AttributeError: ‘NoneType’ object has no attribute ‘CreateDefaultDisplayNodes’</p>
<p>invoking curveNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLMarkupsCurveNode’) return NoneType object.</p>
<p>I am new to slicer programming so I apologize, am I not importing a class or something?<br>
Using Slicer 4.10.2<br>
Thanks!</p>

---

## Post #4 by @jamesobutler (2019-06-26 23:07 UTC)

<p>“vtkMRMLMarkupsCurveNode” is only available in the Slicer nightly (4.11) which is why it is not working for you in Slicer 4.10.2</p>

---

## Post #5 by @talmazov (2019-06-27 00:59 UTC)

<p>Based on my original question, how is it that the 3D world view retains proper orientation of the plane while the node view is flipped? Please refer to screenshot.<br>
Is there some way I can anchor the plane to be parallel in the axial direction?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8614f43d645c30833ea69f58dc1bd4f3cc36e1ec.png" data-download-href="/uploads/short-url/j88Sf9EY4FvZ3PixIw2bSEuHBwg.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/8614f43d645c30833ea69f58dc1bd4f3cc36e1ec_2_388x500.png" alt="Capture" data-base62-sha1="j88Sf9EY4FvZ3PixIw2bSEuHBwg" width="388" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/8614f43d645c30833ea69f58dc1bd4f3cc36e1ec_2_388x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8614f43d645c30833ea69f58dc1bd4f3cc36e1ec.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8614f43d645c30833ea69f58dc1bd4f3cc36e1ec.png 2x" data-dominant-color="494A53"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">513×660 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2019-06-27 04:05 UTC)

<p>You can arbitrarily rotate the slice view content in the image plane or flip it along any axis, the physical position of the slice will still remain the same.</p>
<p>In your script, you computed the normal direction of the curve inconsistently along the curve (you flipped the normal direction along the curve), that’s why you see a flip in the slice view. If the curve is quasi planar then you can use the curve normal computation method implemented that is implemented in endoscopy module as is (that uses the normal of the plane fit to the curve; a reslicing transform is written to the scene that you can use in Volume reslice driver - <a href="https://youtu.be/thExIlffL0I" rel="nofollow noopener">see this video for step-by-step instructions</a>). For arbitrary curve shapes, you can use Frenet-Serret frame (that is implemented in recent Slicer preview versions in curves, see my script <a href="https://discourse.slicer.org/t/slice-rotation-in-viewport-when-using-setslicetorasbyntp-in-python/7191/2">above</a> for a complete working example).</p>

---

## Post #8 by @lassoan (2019-12-18 01:26 UTC)

<p>We now added a module that automates the reformat and creates curved planar reformatted volumes: <a href="https://discourse.slicer.org/t/how-to-implement-cpr-curved-plannar-reconstruction-from-centerline/9456/3" class="inline-onebox">How to implement CPR (curved plannar reconstruction) from centerline?</a></p>

---

## Post #9 by @lassoan (2019-12-31 15:07 UTC)

<p>A post was split to a new topic: <a href="/t/create-curve-from-many-input-points/9673">Create curve from many input points</a></p>

---
