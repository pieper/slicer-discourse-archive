# How to replace markups with np.array in application MarkupsToModel

**Topic ID**: 25000
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/how-to-replace-markups-with-np-array-in-application-markupstomodel/25000

---

## Post #1 by @jumbojing (2022-08-30 13:20 UTC)

<p>I want to convert a set of point clouds (np.array) to closed surfaces, How to use <code>np.array</code> directly in <code>MarkupsToModel</code> instead of converting <code>np.array</code> to <code>Markups</code>?</p>

---

## Post #2 by @lassoan (2022-08-30 18:49 UTC)

<p>You need to convert the numpy array to a MRML model node to use it in Slicer modules. Bulk data (point coordinates) does not have to be copied, so the conversion should take negligible time.</p>

---

## Post #3 by @jumbojing (2022-08-30 22:25 UTC)

<p>Thanks!!!<span class="mention">@lassosan</span><br>
I see <img src="https://emoji.discourse-cdn.com/twitter/innocent.png?v=12" title=":innocent:" class="emoji" alt=":innocent:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25000">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>convert the numpy array to a MRML model node</p>
</blockquote>
</aside>
<p>但是, 我想要这个👇面积, 可是转化为model后得到的表面积似乎有点大, 转化为curve后得到的面积似乎又太小了…</p>
<blockquote>
<p>However, I want <img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20"> this area, but the surface area obtained after converting to model seems to be too large, and the area obtained after converting to curve seems to be too small…what’s wrong?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85df068ce23de1afd235e5016e1e5266f7229194.png" data-download-href="/uploads/short-url/j6hkGGRnVMZpTC7qGTcs2fT2nhq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85df068ce23de1afd235e5016e1e5266f7229194_2_690x151.png" alt="image" data-base62-sha1="j6hkGGRnVMZpTC7qGTcs2fT2nhq" width="690" height="151" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85df068ce23de1afd235e5016e1e5266f7229194_2_690x151.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85df068ce23de1afd235e5016e1e5266f7229194_2_1035x226.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85df068ce23de1afd235e5016e1e5266f7229194_2_1380x302.png 2x" data-dominant-color="DADFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1458×320 56.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e10d4f133a3a5b2e7f6761d408036e1aacdd6c7d.png" data-download-href="/uploads/short-url/w6TWACoAfg0uMX0Rv1LOXTyRuYB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e10d4f133a3a5b2e7f6761d408036e1aacdd6c7d_2_690x196.png" alt="image" data-base62-sha1="w6TWACoAfg0uMX0Rv1LOXTyRuYB" width="690" height="196" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e10d4f133a3a5b2e7f6761d408036e1aacdd6c7d_2_690x196.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e10d4f133a3a5b2e7f6761d408036e1aacdd6c7d_2_1035x294.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e10d4f133a3a5b2e7f6761d408036e1aacdd6c7d_2_1380x392.png 2x" data-dominant-color="D2D1E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1790×510 59.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-08-31 00:47 UTC)

<p>What is your end goal?<br>
What the point cloud represents (points on a curve, points on surface, points in a 3D region,…)?<br>
Do you need to interact with the points or just create a model?</p>

---

## Post #5 by @jumbojing (2022-08-31 00:53 UTC)

<p>I want to get the area of ​​contours formed by a set of point clouds (np.array) that lie in a plane.<br>
<img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji only-emoji" alt=":point_down:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40f103cd20b45f8f8df4f8328a522c5895fc34e3.png" data-download-href="/uploads/short-url/9guVF4JYCylPqaLkEnKn5J1FZJx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40f103cd20b45f8f8df4f8328a522c5895fc34e3_2_690x464.png" alt="image" data-base62-sha1="9guVF4JYCylPqaLkEnKn5J1FZJx" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40f103cd20b45f8f8df4f8328a522c5895fc34e3_2_690x464.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40f103cd20b45f8f8df4f8328a522c5895fc34e3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40f103cd20b45f8f8df4f8328a522c5895fc34e3.png 2x" data-dominant-color="9096BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">862×580 52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2022-08-31 02:48 UTC)

<p>Do you want to fit a plane to these points? You can do that directly using a markup plane, as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#fit-markups-plane-to-model">here</a>. Note that points are imported into a model node instead of a markup point list node.</p>

---

## Post #7 by @jumbojing (2022-08-31 03:12 UTC)

<p>No…I want the surface Area of ​​contours formed by a set of point clouds (np.array) …</p>

---

## Post #8 by @lassoan (2022-08-31 03:20 UTC)

<p>If you want to compute soap bubble surface from ordered points along a closed curve then you can do that by importing the points into a markup closed curve node and enabling the “area” measurement. If you want to see the generated surface then I would recommend to use the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/BafflePlanner.md">Baffle Planner module in SlicerHeart extension</a> and then get the surface area of the generated model from the Models module.</p>

---

## Post #9 by @jumbojing (2022-08-31 23:52 UTC)

<p>I tried to compute the [quote=“lassoan, post:8, topic:25000”]<br>
surface from ordered points along a closed curve then you can do that by importing the points into a markup closed curve node<br>
[/quote], but found that its efficiency is too low, especially when using <code>slicer.util.updateMarkupsControlPointsFromArray</code>, is there a better and faster method to get a curve from np.array?</p>

---

## Post #10 by @lassoan (2022-09-03 02:05 UTC)

<p>I’ve fixed the performance issue in the latest Slicer Preview Release (that you download 2022-09-03 or later). Now <code>slicer.util.updateMarkupsControlPointsFromArray</code> should complete immediately.</p>

---

## Post #11 by @jumbojing (2022-09-03 02:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="25000">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>in the latest Slicer Preview Release (that you download 2022-09-03 or later)</p>
</blockquote>
</aside>
<p>Can I only replace the util.py file in the my current version (5.1.0-2022-05-08) Slicer with <a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py" rel="noopener nofollow ugc">util.py</a>  without updating the Slicer?</p>

---

## Post #12 by @lassoan (2022-09-03 03:21 UTC)

<p>As I remember I’ve made some more improvements since Slicer-5.0.3 in C++ code, so updating util.py is probably not sufficient. Another complication may be that util.py of Slicer-5.1 may not be compatible with Slicer-5.0. I would recommend to download the Slicer Preview Release tomorrow and use that.</p>

---
