---
topic_id: 25048
title: "Grid Projection To Make Uniform Landmarks"
date: 2022-09-02
url: https://discourse.slicer.org/t/25048
---

# Grid projection to make uniform landmarks

**Topic ID**: 25048
**Date**: 2022-09-02
**URL**: https://discourse.slicer.org/t/grid-projection-to-make-uniform-landmarks/25048

---

## Post #1 by @joanne40226 (2022-09-02 03:23 UTC)

<p>Hi community,<br>
now i want to generate landmarks uniformly from a grid plane to my volume mesh as the diagram shown below (since i want to generate a mean model of a series of data sets, i need to generate landmarks uniformly with a grid plane with fixed size points to do projection on volume mesh)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4ca57095409fc69c75703a7f95c58a75fb9f837.jpeg" data-download-href="/uploads/short-url/yVw0SCK5bTx9hRfAIU2Ww9O5RHx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4ca57095409fc69c75703a7f95c58a75fb9f837_2_612x500.jpeg" alt="image" data-base62-sha1="yVw0SCK5bTx9hRfAIU2Ww9O5RHx" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4ca57095409fc69c75703a7f95c58a75fb9f837_2_612x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4ca57095409fc69c75703a7f95c58a75fb9f837_2_918x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4ca57095409fc69c75703a7f95c58a75fb9f837.jpeg 2x" data-dominant-color="ADADBD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1100×898 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>is there any method or module that i can apply? thank you for your time!</p>

---

## Post #2 by @muratmaga (2022-09-02 05:48 UTC)

<p>Perhaps the <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup" rel="noopener nofollow ugc">surface markup extension</a> may give you what you want.</p>
<p>However, last I checked there was a bug in which it cropped the selected model when you enable the warp model option. You may want to check with <a class="mention" href="/u/cpinter">@cpinter</a>.</p>

---

## Post #3 by @cpinter (2022-09-02 09:48 UTC)

<p>I don’t believe the SurfaceMarkup extension would help much in your case, other than with initializing the grid to be projected. The projection will need to be done within your module.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="25048">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>However, last I checked there was a bug in which it cropped the selected model when you enable the warp model option</p>
</blockquote>
</aside>
<p>I don’t understand this. Do you have an issue in the surface markup with your use case?</p>

---

## Post #4 by @muratmaga (2022-09-02 19:12 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="25048">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I don’t understand this. Do you have an issue in the surface markup with your use case?</p>
</blockquote>
</aside>
<p>Perhaps it was a misunderstanding on my part of what surface node option does .  I thought if I choose a model, the Surface markups would be projected to the surface of the model following the topography of the surface. Instead currently it seems to be cropping the model (similar to the plane or curve functionality within Dynamic Modeler).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91cc370fed4f7cdf5cec77feaf24ecd7060816f1.jpeg" alt="image" data-base62-sha1="kNMLfcRsQcTVqd4HgRpqprl0PsJ" width="561" height="295"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9249c99a6e539dc75a7121173e2208bc858f5706.png" data-download-href="/uploads/short-url/kS7NA3t33KCq0x1dgykIfRjlGnA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9249c99a6e539dc75a7121173e2208bc858f5706_2_690x232.png" alt="image" data-base62-sha1="kS7NA3t33KCq0x1dgykIfRjlGnA" width="690" height="232" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9249c99a6e539dc75a7121173e2208bc858f5706_2_690x232.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9249c99a6e539dc75a7121173e2208bc858f5706_2_1035x348.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9249c99a6e539dc75a7121173e2208bc858f5706.png 2x" data-dominant-color="C7C7DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1120×378 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2022-09-03 01:44 UTC)

<p>I would recommend using readily available VTK filters for point sampling, such as <a href="https://vtk.org/doc/nightly/html/classvtkPoissonDiskSampler.html">vtkPoissonDiskSampler</a> and <a href="https://vtk.org/doc/nightly/html/classvtkPolyDataPointSampler.html">vtkPolyDataPointSampler</a>. They produce approximately uniform grid even if the surface is uneven.</p>
<p>Full example:</p>
<pre><code class="lang-python">modelNode = getNode('model')

# Sample points on the surface
sampler = vtk.vtkPoissonDiskSampler()
sampler.SetInputConnection(modelNode.GetPolyDataConnection())
sampler.SetRadius(10.0)
sampler.Update()
sampler.GetOutput().GetNumberOfPoints()

# Get point coordinates as numpy array
import vtk.util.numpy_support
pointData = sampler.GetOutput().GetPoints().GetData()
coordsArray = vtk.util.numpy_support.vtk_to_numpy(pointData)

# Create a markup point list
markupPointList = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode')
markupPointList.CreateDefaultDisplayNodes()
displayNode = markupPointList.GetDisplayNode()
displayNode.SetPointLabelsVisibility(False)
markupPointList.SetLocked(True)

