---
topic_id: 23234
title: "Extremities Of A Long Volume Vanishing When Rotating"
date: 2022-05-02
url: https://discourse.slicer.org/t/23234
---

# extremities of a long volume vanishing when rotating

**Topic ID**: 23234
**Date**: 2022-05-02
**URL**: https://discourse.slicer.org/t/extremities-of-a-long-volume-vanishing-when-rotating/23234

---

## Post #1 by @Jean (2022-05-02 12:21 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.1 r27931<br>
Expected behavior: starting with images that are stacks of binary images,with model maker I generate a 3D view, In the rotation of the 3D views I expect to see the whole volume for all points of view<br>
Actual behavior: when one dimension of these stacks, is clearly longer than the two others, typically 28 x 10 x 5, In my case the x axis of the 2D images is the longest, when rotation the volume, when I set the long length perpendicular to the screen the extremities are missing, as if the working volume available would not be a cube calculated from the longest dimension. Is there a way to decide the working volume sizes? or to set the view point outside the whole volume range in all positions?</p>

---

## Post #2 by @pieper (2022-05-02 15:01 UTC)

<p>It sounds like you need to set the volume spacing.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#panels-and-their-use" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#panels-and-their-use</a></p>
<p>If that’s not it maybe post some screenshots to explain what you are seeing.</p>

---

## Post #3 by @mikebind (2022-05-03 00:23 UTC)

<p>It sounds like this could be due to the camera’s clipping range.  Perhaps it is automatically set for the initial view and not updated during the rotation.  Does that seem consistent with what you are seeing?  What happens if you zoom in or out using the mouse scroll wheel when part of the structure is missing?  Do you see more or less of the ends?  If so, I strongly suspect it is due to the camera clipping planes.</p>

---

## Post #4 by @Jean (2022-05-03 07:02 UTC)

<p>Thank you for your answers. Here are images showing the problem : the entire volume<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc1875562709e25b3a03d7eb29c850017477755.png" data-download-href="/uploads/short-url/46o09azzi2asdwnEPDiODjFWZ9j.png?dl=1" title="entire1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc1875562709e25b3a03d7eb29c850017477755_2_690x475.png" alt="entire1" data-base62-sha1="46o09azzi2asdwnEPDiODjFWZ9j" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc1875562709e25b3a03d7eb29c850017477755_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc1875562709e25b3a03d7eb29c850017477755_2_1035x712.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc1875562709e25b3a03d7eb29c850017477755.png 2x" data-dominant-color="9A8EBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">entire1</span><span class="informations">1080×744 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>when rotating, the whole front end missing<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56dbf1cd245e2b28714563d0ca3b61cac29a13da.png" data-download-href="/uploads/short-url/cooi4lORBK8CO2VcrfANuHezGQO.png?dl=1" title="front_end_missing" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56dbf1cd245e2b28714563d0ca3b61cac29a13da_2_690x475.png" alt="front_end_missing" data-base62-sha1="cooi4lORBK8CO2VcrfANuHezGQO" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56dbf1cd245e2b28714563d0ca3b61cac29a13da_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56dbf1cd245e2b28714563d0ca3b61cac29a13da_2_1035x712.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56dbf1cd245e2b28714563d0ca3b61cac29a13da.png 2x" data-dominant-color="9990C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">front_end_missing</span><span class="informations">1080×744 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and a de-zoom of the same, showing no improvement<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d153a8ac7a7e818fbe6451c27eeec1b66fea0e0.png" data-download-href="/uploads/short-url/6qOY2yDUpCMpBRIevRA4uFdKhoc.png?dl=1" title="front_end_missing_dezoom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d153a8ac7a7e818fbe6451c27eeec1b66fea0e0_2_690x475.png" alt="front_end_missing_dezoom" data-base62-sha1="6qOY2yDUpCMpBRIevRA4uFdKhoc" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d153a8ac7a7e818fbe6451c27eeec1b66fea0e0_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d153a8ac7a7e818fbe6451c27eeec1b66fea0e0_2_1035x712.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d153a8ac7a7e818fbe6451c27eeec1b66fea0e0.png 2x" data-dominant-color="9A97CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">front_end_missing_dezoom</span><span class="informations">1080×744 63.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Steve, when you say “set the volume spacing”, do you mean in the “volumes” module? Isn’t it rather for setting image properties, and not really the working volume around the 3D image stack?<br>
Mike, is this camera clipping range accessible through mouse controlled operations or do I need to programs such as<br>
viewNode = slicer.mrmlScene.GetSingletonNode(“1”, “vtkMRMLViewNode”)<br>
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(viewNode)<br>
position = [0,0,0]<br>
focalPoint = [20,20,20]<br>
viewUpDirection = [0,1,0]<br>
cameraNode.SetPosition(position)<br>
cameraNode.SetFocalPoint(focalPoint)<br>
cameraNode.SetViewUp(viewUpDirection)<br>
and up to now I never went that deep in the use of 3D slicer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @pieper (2022-05-03 19:14 UTC)

