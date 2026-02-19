---
topic_id: 34010
title: "Slicer 5 6 Unable To Change Interactor Style"
date: 2024-01-28
url: https://discourse.slicer.org/t/34010
---

# Slicer 5.6: unable to change interactor style

**Topic ID**: 34010
**Date**: 2024-01-28
**URL**: https://discourse.slicer.org/t/slicer-5-6-unable-to-change-interactor-style/34010

---

## Post #1 by @keri (2024-01-28 17:23 UTC)

<p>Hi,</p>
<p>In previous releases of Slicer (5.2 for example) it used to be possible to change interactor (from <a href="https://discourse.slicer.org/t/customize-mouse-button-function/4966/5">this post</a>):</p>
<pre data-code-wrap="python"><code class="lang-python">lm = slicer.app.layoutManager()
rw = lm.sliceWidget('Red').sliceView().renderWindow()
style = vtk.vtkInteractorStyleRubberBand2D()
rw.GetInteractor().SetInteractorStyle(style)
</code></pre>
<p>and when you start dragging the coursor on Red slice with mouse 1 pressed on you should be able to see a selection rectangle.</p>
<p>In Slicer 5.6 it doesn’t work anymore <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @pieper (2024-01-28 23:09 UTC)

<p>This is probably due to a vtk level change - maybe try to recreate it in pure vtk?  Then posting to the vtk list may help identify the needed new code.</p>

---

## Post #3 by @lassoan (2024-01-28 23:35 UTC)

<p>There have also been some interactor related developments to improve interactions in augmented/virtual reality, which may have changed the behavior. You can find details in the git log.</p>
<p>In general, I find interactor style a very primitive, limited way of translating GUI events to actions. A much more powerful and cleaner approach is what is implemented in Slicer: implement camera manipulation related actions in widgets - the same way as all other actions. Interaction style is probably a remnant from early VTK years when VTK widgets did not exist. Interaction style is also suitable for simple test and example applications, which may explain why it has not been removed from VTK. However, I would not consider using interaction style in full-fledged applications.</p>

---

## Post #4 by @keri (2024-01-29 07:34 UTC)

<p>Yes I’ve tried to run it with pure VTK and the rubber band works:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddc1c9a77725150fbd6847911b8b8e802241ca71.png" alt="image" data-base62-sha1="vDKHYgwktTOrGZ6kHFYws71uyaZ" width="365" height="396"></p>

---

## Post #5 by @keri (2024-01-29 07:37 UTC)

<p>That is very interesting opinion, thank you!<br>
Can’t find any rubber band VTK widget to select rectangle on the screen. Are there any?</p>

---

## Post #6 by @lassoan (2024-01-29 08:46 UTC)

<p>You can add your own displayable manager and widgets in your module.</p>

---

## Post #7 by @keri (2024-01-29 19:07 UTC)

<p>Alright, I think I have found the commits that disturb the possibility of changing interaction style (<a href="https://github.com/Slicer/Slicer/pull/7311" rel="noopener nofollow ugc">here is the link to PR</a>) but I will follow your suggestion and implement my needs through the <a href="https://examples.vtk.org/site/Cxx/Widgets/Slider2D/" rel="noopener nofollow ugc">vtkSliderWidget 2D</a></p>

---

## Post #8 by @lassoan (2024-02-12 03:30 UTC)

<p>That slider looks so ugly, like 20-30 years old technology. They also waste a lot of space (usually these kind of in-view controls only take up space as much as the size of a label when they are not interacted with, but a slider is much bigger). Do you really need it? What parameters do you want to modify with it?</p>

---

## Post #9 by @keri (2024-02-12 07:52 UTC)

<p>Hi Andras,</p>
<p>Agree, it looks pretty old so I’ve found a better solution:<br>
I added custom interaction to Displayabe Manager. <a href="https://discourse.slicer.org/t/add-custom-interaction-with-sliceview/34061">Here is the idea of the solution</a>.<br>
So it is possible to zoom the slice using <code>ctrl + right mouse button</code><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e2b7f16dd22251fb71b64e4abbc7f84767bdfda.gif" alt="Slicer_distorted_zoom" data-base62-sha1="khGZtkL4Jzoikg1M0JD7tARZAro" width="400" height="326" class="animated"></p>

---
