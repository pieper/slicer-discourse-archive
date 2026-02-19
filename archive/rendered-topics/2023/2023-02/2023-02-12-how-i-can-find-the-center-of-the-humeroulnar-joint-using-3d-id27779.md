---
topic_id: 27779
title: "How I Can Find The Center Of The Humeroulnar Joint Using 3D"
date: 2023-02-12
url: https://discourse.slicer.org/t/27779
---

# How I can find the center of the humeroulnar joint using 3d slicer ?

**Topic ID**: 27779
**Date**: 2023-02-12
**URL**: https://discourse.slicer.org/t/how-i-can-find-the-center-of-the-humeroulnar-joint-using-3d-slicer/27779

---

## Post #1 by @Julian_KC (2023-02-12 12:45 UTC)

<p>Hello everyone,<br>
I am currently working on the morphology of the ulna and I need to calculate the biomechanical length of some ulnas by placing a landmark at the center of the trochlear notch (the center of the joint). I thought I could do this by creating a sphere that passes through different landmarks at the center of the notch, I use this code :</p>
<pre><code class="lang-auto"># Get markup node from scene
markups = slicer.util.getNode("F")

from scipy.optimize import least_squares
import numpy

def fit_sphere_least_squares(x_values, y_values, z_values, initial_parameters, bounds=((-numpy.inf, -numpy.inf, -numpy.inf, -numpy.inf),(numpy.inf, numpy.inf, numpy.inf, numpy.inf))):
  """
  Source: https://github.com/thompson318/scikit-surgery-sphere-fitting/blob/master/sksurgeryspherefitting/algorithms/sphere_fitting.py
  Uses scipy's least squares optimisor to fit a sphere to a set
  of 3D Points
  :return: x: an array containing the four fitted parameters
  :return: ier: int An integer flag. If it is equal to 1, 2, 3 or 4, the
          solution was found.
  :param: (x,y,z) three arrays of equal length containing the x, y, and z
          coordinates.
  :param: an array containing four initial values (centre, and radius)
  """
  return least_squares(_calculate_residual_sphere, initial_parameters, bounds=bounds, method="trf", jac="3-point", args=(x_values, y_values, z_values))

def _calculate_residual_sphere(parameters, x_values, y_values, z_values):
  """
  Source: https://github.com/thompson318/scikit-surgery-sphere-fitting/blob/master/sksurgeryspherefitting/algorithms/sphere_fitting.py
  Calculates the residual error for an x,y,z coordinates, fitted
  to a sphere with centre and radius defined by the parameters tuple
  :return: The residual error
  :param: A tuple of the parameters to be optimised, should contain [x_centre, y_centre, z_centre, radius]
  :param: arrays containing the x,y, and z coordinates.
  """
  #extract the parameters
  x_centre, y_centre, z_centre, radius = parameters
  #use numpy's sqrt function here, which works by element on arrays
  distance_from_centre = numpy.sqrt((x_values - x_centre)**2 + (y_values - y_centre)**2 + (z_values - z_centre)**2)
  return distance_from_centre - radius

# Fit a sphere to the markups fidicual points
markupsPositions = slicer.util.arrayFromMarkupsControlPoints(markups)
import numpy as np
# initial guess
center0 = np.mean(markupsPositions, 0)
radius0 = np.linalg.norm(np.amin(markupsPositions,0)-np.amax(markupsPositions,0))/2.0
fittingResult = fit_sphere_least_squares(markupsPositions[:,0], markupsPositions[:,1], markupsPositions[:,2], [center0[0], center0[1], center0[2], radius0])
[centerX, centerY, centerZ, radius] = fittingResult["x"]

# Create a sphere using the fitted parameters
sphere = vtk.vtkSphereSource()
sphere.SetPhiResolution(30)
sphere.SetThetaResolution(30)
sphere.SetCenter(centerX, centerY, centerZ)
sphere.SetRadius(radius)
sphere.Update()

# Add the sphere to the scene
modelsLogic = slicer.modules.models.logic()
model = modelsLogic.AddModel(sphere.GetOutput())
model.GetDisplayNode().SetSliceIntersectionVisibility(True)
model.GetDisplayNode().SetSliceIntersectionThickness(3)
model.GetDisplayNode().SetColor(1,1,0)
</code></pre>
<p>and when I tried I got this :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db6f3498c5132b1f317cc175326f7ba9b8a1047.jpeg" data-download-href="/uploads/short-url/b5uJxvgkWrv9sZCkkJBnZV9Ml9l.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4db6f3498c5132b1f317cc175326f7ba9b8a1047_2_567x500.jpeg" alt="image" data-base62-sha1="b5uJxvgkWrv9sZCkkJBnZV9Ml9l" width="567" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4db6f3498c5132b1f317cc175326f7ba9b8a1047_2_567x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db6f3498c5132b1f317cc175326f7ba9b8a1047.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db6f3498c5132b1f317cc175326f7ba9b8a1047.jpeg 2x" data-dominant-color="96958E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">699×616 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My ultimate goal is to calculate the length from the center of the joint to the end of the ulnar head. Could you please help me achieve this ?<br>
Thank you for your answers !</p>

