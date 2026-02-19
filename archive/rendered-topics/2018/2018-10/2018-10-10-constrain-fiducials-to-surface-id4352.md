---
topic_id: 4352
title: "Constrain Fiducials To Surface"
date: 2018-10-10
url: https://discourse.slicer.org/t/4352
---

# Constrain fiducials to surface

**Topic ID**: 4352
**Date**: 2018-10-10
**URL**: https://discourse.slicer.org/t/constrain-fiducials-to-surface/4352

---

## Post #1 by @smrolfe (2018-10-10 23:08 UTC)

<p>Hello,<br>
I’m interested in making some improvements to the Markups Module, as discussed in this <a href="https://discourse.slicer.org/t/markups-module-enhancements/4335">thread</a>. I’m starting by looking at how to stick and slide fiducial points along a surface.</p>
<p>I’m new to Slicer so any suggestions or pointers would be welcome. <a class="mention" href="/u/lassoan">@lassoan</a>, I’d appreciate hearing any design ideas you have for this feature.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-10-11 03:23 UTC)

<p>Markups fiducials are displayed in 3D views using <code>vtkAbstractPolygonalHandleRepresentation3D</code>. By default, it uses <code>vtkFocalPlanePointPlacer</code> for converting 2D click position to 3D position (this class constrains point positions to a plane parallel to the focal plane), but using <code>SetPointPlacer</code> method of the representation, it should be possible to change the placer. For example, if you set a <code>vtkPolyDataPointPlacer</code> instance as placer then point positions will be constrained to selected polygonal actor. Model displayable manager should be able to provide polygonal actor corresponding to a model node.</p>

---

## Post #3 by @smrolfe (2018-10-25 23:39 UTC)

<p>Thanks for your reply <a class="mention" href="/u/lassoan">@lassoan</a>. I’ve looked at the current implementation and would like to clarify how the handles are being used by the markups.</p>
<p>Would it be correct change the point placer of the handle created by vtkMRMLMarkupsFiducialDisplayableManager3D::CreateWidget or the handle of the Nth seed placed by vtkMRMLMarkupsFiducialDisplayableManager3D::SetNthSeed? If I understand correctly both are using vtkOrientedPolygonalHandleRepresentation3D and would be able to use the vtkPolyDataPointPlacer.</p>

---

## Post #4 by @pieper (2019-01-15 23:05 UTC)

<p>I started an experiment in this branch linked below.  I didn’t use the vtkPolyDataPointPlacer approach, because we’d also like the method to work well on volume renderings and segmentations, etc.  What I have almost works but not perfectly.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/1076">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/1076" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/1076" target="_blank" rel="noopener">Interface settings are not saved</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:37:15" data-timezone="UTC">10:37PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:37:16" data-timezone="UTC">10:37PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=1076). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @szhang (2020-08-19 16:29 UTC)

<p>May I follow up on this topic? I do not see it implemented in the latest Preview Release.<br>
Would you suggest any workaround to place a fiducial markup constrained to a surface?</p>

---

## Post #6 by @pieper (2020-08-19 17:42 UTC)

<p>Markup points are constrained to the surface of models now by default in the nightly preview.  Are you seeing something different?</p>

---

## Post #7 by @szhang (2020-08-19 18:04 UTC)

<p>Hi Steve,<br>
I am not sure what you mean by “default”. If I just make a “MarkupFiducial”, it does not have any constraint on its location.</p>
<p>Thank you!</p>

---

## Post #8 by @pieper (2020-08-19 18:05 UTC)

<p>Hi - I mean that with the current nightly if I place a markup fiducial it places on a model and sticks to it if I drag.  Is that not what you are referring to?</p>

---

## Post #9 by @szhang (2020-08-19 18:14 UTC)

<p>Yes, it is, i.e. a markup point is automatically positioned to a location closest to the model surface, kind of like “Shortest distance on surface” for curve setting. However, I do not see this feature for markup points in the latest preview release 2020-08-18. What am I missing?</p>

---

## Post #10 by @pieper (2020-08-19 18:21 UTC)

<p>For me it just happens with no feature setting required.  I guess if you don’t want to snap to a surface than you make that model invisible.</p>
<p>If you have a model visible and you click to add a fiducial in the 3D view it should be on the surface, and then stay on the surface when you drag.  That’s what happens for me anyway with today’s nightly preview.</p>

---

## Post #11 by @mikebind (2020-08-19 22:07 UTC)

<p>How does this work with volume rendering?  What if there is some transparency?</p>