# Set sampled point coordinates into the markup point list
updateMarkupsControlPointsFromArray(markupPointList, coordsArray)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b15ccecf0b46eb5acf42a8fa4ca154d18381886d.jpeg" data-download-href="/uploads/short-url/pj1lPIyRG7OZvcCS0VtS5ni0neJ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b15ccecf0b46eb5acf42a8fa4ca154d18381886d_2_644x500.jpeg" alt="image" data-base62-sha1="pj1lPIyRG7OZvcCS0VtS5ni0neJ" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b15ccecf0b46eb5acf42a8fa4ca154d18381886d_2_644x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b15ccecf0b46eb5acf42a8fa4ca154d18381886d_2_966x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b15ccecf0b46eb5acf42a8fa4ca154d18381886d_2_1288x1000.jpeg 2x" data-dominant-color="8C94AF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1436×1114 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Note that in the very latest Slicer Preview Release (that you download on 2022-09-03 or later) I’ve made some performance improvements in <code>updateMarkupsControlPointsFromArray</code> completes immediately instead in tens of seconds (if you have many points).</p>
<p>If you want to place points only in a specific part of the surface then you can clip the model using Dynamic Modeler module (<code>Curve cut</code>, <code>Boundary cut</code>, or <code>Select by points</code> tool) before you project.</p>
<p>You may also find this discussion useful: <a href="https://discourse.vtk.org/t/how-to-project-points-to-polydata/5694/6" class="inline-onebox">How to project points to Polydata? - #6 by will.schroeder - Support - VTK</a></p>

---

## Post #6 by @joanne40226 (2022-09-04 14:40 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you so much for the useful information!</p>

---

## Post #7 by @joanne40226 (2022-09-05 06:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Sorry to interrupt, I also want to know if I can set the exact amount of point size? So that every model can generate same amount of uniform points.<br>
Thank you for your time!</p>

---

## Post #8 by @lassoan (2022-09-05 13:25 UTC)

<p>If you want to have exact same number of points then I would do that by registering the model where you placed the points to the other models. If you have the transformation then you can use that to transfer the landmark points.</p>
<p>There are lots of tools for these kinds of things in Slicer. If you describe your overall goal then we can give better advice.</p>

---

## Post #9 by @joanne40226 (2022-09-05 16:41 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Okay, so for example i have three data sets which are three models of different patients. And i want to place a fixed size of landmarks on them(for example 1000 points) so that i can calculate the mean model of the 3 models.<br>
Model 1: X1,1/X1,2/X1,3/…X1,1000<br>
Model 2: X2,1/X2,2/X2,3/…X2,1000<br>
Model 3: X3,1/X3,2/X3,3/…X3,1000<br>
Mean model:( (X1,1+X2,1+X3,1)/3  /   (X1,2+X2,2+X3,2)/3  /…/ (X1,1000+X2,1000+X3,1000)/3<br>
So now i want to generate points on each model. Which the points size must be fixed(for example 1000 points) and each point should be generated at a similar location.(X1,1 and X2,1 should be place at similar anatomy location)</p>
<p>Therefore for my previous problem i hope to solve it by projecting a set points of a grid plane so that i can achieve my goal.<br>
However, do you have further advices? Thank you so much for your time.</p>

---

## Post #10 by @lassoan (2022-09-06 00:46 UTC)

<p>Thanks, this is very useful information. This is a quite common shape analysis task and SlicerMorph and SlicerSalt extensions have very sophisticated tools for it. I would recommend to follow the tutorial created for these extensions.</p>

---

## Post #11 by @joanne40226 (2022-09-06 00:54 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you so much!<br>
However I’ve tried it but for the point generation part I could not set a fixed size of points.<br>
Do you have any advice about it?<br>
Thank you for your time.</p>

---

## Post #12 by @muratmaga (2022-09-06 04:44 UTC)

<p><a class="mention" href="/u/joanne40226">@joanne40226</a> you are trying to achieve something that as far as I know nobody has achieved to do successfully (and in a repeatable way). Even if you can create identical number of points on them, there is no guarantee that these points will correspond correctly (anatomically speaking) and averaging them may not give an accurate representation.</p>
<p>Typically one uses deformable registration to project all these shapes into a common coordinate system, do the averaging there and then sample the grid on the average model and inverse the deformation to map the grid points created on the average model to the subjects.</p>
<p>You can sort of replicate this pipeline in ALPACA (SLicerMorph extension). You will start with one sample (as opposed to the mean), create your grid points. Then use ALPACA to transfer those points to the remaining samples. To create the mean model, you can take this set of points (that now exists for all your samples), feed them into the GPA and estimate a mean shape. You can then assign one of your samples as a reference sample and deform it to this mean shape, and export it as a model.</p>
<p>You can find our tutorials at <a href="https://github.com/SlicerMorph/Tutorials" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a>. The relevant modules to look at are ALPACA and GPA. <a href="https://github.com/SlicerMorph/SlicerMorph#how-to-cite" rel="noopener nofollow ugc">How to cite section of main repo</a> shows the papers published on these models, they may come in handy to understand.</p>
<p>ANother alternative is a different <a href="https://github.com/ToothAndClaw/SlicerAuto3dgm" rel="noopener nofollow ugc">extension called Auto3DGM</a> that tries to create points and correspondence at the same time. It is typically used for evolutionary studies, where correspondences are hard to pin down. I think their repository also lists some papers that explain the method along with what groups that it has been applied to. After the AUto3DGM creates these points, you can repeat the GPA step I described above to create your mean model.</p>
<p>When you are working with GPA make sure to check “Skip Scaling” during GPA alignment, so that the final mean shape is in physical coordinates (as opposed to being in procrustes coordinates).</p>

---

## Post #13 by @joanne40226 (2022-09-07 05:44 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> i see, thank you so much for the information!</p>

---
