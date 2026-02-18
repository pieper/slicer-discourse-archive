# SetSliceToRASByNTP

**Topic ID**: 17578
**Date**: 2021-05-11
**URL**: https://discourse.slicer.org/t/setslicetorasbyntp/17578

---

## Post #1 by @jumbojing (2021-05-11 23:55 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/markups.html?highlight=position%20fiducial#set-slice-position-and-orientation-from-3-markup-fiducials" rel="noopener nofollow ugc">Set slice position and orientation from 3 markup fiducials</a><br>
这段代码通过3个fiducials,来定位旋转red_slicer,怎样用同样的方法来定位和旋转yellow_slicer呢?就像这样…</p>
<p>This code uses 3 fiducials to position and orientation the red slice view, how to position and rotate the yellow_slicer in the same way? Just like this…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18b6c90e07ff7c290072efedda01cd03287abf0e.jpeg" data-download-href="/uploads/short-url/3wD4EQ7k9juvc5PMKvWN3YlsIBU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18b6c90e07ff7c290072efedda01cd03287abf0e_2_690x431.jpeg" alt="image" data-base62-sha1="3wD4EQ7k9juvc5PMKvWN3YlsIBU" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18b6c90e07ff7c290072efedda01cd03287abf0e_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18b6c90e07ff7c290072efedda01cd03287abf0e_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18b6c90e07ff7c290072efedda01cd03287abf0e_2_1380x862.jpeg 2x" data-dominant-color="868180"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1416×886 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jumbojing (2021-05-12 03:43 UTC)

<p>我的微信号(My WeChat ID):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49a4dcdf58ad5a829ece0c2402c11a283ea248b7.jpeg" data-download-href="/uploads/short-url/avu4tDywfpybiR27HUEKvoZ1Tq7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49a4dcdf58ad5a829ece0c2402c11a283ea248b7.jpeg" alt="image" data-base62-sha1="avu4tDywfpybiR27HUEKvoZ1Tq7" width="500" height="500" data-dominant-color="B78365"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">512×512 63.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a href="mailto:gelamb@sina.com">gelamb@sina.com</a></p>

---

## Post #3 by @lassoan (2021-05-13 05:44 UTC)

<p>You can rotate views by Ctrl-Alt-Left-click-and-drag or two-finger pinch on a Windows touchscreen or macOS touchpad (after enabling slice intersections).</p>
<p>There are many modules for exploring tool trajectories and rotating views.</p>
<p>For example, you can use Path Explorer module (in SlicerIGT extension) - specify entry and target point, create a trajectory, select it, and if you select an In Plane view, you can rotate it along the trajectory using the slider.</p>
<p>For just simple rotating of views, you can use or copy-paste code from Valve View module in SlicerHeart extension.</p>

---

## Post #4 by @jumbojing (2021-05-13 12:16 UTC)

<p>我整明白了…三点决定一个平面,所以,要从两个视角来观察一条直线的关键是第3个点的选择!<br>
下面是解决方案:</p>
<blockquote>
<p>I fully understand…Three points determine a plane, so the key to observing a straight line from two perspectives is the third point!<br>
Here is the solution:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/accd83e3660dfaaae14231902d959e996e9dfe7f.jpeg" data-download-href="/uploads/short-url/oEGrecqy0qfafB5rVPadazQzfXN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/accd83e3660dfaaae14231902d959e996e9dfe7f_2_451x500.jpeg" alt="image" data-base62-sha1="oEGrecqy0qfafB5rVPadazQzfXN" width="451" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/accd83e3660dfaaae14231902d959e996e9dfe7f_2_451x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/accd83e3660dfaaae14231902d959e996e9dfe7f_2_676x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/accd83e3660dfaaae14231902d959e996e9dfe7f_2_902x1000.jpeg 2x" data-dominant-color="8E8D8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1296×1436 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>

---

## Post #5 by @jumbojing (2021-05-13 12:35 UTC)

<p>只是得到的视角或slice view无法和坐标轴对齐…有点小遗憾…</p>
<blockquote>
<p>It’s just that the obtained perspective or slice view cannot be aligned with the coordinate axis…it’s a little regrettable…</p>
</blockquote>

---

## Post #6 by @lassoan (2021-05-13 13:07 UTC)

<p>You can specify what is “up” in the slice view by the transverse vector (<code>planeX</code> in the code snippet above). See in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-a-normal-vector-and-position">this example</a> how to make the “up” direction snap to meaningful anatomical axis directions.</p>

---
