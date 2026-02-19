---
topic_id: 22501
title: "How To Find A Default Colorbar Unit Or Calibrate In Mm"
date: 2022-03-14
url: https://discourse.slicer.org/t/22501
---

# How to find a default colorbar unit or calibrate in mm

**Topic ID**: 22501
**Date**: 2022-03-14
**URL**: https://discourse.slicer.org/t/how-to-find-a-default-colorbar-unit-or-calibrate-in-mm/22501

---

## Post #1 by @Lexus_H (2022-03-14 16:19 UTC)

<p>Hi,</p>
<p>I have been able to colormap surface difference with ranges from -5 to 0 then differences from model 1 to model 2 ranging from 3mm to 9mm so I am wondering if the color bar ranges or values are based on mm or whatever that is set by an user.</p>
<p>It will be nice to know units or ways to calibrate it.</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2022-03-14 16:39 UTC)

<p>Length unit is in millimeters by default. So, unless you have changed it in application settings / units (which is very unlikely), the values that you see are in millimeters.</p>

---

## Post #3 by @Lexus_H (2022-03-14 16:44 UTC)

<p>Thanks!<br>
If so, why is it not depicting the difference between -9 and 0, since my samples vary from 0 to 9mm?<br>
It seems to show in color if I set the range from -5 to 0 not -9 to 0.<br>
Do you have any suggestion how to set range?<br>
Best,</p>

---

## Post #4 by @lassoan (2022-03-14 20:20 UTC)

<p>The sign indicates if the closest point on one model is inside or outside the other model. If you are not interested in the sign then you can choose <code>absolute_closest_point</code> in <code>Model to model distance</code> module.</p>

---

## Post #5 by @Lexus_H (2022-03-15 01:38 UTC)

<p>The changes are inside, so the sign helps, but the signed ranges are between -5 to 0.9 when the real changes range from -9 to 0.  It only makes sense to double the colorbar value then it makes up for the difference(change).  Is there a way to make it 1:1 ratio?  Or does that mean that anything deeper than -5 is not picked up by the colormap?  Is there a way to change the setting?<br>
Thanks</p>

---

## Post #6 by @lassoan (2022-03-15 03:09 UTC)

<p>By default the color legend is set to the data range, so if it is set to -5 to 0.9 then it means that the maximum distance found was 5mm. Note that closest distance measurement is not symmetric, so if you get an unexpected result it might be due to that you switched up the source and target models.</p>
<p>Make sure you use the latest Slicer Preview Release. It should look something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3e28f08694e7a51b9da5d5c2b2039615dd16bc2.png" data-download-href="/uploads/short-url/nnNe6xcGjeS5vhOd57foBzrIdGO.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3e28f08694e7a51b9da5d5c2b2039615dd16bc2_2_690x424.png" alt="image" data-base62-sha1="nnNe6xcGjeS5vhOd57foBzrIdGO" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3e28f08694e7a51b9da5d5c2b2039615dd16bc2_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3e28f08694e7a51b9da5d5c2b2039615dd16bc2_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a3e28f08694e7a51b9da5d5c2b2039615dd16bc2_2_1380x848.png 2x" data-dominant-color="C3C9DC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2027×1247 292 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If you want to change the displayed range then change <code>Data scalar range (auto)</code> to <code>Manual</code> and set the range that you prefer.</p>

---

## Post #7 by @Lexus_H (2022-03-16 02:58 UTC)

<p>I downloaded the preview release then changed the displayed range up to -8 which is the end of range then I ran predefect model as target and registered model of both pre and post as source.  I still get the same result.  Also, shapepopulation viewer was unstable.  What else can I try now?  Thanks</p>

---

## Post #8 by @Lexus_H (2022-03-16 02:59 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/234c84a11d522badbe00acd1dde7e58d72e709b0.png" data-download-href="/uploads/short-url/52gEliPjQ43z2n1a8na2oE5MPBu.png?dl=1" title="Screen Shot 2022-03-15 at 10.44.12 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/234c84a11d522badbe00acd1dde7e58d72e709b0_2_690x483.png" alt="Screen Shot 2022-03-15 at 10.44.12 PM" data-base62-sha1="52gEliPjQ43z2n1a8na2oE5MPBu" width="690" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/234c84a11d522badbe00acd1dde7e58d72e709b0_2_690x483.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/234c84a11d522badbe00acd1dde7e58d72e709b0_2_1035x724.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/234c84a11d522badbe00acd1dde7e58d72e709b0.png 2x" data-dominant-color="414141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-03-15 at 10.44.12 PM</span><span class="informations">1310×918 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Lexus_H (2022-03-16 18:46 UTC)

