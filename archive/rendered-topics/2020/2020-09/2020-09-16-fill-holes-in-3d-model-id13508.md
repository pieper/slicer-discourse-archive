# Fill holes in 3D model

**Topic ID**: 13508
**Date**: 2020-09-16
**URL**: https://discourse.slicer.org/t/fill-holes-in-3d-model/13508

---

## Post #1 by @ru6928 (2020-09-16 18:52 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e53a0d3c9865c759fc126d6d9d480c6a9fb970a.png" alt="Screen Shot 2020-09-16 at 11.44.10 AM" data-base62-sha1="8TmM6htq3kcCKql2q67ASRPUfz4" width="444" height="330"></p>
<p>Hi all,</p>
<p>I would like to fill the holes in the 3D model using some sort of interpolation. How do I do it in 3DSlicer?</p>
<p>These are segmentations obtained from a deep learning algorithm for cardiac MR images. The myocardium should be continuous, devoid of these holes.</p>
<p>Thank you,<br>
Anshro</p>

---

## Post #2 by @lassoan (2020-09-16 20:07 UTC)

<p>Convex hull may fix the outer surface. You can get it by copy-pasting this code snippet to the Python console (replace <code>mySurface</code> with your model node’s name):</p>
<pre><code class="lang-python">modelNode = getNode('mySurface')

convexHull = vtk.vtkDelaunay3D()
convexHull.SetInputData(modelNode.GetPolyData())
outerSurface = vtk.vtkGeometryFilter()
outerSurface.SetInputConnection(convexHull.GetOutputPort())
outerSurface.Update()
modelNode.SetAndObservePolyData(outerSurface.GetOutput())
</code></pre>
<p>You may then use Segment Editor, Logical operators, maybe <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">Wrap Solidify effect</a> to figure out a workflow for reconstructing the inner surface.</p>

---

## Post #3 by @ru6928 (2020-09-16 22:36 UTC)

<p>Hi Andras,</p>
<p>Thank you very much for the quick reply. I tried the method you suggested. The result is - <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10ec068de32fa7e091e0e1cd535d34ed21a7854c.png" alt="Screen Shot 2020-09-16 at 6.30.22 PM" data-base62-sha1="2pHjXX9IDKJ3ElOyGBtOpiXi3BG" width="287" height="274"></p>
<p>I want only the small holes to be filled and the myocardium should be hollow. Not a solid as shown above. Is there anything we can do about that. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0abb6d327bee2e45c77ac750de84734a7e56cbf.png" alt="Screen Shot 2020-09-16 at 6.30.58 PM" data-base62-sha1="yl4uiWbrY2QEabChWxGXeU8Sebd" width="231" height="162"></p>
<p>Thanks again,<br>
Anshro</p>

---

## Post #4 by @lassoan (2020-09-17 02:56 UTC)

<p>Convex hull was just suggested as an initial step.</p>
<p>There are lots of tools in Segment Editor. If the holes are small then you can fill them using Smoothing effect - “Closing (fill holes)” method. You can also go full manual and fill the holes using Paint or Draw effects.</p>

---

## Post #5 by @Hamid (2021-04-15 16:49 UTC)

<p>Is it possible to select a specific hole to fill while using Smoothing? Because there are some other inlets and outlets open in my model that I do not want to fill them.</p>

---

## Post #6 by @lassoan (2021-04-15 21:17 UTC)

<p>Instead of applying global smoothing, you can use the smoothing brush:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="rjNcvefBaNU" data-video-title="Segmentation smoothing brush - new segmentation tool in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=rjNcvefBaNU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/rjNcvefBaNU/maxresdefault.jpg" title="Segmentation smoothing brush - new segmentation tool in 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #7 by @Hamid (2021-04-27 20:40 UTC)

<p>Lassoan thanks for introducing very efficient way. I’m usimg slicer 4.11.20200930 and the “smoothing brush option” dose not show up!! what should I do to have it?any extension or…?</p>

---

## Post #8 by @lassoan (2021-04-27 22:23 UTC)

<p>You need to use a more recent Slicer version.</p>

---

## Post #9 by @slicer365 (2021-04-28 00:28 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="4" data-topic="13508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>用“绘画”或“绘制”效果填充孔。</p>
</blockquote>
</aside>
<p>The slicer tool is very flexible. You can use different functions to achieve this effect by thinking about it. There are many tools in the segmentation.</p>

---

## Post #10 by @Hamid (2021-04-29 12:32 UTC)

<p>I Installed a recent version and now I have access to brush option. when I choose smoothing and then brush option,Median smoothing method and finally kernel size of 5mm, the effect make hole instead of filling hole!!! In the video you sent it works correct and fills the holes. what is wrong with me?</p>

---

## Post #11 by @Hamid (2021-04-29 16:13 UTC)

<p>i am working on Linux system. Maybe this is a bug for the linux system. please consider it.</p>

---

## Post #12 by @lassoan (2021-04-30 02:29 UTC)

<p>Median means that each voxel is replaced by the median value of its neighborhood. Therefore, it can add or remove points - whatever makes the region smoother. If you want to fill holes, choose the fill holes option.</p>

---
