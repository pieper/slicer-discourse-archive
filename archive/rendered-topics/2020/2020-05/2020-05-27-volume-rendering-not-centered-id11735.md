---
topic_id: 11735
title: "Volume Rendering Not Centered"
date: 2020-05-27
url: https://discourse.slicer.org/t/11735
---

# Volume rendering not centered

**Topic ID**: 11735
**Date**: 2020-05-27
**URL**: https://discourse.slicer.org/t/volume-rendering-not-centered/11735

---

## Post #1 by @Henry_Cope (2020-05-27 15:42 UTC)

<p>Hello,<br>
I’m running into an issue where my volume rendering is not centered. I’ve attached a picture of the result that occurs:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53dd5d4907f7f41c8cc74e62b43ab33671752a3d.png" data-download-href="/uploads/short-url/bXTTRK0RNVVqTQPUhp7vg0d9urP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53dd5d4907f7f41c8cc74e62b43ab33671752a3d_2_270x500.png" alt="image" data-base62-sha1="bXTTRK0RNVVqTQPUhp7vg0d9urP" width="270" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53dd5d4907f7f41c8cc74e62b43ab33671752a3d_2_270x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53dd5d4907f7f41c8cc74e62b43ab33671752a3d_2_405x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53dd5d4907f7f41c8cc74e62b43ab33671752a3d_2_540x1000.png 2x" data-dominant-color="3A3B47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">688×1274 18.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Ideally, the aorta would be centered within the box. I realize I can click on the centering button and have the volume centered automatically. However, this change is only temporary and I need to have this center made permanent. Is there a way for me to edit the .nrrd file directly such as changing the space origin : (vector)? Or is it possible to bake this in as a transform? Any guidance would be appreciated.</p>

---

## Post #2 by @pieper (2020-05-27 19:48 UTC)

<p>It looks like you realize that this little button at the top of the 3D view to center the box and view to your current data.  That’s the suggested approach since it doesn’t modify your data.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/396e0bc6c9f4990915fcff3ad1666a6c026caea6.png" alt="image" data-base62-sha1="8c2ZgYBbOcwdy6BKX1g0nVxlV78" width="37" height="24"></p>
<p>But another alternative is to use the Volumes module’s “Center Volume” button.  Then you can save and restore the centered volume as nrrd.  This is effectively the same as hardening a transform or changing the origin manually.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c1f4c696fb7d8888f9c216be6578be6af9b2e4c.png" data-download-href="/uploads/short-url/mh7xBLpFZi2f8cZsxZIwekWMAzy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c1f4c696fb7d8888f9c216be6578be6af9b2e4c.png" alt="image" data-base62-sha1="mh7xBLpFZi2f8cZsxZIwekWMAzy" width="690" height="147" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">863×184 7.94 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2020-05-27 20:04 UTC)

<p>“Center Volume” overwrites the volume’s position without any way to recover it later. It makes all registrations, segmentations, markups, etc. associated with the volume invalid. So, I would not recommend using this feature unless there is absolutely no other way of achieving something.</p>
<p>Applying a centering transform is fine, because you can save that transform, apply it to other associated nodes, etc.</p>

---

## Post #4 by @muratmaga (2020-05-27 21:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="11735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Applying a centering transform is fine, because you can save that transform, apply it to other associated nodes, etc.</p>
</blockquote>
</aside>
<p>Is that doable through GUI? It may be useful addition.</p>

---

## Post #5 by @pieper (2020-05-28 12:01 UTC)

<p>No gui option currently.  Perhaps in the volume module we should add an ‘add centering transform’ button option.</p>

---

## Post #6 by @Henry_Cope (2020-05-28 13:12 UTC)

<p>Thank you to all for the helpful suggestions. I had used the dreaded “Center Volume” operation before, but I was saving it to a different path and therefore very confused as to why the changes I made weren’t being saved. After finding the correct file, it works as intended.</p>

---

## Post #7 by @Henry_Cope (2020-05-28 13:14 UTC)

