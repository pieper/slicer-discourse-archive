---
topic_id: 9554
title: "Fiducial To Model Surface Distance"
date: 2019-12-18
url: https://discourse.slicer.org/t/9554
---

# Fiducial to Model Surface Distance

**Topic ID**: 9554
**Date**: 2019-12-18
**URL**: https://discourse.slicer.org/t/fiducial-to-model-surface-distance/9554

---

## Post #1 by @Juicy (2019-12-18 22:24 UTC)

<p>Hi Everyone</p>
<p>I am working on a project to quantify how closely a surface model generated from a CT scan matches the true bone geometry. This has been done quite extensively in literature but we have a need to quantify accuracy specifically with our tools and scan protocols etc.</p>
<p>The plan at the moment is to get a piece of animal bone and mount it on a small stand. We will then put the bone in a coordinate measuring machine and touch some points on the bone to get a low density point cloud of XYZ points which are exactly on the edge of the bone surface.</p>
<p>We will then put the bone in a container and fill it with gelatin to simulate soft tissue and put the container through the CT scanner to get an image set. This image set will then be used to generate an surface model of the bone with commercial segmentation software.</p>
<p>The next question is how to assess the accuracy of the surface model to the true surface of the bone. Thus far my thinking is to put all the XYZ points into the computer as fiducials, then load the STL model in as well like so. (pictures are just a practice example)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a21aa30f5af8cefd6c4a39ae599cd0d9cb7fefd.jpeg" data-download-href="/uploads/short-url/3JaxwEHNuPVcB1On62dul57YdYh.jpeg?dl=1" title="Un Registered" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a21aa30f5af8cefd6c4a39ae599cd0d9cb7fefd_2_690x471.jpeg" alt="Un Registered" data-base62-sha1="3JaxwEHNuPVcB1On62dul57YdYh" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a21aa30f5af8cefd6c4a39ae599cd0d9cb7fefd_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1a21aa30f5af8cefd6c4a39ae599cd0d9cb7fefd_2_1035x706.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a21aa30f5af8cefd6c4a39ae599cd0d9cb7fefd.jpeg 2x" data-dominant-color="BFC0DA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Un Registered</span><span class="informations">1251×855 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then I use fiducial registration and fiducial to model registration in SlicerIGT to get the model very close to the fiducials.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/956aa13f92bd8869f6f3a247195f93ff3d0a908b.jpeg" data-download-href="/uploads/short-url/ljNAZ9luSrjFgovLomaQFtxy8bx.jpeg?dl=1" title="Registered" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/956aa13f92bd8869f6f3a247195f93ff3d0a908b_2_690x471.jpeg" alt="Registered" data-base62-sha1="ljNAZ9luSrjFgovLomaQFtxy8bx" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/956aa13f92bd8869f6f3a247195f93ff3d0a908b_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/956aa13f92bd8869f6f3a247195f93ff3d0a908b_2_1035x706.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/956aa13f92bd8869f6f3a247195f93ff3d0a908b.jpeg 2x" data-dominant-color="B9BAD1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Registered</span><span class="informations">1251×855 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The fiducial to model registration module gives a readout of the average distance which is great but it would also be very handy to know the distance between each fiducial point and the closest point on the model surface say in a table or something.</p>
<p>Is there an easy way to do this or does it involve writing python scripts? I have found some scripts which look like they do similar things but not quite the same in the script repository.</p>
<p>I have seen this post which seemed kind of similar: <a href="https://discourse.slicer.org/t/model-to-model-distance/5551">https://discourse.slicer.org/t/model-to-model-distance/5551</a></p>

---

## Post #2 by @manjula (2019-12-18 22:32 UTC)

<p>If i understand correctly,</p>
<p>you should first register the models. You have number of tools in 3D slicer,</p>
<ol>
<li>IGT Fiducial registration wizard</li>
<li>CMFRegistration - Surface registration, ROI registration and Landmark registration.</li>
</ol>
<p>For me the best results i have obtained was with CMFReg- ROI registration.  But first try surface registration with Max iterations and max landmarks as it is the easiest method.</p>
<p>Next you need to apply the transformation to the moving model and then use Model to model distance module to calculate the distance.  and you can export the values as a file too if you want to.</p>
<ol start="3">
<li>or you can use ShapePopulation viewer to look at the areas of difference the aid of a color map which would be best in this i case for visualization purposes.</li>
</ol>