<p>You shouldn’t need to use the python commands to set the view if all you want to do is rotate.  The clip planes should be automatically reset for you.</p>
<p>Looks like you are using an old version of Slicer.  Can you try the latest preview version?  If you are still having trouble maybe you can share the data and see if someone else can replicate.</p>

---

## Post #6 by @Jean (2022-05-04 13:15 UTC)

<p>Hello again, so, yes I installed 5.0.1 r30814 / fff8c39, and I am happy because now I can use the sandbox extension that I could not find previously, with the lightning control, that will solve a problem I had.<br>
About my question, the change in version does not seem to solve the problem. Maybe it behaves a bit differently but still strangely to me. I built a test image stack, the corresponding scene, and two animated rotating gifs, one worked correctly and not the other. The difference was the starting point, when starting from the "I " position (or the “S”) it vanishes in the rotation, when moving slightly from this position it sometimes works correctly sometimes not. You should find these files in<br>
<a href="https://filesender.renater.fr/?s=download&amp;token=a3b66242-a6d8-4fd3-856f-444620cfef68" class="onebox" target="_blank" rel="noopener nofollow ugc">https://filesender.renater.fr/?s=download&amp;token=a3b66242-a6d8-4fd3-856f-444620cfef68</a><br>
I’ll be happy to know what I’m doing wrong.</p>

---

## Post #7 by @pieper (2022-05-04 15:57 UTC)

<p>Thanks for sharing the data.  I load it in my Slicer and I don’t see the issue you reported.  Maybe someone else can replicate?</p>

---

## Post #8 by @Jean (2022-05-05 06:05 UTC)

<p>Mmmm, strange…did you try the Screen Capture yaw rotation starting from the “I” position?</p>

---

## Post #9 by @pieper (2022-05-05 12:56 UTC)

<p>No, I just looked on the screen while rotating with the mouse or using the spin button in the view controller.  If you are using Screen Capture and get different results that’s an important clue.  Maybe we need to add the call to reset clipping planes to the Screen Capture render loop.</p>

---

## Post #10 by @lassoan (2022-05-05 22:55 UTC)

<p>ScreenCapture module uses the CTK render view’s yaw and pitch methods, which indeed do not reset the camera clipping range after rotation, so clipping can occur. I’ll add the reset to CTK. Until then you can edit your ScreenCapture.py file in your Slicer installation and add the following line above <a href="https://github.com/Slicer/Slicer/blob/9f108c3ffe3a7f3f466204ae6a4eee715f67f0b0/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1312">this line</a>:</p>
<pre><code>slicer.modules.cameras.logic().GetViewActiveCameraNode(viewNode).ResetClippingRange()</code></pre>

---

## Post #11 by @mikebind (2022-05-05 23:52 UTC)

<p>It’s possible the lack of reset of the clipping planes is deliberate for the Screen Capture module.  I recall needing to manually manage the clipping planes in the past when doing endoscopy-style animations because the auto-reset close plane was not close enough to the camera (close objects in the wide-angle field of view were clipped) and the far plane was needlessly distant (nothing being rendered was very far away because the view was inside the lumen of a structure).  When learning about the clipping planes I recall that the ratio of the distance between the camera and the close clipping plane and the camera and the far clipping plane is important because it sets the resolution of the z-buffer bins.  Because of this, you get different rendering problems if you move the close plane closer to the camera without also moving the far plane proportionally closer as well.</p>
<p>Having the clipping planes reset automatically is probably best for most use cases, so that’s probably the best default behavior.  If there is a way to turn that off, that would be helpful for cases where clipping planes need to be managed more directly.</p>

---

## Post #12 by @lassoan (2022-05-06 00:39 UTC)

<p>Yes, resetting clipping planes after manipulating camera parameters is not always desirable - probably that is why it is not done at very low level in vtkCamera. However, when the camera is manipulated using the GUI then it is probably the best option.</p>
<p>I’ve submitted a pull request to CTK to reset the camera clipping range in view rotation methods:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/commontk/CTK/pull/1031">
  <header class="source">

      <a href="https://github.com/commontk/CTK/pull/1031" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/pull/1031" target="_blank" rel="noopener">BUG: Fix clipped view content when rotating view</a>
    </h4>

    <div class="branches">
      <code>commontk:master</code> ← <code>lassoan:fix-clipping-during-rotation</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-05-05" data-time="23:03:41" data-timezone="UTC">11:03PM - 05 May 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 5 additions and 0 deletions">
        <a href="https://github.com/commontk/CTK/pull/1031/files" target="_blank" rel="noopener">
          <span class="added">+5</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Camera clipping range must be reset after camera motion.

Fixes issue describe<span class="show-more-container"><a href="https://github.com/commontk/CTK/pull/1031" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">d here: https://discourse.slicer.org/t/extremities-of-a-long-volume-vanishing-when-rotating/23234/10?u=lassoan</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
