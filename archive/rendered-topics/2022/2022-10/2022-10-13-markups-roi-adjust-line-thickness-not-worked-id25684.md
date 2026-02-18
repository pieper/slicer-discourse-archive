# Markups ROI, adjust line thickness not worked?

**Topic ID**: 25684
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/markups-roi-adjust-line-thickness-not-worked/25684

---

## Post #1 by @StephenLeePeng (2022-10-13 15:37 UTC)

<p>Hello every:<br>
When I created a Markups ROI default, then I want to change the line thickness of ROI.<br>
And according to the toolbar, I find the “Line thickness” option to achieve the goal.<br>
Line thickness supply two method: absolute or ratio.<br>
But when I tried two mode, none of modes worked.<br>
Even though I change the thickness to  99.9900mm (Maximum values) in absoulte mode; or change the ratio to 100%, not any changed appear.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6783f563cb51193ff0e2d5fb310a6d477263251.png" data-download-href="/uploads/short-url/zan5mXm23rqjPoIFOntVpTtB7fb.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6783f563cb51193ff0e2d5fb310a6d477263251_2_690x252.png" alt="1" data-base62-sha1="zan5mXm23rqjPoIFOntVpTtB7fb" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6783f563cb51193ff0e2d5fb310a6d477263251_2_690x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6783f563cb51193ff0e2d5fb310a6d477263251_2_1035x378.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6783f563cb51193ff0e2d5fb310a6d477263251.png 2x" data-dominant-color="262027"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1078×395 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d29f7ac633375ff9e8e8b4d6636b10298251db88.png" data-download-href="/uploads/short-url/u3fX2nPo0DdaOL420uJpXBAyUAw.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d29f7ac633375ff9e8e8b4d6636b10298251db88.png" alt="2" data-base62-sha1="u3fX2nPo0DdaOL420uJpXBAyUAw" width="690" height="286" data-dominant-color="262229"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1005×418 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Why the line thickness adjustment not worked, and How I can achieve my goal.<br>
Any advice will be appreciate!</p>
<p>And thanks to <a class="mention" href="/u/lassoan">@lassoan</a> in advance, expect your advice.</p>

---

## Post #2 by @lassoan (2022-10-13 16:38 UTC)

<p>Line thickness of plane and ROI markups is not editable. Please submit a feature request at <a href="https://github.com/Slicer/Slicer/issues" class="inline-onebox">Issues · Slicer/Slicer · GitHub</a> and we’ll implement this, probably within the next few months. If it is more urgent then you may consider adding this feature yourself (porting it over from the line markup). We can help you getting started.</p>

---

## Post #3 by @jamesobutler (2022-10-13 16:43 UTC)

<p>Line Thickness of ROI Markups was something I mentioned at</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5061#issuecomment-859090531">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5061#issuecomment-859090531" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5061#issuecomment-859090531" target="_blank" rel="noopener nofollow ugc">Create markups ROI</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-07-25" data-time="00:33:02" data-timezone="UTC">12:33AM - 25 Jul 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Annotation ROI nodes have many limitations. We need complete rework, based on ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rkups infrastructure.

## Describe the solution you'd like

