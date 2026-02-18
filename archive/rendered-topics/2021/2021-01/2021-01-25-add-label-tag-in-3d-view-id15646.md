# Add label tag in 3D view

**Topic ID**: 15646
**Date**: 2021-01-25
**URL**: https://discourse.slicer.org/t/add-label-tag-in-3d-view/15646

---

## Post #1 by @RanChenSignIn (2021-01-25 07:44 UTC)

<p>hello everyone, i have a question, i have a segmentation with many labels,<br>
How do i add a tag on each label  in 3D view, and rotation angle of view to display only part of the labels  tag?</p>

---

## Post #2 by @RanChenSignIn (2021-01-25 08:58 UTC)

<p>Anyone can give me some advice?</p>

---

## Post #3 by @lassoan (2021-01-25 21:10 UTC)

<p>Could you attach an image that illustrates what you would like to achieve?</p>

---

## Post #4 by @RanChenSignIn (2021-01-26 02:33 UTC)

<p>OK. thank you!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d787d021fa86a83db18ebf35f3414e585bdf830b.jpeg" data-download-href="/uploads/short-url/uKFDjQOKFni6OfLhAZMOgTUaCBJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d787d021fa86a83db18ebf35f3414e585bdf830b_2_690x371.jpeg" alt="image" data-base62-sha1="uKFDjQOKFni6OfLhAZMOgTUaCBJ" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d787d021fa86a83db18ebf35f3414e585bdf830b_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d787d021fa86a83db18ebf35f3414e585bdf830b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d787d021fa86a83db18ebf35f3414e585bdf830b.jpeg 2x" data-dominant-color="4F4C58"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1024×552 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I want to add a label to the surface of the different brain structures in the 3D view,<br>
realize the rotation view to show the front label</p>

---

## Post #5 by @RanChenSignIn (2021-01-26 02:43 UTC)

<p>I have tried to add different labels centroid, but the centroid of the label is inside the label, so it cannot be displayed normally</p>

---

## Post #6 by @lassoan (2021-01-26 02:55 UTC)

<p>We recently added the option to make markups visible, even if they are occluded by other 3D objects. You can enable it in Markups module / Display / Advanced / 3D Display / Occluded visibility.</p>
<p>However, you may find that it line markups pointing from outside the volume into the target points provides better 3D depth cues than isolated points. If you want the lines to be arranged nicely, you can add an observer to the camera node and add a Python script that updates the line endpoints when the view direction changes (so that the lines and labels are always visible from the current viewpoint and don’t cross or overlap each other).</p>

---

## Post #8 by @RanChenSignIn (2021-01-26 10:00 UTC)

<p>Fine,line markups look better, thank you!</p>
<p>Could you provide some similar script examples or related information links which add an observer to the camera node and add a Python script that updates the line endpoints when the view direction changes？</p>

---

## Post #9 by @RanChenSignIn (2021-01-26 10:10 UTC)

<p>The occluded visibility approach is not suitable for my example, because there are too many brain structures targets to display, so that  too many markups in  3D view.</p>

---