<p>The displayed range should from -9 to 0 but the data suggests -6 to 0.9 so I don’t know what I need to do.  If I leave it auto then iit ranges from -5 to 0.9.</p>
<p>Also, Shapepopulationviiewer is not found to install as an extension on the newest preview version.</p>
<p>Thanks,</p>

---

## Post #10 by @lassoan (2022-03-16 19:20 UTC)

<aside class="quote no-group" data-username="Lexus_H" data-post="9" data-topic="22501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lexus_h/48/4110_2.png" class="avatar"> Lexus_H:</div>
<blockquote>
<p>The displayed range should from -9 to 0 but the data suggests -6 to 0.9 so I don’t know what I need to do. If I leave it auto then iit ranges from -5 to 0.9.</p>
</blockquote>
</aside>
<p>If you set <code>Scalar Range Mode</code> → <code>Data scalar range (auto)</code> then the displayed range should be the same as the data range. If you find that the selected scalar’s range is not the same as the displayed data range then let us know.</p>
<aside class="quote no-group" data-username="Lexus_H" data-post="9" data-topic="22501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lexus_h/48/4110_2.png" class="avatar"> Lexus_H:</div>
<blockquote>
<p>Shapepopulationviiewer is not found to install as an extension on the newest preview version</p>
</blockquote>
</aside>
<p>Thanks for reporting, we are aware of this issue. The problem is expected to be fixed within a few days. You can track the progress here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5269">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5269" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5269" target="_blank" rel="noopener">Update extensions for Slicer-4.13</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-10-26" data-time="20:39:44" data-timezone="UTC">08:39PM - 26 Oct 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-04-30" data-time="00:05:41" data-timezone="UTC">12:05AM - 30 Apr 22 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">It is expected that due to VTK and other library updates, extensions may need to<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> be updated, too. This ticket tracks these necessary updates.

Extensions that were considered to be fixed: https://docs.google.com/spreadsheets/d/1GC4DWDpOXhuDYdfYOjJ6PmjHTeMM3-K7SoiC5ZR1GYg/edit?usp=sharing

