# Shading changes with default orientation buttons at different zooms

**Topic ID**: 8907
**Date**: 2019-10-25
**URL**: https://discourse.slicer.org/t/shading-changes-with-default-orientation-buttons-at-different-zooms/8907

---

## Post #1 by @ezgimercan (2019-10-25 19:53 UTC)

<p>In preview version 4.11.0-2019-10-23, <strong>in orthographic rendering</strong>, shading changes when default orientation buttons are clicked after zooming in and out. See attached videos comparing current stable (4.10.2) and preview versions. It is reproducible on Windows 10 and CentOS 7.<br>
Unexpected behavior in preview version:<br>
[<a href="https://www.dropbox.com/s/x0vjmr8i3fmtlx0/preview.mp4?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/x0vjmr8i3fmtlx0/preview.mp4?dl=0</a>]<br>
Stable version:<br>
[<a href="https://www.dropbox.com/s/1r327yz1h0vn86z/stable.mp4?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/1r327yz1h0vn86z/stable.mp4?dl=0</a>]</p>

---

## Post #2 by @pieper (2019-10-25 21:07 UTC)

<p>Thanks for the clear report <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>I suspect this is something with the new opengl backend of vtk that we use in the latest slicer.</p>
<p>Often the best way forward is to try replicating the issue in native vtk, like in one of <a href="https://lorensen.github.io/VTKExamples/site/">the examples</a>.</p>

---

## Post #3 by @ezgimercan (2019-10-25 21:32 UTC)

<p>Thanks for the quick response, <a class="mention" href="/u/pieper">@pieper</a>. I know a little bit VTK but I haven’t done any coding for Slicer. For example, which functions are called in VTK when you set default orientations in Slicer? How does Slicer sets ortho projection in VTK? Any pointers?</p>

---

## Post #4 by @pieper (2019-10-25 21:50 UTC)

<p>There are multiple layers involved in slicer, but hopefully the effect could be captured in a simple easily reproduced script by changing the camera parameters in something like <a href="https://lorensen.github.io/VTKExamples/site/Python/VolumeRendering/SimpleRayCast/">this script</a>.</p>
<p>Also, now that I think about it, can you confirm whether this same effect happens with the CPU volume rendering, or only with the GPU (this would be another thing to capture in an example script).</p>

---

## Post #5 by @ezgimercan (2019-10-25 21:55 UTC)

<p>It’s only with GPU Ray Casting but that’s the only thing my lab uses. I’ll try VTK scripting - I assume it’s VTK-8.2.0?</p>

---

## Post #6 by @muratmaga (2019-10-25 22:10 UTC)

<p>I can replicate this with MRhead.nrrd using cpu rendering. It is a lot more subtle than GPU raycasting, but it is there (Windows 10, r28545)</p>

---

## Post #7 by @ezgimercan (2019-10-25 23:02 UTC)

<p>I cannot reproduce using this simple VTK script where I</p>
<ul>
<li>read the CTHead from sample data as .vtk object (I checked Slicer with this file and the behavior is still the same),</li>
<li>rotate the camera with right mouse click.</li>
<li>zoom in and out</li>
<li>right click on the screen to change the camera angle<br>
but the shading seems to be OK. I used PythonSlicer executable from preview.</li>
</ul>
<p><a href="https://www.dropbox.com/s/z6no64hcyzdtvyg/vtk.test.camera.rotation.shading.py?dl=0" rel="nofollow noopener">script</a><br>
<a href="https://www.dropbox.com/s/bo82nyih3m9gmhf/vtk.test.camera.rotation.shading.mp4?dl=0" rel="nofollow noopener">video</a></p>
<p>But again, I am not sure this is the way default orientation buttons change the 3D view.</p>

---

## Post #8 by @lassoan (2019-10-26 00:46 UTC)

<p>Good catch.</p>
<p>The lighting change is because default light in a renderer is a headlight, which is a light fixed to the camera’s position. When in parallel projection mode, the camera distance is changed when you click the standard view orientation buttons, based on current zoom factor (see ctkVTKRenderView::lookFromAxis).</p>
<p>This camera position change is unnecessary for perspective projection (we have separate functions for resetting field of view) and causes unexpected lighting update for parallel projection, so it should be removed. <a href="https://github.com/commontk/CTK/pull/889">Pull request with a fix</a> submited.</p>

---

## Post #9 by @ezgimercan (2019-11-05 00:12 UTC)

<p>Quick question <a class="mention" href="/u/lassoan">@lassoan</a>, will this also fix the cropping effect in 3D rendering of segmentations? It happens in ortho projection when the same default orientation buttons are clicked. The portion of the 3D rendering closer to the camera is cropped if zoomed in. I believe VTK renderer has a clipping range and it seems related. Again, this was not the case in stable version. See below:</p>
<p>3D rendering of a segment via “Show 3D” button (it also happens with any model (mesh):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c0c3e1fa2a1b1ef5af9cd4a536a75e38553a868.jpeg" data-download-href="/uploads/short-url/aQKw5tDd7xLgaZeN5bcY5GYjOmA.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c0c3e1fa2a1b1ef5af9cd4a536a75e38553a868_2_345x177.jpeg" alt="PNG" data-base62-sha1="aQKw5tDd7xLgaZeN5bcY5GYjOmA" width="345" height="177" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c0c3e1fa2a1b1ef5af9cd4a536a75e38553a868_2_345x177.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c0c3e1fa2a1b1ef5af9cd4a536a75e38553a868_2_517x265.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c0c3e1fa2a1b1ef5af9cd4a536a75e38553a868_2_690x354.jpeg 2x" data-dominant-color="8C94BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1145×590 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Zoom in and click on A (anterior) direction button from the top-left pin:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac2f0572810146e716d54201debdbce13e94e5cf.png" data-download-href="/uploads/short-url/ozcRMPtjRjStcyzx3neeuEnVRwj.png?dl=1" title="slicer2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac2f0572810146e716d54201debdbce13e94e5cf_2_345x167.png" alt="slicer2" data-base62-sha1="ozcRMPtjRjStcyzx3neeuEnVRwj" width="345" height="167" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac2f0572810146e716d54201debdbce13e94e5cf_2_345x167.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac2f0572810146e716d54201debdbce13e94e5cf_2_517x250.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac2f0572810146e716d54201debdbce13e94e5cf_2_690x334.png 2x" data-dominant-color="5A785B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer2</span><span class="informations">1276×621 568 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Zooming out to show the cropping:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c477ab4acb09325a21bfa1c08100062c8a254ce.png" data-download-href="/uploads/short-url/hJqlHFKYjneQzFREG0BDJ4FQrpA.png?dl=1" title="slicer3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c477ab4acb09325a21bfa1c08100062c8a254ce_2_345x168.png" alt="slicer3" data-base62-sha1="hJqlHFKYjneQzFREG0BDJ4FQrpA" width="345" height="168" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c477ab4acb09325a21bfa1c08100062c8a254ce_2_345x168.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c477ab4acb09325a21bfa1c08100062c8a254ce_2_517x252.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c477ab4acb09325a21bfa1c08100062c8a254ce_2_690x336.png 2x" data-dominant-color="9398C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer3</span><span class="informations">1280×625 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When you rotate the rendering, the cropped area is still the nearest portion of the rendering, again probably due to the camera clipping range.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3ffb193bf24ad0e2afa43b5ed28d9100e9693a9.png" data-download-href="/uploads/short-url/wwYcPs1S29ULsSn3KaGz1toIrkB.png?dl=1" title="slicer4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3ffb193bf24ad0e2afa43b5ed28d9100e9693a9_2_345x169.png" alt="slicer4" data-base62-sha1="wwYcPs1S29ULsSn3KaGz1toIrkB" width="345" height="169" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3ffb193bf24ad0e2afa43b5ed28d9100e9693a9_2_345x169.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3ffb193bf24ad0e2afa43b5ed28d9100e9693a9_2_517x253.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3ffb193bf24ad0e2afa43b5ed28d9100e9693a9_2_690x338.png 2x" data-dominant-color="9398C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer4</span><span class="informations">1280×628 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2019-11-05 01:21 UTC)

<p>The fix has been available for almost a week now (in Slicer Preview Releases), feel free to try it.</p>
<p>“Center the 3D view” button does not change zoom factor or camera position in parallel projection mode, so you can still end up having objects clipped by the camera clipping plane. If you press <code>r</code> key on the keyboard then the camera is moved and zoom factor is changed to ensure that the everything is visible.</p>
<p>This difference between the center button and <code>r</code> key is not intuitive for users (<code>r</code> key is very hard to discover). We already have a bug report for this: <a href="https://issues.slicer.org/view.php?id=4381">https://issues.slicer.org/view.php?id=4381</a> - I’ve re-targeted it for Slicer-4.11.</p>

---

## Post #11 by @ezgimercan (2019-11-05 01:30 UTC)

<p>Unless I am missing something, the preview version 2019-11-03 for Windows still has the first problem with the shading. Your fix seems to be not merged to the master -again I am a novice GitHub user and don’t know what goes into nightly builds.</p>

---

## Post #12 by @lassoan (2019-11-05 01:35 UTC)

<p>You are right, the fix in CTK was not merged! I’ll take care of that tonight so that tomorrow’s preview release will contain it.</p>

---

## Post #13 by @ezgimercan (2019-11-05 01:36 UTC)

<p>Thank you! I will check again tomorrow.</p>

---

## Post #14 by @ezgimercan (2019-12-06 19:48 UTC)

<p>Just an update: I’ve been using the 2019-11-11 version for a while now. It works beautifully. But once in a while, when I am using dual 3D and loading and removing a bunch of CTs in the same session, the 3D rendering in the second 3D view ends up having the same shading problem. I cannot reliably reproduce the error. And it goes away when I remove the volume from the workspace and re-load.</p>
<p>It happened to me a couple of times when I do back-to-back “Close the Scene and load 2 new volumes, render them in two separate 3D views”. First I thought it only happens when</p>
<ol>
<li>Render the volume1 in both 3D views,</li>
<li>Turn on the volume1’s visibility in the view2,</li>
<li>Render the volume2 (which renders in view1 only automatically since that’s state of the volume rendering module),</li>
<li>Turn off the visibility of the volume2 in view1 (which automatically turns it on both views),</li>
<li>Turn off the visibility of the second volume in the view1 again - then you have a bogeyman in 3D view2.</li>
</ol>
<p>I checked the cameras and everything but could not identify what it is and it doesn’t reproduce every time I do the same sequence. I fiddled with changing the inputs settings before and after turning on the visibility, still couldn’t figure out the exact sequence of events. If I figure it out, I will let you know. Maybe the fact that it only happens with 2 3D views and after close-the-scene can help you identify it.</p>

---