---

## Post #3 by @muratmaga (2019-12-19 05:07 UTC)

<p>The question is how do you know the closest point registration found on the model derived from CT is indeed the point you recorded with your coordinate reading machine.</p>
<p>If you go with sparse manual sampling, perhaps stick garnet sands (you can find them about 50-100 micron diameter), then record their coordinates with your digitizer, and then scan them. They will show up like bright spots in the CT scan.</p>
<p>Or you can use a well-calibrated microCT to obtain a dense mesh and use that as your reference and use model-to-model distance module.</p>

---

## Post #4 by @Juicy (2019-12-19 06:33 UTC)

<p>Manjula - thanks for the suggestions, Unfortunatly model-model distance is not useful in this case. I would need a fiducial to model distance module but I havent seen that one exists.</p>
<p>Muratmaga - Yes good suggestion about the markers. I suppose I could put another set of fiducials on the markers as seen on the scan and register the two sets of fiducials. It is also simpler for me to measure the distance between two fiducials than between fiducials and a surface. Other studies use surface scans of the bone as the gold standard to compare the CT to which would also be easier to analyse using model-model distance, however the others I am working with are keen to use the method described above.</p>

---

## Post #5 by @manjula (2019-12-19 07:49 UTC)

<p>Isn’t it what SPHARM-PDM module do?</p>

---

## Post #6 by @lassoan (2019-12-19 14:09 UTC)

<p>I’ve added a simple script to the script repository to measure closest point on a surface and write results into a table: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_distance_of_points_from_surface">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_distance_of_points_from_surface</a></p>
<p>It would be nice if somebody could put it in a simple scripted module as described in this <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true">tutorial</a>.</p>

---

## Post #7 by @Juicy (2019-12-19 18:18 UTC)

<p>Wow thanks Andras, that is really useful. I was trying to figure it out on python last night but I am more or less a complete noob at programming. I am trying to learn though as more and more I am realising how useful python is in slicer. I can try and make a module it just might take me a while…</p>
<p>Thanks again. Do you have any pointers on where a complete novice could learn to write a script like the one you just made?</p>

---

## Post #8 by @lassoan (2019-12-19 18:36 UTC)

<p>You need to be comfortable with Python language, which you can learn in a few days from tutorials on the web. Then the rest is about getting to know libraries. Slicer mainly relies on VTK (that you can learn from VTK <a href="https://vtk.org/documentation/">textbook</a> and <a href="https://lorensen.github.io/VTKExamples/site/">examples</a>), ITK (for image processing, that you can learn from the <a href="https://itk.org/ITKSoftwareGuide/html/">ITK software guide</a>), and Qt (for GUI; which you can learn from Qt documentation and examples). Slicer adds a little extra layer and logic, which you can learn from studying Slicer programming tutorials, script repository, and source code of Slicer core and extensions.</p>
<p>The tutorial that I linked above is a good starting point and you can always ask questions here. You can also come to one of the <a href="https://projectweek.na-mic.org/">Slicer project weeks</a> where you bring your own problem that you work on with help from Slicer experts.</p>

---

## Post #9 by @Juicy (2019-12-21 07:05 UTC)

<p>Quick question, I am doing some python courses to try and get up to speed. Is python 2 or python 3 more relevant to slicer?</p>

---

## Post #10 by @lassoan (2019-12-21 14:08 UTC)

<p>Only Python3 is relevant now. Recent Slicer versions use Python3 (stable version still uses Python2, but it will be phased out soon).</p>

---

## Post #11 by @Juicy (2020-01-08 01:45 UTC)

