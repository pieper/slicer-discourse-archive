# Why does 3D model flip from other views? 

**Topic ID**: 28615
**Date**: 2023-03-28
**URL**: https://discourse.slicer.org/t/why-does-3d-model-flip-from-other-views/28615

---

## Post #1 by @Jed (2023-03-28 11:23 UTC)

<p>while using 4 up views, the 3D view is opposite. The 3D view has to be flipped to match.<br>
looking at axial. item is on the left, in 3D it’s on the right. The only way I got it to look right was to flip the picture. I have a pic to demonstrate, how do I share it?</p>

---

## Post #2 by @Jed (2023-03-28 11:26 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b3410ac95470dcb7f7047dff18e74284055e2f0.jpeg" data-download-href="/uploads/short-url/aJhmhdqQyOWsMk2Y3gJnD3u8wow.jpeg?dl=1" title="F1 on" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b3410ac95470dcb7f7047dff18e74284055e2f0_2_690x420.jpeg" alt="F1 on" data-base62-sha1="aJhmhdqQyOWsMk2Y3gJnD3u8wow" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b3410ac95470dcb7f7047dff18e74284055e2f0_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b3410ac95470dcb7f7047dff18e74284055e2f0_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b3410ac95470dcb7f7047dff18e74284055e2f0_2_1380x840.jpeg 2x" data-dominant-color="5B595F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">F1 on</span><span class="informations">1389×847 85.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried everything, I had to photo cut and flip 3D version, P is backwards.</p>

---

## Post #3 by @lassoan (2023-03-28 11:31 UTC)

<p>Please zoom out a bit and enable orientation marker display on all views so that we can see if the view orientations are correct.</p>
<p>What kind of files have you loaded the image from? If you loaded DICOM images: have you used the DICOM module?</p>

---

## Post #4 by @Jed (2023-03-28 15:08 UTC)

<p>The marker is active it don’t matter zoom in or out</p>

---

## Post #5 by @Jed (2023-03-28 15:29 UTC)

<p>You can see they are mirrored</p>

---

## Post #6 by @pieper (2023-03-28 17:54 UTC)

<p>In the 3D view you are looking at the bone from above (from the head to the toes).  The radiology convention used in the slice views is to look from the toes toward the head.  You can tell this by looking at the letters: S for Superior (head), I for Inferior (toes).</p>

---

## Post #7 by @lassoan (2023-03-28 19:01 UTC)

<p>I mean to zoom out the 3D view and enable orientation markers on all views like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2415bb6bafb7b72baa9c977fc776f14ba9f4b0b5.jpeg" data-download-href="/uploads/short-url/59dKu7tfLQ1JdNpbq3Y03iyy0Sh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2415bb6bafb7b72baa9c977fc776f14ba9f4b0b5_2_690x425.jpeg" alt="image" data-base62-sha1="59dKu7tfLQ1JdNpbq3Y03iyy0Sh" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2415bb6bafb7b72baa9c977fc776f14ba9f4b0b5_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2415bb6bafb7b72baa9c977fc776f14ba9f4b0b5_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2415bb6bafb7b72baa9c977fc776f14ba9f4b0b5_2_1380x850.jpeg 2x" data-dominant-color="6C6B75"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1184 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Based on what I see in your image it all looks good: images are shown according to radiology convention that are used on nearly all image viewers.</p>
<p>What image viewers you are referring to when you say that the orientation is flipped? Would you like to see differently oriented views of the data (that’s not a problem, you can choose your view orientations any way you want) or you find that the orientation markers are not consistent with the displayed content (which is a data import problem that must be fixed)?</p>

---

## Post #8 by @Jed (2023-03-29 09:15 UTC)

<p>It just didn’t make sense, you can’t see the screw in 3D unless you look from the top.<br>
Being the 3D view is not normally used should the views line up accordingly?<br>
I can 3ad print my CT scans how common is that?<br>
I did not know about the direction the scans were lucked up to the head.<br>
I like this program, I am permanently disabled, I am good with scans.<br>
I merged a MRI and a CT scan to show the disc, spinal canal, and some nerves.<br>
Crashed my hard drive trying to process it.<br>
What company 3D prints information?</p>

---

## Post #9 by @pieper (2023-03-29 18:26 UTC)

<aside class="quote no-group" data-username="Jed" data-post="8" data-topic="28615">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/34f0e0/48.png" class="avatar"> Jed:</div>
<blockquote>
<p>It just didn’t make sense, you can’t see the screw in 3D unless you look from the top.<br>
Being the 3D view is not normally used should the views line up accordingly?</p>
</blockquote>
</aside>
<p>If you show the Slice in the 3D view using <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">the “Show in 3D” button here</a> and rotate the 3D view it should help you better see the relationship.</p>
<p>You can probably 3D print this data, but sometimes the volume rendering like you have already is more informative.  To 3D print you can start <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">with segmentation</a> and save in a format compatible with 3D printing services.  I don’t do it myself and don’t have any suggestions, but I know they are readily avalable.</p>

