---
topic_id: 17344
title: "Help Me Update Plane From Fiducial Points How Can I Aligne T"
date: 2021-04-27
url: https://discourse.slicer.org/t/17344
---

# Help me! Update plane from fiducial points...How can I aligne the red plane with Coordinate axis?

**Topic ID**: 17344
**Date**: 2021-04-27
**URL**: https://discourse.slicer.org/t/help-me-update-plane-from-fiducial-points-how-can-i-aligne-the-red-plane-with-coordinate-axis/17344

---

## Post #1 by @jumbojing (2021-04-27 05:46 UTC)

<pre><code class="lang-python"># Update plane from fiducial points
def UpdateSlicePlane(data):
  a = data
  points = np.array([list(zip(*a))])[0]
#     b2 = np.array([list(zip(*a))])
  sliceNode = slicer.app.layoutManager().sliceWidget("Red").mrmlSliceNode()
  planePosition = points.mean(axis=1)
  planeNormal = np.cross(points[:,1] - points[:,0], points[:,2] - points[:,0])
  planeX = points[:,1] - points[:,0]
  sliceNode.SetSliceToRASByNTP(planeNormal[0], planeNormal[1], planeNormal[2],
    planeX[0], planeX[1], planeX[2],
    planePosition[0], planePosition[1], planePosition[2], 0)

UpdateSlicePlane(data33)
slicernb.ViewDisplay('OneUpRedSlice', center=False)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://user-images.githubusercontent.com/10215735/116176690-26c5a080-a745-11eb-8c75-e25a6f955804.png" title="下载" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/10215735/116176690-26c5a080-a745-11eb-8c75-e25a6f955804.png" alt="下载" width="690" height="436"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use xlink:href="#far-image"></use></svg><span class="filename">下载</span><span class="informations">2006×1268</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use xlink:href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>我想将图片对齐,就像这样:</p>
<p>I  want aligne the red plane with Coordinate axis?, like that:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://user-images.githubusercontent.com/10215735/116177287-1eba3080-a746-11eb-960b-a55bbfcaf8a6.png" title="image" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/10215735/116177287-1eba3080-a746-11eb-960b-a55bbfcaf8a6.png" alt="image" width="690" height="486"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use xlink:href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1042×734</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use xlink:href="#discourse-expand"></use></svg>
</div></a></div></p>

---