<p>Hi Andras,</p>
<p>I have been trying to learn some python 3 using <a href="http://codeacademy.com" rel="noopener nofollow ugc">codeacademy.com</a> which seems good.</p>
<p>I added some extra lines to your code to print out the min, max, mean and RMS values from the distances in the table.</p>
<p>I am not sure about the RMS calculation. I was looking at the code for the fiducial to model registration module in Slicer IGT <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialsToModelRegistration/FiducialsToModelRegistration.py" rel="noopener nofollow ugc">here</a> and trying to copy what the ComputeMeanDistance function does. However their closest point function must work differently to your one as your code seems to give a negative distance when the fiducial is inside the surface of the model (which is good), however it is not possible to take the square root of a negative number.</p>
<p>To get around this I have taken the absolute value of the numbers in the table but I cannot get the same result as is printed in the fiducial to model registration. I have tried applying the transfrom to the model, I have tried inverting the transform and applying it to the model and I have tried with no transform applied. I cannot get my RMS printout to match the value in the fiducials-model registration output box.</p>
<p>Do you know what I might be doing wrong? Here is my code. I don’t understand how to use the vtk arrays so I have made a parallel list to do operations on.</p>
<pre><code>import statistics
import math
markupsNode = getNode('F')
modelNode = getNode('mymodel')

# Transform model polydata to world coordinate system
if modelNode.GetParentTransformNode():
    transformModelToWorld = vtk.vtkGeneralTransform()
    slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(modelNode.GetParentTransformNode(), None, transformModelToWorld)
    polyTransformToWorld = vtk.vtkTransformPolyDataFilter()
    polyTransformToWorld.SetTransform(transformModelToWorld)
    polyTransformToWorld.SetInputData(modelNode.GetPolyData())
    polyTransformToWorld.Update()
    surface_World = polyTransformToWorld.GetOutput()
else:
    surface_World = modelNode.GetPolyData()

# Create arrays to store results
indexCol = vtk.vtkIntArray()
indexCol.SetName("Index")
labelCol = vtk.vtkStringArray()
labelCol.SetName("Name")
distanceCol = vtk.vtkDoubleArray()
distanceCol.SetName("Distance")
# Create blank list becuase I dont know how to use vtk arrays yet
dist_list = []

distanceFilter = vtk.vtkImplicitPolyDataDistance()
distanceFilter.SetInput(surface_World);
nOfFiduciallPoints = markupsNode.GetNumberOfFiducials()
for i in range(0, nOfFiduciallPoints):
    point_World = [0,0,0]
    markupsNode.GetNthControlPointPositionWorld(i, point_World)
    closestPointOnSurface_World = [0,0,0]
    closestPointDistance = distanceFilter.EvaluateFunctionAndGetClosestPoint(point_World, closestPointOnSurface_World)
    indexCol.InsertNextValue(i)
    labelCol.InsertNextValue(markupsNode.GetNthControlPointLabel(i))
    distanceCol.InsertNextValue(closestPointDistance)
    #fill the list with closest point distances
    dist_list.append(closestPointDistance)

# Create a table from result arrays
resultTableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", "Points from surface distance")
resultTableNode.AddColumn(indexCol)
resultTableNode.AddColumn(labelCol)
resultTableNode.AddColumn(distanceCol)

# Show table in view layout
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpTableView)
slicer.app.applicationLogic().GetSelectionNode().SetReferenceActiveTableID(resultTableNode.GetID())
slicer.app.applicationLogic().PropagateTableSelection()

# math for min, max, mean and RMS values
max_value = max(dist_list)
min_value = min(dist_list)
mean_value = statistics.mean(dist_list)
sqrt_list = [math.sqrt(abs(i)) for i in dist_list]
rms_value = statistics.mean(sqrt_list)

# print min, max, mean and RMS values
print("The min value is " + "%.3f" % min_value + ".")
print("The max value is " + "%.3f" % max_value + ".")
print("The mean value is " + "%.3f" % mean_value + ".")
print("The Root Mean Square Value is " + "%.3f" % rms_value + ".")
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4512abe2d78b2fdfcb224743f3d1e4a2556e1328.jpeg" data-download-href="/uploads/short-url/9R2WPfhPbk2kkmypuQPv5e8f4ta.jpeg?dl=1" title="Slicer code" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4512abe2d78b2fdfcb224743f3d1e4a2556e1328_2_690x471.jpeg" alt="Slicer code" data-base62-sha1="9R2WPfhPbk2kkmypuQPv5e8f4ta" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4512abe2d78b2fdfcb224743f3d1e4a2556e1328_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4512abe2d78b2fdfcb224743f3d1e4a2556e1328_2_1035x706.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4512abe2d78b2fdfcb224743f3d1e4a2556e1328.jpeg 2x" data-dominant-color="D7D7D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer code</span><span class="informations">1251×855 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @Juicy (2020-01-08 02:17 UTC)

