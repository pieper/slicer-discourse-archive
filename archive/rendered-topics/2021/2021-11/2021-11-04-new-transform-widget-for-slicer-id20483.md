---
topic_id: 20483
title: "New Transform Widget For Slicer"
date: 2021-11-04
url: https://discourse.slicer.org/t/20483
---

# New transform widget for Slicer

**Topic ID**: 20483
**Date**: 2021-11-04
**URL**: https://discourse.slicer.org/t/new-transform-widget-for-slicer/20483

---

## Post #1 by @mau_igna_06 (2021-11-04 01:00 UTC)

<p>Hi devs. Like I mentioned on the Slicer meeting. I would be interested in contributing a transform widget similar to the one used in the following video: <a href="https://youtu.be/7RMermYOOYY?t=96" class="inline-onebox" rel="noopener nofollow ugc">Virtual surgical planning using a DCIA free flap for mandibular reconstruction - YouTube</a></p>
<p>As you can see in the video next 60 seconds the iliac crest is registered to the mandible successfully. This is the software 3D Systems use for planning this kind of surgery. And I think this widget would be useful for making this planning possible in Slicer also.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/048d156e1983ac136d9a9938229d7c2b0526111a.jpeg" alt="3DSystemsTransformWidget.PNG" data-base62-sha1="EgbbdQDxPYuLyug62JyA5DFHJ0" width="292" height="320"></p>
<p>The widget has two modes (possibly activated with hotkeys):</p>
<ul>
<li>The widget reposition mode, where you move the frame of the widget without transforming the mesh</li>
<li>The widget transform mode, where you are able to rotate the mesh around the widget’s origin or translate the mesh by moving the widget</li>
</ul>
<p>The widget allows traslations that are:</p>
<ul>
<li>Linear, following the arrows of the frame</li>
<li>In the camara plane, moving the origin of the frame. (*)</li>
</ul>
<p>The rotations can be:</p>
<ul>
<li>Using the rings corrresponding to each arrow of the frame (rotation around that axis)</li>
<li>Using the ring that has and axis always parallel to the camera direction of view. (*)</li>
</ul>
<p>Both (*) I consider very useful because those are the only movements used in the registration shown in the video.</p>
<p>I would appreciate comments or suggestions regarding/guiding the implementation.</p>
<p>My objetive would be to make the widget as similar as possible to the one shown in the video because I consider it has great usability.</p>

---

## Post #2 by @lassoan (2021-11-04 04:41 UTC)

