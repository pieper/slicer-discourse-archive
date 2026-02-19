---
topic_id: 9898
title: "Control Of Rotation In Curved Planar Reformat Instead Of Usi"
date: 2020-01-21
url: https://discourse.slicer.org/t/9898
---

# Control of rotation in Curved Planar Reformat (instead of using Frenet Serret frame)

**Topic ID**: 9898
**Date**: 2020-01-21
**URL**: https://discourse.slicer.org/t/control-of-rotation-in-curved-planar-reformat-instead-of-using-frenet-serret-frame/9898

---

## Post #1 by @mikebind (2020-01-21 18:10 UTC)

<p>Hello, I was excited to discover the Curved Planar Reformat module recently.  It does 95% of what I need it for.  However, the rotation of the images in the straightened volume is sometimes awkward for my purposes.  I am reformatting down the centerline of airway in a CT volume, and would like to keep “up” in the reformatted volume to be in as consistent an anatomical direction as possible (for example, anterior). The current module uses Frenet-Serret frames, which makes a lot of sense for generality, but for anatomical interpretability it is more helpful if the output volume avoids twisting because of small wiggles in the curve.</p>
<p>I do see that there is a “Rotation angle” parameter in the existing CPR module, however I believe this applies a constant rotation to the Frenet-Serret frame, which does not solve my problem.</p>
<p>The current code uses vtkSplineDrivenImageSlicer, which calculates the Frenet-Serret frame internally and uses that to set the orientation of the output image slices.  What I would prefer would be the ability to supply preferred orientation information somehow.</p>
<p>Theoretically, it seems sufficient to supply one preferred orientation vector, and a second back-up one to use if the the curve is perpendicular to the first orientation vector.  Then, the “up” direction in the sliced image would be the projection of the preferred orientation vector into the slice plane.  If the slice plane were perpendicular to the preferred orientation vector (resulting in a zero projection), then the back-up orientation vector would be projected into the slice plane instead, and that direction used as “up”.  The transverse direction in the sliced images would be given by the cross-product of the curve tangent and the projected “up” vector (just like in the Frenet-Serret frame calculation of the binormal).</p>
<p>In my use case, the preferred orientation would be for “up” to be anterior in the original volume, with a back-up of orientation of “up” being inferior.</p>
<p>I think what I would like should be relatively straightforward to implement, but I have essentially no C++ skill, so I am feeling stuck as to how to proceed. Is there a way I could move forward using python, maybe with a simpler reslicer than vtkSplineDrivenImageSlicer?</p>
<p>Thanks for any help you can provide.</p>

---

## Post #2 by @pieper (2020-01-22 08:14 UTC)

<p>Hi - yes, what you describe sounds very doable (I’ve done the same in the past but the code was not open).  It sounds like you understand the math well enough that hopefully you could learn the C++ code or recreate the same in python.  Below is some similar code in python if you decide to go that route.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py#L314-L450" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py#L314-L450" target="_blank">Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py#L314-L450</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="314" style="counter-reset: li-counter 313 ;">
<li>class EndoscopyComputePath(object):</li>
<li>  """Compute path given a list of fiducials.</li>
<li>  A Hermite spline interpolation is used. See http://en.wikipedia.org/wiki/Cubic_Hermite_spline</li>
<li>
</li>
<li>  Example:</li>
<li>    result = EndoscopyComputePath(fiducialListNode)</li>
<li>    print "computer path has %d elements" % len(result.path)</li>
<li>
</li>
<li>  """</li>
<li>
</li>
<li>  def __init__(self, fiducialListNode, dl = 0.5):</li>
<li>    import numpy</li>
<li>    self.dl = dl # desired world space step size (in mm)</li>
<li>    self.dt = dl # current guess of parametric stepsize</li>
<li>    self.fids = fiducialListNode</li>
<li>
</li>
<li>    # hermite interpolation functions</li>
<li>    self.h00 = lambda t: 2*t**3 - 3*t**2     + 1</li>
<li>    self.h10 = lambda t:   t**3 - 2*t**2 + t</li>
<li>    self.h01 = lambda t:-2*t**3 + 3*t**2</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py#L314-L450" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2020-01-22 09:40 UTC)

<p>Could you show a few screenshots that illustrate unwanted wiggles?</p>
<p>Switching between primary and secondary “up” direction is not trivial (there could be artifacts due to the sudden twist). Have you tried this on curves that had sections with large bends?</p>
<p>In endoscopy module, rotation is constrainex automatically based on plane fitting (<a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py#L29">“up” vector is the least-square-fit plane normal</a>). Would that work for you? “up” is not aligned with any anatomical direction exactly but it is more robust (less chance of tangent being nearly equal to “up”) and simpler for the user (no need to choose a direction manually). Maybe we can add options for choosing eirher fitted plane normal or one of the anatomical axes.</p>

---

## Post #4 by @mikebind (2020-01-23 18:51 UTC)

<p>Yes, I will try to get to posting some screenshots soon.</p>
<p>I’ll also take a look at the way the endoscopy module does it.  Thanks for taking a look at this!</p>

---

## Post #5 by @mikebind (2020-01-27 16:53 UTC)

<p>Looking at the Endoscopy module, I think I may not understand it correctly.  I can see that the Endoscopy module fits a plane to all the supplied points, and then finds the normal to that plane, and then I thought it used that normal to determine the camera View Up vector.  However, this does not appear to be the case.</p>
<p>The fit plane normal is definitely used to set the Transform which is used to place the cursor model on the path, but the orientation of this model actually isn’t important because it’s a sphere.  <a href="https://github.com/Slicer/Slicer/blob/bd9e2c0b4d2855cb4e24b5331f994e064d1f21e2/Modules/Scripted/Endoscopy/Endoscopy.py#L290-L309" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/bd9e2c0b4d2855cb4e24b5331f994e064d1f21e2/Modules/Scripted/Endoscopy/Endoscopy.py#L290-L309</a></p>
<p>Instead, I think the only thing which is changing the camera View Up is the camera OrthogonalizeViewUp() command ( <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py#L282" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py#L282</a>).  I think this effectively takes whatever the current camera ViewUp vector is, projects it into the plane orthogonal to the current view, and renormalizes.  In the vtkCamera code, there is also an optional UserViewTransform which I don’t understand (<a href="https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/Core/vtkCamera.cxx#L346-361" rel="nofollow noopener">https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/Core/vtkCamera.cxx#L346-361</a>), but at least in the absence of this, I think the camera view up is not based on the fit plane at all.  Instead, I think that the endoscopy camera view management is based on minimally changing it from whatever the view up was in the previous view. This makes for smooth changes from frame to frame, but does nothing to privilege any particular direction.</p>
<p>However, I think I now understand enough about how this works to get a version working on my own.  If I am successful, I will try to come back and post my solution here.</p>

---

## Post #6 by @lassoan (2020-01-27 20:12 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="5" data-topic="9898">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Looking at the Endoscopy module, I think I may not understand it correctly. I can see that the Endoscopy module fits a plane to all the supplied points, and then finds the normal to that plane, and then I thought it used that normal to determine the camera View Up vector. However, this does not appear to be the case.</p>
</blockquote>
</aside>
<p>Yes, this is correct and as intended. We only use the curve normal in the Transform node update; the 3D view camera’s view up is kept as is (only orthogonalized with the view normal direction).</p>
<p>The transform node is computed so that it can be used for reslicing the images (e.g., using SlicerIGT extension’s Volume Reslice Driver module), position models, etc.</p>

---
