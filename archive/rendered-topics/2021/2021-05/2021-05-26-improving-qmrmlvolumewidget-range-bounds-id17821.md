---
topic_id: 17821
title: "Improving Qmrmlvolumewidget Range Bounds"
date: 2021-05-26
url: https://discourse.slicer.org/t/17821
---

# Improving qMRMLVolumeWidget range bounds

**Topic ID**: 17821
**Date**: 2021-05-26
**URL**: https://discourse.slicer.org/t/improving-qmrmlvolumewidget-range-bounds/17821

---

## Post #1 by @jamesobutler (2021-05-26 22:49 UTC)

<p>I’m hoping to improve the qMRMLVolumeWidget based on feedback from several users that I know. There is a common complaint about widgets that inherit functionality from qMRMLVolumeWidget, specifically commonly used qMRMLWindowLevelWidget and qMRMLVolumeThresholdWidget.</p>
<p>There is frequent frustrations regarding the range bounds slider in the popup widget and the values that it chooses to use.  Users find it annoying and weird that the primary slider can select values outside of the scalar range of the MRMLVolumeNode that is currently set to the widget. There appears to be some logic that tries to provide some space above and below the min/max of the scalar range. Is there a reason why it was decided to function like this? It appears that setting bounds inside the min max scalar range could help fine tune slider selection, but it doesn’t seem to make sense to support values outside the range of the min max scalar values. When users are changing sliders and nothing is happening due to being outside scalar range, that’s explained as being frustrating. cc: <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>The specific code in question is <code>updateRangeForVolumeDisplayNode</code>. See</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/Slicer/blame/daad7c2f41f1706ab8c2d0b144aeea38f9b5c6a3/Libs/MRML/Widgets/qMRMLVolumeWidget.cxx#L120-L163">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/blame/daad7c2f41f1706ab8c2d0b144aeea38f9b5c6a3/Libs/MRML/Widgets/qMRMLVolumeWidget.cxx#L120-L163" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/733e2d7be49394fca67b5d1f3cb947e411cfd5c324df6c1c5056154e276b39bc/Slicer/Slicer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/Slicer/blame/daad7c2f41f1706ab8c2d0b144aeea38f9b5c6a3/Libs/MRML/Widgets/qMRMLVolumeWidget.cxx#L120-L163" target="_blank" rel="noopener nofollow ugc">Blaming Slicer/Libs/MRML/Widgets/qMRMLVolumeWidget.cxx at...</a></h3>

  <p>Multi-platform, free open source software for visualization and image computing. - Blaming Slicer/Libs/MRML/Widgets/qMRMLVolumeWidget.cxx at daad7c2f41f1706ab8c2d0b144aeea38f9b5c6a3 · Slicer/Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ef3bbc893d3a20eab082ee5b679edfde4d5a449.png" data-download-href="/uploads/short-url/28gSDA0sU50DVYjaTZRazmDHXhD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ef3bbc893d3a20eab082ee5b679edfde4d5a449_2_690x373.png" alt="image" data-base62-sha1="28gSDA0sU50DVYjaTZRazmDHXhD" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ef3bbc893d3a20eab082ee5b679edfde4d5a449_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ef3bbc893d3a20eab082ee5b679edfde4d5a449_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0ef3bbc893d3a20eab082ee5b679edfde4d5a449_2_1380x746.png 2x" data-dominant-color="76757D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Would it be valid to change the current behavior to pin these sliders so the range could never be set lower than the scalar min or greater than the scalar max? Or does this need be a new parameter for this qMRMLVolumeWidget for choosing between desired functionality?</p>

---