<p>Wait, before you spend any time looking at this, I might have figured out what I did. I will report back</p>

---

## Post #13 by @Juicy (2020-01-08 03:24 UTC)

<p>Ok, this new code seems to work and get the same value. I had to take the absolute value of all the entries on the table and take the average of them.</p>
<p>I got confused by the sqrt in the fiducials-model code and thought I had to take the sqrt of all the values in the list but apparently not.</p>
<pre><code>import statistics
import math
markupsNode = getNode('F')
modelNode = getNode('mymodel')

# Transform model polydata to world coordinate system
if modelNode.GetParentTransformNode():
transformModelToWorld = vtk.vtkGeneralTransform()
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(modelNode.GetParentTransformNode(), None, transformModelToWorld)
polyTransformToWorld = vtk.vtkTransformPolyDataFilter()
polyTransformToWorld.SetTransform(transformModelToWorld)
polyTransformToWorld.SetInputData(modelNode.GetPolyData())
polyTransformToWorld.Update()
surface_World = polyTransformToWorld.GetOutput()
else:
surface_World = modelNode.GetPolyData()

# Create arrays to store results
indexCol = vtk.vtkIntArray()
indexCol.SetName("Index")
labelCol = vtk.vtkStringArray()
labelCol.SetName("Name")
distanceCol = vtk.vtkDoubleArray()
distanceCol.SetName("Distance")
# Create blank list becuase I dont know how to use vtk arrays yet
dist_list = []

distanceFilter = vtk.vtkImplicitPolyDataDistance()
distanceFilter.SetInput(surface_World);
nOfFiduciallPoints = markupsNode.GetNumberOfFiducials()
for i in range(0, nOfFiduciallPoints):
point_World = [0,0,0]
markupsNode.GetNthControlPointPositionWorld(i, point_World)
closestPointOnSurface_World = [0,0,0]
closestPointDistance = distanceFilter.EvaluateFunctionAndGetClosestPoint(point_World, closestPointOnSurface_World)
indexCol.InsertNextValue(i)
labelCol.InsertNextValue(markupsNode.GetNthControlPointLabel(i))
distanceCol.InsertNextValue(closestPointDistance)
#fill the list with closest point distances
dist_list.append(closestPointDistance)

# Create a table from result arrays
resultTableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", "Points from surface distance")
resultTableNode.AddColumn(indexCol)
resultTableNode.AddColumn(labelCol)
resultTableNode.AddColumn(distanceCol)

# Show table in view layout
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpTableView)
slicer.app.applicationLogic().GetSelectionNode().SetReferenceActiveTableID(resultTableNode.GetID())
slicer.app.applicationLogic().PropagateTableSelection()

# math for min, max, mean
abs_list = [abs(i) for i in dist_list]
absolute_max_value = max(abs_list)
absolute_min_value = min(abs_list)
absolute_mean_value = statistics.mean(abs_list)

# print min, max, mean
print("The absolute min value is " + "%.3f" % absolute_min_value + ".")
print("The absolute max value is " + "%.3f" % absolute_max_value + ".")
print("The absolute mean value is " + "%.3f" % absolute_mean_value + ".")
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5669a7713cddae92bc92c19ab41abcb08e49fe31.jpeg" data-download-href="/uploads/short-url/ckrqmI6lnrrHS3dGppvwcUpbH5n.jpeg?dl=1" title="Slicer code" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5669a7713cddae92bc92c19ab41abcb08e49fe31_2_690x471.jpeg" alt="Slicer code" data-base62-sha1="ckrqmI6lnrrHS3dGppvwcUpbH5n" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5669a7713cddae92bc92c19ab41abcb08e49fe31_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5669a7713cddae92bc92c19ab41abcb08e49fe31_2_1035x706.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5669a7713cddae92bc92c19ab41abcb08e49fe31.jpeg 2x" data-dominant-color="D7D7D7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer code</span><span class="informations">1251×855 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @Juicy (2020-01-08 04:17 UTC)

