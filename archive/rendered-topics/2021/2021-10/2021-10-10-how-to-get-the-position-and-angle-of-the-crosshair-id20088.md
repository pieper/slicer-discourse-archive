---
topic_id: 20088
title: "How To Get The Position And Angle Of The Crosshair"
date: 2021-10-10
url: https://discourse.slicer.org/t/20088
---

# How to get the position and angle of the crosshair?

**Topic ID**: 20088
**Date**: 2021-10-10
**URL**: https://discourse.slicer.org/t/how-to-get-the-position-and-angle-of-the-crosshair/20088

---

## Post #1 by @jumbojing (2021-10-10 09:26 UTC)

<p>How to get the position and angle of the crosshair?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11c7526ceec6539b5e65e642ee09b84cad00b961.jpeg" data-download-href="/uploads/short-url/2xha46FjlffdWXkHiwrL0UVH2eZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11c7526ceec6539b5e65e642ee09b84cad00b961_2_611x500.jpeg" alt="image" data-base62-sha1="2xha46FjlffdWXkHiwrL0UVH2eZ" width="611" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11c7526ceec6539b5e65e642ee09b84cad00b961_2_611x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11c7526ceec6539b5e65e642ee09b84cad00b961_2_916x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/11c7526ceec6539b5e65e642ee09b84cad00b961_2_1222x1000.jpeg 2x" data-dominant-color="60616B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1558×1274 79.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I try to <code>crosshair = slicer.util.getNode('Crosshair') </code><br>
and <code>print(crosshair)</code>,get those :</p>
<pre><code class="lang-auto">vtkMRMLCrosshairNode (0x7fea623dbca0)
  ID: vtkMRMLCrosshairNodedefault
  ClassName: vtkMRMLCrosshairNode
  Name: Crosshair
  Debug: false
  MTime: 17590155
  Description: (none)
  SingletonTag: default
  HideFromEditors: true
  Selectable: true
  Selected: false
  UndoEnabled: false
  CrosshairMode: NoCrosshair
  CrosshairBehavior: CenteredJumpSlice
  CrosshairThickness: Thick
  CrosshairRAS: [-3.89054, -24.6428, 202.575]
  FastPick3D: false
</code></pre>
<p>There is no information about angle…</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @jumbojing (2021-10-10 10:40 UTC)

<p>这个似乎不是crosshair的问题…应该是返回"the orthogonal nodes around the common <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveView/ValveView.py" rel="noopener nofollow ugc">intersection point</a>"的位置和角度问题…<br>
我用<code> sliceToRAS = slicer.mrmlScene.GetNodeByID(sliceNodeId).GetSliceToRAS()</code>得到了4x4martix, 怎么能够利用该变量, Set the slice to ras呢?</p>
<blockquote>
<p>This does not seem to be a <strong>crosshair</strong> problem… It should be a problem of the position and angle of returning “<strong>the orthogonal nodes around the common intersection point</strong>”… I used sliceToRAS = slicer.mrmlScene.GetNodeByID(sliceNodeId).GetSliceToRAS() to get 4x4martix, how can I use this  Variables, howto Set the slice to ras?</p>
</blockquote>

---

## Post #3 by @lassoan (2021-10-10 12:06 UTC)

<p>The crosshair only stores position and the current core node ID. If you current view is a slice node then you can get the orientation of that slice from the SliceToRAS matrix.</p>
<p>What are you trying to achieve?</p>

---

## Post #4 by @jumbojing (2021-10-10 12:27 UTC)

<p>I tried to get the slicenormal form <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveView/ValveView.py" rel="noopener nofollow ugc">def getPlaneIntersectionPoint</a>, and then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-a-normal-vector-and-position" rel="noopener nofollow ugc"> Set slice position and orientation from a normal vector and position</a>.<br>
but I haven’t got the slicenormal yet…do you help me?</p>

---

## Post #5 by @lassoan (2021-10-10 12:48 UTC)

<p>Slice normal is the third column of the SliceToRAS matrix.</p>

---

## Post #6 by @jumbojing (2021-10-10 20:48 UTC)

<p>yes, I’ve got sliceposition and slicenormal from the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveView/ValveView.py" rel="noopener nofollow ugc">def getPlaneIntersectionPoint</a> through <code>return x,n1,n2,n3</code>,  and then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-a-normal-vector-and-position" rel="noopener nofollow ugc"> Set slice position and orientation from a normal vector and position</a>.</p>
<p>谢谢老师</p>

---
