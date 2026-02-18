# Radius of Centreline Curve

**Topic ID**: 19103
**Date**: 2021-08-06
**URL**: https://discourse.slicer.org/t/radius-of-centreline-curve/19103

---

## Post #1 by @AshvinGupta (2021-08-06 12:46 UTC)

<p>Hello, I am trying to find the radius of vessels using the extract centreline module. From reading previous posts on 3D slicer, I am able to find the radius of vessels if I create a centreline model using the following code:</p>
<blockquote>
<blockquote>
<blockquote>
<p>c = getNode(‘Centerline model’)<br>
points = slicer.util.arrayFromModelPoints(c)<br>
radii = slicer.util.arrayFromModelPointData(c, ‘Radius’)<br>
for i, radius in enumerate(radii):<br>
print(“{0},{1}”.format(points[i],radius))</p>
</blockquote>
</blockquote>
</blockquote>
<p>However, is there any way to do the same but for centreline curves? I see there’s the slicer.util.arrayFromMarkupsCurvePoints() function but no function to find the data from the curve if I’m correct?<br>
My second question is how reliable are these radius values? Maximum accuracy is vital to my project and I was trying to verify if these are the correct radii but to no avail.</p>

---

## Post #2 by @chir.set (2021-08-06 15:57 UTC)

<aside class="quote no-group" data-username="AshvinGupta" data-post="1" data-topic="19103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/4af34b/48.png" class="avatar"> AshvinGupta:</div>
<blockquote>
<p>My second question is how reliable are these radius values?</p>
</blockquote>
</aside>
<p>As I understood, it’s the radius of the maximum sphere that can fit at a point of the centerline. It’s an algorithmic proposal of what can be calculated at this point.</p>
<p>The picture below shows a common situation : a cross-section of a pathological artery.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3247764b5e1527d451983427d8ab0df9448efcc0.png" alt="radius" data-base62-sha1="7aMYMqc2IPY5kSFbbTvh2XWQpnG" width="554" height="398"></p>
<p>The radius reported by the extract centerline module is that of the grey circle.<br>
You may also be tempted to imagine the patent lumen’s diameter according to the white lines. Then you’ll need to measure by hand, or devise an algorithm to measure as per your project’s requirements.</p>

---