Extensions that were decided to fix before Slicer5 release:
- [x] Chest_Imaging_Platform ([C++11/14 configuration mismatch](https://github.com/acil-bwh/ChestImagingPlatform/pull/42) + [VTK API change](https://github.com/acil-bwh/SlicerCIP/pull/37))
- [x] SlicerRadiomics (https://discourse.slicer.org/t/slicerradiomics-error/14258, https://discourse.slicer.org/t/factory-build-of-python-extensions-conflicting-with-each-other/21935)
- [x] SlicerVirtualReality (https://github.com/KitwareMedical/SlicerVirtualReality/pull/90)
- [x] ShapePopulationViewer
- [x] ShapeVariationAnalyzer
- [x] SPHARM-PDM
- [x] ukftractography
- [x] ModelToModelDistance
- [x] SlicerVMTK - macOS packaging is broken (https://github.com/vmtk/SlicerExtension-VMTK/issues/37)
- [x] SlicerJupyter - linux build failed, Python and library updates fixed it
- [x] SlicerElastix
- [x] SlicerRT - linux build error due to ITK https://github.com/SlicerRt/SlicerRT/issues/206
- [x] PathReconstruction - linux build fails, probably due to SlicerRT failure
- [x] SegmentRegistration
- [x] CMFreg - Windows build fails
- [x] DCMQI (see https://github.com/QIICR/dcmqi/issues/446)
- [x] Slicer-AirwaySegmentation
- [x] SlicerOpenIGTLink
- [x] SlicerIGSIO (https://github.com/IGSIO/SlicerIGSIO/issues/17)
- [x] SlicerDMRI</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @Lexus_H (2022-03-16 19:39 UTC)

<p>It was in Auto then you told me to do it manually on the preview release.  My data ranges from -9 to 0 but displayed range runs from -5 (auto) to 0.9/ -6(manual) to 0.9.</p>
<p>So I am letting you know.  Is there other version that has a way to set the range manually with a working shapepopulationviewer?<br>
Thanks</p>

---

## Post #12 by @lassoan (2022-03-16 19:58 UTC)

<aside class="quote no-group" data-username="Lexus_H" data-post="11" data-topic="22501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lexus_h/48/4110_2.png" class="avatar"> Lexus_H:</div>
<blockquote>
<p>My data ranges from -9 to 0 but displayed range runs from -5 (auto) to 0.9/ -6(manual) to 0.9.</p>
</blockquote>
</aside>
<p>How did you determine that your data ranges from -9 to 0?</p>

---

## Post #13 by @Lexus_H (2022-03-16 20:02 UTC)

<p>-9 to 0 means the difference betweeen model 1 (predefect)  model 2 (post defect)</p>
<p>Are you referring to something else when you said data range?</p>

---

## Post #14 by @lassoan (2022-03-16 20:14 UTC)

<p>How did you get the -9 and 0 numbers: did you save the .vtk/.vtp file and looked into the file, or loaded it into ParaView, typed a Python command to in Slicer, …?</p>

---

## Post #15 by @Lexus_H (2022-03-16 20:21 UTC)

<p>none of that but my gold standards range from -9 to 0 which I believe it was depicted in the dicom files.  I also measured in dicom format and measured it to be -9 (inside of pre model) tto 0.</p>

---

## Post #16 by @lassoan (2022-03-16 20:32 UTC)

<p>Maybe the “gold standard” data set computes something different. For example, distance between corresponding points in two meshes is entirely different than distance between closest surface points. How the that gold standard range was computed? Do you know where the 9mm distance was measured in the gold standard data set?</p>

---

## Post #17 by @Lexus_H (2022-03-16 20:49 UTC)

<p>Maybe the “gold standard” data set computes something different. For example, distance between corresponding points in two meshes is entirely different than distance between closest surface points:  How do I check this?</p>
<p>How the that gold standard range was computed?  It was created to be exact on model 2 which is same model 1 with defects.</p>
<p>Yes, it was the floor of defect from the crestal bone around a given tooth.</p>

---

## Post #18 by @lassoan (2022-03-16 21:47 UTC)

<p>Probably you did not get the answer you expected because the closest point on surface is searched in every directions. For example, if you simulated a cylinder-shaped hole then closest distance will not give you the depth of the hole but the maximum distance will be the radius of the cylinder. Closest distance is also not symmetric. The result depends on which surface you choose as source and target.</p>
<p>If you want to quantify bone loss then it may be easier to segment the bone on the two CBCTs and subtract the one with bone loss from the other. You can then use Segment Statistics module to get robust metrics, such as volume and oriented bounding box size.</p>

---

## Post #19 by @Lexus_H (2022-03-16 23:36 UTC)

<p>Colormap did depict the change in right color scheme but the deepest end, which is -9, shows as -5 with auto, -6 with manual.  Is thatt all I can get?</p>
<p>Also, regarding the bone loss, please elaborate steps in details for me.</p>
<ol>
<li>How to substract</li>
<li>how to get robust metrics</li>
<li>how to get actual measurements<br>
Thanks</li>
</ol>

---

## Post #20 by @lassoan (2022-03-17 00:31 UTC)

<p>If it the automatic scalar range is up to -5 then it means that the maximum distance in the entire mesh is 5mm.</p>
<p>If you want to understand how this was computed then for example you can check what the value is at a specific mesh position using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-scalar-values-at-surface-of-a-model">this code snippet</a>.</p>
<p>Or you can copy-paste this code snippet to visualize a selected point on the output mesh, closest distance at that point, and the closest point position in the 3D view:</p>
<pre data-code-wrap="python"><code class="lang-python">modelNode = getNode('VTK Output File')

modelPointValues = modelNode.GetPolyData().GetPointData().GetArray("PointToPointVector")
pointListNode = slicer.mrmlScene.GetFirstNodeByName("F")

if not pointListNode:
  pointListNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode","F")

while pointListNode.GetNumberOfControlPoints() &lt; 2:
  pointListNode.AddControlPoint(0,0,0)

pointsLocator = vtk.vtkPointLocator() # could try using vtk.vtkStaticPointLocator() if need to optimize
pointsLocator.SetDataSet(modelNode.GetPolyData())
pointsLocator.BuildLocator()

import numpy as np

def onMouseMoved(observer,eventid):
  ras=[0,0,0]
  crosshairNode.GetCursorPositionRAS(ras)
  closestPointId = pointsLocator.FindClosestPoint(ras)
  ras = modelNode.GetPolyData().GetPoint(closestPointId)
  closestPointValue = modelPointValues.GetTuple(closestPointId)
  closestPointPositionOnOtherMesh = [ras[0]-closestPointValue[0], ras[1]-closestPointValue[1], ras[2]+closestPointValue[2]]
  distance = np.linalg.norm(np.array(ras)-np.array(closestPointPositionOnOtherMesh))
  print(f"distance = {distance:.1f}   point1 = {ras}   point2 = {closestPointPositionOnOtherMesh}")
  pointListNode.SetNthControlPointPosition(0, ras)
  pointListNode.SetNthControlPointPosition(1, closestPointPositionOnOtherMesh)

crosshairNode=slicer.util.getNode("Crosshair")
observationId = crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, onMouseMoved)

# To stop printing of values run this:
# crosshairNode.RemoveObserver(observationId)
</code></pre>
<aside class="quote no-group" data-username="Lexus_H" data-post="19" data-topic="22501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lexus_h/48/4110_2.png" class="avatar"> Lexus_H:</div>
<blockquote>
<p>Also, regarding the bone loss, please elaborate steps in details for me.</p>
<ol>
<li>How to substract</li>
<li>how to get robust metrics</li>
<li>how to get actual measurements</li>
</ol>
</blockquote>
</aside>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">This page</a> is a good starting point for learning about image segmentation. You can subtract two segments by using <code>Logical operators</code> effect. You can get segmentation metrics (volume, bounding box size, etc.) using <code>Segment statistics</code> module.</p>

---

## Post #21 by @Lexus_H (2022-03-17 02:00 UTC)

<p>I have segmented model 1 (pre) model 2 (post) and registered segmentation (both models).  what data goes in each blank for logical effect under the segment editor module in order to substract model 2 from model 1?</p>
<p>Do I keep the segmentation in gipl format or change it to stl?</p>
<p>Thanks</p>

---

## Post #22 by @Lexus_H (2022-03-17 02:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="22501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If it the automatic scalar range is up to -5 then it means that the maximum distance in the entire mesh is 5mm.</p>
</blockquote>
</aside>
<p>So then is it ok for me to write in the manuscript that each mm in mesh corresponds to 2 mm in the actual data (sample)?</p>

---

## Post #23 by @lassoan (2022-03-17 02:14 UTC)

<aside class="quote no-group" data-username="Lexus_H" data-post="21" data-topic="22501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lexus_h/48/4110_2.png" class="avatar"> Lexus_H:</div>
<blockquote>
<p>I have segmented model 1 (pre) model 2 (post) and registered segmentation (both models). what data goes in each blank for logical effect under the segment editor module in order to substract model 2 from model 1?</p>
</blockquote>
</aside>
<p>You select the larger segment (without bone loss) in the segment list at the top, and you select the other segment in the segment list in the <code>Logical operators</code> section.</p>
<aside class="quote no-group" data-username="Lexus_H" data-post="21" data-topic="22501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lexus_h/48/4110_2.png" class="avatar"> Lexus_H:</div>
<blockquote>
<p>Do I keep the segmentation in gipl format or change it to stl?</p>
</blockquote>
</aside>
<p>You would work with binary labelmap representation, which is usually stored in nrrd files.</p>
<aside class="quote no-group" data-username="Lexus_H" data-post="22" data-topic="22501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lexus_h/48/4110_2.png" class="avatar"> Lexus_H:</div>
<blockquote>
<p>So then is it ok for me to write in the manuscript that each mm in mesh corresponds to 2 mm in the actual data (sample)?</p>
</blockquote>
</aside>
<p>Maybe what I wrote was misunderstandable because of using signed distance in the example. To make it clear: length unit of the world (a.k.a. RAS or renderer) coordinate system is mm. If distance is 1 that means the distance is 1mm.</p>

---

## Post #24 by @Lexus_H (2022-03-17 14:56 UTC)

<p>I uploaded pre/post nrrd files then what do I put on segmentation on top then master volumne and then how do I turn oon logical effect?  once I select substracct how do I select post nrrd file?  After hitting apply then where do I get a result?<br>
thanks<br>
Do you have a video for it?</p>

---

## Post #25 by @Lexus_H (2022-04-12 03:03 UTC)

<p>Please help me to determine corresponding points between two models so I can measure the distance between two corresponding points.  Also, do I need to use one model as source and registered model of two source and target models so I can get a color map along with that?</p>
<p>Thanks,</p>

---