## Post #2 by @lassoan (2021-05-27 02:49 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="17821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I’m hoping to improve the qMRMLVolumeWidget based on feedback from several users that I know. There is a common complaint about widgets that inherit functionality from qMRMLVolumeWidget, specifically commonly used qMRMLWindowLevelWidget and qMRMLVolumeThresholdWidget.</p>
</blockquote>
</aside>
<p>I have only used these widgets a few times in my life. Maybe partly because they are inconvenient, but mainly because I always set window/level visually (using the window/level mouse mode). Can you describe why and how do you use these widgets? Is there any workflow when you rely on setting these values numerically instead of visually?</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="17821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>There is frequent frustrations regarding the range bounds slider in the popup widget and the values that it chooses to use.</p>
</blockquote>
</aside>
<p>The popup makes sense in theory (it saves space and clicks), but I think the widget is quite confusing.</p>
<p><code>slicer.qMRMLRangeWidget()</code> solves the same task in a much cleaner way. It uses more space (the “…” button), and it requires one more click, but it is still easier to understand its logic.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb1b5d4434f3d1da6ee319c24bcd09d0fcbad9e.png" alt="image" data-base62-sha1="de0FwD6T7umSPucZGK3tyvPIEW2" width="605" height="108"></p>
<p>When clicking on the range adjustment slider:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46478702115c519772121557a0d3b1259fc3c1a3.png" data-download-href="/uploads/short-url/a1IFw2Gvnf1A9l759RdhHqtkixJ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46478702115c519772121557a0d3b1259fc3c1a3_2_690x131.png" alt="image" data-base62-sha1="a1IFw2Gvnf1A9l759RdhHqtkixJ" width="690" height="131" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46478702115c519772121557a0d3b1259fc3c1a3_2_690x131.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46478702115c519772121557a0d3b1259fc3c1a3_2_1035x196.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46478702115c519772121557a0d3b1259fc3c1a3.png 2x" data-dominant-color="CED0E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1082×206 9.82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="17821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Users find it annoying and weird that the primary slider can select values outside of the scalar range of the MRMLVolumeNode that is currently set to the widget.</p>
</blockquote>
</aside>
<p>Most often you actually select values outside of the scalar range of the volume, so this should not be annoying or weird. If the min/max values are set to values within the scalar range then the display is saturated (=signal is lost), so this should not be the norm.</p>
<p>I agree that it is not useful is to allow the minimum mapped value to be larger than the scalar range maximum, or the maximum mapped value to be smaller than the scalar range minimum. However, these limits don’t help with specifying a finite range for the slider, because the minimum mapped value must still be allowed to be much lower than the scalar range minimum and the maximum mapped value must be allowed to go well above the scalar range maximum.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="17821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>There appears to be some logic that tries to provide some space above and below the min/max of the scalar range. Is there a reason why it was decided to function like this?</p>
</blockquote>
</aside>
<p>The logic is that maximum range of the slider is 5x larger than the scalar range of the volume (with some extra heuristics, that if the scalar range is larger than 10 then the mapped range is minimum -1200 to 900). It means that you can reduce the displayed contrast of the volume to 1/5th of the original contrast.</p>
<p>Mapped range = scalar range:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48f46be95916a92db9495205347c03f71da69159.jpeg" data-download-href="/uploads/short-url/apo30KT6Ua0uErI1ueOjlkyuSNP.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48f46be95916a92db9495205347c03f71da69159_2_690x296.jpeg" alt="image" data-base62-sha1="apo30KT6Ua0uErI1ueOjlkyuSNP" width="690" height="296" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48f46be95916a92db9495205347c03f71da69159_2_690x296.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48f46be95916a92db9495205347c03f71da69159_2_1035x444.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48f46be95916a92db9495205347c03f71da69159.jpeg 2x" data-dominant-color="2C2C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1325×569 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Mapped range = 5x scalar range (1/5th contrast):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78dbd65bbeeb6e7222b86c0179ecfd127d6b3af8.jpeg" data-download-href="/uploads/short-url/hfaikXXRsmWIAt1UXgMarlTU2O4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78dbd65bbeeb6e7222b86c0179ecfd127d6b3af8_2_690x296.jpeg" alt="image" data-base62-sha1="hfaikXXRsmWIAt1UXgMarlTU2O4" width="690" height="296" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78dbd65bbeeb6e7222b86c0179ecfd127d6b3af8_2_690x296.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78dbd65bbeeb6e7222b86c0179ecfd127d6b3af8_2_1035x444.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78dbd65bbeeb6e7222b86c0179ecfd127d6b3af8.jpeg 2x" data-dominant-color="5C5C5C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1327×570 44.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To me it looks reasonable that we allow this much contrast reduction. Most details are still visible and such faded out image can be quite useful for example when the image is shown overlaid on another image.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="17821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>It appears that setting bounds inside the min max scalar range could help fine tune slider selection, but it doesn’t seem to make sense to support values outside the range of the min max scalar values.</p>
</blockquote>
</aside>
<p>Considering all the above, most likely the frustration is not due to the size of the accessible slider range (which seems reasonable), but how the widget appears and behaves (the popup automatically showing up when the widget is approached, and the main slider and the popup slider being too close and too similar).</p>
<p>What do you think about replacing the automatic popup with a <code>...</code> button similar to the qMRMLRangeWidget?</p>

