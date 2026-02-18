# Get the most separated points

**Topic ID**: 38020
**Date**: 2024-08-24
**URL**: https://discourse.slicer.org/t/get-the-most-separated-points/38020

---

## Post #1 by @chir.set (2024-08-24 09:32 UTC)

<p>Hello,</p>
<p>Given a cloud of points, what would be the smartest way to determine the two points that are most widely separated?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad775b5b361b7554e2de1a8230cdd036e15d089.png" alt="get_max_distance" data-base62-sha1="1xUovarHJgEBRWWO068T0jxJ3E5" width="545" height="240"></p>
<p>It is possible to loop through all points and calculate the distances between points so as to get the maximum, it would require n x n iterations. I wish to know if there exists a class that can do that, preferably not Python exclusive.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2024-08-24 16:50 UTC)

<p>This is a <a href="https://en.m.wikipedia.org/wiki/Smallest-circle_problem">classic computational geometry problem</a> with some smart solutions. I would expect that you do not have to implement one, but you can find free, open- source implementations in Python and C++.</p>

---

## Post #3 by @chir.set (2024-08-24 19:26 UTC)

<p>Thank you for the link.</p>
<p>vtkSphere offers to compute a <a href="https://vtk.org/doc/nightly/html/classvtkSphere.html#ad86cfd7f3ebd6f1d62ff06ad83aacdf5" rel="noopener nofollow ugc">bounding sphere</a>. The problem is that it requires a hints[2] field, which is a <em>guess</em> of the 2 most distant points. Random pairs give different results, so getting the exact pair of points is my purpose. I’ll delve further into this slowly.</p>

---

## Post #4 by @lassoan (2024-08-25 05:40 UTC)

<p>I<a href="https://github.com/Kitware/VTK/blob/550a7e3e94cffd25795a2362aefbcede2fe46b5e/Common/DataModel/vtkSphere.cxx#L59">mplementation in VTK</a> seems to be a standard one (same as in <a href="https://github.com/mrdoob/three.js/blob/3e6ab2d9c7f2d8e8d798aa5e1f628e25149e808c/src/objects/SkinnedMesh.js#L65">three.js</a>) that computes a bounding sphere with a simple method, which is not guaranteed to be minimal, but it is close. Hints are not required. If you don’t provide hints then the bounding box extreme points are used to initialize the computation.</p>
<p>If you only need an approximate binding sphere (that can be a few percent larger than needed) then this should work well. If you need the optimal sphere then it will require a more complex, more costly computation.</p>
<p>What are you planning to use this bounding sphere for?</p>

---

## Post #5 by @chir.set (2024-08-25 07:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="38020">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What are you planning to use this bounding sphere for?</p>
</blockquote>
</aside>
<p>It’s intended to add 1 more option to <a href="https://gitlab.com/chir-set/Tools7/-/tree/master/MarkupsToSurface/" rel="noopener nofollow ugc">this</a> module.</p>
<p>It needs not have an exact precision. However, the ‘hints[2]’ parameter can be passed as ‘nullptr’ in C++, while passing ‘None’ fails in Python. Passing arbitrary values like ‘[0, 0]’ is meaningless. How to handle this situation in Python?</p>

---

## Post #6 by @lassoan (2024-08-25 08:02 UTC)

<p>If <a href="https://docs.vtk.org/en/latest/advanced/PythonWrappers.html" class="inline-onebox">Python Wrappers - VTK documentation</a> does not help then you can ask on the VTK forum.</p>

---

## Post #7 by @mau_igna_06 (2024-08-25 19:11 UTC)

<p>Check 2nd question’s answer here:<br>
<a href="https://www.perplexity.ai/search/declare-a-vtkidtype-2-array-on-3XtK9t28SqKQerTfUb5X8g#1" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.perplexity.ai/search/declare-a-vtkidtype-2-array-on-3XtK9t28SqKQerTfUb5X8g#1</a></p>
<p>HIH</p>

---

## Post #8 by @chir.set (2024-08-25 20:00 UTC)

<p>Thanks for the link.</p>
<p>Unfortunately, I needed to pass a ‘None’ parameter that would mean ‘nullptr’, but the python wrapper always wants to pass ‘something’ else than 0x0 to the underlying C++ function.</p>
<p>It would have been nice if this C++ function signature defined ‘hints[2] = nullptr’ since it is optional. I suppose it should have worked.</p>
<p>Anyway, I’m baking a solution that should not be resource intensive.</p>

---

## Post #9 by @lassoan (2024-08-25 21:08 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="8" data-topic="38020">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>would have been nice if this C++ function signature defined ‘hints[2] = nullptr’ since it is optional.</p>
</blockquote>
</aside>
<p>Agreed. You can send a merge request to VTK with this simple change. It should go through review really quickly. You can also <span class="mention">@mention</span> David Gobbi in the merge request, asking him about the VTK null pointer syntax in Python (maybe there is a way to specify a null pointer just not documented well).</p>

---

## Post #10 by @chir.set (2024-08-26 11:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="38020">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>send a merge request to VTK</p>
</blockquote>
</aside>
<p>Ok, I’ll do that ASAP. Just hoping they don’t require a test case for such trivial change.</p>

