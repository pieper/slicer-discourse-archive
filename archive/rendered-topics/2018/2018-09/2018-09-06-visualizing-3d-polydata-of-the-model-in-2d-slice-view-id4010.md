---
topic_id: 4010
title: "Visualizing 3D Polydata Of The Model In 2D Slice View"
date: 2018-09-06
url: https://discourse.slicer.org/t/4010
---

# Visualizing 3D polydata of the model in 2D slice view

**Topic ID**: 4010
**Date**: 2018-09-06
**URL**: https://discourse.slicer.org/t/visualizing-3d-polydata-of-the-model-in-2d-slice-view/4010

---

## Post #1 by @Feodor (2018-09-06 20:37 UTC)

<p>Hi all.<br>
The idea is to display the 3d model in the same way as its intersection with the slice plane, that is each 2D slice view display the 3d model from its own  “angle of view”.<br>
I’m trying to add the polydata of the vtkMRMLModelNode to the visualizing pipeline of the vtkMRMLModelSliceDisplayableManager class simply by adding the 3d actor and vtkPolyDataMapper.<br>
The only TransformFilter I’m using is the ModelWarper - the one that is used for transforming the 2d intersection polydata. The rendered polydata seems to be inproperly positioned and oriented as can be seen on the screenshot below.</p>
<p>Could anyone please advise me which transform should I use to achieve the initial goal? Thank you in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bb4d20d0171923009b26351562c8f04df8e5eaa.png" data-download-href="/uploads/short-url/1FyEODaUfuyRWuDv0O58WLO758u.png?dl=1" title="falsely_positioned_model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bb4d20d0171923009b26351562c8f04df8e5eaa_2_690x451.png" alt="falsely_positioned_model" data-base62-sha1="1FyEODaUfuyRWuDv0O58WLO758u" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bb4d20d0171923009b26351562c8f04df8e5eaa_2_690x451.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bb4d20d0171923009b26351562c8f04df8e5eaa_2_1035x676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bb4d20d0171923009b26351562c8f04df8e5eaa_2_1380x902.png 2x" data-dominant-color="670566"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">falsely_positioned_model</span><span class="informations">1472×963 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-09-06 23:48 UTC)

<p>3D views are supposed to be used for displaying 3D content. If you want to show mixed 2D and 3D (e.g., image slice and 3D content) then you also need to use 3D views. What is your end goal? Augmented reality display?</p>

---

## Post #3 by @Feodor (2018-09-07 12:46 UTC)

<p>Hi Andras!</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is your end goal? Augmented reality display?</p>
</blockquote>
</aside>
<p>No, the goal is to display the full 3d model behind its intersection with the slice plane. The screenshot in my initial post shows that 3D content can be shown within 2D view. The only problem that I’m currently facing is the absence of the transformation matrix which should be applied to the polydata.<br>
My guess is that it should be in form of the <strong>RASToXY</strong>, but it would give me the display coordinates, which is unsuitable in case of 3D mapper/actor.</p>

---

## Post #4 by @lassoan (2018-09-07 13:14 UTC)

<aside class="quote no-group" data-username="Feodor" data-post="3" data-topic="4010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/71c47a/48.png" class="avatar"> Feodor:</div>
<blockquote>
<p>the goal is to display the full 3d model behind its intersection with the slice plane</p>
</blockquote>
</aside>
<p>You are not supposed to add 3D actors to slice views. If you want to work with 3D actors then you need to use 3D views.</p>
<p>You can display clipped models in the 3D view (see clipping section in Models module). You can also show slice view in 3D views (click eye icon of the slice view to enable this). If these are not enough then tell a bit more about what exactly you would like to show (an example rendering or photoshopped image of what you would like to see would help a lot).</p>

---

## Post #5 by @cpinter (2018-09-07 13:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="4010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>tell a bit more about what exactly you would like to show (an example rendering or photoshopped image of what you would like to see would help a lot).</p>
</blockquote>
</aside>
<p>Yes, please! I’m quite curious now.</p>

---

## Post #6 by @Feodor (2018-09-07 14:14 UTC)

<p>Hi Csaba!</p>
<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="4010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Yes, please! I’m quite curious now.</p>
</blockquote>
</aside>
<p>The initial goal is to have a dental implants viewer based on Slicer (as it already has the radiological background for working in several view projections). Below is the snapshot of the UI of the <strong>Blue Sky Plan</strong> dental software which has the exact functionality that I’m trying to achieve for displaying both the 3d model of the implant and its intersection with the current slice (overlayed) within the 2D slice view:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fd8893cf543a6b0fc6086a2be8bdeaf146fce2b.png" data-download-href="/uploads/short-url/96O0r9uUBzfLfZbFgd4UFUkexHJ.png?dl=1" title="bsp_implants" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fd8893cf543a6b0fc6086a2be8bdeaf146fce2b_2_620x500.png" alt="bsp_implants" data-base62-sha1="96O0r9uUBzfLfZbFgd4UFUkexHJ" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fd8893cf543a6b0fc6086a2be8bdeaf146fce2b_2_620x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fd8893cf543a6b0fc6086a2be8bdeaf146fce2b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fd8893cf543a6b0fc6086a2be8bdeaf146fce2b.png 2x" data-dominant-color="585555"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bsp_implants</span><span class="informations">685×552 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To achieve the result shown on the snapshot from my initial post, I had to modify the vtkMRMLSliceModelDisplayableManager class, precisely I’ve increased the number of rendering layers in the renderwindow and added additional 2 renderers for 3D model and 2D intersections accordingly.<br>
As I already wrote, if I could apply the proper transformation matrix to 3D polydata, the problem would be solved then.</p>

