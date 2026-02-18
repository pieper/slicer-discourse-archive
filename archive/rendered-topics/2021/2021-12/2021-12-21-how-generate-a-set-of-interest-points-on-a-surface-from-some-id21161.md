# How generate a set of interest points on a surface from some points.

**Topic ID**: 21161
**Date**: 2021-12-21
**URL**: https://discourse.slicer.org/t/how-generate-a-set-of-interest-points-on-a-surface-from-some-points/21161

---

## Post #1 by @egomiguel (2021-12-21 05:13 UTC)

<p>Hello, I have been able to see in some surgical navigation systems (like Mako for example) selecting some points, the system can generate automatically a broader set of points in places of interest.<br>
For example, in this case:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7721a8fa575f9676d9fcb5176bac11549beb1000.png" alt="Hip_Points" data-base62-sha1="gZSVZueUZSt2rilfFwFJsR3xCyA" width="456" height="440"><br>
<em>Figure 1. A 3D image of the pelvis and three selected points.</em></p>
<p>Selecting those 3 points (A, B, C) is enough to generate these other set of points</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93466bd5b606e5368f57160ea389fbb3cc2d2289.png" alt="Hip_All_Points" data-base62-sha1="l0R41EaYm0rMLT2aJXVpvXGv1VL" width="550" height="476"><br>
<em>Figure 2. Points generated automatically.</em></p>
<p>Does anyone have any idea how to do these things, if there is any recommended methodology or algorithms? I suppose that in this case, it is possible adjust a circle to those 3 points and generate some points, but there would still be more points that cannot be generated from a circle.</p>
<p>Anyone have any ideas or recommendations on how to do these things?</p>

---

## Post #2 by @lassoan (2021-12-21 17:30 UTC)

<p>To give some more context, this is a point pattern that the Stryker/Mako surgical navigation system generates to guide the surgeon in surface point collection (page 33 in this <a href="https://www.strykermeded.com/media/2223/mako-tka-surgical-guide.pdf">online pdf</a>):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c4c0ddb518c6dbd62ba01b06704396fcc9c220e.png" data-download-href="/uploads/short-url/8BpANcnjucFR5cAge7BE37C7EL4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c4c0ddb518c6dbd62ba01b06704396fcc9c220e_2_565x500.png" alt="image" data-base62-sha1="8BpANcnjucFR5cAge7BE37C7EL4" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c4c0ddb518c6dbd62ba01b06704396fcc9c220e_2_565x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c4c0ddb518c6dbd62ba01b06704396fcc9c220e_2_847x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c4c0ddb518c6dbd62ba01b06704396fcc9c220e_2_1130x1000.png 2x" data-dominant-color="E1E1E1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1536×1359 395 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is just a convenience feature to guide surgeons who are not familiar with capabilities and limitations of point based registration. It is not necessary for the registration.</p>
<p>You can of course implement a similar feature. For example you can designate areas of interest on a template that you approximately register to the patient anatomy and then do random uniform sampling in those areas.</p>
<p>Note that convenience features like this are often covered by patents, so before investing significant amount of time into developing this you may want to have a look at <a href="https://www.stryker.com/us/en/about/patents.html">Stryker’s patents</a>. There is a lot of prior art and many variations in how to do this registration, so patents rarely have any practical relevance, but it is still useful to be aware.</p>

---

## Post #3 by @lassoan (2021-12-21 17:31 UTC)

<p>The question was first posted on the VTK forum and some discussion is going on there, too:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/t/how-generate-a-set-of-interest-points-on-a-surface-from-some-points/7436/6">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/how-generate-a-set-of-interest-points-on-a-surface-from-some-points/7436/6" target="_blank" rel="noopener" title="05:32AM - 21 December 2021">VTK – 21 Dec 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:456/440;"><img src="https://discourse.vtk.org/uploads/default/original/2X/5/5796848de41d4f010f649aed150449492d01b721.png" class="thumbnail" width="456" height="440"></div>

<h3><a href="https://discourse.vtk.org/t/how-generate-a-set-of-interest-points-on-a-surface-from-some-points/7436/6" target="_blank" rel="noopener">How generate a set of interest points on a surface from some points.</a></h3>

  <p>Sorry, it is still not clear for me why a surgical navigation system would generate this point pattern. Is it for patient registration? Which navigation system is this? How the patient registration is done?</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @egomiguel (2021-12-22 01:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for your answer,  I just needed to know what is the methodology used to work with these problems and your answer has helped me. Thank you.</p>

---

## Post #5 by @lassoan (2021-12-22 03:37 UTC)

<p>To learn more about how exactly the Stryker/Mako software chooses the recommended sampling points, you may have a look at the patents that describe this method. They might have even published some papers about it.</p>

---

## Post #6 by @drvarunagarwal (2021-12-24 03:45 UTC)

<p>Is a preop patient CT is being used and loaded in the system before hand?</p>

---

## Post #7 by @egomiguel (2021-12-24 08:29 UTC)

<p><a class="mention" href="/u/drvarunagarwal">@drvarunagarwal</a>  yes, it is</p>

---

## Post #8 by @drvarunagarwal (2021-12-29 04:16 UTC)

<p>I suspect that placing the point is not as simple as placing those in a circle.<br>
The system maybe using some algorithms to segment the bone<br>
and using some AI model data to determine an place those points on the bone for registration.</p>

---
