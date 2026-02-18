# Do projection from polydata to a model surface

**Topic ID**: 18451
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/do-projection-from-polydata-to-a-model-surface/18451

---

## Post #1 by @sandyaa0313 (2021-07-01 09:24 UTC)

<p>Operating system: windows10<br>
Slicer version:4.11.20200930<br>
I want to do the orthogonal projection (or just the simplest projection) from a polydata array to a model surface. The input polydata is the edge of another model.<br>
My goal is to receive the new coordinates of polydata after the projection, but I don’t know how to do the projection.<br>
Now I only know how to get the coordinates from polydata, just like the code below. Thanks!</p>
<p>Here is my code:</p>
<p>PolyData = modelNode.GetPolyData()<br>
Point_coordinates = PolyData.GetPoints().GetData()<br>
numpy_coordinates = numpy_support.vtk_to_numpy(Point_coordinates)</p>

---

## Post #2 by @lassoan (2021-07-02 04:59 UTC)

<p>It is not yet completely clear what you would like to achieve. A model node already stores a polydata. Maybe it would be easier if you attached an image.</p>
<p>If you want to transfer scalar values from one model to another then you use the method described here:</p>
<aside class="quote quote-modified" data-post="3" data-topic="15682">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/merge-scalars-of-two-models/15682/3">Merge scalars of two models</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If you want to keep the models separate and just copy the scalar data then you can achieve it by following these steps: 

install ModelToModelDistance extension and use Model to model distance module to compute vector that moves points of one surface to the other (based on closest point of one surface on the other) - result will be stored in PointToPointVector point array of the output mesh
use vtkWarpVector filter with PointToPointVector to warp the model to match the surface of the other model
…
  </blockquote>
</aside>


---

## Post #3 by @sandyaa0313 (2021-07-02 15:42 UTC)

<p>I have three input models. One is the chest wall model(3d), and others are breast models(surfaces).<br>
My goal is to calculate the breast volume. These three models are already in the correct relative positions. So I need to closing each breast model to the chest wall model.<br>
I have no  idea now, so I think getting the new coordinates of breast model after projection(red dotted line on the chest wall) may helps. Thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fd9b19df7bbe47207d4860c42fc0e9e4ecf6fda.jpeg" data-download-href="/uploads/short-url/6PiQzz8JRCLXRJoMB9Xxs69LYNQ.jpeg?dl=1" title="3d_slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fd9b19df7bbe47207d4860c42fc0e9e4ecf6fda_2_374x500.jpeg" alt="3d_slicer" data-base62-sha1="6PiQzz8JRCLXRJoMB9Xxs69LYNQ" width="374" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fd9b19df7bbe47207d4860c42fc0e9e4ecf6fda_2_374x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fd9b19df7bbe47207d4860c42fc0e9e4ecf6fda_2_561x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2fd9b19df7bbe47207d4860c42fc0e9e4ecf6fda_2_748x1000.jpeg 2x" data-dominant-color="94928B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d_slicer</span><span class="informations">1108×1478 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-07-02 15:58 UTC)

<p>We have come up with a complete workflow for measuring breast volume from surfaces, which may be exactly what you need:</p>
<ul>
<li><a href="https://qspace.library.queensu.ca/jspui/bitstream/handle/1974/26146/House_Rachael_M_201904_MSc.pdf?sequence=3&amp;isAllowed=y">Master thesis describing all the details</a></li>
<li><a href="https://github.com/PerkLab/BreastReconstruction">Slicer extension implementing all the computations</a></li>
</ul>

---

## Post #5 by @sandyaa0313 (2021-07-04 05:57 UTC)

<p>I’ve tried, but this module seems not to suit for my case.<br>
I already have chest model so I don’t have to use markup points to create the chest wall.<br>
Because the chest wall in breast reconstruction module is created by markup points, and markup points are situated on the breast model, it can create a closed model obviously.<br>
However, in my module, the chest wall model is from CT, and the breast model is from 3d scan, they are aligned but with some distance.<br>
I think these two modules have different ideas. The breast reconstruction model focus on the volume difference between the breasts, but I focus on the exact volume.<br>
So, I still want to ask how to project a breast model on the chest wall model and get its new position.<br>
Thank you! Sorry to ask so many questions.</p>
<p>I try to draw their difference. In the breast reconstruction model, the chest wall latter sticks to the surface model of 3d scan.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e339ce9df1e14da8248b50d48ae4aa9d0064b9c2.jpeg" data-download-href="/uploads/short-url/wq8eGKoq6IUawzhVeC97qJjWviG.jpeg?dl=1" title="B124BDE3-BD02-44A8-B87A-D5B10FC74262" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e339ce9df1e14da8248b50d48ae4aa9d0064b9c2_2_375x500.jpeg" alt="B124BDE3-BD02-44A8-B87A-D5B10FC74262" data-base62-sha1="wq8eGKoq6IUawzhVeC97qJjWviG" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e339ce9df1e14da8248b50d48ae4aa9d0064b9c2_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e339ce9df1e14da8248b50d48ae4aa9d0064b9c2_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e339ce9df1e14da8248b50d48ae4aa9d0064b9c2_2_750x1000.jpeg 2x" data-dominant-color="B0AFAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">B124BDE3-BD02-44A8-B87A-D5B10FC74262</span><span class="informations">3024×4032 2.68 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here is how my chest model built. The picture is in the paper you sent.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ebbc573110846c0ab1afef330e81ae04fc08fab.jpeg" alt="chest_wall" data-base62-sha1="mEdJMDdTcxKHeogtl2i02btSAfV" width="481" height="314"></p>

---

## Post #8 by @sandyaa0313 (2021-07-04 16:50 UTC)

<p>Sorry. I want to explain my goal explicitly.<br>
Actually I want to close these 3 models and their junctions are situated on the<br>
projection coordinates.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6026af7e900813a246dacccfe36781ce9795a210.jpeg" alt="c" data-base62-sha1="dIAIFFCIjClzdeSMwYSW16I8lfq" width="438" height="301"></p>

---

## Post #9 by @lassoan (2021-07-09 14:56 UTC)

<p>You can segment the skin surface, subtract the chest wall segment from it (using Logical operators effect), then trim the resulting segment using Scissors effect.</p>

---
