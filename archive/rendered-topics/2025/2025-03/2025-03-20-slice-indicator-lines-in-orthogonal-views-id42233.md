# Slice-indicator lines in orthogonal views?

**Topic ID**: 42233
**Date**: 2025-03-20
**URL**: https://discourse.slicer.org/t/slice-indicator-lines-in-orthogonal-views/42233

---

## Post #1 by @robertf (2025-03-20 16:44 UTC)

<p>When displaying orthogonal views, I would like to have lines displayed in each view that indicate the positions of the slices viewed in the other two views? For example, in the image below, red and yellow lines are shown in the green view to indicate which slices are being shown in the red and yellow views. The red view would show green and yellow lines, and the yellow view would show red and green lines; I haven’t shown them in the image because it’s difficult to figure out where they would be.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dca7c38ce5c9a2da567ba0ea75aa72369d25b646.jpeg" data-download-href="/uploads/short-url/vu0tvtnRbU7I1hB74lRh8P2Sgei.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dca7c38ce5c9a2da567ba0ea75aa72369d25b646_2_345x163.jpeg" alt="image" data-base62-sha1="vu0tvtnRbU7I1hB74lRh8P2Sgei" width="345" height="163" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dca7c38ce5c9a2da567ba0ea75aa72369d25b646_2_345x163.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dca7c38ce5c9a2da567ba0ea75aa72369d25b646_2_517x244.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dca7c38ce5c9a2da567ba0ea75aa72369d25b646_2_690x326.jpeg 2x" data-dominant-color="ADABA6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1090×516 94.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is this already possible in Slicer?<br>
In principle the same information can be found by looking at the 3D view, but it gets very messy and hard to interpret.<br>
Thank you.</p>

---

## Post #2 by @jamesobutler (2025-03-20 17:38 UTC)

<p>I think the existing the slice intersection tool button covers what you need here. When it is checked you get the intersection lines in the 2D slice viewers.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f632a5cae942ee656b95f31bd230272b1a422e3.jpeg" data-download-href="/uploads/short-url/4tFghzYavFjCb3XPW5jI1cGH8rN.jpeg?dl=1" title="{0FC4139A-BE41-40F6-BA04-DFF4CE6F42CB}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f632a5cae942ee656b95f31bd230272b1a422e3_2_660x500.jpeg" alt="{0FC4139A-BE41-40F6-BA04-DFF4CE6F42CB}" data-base62-sha1="4tFghzYavFjCb3XPW5jI1cGH8rN" width="660" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f632a5cae942ee656b95f31bd230272b1a422e3_2_660x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f632a5cae942ee656b95f31bd230272b1a422e3_2_990x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f632a5cae942ee656b95f31bd230272b1a422e3_2_1320x1000.jpeg 2x" data-dominant-color="59585C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{0FC4139A-BE41-40F6-BA04-DFF4CE6F42CB}</span><span class="informations">1361×1031 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @robertf (2025-03-24 23:55 UTC)

<p>Yes! That’s exactly what I wanted. Thank you. I should have found it myself.</p>
<p>It doesn’t seem to be mentioned at <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#interacting-with-views" class="inline-onebox" rel="noopener nofollow ugc">User Interface — 3D Slicer documentation</a>. ‘slice intersection’ is mentioned only in ‘Mouse &amp; Keyboard Shortcuts’, and there it says ‘<code>Slice intersections</code> must be enabled in <code>Crosshair selection</code> toolbar’, which I don’t understand.</p>

---

## Post #4 by @jamesobutler (2025-03-25 00:38 UTC)

<p>If you right-click in an empty place of the top toolbar area you get a context menu to show/hide various toolbars. The “Crosshair selection” named toolbar contains both the button associated with the Crosshair functionality and also the button for Slice intersection visibility.</p>

---

## Post #5 by @pieper (2025-03-25 11:05 UTC)

<p><a class="mention" href="/u/robertf">@robertf</a> glad you found what you needed.  if anything is unclear or incomplete in the documentation please suggest changes using the pull request mechanism.</p>

---

## Post #6 by @Shirly_Someck (2025-08-26 10:26 UTC)

<p>Hi,</p>
<p>Is there also an option to show intersection on the 3D view without the actual 2D scans on top of it?</p>
<p>Thanks</p>

---
