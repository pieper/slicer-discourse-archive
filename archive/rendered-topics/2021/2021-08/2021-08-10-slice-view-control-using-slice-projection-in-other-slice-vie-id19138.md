# Slice View Control using Slice Projection in other Slice View

**Topic ID**: 19138
**Date**: 2021-08-10
**URL**: https://discourse.slicer.org/t/slice-view-control-using-slice-projection-in-other-slice-view/19138

---

## Post #1 by @PCRedHot2 (2021-08-10 12:48 UTC)

<p>Hi, I am currently trying to add some more control options for the three slice view to the application. One thing I want to accomplish is that, through the projection line of Slice A in Slice B, user could maybe drag and move the projection line of Slice A in Slice B to move Slice A.</p>
<p>I know that the projection lines could be turned on in the crosshair button on top, but I could not find the corresponding module/class source code for the projection lines.</p>
<p>I am thinking the Class vtkMRMLSliceIntersectionWidget might be useful. Any thoughts on how this could be implemented?</p>

---

## Post #2 by @pieper (2021-08-10 13:18 UTC)

<p>There’s work already underway on this <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/InteractiveSliceIntersections/">from project week</a>.  I’m not sure of the current schedule but perhaps you could help move this along.</p>

---

## Post #3 by @lassoan (2021-08-10 16:20 UTC)

<p><a class="mention" href="/u/dgmato">@dgmato</a> it would be great if you could give us an update on your draggable slice intersections development work.</p>

---

## Post #4 by @PCRedHot2 (2021-08-10 17:55 UTC)

<p>Thank you, I will take a look at the project <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @dgmato (2021-08-11 08:58 UTC)

<p>Hi!</p>
<p>You can see the code and commits for this topic in my branch:<br>
<a href="https://github.com/dgmato/Slicer/tree/interactive_slice_intersection" rel="noopener nofollow ugc">https://github.com/dgmato/Slicer/tree/interactive_slice_intersection</a></p>
<p>Regarding the current progress, I have created new classes to render the interaction handles for interactive slice intersection. These are: <strong>vtkMRMLSliceIntersectionInteractionWidget</strong> and vtkMRMLSliceIntersectionInteractionRepresentation . I have used the classes vtkMRMLTransformHandleWidget and vtkMRMLTransformHandleRepresentation as a template. These classes were developed by <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> during last NA-MIC Project Week. Instead of managing the interaction handles based on a vtkMRMLTransformNode and vtkMRMLDisplayNode, for our case, we need to use a vtkMRMLSliceNode as a reference to enable interactive slice intersection. Therefore, I have adapted the code for that, associating a SliceNode to the interaction pipelines.</p>
<p>Also, I have created a new action to the viewers toolbar to select “interactive slice intersection” and I have added a new variable to the vtkMRMLSliceCompositeNode to control the visibility of the handles, similar to the way the normal slice intersection visibility is controlled.</p>
<p>I have also added new parameters to the vtkMRMLSliceNode class to control the interaction handles: size, active widgets, visibility, … I did this to enable the use of the functions “GetActiveComponentType” and “GetActiveComponentIndex” from the vtkMRMLSliceIntersectionInteractionRepresentation class, which are needed to know which handle the user is hovering over (translation handle or rotation handle).</p>
<p>Currently, I am working to pass function calls from the displayable manager to the widget class. I am using the vtkMRMLCrosshairDisplayableManager for that. I am having some trouble developing this last part, so I would really appreciate some help.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> told me he could contribute to this project soon. <a class="mention" href="/u/pcredhot2">@PCRedHot2</a>, you can also contribute to this branch.</p>

---

## Post #6 by @PCRedHot2 (2021-08-26 13:30 UTC)

<p>I think new updates won’t help my situation, because my project is using an older version. Instead, I have created a temporary module to implement this feature - directly drag and move/rotate the slice in other slices. Thank you for all your help!</p>
<p>For anyone with similar issue, here is the extension code <a href="https://github.com/PCRedHot/SliceIntersection" rel="noopener nofollow ugc">PCRedHot/SliceIntersection (github.com)</a>, just import to slicer directly using the extension wizard should be fine.</p>
<p>Translation by dragging the middle of the projection line.<br>
Rotation by dragging the ends of the projection line.</p>

