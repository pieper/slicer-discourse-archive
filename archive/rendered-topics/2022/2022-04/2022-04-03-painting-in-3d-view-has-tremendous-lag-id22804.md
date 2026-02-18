# Painting in 3D view has tremendous lag

**Topic ID**: 22804
**Date**: 2022-04-03
**URL**: https://discourse.slicer.org/t/painting-in-3d-view-has-tremendous-lag/22804

---

## Post #1 by @drvarunagarwal (2022-04-03 12:54 UTC)

<p>Hi,</p>
<p>We are developing an extension which requires extensive painting on the 3D model.<br>
However there is a tremendous appreciable lag while painting and it takes couple of seconds to catch up.<br>
Please see the attached video</p>
<p><a href="https://youtu.be/H_I7op9XU50" rel="noopener nofollow ugc">https://youtu.be/H_I7op9XU50</a></p>
<p>Please advise how to fix this</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2022-04-03 13:29 UTC)

<p>This is expected when large, complex meshes are displayed, because finding 3D position from a 2D cursor position is a computationally expensive operation.</p>
<p>If you don’t need to pick 3D position on volume rendering or on semi-transparent objects then you can get position from the renderer’s depth buffer. You can enable this by copying this code to the Python console:</p>
<pre><code class="lang-python">slicer.mrmlScene.GetSingletonNode('default', 'vtkMRMLCrosshairNode').SetFastPick3D(True)
</code></pre>
<p>If you always want this option to be enabled then you can put it in your Slicer startup file.</p>

---

## Post #3 by @drvarunagarwal (2022-04-03 13:39 UTC)

<p>does increasing RAM or 3D graphics card upgrade help with this?</p>

---

## Post #4 by @lassoan (2022-04-03 14:03 UTC)

<p>More RAM or stronger GPU will not help with CPU-based picking. The GPU can only be used for picking on opaque surfaces. The CPU needs to iterate through mesh points, so increasing RAM or CPU speed will make the most difference.</p>
<p>If this is an issue for your application and enabling <code>FastPick3D</code> is not feasible then there would be relatively easy ways to improve picking performance by 1-2 magnitudes. One option would be to maintain a list of locators (objects that maintain a spatial index of the object for faster picking) for complex meshes in vtkMRMLCameraDisplayableManager. Another option would be to use a slow CPU-based picking for volume nodes and semi-transparent meshes and use fast picking for all other actors.</p>

---

## Post #5 by @lassoan (2022-04-06 16:23 UTC)

<p>I’ve implemented an <a href="https://github.com/Slicer/Slicer/commit/17429e3937b31b6c3505874b64ac6cd4973caa81">improvement to the <code>FastPick3D</code> mode</a> in the latest Slicer Preview Release: fast picking now works for volume rendering, too. Fast picking still ignores semi-transparent models.</p>

---

## Post #6 by @siqueirl (2022-04-07 17:17 UTC)

<p>Hi Andras, would it be faster if we used some sort of 3D pointer device? Is that something that SlicerVR plans to implement? Thanks</p>

---

## Post #7 by @lassoan (2022-04-12 15:48 UTC)

<p>Painting a 3D volume with a brush would be extremely tedious. It is hard enough to fill a 2D shape, but filling a 3D shape would be practically impossible: you would need to spend a lot of time, moving your arms extended in the air, which would become physically tiring after a few minutes.</p>
<p>What virtual reality and 3D controllers could be very useful for is getting an understanding of 3D shape, finding any errors, and fixing them - all very quickly, within a few minutes. Doing the same with regular screen+mouse+keyboard could take tens of minutes.</p>

---

## Post #8 by @siqueirl (2022-04-12 19:05 UTC)

<p>Hi Andras, thank you for your answer. I understand the reasons for your team to not want to pursue it. I think in HCI they say this type of interaction suffers from a gorilla effect.</p>

---

## Post #9 by @lassoan (2022-04-12 19:46 UTC)