<p>Ok, sorry about this. Maybe I need to wait longer before posting. I have some more confusion now.</p>
<p>The definition of the Root mean square value of a set of numbers is shown below (from <a href="https://en.wikipedia.org/wiki/Root_mean_square" rel="noopener nofollow ugc">wikipedia</a>):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5ce18f754f3d656e8d9e2257cf6d84e26675169c.jpeg" data-download-href="/uploads/short-url/dfFbFliXC0zrKmIQN0m4UtHJ8wk.jpeg?dl=1" title="RMS definition" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ce18f754f3d656e8d9e2257cf6d84e26675169c_2_345x66.jpeg" alt="RMS definition" data-base62-sha1="dfFbFliXC0zrKmIQN0m4UtHJ8wk" width="345" height="66" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ce18f754f3d656e8d9e2257cf6d84e26675169c_2_345x66.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ce18f754f3d656e8d9e2257cf6d84e26675169c_2_517x99.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ce18f754f3d656e8d9e2257cf6d84e26675169c_2_690x132.jpeg 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">RMS definition</span><span class="informations">810×157 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I made this code to compute the RMS how it is defined in wikipedia vs how it is computed in the fiducial-model distance code. As you can see there is a difference.</p>
<p>import math</p>
<pre><code>dist_list = [-0.0778, 0.0521, -0.0069, -0.0620, 0.0526, 0.0078]

# How it is defined in wikipedia
squared_list = [i ** 2 for i in dist_list]
sum_of_squared_list = sum(squared_list)
squared_mean = sum_of_squared_list / len(squared_list)
rms_wiki = math.sqrt(squared_mean)

# How it is computed in fiducial-model module
squared_list2 = [i ** 2 for i in dist_list]
root_list = [math.sqrt(j) for j in squared_list2]
rms_fid_mod = sum(root_list) /  len(root_list)

print (rms_wiki)
print (rms_fid_mod)
</code></pre>
<p>and here are the results:</p>
<blockquote>
<blockquote>
<blockquote>
<p>print (rms_wiki)<br>
0.050804297718467346<br>
print (rms_fid_mod)<br>
0.04319999999999999</p>
</blockquote>
</blockquote>
</blockquote>
<p>obviously there is a difference here. Which way is the correct way of computing the RMS?</p>

---

## Post #15 by @lassoan (2020-01-08 14:20 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="14" data-topic="9554">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>Which way is the correct way of computing the RMS</p>
</blockquote>
</aside>
<p>Definition of RMSE above is correct (root of the mean of squared differences). It is up to you if you use RMS or MAD (mean of absolute differences) as error metric. RMSE is more sensitive to outliers.</p>

---

## Post #16 by @Juicy (2020-01-23 07:56 UTC)

<p>Hi Andras</p>
<p>I have made your code above into a scripted module. I have also added some output boxes in the UI to show some other data such as mean of absolute differences, root mean square, min, max etc.</p>
<p>I have got it working but some of my code feels a bit dubious. I am still very newb at programming. I am also not really sure what to put in the test area.</p>
<p>I have made an icon graphic and put it in the the icon folder but I am not sure where to put it for displaying in the extension store/manager thing.</p>
<p>do you mind taking a look at the files in github <a href="https://github.com/ReynoldsJ20/Fiducials-to-Model-Distance" rel="nofollow noopener">here</a>?</p>
<p>Thank you</p>

---

## Post #17 by @Frederic (2020-01-23 08:28 UTC)

<p>Hi Juicy,<br>
Andras already reply a efficient answer to you, and I almost miss the boat, but it was also possible for you to use this <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/GeodesicSlicer#Parameters_to_find_the_shortest_path" rel="nofollow noopener">function</a> of GeodesicSlicer to have the measurement of your fiducial points by geodesic distance.<br>
Best,<br>
Frederic</p>

---

## Post #18 by @lassoan (2020-01-23 11:23 UTC)

<p>For me, it seems that <a class="mention" href="/u/juicy">@Juicy</a> is interested in length of the straight line connecting a point and the closest surface point, while GeodesicSlicer computes length of the curve that connects two points on the surface. Both of them are important and interesting metrics, but they are different.</p>
<p><a class="mention" href="/u/juicy">@Juicy</a> it is very useful to have this module that computes point-to-surface error metrics. As a test, you can create a small test function that creates a model node (e.g., using vtkCylinderSource), adds a few points (just hardcode their positions), run the logic, and check if the computed values match what you expect (values that you computed and verified before).</p>
<p>It would be nice to extend it to be able to compute point-to-point error metrics, too (for people who use landmark point based registration).</p>
<p>You can submit this module as a separate extension, but it would be probably simpler to just add it to SlicerIGT extension.</p>