---

## Post #7 by @lassoan (2021-08-27 02:13 UTC)

<p>Thanks for sharing. This may be useful until the implementation in Slicer core is ready.</p>
<p><a class="mention" href="/u/dgmato">@dgmato</a> Have you made progress since your last report? Do you need any help?</p>

---

## Post #8 by @dgmato (2021-08-30 16:44 UTC)

<p>Thanks for sharing <a class="mention" href="/u/pcredhot2">@PCRedHot2</a></p>
<p>I was able to display the interaction handles in the slice views and to enable interactions with these handles using the base classes developed by <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> . I am currently updating the SliceToRAS transform in the function <a href="https://github.com/dgmato/Slicer/commit/d633d4aaea3d3a51b8cbdf7b27e1e7fe954dfa40" rel="noopener nofollow ugc">ApplyTransform</a> of the vtkMRMLSliceIntersectionInteractionWidget class. I’ve checked the code by <a class="mention" href="/u/pcredhot2">@PCRedHot2</a>  and I am using a similar approach to update the SliceToRAS transform:</p>
<blockquote>
<p>// Update SliceToRAS transform<br>
vtkMatrix4x4* matrix = transform-&gt;GetMatrix();<br>
vtkMRMLSliceNode* sliceNode = this-&gt;GetSliceNode();<br>
vtkNew transformedSliceToRAS;<br>
vtkMatrix4x4::Multiply4x4(matrix, sliceNode-&gt;GetSliceToRAS(), transformedSliceToRAS);<br>
sliceNode-&gt;GetSliceToRAS()-&gt;DeepCopy(transformedSliceToRAS);<br>
sliceNode-&gt;UpdateMatrices();</p>
</blockquote>
<p>This is my branch for this development: <a href="https://github.com/dgmato/Slicer/tree/interactive_slice_intersection" rel="noopener nofollow ugc">https://github.com/dgmato/Slicer/tree/interactive_slice_intersection</a></p>
<p>However, when interacting with the handles in a slice view, the image is transformed in that view but the slice intersection in the other views do not change. See image below. See how I am able to transform the volume, but not the slice intersections.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe046f1d8440cebd0edb132b58e99b3b80315d62.gif" alt="2021-08-30 11-25-01" data-base62-sha1="Af8MchL3EsBzPY995xo6cCRKt3k" width="690" height="388" class="animated"></p>
<p>Also, the rotation and translation movements are inverted. I mean that if I move the translation handle to the right, the image is translated to the left. The same thing happens with the rotation direction.</p>
<p>Do you know what may be the problem here?</p>
<p>I would really appreciate some help on this. Thanks!</p>
<p>David</p>

---

## Post #9 by @lassoan (2021-08-31 03:05 UTC)

<p>THansk for the update. You should not modify the current view node’s SlicerToRAS, but the SliceToRAS of that slice that intersection of you interact with. If the slice views are linked or you move the intersection position then you need to modify SliceToRAS of all the other views in the same view group (see vtkMRMLSliceIntersectionWidget::ProcessSetCrosshair, vtkMRMLSliceIntersectionWidget::ProcessRotate).</p>

---

## Post #10 by @dgmato (2021-08-31 16:23 UTC)

<p>Thanks for the tip <a class="mention" href="/u/lassoan">@lassoan</a> . I was able to fix this. Now, the SliceToRAS transform is updated in the rest of the slice nodes in the view group.</p>
<p>Current state:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5051781299d583ff3e4737a687f29b0c8ec599e0.gif" alt="2021-08-31 17-14-48" data-base62-sha1="bswK8QfI1etbGQWxPcyHahK939K" width="690" height="388" class="animated"></p>
<p>I am currently working on updating the <strong>handleToWorld transforms</strong> so that the interaction handles follow the position of the slice intersection lines. I have not been able to come up with a solution for this yet.</p>

---

## Post #11 by @lassoan (2021-09-01 04:14 UTC)

<p>This is getting quite nice. You might do without the interaction handles, just change the mouse cursor near the intersection lines to indicate there is some action there.</p>

---
