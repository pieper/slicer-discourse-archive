# Dillation of a specific label, and pushing other label?

**Topic ID**: 31808
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/dillation-of-a-specific-label-and-pushing-other-label/31808

---

## Post #1 by @Romain_Valabregue (2023-09-20 15:57 UTC)

<p>Dear all</p>
<p>This is my first post, so I would like to first thanks you for this nice community, this forum has already been a great source for me.</p>
<p>I am working with full brain segmentation, with tissue label (GM, WM, CSF, deep gray matter, ventricle ect…) and I would like to transform a given label map to a new one containing  bigger ventricles (simulation an old subject from a young one). The difficulty is that I would like to preserve the other labels ie pushing other neighbor labels. (ideally with a bit on contraction)</p>
<p>if I simply dilate the csf extracted mask, and incorporate it to the original label map this will erase neighbor labels<br>
So I was thinking to try with Simple itk DisplacementFieldTransform, if I could build a displacement field that would be initialized with the normal vector of the CSF surface, and gently smoothed.<br>
Any help how to get the normal vector and smooth a displacement field ? (sorry if this is not the right forum to ask)</p>
<p>Many thanks</p>
<p>Romain</p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2023-09-20 20:47 UTC)

<p>Ideally you would like to have the simulation that deformed the MR to export a nonlinear transform that you could apply to the segmentation.  Another alternative would be to segment using SynthSeg, which is nicely robust in the face of variations like large ventricles.  Otherwise you could try a nonlinear registration tool like BRAINSFit or Elastix to calculate a transform to apply to the segmentation.</p>

---

## Post #3 by @Romain_Valabregue (2023-09-21 06:11 UTC)

<p>The final objective is to deformed a given (high resolved) template to augment the labels in order to build a synthetic training set and to train a deep model exactly as proposed by SynthSeg (yes SynthSeg is nicely robust and I am a big fan of this method. Here I want to explore this approach but starting from only one template)<br>
I agree a non linear deformation would be an alternative, although I would prefer an intrinsic method (ie without the need of a reference), and also only specific to a given label boundary (ventricles, for instance).</p>

---

## Post #4 by @Romain_Valabregue (2023-09-21 06:50 UTC)

<p>Just to precise the question:</p>
<p>I can use skimage marching_cubes methods to get the normal vector of the mask, but how to put the normal vector list into a 3D grid (let say at the original dimension) ? and how to smooth the vector field after that ?</p>

---

## Post #7 by @mikebind (2023-09-21 18:58 UTC)

<p>You might find this approach helpful:  <a href="https://discourse.slicer.org/t/dynamic-3d-object-manipulation-for-surgery-simulation/22508/2" class="inline-onebox">Dynamic 3D Object Manipulation for surgery simulation - #2 by lassoan</a>.  The video shows how you can create a smooth nonlinear warping transformation via paired sets of markups points.  You could experiment with</p>
<ol>
<li>generating points at on the ventricle surface and at the distance at which you want no motion to occur</li>
<li>duplicating those points, and then displacing the ventricle surface points by the amount you want the ventricles to dilate and in the direction normal to the ventricle surface, while leaving the other points umoved</li>
</ol>
<p>The resulting transformation should (to a first approximation) show no motion at your fixed points or outside them (provided you have enough fixed points in enough directions), your specified displacement at the ventricle surfaces, and some sort of smoothed interpolation of partial displacement further out.  This may be good enough for your purposes, or you can try to refine it by adding more points along with the displacements you want to force at those locations.</p>

---

## Post #8 by @Romain_Valabregue (2023-09-25 07:10 UTC)

<p>thank you <a class="mention" href="/u/mikebind">@mikebind</a> this looks very nice, and it fits perfectly to what I was looking for.<br>
The only problem is that I need to do it automatically (to possibly incorporate it to torchio). Are you aware of any python script that implement those kind of transform ?</p>

---

## Post #9 by @mikebind (2023-09-25 17:25 UTC)

