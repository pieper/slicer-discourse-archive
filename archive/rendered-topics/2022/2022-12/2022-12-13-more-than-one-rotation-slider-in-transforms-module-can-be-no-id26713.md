# More than one rotation slider in transforms module can be non-zero

**Topic ID**: 26713
**Date**: 2022-12-13
**URL**: https://discourse.slicer.org/t/more-than-one-rotation-slider-in-transforms-module-can-be-non-zero/26713

---

## Post #1 by @jamesobutler (2022-12-13 15:35 UTC)

<p>As mentioned in the below comment in another thread,</p><aside class="quote" data-post="2" data-topic="11091">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/bug-in-transforms-module/11091/2">Bug in Transforms module</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Thanks for letting us know. This is the intended behavior - only one slider can be at non-zero position at a time (with only one exception). See explanation in Transform’s module documentation’s <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_editing_and_application" rel="noopener nofollow ugc">Transform editing and application</a> section. Let us know if something is not clear.
  </blockquote>
</aside>

<p>and according to the Transforms module documentation regarding <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#edit" rel="noopener nofollow ugc">editing</a>:</p>
<blockquote>
<p>Note: Linear transform edit sliders only show relative translation and rotation because a transformation can be achieved using many different series of transforms. To make this clear to users, only one transform slider can be non-zero at a time (all previously modified sliders are reset to 0 when a slider is moved). The only exception is translation sliders in “translate first” mode (i.e., when translation in global/local coordinate system button is not depressed): in this case there is a only one way how a specific translation can be achieved, therefore transform sliders are not reset to 0.</p>
</blockquote>
<p>there should only be one slider with a non-zero position at a time. However, using latest stable Slicer 5.2.1, I’m observing that I can cause more than 1 slider to be non-zero. Moving the sliders will reset the other, but if I insert in the rotation with the spinbox, that resetting behavior seems to no longer work. Is this a bug?</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bc3c24147ebfa698a291e67f31a635ff028381a.mp4">
  </div><p></p>
<p>Related threads on transform sliders behavior:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/bug-in-transforms-module/11091" class="inline-onebox">Bug in Transforms module</a></li>
<li><a href="https://discourse.slicer.org/t/is-the-rotation-of-the-3d-slicers-transform-module-euler-or-quaternion/11944" class="inline-onebox">Is the rotation of the 3D Slicer's Transform module Euler or Quaternion?</a></li>
<li><a href="https://discourse.slicer.org/t/reformat-module-values-not-resetting/15873" class="inline-onebox">Reformat module Values not resetting</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-doesnt-show-rotation-slider-value-corresponding-to-a-transform-after-rotation-axis-is-not-cannonical/23943" class="inline-onebox">Slicer doesn't show rotation slider value corresponding to a transform after rotation axis is not cannonical</a></li>
</ul>

---

## Post #2 by @pieper (2022-12-13 18:18 UTC)

<p>Yes, sounds like a bug to me.</p>

---

## Post #3 by @jamesobutler (2022-12-14 15:57 UTC)

<p>This issue is being tracked at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6735">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6735" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6735" target="_blank" rel="noopener nofollow ugc">More than one rotation slider in transforms module can be non-zero</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-12-14" data-time="15:25:30" data-timezone="UTC">03:25PM - 14 Dec 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

Originally mentioned at https://discourse.slicer.org/t/more-than-o<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ne-rotation-slider-in-transforms-module-can-be-non-zero/26713

## Steps to reproduce

1. Go to Transforms module and add a new linear transform node
2. Change the LR, PA, IS slider value and observe that upon changing one it resets the others
3. Change the LR. PA, IS spinbox values directly and observe that more than one rotation slider can be non-zero
4. Change the LR, PA, IS slider value and observe that more than one rotation slider can be non-zero.


https://user-images.githubusercontent.com/15837524/207636840-7c4541a7-cc8f-4c7c-b371-72d17fd7cbdc.mp4


## Expected behavior

Only one rotation slider can be non zero (as according to the Slicer documentation)

https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#edit

&gt; Note: Linear transform edit sliders only show relative translation and rotation because a transformation can be achieved using many different series of transforms. To make this clear to users, only one transform slider can be non-zero at a time (all previously modified sliders are reset to 0 when a slider is moved). The only exception is translation sliders in “translate first” mode (i.e., when translation in global/local coordinate system button is not depressed): in this case there is a only one way how a specific translation can be achieved, therefore transform sliders are not reset to 0.

## Environment
- Slicer version: Slicer-5.2.1
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