---

## Post #2 by @chir.set (2023-02-12 13:29 UTC)

<p>Would this fit your requirements ? You can draw an arbitrary sphere if you install ExtraMarkups with the Extensions manager. Please note that you can also transform an arbitrary sphere using IGT extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ed5803ed1ae741a0efa3e8023e365f6171da35b.jpeg" data-download-href="/uploads/short-url/knzdUY7laZWXSVaGEbnEQcmm1BN.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ed5803ed1ae741a0efa3e8023e365f6171da35b_2_679x500.jpeg" alt="Screenshot" data-base62-sha1="knzdUY7laZWXSVaGEbnEQcmm1BN" width="679" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ed5803ed1ae741a0efa3e8023e365f6171da35b_2_679x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8ed5803ed1ae741a0efa3e8023e365f6171da35b_2_1018x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ed5803ed1ae741a0efa3e8023e365f6171da35b.jpeg 2x" data-dominant-color="4C4D47"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1215×894 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Julian_KC (2023-02-12 17:14 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="27779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>ExtraMarkups</p>
</blockquote>
</aside>
<p>Thanks a lot for your answer It can resolve my probleme but I have to try it first and I really can find it on the extensions manager, neither with the name ExtraMarkups or SlicerExtraMarkups, can you helps me ?<br>
And IGT I find it but don’t undertand how it can help me …</p>
<p>Thanks a lot for your answer !</p>

---

## Post #4 by @chir.set (2023-02-12 17:50 UTC)

<p>You’re probably using Slicer stable 5.2. ExtraMarkups is available in Slicer preview that you can download similarly.</p>
<p>As for IGT, you can use the “Create models” module in this extension. Then in “Data module”, you can create a transform on this object, show the transform in GUI and manipulate it.</p>
<p>Tinker with one at a time to be less confused.</p>

---

## Post #5 by @Julian_KC (2023-02-12 23:01 UTC)

<p>Thank you very much !</p>
<p>I try it :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bbff1b1ecc43d373a16b404b72aba45f8981599.png" data-download-href="/uploads/short-url/mdPfgMNTApuSG1fEUJfuZhQqCed.png?dl=1" title="Capture d’écran 2023-02-12 235651" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbff1b1ecc43d373a16b404b72aba45f8981599_2_136x500.png" alt="Capture d’écran 2023-02-12 235651" data-base62-sha1="mdPfgMNTApuSG1fEUJfuZhQqCed" width="136" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbff1b1ecc43d373a16b404b72aba45f8981599_2_136x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbff1b1ecc43d373a16b404b72aba45f8981599_2_204x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bbff1b1ecc43d373a16b404b72aba45f8981599.png 2x" data-dominant-color="9E9ABA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-02-12 235651</span><span class="informations">236×863 47.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70be3e4dbf6fa0172d2d19330346fbfe04d20424.png" data-download-href="/uploads/short-url/g5n4pQeqDCO4tZD2WzsVLmdUPjK.png?dl=1" title="Capture d’écran 2023-02-12 235748" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70be3e4dbf6fa0172d2d19330346fbfe04d20424_2_531x500.png" alt="Capture d’écran 2023-02-12 235748" data-base62-sha1="g5n4pQeqDCO4tZD2WzsVLmdUPjK" width="531" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70be3e4dbf6fa0172d2d19330346fbfe04d20424_2_531x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70be3e4dbf6fa0172d2d19330346fbfe04d20424.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70be3e4dbf6fa0172d2d19330346fbfe04d20424.png 2x" data-dominant-color="ADA165"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-02-12 235748</span><span class="informations">592×557 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
As you can see it work pretty well !<br>
But in fact I’m not sure it’s really the best fit sphere and if I’m really in the center joint but honestly I think it’s enough for my purpose.<br>
Is it possible to define de sphere with more than one point or no ?</p>

---

## Post #6 by @chir.set (2023-02-13 08:25 UTC)

<aside class="quote no-group" data-username="Julian_KC" data-post="5" data-topic="27779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julian_kc/48/18359_2.png" class="avatar"> Julian_KC:</div>
<blockquote>
<p>sphere with more than one point or no ?</p>
</blockquote>
</aside>
<p>Yes, but it implies complicating the code, meaning risks of errors and risks of crash, with little benefit. So no.</p>
<aside class="quote no-group" data-username="Julian_KC" data-post="5" data-topic="27779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julian_kc/48/18359_2.png" class="avatar"> Julian_KC:</div>
<blockquote>
<p>really in the center joint</p>
</blockquote>
</aside>
<p>If you have the source images, you may reslice on the humeral trochlea and get a reliable sphere.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f4b471725cefa271b58ab365adfd8d544b68e4.png" data-download-href="/uploads/short-url/hg1zBbz7QAcoYDXswsfTIdKJjGk.png?dl=1" title="TrochleaGuide" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78f4b471725cefa271b58ab365adfd8d544b68e4_2_331x500.png" alt="TrochleaGuide" data-base62-sha1="hg1zBbz7QAcoYDXswsfTIdKJjGk" width="331" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78f4b471725cefa271b58ab365adfd8d544b68e4_2_331x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f4b471725cefa271b58ab365adfd8d544b68e4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f4b471725cefa271b58ab365adfd8d544b68e4.png 2x" data-dominant-color="525250"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TrochleaGuide</span><span class="informations">429×647 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Julian_KC (2023-02-13 10:43 UTC)

<p>Thanks a lot for your answer.</p>
<aside class="quote no-group" data-username="chir.set" data-post="6" data-topic="27779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Yes, but it implies complicating the code, meaning risks of errors and risks of crash, with little benefit. So no.</p>
</blockquote>
</aside>
<p>Ok I understand</p>
<aside class="quote no-group" data-username="chir.set" data-post="6" data-topic="27779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>If you have the source images</p>
</blockquote>
</aside>
<p>I don’t have the source image, I just have the 3D surface model.</p>
<p>Well it works for now so thank you very much but if anyone else (or even you) have another idea to better fit my requirement, I’m open.</p>

---

## Post #8 by @lassoan (2023-02-16 00:24 UTC)

<p>You can get the optimal best fit sphere the way you tried it at the very beginning. The only mistake was that you only placed 8 points, mostly in a single plane. If you place dozens of points, well dispersed on the entire joint surface then the automatically fit sphere should provide the correct solution.</p>

---

## Post #9 by @Julian_KC (2023-02-16 08:12 UTC)

<p>Hi, thank you for your answer.</p>
<p>I tried again and you have right, it’s work, thank you very much so I have two methods  :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd085f3a3b103d1bc45ddc0265e7a0af8a1eeac0.png" alt="image" data-base62-sha1="tfNOJFheUDFJC6W9IrHJGvdEknK" width="543" height="466"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d86a884610d7774b3788dff551eece525d12fccf.png" alt="image" data-base62-sha1="uSvnrfORtEAlAWkIBG9GMbWcPSf" width="251" height="421"></p>
<p>And this one :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccf35d7579ee6415ac56604a14064477257aaf04.jpeg" data-download-href="/uploads/short-url/tf4OioC1CV7ZUX3Zos4DBSM83Os.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccf35d7579ee6415ac56604a14064477257aaf04_2_531x500.jpeg" alt="image" data-base62-sha1="tf4OioC1CV7ZUX3Zos4DBSM83Os" width="531" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccf35d7579ee6415ac56604a14064477257aaf04_2_531x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccf35d7579ee6415ac56604a14064477257aaf04.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccf35d7579ee6415ac56604a14064477257aaf04.jpeg 2x" data-dominant-color="ADA165"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">592×557 83.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I don’t know if it’s really a probleme that the sphere don’t fit only the keeled part of the joint. I will try to get the center of that sphere and compare both mesures</p>
<p>Thank you very much again, if anyone know how to create a landmarks at the center of that sphere i’m interested in !</p>
<p>PS: I already looked here : <a href="https://discourse.slicer.org/t/get-best-fit-sphere-of-humeral-head/22975/6" class="inline-onebox">Get best fit sphere of humeral head - #6 by lassoan</a>, But I don’t understand.</p>
<p>Thank you for your help !</p>

---

## Post #10 by @chir.set (2023-02-16 10:29 UTC)

<aside class="quote no-group" data-username="Julian_KC" data-post="9" data-topic="27779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julian_kc/48/18359_2.png" class="avatar"> Julian_KC:</div>
<blockquote>
<p>if anyone know how to create a landmarks at the center of that sphere i’m interested in</p>
</blockquote>
</aside>
<p>I suppose you are referring to the markups Shape node, in which case, you can use this function to get the center :</p>
<pre><code class="lang-auto">def getShapeCenter(markupsNode):
    center = None
    if markupsNode.GetClassName() != "vtkMRMLMarkupsShapeNode":
        return center
    if markupsNode.GetShapeName( ) != slicer.vtkMRMLMarkupsShapeNode.Sphere:
        return center
    p1 = [ 0.0 ] * 3
    p2 = [ 0.0 ] * 3
    markupsNode.GetNthControlPointPositionWorld(0, p1)
    markupsNode.GetNthControlPointPositionWorld(1, p2)
    if markupsNode.GetRadiusMode() == slicer.vtkMRMLMarkupsShapeNode.Centered:
        return p1
    else:
        center = [ 0.0 ] * 3
        for i in range(3):
            center[i] = (p1[i] + p2[i]) / 2.0
            
        return center
</code></pre>

---

## Post #11 by @lassoan (2023-02-16 12:09 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> it would be nice to add a “best fit” mode for the sphere markup that would compute least square fit sphere for all the control points. It could provide the center and radius as measurements.</p>

---

## Post #12 by @Julian_KC (2023-02-16 14:21 UTC)

<p>Yes it could be awsome to add this mode  !</p>

---

## Post #13 by @Julian_KC (2023-02-16 14:22 UTC)

<p>I try this code, but anything happen when I run it  :</p>
<aside class="quote no-group" data-username="chir.set" data-post="10" data-topic="27779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<pre><code class="lang-auto">def getShapeCenter(markupsNode):
    center = None
    if markupsNode.GetClassName() != "vtkMRMLMarkupsShapeNode":
        return center
    if markupsNode.GetShapeName( ) != slicer.vtkMRMLMarkupsShapeNode.Sphere:
        return center
    p1 = [ 0.0 ] * 3
    p2 = [ 0.0 ] * 3
    markupsNode.GetNthControlPointPositionWorld(0, p1)
    markupsNode.GetNthControlPointPositionWorld(1, p2)
    if markupsNode.GetRadiusMode() == slicer.vtkMRMLMarkupsShapeNode.Centered:
        return p1
    else:
        center = [ 0.0 ] * 3
        for i in range(3):
            center[i] = (p1[i] + p2[i]) / 2.0
            
        return center
</code></pre>
</blockquote>
</aside>
<p>What am I doing wrong ?</p>
<p>Thanks so much for your answers !</p>

---

## Post #14 by @chir.set (2023-02-16 19:07 UTC)

<p>I’ll get back for more info in a few days, not possible right now.</p>

---

## Post #15 by @chir.set (2023-02-18 16:03 UTC)

<aside class="quote no-group" data-username="Julian_KC" data-post="13" data-topic="27779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julian_kc/48/18359_2.png" class="avatar"> Julian_KC:</div>
<blockquote>
<p>I try this code, but anything happen when I run it :</p>
</blockquote>
</aside>
<p>It’s a function that you must call, passing it a Sphere markups object :</p>
<pre><code class="lang-auto"># After pasting the function in the Python console :
sh = slicer.util.getNode("SH")
center = getShapeCenter(sh)
print(center)
</code></pre>
<p>where ‘SH’ is the name of a markups Shape node of type Sphere.</p>

---

## Post #16 by @chir.set (2023-02-18 20:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="27779">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it would be nice to add a “best fit” mode for the sphere markup</p>
</blockquote>
</aside>
<p>This <a href="https://wuyang-li1990.medium.com/point-cloud-sphere-fitting-cc619c0f7ced" rel="noopener nofollow ugc">page</a> would be quite helpful for this. The solution is still in Python and  it should be implemented in C++ to fit in ExtraMarkups. I would need to call np.linalg.lstsq from C++. Is it doable and how ?</p>

---

## Post #17 by @lassoan (2023-02-18 22:25 UTC)

<p>You can call Python from C++ using the Python manager class. However, it would a bit nicer to use the optimization methods that are directly available in C++. ITK has several optimizer, both linear and non-linear. For example lbfgs-b is a good non-linear one. I’ve found a simple Powell optimizer example here: <a href="https://github.com/PlusToolkit/PlusLib/blob/master/src/PlusCalibration/vtkProbeCalibrationAlgo/vtkPlusProbeCalibrationOptimizerAlgo.cxx" class="inline-onebox">PlusLib/vtkPlusProbeCalibrationOptimizerAlgo.cxx at master · PlusToolkit/PlusLib · GitHub</a></p>

---

## Post #18 by @chir.set (2023-02-19 18:09 UTC)

<p>This task is out of reach to me.</p>
<p>I don’t see how to input point coordinates to the ITK optimizer, where it processes the input and where/how to get output, despite the example you provide. After many hours, I conclude it’s time to stop.</p>
<p>Python has a great advantage of higher level functions here. Perhaps it could be a slicer.util.bestFitSphereFromPoints function, in the same line as dataFrameFrom*, arrayFrom* functions in slicer.util. Using the Python manager via a temporary file is obviously not elegant from C++.</p>

---
