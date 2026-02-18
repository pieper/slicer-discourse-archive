# The Slice Focus Fun seems still perfect

**Topic ID**: 19909
**Date**: 2021-09-29
**URL**: https://discourse.slicer.org/t/the-slice-focus-fun-seems-still-perfect/19909

---

## Post #1 by @jumbojing (2021-09-29 10:16 UTC)

<pre><code class="lang-auto">
# ### P4SliceFocus
# - [[P4SliceFocus]]
# - From: [Set slice position and orientation from 3 markup fiducials](https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-3-markup-fiducials)
# - [TODO]: 2点聚焦, slice对正, 某个slice放大, 简化代码用循环

  def P4SliceFocus(self, oP, xP, yP, zP):
      '''
      Param:oP:原点
            xP:X轴上的一点
            yP:Y轴上的一点
            zP:Z轴上的一点
      return:在3个slic上聚焦
      
      '''
      oP = oP + [.01, .01, .01]
      yP = yP + [0, .01, 0]
      xP = xP + [.01, 0, 0]
      zP = zP + [0, 0, .01]
      sliceNode = slicer.app.layoutManager().sliceWidget("Red").mrmlSliceNode()
      points = np.array([list(zip(*np.array([oP,xP,yP])))])[0]
      planePosition = points.mean(axis=1)
      planeNormal = np.cross(points[:,1] - points[:,0], points[:,2] - points[:,0])
      planeX = points[:,1] - points[:,0]
      sliceNode.SetSliceToRASByNTP(planeNormal[0], planeNormal[1], planeNormal[2], planeX[0], planeX[1], planeX[2], planePosition[0], planePosition[1], planePosition[2], 0)

      sliceNode = slicer.app.layoutManager().sliceWidget("Yellow").mrmlSliceNode()
      points = np.array([list(zip(*np.array([yP,zP,oP])))])[0]
      planePosition = points.mean(axis=1)
      planeNormal = np.cross(points[:,1] - points[:,0], points[:,2] - points[:,0])
      planeX = points[:,1] - points[:,0]
      sliceNode.SetSliceToRASByNTP(planeNormal[0], planeNormal[1], planeNormal[2], planeX[0], planeX[1], planeX[2], planePosition[0], planePosition[1], planePosition[2], 0)

      sliceNode = slicer.app.layoutManager().sliceWidget("Green").mrmlSliceNode()
      points = np.array([list(zip(*np.array([oP,xP,zP])))])[0]
      planePosition = points.mean(axis=1)
      planeNormal = np.cross(points[:,1] - points[:,0], points[:,2] - points[:,0])
      planeX = points[:,1] - points[:,0]
      sliceNode.SetSliceToRASByNTP(planeNormal[0], planeNormal[1], planeNormal[2], planeX[0], planeX[1], planeX[2], planePosition[0], planePosition[1], planePosition[2], 0)

    
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8efe5105fdc937a8af216bee7c3477970fea9641.jpeg" data-download-href="/uploads/short-url/koYFCOlvvttZdLeZbDS5AcD7LhL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8efe5105fdc937a8af216bee7c3477970fea9641_2_565x500.jpeg" alt="image" data-base62-sha1="koYFCOlvvttZdLeZbDS5AcD7LhL" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8efe5105fdc937a8af216bee7c3477970fea9641_2_565x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8efe5105fdc937a8af216bee7c3477970fea9641_2_847x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8efe5105fdc937a8af216bee7c3477970fea9641_2_1130x1000.jpeg 2x" data-dominant-color="43424D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1770×1566 97.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>根据这段代码, 我做了上面这段代码, 我的目的是在3个slice里聚焦一个model…这段代码不够完美:</p>
<ul>
<li>
<p>有2个点就可以完成聚焦任务了</p>
</li>
<li>
<p>如何对齐各个slice</p>
</li>
<li>
<p>如何放大某个slice</p>
</li>
</ul>
<p>According to  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-3-markup-fiducials" rel="noopener nofollow ugc">Set slice position and orientation from 3 markup fiducials</a>,  I wrote the above code, my purpose is to focus on a model in 3 slices… This code is not perfect:</p>
<ul>
<li>2 points to complete the focus task</li>
<li>How to align each slice</li>
<li>How to enlarge a slice</li>
</ul>

---

## Post #2 by @jumbojing (2021-09-29 10:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <span class="mention">@pieperThanks</span> <a class="mention" href="/u/chir.set">@chir.set</a></p>

---
