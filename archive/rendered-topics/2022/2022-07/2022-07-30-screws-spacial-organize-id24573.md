---
topic_id: 24573
title: "Screws Spacial Organize"
date: 2022-07-30
url: https://discourse.slicer.org/t/24573
---

# Screws spacial organize

**Topic ID**: 24573
**Date**: 2022-07-30
**URL**: https://discourse.slicer.org/t/screws-spacial-organize/24573

---

## Post #1 by @apparrilla (2022-07-30 08:39 UTC)

<p>Hi everyone,<br>
I´ve segmented the screws of an intraoperative CBCT of one of my spinal surgeries.<br>
This is the result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e4b8d8bd927e62bd6ad5271dac19b1e598d3d64.png" data-download-href="/uploads/short-url/mAljkc40SI5NbpSd0rEY8w5Wi2w.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e4b8d8bd927e62bd6ad5271dac19b1e598d3d64_2_223x500.png" alt="image" data-base62-sha1="mAljkc40SI5NbpSd0rEY8w5Wi2w" width="223" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e4b8d8bd927e62bd6ad5271dac19b1e598d3d64_2_223x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e4b8d8bd927e62bd6ad5271dac19b1e598d3d64.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e4b8d8bd927e62bd6ad5271dac19b1e598d3d64.png 2x" data-dominant-color="8D8DAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">235×525 67.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I´ve used Segment Statistics to get each segment center and I want to iterate all of them.</p>
<p>My problem is that they are messed up in space. Is there any way to organize them in colums and rows to iterate them in logical order from upper left to botton right?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2022-07-30 14:23 UTC)

<p>Maybe you can give them names related to the level in the spine and then sort them in the resulting statistics table.</p>

---

## Post #3 by @apparrilla (2022-07-30 15:16 UTC)

<p>Hi Steve,<br>
This is the main problem. I get all screws in a single segment and then I split it with Islands tool. They have no order at all and I want to rename them in an automated way by position in the space.<br>
Thanks for your help!</p>

---

## Post #4 by @pieper (2022-07-30 15:39 UTC)

<p>Glad to help, but unfortunately I don’t think there’s any existing/reliable way to do this automatically.  It would be possible to come up with a heuristic that would usually give you a reasonable answer but may not be correct if there is a lot of variability in the input.  In the Segment Statistics advanced options you can enable calculation of centroids (in patient RAS space).  You could break those into R, A, and S and probably sorting by R and S would be what you want.</p>

---

## Post #5 by @lassoan (2022-07-31 08:37 UTC)

<p><a class="mention" href="/u/apparrilla">@apparrilla</a> what is your end goal? Would you like to simulate insertion (choose a screw and position/orient in a CT image)?</p>

---

## Post #6 by @apparrilla (2022-07-31 23:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , This is just what I want to do.</p>
<p>I have some peace of code that is working for me. Maybe usefull for anyone else:</p>
<pre><code class="lang-auto">def orderScrews (self, segmentationNode):
    import SegmentStatistics
    segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
    segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
    segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.centroid_ras.enabled", str(True))
    segStatLogic.computeStatistics()
    stats = segStatLogic.getStatistics()

    pointListNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode","ScrewPoints")
    pointListNode.CreateDefaultDisplayNodes()
    for segmentId in stats["SegmentIDs"]:
      centroid_ras = stats[segmentId,"LabelmapSegmentStatisticsPlugin.centroid_ras"]
      segmentName = segmentationNode.GetSegmentation().GetSegment(segmentId).GetName()
      pointListNode.AddFiducialFromArray(centroid_ras, segmentName)

    nOfControlPoints = pointListNode.GetNumberOfControlPoints()
    points = np.zeros([nOfControlPoints,2])
    for i in range(0, nOfControlPoints):
      point = np.zeros(3)
      pointListNode.GetNthControlPointPosition(i, point)
      points[i,:] = (point[0],point[2])
    print("points: %s"%points)

    numberScrew = 1
    pointsMini = points
    while pointsMini.size &gt; 2:
      s = pointsMini.sum(axis=1)
      diff = np.diff(pointsMini, axis=1)
      first = pointsMini[np.argmax(diff)]
      print("first: %s" % first)
      first_index = np.where(points == first)
      first_mini_index = np.where(pointsMini == first)
      segmentationNode.GetSegmentation().GetNthSegment(int(first_index[0][0])).SetName("Screw_%s"% numberScrew)
      numberScrew += 1
      second = pointsMini[np.argmax(s)]
      print("second: %s" % second)
      second_index = np.where(points == second)
      second_mini_index = np.where(pointsMini == second)
      segmentationNode.GetSegmentation().GetNthSegment(int(second_index[0][0])).SetName("Screw_%s"% numberScrew)
      numberScrew += 1
      pointsMini = np.delete(pointsMini, [first_mini_index[0][0],second_mini_index[0][0]], axis=0)
      print ("pointsMini: %s" % pointsMini)    
    print("pointsMini.size: %s" % pointsMini.size)
    if pointsMini.size ==2:
      print("pointsMini[0]: %s" %pointsMini[0])
      last_index = np.where(points == pointsMini[0])
      print("last_index: %s"%last_index[0][0])
      segmentationNode.GetSegmentation().GetNthSegment(int(last_index[0][0])).SetName("Screw_%s"% numberScrew)
</code></pre>

---

## Post #7 by @apparrilla (2022-08-01 05:46 UTC)

<p>My end goal is to speed up the intraoperative screw reviewing after control CBCT.</p>

---

## Post #8 by @apparrilla (2022-08-01 08:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> .<br>
I´ve found a problem with my code if “second” i the same point as “first” because I loose a screw.<br>
I´ve tryied to fix it with:</p>
<pre><code class="lang-auto">second = pointsMini[np.argmax(s)]
if np.array_equal(first, second): continue
</code></pre>
<p>Slicer crash with this with no error in Python Interactor. I just have to close Slicer because it´s continuosly processing something (while loop… of couse).<br>
I´ve also tried: (first==second).all() and np…array_equiv(first, second) but all of them block Slicer app.</p>
<p>Do you know what i´m doing worng?<br>
Thanks in advance.</p>

---
