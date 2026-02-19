---
topic_id: 30089
title: "Markup Fiducial Changing Position"
date: 2023-06-16
url: https://discourse.slicer.org/t/30089
---

# Markup - fiducial- changing position

**Topic ID**: 30089
**Date**: 2023-06-16
**URL**: https://discourse.slicer.org/t/markup-fiducial-changing-position/30089

---

## Post #1 by @hortakc (2023-06-16 22:49 UTC)

<p>Hello!<br>
I need to change the position of some markups (fiducial or landmarks). I am use to do it with ITK Snap because it shows me the lines of the axes crossing my markup to have them as references.<br>
More importantly, if I move one markup, it simultaneously shows me the movement in the other axes jumping through slices. For example, while moving my landmark in Axial plane, it will show me simultaneously the movement in Sagittal and Coronal slices, by moving the slices while the markup is static in these axes.<br>
At the moment, in Slicer, if I move my markup in axial, the markup disappear in sagittal and coronal axes (my slices do not move, only my markup, eventually it disappear in these axes). If I double click on it will show me where are them in all axes, but I lost the reference and complicated the exact location of my markup.</p>
<p>Is there any way to have the reference lines (which represent the intersection of axes) crossing the markups?<br>
Can I move the markup in one axes (plane) and have the movement reflected in the other planes associated with the slices movement?</p>
<p>Operating system: Windows<br>
Slicer version: 5.2.2<br>
Expected behavior: moving markups trough slices in all axes simultaneously (slices in axial, coronal and sagittal planes) showing the movement in the slices of all planes<br>
Actual behavior: movement of the markup only not movement of the slices in the remaining planes</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4797e276cf316f580b7c65e06160ceeb44042be.jpeg" data-download-href="/uploads/short-url/wBb9WqSy5COOs4zMM9YAkut00vI.jpeg?dl=1" title="ITK - fiducial - reference axis1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4797e276cf316f580b7c65e06160ceeb44042be_2_690x373.jpeg" alt="ITK - fiducial - reference axis1.PNG" data-base62-sha1="wBb9WqSy5COOs4zMM9YAkut00vI" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4797e276cf316f580b7c65e06160ceeb44042be_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4797e276cf316f580b7c65e06160ceeb44042be_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4797e276cf316f580b7c65e06160ceeb44042be_2_1380x746.jpeg 2x" data-dominant-color="4A4A4A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ITK - fiducial - reference axis1.PNG</span><span class="informations">1920×1040 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2023-06-17 03:58 UTC)

<p>I think you can do what you want if you choose the <strong>Jump Slices: Centered mode</strong> and by enabling the <strong>Show Slice interactions</strong> in Markups module (see the screenshot below). Then when you click a point, it will make sure it is centered in both slice views.</p>
<p>However, I noticed that if you move the markup point, the other slice views are not updated in real-time, you have to click another point and then click back again. I never used this feature like this before, so I do not know if this is a bug or a normal behavior. <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/smrolfe">@smrolfe</a> can you comment?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d24b83b1dc01b5ed59cb10e46468c5a5cbc9f8e9.jpeg" data-download-href="/uploads/short-url/u0m3zSk44WR1ja9MNCjFJrxbMcF.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d24b83b1dc01b5ed59cb10e46468c5a5cbc9f8e9_2_674x500.jpeg" alt="image" data-base62-sha1="u0m3zSk44WR1ja9MNCjFJrxbMcF" width="674" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d24b83b1dc01b5ed59cb10e46468c5a5cbc9f8e9_2_674x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d24b83b1dc01b5ed59cb10e46468c5a5cbc9f8e9_2_1011x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d24b83b1dc01b5ed59cb10e46468c5a5cbc9f8e9_2_1348x1000.jpeg 2x" data-dominant-color="B1B1B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1431×1061 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2023-06-17 04:37 UTC)

<p>If you enable “Jump slices” in the “Control Points” section then when you click on a control point in the table then slices jump to that location (same effect as clicking on a control point in a view).</p>
<p>You can enable slice intersection lines either in the same section or in the “Crosshair selection” toolbar.</p>
<p>While placing a markup point, you can hold down the Shift key to see the position in real-time in all the views (exactly what you describe as your preferred behavior).</p>
<p>After you placed the point, you can click it to jump to that point. I usually use this method for landmarking on image slices. Holding down Shift key (after you started dragging) will update slice positions in real-time, but that position is the mouse cursor position, which is not exactly the markup control point position (because you typically don’t click exactly in the middle of the markup control point). Real-time update of slice positions during control point position adjustment is implemented in individual modules that need this feature, for example in Landmark registration module.</p>
<p>Adding a “track mode” option to Markups module (either by modifying Shift + Click-and-drag behavior to make move the slices; or by adding a checkbox somewhere on the module GUI) would be very easy, so if the solutions above are not ideal for you then you can submit a <a href="https://discourse.slicer.org/c/support/feature-requests/9">feature request</a>. If it gets a good number of votes then we implement it.</p>

---

## Post #4 by @hortakc (2023-06-20 22:47 UTC)

<p>Dear Muratmaga, thank you so much for your reply.<br>
I did this before and it did not work. After you mentioned I re-installed 3DSlicer and the functions performed. The picture you send is really appreciated.<br>
As I needed a real-time change position using the Shift bottom helps, but it is hard to control.</p>
<p>Thank you very much for the help!!!</p>

---

## Post #5 by @hortakc (2023-06-20 22:59 UTC)

<p>Dear Lassoan,<br>
I am using the "Jump slices and “Control points”, Thanks!  The Crosshair selection did not work for my landmarking purposes. However, if did right-click on one slice and select “Slice Intersection” and “Slice Interaction,” the slices now interact.</p>
<p>As I needed a real-time change of position, using Shift did exactly what I needed!  But it is hard to control since the “Slice Intersection” function keeps activating over my real-time landmark change movement.<br>
So I am changing the landmark position using “Jump slices”, “Control points”, “Slice Intersection” and “Slice Interaction”. I move the Slice intersection on one axe (Ex coronal) to the position I want and drag the landmark in the other axe slice (Ex sagittal).</p>
<p>*One more question: How can I activate the “Crosshair selection” to be shown in the 3D window?<br>
So far I can see the axes intersection only in X, Y, Z windows.<br>
Thank you very much for the help!!!</p>

---

## Post #6 by @lassoan (2023-07-02 12:13 UTC)

<p>Crosshair (not the slice intersections) is displayed in all slice views and 3D views on the same view group. If your don’t see it then you can make it a bit larger and make 3D content semi-transparent.</p>

---