---

## Post #12 by @lassoan (2020-08-19 22:16 UTC)

<p>It works great with volume rendering - point is placed where 50% opacity is reached.</p>

---

## Post #13 by @szhang (2020-08-21 19:39 UTC)

<p>Hi Steve, I tried on the 0818 nightly build but did not see any automatic “snap” to the surface, what am I missing?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68cd680e42c2bd093a66405072e0571c6cf8e2c9.png" data-download-href="/uploads/short-url/eX7JLQzLK4SQGnXVJmZDVJedEPT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68cd680e42c2bd093a66405072e0571c6cf8e2c9_2_690x373.png" alt="image" data-base62-sha1="eX7JLQzLK4SQGnXVJmZDVJedEPT" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68cd680e42c2bd093a66405072e0571c6cf8e2c9_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68cd680e42c2bd093a66405072e0571c6cf8e2c9_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68cd680e42c2bd093a66405072e0571c6cf8e2c9_2_1380x746.png 2x" data-dominant-color="6A7372"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @pieper (2020-08-21 20:01 UTC)

<p>Maybe it’s that we mean slightly different things.  What I mean is that if you click on the green part when placing the fiducial it will snap to the surface, but if you click on the blue part it will be a an arbitrary distance from the camera.  If you drag the fiducial over the green object it should snap to that.</p>

---

## Post #15 by @szhang (2020-08-21 22:29 UTC)

<p>Great, I think I finally get your meaning, so as long as the fiducial is on top of some background color of the model, it will stick to the surface. Otherwise it will be floating in free space, right?</p>
<p>In a sense it will not always retract to surface, like in the “Curve Setting” case that no matter what the curve will be sticking to the surface.</p>

---

## Post #16 by @lassoan (2020-08-21 22:52 UTC)

