# Scale Factor not loading image correctly when trying to save a volume rendering photograph

**Topic ID**: 40184
**Date**: 2024-11-13
**URL**: https://discourse.slicer.org/t/scale-factor-not-loading-image-correctly-when-trying-to-save-a-volume-rendering-photograph/40184

---

## Post #1 by @Tatiana_Egbert (2024-11-13 21:55 UTC)

<p>When trying to increase the scale factor to obtain a higher resolution volume rendering photograph, any scale factor above 1.0 will alter the image itself and overlap my volume rendering image onto itself and save incorrectly, not sure how to go about fixing this issue. I have restarted the program and even re-downloaded it.</p>

---

## Post #2 by @muratmaga (2024-11-13 22:22 UTC)

<p>please see this thread:</p><aside class="quote" data-post="2" data-topic="40178">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/scale-factor-on-images-taken-from-a-scene-not-working/40178/2">Scale factor on images taken from a scene not working</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    That functionality is broken. Please use the HiResScreenCapture module in SlicerMorph instead. 
See the tutorial: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/HiResScreenCapture" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/HiResScreenCapture at main · SlicerMorph/Tutorials · GitHub</a>
  </blockquote>
</aside>


---
