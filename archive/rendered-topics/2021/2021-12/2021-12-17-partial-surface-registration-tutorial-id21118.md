# Partial Surface Registration Tutorial

**Topic ID**: 21118
**Date**: 2021-12-17
**URL**: https://discourse.slicer.org/t/partial-surface-registration-tutorial/21118

---

## Post #1 by @mau_igna_06 (2021-12-17 16:40 UTC)

<p>Hi devs.</p>
<p>I have made a tutorial for Partial Surface Registration, something similar to weight-painting ICP that is done in Blender.</p>
<p>Here you can access it:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1Eiokb2aXohKGcyxVn42f7diF_u8Il_LH/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1Eiokb2aXohKGcyxVn42f7diF_u8Il_LH/view?usp=sharing" target="_blank" rel="noopener">drive.google.com</a>
  </header>

  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://lh6.googleusercontent.com/bYIs94hBzrgLmD8eM8LE25UfVB8cLhBZPHnqTrJ9Sv5BhlyDbcaBgZrkdvscp7YXrgI=w1200-h630-p" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://drive.google.com/file/d/1Eiokb2aXohKGcyxVn42f7diF_u8Il_LH/view?usp=sharing" target="_blank" rel="noopener">PartialSurfaceRegistrationV2.mp4 (video)</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If there are no suggestions for corrections I’ll later upload it to Youtube.</p>
<p>Mauro</p>

---

## Post #2 by @mikebind (2021-12-17 17:53 UTC)

<p>I think this looks good. I was able to follow the process and fully understand it after watching it twice.</p>
<p>A question I have is what is the primary motivation for partial surface registration (vs other registration options)?  I can imagine a few possible use cases:</p>
<ul>
<li>Maybe partial surface registration is much faster to when full model to full model registration is prohibitively slow?</li>
<li>Maybe you are trying to align a particular region in order to look at differences in another region, so a full registration which tried to align everything would be counterproductive</li>
<li>Maybe regions you are trying to align do not have clear landmarks (like the smooth section of bone you chose)</li>
</ul>
<p>Any other reasons someone should think of partial surface registration when trying to solve a problem?</p>
<p>Are there any caveats to the method or things people should keep in mind when choosing regions?  Perhaps a trade-off in size of chosen region vs registration time?  Are disconnected regions OK or must the regions to be registered be a single connected region?</p>
<p>Many Slicer tutorial videos do not address these broader questions (I assume to focus on brevity), so I don’t think you need to either, but these are a couple of things I wondered about after watching and which aren’t addressed.</p>
<p>Thanks for making the video demonstration tutorial, these kinds of videos are very helpful in learning how to do things in Slicer!!</p>

---

## Post #3 by @mau_igna_06 (2021-12-17 18:06 UTC)

<p>Hi Mike.</p>
<p>Thanks for the feedback.</p>
<blockquote>
<p>A question I have is what is the primary motivation for partial surface registration (vs other registration options)?</p>
</blockquote>
<p>I think this is the main reason:</p>
<blockquote>
<p>Maybe you are trying to align a particular region in order to look at differences in another region, so a full registration which tried to align everything would be counterproductive</p>
</blockquote>
<blockquote>
<p>Are there any caveats to the method or things people should keep in mind when choosing regions?</p>
</blockquote>
<p>I would choose a little bit of a well-matched region to work as pivot, and then the rest of the selection would be badly matched parts. The idea in my mind is trying to set up a context that would push or rotate the moving-model to the correct place considering points of both models will try to be as close as possible as they can. For a deeper idea of this, I think you should study how the algorithm works, I think I just have a general idea of it.</p>
<blockquote>
<p>Are disconnected regions OK or must the regions to be registered be a single connected region?</p>
</blockquote>
<p>I think there is no constraint that obligates you to use a single connected region.</p>

---

## Post #4 by @mau_igna_06 (2022-02-24 20:25 UTC)

<div class="youtube-onebox lazy-video-container" data-video-id="i7gDZP1Zdx4" data-video-title="Partial Surface Registration on Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=i7gDZP1Zdx4" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/i7gDZP1Zdx4/maxresdefault.jpg" title="Partial Surface Registration on Slicer" width="" height="">
  </a>
</div>

<p>This videotutorial show how to make a rigid registration of two models corresponding to the same anatomy on different subjects so that the selected region of one model matchs a similar region on the other model (no entire model matching is done, only region of interest is accounted for registration)</p>
<p>First an approximate registration is done with PointToPoint registration.<br>
Then the selected part of one of the models is used for ICP resulting on similar regions matching/overlapping.</p>
<p>Workflow developed ad-honorem by Mauro I. Dominguez</p>

---

## Post #5 by @Ruida_Cheng (2025-03-07 08:44 UTC)

<p>Hi, Mauro.   Fiducial Registration Wizard. Is this Wizard from SlicerIGT?<br>
How do you load the two tibia bone surfaces from the 3D Slicer GUI interface? Do you have the two tibia bones 3D models that I can try it out?  Thank.</p>

---

## Post #6 by @mau_igna_06 (2025-03-11 12:42 UTC)

<p>Hi</p>
<blockquote>
<p>Fiducial Registration Wizard. Is this Wizard from SlicerIGT?</p>
</blockquote>
<p>Yes, “Fiducial Registration Wizard” and “Model Registration” modules are from the “SlicerIGT” extension</p>
<blockquote>
<p>How do you load the two tibia bone surfaces from the 3D Slicer GUI interface?</p>
</blockquote>
<p>You load them with the button shown on the left of picture below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13ac530a3d5a5b35f70c5084ed8e3f116dd9a50f.png" data-download-href="/uploads/short-url/2O2h3U3M1Lz4oHQivUkAJvRSCTB.png?dl=1" title="Screenshot from 2025-03-11 09-38-32_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ac530a3d5a5b35f70c5084ed8e3f116dd9a50f_2_690x390.png" alt="Screenshot from 2025-03-11 09-38-32_2" data-base62-sha1="2O2h3U3M1Lz4oHQivUkAJvRSCTB" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ac530a3d5a5b35f70c5084ed8e3f116dd9a50f_2_690x390.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ac530a3d5a5b35f70c5084ed8e3f116dd9a50f_2_1035x585.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ac530a3d5a5b35f70c5084ed8e3f116dd9a50f_2_1380x780.png 2x" data-dominant-color="56555D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-03-11 09-38-32_2</span><span class="informations">2484×1405 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here are <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#models" rel="noopener nofollow ugc">3D model formats that Slicer supports</a></p>
<blockquote>
<p>Do you have the two tibia bones 3D models that I can try it out?</p>
</blockquote>
<p>I don’t, sorry</p>
<p>HIH<br>
Mauro</p>

---