<p>Some more information, if you are contemplating segmentation by painting in 3D:</p>
<p>My dislike for the idea of painting in 3D comes from an experience with a project where we collected samples in a 3D space using electromagnetic+optical tracking (to estimate electromagnetic field distortion). First we just moved the pointer randomly, but it resulted in so sparse and non-uniform filling of the volume that it was unusable. Then we switched to more systematic sampling: moving the pointer around in a zig-zag pattern in a plane. On the table surface we could achieve full coverage in several minutes. However, when we had to take samples 1cm, 2cm etc. away from the table surface we realized that the task is impossible to do it freehand (we just cannot keep the pointer within the desired plane), so we used a lab jack to raise a plate and use that as a guide. After we got experienced we could sample a single plane in a few minutes, but the sampling still took so long time (half an hour to an hour) and was extremely boring and quite tiring. I realized then that just how much 3D space is bigger than 2D, how much harder it is to fill with point samples.</p>
<p>Commercial systems realized the need for a guiding plane, too. See for example demos at <a href="https://www.realizemed.com/">https://www.realizemed.com/</a>. However, if you use a guiding plane then you essentially just work in 2D, almost exactly the same as in a regular flat display/mouse/keyboard setup. They show some freehand “painting” demos, too, but anyone who is experienced in image segmentation can easily see that they just do threshold painting with a huge brush, which is like a slower and more tiring version of a simple global thresholding.</p>
<p>Even though it is very likely that simple painting with a brush does not work in 3D, and commercial companies could not come up with any even slightly convincing segmentation demos so far, it does not mean that segmentation in virtual reality is hopeless. The immersive 3D display and two 6-DOF controllers are very powerful tools that should be possible to leverage for segmentations. The difficulty is just that segmentation is typically a lengthy, high-precision task, which is not very well suited to do in virtual reality. For example the user just providing approximate strokes and detailed 3D segmentations being computed automatically from them (using “Grow from seeds” algorithm or AI-assisted versions) might be a promising approach. Also, quick local sculpting and polishing tools (smoothing, filling holes, pulling/pushing) might be useful for fixing small errors.</p>

---

## Post #10 by @mau_igna_06 (2022-11-26 11:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>One option would be to maintain a list of locators (objects that maintain a spatial index of the object for faster picking) for complex meshes in vtkMRMLCameraDisplayableManager.</p>
</blockquote>
</aside>
<p>Dear Andras</p>
<p>I didn’t find how to set the <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Docs/developer_guide/script_repository/models.md#get-scalar-values-at-surface-of-a-model" rel="noopener nofollow ugc">pointLocator</a> to the cameraDisplayableManager. Could you give more details on how to do this?</p>
<p>Thank you</p>

---

## Post #11 by @lassoan (2022-11-26 13:48 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="10" data-topic="22804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I didn’t find how to set the <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Docs/developer_guide/script_repository/models.md#get-scalar-values-at-surface-of-a-model">pointLocator</a> to the cameraDisplayableManager. Could you give more details on how to do this?</p>
</blockquote>
</aside>
<p>It is not implemented. You could implement it, but maybe there are easier ways.</p>
<p>For example, instead of managing a software picker for each actor, it would be much simpler and much faster to get the Z buffer at the beginning of the paint stroke and then get the 3D position from that extremely quickly. The same way as vtkWorldPointPicker does it, but instead of getting the Z buffer for each pick, we would do that only once. It could be implemented by cloning and modifying vtkWorldPointPicker. To support picking on volume rendering, we also need to use a vtkVolumePicker for each volume (as it is done in vtkMRMLThreeDViewInteractorStyle). Maybe vtkMRMLThreeDViewInteractorStyle could be modified so that it uses this modified vtkWorldPointPicker and get the Z buffer when interaction starts and then Shift+MouseMove would also be extremely fast.</p>

---

## Post #12 by @mau_igna_06 (2023-08-17 17:16 UTC)

<blockquote>
<p>If you don’t need to pick 3D position on volume rendering or on semi-transparent objects then you can get position from the renderer’s depth buffer.</p>
</blockquote>
<p>Is that expected to work on the current Stable release? I cannot notice any increase on 3D painting speed by enabling or disabling FastPick3D over an opaque segment mesh</p>

---

## Post #13 by @lassoan (2023-08-19 09:02 UTC)

<p>I don’t think there were any updates in this.</p>
<p>If you want to make picking faster on segmentations then you can increase decimation factor to 0.95 to 0.999 in segmentarion conversion parameters.</p>

---