<p>In curves control points behave the same way as fiducials, only the curve points are strictly constrained to the selected surface. I agree that it could be useful to add a hard constraint to the control point themselves. We will implement this if one of the funded projects will require this feature. I’ve added an issue so that you can monitor if there is any progress:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5126" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5126" target="_blank" rel="noopener">Allow markups control points constrained to surface</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-08-21" data-time="22:52:09" data-timezone="UTC">10:52PM - 21 Aug 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">It would be nice to be able to constrain markups control points movement to visible surfaces (or surface of a selected...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:enhancement</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #17 by @Yuting_Deng (2020-10-15 19:27 UTC)

<p>I have encountered the same issue. I was trying to measure a surface of the cross-sections of hummingbird tongue. In order to measure the surface perpendicular to the longitudinal axes to the tongue, I transformed ROI and made measurements directly on my 3D model. However, the fiducials in the blue space is not constrained to the surface of the tongue. I wonder if it’s possible to constrain fiducials to a markup plane so it will be very flexible?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe86f8177b43fa0be85b5b4f05899510e9af2584.jpeg" data-download-href="/uploads/short-url/AjErK5Og48ZycBMbdzzaQkwtrDe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe86f8177b43fa0be85b5b4f05899510e9af2584_2_690x357.jpeg" alt="image" data-base62-sha1="AjErK5Og48ZycBMbdzzaQkwtrDe" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe86f8177b43fa0be85b5b4f05899510e9af2584_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe86f8177b43fa0be85b5b4f05899510e9af2584_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fe86f8177b43fa0be85b5b4f05899510e9af2584_2_1380x714.jpeg 2x" data-dominant-color="3C3C40"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1936×1003 393 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you!</p>

---

## Post #18 by @Yuting_Deng (2020-10-15 19:28 UTC)

<p>A sideview of the fiducials<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6edc2ae6728a9d0d8d51f47b2de21337dc96920.jpeg" alt="image" data-base62-sha1="nOIETlDfqcCL3fMWjZUmx182yBi" width="688" height="447"></p>

---

## Post #19 by @muratmaga (2020-10-15 19:36 UTC)

<p>I dont think you have 3D model, all I can see is a volume rendering. If you use curves on volume rendering, you I suspect you will be susceptible to rendering artifacts. You will be better of doing a segmentation of this region, then export it as a model and then repeat the task.</p>

---

## Post #20 by @lassoan (2020-10-15 19:43 UTC)

<p>From your screenshot it looks like Slicer works as it is supposed to. In 3D views, points are snapped to visible surfaces, which works for volume rendering, too, and as long as you can clearly see a surface in the view, the placed point positions will be predictable, too.</p>
<p>If you mean that you would like to constrain placement to an image plane then you can move a slice view where you want to annotate (by holding down Shift key while moving the mouse) and place points on that slice.</p>

---

## Post #21 by @Yuting_Deng (2020-10-15 21:57 UTC)

<p>Thank you for the info. I understand how the points are located based on the previous discussion in this thread. However, I want to make “closed curve” markups on a defined plane on my own rather than the 2D plane, because the Red 2D image plane is not actually perpendicular to the longitudinal axes to the tongue. I wonder if I can generate a new cut/a slice/a plane in 3D view to annotate?</p>

---

## Post #22 by @lassoan (2020-10-16 00:02 UTC)

<p>There are many ways to orient your slice views orthogonally to the longitudinal axis of the tongue.</p>
<p>The simplest is to enable slice intersections and rotate slice views using Ctrl/Cmd + Alt + left-click and drag in slice views until you get the right orientation.</p>
<p>If you want to reslice the tongue along its center axis, then define a markups curve corresponding to the central axis of the tongue (you can define a straight axis with two points, or you can make it curved by placing more control points).</p>
<ul>
<li>You can then use Cross-section analysis (provided by SlicerVMTK extension) to reslice with a plane orthogonal to this line.</li>
<li>If you defined a curve, you can straighten the tongue to simplify visualization and analysis using Curved Planar Reformat module (provided by Sandbox extension).</li>
<li>You can then get cross section area along the entire tongue, using Segment Cross-section Area module (provided by Sandbox extension).</li>
<li>If you find it hard to extract the tongue’s centerline exactly, then you can segment it using Segment Editor module, and compute the centerline using Extract centerline module (provided by SlicerVMTK extension)</li>
</ul>

---

## Post #23 by @Yuting_Deng (2020-10-16 17:53 UTC)

<p>It works for my purpose perfectly! Thank you so much for your help!</p>

---

## Post #24 by @Yuting_Deng (2020-10-16 19:15 UTC)

<p>As I was measuring the length of the tongue, I can see the total length is 759.3mm after I created an open curve along the center axis. I wonder if there’s a way to know the length from control point “C-1” to “C-4” for example? In this way, I will be able to know the distance between the beginning of the tongue and each point.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74b3ebcd41d9af07ac1a72e65dd449c81f1732d1.png" data-download-href="/uploads/short-url/gEoRFX56G1A3oRmKIkdnh4F5C6t.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74b3ebcd41d9af07ac1a72e65dd449c81f1732d1_2_690x361.png" alt="image" data-base62-sha1="gEoRFX56G1A3oRmKIkdnh4F5C6t" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74b3ebcd41d9af07ac1a72e65dd449c81f1732d1_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74b3ebcd41d9af07ac1a72e65dd449c81f1732d1_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74b3ebcd41d9af07ac1a72e65dd449c81f1732d1_2_1380x722.png 2x" data-dominant-color="212222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1004 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #25 by @muratmaga (2020-10-16 19:21 UTC)

<p>If you only highlight those two and right click on them, you will see the distance reported.</p>

---

## Post #26 by @Yuting_Deng (2020-10-16 21:32 UTC)

<p>When you say highlight, so you mean unselect all the other points? I right click on them and the length didn’t show up. Is there something that I did wrong?</p>

---

## Post #27 by @Yuting_Deng (2020-10-16 21:56 UTC)

<p>I understand what you mean now, but the problem is that I can only see “summed linear distance” rather than the curve length along the tongue. Is there a way to see the “open curve” length by section rather than only the total length?</p>

---

## Post #28 by @muratmaga (2020-10-16 22:00 UTC)

<p>When you have only two points selected, summed distance is the same as the distance between them. See the screenshot below.</p>
<p>It is of course difference if you have three points. it will be equivalent to distance of point 1 and 2 plus point 2 and 3.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e4ab7b6fc24ac9810c62893c7988228c82ecff7.png" data-download-href="/uploads/short-url/ds8XLGFzrmB2V5sFpcWWCBqqEYv.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e4ab7b6fc24ac9810c62893c7988228c82ecff7_2_506x499.png" alt="image" data-base62-sha1="ds8XLGFzrmB2V5sFpcWWCBqqEYv" width="506" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e4ab7b6fc24ac9810c62893c7988228c82ecff7_2_506x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e4ab7b6fc24ac9810c62893c7988228c82ecff7_2_759x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5e4ab7b6fc24ac9810c62893c7988228c82ecff7_2_1012x998.png 2x" data-dominant-color="4E525E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1438×1419 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