---

## Post #11 by @chir.set (2024-08-26 20:04 UTC)

<p>I came up to this function to determine the two most distant points in a cloud of points. It’s decently fast, 0.06 s for 10⁶ points, 1.01 s for 10⁷ points, 11.69 s for 10⁸ points and bumps to 135.67 s for 10⁹ points.</p>
<p>The logic seems OK to me, dropping it here for any purpose and remaining open for comments.</p>
<pre><code class="lang-auto">def findMostDistantPoints(points : vtk.vtkPoints):
    pointData = points.GetData()
    numberOfPoints = points.GetNumberOfPoints()
    
    # Sort the points on each axis, get the bounding points.
    sorter = vtk.vtkSortDataArray()

    sorter.SortArrayByComponent(pointData, 0, 0)
    xMin = pointData.GetTuple3(0)
    xMax = pointData.GetTuple3(numberOfPoints - 1)

    sorter.SortArrayByComponent(pointData, 1, 0)
    yMin = pointData.GetTuple3(0)
    yMax = pointData.GetTuple3(numberOfPoints - 1)

    sorter.SortArrayByComponent(pointData, 2, 0)
    zMin = pointData.GetTuple3(0)
    zMax = pointData.GetTuple3(numberOfPoints - 1)

    boundingPoints = vtk.vtkPoints()
    boundingPoints.InsertNextPoint(xMin)
    boundingPoints.InsertNextPoint(xMax)
    boundingPoints.InsertNextPoint(yMin)
    boundingPoints.InsertNextPoint(yMax)
    boundingPoints.InsertNextPoint(zMin)
    boundingPoints.InsertNextPoint(zMax)
    
    # Calculate the distances between each pair of points: 6 x 6 iterations.
    distances = vtk.vtkDoubleArray()
    distances.SetNumberOfComponents(7)
    numberOfBoundingPoints = boundingPoints.GetNumberOfPoints()
    for i in range(numberOfBoundingPoints):
        referencePoint = boundingPoints.GetPoint(i)
        for j in range(numberOfBoundingPoints):
            nextPoint = boundingPoints.GetPoint(j)
            distance2 = vtk.vtkMath.Distance2BetweenPoints(referencePoint, nextPoint)
            distances.InsertNextTuple([referencePoint[0], referencePoint[1], referencePoint[2], nextPoint[0], nextPoint[1], nextPoint[2], distance2])
    
    # Sort the bounding points in descending order by distance squared.
    distanceSorter = vtk.vtkSortDataArray()
    distanceSorter.SortArrayByComponent(distances, 6, 1)
    
    # Get the most distant points.
    mostDistantTuple = distances.GetTuple(0)
    p1 = [mostDistantTuple[0], mostDistantTuple[1], mostDistantTuple[2]]
    p2 = [mostDistantTuple[3], mostDistantTuple[4], mostDistantTuple[5]]
    
    # Return as vtkPoints.
    result = vtk.vtkPoints()
    result.InsertNextPoint(p1)
    result.InsertNextPoint(p2)

    return result
</code></pre>

---

## Post #12 by @lassoan (2024-08-26 21:53 UTC)

<p>Computation is quite fast and the method is simple, but I don’t think it gives you the two farthest points (when the two farthest points are near the corners of the bounding box, in two opposite corners).</p>
<p>Instead of reinventing the wheel, you can use a free, open-source, restriction-free implementation like <a href="https://github.com/hbf/miniball">this</a>.</p>

---

## Post #13 by @chir.set (2024-08-27 06:40 UTC)

<p>Thank you for the interesting link and comment, they highlight situations termed as ‘degenerate’ which have not been accounted for.</p>

---

## Post #14 by @chir.set (2024-08-30 20:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="38020">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can send a merge request to VTK with this simple change.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>vtkSphere::ComputeBoundingSphere() has now an overload in <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/11444" rel="noopener nofollow ugc">VTK</a> that does not mandate a hint parameter. Thank you for your support.</p>

---

## Post #15 by @chir.set (2024-09-29 20:07 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="13" data-topic="38020">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>they highlight situations termed as ‘degenerate’ which have not been accounted for</p>
</blockquote>
</aside>
<p>This <a href="https://gitlab.com/chir-set/Tools7/-/blob/7311144c926479f5b209755be8f1e83dcb8e5942/MarkupsToSurface/MarkupsToSurface.py#L309" rel="noopener nofollow ugc">implementation</a> should overcome these limitations.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #16 by @lassoan (2024-09-29 21:36 UTC)

<p>How does it work? Have you you implemented a known algorithm, or you invented something new? If it is something new, how it compares to known algorithms?</p>

---

## Post #17 by @chir.set (2024-09-30 13:42 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="16" data-topic="38020">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How does it work?..?</p>
</blockquote>
</aside>
<p>On test data, it seems to be accurate. I’ll compare when VTK 8fcf3271ab is available in Slicer’s VTK. I just wanted to propose another possible solution to a question I opened.</p>

---
