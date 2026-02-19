---
topic_id: 26645
title: "How To Calculate 3D Line Line Interesction"
date: 2022-12-08
url: https://discourse.slicer.org/t/26645
---

# How to calculate 3D line-line interesction?

**Topic ID**: 26645
**Date**: 2022-12-08
**URL**: https://discourse.slicer.org/t/how-to-calculate-3d-line-line-interesction/26645

---

## Post #1 by @nnzzll (2022-12-08 03:58 UTC)

<p>I got 2 infinite lines and each line was defined by two points.<br>
I’m trying to compute the intersection of the two lines with code below:</p>
<pre><code class="lang-auto">img1Line1P1 = [35.522341272816135, 244.0, -81.8808026069687]
img1Line1P2 = [36.1800944701046, 231.0, -81.31657002936069]
img2Line1P1 = [72.34037273903428, 244.0, -81.8925739257786]
img2Line1P2 = [70.43558942657907, 231.0, -81.32453925781688]

u = vtk.mutable(0)
v = vtk.mutable(0)

intersectType = vtk.vtkLine().Intersection(
img1Line1P1, img1Line1P2, img2Line1P1, img2Line1P2, u, v)
target11 = [img1Line1P1[i]+u*(img1Line1P2[i]-img1Line1P1[i]) for i in range(3)]
target12 = [img2Line1P1[i]+v*(img2Line1P2[i]-img2Line1P1[i]) for i in range(3)]
target1 = [(target11[i]+target12[i])/2 for i in range(3)]

print(intersectType)
print(u,v)
print(target11)
print(target12)
print(target1)

img1Line1P1 = [35.5223, 244, -81.8808]
img1Line1P2 = [36.4701, 231, -81.3736]
img2Line1P1 = [72.3401, 244, -81.8927]
img2Line1P2 = [70.4352, 231, -81.3244]

u = vtk.mutable(0)
v = vtk.mutable(0)

intersectType = vtk.vtkLine().Intersection(
img1Line1P1, img1Line1P2, img2Line1P1, img2Line1P2, u, v)
target11 = [img1Line1P1[i]+u*(img1Line1P2[i]-img1Line1P1[i]) for i in range(3)]
target12 = [img2Line1P1[i]+v*(img2Line1P2[i]-img2Line1P1[i]) for i in range(3)]
target1 = [(target11[i]+target12[i])/2 for i in range(3)]

print(intersectType)
print(u,v)
print(target11)
print(target12)
print(target1)
</code></pre>
<p>Output of code above goes like:</p>
<blockquote>
<p>0<br>
14.367889142863488 14.367746083471086<br>
[44.972866294820804, 57.217441142774646, -73.7739714811047]<br>
[44.97292976164488, 57.21930091487587, -73.73119604989571]<br>
[44.97289802823284, 57.21837102882526, -73.7525837655002]<br>
0<br>
12.902095599460948 12.899676454379204<br>
[47.7509062091691, 76.27275720700769, -75.33685711195344]<br>
[47.76750632205291, 76.30420609307035, -74.56181387097621]<br>
[47.759206265611006, 76.28848165003902, -74.94933549146482]</p>
</blockquote>
<p>As you can see, even with a tiny difference of the points coordinates, the intersection calculated was totally different, especially with the Y-axis.</p>
<p>I was wondering if my code is the correct way to calculate the intersection of two 3D lines? If not, is there a better way to calculate 3D line-line intersection?</p>

---

## Post #2 by @lassoan (2022-12-08 17:58 UTC)

<p>I used this function for intersection of finite line segments and it worked perfectly:</p>
<p><a href="http://paulbourke.net/geometry/pointlineplane/L3D.py" class="onebox" target="_blank" rel="noopener">http://paulbourke.net/geometry/pointlineplane/L3D.py</a></p>

---

## Post #3 by @lassoan (2022-12-08 18:02 UTC)

<p>The question was also asked on the VTK forum:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/t/how-to-calculate-line-line-intersection/10108/4">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/how-to-calculate-line-line-intersection/10108/4" target="_blank" rel="noopener" title="05:58PM - 08 December 2022">VTK – 8 Dec 22</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<h3><a href="https://discourse.vtk.org/t/how-to-calculate-line-line-intersection/10108/4" target="_blank" rel="noopener">How to calculate line line intersection</a></h3>

  <p>The question was also asked and answered on the Slicer forum:</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/nnzzll">@nnzzll</a> please avoid cross-posting to prevent multiple people spending time with answering your question at the same time. Instead, post to the most relevant forum and give some time for people to respond.</p>
<p>If you post to multiple forums, e.g., because you are in some exceptional circumstance, like a very close deadline, then you must disclose every other location where you posted the question elsewhere so that people can check if the question was answered already, before taking the time to answer. Discourse warns me when I’m starting to answer a question and somebody else is already working on an answer within the same forum, so unnecessary duplicate efforts are minimized; but manual checking is needed if the question is asked at the same time on different forums.</p>

---

## Post #4 by @esomjai (2023-03-25 12:15 UTC)

<p>Can you please advise on how to load this into slicer and what to modify if I would use the 4 control points of the two intersecting line in the codes? Thank you in advance.</p>

---

## Post #5 by @jumbojing (2023-03-25 13:56 UTC)

<pre><code class="lang-auto">    def lines2P(p0, p01, p1, p11):
        '''lines2P 2线交点

        '''
        drt00 = np.array([p01[0]])
        drt01 = np.array([p01[1]])
        drt02 = np.array([p01[2]])
        drt10 = np.array([p11[0]])
        drt11 = np.array([p11[1]])
        p0x = np.array([p0[0]])
        p0y = np.array([p0[1]])
        p0z = np.array([p0[2]])
        p1x = np.array([p1[0]])
        p1y = np.array([p1[1]])
        t = (drt10 * (p1y - p0y) + drt11 * (p0x - p1x)) / ((drt10 * drt01) - (drt00 * drt11))
        x = p0x + drt00 * t
        y = p0y + drt01 * t
        z = p0z + drt02 * t
        return np.array([x[0], y[0], z[0]])
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20">我写了一个函数, 可以试一试啊</p>

---
