# How to reset the size of one slice to make it display maximum

**Topic ID**: 14940
**Date**: 2020-12-08
**URL**: https://discourse.slicer.org/t/how-to-reset-the-size-of-one-slice-to-make-it-display-maximum/14940

---

## Post #1 by @Tesla2678 (2020-12-08 15:05 UTC)

<p>Operating system: Win10<br>
Slicer version:4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I want to maximum slice to make them fit the size of their viewer box by a python script.</p>
<p>I found a method: slicer.util.resetSliceViews(),</p>
<p>But it can’t work well. Is there any other method to do that?</p>
<p>Thank you very much!</p>

---

## Post #2 by @lassoan (2020-12-09 03:42 UTC)

<p><code>slicer.util.resetSliceViews()</code> works well for me. What did you expect the method will do? What happened instead?</p>

---

## Post #3 by @Tesla2678 (2020-12-17 02:52 UTC)

<p>Hello lassoan,</p>
<p>It’s hard to express.<br>
I just want to reset the size of the image in each widget to make them display maximum.<br>
I call this function while one button was pressed.</p>
<p>so How can I make it work?</p>
<p>Thank you for your help~</p>

---

## Post #4 by @lassoan (2020-12-17 03:02 UTC)

<p>Please post a screenshot of what you see and mark on it what/where would like to be different.</p>

---

## Post #5 by @Tesla2678 (2020-12-18 07:12 UTC)

<p>Hello Iassoan,</p>
<p>I want to maximum slice in each widget.<br>
From<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8a98c6c827bd243659d69ea618585bebd6ebee0.png" alt="image" data-base62-sha1="o43tcRgO8urhokQ4HBfRjELKxna" width="362" height="258"><br>
to<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5baac535bf94cf56c6392ab2d325b232025c643.jpeg" alt="image" data-base62-sha1="pVEmMLhOI4drSlJUVjvVjOD0TJh" width="389" height="316"><br>
but don’t want to reset slicer offset.</p>
<p>Thank you very much.</p>

---

## Post #6 by @mikebind (2020-12-18 23:29 UTC)

<p>If you don’t want to reset the offset, but want to change the zoom, right-clicking and dragging up and down will allow you to zoom in or out to any degree you want.  If you are concerned with keeping multiple slices in sync with one another in terms of relative physical scaling, linking the slices together (making the rings just below the pressed push pin toggle to linked rather than unlinked) and then changing the zoom on any of the slices will cause their scaling to sync.  Generally I find those two controls cover most of my use cases well enough.  If I want the image to be exactly filling the slice, then I click the center button and then scroll the offset back to where I want to be, either by spinning the scroll wheel or by holding the shift key down and moving the cursor (no click) to the region I want to focus on in another slice. Holding the shift key down centers all of the slices on the point your cursor is over (if the meaning of that isn’t clear, just give it a try, it is easier to understand in action that it is to describe it).</p>

---

## Post #7 by @Tesla2678 (2020-12-19 01:14 UTC)

<p>Hello mikebind,</p>
<p>Thank you for your reply.<br>
In fact, I want to maximize the view by python code.</p>

---

## Post #8 by @mikebind (2020-12-19 02:49 UTC)

<p>In that case, you might find this code from the script repository helpful: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_3_markup_fiducials" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_3_markup_fiducials</a></p>

---

## Post #9 by @Tesla2678 (2020-12-19 06:07 UTC)

<p>Hello mikebind,</p>
<p>Thank you very much, I will try it~</p>

---