<p>Thank you for the suggestions, I do have a further question regarding “Center Volume”. When you say that it makes “all registrations, segmentations, markups, etc. associated with the volume invalid.” that only applies to the operations already performed on the image correct? If I were to center volume and then try to register,  that would be fine? Also the image I’m trying to center is a segmented piece of a CT scan so that I can highlight it when overlaying it on the original.</p>

---

## Post #8 by @pieper (2020-05-28 13:30 UTC)

<p>Image geometry is described with respect to a frame of reference, so any coordinates or orientations that share the same frame of reference (denoted by <code>FrameOfReferenceUID</code> in the dicom header) can be compared and overlaid with some confidence, modulo patient motion or other issues.  Centering the volume destroys that.  But if you center first, and then use that new coordinate system you should be okay, even if it makes some of us cringe : )</p>

---

## Post #9 by @Henry_Cope (2020-05-28 13:36 UTC)

<p>I apologize for the inadvertent cringe causing. Is there a better way to solve the problem? If I don’t use center volume, the ITK software will be rotating my image around a point 200 mm above where any meaningful data is, making the images I receive from that part blank. Also I’m trying to use transforms to change the rotation of the original image but even when I harden them they don’t appear to take to the .nrrd file. I’d hate to cause some more cringing, but is there a way to alter the rotation parameters of the .nrrd file also?</p>

---

## Post #10 by @lassoan (2020-05-28 13:43 UTC)

<aside class="quote no-group" data-username="pieper" data-post="8" data-topic="11735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>even if it makes some of us cringe : )</p>
</blockquote>
</aside>
<p>Yes, I’m one of those…</p>
<aside class="quote no-group" data-username="Henry_Cope" data-post="9" data-topic="11735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/henry_cope/48/6945_2.png" class="avatar"> Henry_Cope:</div>
<blockquote>
<p>the ITK software will be rotating my image around a point 200 mm above where any meaningful data is</p>
</blockquote>
</aside>
<p>What ITK software? There are lots of ITK transforms, most of them are parametrized so that you can <a href="https://itk.org/Doxygen/html/classitk_1_1MatrixOffsetTransformBase.html#af6a52defb0f9bbb45058b0323a3abdba">specify a center of rotation</a>, regardless of what frame of reference the volume is defined in.</p>

---

## Post #11 by @Henry_Cope (2020-05-28 13:52 UTC)

<p>I’m using the <a href="http://www.openrtk.org/Doxygen/classrtk_1_1JosephForwardProjectionImageFilter.html" rel="nofollow noopener">rtk forward projection</a> program. The parameters it takes are i,j,k axes rotation and x,y translation. You’re correct, I can center my image correctly by adjusting those parameters, but this relies heavily on guess &amp; check, which would need to be repeated whenever I have a new CT.</p>

---

## Post #12 by @lassoan (2020-05-31 16:09 UTC)

<p>Note that for forward projection (DRR generation by raycasting) you may not need RTK, but Slicer’s GPU-accelerated raycaster (volume renderer) should work well. The advantage that it is very fast (can render tens of images per second) and integrated into the application - the only limitation is that it can only create 8-bit image (i.e., the displayed image that you get after dynamic range compression of a 10-12-bit X-ray image).</p>
<p>If you want to use RTK then transforming the volume to the origin makes sense, as RTK does not support 3D positioning of the isocenter (it assumes to be in the origin).</p>
<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="11735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Perhaps in the volume module we should add an ‘add centering transform’ button option.</p>
</blockquote>
</aside>
<p>This is a great idea. We should simply change the centering function so that it crates and applies a transform, but does not harden it. This preserves all information, allows users to apply the same transform to other nodes, and it can be easily undone. I added a ticket to keep track of this idea:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4952">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4952" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4952" target="_blank" rel="noopener">Make volume centering apply a transform</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-05-31" data-time="16:07:36" data-timezone="UTC">04:07PM - 31 May 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-07-31" data-time="05:08:39" data-timezone="UTC">05:08AM - 31 Jul 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          good first issue
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Center volume function (in Volumes module and in Add data/Center option) hardens<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> the centering transform on the volume. It should apply the centering transform but should not harden it so that no information is discarded, the same transform can be applied to other nodes, and the transformation can be undone.