---

## Post #10 by @Jed (2023-03-30 02:43 UTC)

<p>Any suggestions to where I may find employment converting scans into models. I have a knack using slicer, background in machine shops.<br>
Just curious if there is a place to seek employment with this.<br>
Thank you for your time</p>

---

## Post #11 by @lassoan (2023-03-30 12:22 UTC)

<p>Converting scans into models is done by segmenting the image. It is increasingly performed fully automatically by “AI” tools. Manual segmentation is still done either for one-off cases that are too difficult for automatic methods, for segmentation tasks that are rarely done so that no automatic tool exists, or for creating reliable training data for machine learning. All these are not very stable source of income, as they are either rare cases or you get paid very low wages (manual training data generation is often outsourced to very low cost countries).</p>
<p>You can make better use of your image segmentation expertise if you combine it with other skills, such as computing skills (so that you can train your own AI segmentation tools), artistic skills (so that you can create personalized 3D printed souvenirs), etc.</p>

---

## Post #12 by @Dang_Minh_Hieu (2024-11-14 07:40 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Why in Stable release and Preview, image will display differently, they are reversed<br>
Stable Release<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9128d6ccb5b54e4ea9b430b88f850f668d4babde.jpeg" data-download-href="/uploads/short-url/kI8Ji2BZySDStQbSJwSYZOC1jOu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9128d6ccb5b54e4ea9b430b88f850f668d4babde_2_690x363.jpeg" alt="image" data-base62-sha1="kI8Ji2BZySDStQbSJwSYZOC1jOu" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9128d6ccb5b54e4ea9b430b88f850f668d4babde_2_690x363.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9128d6ccb5b54e4ea9b430b88f850f668d4babde_2_1035x544.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9128d6ccb5b54e4ea9b430b88f850f668d4babde_2_1380x726.jpeg 2x" data-dominant-color="8A8A91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1011 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Preview release<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a6ddc22cee532eccee995642a68772d06aafa99.jpeg" data-download-href="/uploads/short-url/1ug9cI2JW9IgmudP3ReMUQAwmuZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a6ddc22cee532eccee995642a68772d06aafa99_2_690x356.jpeg" alt="image" data-base62-sha1="1ug9cI2JW9IgmudP3ReMUQAwmuZ" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a6ddc22cee532eccee995642a68772d06aafa99_2_690x356.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a6ddc22cee532eccee995642a68772d06aafa99_2_1035x534.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a6ddc22cee532eccee995642a68772d06aafa99_2_1380x712.jpeg 2x" data-dominant-color="7A787C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1891×977 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2024-11-14 12:45 UTC)

<p>Probably this was the issue in the stable release that got fixed in the preview release:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7987">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7987" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7987" target="_blank" rel="noopener">BUG: Regression for scans with negative spacing in DICOM</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>pieper:7937-dicom-regression</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-10-08" data-time="20:22:15" data-timezone="UTC">08:22PM - 08 Oct 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7987/files" target="_blank" rel="noopener">
            <span class="added">+1</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes #7937

See original report here about a dataset being scrambled that loa<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7987" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ded well in the 5.6.2 release:

https://discourse.slicer.org/t/regression-in-the-dicom-data-base/37913

This corresponds to the change in behavior described here, where spacing from ITK that used to be 1 is now, for example 5 or -1:

* https://github.com/InsightSoftwareConsortium/ITK/issues/4794

Which is believed to be due to the changes here, which was added so that for Secondary Capture files the spacing would be respected if present:

* https://github.com/InsightSoftwareConsortium/ITK/pull/4521

However adding this code in GDCM meant that if the SpacingBetweenSlices tag is present, even in a CT, it is being used by ITK to calculate spacing, and also ITKToRAS transforms when trying to orthogonalize the transform.

Since Slicer doesn't rely on orthogonal IJKToRAS transforms, this change tells ITK to skip that step and instead it relies on the positions and orientations of the slices to calculate the IJKToRAS transform, which is compatible with what Slicer expects.

This code was tested on both the CT scan with the negative spacing that was reported in the original issue, and on other CT cans without that tag and the geometry matches what was obtained in 5.6.2.

This change was discussed in the Slicer developer meeting 2024-10-08 and determined to be the best course of action.  Further fixes in GDCM or ITK were not pursued because it was unclear whta the correct behavior should be at the library level considering that a negative spacing between slices is technically invalid for CT scans according to the DICOM standard.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
