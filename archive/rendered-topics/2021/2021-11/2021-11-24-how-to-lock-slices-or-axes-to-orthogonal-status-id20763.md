---
topic_id: 20763
title: "How To Lock Slices Or Axes To Orthogonal Status"
date: 2021-11-24
url: https://discourse.slicer.org/t/20763
---

# How to lock slices or axes to orthogonal status?

**Topic ID**: 20763
**Date**: 2021-11-24
**URL**: https://discourse.slicer.org/t/how-to-lock-slices-or-axes-to-orthogonal-status/20763

---

## Post #1 by @jumbojing (2021-11-24 04:16 UTC)

<p>How to lock slices or axes to  orthogonal status(be perpendicular to each other)?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @lassoan (2021-11-26 00:12 UTC)

<p>By when you rotate slices using Ctrl + Alt + Left-click-and-drag, relative angle between slices planes are preserved. You can use this for quick interactive image reslicing with orthogonal planes.</p>
<p>You can also use Valve View module (in SlicerHeart extension). It is useful for rotation around a fixed center point.</p>
<p>You can also use a transform to reslice an image with orthogonal slices, using Volume Reslice Driver module (in SlicerIGT extension). It can be used in combination with Endoscopy module to reslice along a curved trajectory.</p>
<p>There are many more ways. If you describe what you want to do then we can give more specific advice.</p>

---

## Post #3 by @jumbojing (2021-11-26 03:07 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>我在程序里用了这个<a href="https://github.com/SlicerHeart/SlicerHeart/blob/ae7d4af1c5c0e61ebd988a2d8c6d6905ad126514/ValveView/ValveView.py#L213-L273" rel="noopener nofollow ugc">代码</a>, 好像是因为这个原因,RedSlice发生了偏斜,救助好几天…没人回答,我找到了<a href="https://github.com/chir-set/FlipViewPoint/blob/53e0777d8d495ec395adf68ad4867c01c836830e/FlipViewPoint/FlipViewPoint.py#L189-L196" rel="noopener nofollow ugc">restoreViews</a>来控制似乎管用</p>
<p>谢谢老师</p>
<blockquote>
<p>I used the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/ae7d4af1c5c0e61ebd988a2d8c6d6905ad126514/ValveView/ValveView.py#L213-L273" rel="noopener nofollow ugc">getPlaneIntersectionPoint</a>,  in the program. It seems that for this reason, redSlice deflected and saved for several days… No one answered. I found <a href="https://github.com/chir-set/FlipViewPoint/blob/53e0777d8d495ec395adf68ad4867c01c836830e/FlipViewPoint/FlipViewPoint.py#L189-L196" rel="noopener nofollow ugc">restoreViews</a> to control it. It seems to work.</p>
</blockquote>

---