---

## Post #3 by @pieper (2021-05-27 12:06 UTC)

<p>+1 for changing the popup to a collapsible area to set the range and maybe other properties.  The way the current widget comes and goes makes things seem more complex than they really are.</p>

---

## Post #4 by @jamesobutler (2021-05-27 13:08 UTC)

<p>Yes, I would be a +1 for changing qMRMLVolumeWidget to use a qMRMLRangeWidget rather than the current ctkRangeWidget + ctkPopupWidget usage. Indeed, users didn’t like the popup as often they were just hovering over and they were just trying to change the values of Window/Level or Threshold. Also the popup would appear and cover up widgets below too. They weren’t actually wanting to change bounds. Having the ToolButton extra click option would seem appropriate for the less used action to make it more deliberate. I had previously tried manipulating things such as calling <code>popup_widget.autoShow = False</code> but then changing Window/Level mode would then cause the popup to appear again.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d944764be3c4f5e0be65650ad705c033c593d6e.png" alt="image" data-base62-sha1="8MKOkj6RVJgUAcdfmQpfsWOrNBI" width="553" height="102"></p>
<p>As it relates to setting the bounds based on the scalar range of the current set volume, I think the primary reason for this was specifically as it relates to the qMRMLVolumeThresholdWidget. Having the threshold min value be less than scalar min or the threshold max be greater than the scalar max doesn’t make sense as nothing will change. So currently if you load the MRHead sample dataset, the threshold min/max will be set to -600 to 600 (the full range based on the current bounds). However, the scalar range for the volume is between 0 and 279. It is confusing to the user to change threshold value and nothing change in the image. Moving the threshold min form -600 to 0 does nothing in this case. Only,  279/1200=0.2325, 23.5% of the slider is actually doing anything.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/912340c48a20bd352984549c17cfd5bac6ecd28e.png" alt="image" data-base62-sha1="kHWLgJkkvJMU13Ql6mqhXQZ1RG6" width="551" height="106"></p>
<p>I’m going to ask the user more about the qMRMLWindowLevelWidget bounds usage and will report back here. Just wanted to go ahead and provide some more feedback.</p>

---

## Post #5 by @cpinter (2021-05-27 13:33 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="4" data-topic="17821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>…users didn’t like the popup as often they were just hovering over and they were just trying to change the values of Window/Level or Threshold. Also the popup would appear and cover up widgets below too. They weren’t actually wanting to change bounds. Having the ToolButton extra click option would seem appropriate for the less used action to make it more deliberate.</p>
</blockquote>
</aside>
<p>100% agree, using the tool button or another explicit solutions seems like a good alternative to the intrusive and unexpected popup.</p>

---

## Post #6 by @jamesobutler (2021-05-27 15:00 UTC)

<p>Ok here are some updates after clarifying behavior from some users.</p>
<p>They are all on board for the change to the qMRMLRangeWidget instead of the ctkRangeWidget + ctkPopupWidget usage. They also appreciate how the bounds works in the qMRMLRangeWidget in that it allows setting pretty much an infinite value. In the current widget, the MRHead volume has bounds of -600 to 600 but only allows the bounds to become -1200 to 900. They want to be able to set their bounds to whatever they want. Some of the images we work with have representations that have upper bounds dependent on various acquisition settings and not the base units of the detector for say like a uint8 of 0 to 255. So providing the flexibility to set upper bound to whatever is desired. The qMRMLRangeWidget will support this and they are excited to see this change.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4976beecc235e9fc94eb840252b017b9fc01f1a.png" alt="image" data-base62-sha1="yTKVaxOiMhYYlGr879LpZAUM1se" width="610" height="124"></p>
<p>What they are really desiring is being able to set the Window/Level Min/Max to the exact same values across various volumes to then be able to visually compare that this Ultrasound image is brighter than the other Ultrasound image. How the current widget bounds work (that -1200 to 900 range), it can at times prevent two volumes from having the exact same Window/Level Min/Max for comparison.</p>
<p>As it relates to qMRMLVolumeThresholdWidget, they want the values used for the bounds to be set automatically based on the scalar range. So when a new volume node is set to the widget the bounds get automatically set to the scalar min max value. The widget values would continue to reflect the upper and lower threshold values as set in the volume node’s display node. Of course after changing to the qMRMLRangeWidget for this widget as well, the upper bounds could be set to anything and that could still be supported for consistency reasons with the Window Level Widget, although setting bounds above the max scalar value really doesn’t seem to be helpful in any way and same with setting lower bound to anything less than the min scalar value.</p>