<p>Unfortunately, I am not aware of an existing python script which would set up and generate the transform you need automatically.  I looked briefly at the Fiducial Registration Wizard module code (available here: <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.cxx" rel="noopener nofollow ugc">https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.cxx</a> ), but it is in C++.  C++ modules are callable from python within Slicer, and if you got the inputs sorted out, you could definitely use this module to automatically generate the transform you need, and then could use a different resampling module (also callable using python) to automatically generate the warped version of the image.  What is not provided for in these steps is the generation of the sets of input points that will be used to generate the transform.  You would likely need to write that code yourself (in python would be fine) as your use case seems pretty specialized.  If you want to go that route, the approach I might try first is to</p>
<ol>
<li>set up a regular mesh of point coordinates which cover your image volume (a subset of these will be your non-moving points)</li>
<li>find a set of points on your ventricle surfaces, and gather the surface normal vector for each of your points</li>
<li>from your regular mesh of points found in step 1, remove any points which are within some defined distance from the ventricles</li>
<li>make a copy of the set of remaining points in step 3, and make a copy of the set of points from step 2.</li>
<li>combine one copy of the remaining mesh points with one copy of the ventricle surface points; this will be your unwarped (fixed) fiducial point set</li>
<li>For the other copy of the ventricle surface points, displace each point in the direction of the local surface normal some defined amount (however much you want to grow your ventricles) to form a warped ventricle set of points</li>
<li>combine the other copy of the remaining mesh points with this new warped set of ventricle surface points; this is your warped (moving) fiducial point set</li>
</ol>
<p>The fixed and moving fiducial point sets are the key inputs you’ll need to give to the Fiducial Registration Wizard, which would then be able to calculate the warping transform you are looking for.  I don’t see any reason you couldn’t get this procedure to be fully automated, but it will likely take some work setting it up and then experimenting with what is an acceptable density of points for your mesh, what is a good distance gap around the ventricles to allow deformation to occur over (the “defined distance” in step 3), what is a good density and choosing method for the number and location of ventricle surface points to use, etc.</p>

---

## Post #10 by @Romain_Valabregue (2023-09-26 14:27 UTC)

<p>Hi,<br>
thanks for the detailled description, and I agree there will need some development and tunning but I thinks it worth the try, so I am motivated.<br>
Your description of the step is very clear, and I should be able to go with it. The only question I have is about the points format. I guess it should be a python list, of (3D) coordinate but what is the unit ? Should I express those coordinate in the pixel space (integer grid from the original data) or in mm space (ie taking into account the affine of the 3D data.</p>
<p>Finally the more unclear part to me is how to finish the job once the Two set of point has been construct. (1) build the nonlinear transform, and 2) applied it to the image. I am not familiar with C++ module, how do I call them from python ? Probably if someone can point me the corresponding python code that Slicer use to implement it I should be able to copy paste the code I need. if it is not to big.<br>
Probably, I would also need other example of python script using 3D Slicer tool, so that I understand, which import (lib) I need to have access to those C++ binding (may be not, if the Slicer python code is enough to build a similar function but standalone …)</p>
<p>Many thanks</p>

---

## Post #11 by @mikebind (2023-09-26 18:48 UTC)

<aside class="quote no-group" data-username="Romain_Valabregue" data-post="10" data-topic="31808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/romain_valabregue/48/67363_2.png" class="avatar"> Romain_Valabregue:</div>
<blockquote>
<p>The only question I have is about the points format. I guess it should be a python list, of (3D) coordinate but what is the unit ? Should I express those coordinate in the pixel space (integer grid from the original data) or in mm space (ie taking into account the affine of the 3D data.</p>
</blockquote>
</aside>
<p>The points should be in mm space</p>
<aside class="quote no-group" data-username="Romain_Valabregue" data-post="10" data-topic="31808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/romain_valabregue/48/67363_2.png" class="avatar"> Romain_Valabregue:</div>
<blockquote>
<p>Finally the more unclear part to me is how to finish the job once the Two set of point has been construct. (1) build the nonlinear transform, and 2) applied it to the image. I am not familiar with C++ module, how do I call them from python ? Probably if someone can point me the corresponding python code that Slicer use to implement it I should be able to copy paste the code I need. if it is not to big.<br>
Probably, I would also need other example of python script using 3D Slicer tool, so that I understand, which import (lib) I need to have access to those C++ binding (may be not, if the Slicer python code is enough to build a similar function but standalone …)</p>
</blockquote>
</aside>
<p>I looked into the Fiducial Registration Wizard code a bit more, and I think the key function being used is provided by <code>vtkThinPlateSplineTransform</code>  (<a href="https://vtk.org/doc/nightly/html/classvtkThinPlateSplineTransform.html" class="inline-onebox">VTK: vtkThinPlateSplineTransform Class Reference</a>).  I do pretty much all of my work within the Slicer environment, so I am not very familiar with this, but I believe you can use VTK from python outside of Slicer without any problems (<a href="https://docs.vtk.org/en/latest/getting_started/index.html" class="inline-onebox">Getting Started - VTK documentation</a>).   It looks like you would create a vtkThinPlateSplineTransform, set the source and target landmarks, set the basis to R (because you’re in 3D), and then <code>Update()</code> to calculate the transform.  I’m sure there are other VTK functions which would allow you to apply that transform to a base image to generate a warped image.  This might be the best approach for you if you are looking to set up a pipeline which can run automatically outside of Slicer.  However, if it turns out you want to use Slicer functionality, you might also like to be aware that it is possible to access Slicer code without running the full GUI in a few different ways, and looking at this discussion might help orient and get you started: <a href="https://discourse.slicer.org/t/using-slicer-and-slicer-modules-from-command-line/8162" class="inline-onebox">Using Slicer and Slicer Modules from Command-Line</a></p>

---
