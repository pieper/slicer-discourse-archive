# Distance between point and plane

**Topic ID**: 22091
**Date**: 2022-02-21
**URL**: https://discourse.slicer.org/t/distance-between-point-and-plane/22091

---

## Post #1 by @Annett (2022-02-21 17:15 UTC)

<p>how can i calculate the distance between a point and a plane?<br>
the segment that calculates the distance must be perpendicular to the plane and I’m not able to create it perpendicularly…<br>
Thanks!</p>

---

## Post #2 by @lassoan (2022-02-21 17:25 UTC)

<p>A very simple method is to transform the point in the plane’s coordinates system as it is shown in this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#project-a-line-to-a-plane">example in the script repository</a>. The distance from the plane is the third coordinate of the point in the plane coordinate system (<code>point_Plane[2]</code>).</p>

---

## Post #3 by @anasmh101 (2024-09-29 04:37 UTC)

<p>hi , could you please elaborate more on this , after copying the script and past it in the python console, how can I get the measurement? how can I define the point and the plane that I want to measure the distance between them ?</p>

---

## Post #4 by @lassoan (2024-09-29 11:47 UTC)

<aside class="quote no-group" data-username="anasmh101" data-post="3" data-topic="22091">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/anasmh101/48/80621_2.png" class="avatar"> anasmh101:</div>
<blockquote>
<p>how can I get the measuremen</p>
</blockquote>
</aside>
<pre data-code-wrap="python"><code class="lang-python">print(point_Plane[2])
</code></pre>
<aside class="quote no-group" data-username="anasmh101" data-post="3" data-topic="22091">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/anasmh101/48/80621_2.png" class="avatar"> anasmh101:</div>
<blockquote>
<p>how can I define the point and the plane</p>
</blockquote>
</aside>
<p>You can place a point and plane markup using Markups module. Let us know if you have difficulty figuring out how to do it.</p>

---

## Post #5 by @anasmh101 (2024-10-01 04:47 UTC)

<p>Thank you for your reply, but I still do not know how to apply this script on python console , so for example; in markups module, I establish a Plane named P and a Point named M . So the script on python console would be " print(point M _Plane[ P ]) " ? is this the way to deal with python script ?</p>

---

## Post #6 by @lassoan (2024-10-01 13:54 UTC)

<p>You can see that the point list in the example is called <code>P</code>, so you either need to rename your point list in to <code>P</code> or change the name in the code from <code>P</code> to the actual name of your point list.</p>
<p>I added a code snippet to the script repository that prints the points-to-plane distances  (<code>point_Plane[2]</code>) - see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-distances-of-points-from-a-plane">here</a>.</p>

---

## Post #7 by @anasmh101 (2024-10-02 13:00 UTC)

<p>Thank you so much , it works perfectly, appreciate your help.</p>
<p>May I ask , most of the time I make planes by defining points on specific anatomic land mark by " markups module" then use “Angle planes” module to construct the plane, is there a code snippet to do the same calculations as if the plane is constructed by " Markups Module "?</p>
<p>I tried the code snippet you added on planes constructed by " Angle planes" module, but it did not work</p>

---

## Post #8 by @lassoan (2024-10-02 13:16 UTC)

<p>You can place a plane on anatomical landmarks by fitting it to points. It is available in Markups module / Plane settings / Type → Plane fit.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee71cb48b8e7d1b0e026b03bc46b0e2817f40dcc.png" data-download-href="/uploads/short-url/y1nrjSwYI1CL8XpEEbn9PN1fyeE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee71cb48b8e7d1b0e026b03bc46b0e2817f40dcc_2_350x500.png" alt="image" data-base62-sha1="y1nrjSwYI1CL8XpEEbn9PN1fyeE" width="350" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee71cb48b8e7d1b0e026b03bc46b0e2817f40dcc_2_350x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee71cb48b8e7d1b0e026b03bc46b0e2817f40dcc_2_525x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee71cb48b8e7d1b0e026b03bc46b0e2817f40dcc_2_700x1000.png 2x" data-dominant-color="3A3D3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1081×1542 71.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @anasmh101 (2024-10-02 13:36 UTC)

<p>Thank you so much , it works very well</p>

---