---

## Post #19 by @Juicy (2020-02-02 01:01 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I have done some more work on the Fiducial to Model Distance scripted module.</p>
<ol>
<li>I have added the ability to compute the same set of error metrics between two point clouds made of fiducials.</li>
<li>I have added a simple test which adds a 100 x 100 x 100mm vtk cube and then adds a set of six “fixed” reference fiducial points on the surface of the cube. Then another set of 6 “moving” fiducials are added around the cube before running both the Fiducial to Model and then Fiducial to Fiducial algorithms.  3 of the “moving” fiducial points are 1mm from the cube surface and 3 more are 2mm from the cube surface so the average distance will be 1.5mm.</li>
</ol>
<p>I was reading through your powerpoint and one thing I don’t really understand is how to make a parameter node to save the settings in the GUI?</p>
<p>Do you mind having a quick look over the code <a href="https://github.com/ReynoldsJ20/Fiducials-to-Model-Distance" rel="nofollow noopener">here</a>? Let me know if you have any suggestions. Again, sorry about any dubious coding.</p>
<p>Thanks,</p>

---

## Post #20 by @lassoan (2020-02-02 01:12 UTC)

<p>I’ve added answer and a number of other code review comments here: <a href="https://github.com/ReynoldsJ20/Fiducials-to-Model-Distance/issues/3">https://github.com/ReynoldsJ20/Fiducials-to-Model-Distance/issues/3</a></p>

---

## Post #21 by @Juicy (2020-02-11 22:25 UTC)

<p>Update: The Fiducials to Model Distance module is now available in the extension manager in the ‘Quantification’ area.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01f8c3accce820b18e351bd6f4440867c65178df.jpeg" alt="Fiducial To Model Distance" data-base62-sha1="hrs3XJP1nfXiqhQeLvww5aii0D" width="174" height="256"></p>

---

## Post #22 by @sfglio (2020-02-22 21:49 UTC)

<p>Is this module already available because right now I cannot find it in the extension manager:(</p>

---

## Post #23 by @Juicy (2020-02-22 22:07 UTC)

<p>It should appear in the extension manager in the latest preview release of slicer. It may not appear if you are using slicer 4.10.2 or older versions of 4.11.0. It is under the ‘Quantification’ section</p>

---

## Post #24 by @Juicy (2020-02-22 22:40 UTC)

<p>The module was written for 4.11.0 but it may work on earlier versions although I can’t guarantee it.</p>
<p>If you do need to get it on an older version then you should be able to just download the files from the github site <a href="https://github.com/ReynoldsJ20/SlicerFiducialsToModelDistance" rel="nofollow noopener">here.</a>  Click the green button in the top right corner of the webpage called “Clone or Download” download the files as a zip. Then unzip the files and move them to a folder of your choice. The standard file path for modules on slicer (in windows) seems to be C:/Users/“your user name here”/AppData/Roaming/NA-MIC/“Extensions of your version of slicer here”. So to be tidy you could put it in here with the rest of your extensions, but anywhere will work.</p>
<p>Then in slicer go to Edit &gt; Application Settings &gt; Modules, in the Additional Module paths area click “Add”. Then browse to the folder where you put the files which you downloaded from github. You will need to browse to the “FiducialsToModelDistance” folder for it to work. Then you will need to restart slicer and it should now appear in the module area under “Quantification”.</p>

---

## Post #25 by @sfglio (2020-02-23 16:29 UTC)

<p>I have used a nighty version of 4.11.0 from january, but after updating, the module can be found in extension manager. Thank you for your helpful reply!</p>

---

## Post #26 by @Saima (2021-09-14 01:30 UTC)

<p>Hi Andras,<br>
I can do this one and put it on github.</p>
<p>I am also using the code a little bit differently for some other modules in our project.</p>
<p>Thanks alot. Its very useful</p>
<p>Regards,<br>
Saima Safdar</p>

---
