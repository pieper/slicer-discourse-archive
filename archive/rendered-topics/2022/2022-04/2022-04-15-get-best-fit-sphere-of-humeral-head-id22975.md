# Get best fit sphere of humeral head

**Topic ID**: 22975
**Date**: 2022-04-15
**URL**: https://discourse.slicer.org/t/get-best-fit-sphere-of-humeral-head/22975

---

## Post #1 by @osints (2022-04-15 11:09 UTC)

<p>Hi,<br>
I am tyring to makes best fit sphere of humeral head.<br>
So i makes 3 land marks and then import above code to python interactor.<br>
but there is no sphere and some red text is shown…<br>
plase some help…<br>
thank you<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39abd41525623548dd32836cf746cbe89940c6e5.png" data-download-href="/uploads/short-url/8ebm6DRPlt5aT9NnGg9Qv03QvNX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39abd41525623548dd32836cf746cbe89940c6e5.png" alt="image" data-base62-sha1="8ebm6DRPlt5aT9NnGg9Qv03QvNX" width="690" height="410" data-dominant-color="FBF7FB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1267×753 17.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32cbd449d2009566db530bd7ac5fe1a9416f12c3.png" data-download-href="/uploads/short-url/7fmzGUypMOiRlfu6O80HIIiwhKX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32cbd449d2009566db530bd7ac5fe1a9416f12c3.png" alt="image" data-base62-sha1="7fmzGUypMOiRlfu6O80HIIiwhKX" width="690" height="446" data-dominant-color="EAF8CD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1413×915 21.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jamesobutler (2022-04-15 11:38 UTC)

<p><code>slicer.util.arrayfromMarkupsControlPoints(markups)</code> has an undefined “markups” object. This variable must be a reference to your point list.</p>
<p><code>markups=slicer.util.getNode("F")</code> is example code of getting a point list with a current name of “F” which is a common default name for it.</p>

---

## Post #5 by @osints (2022-04-16 11:16 UTC)