See more information in this discussion: https://discourse.slicer.org/t/volume-rendering-not-centered/11735</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #13 by @Henry_Cope (2020-06-01 14:21 UTC)

<p>Hi all,<br>
Thank you for the many suggestions, however I am still stuck. Centering the volume works great and does exactly what I want it to do. However, when I try to apply a transform and rotate the volume, it doesn’t seem to stick to the .nrrd file even if I harden the transform. Is there a way to permanently rotate the volume?</p>

---

## Post #14 by @cpinter (2020-06-01 14:37 UTC)

<aside class="quote no-group" data-username="Henry_Cope" data-post="13" data-topic="11735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/henry_cope/48/6945_2.png" class="avatar"> Henry_Cope:</div>
<blockquote>
<p>even if I harden the transform</p>
</blockquote>
</aside>
<p>This is how you “permanently” transform a volume. Either there is something you skip from the process or there is a bug. Can you describe the steps you take when hardening? Screenshots help a lot. Thanks!</p>

---

## Post #15 by @Henry_Cope (2020-06-01 15:19 UTC)

<p>Sure can! First I load in my .nrrd file and turn on volume rendering so I can see what I’m working with <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97d87361fe0b8b49e416c00eaeec26a6cc229a59.png" data-download-href="/uploads/short-url/lFhQaVPozslJOrBhluiy4ehIVXX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97d87361fe0b8b49e416c00eaeec26a6cc229a59_2_690x388.png" alt="image" data-base62-sha1="lFhQaVPozslJOrBhluiy4ehIVXX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97d87361fe0b8b49e416c00eaeec26a6cc229a59_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97d87361fe0b8b49e416c00eaeec26a6cc229a59_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97d87361fe0b8b49e416c00eaeec26a6cc229a59_2_1380x776.png 2x" data-dominant-color="B2B4DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1440 318 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Next I switch to the transform module and choose a linear transform to apply. In my case I’m rotating by -90 on the LR axis and 180 on the IS axis. I also select the .nrrd file as my target for the transform.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/2741ef530eb03c510b0cb0b2ebc979f5ce68752c.png" data-download-href="/uploads/short-url/5BhSWj09RahUec1Zbp8w2549pko.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2741ef530eb03c510b0cb0b2ebc979f5ce68752c_2_690x388.png" alt="image" data-base62-sha1="5BhSWj09RahUec1Zbp8w2549pko" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2741ef530eb03c510b0cb0b2ebc979f5ce68752c_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2741ef530eb03c510b0cb0b2ebc979f5ce68752c_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2741ef530eb03c510b0cb0b2ebc979f5ce68752c_2_1380x776.png 2x" data-dominant-color="B0B3DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1440 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Next I click the Harden Transformation button.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5201ea340e7d7c4869b5a8786ee0b591c899d20a.png" data-download-href="/uploads/short-url/bHtfOKGgIVewRTfkJkCiEZ0FSWe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5201ea340e7d7c4869b5a8786ee0b591c899d20a_2_690x388.png" alt="image" data-base62-sha1="bHtfOKGgIVewRTfkJkCiEZ0FSWe" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5201ea340e7d7c4869b5a8786ee0b591c899d20a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5201ea340e7d7c4869b5a8786ee0b591c899d20a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5201ea340e7d7c4869b5a8786ee0b591c899d20a_2_1380x776.png 2x" data-dominant-color="B0B3DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1440 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>… and of course now it works as intended…<br>
It seems that I was not selecting the transform target before clicking on the harden transform button. Whoops</p>

---

## Post #16 by @cpinter (2020-06-01 15:49 UTC)

<p>Great, I’m glad it worked. Yes, you need to select the transformed node and then click the harden button.</p>
<p>If the next time it doesn’t work, then it might be a bug, but we haven’t had problems with this feature lately.</p>

---