Have a new vtkMRMLMarkupsROINode, similar to vtkMRMLAnnotationROINode but with these additional features:
- [x] can be rotated
- [x] can be transformed (#1636)
- [x] has label
- [x] its color can be set
- [x] has inside-out mode (https://github.com/Slicer/Slicer/issues/1596)

Additional specific requests:

High priority:
- [x] Storage: use a single "orientation" matrix for storing orientation (instead of separate xAxis, yAxis, zAxis"), as it is more consistent with how we usually manage orientation
- [x] Storage: "sideLenghts" is very clear definition for a box, but not so good if we generalize the ROI (e.g., to ellipsoid); "diameter" or "size" could be better, as they are probably still clear enough and applicable to more shapes than just a box
- [x] Storage: "origin" is consistent with how we represent a coordinate system, but in case of a ROI, it may be more informative to have the "center" displayed in the file (if users create a file manually or from an external software, it could be more intuitive if they specify the center); "center" is also a bit more clear than "origin" (it may not be clear for everyone that origin is in a corner)
- [x] Storage: it would be better to display ROI properties (origin, size, etc.) near the beginning (before control points, measurments, display sections), because these files will be directly viewed and edited by users, so we should always start with the most important information
- [x] Make filling 20% opacity by default (and set it to 0% when used as volume rendering clipping ROI)
- [x] Translation/rotation handles are too small in 3D (about half the size compared to slice views)
- [x] When a ROI is already the active widget and user clicks place mode again then a new widget should be created (now it resets the current widget). At least until we improve the widget toolbar (we should have separate options for editing selected segmentation or create a new one).
- [x] When the ROI is in bounding box mode and has many control points and then you switch to box mode then the ROI seems to remain in bounding box mode.
- [x] We need outline (wireframe) display in 3D view (for example, for volume rendering clipping that would be a good representation)
- [x] After placing a ROI (at least when it is done, interactively, initiated via the GUI) then make the interaction handles displayed by default, because now after you place the ROI it is very hard to adjust it.
- [x] Make right-click menu work on all interaction handle points
- [x] Make right-click work on the outline (but maybe on the filled area as well, if it is &gt;0%) so that interaction handles can be activated/deactivated in a viewer (it can be hard to find a ROI node in the Data module)
- [x] Add "Interaction handles visibility" option to eye icon right-click menu in subject hierarchy tree (probably for all markups)

Medium priority:
- [x] Cannot unzoom the slice view using right-click-and-drag when the ROI fills the slice view. Maybe the ROI should not respond to right-click inside the ROI, only at the boundary.
- [x] By default, left-click on a handle should jump slice views to that position (the same way as control points; configurable with event translations) (https://github.com/Slicer/Slicer/pull/6153)
- [x] Make the interaction arrows a bit more subtle. ROIs can be quite small and those arrows can be relatively very large. Maybe make it possible to only show the sphere handles and not the arrows.
- See task below ~~Prevent the arrows crossing the ROI boundary: it is a bit confusing that when the ROI is small then the interaction arrows cross the interaction handles on the sides. A possible solution could be to shorten the arrows for small ROIs so that its maximum size would be capped at 50-70% of the ROI box radius (it would be just shortened when the ROI is small, but it would not grow longer than the current size).~~
- [x] Add separate scale parameter for interaction handles.
- [x] Bounds of the ROI should be the bounds of the ROI box (currently bounds has zero extent along all 3 axes if ROI type is box; if it is bounding box then it has some extent, but it does not include the corners of the box, so it is quite confusing). 
- [x] ROI center is not always visible in slice views. This makes it difficult to translate the entire ROI and it would be better to see the ROI property (label, measurements), too. (https://github.com/Slicer/Slicer/pull/6173)

Low priority:
- [x] Make Get/SetXYZ more consistent with the Annotation ROI node: in annotation ROI node these values are not affected by the parent transform node, so they are in the node's coordinate system, and not in world. RadiusXYZ in markups ROI node is not affected by parent transform node (good), but XYZ value in markups ROI node _is_ affected by parent transform node (not consistent with annotation ROI node).
- [x] Fix volume measurement of transformed ROI: applying a transform with diag(2.0, 2.0, 2.0, 1.0) makes the ROI appear bugger but its volume remains the same. Need to update the measurement to compute true volume. It would be useful to add a GetSizeWorld() method.
- [ ] If the ROI is transformed using a rotation transform then ROI size adjustment sliders (Markups module / ROI settings / ... Range sliders) change all the bounds of the ROI. The sliders should probably show and change size in the local coordinate system (without any potential scaling by the parent transform). In the future there might be a "Transformed" flag (similarly to how control point coordinates can be displayed with/without the parent transform applied), but we don't need this dual mode for now.
- [x] Add a flag to enable/disable rotation
- [x] It is odd that there are no control points at all in box mode. Could we store at least the center as a control point?
- [ ] If a bounding box type ROI is created and two points are placed then the ROI is not filled (even though it has 0 thickness, it should be filled)
- [x] When moving the mouse over an interaction handle, the mouse cursor and handle color alternates between hand and arrow and selected/unselected color. It always ends up being correct but the flickering is distracting.
- [ ] Interaction is very slow in debug mode. It seems to be due to plane clipping. It couldbe nicer if we could use one clipping filter because this filter has huge overhead when clipping very simple shapes. It could be also faster to use vtkPlaneCutter.
- [ ] When interacting with the ROI in one-up 3D view, the slice representation is still being updated (vtkSlicerROIRepresentation2D::UpdateFromMRML is called and it runs this-&gt;ROIWorldToSliceTransformFilter-&gt;Update(), which takes a long time)
- [x] It would be probably better if all interaction handles disappear when the ROI is out of the slice plane (now the arrows are always displayed)
- [x] Add a shortcut (Alt+Left-click-and-drag) for symmetric adjustment of handle. This allows making the ROI box thinner without changing its position.
- [ ] Can you add an ellipsoid mode? It would help identifying any design issues that may come up in the future when we want to generalize the concept (e.g., create custom ROI widgets). Handles could be probably the same as now.
- [x] Show node name in views (it could be similar how I enabled label display recently for curves, but in this case the label should be displayed in the center)
- [x] Add measurement plugins (volume, diagonal, maybe xyz diameter)
- [x] When only rotation handles are visible then the arc just hangs in the air. It would be nice to somehow make it connected to the center.
![image](https://user-images.githubusercontent.com/307929/110144045-e5002580-7da5-11eb-8e66-f0faa6496a14.png)

To discuss:
- [x] Would it be possible to add corner handles to slice views? (just for consistency with 3D views)
- [ ] How does the ROI work with non-linear transforms? It should probably work similarly to angle and line markup, so that it would not be warped by the transforms, only the control points/handles would be transformed and they would be connected with straight lines.
- [ ] We could consider initializing the ROI with single-slice thickness. This would facilitate using it for generating 2D-like ROIs (useful for generating training data for object detection AI applications). At the same time, it is easier to adjust bounds of a cubic ROI than expanding of a flat plane.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @StephenLeePeng (2022-10-14 02:32 UTC)

<p>Thank you for your reply.<br>
The markupsROI I created is to display the range of lung nodule. And the doctor said the thickness of ROI lines is too thick to cover the edge of nodule.<br>
So I want to adjust the ROI line more thiner, and this requirement is very urgent.<br>
Could you show me how to edit the source code to achieve this target.<br>
Expect to your reply.</p>

---

## Post #5 by @lassoan (2022-10-14 13:12 UTC)

<p>Immediate solution/workaround: Line thickness is currently set in pixel units, so the line will be thinner if you set your screen to higher resolution or you can make the line relatively thinner by making the view larger. You can also change outline opacity to make sure the line does not occlude any important details.</p>
<aside class="quote no-group" data-username="StephenLeePeng" data-post="4" data-topic="25684">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephenleepeng/48/11892_2.png" class="avatar"> StephenLeePeng:</div>
<blockquote>
<p>Could you show me how to edit the source code to achieve this target.</p>
</blockquote>
</aside>
<p>The first step is to build Slicer, as explained in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">build instructions</a>. If you are done (or run into issues) then let us know and we can proceed to discuss how to add line thickness adjustment from the Line markup widget to the ROI markup widget.</p>

---

## Post #6 by @drvarunagarwal (2022-10-15 14:24 UTC)

<p>Hi,</p>
<p>Is it possible to increase the size of glyph. The handles that are used to drag the ROI box?<br>
Please advise</p>
<p>thanks</p>

---

## Post #7 by @lassoan (2022-10-15 14:26 UTC)

<p>Yes, you can change size of interaction handles in Markups module: Display / Interaction handles / Size.</p>

---