<p>Thank you…<br>
That`s works.<br>
I have some more questions.</p>
<ol>
<li>Can i get center point of that sphere?</li>
<li>Is there any method that one plane move to crossing the point which made by question 1. (Center ponints of sphere)</li>
<li>Is there any method that calculate the distance between above 2 planes.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec1ab4cc637e23071b6867dd9f839b09b859ad9c.jpeg" data-download-href="/uploads/short-url/xGFTR18vVsIEP1FWyBinwH4cMoc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec1ab4cc637e23071b6867dd9f839b09b859ad9c_2_482x499.jpeg" alt="image" data-base62-sha1="xGFTR18vVsIEP1FWyBinwH4cMoc" width="482" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ec1ab4cc637e23071b6867dd9f839b09b859ad9c_2_482x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec1ab4cc637e23071b6867dd9f839b09b859ad9c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec1ab4cc637e23071b6867dd9f839b09b859ad9c.jpeg 2x" data-dominant-color="A59F8A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">568×588 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2022-04-16 14:19 UTC)

<aside class="quote no-group" data-username="osints" data-post="5" data-topic="22975">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/4af34b/48.png" class="avatar"> osints:</div>
<blockquote>
<p>Can i get center point of that sphere?</p>
</blockquote>
</aside>
<p>Yes, sure. You have set it yourself in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-control-points">script</a>: <code>sphere.SetCenter(centerX, centerY, centerZ)</code></p>
<aside class="quote no-group" data-username="osints" data-post="5" data-topic="22975">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/4af34b/48.png" class="avatar"> osints:</div>
<blockquote>
<p>Is there any method that one plane move to crossing the point which made by question 1. (Center ponints of sphere)</p>
</blockquote>
</aside>
<p>You can create a plane at any position. Add a new plane node, set its position to the sphere centerpoint, and set a normal.</p>
<aside class="quote no-group" data-username="osints" data-post="5" data-topic="22975">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/4af34b/48.png" class="avatar"> osints:</div>
<blockquote>
<p>Is there any method that calculate the distance between above 2 planes.</p>
</blockquote>
</aside>
<p>You can use basic computational geometry methods for computing distances, angles between points, lines, planes, project points, lines, determine intersections, etc. There are a couple of <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-markup-planes">examples in the script repository</a> to see how to get inputs and show outputs in Slicer, and you can learn the rest by typing your question into Google search (for example <code>python distance between two planes</code>) and reading through the search results. You will get both detailed mathematical explanation and complete Python implementations (typically few lines of numpy code). If you really get stuck then you can ask here, but it could be useful for you to spend some with reading and experimenting.</p>

---

## Post #7 by @osints (2022-04-17 02:54 UTC)

<p>thank you…<br>
I have some more question…<br>
I can`t find by google search…</p>
<ol>
<li>
<p>Can i get center point of that sphere? → I`m trying to find center point of sphere aleady made by humeral head fiduciel not set a center point before making sphere.</p>
</li>
<li>
<p>I want make plane which are exactly parallel to one plane (Aleady made by GT foot print) and crossing center points of sphere.</p>
</li>
<li>
<p>can i subtract plane by overlapped with humerus bone defect?<br>
I want measure the depth of defect. image below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b236a91ac75676c1f193cedc57bef267b64470e.jpeg" alt="image" data-base62-sha1="69Cpr4YyYtXfNXW1C1cBRXjt49E" width="338" height="347"></p>
</li>
</ol>

---

## Post #8 by @lassoan (2022-04-17 03:29 UTC)

<aside class="quote no-group" data-username="osints" data-post="7" data-topic="22975">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/4af34b/48.png" class="avatar"> osints:</div>
<blockquote>
<p>Can i get center point of that sphere? → I`m trying to find center point of sphere aleady made by humeral head fiduciel not set a center point before making sphere.</p>
</blockquote>
</aside>
<p>The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-control-points">script</a> computes the centerpoint position and stores it in <code>centerX, centerY, centerZ</code>.</p>
<aside class="quote no-group" data-username="osints" data-post="7" data-topic="22975">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/4af34b/48.png" class="avatar"> osints:</div>
<blockquote>
<p>I want make plane which are exactly parallel to one plane (Aleady made by GT foot print) and crossing center points of sphere.</p>
</blockquote>
</aside>
<p>The plane orientation is defined by the plane normal vector. You can create parallel planes by setting the same plane normal vector.</p>
<aside class="quote no-group" data-username="osints" data-post="7" data-topic="22975">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/4af34b/48.png" class="avatar"> osints:</div>
<blockquote>
<p>can i subtract plane by overlapped with humerus bone defect?<br>
I want measure the depth of defect. image below</p>
</blockquote>
</aside>
<p>You can use Dynamic Modeler to cut a model with planes.</p>
<p>For making measurements you probably don’t need to actually cut a model, but it is enough to view a cross-section in a slice view. You can enable display of slice intersections and then rotate the slice intersections; or you can enable <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">reformat</a> widget to translate/rotate a slice plane in 3D.</p>

---

## Post #9 by @gsirca (2022-07-28 18:10 UTC)

<p>Hello,<br>
I’m experiencing the same problem:</p>
<pre><code class="lang-auto"># Get markup node from scene
&gt;&gt;&gt; pointListNode = slicer.util.getNode("F")
&gt;&gt;&gt; 
&gt;&gt;&gt; from scipy.optimize import least_squares
&gt;&gt;&gt; import numpy
&gt;&gt;&gt; 
&gt;&gt;&gt; def fit_sphere_least_squares(x_values, y_values, z_values, initial_parameters, bounds=((-numpy.inf, -numpy.inf, -numpy.inf, -numpy.inf),(numpy.inf, numpy.inf, numpy.inf, numpy.inf))):
...   """
...   Source: https://github.com/thompson318/scikit-surgery-sphere-fitting/blob/master/sksurgeryspherefitting/algorithms/sphere_fitting.py
...   Uses scipy's least squares optimisor to fit a sphere to a set
...   of 3D Points
...   :return: x: an array containing the four fitted parameters
...   :return: ier: int An integer flag. If it is equal to 1, 2, 3 or 4, the
...           solution was found.
...   :param: (x,y,z) three arrays of equal length containing the x, y, and z
...           coordinates.
...   :param: an array containing four initial values (centre, and radius)
...   """
...   return least_squares(_calculate_residual_sphere, initial_parameters, bounds=bounds, method="trf", jac="3-point", args=(x_values, y_values, z_values))
... 
&gt;&gt;&gt; def _calculate_residual_sphere(parameters, x_values, y_values, z_values):
...   """
...   Source: https://github.com/thompson318/scikit-surgery-sphere-fitting/blob/master/sksurgeryspherefitting/algorithms/sphere_fitting.py
...   Calculates the residual error for an x,y,z coordinates, fitted
...   to a sphere with centre and radius defined by the parameters tuple
...   :return: The residual error
...   :param: A tuple of the parameters to be optimised, should contain [x_centre, y_centre, z_centre, radius]
...   :param: arrays containing the x,y, and z coordinates.
...   """
...   #extract the parameters
...   x_centre, y_centre, z_centre, radius = parameters
...   #use numpy's sqrt function here, which works by element on arrays
...   distance_from_centre = numpy.sqrt((x_values - x_centre)**2 + (y_values - y_centre)**2 + (z_values - z_centre)**2)
...   return distance_from_centre - radius
... 
&gt;&gt;&gt; # Fit a sphere to the markups fidicual points
&gt;&gt;&gt; markupsPositions = slicer.util.arrayFromMarkupsControlPoints("F")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "D:\gsirc\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py", line 1808, in arrayFromMarkupsControlPoints
    numberOfControlPoints = markupsNode.GetNumberOfControlPoints()
