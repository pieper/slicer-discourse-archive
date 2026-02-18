# Text overlayed on slice

**Topic ID**: 12982
**Date**: 2020-08-13
**URL**: https://discourse.slicer.org/t/text-overlayed-on-slice/12982

---

## Post #1 by @rohan_n (2020-08-13 18:04 UTC)

<p>Hello,<br>
Is it possible to add Python code to your scripted module that displays custom text on top of the slice view? In particular, I’m interested in displaying the slice position in a user-friendly way. I created an example of what I want to add to my scripted module in MS Paint; it is shown in the image below</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ec0bc43a6be5bae9ebfa1bef3b5f8606ab1a22e.png" data-download-href="/uploads/short-url/8X8xhJZhjjSdVWPTwTF6uy2UoxM.png?dl=1" title="red_slice" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ec0bc43a6be5bae9ebfa1bef3b5f8606ab1a22e_2_464x500.png" alt="red_slice" data-base62-sha1="8X8xhJZhjjSdVWPTwTF6uy2UoxM" width="464" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ec0bc43a6be5bae9ebfa1bef3b5f8606ab1a22e_2_464x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ec0bc43a6be5bae9ebfa1bef3b5f8606ab1a22e_2_696x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ec0bc43a6be5bae9ebfa1bef3b5f8606ab1a22e.png 2x" data-dominant-color="2C2929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">red_slice</span><span class="informations">886×954 327 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-08-13 18:09 UTC)

<p>Slice viewers have corner annotations, so you can easily <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Display_text_in_a_3D_view_or_slice_view">add text in any corner</a>. In case you want to add text to any other location, you need to add a VTK text actor (preferably in a displayable manager).</p>

---

## Post #3 by @rohan_n (2020-08-13 20:00 UTC)

<p>I tried the method in the link and it worked, but the text permanently disappears as soon as you move the slider. What is the easiest way to make sure that the text gets printed to upper right corner again every time the slice slider position is moved?</p>

---

## Post #4 by @lassoan (2020-08-13 20:46 UTC)

<p>DataProbe module already uses corner annotations to display text, which erases any previous content. You can <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Hide_slice_view_annotations_.28DataProbe.29">hide slice view annotations</a>, as you can display any information you need anyway.</p>

---

## Post #5 by @rohan_n (2020-08-13 21:40 UTC)

<p>Thanks for all your help so far.<br>
Last question: What is the syntax for calling a function every time the user scrolls to a different slice in red slice view using slider or mouse scroll? I want to do something analogous to this:</p>
<p>self.CheckBox.stateChanged.connect(self.checkboxFunc)</p>
<p>Except that it detects a change in axial position viewed in red slice, instead of checkbox being checked or unchecked.</p>

---

## Post #6 by @lassoan (2020-08-13 21:48 UTC)

<p>You can get notification of slice position changes using standard VTK observations. See how <code>AddObserver</code> is used to observe a slice in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Measure_angle_between_two_slice_planes">this example</a>.</p>

---

## Post #7 by @rohan_n (2020-08-13 23:17 UTC)

<p>Great, thanks. I understand how to do what I need now.</p>

---