---

## Post #7 by @lassoan (2021-05-28 19:27 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="17821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>What they are really desiring is being able to set the Window/Level Min/Max to the exact same values across various volumes</p>
</blockquote>
</aside>
<p>This makes complete sense.</p>
<p>Such feature could be added as a right-click menu action to Data module, similarly to the “Show volumes in folder” action (right-click on eye icon of a folder; see implementation <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Volumes/SubjectHierarchyPlugins/qSlicerSubjectHierarchyVolumesPlugin.cxx#L111">here</a>). Or it could be a right-click action on a volume that would copy the volume’s window/level settings to all other sibling volumes (volumes in the same branch of the tree).</p>
<p>Or, it could be added to the “Compare volumes” module (or any equivalent module that you use now for setting up volume comparison).</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="17821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>As it relates to qMRMLVolumeThresholdWidget, they want the values used for the bounds to be set automatically based on the scalar range.</p>
</blockquote>
</aside>
<p>I agree that setting the threshold widget range to the volume scalar range by default makes sense (if the current threshold is outside the volume’s scalar range then the widget range would need to be set to accommodate that).</p>
<p>It would be great if you could update qMRMLVolumeThresholdWidget and qMRMLWindowLevelWidget so that they used qMRMLRangeWidget internally, while keeping the current API.</p>

---

## Post #8 by @jamesobutler (2021-05-28 21:41 UTC)

<p>Sure I can try to make these edits. I may post a PR to get final help on some C++ related help as that’s not my strong point. Expect something this upcoming week.</p>
<p>Should the min/max spinboxes on either side of the window level mode combobox be replaced by the spinboxes included in the qMRMLRangeWidget? I think the current logic is doing some show/hiding of spinboxes whether window/level or the min/max value. Then the combobox expanding the full width?</p>

---

## Post #9 by @lassoan (2021-05-29 01:39 UTC)

<p>I see, the qMRMLRangeWidget does not have the window/level numerical display mode, so it is not a full replacement of the window/level widget. Since the layout of the window/level widget is quite nice and the only issue is the automatic popup, it may be easier to just modify the current widgets by making the popup appear when the newly added <code>...</code> button is clicked. The <code>...</code> button should be added to the top row because there is more space there, but it’s probably fine to add it next to the bottom row (on the right side of the range slider), too.</p>

---

## Post #10 by @jamesobutler (2021-06-04 18:02 UTC)

<p>I’ve posted a PR regarding this work:</p><aside class="onebox githubpullrequest">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5676" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5676" target="_blank" rel="noopener nofollow ugc">Improving qMRMLVolumeWidget range bounds functionality</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:volume-widget-bounds-update</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-06-04" data-time="18:01:53" data-timezone="UTC">06:01PM - 04 Jun 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="2 commits changed 8 files with 167 additions and 83 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5676/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+167</span>
          <span class="removed">-83</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This PR aims to improve range bounds behavior for widgets that use qMRMLVolumeWi<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5676" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">dget including the Window Level and Threshold widgets. See https://discourse.slicer.org/t/improving-qmrmlvolumewidget-range-bounds/17821 for full discussion about this work.

I have added a "..." toolbutton next to the sliders in the window/level and threshold UI files that is similar in nature to what is used in the Slicer qMRMLRangeWidget. 

Shown in the image below is what things look like now. Pressing the "..." toolbutton will show/hide the popup widget contain widgets for setting the bounds of the main slider widget. The previous hover action that would trigger the popup widget was very frustrating to users as in most cases they were looking to change bounds. This toolbutton now makes changing bounds a deliberate action.

A second commit here also sets the threshold slider bounds based on the scalar range of the set MRML volume node. Thresholding outside of the scalar range does not make sense and does nothing. When things do nothing this often confuses users. Users can still change the bounds using the "..." toolbutton in the threshold widget.

![image](https://user-images.githubusercontent.com/15837524/120843878-a0b72980-c53c-11eb-91fa-0fbda088097d.png)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @jamesobutler (2021-06-28 13:52 UTC)

<p>As a final update, the PR has been merged for this work.</p>

---
