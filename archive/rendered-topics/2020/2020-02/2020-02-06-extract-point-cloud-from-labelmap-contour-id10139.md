---
topic_id: 10139
title: "Extract Point Cloud From Labelmap Contour"
date: 2020-02-06
url: https://discourse.slicer.org/t/10139
---

# Extract point cloud from labelMap contour

**Topic ID**: 10139
**Date**: 2020-02-06
**URL**: https://discourse.slicer.org/t/extract-point-cloud-from-labelmap-contour/10139

---

## Post #1 by @loubna (2020-02-06 14:46 UTC)

<p>Hi,</p>
<p>I want to Apply two filters on a binary volume (labelMap). The first one is 3D Gaussian filter to blur the boundry between inside and outside voxels , and the second one is the sobel filter at the voxel locations corresponding to the contour of the labelMap in order to calculate the gradiant . The resulting gradiants at the set of contour points are then normalized and negated to produce the normal associated with each point contour.</p>
<p>My question is how to transform the voxels of labelMap to 3D points? and how to extract the set of 3D points situated on the contour of the label Map in order to Apply the sobel filter and deduce the normals?<br>
are there VTK filters to do this in c++?</p>
<p>Thank you in advance fro your help</p>

---

## Post #2 by @lassoan (2020-02-06 15:06 UTC)

<p>No need to reimplement basic features such as labelmap to point cloud (surface mesh) conversion: in Data module, right-click on your labelmap volume to convert it to segmentation, then right-click on the segmentation to export it to model node.</p>

---

## Post #3 by @loubna (2020-02-06 15:12 UTC)

<p>Thanks for your response.</p>
<p>I need to re-implment the process using vtk and c++. My goal is to use MPU implicite models to reconstruct a smooth surface . So i need to know how can i do this using VTK filters.</p>

---

## Post #4 by @lassoan (2020-02-06 15:40 UTC)

<aside class="quote no-group" data-username="loubna" data-post="3" data-topic="10139">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/cab0a1/48.png" class="avatar"> loubna:</div>
<blockquote>
<p>My goal is to use MPU implicite models to reconstruct a smooth surface</p>
</blockquote>
</aside>
<p>If your goal is to implement a particular method then sure, go on, implement it. If you want to solve a clinical problem then you can sidestep the hard problem of creating smooth surface from parallel contours: create surface from the 3D labelmap directly.</p>
<p>If you want to extract smaller details than those that are actually visible in the image (e.g., you want to segment a thin boundary that you know is there, even if it is not visible in the image) then you can oversample the input volume: either use Crop volume module on the input volume before segmentation; or use segmentation geometry button next to master volume selector in Segment Editor module and specify an oversampling factor &gt; 1.</p>

---

## Post #5 by @loubna (2020-02-10 09:16 UTC)

<p>In fact, my target is to implement a particular method in which i find some difficulties to start. So my question is simple. I have a labelMap as input , I need to compute the normal vectors only on points contours of the labelMap  and not at the entire  label Map.</p>
<p>I Wonder if is there a way to compute contour’s points informations from labelMap in c++ and using VTK filters (i talk about implementation aspect )?</p>
<p>I can use  this vtkImageData ::GetPointData() -&gt; vtkPointData ::GetScalars() -&gt; vtkDataArray::getVoidPointer()  to get the set of points but what i nedd is only the points of labelMap’s contour.<br>
I hope my question is clear. Thank’s in advance Mr.</p>

---

## Post #6 by @lassoan (2020-02-11 14:22 UTC)

<aside class="quote no-group" data-username="loubna" data-post="5" data-topic="10139">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/cab0a1/48.png" class="avatar"> loubna:</div>
<blockquote>
<p>I need to compute the normal vectors only on points contours of the labelMap and not at the entire label Map.</p>
</blockquote>
</aside>
<p>What do you mean by “points contours of the labelMap”?</p>
<aside class="quote no-group" data-username="loubna" data-post="5" data-topic="10139">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/cab0a1/48.png" class="avatar"> loubna:</div>
<blockquote>
<p>I Wonder if is there a way to compute contour’s points informations from labelMap in c++ and using VTK filters (i talk about implementation aspect )?</p>
</blockquote>
</aside>
<p>To avoid premature optimization (and since gradient computation is so quick), I would recommend to compute the gradient for the entire image using vtkImageGradient and then use vtkProbeFilter to get the gradient at every point of a point set. If later the step proves to be a performance bottleneck then you can still revisit this.</p>

