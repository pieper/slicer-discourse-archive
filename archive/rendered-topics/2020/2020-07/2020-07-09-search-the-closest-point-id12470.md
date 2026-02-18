# Search the closest point

**Topic ID**: 12470
**Date**: 2020-07-09
**URL**: https://discourse.slicer.org/t/search-the-closest-point/12470

---

## Post #1 by @loubna (2020-07-09 18:55 UTC)

<p>Hi;<br>
I have found many spatial locators like : vtkPointLocator, vtkKdTree, and vtkOctreePointLocator, but I am confused about the most efficent one.</p>
<p>I have a polydata from which I construct a vtkImageData using some filters like (vtkPolydataToImageData, vtkExtruderFilter and vtkImageStencil).I want for each point in the polydata search  the closest point in the vtkImageData and extract the scalar value.</p>
<p>My question is : what is the the best spatial Locator which I can use in this case.</p>
<p>thank you very much in advance</p>

---

## Post #2 by @lassoan (2020-07-09 19:15 UTC)

<p>There is no “best” one (otherwise only that one would be kept in VTK and the others would be removed). Each has its own advantages and disadvantages. Also note that there are many other locators, including cell locators (which provide nearest position on the surface, not the nearest mesh point).</p>
<aside class="quote no-group" data-username="loubna" data-post="1" data-topic="12470">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/cab0a1/48.png" class="avatar"> loubna:</div>
<blockquote>
<p>I want for each point in the polydata search the closest point in the vtkImageData and extract the scalar value.</p>
</blockquote>
</aside>
<p>vtkImageData is solid structured grid block, so you don’t need to use locator to get voxel position (locators are only for meshes).</p>
<p>You can get image scalar value at all points of a model using vtkProbeFilter. It is available in Slicer with a convenient GUI in “Probe volume with model” module.</p>

---

## Post #3 by @loubna (2020-07-10 10:09 UTC)

<p>Hi Mr;</p>
<p>I have constructed vtkImageData from a set Of planar Contours (after doing some operations inspired from SlicerRT : fixHoles, sort Contours…) the imageData is well reconstruted in some cases.</p>
<p>Now I want retrieve for each polydata point of contour, scalar value from vtkImagedata.</p>
<p>I threw a glance on “ProbeVolume with Model” .cxx code. But, to be able to Apply vtkProbFilter I must do some conversions between spaces (ijk To RAs). How can I get IJKTo Ras Matrix from the reconstructed imagedata in my case?</p>

---

## Post #4 by @lassoan (2020-07-10 17:36 UTC)

<p>You can do the same as it is done in “Probe volume with model” module.</p>

---