<p>While such widget is never the best tool for alignment (it is very inaccurate and slow), I agree that it would be nice to have it available in Slicer.</p>
<p>We already have an issue to track this task (<a href="https://github.com/Slicer/Slicer/issues/2579" class="inline-onebox">Transform Widget: easy enhancements for more user-friendly manual registrations · Issue #2579 · Slicer/Slicer · GitHub</a>), but I think you summarized the main requirements well.</p>
<p>We already have a transform widget but it has a few important limitations:</p>
<ul>
<li>the center of rotation is not adjustable</li>
<li>there are no arrows to limit translation/rotation to a single axis at a time</li>
<li>it uses a plain VTK widget instead of being based on vtkMRMLAbstractWidget</li>
</ul>
<p>There are many advantages of vtkMRMLAbstractWidget over basic VTK widgets, including support for multiple views, efficient (updates itself directly from MRML), built-in methods for focus management (as opposed to VTK’s complex and limited picking manager), support for interaction in multiple contexts (e.g., manipulating with the mouse on the desktop and using two virtual reality controllers in an immersive view), and fully customizable keyboard and mouse shortcuts.</p>
<p>You could update vtkMRMLLinearTransformsDisplayableManager3D to work similarly to how vtkMRMLMarkupsDisplayableManager works. You could create the vtkMRMLAbstractWidget based widget by cloning and modifying vtkBoxWidget2, but since we probably don’t need the box, I think it would be better to start from one of the markup widgets. Markup widgets already have handles for rotation and translation, which should be usable for transforms, too. You can ask advice from <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> about how to use these arrows in your widget.</p>
<p>Instead of having a reposition and transform mode (state), I would recommend to just use different keyboard shortcuts to translate/rotate the transform axes or change the transform.</p>
<p>Translation along the arrows or the camera plane is already implemented (dragging in the center handle moves in the camera plane; dragging the arrows translate along that axis).</p>
<p>Rotation: current rotation arrows only allow rotation along the widget axes, but I agree that it would be nice to add a rotation around camera axes option, too. It could be either by adding an outer ring or by adding a button somewhere that would toggle between widget an screen axes. Probably the outer ring is a bit simpler to implement and use.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="20483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>My objetive would be to make the widget as similar as possible to the one shown in the video because I consider it has great usability.</p>
</blockquote>
</aside>
<p>It is important to use the same translation/rotation arrows implementation in both markups and transforms, otherwise we would duplicate maintenance effort. I like how the widget looks in the video, so if you can make our current arrows prettier in any way then that’s great.</p>

---

## Post #3 by @mau_igna_06 (2021-11-04 11:21 UTC)

<p>I think the first step would be to add these actors to the vtkSlicerMarkupsWidgetRepresentation: NormalToRedSliceRotationActor, NormalToYellowSliceRotationActor, NormalToGreenSliceRotationActor and NormalToCameraPlaneRotationActor</p>
<p>I don’t know how to selectively render this actors so that NormalToRedSliceRotationActor is only rendered in the RedSliceView and so on.</p>
<p>Is this approach okay <a class="mention" href="/u/lassoan">@lassoan</a>? Maybe after I have this working I can work on the transformsWidget</p>

---

## Post #4 by @lassoan (2021-11-04 12:53 UTC)

<p>Each view has its own widget representation object, so you need to add only one more actor for rotating around the view normal.</p>

---

## Post #5 by @Sunderlandkyl (2021-11-04 14:35 UTC)

<p>Last project week I started moving the interaction handles from Markups and making them more generic, and adding them to Transform nodes. This is the branch that contains the changes: <a href="https://github.com/Sunderlandkyl/Slicer/tree/interaction_display_manager" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Sunderlandkyl/Slicer at interaction_display_manager</a>.</p>

---

## Post #6 by @mau_igna_06 (2021-11-04 20:46 UTC)

<p>Hi Kyle. I’ll look into it when I have the normalToViewRotationHandle ready for markups.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> these are the functions I don’t know how to rewrite because now there are two actors:</p>
<pre><code class="lang-auto">void vtkSlicerMarkupsWidgetRepresentation::GetActors(vtkPropCollection* pc)
void vtkSlicerMarkupsWidgetRepresentation::ReleaseGraphicsResources(vtkWindow* window)
int vtkSlicerMarkupsWidgetRepresentation::RenderOpaqueGeometry(vtkViewport* viewport)
int vtkSlicerMarkupsWidgetRepresentation::RenderTranslucentPolygonalGeometry(vtkViewport* viewport)
vtkTypeBool vtkSlicerMarkupsWidgetRepresentation::HasTranslucentPolygonalGeometry()

</code></pre>
<p>Here is my <a href="https://github.com/mauigna06/Slicer/tree/rotationHandleOrthogonalToCamaraViewDirectionFeature">branch</a>.</p>

---

## Post #7 by @mau_igna_06 (2023-11-07 20:59 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>
<p>Can we talk about the implementation plans of this feature? I really want learn some more C++ and VTK, and I’ll have time starting next month to work on it.</p>
<p>I already have a buggy branch that adds in-plane rotations to the interactiveHandle of the markups in both 2D and 3D views. I could start from here.</p>
<p>Also just to not cross-post, here is the <a href="https://github.com/Slicer/Slicer/issues/2579" rel="noopener nofollow ugc">issue</a> about this</p>

---

## Post #8 by @Sunderlandkyl (2023-11-08 16:56 UTC)

<p>Sure, let me take a look a the existing branches and come up with a plan to move forward. I’ll see how the work could be divided up.</p>

---

## Post #9 by @mau_igna_06 (2023-11-09 15:06 UTC)

<p>Here is <a href="https://www.linkedin.com/posts/david-collins-phd-3a5a009a_orthopedics-orthopedicsurgery-orthopedicimplants-activity-7128390258961903617-pLP8" rel="noopener nofollow ugc">another implementation</a> of a transform widget using a cube (apparently for rotations) <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