---

## Post #7 by @loubna (2020-02-13 13:27 UTC)

<p>Thank you for the response.  what i mean by contours of labelMap is I need only the informations (gradiants at labelMap outlines and not at each voxel of the label Map. I found this filter, I think is what i must to use if i need only the contours:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">
      <a href="https://discourse.vtk.org/t/how-to-render-the-pixel-contour-of-an-image-follow-up/463" target="_blank" title="03:44PM - 12 March 2019" rel="nofollow noopener">VTK – 12 Mar 19</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<h3><a href="https://discourse.vtk.org/t/how-to-render-the-pixel-contour-of-an-image-follow-up/463" target="_blank" rel="nofollow noopener">"How to render the pixel contour of an image" Follow-Up</a></h3>

<p>I have a follow-up question to this thread: https://public.kitware.com/pipermail/vtkusers/2011-June/068268.html  I have the same problem that his example pictures demonstrate well - I want to render the edges of the “inside” mask pixels, not contours...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #8 by @loubna (2020-02-14 10:07 UTC)

<p>Hi Mr;</p>
<p>And my last question is: in fact to compute the normal vector at each point. I applied “vtkImageGaussianSmooth” on the labelMap to get a blurred label Map like this:</p>
<pre><code> double gaussianStandardDeviation = 2.0;
 vtkSmartPointer&lt;vtkImageGaussianSmooth&gt; gaussian =
 vtkSmartPointer&lt;vtkImageGaussianSmooth&gt;::New();
 gaussian-&gt;SetStandardDeviations (gaussianStandardDeviation,
                           gaussianStandardDeviation,
                            gaussianStandardDeviation);
 
gaussian-&gt;SetInputData(labelMap);
gaussian-&gt;Update();
</code></pre>
<p>then to get the gradiant, I wish Apply the soble filter using " [vtkImageSobel3D]"</p>
<p>Now the last step is to deduce the normal vector from gradiant. I know how to recover the x,y,z components, but how to compute the norm of the vector  and get the normal vector from gradiant image? are there vtk filters to do that?</p>

---

## Post #9 by @lassoan (2020-02-16 13:43 UTC)

<p>To get the image gradient, do not use the Sobel operator, but vtkImageGradient filter.</p>

---

## Post #10 by @loubna (2020-02-16 14:05 UTC)

<p>OK this is a one a solution. But in the method which I try to implement uses:</p>
<p>3d gaussain filter to get a blurred label Map. Then it applied a 3D sobel filter to the blurred volume  to compute the gradiant at each voxel location. The Sobel filter was chosen because it takes into account information on the diagonals surrounding the processed point in addition to the information<br>
along the volume’s axes.The resulting gradient is normalized and negated to produce the normal associated with each input point.  My ambiguity is when i apply the soble Filter, how can I transform the scalars to vectors in order to normalize  them and obtain the normal vector which points away from the model’s interior.</p>

---

## Post #11 by @lassoan (2020-02-16 14:19 UTC)

<aside class="quote no-group" data-username="loubna" data-post="10" data-topic="10139">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/cab0a1/48.png" class="avatar"> loubna:</div>
<blockquote>
<p>Then it applied a 3D sobel filter to the blurred volume to compute the gradiant at each voxel location</p>
</blockquote>
</aside>
<p>The Sobel operator returns something similar to to gradient magnitude. It is not the gradient.</p>
<p>If you are interested in the gradient vector then use vtkImageGradient filter. If you need the gradient magnitude then use vtkImageGradientMagnitude filter.</p>

---
