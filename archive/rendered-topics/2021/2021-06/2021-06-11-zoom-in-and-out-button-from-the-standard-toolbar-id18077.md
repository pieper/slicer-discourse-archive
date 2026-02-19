---
topic_id: 18077
title: "Zoom In And Out Button From The Standard Toolbar"
date: 2021-06-11
url: https://discourse.slicer.org/t/18077
---

# Zoom in and out button from the standard toolbar

**Topic ID**: 18077
**Date**: 2021-06-11
**URL**: https://discourse.slicer.org/t/zoom-in-and-out-button-from-the-standard-toolbar/18077

---

## Post #1 by @Kshitij_Panchal (2021-06-11 12:13 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a><br>
Hello. I am trying to create zoom buttons. Basically, these buttons will zoom in and out the loaded Dicom data in a particular view (red slice, yellow slice, green slice).</p>
<p>It will be a simple zoom in and out. Like; if the red slice view is selected then by clicking on the zoom in (+) button it will be zoom in to 110 %. To zoom out click on the zoom out button (-) to go back to normal. If another view (let’s say yellow slice) is selected then the zoom value (default 100%) will be replaced according to that view.</p>
<p>please guide to develop this feature.</p>

---

## Post #2 by @lassoan (2021-06-11 17:57 UTC)

<p>Try to follow <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">this process</a>. Let us know if you get stuck.</p>

---

## Post #3 by @pieper (2021-06-11 18:39 UTC)

<p><a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L447-L465">This code</a> should also help.</p>

---

## Post #4 by @drvarunagarwal (2021-06-14 16:27 UTC)

<p>how to do the same for brightness and contrast?<br>
trying to design and have buttons for it rather than mouse controls</p>

---

## Post #5 by @drvarunagarwal (2021-06-14 16:30 UTC)

<p>Also how can I decrease the options in the layout toolbar?</p>
<p>Please advise many thanks</p>

---

## Post #6 by @cpinter (2021-06-15 09:18 UTC)

<aside class="quote no-group" data-username="drvarunagarwal" data-post="4" data-topic="18077">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drvarunagarwal/48/8914_2.png" class="avatar"> drvarunagarwal:</div>
<blockquote>
<p>how to do the same for brightness and contrast?</p>
</blockquote>
</aside>
<p>In this case the buttons will need to set <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.h#L93">these values</a> after disabling <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.h#L79">auto window/level</a>.</p>

---