AttributeError: 'str' object has no attribute 'GetNumberOfControlPoints'
&gt;&gt;&gt; import numpy as np
&gt;&gt;&gt; # initial guess
&gt;&gt;&gt; center0 = np.mean(markupsPositions, 0)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'markupsPositions' is not defined
&gt;&gt;&gt; radius0 = np.linalg.norm(np.amin(markupsPositions,0)-np.amax(markupsPositions,0))/2.0
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'markupsPositions' is not defined
&gt;&gt;&gt; fittingResult = fit_sphere_least_squares(markupsPositions[:,0], markupsPositions[:,1], markupsPositions[:,2], [center0[0], center0[1], center0[2], radius0])
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'markupsPositions' is not defined
&gt;&gt;&gt; [centerX, centerY, centerZ, radius] = fittingResult["x"]
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'fittingResult' is not defined
&gt;&gt;&gt; 
&gt;&gt;&gt; # Create a sphere using the fitted parameters
&gt;&gt;&gt; sphere = vtk.vtkSphereSource()
&gt;&gt;&gt; sphere.SetPhiResolution(30)
&gt;&gt;&gt; sphere.SetThetaResolution(30)
&gt;&gt;&gt; sphere.SetCenter(centerX, centerY, centerZ)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'centerX' is not defined
&gt;&gt;&gt; sphere.SetRadius(radius)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
NameError: name 'radius' is not defined
&gt;&gt;&gt; sphere.Update()
&gt;&gt;&gt; 
&gt;&gt;&gt; # Add the sphere to the scene
&gt;&gt;&gt; modelsLogic = slicer.modules.models.logic()
&gt;&gt;&gt; model = modelsLogic.AddModel(sphere.GetOutput())
&gt;&gt;&gt; model.GetDisplayNode().SetSliceIntersectionVisibility(True)
&gt;&gt;&gt; model.GetDisplayNode().SetSliceIntersectionThickness(3)
&gt;&gt;&gt; model.GetDisplayNode().SetColor(1,1,0)
&gt;&gt;&gt; 
&gt;&gt;&gt; 
</code></pre>
<p>Can anybody provide some help?</p>

---

## Post #10 by @lassoan (2022-07-28 18:16 UTC)

<aside class="quote no-group" data-username="gsirca" data-post="9" data-topic="22975">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/a587f6/48.png" class="avatar"> gsirca:</div>
<blockquote>
<p><code>markupsPositions = slicer.util.arrayFromMarkupsControlPoints("F")</code></p>
</blockquote>
</aside>
<p><code>F</code> is the a name of a node. <code>slicer.util.arrayFromMarkupsControlPoints</code> requires a node object as input. You can get the node object from a node name by calling <code>getNode()</code>:</p>
<p><code>markupsPositions = slicer.util.arrayFromMarkupsControlPoints(slicer.util.getNode("F"))</code></p>

---

## Post #11 by @gsirca (2022-07-30 14:19 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="10" data-topic="22975">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.util.getNode(“F”)</p>
</blockquote>
</aside>
<p>Thank you for the help. It worked smoothly.</p>

---

## Post #13 by @Bkeohane (2022-12-07 13:48 UTC)

<p>Hi, I succesfully extratced the coordinates and radius and I assume, they are in mm, right?</p>

---

## Post #14 by @lassoan (2022-12-07 14:58 UTC)

<p>Yes, length unit is millimeters by default. It is always recommended to validate your entire workflow by testing on some object of known size.</p>

---