---

## Post #7 by @lassoan (2018-09-07 17:09 UTC)

<p>You already achieve this visualization in 3D views. You can disable camera rotation by mouse (see Slicer script repository for details). You can also set up slice view to be parallel to the camera image plane (in Reformat module).</p>
<p>In 2D views you can see intersection or (optionally distance-encoded) projection of models.</p>

---

## Post #8 by @Feodor (2018-09-07 17:18 UTC)

<p>I’m wondering if there is no suitable transformation for the 3d model to be shown properly scaled, considering the fact that this model is already shown as 3D polydata in 2D slice view.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="4010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>or (optionally distance-encoded) projection of models.</p>
</blockquote>
</aside>
<p>Could you please clarify on that?</p>

---

## Post #9 by @cpinter (2018-09-07 17:25 UTC)

<p>I agree with Andras, you can achieve the same thing you want by actually not modifying any classes.</p>
<p>However I think in your case it’s just a matter of removing pipeline-&gt;Cutter and everything after this filter from the pipeline to prevent creating the slice intersection and showing the model as is. The slice intersection is already in the proper position so you just need to use what is being done there.</p>

---

## Post #10 by @lassoan (2018-09-08 04:20 UTC)

<aside class="quote no-group" data-username="Feodor" data-post="8" data-topic="4010">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/71c47a/48.png" class="avatar"> Feodor:</div>
<blockquote>
<p>wondering if there is no suitable transformation for the 3d model</p>
</blockquote>
</aside>
<p>There certainly is. However, even if the actor appears correctly, by placing 3D content into slice views you violate basic assumption of Slicer core and extension developers. It is difficult to assess what problems it may cause, but probably markup fiducials and other content would be occluded.</p>

---

## Post #11 by @park (2024-05-29 09:47 UTC)

<p>Hello,</p>
<p>I would like to discuss this topic again.</p>
<p>Is there an existing implementation where a model appears three-dimensional (3D) in a 2D slice?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3e5cf4dd3414a1494b148d4508d0074411d31b7.png" data-download-href="/uploads/short-url/uex6UpJSyCCPWwssL1QROCm9nBd.png?dl=1" title="2D view" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3e5cf4dd3414a1494b148d4508d0074411d31b7_2_690x272.png" alt="2D view" data-base62-sha1="uex6UpJSyCCPWwssL1QROCm9nBd" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3e5cf4dd3414a1494b148d4508d0074411d31b7_2_690x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3e5cf4dd3414a1494b148d4508d0074411d31b7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3e5cf4dd3414a1494b148d4508d0074411d31b7.png 2x" data-dominant-color="828282"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2D view</span><span class="informations">742×293 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The lighting direction and such are not very important as long as it looks three-dimensional.</p>
<p>Thank you.</p>

---

## Post #12 by @lassoan (2024-05-29 13:51 UTC)

<p>You can use 3D views if you want to display 3D content over slice images. Click the eye icon in the slice view controller to show the slice image in 3D.</p>

---

## Post #13 by @park (2024-05-29 14:16 UTC)

<p>Hello Iassoan,</p>
<p>Thank you very much for your response.</p>
<p>As you mentioned, we have confirmed that the feature is available in the 3D view. Thank you for that.</p>
<p>However, our ultimate goal is to create a panoramic view as shown below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a165472e30ec6d80963b81e6a8ebaf731dd1c25.jpeg" data-download-href="/uploads/short-url/jHzJpAVd8s6sOfw0FD1h5NtMOuF.jpeg?dl=1" title="IMG_7830" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a165472e30ec6d80963b81e6a8ebaf731dd1c25_2_690x325.jpeg" alt="IMG_7830" data-base62-sha1="jHzJpAVd8s6sOfw0FD1h5NtMOuF" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a165472e30ec6d80963b81e6a8ebaf731dd1c25_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a165472e30ec6d80963b81e6a8ebaf731dd1c25_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a165472e30ec6d80963b81e6a8ebaf731dd1c25_2_1380x650.jpeg 2x" data-dominant-color="B8B9B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_7830</span><span class="informations">1446×682 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a way to implement this feature in the 2D Slice?</p>

---

## Post #14 by @lassoan (2024-05-29 14:28 UTC)

<p>Yes, of course. Slicer can already compute the panoramic view and display it intermixed with the 3D implants. If you want to show the implants as a 3D rendering overlaid on the panoramic image then you can use a 3D view. If you want to show the implants as intersection lines then probably a slice view is easier.</p>
<p>Note that <a class="mention" href="/u/cpinter">@cpinter</a> has been working on very similar features for a long time. It may make sense to contact him instead of redeveloping everything from scratch.</p>

---
