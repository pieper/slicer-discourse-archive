# Modify other segments:

**Topic ID**: 19568
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/modify-other-segments/19568

---

## Post #1 by @franbuemi (2021-09-08 13:02 UTC)

<p>Hi everyone. I am trying to segment a liver following a tutorial. I cannot prevent to remove other segmentations every time I try to overwrite them…in the new 3d slicer version, in “modify other segments” “none” has been removed. Even trying “allow overlap” I cannot solve this issue. How can I fix it?</p>

---

## Post #2 by @lassoan (2021-09-08 14:18 UTC)

<p>“Allow overlap” will prevent overwriting other segments when you are painting into a segment. Please provide a screen video recording (or detailed description of all the steps with screenshots) to show what you do exactly, what you expect to happen, and what happens instead.</p>

---

## Post #3 by @franbuemi (2021-09-10 07:56 UTC)

<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34d2dd60edb8827be4016f6a487e29e2a237f369.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34d2dd60edb8827be4016f6a487e29e2a237f369.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34d2dd60edb8827be4016f6a487e29e2a237f369.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #4 by @lassoan (2021-09-10 19:13 UTC)

<p>Thank you, the video was very useful. You did everything right, the masking settings were correct- the liver segment should not have been changed when you painted the vein. I could not reproduce the issue with the same Slicer version or with the latest Slicer Preview Release, so something must be special in your scene.</p>
<p>There have been fixes in masking settings recently, so before we go any further with the investigation, please try if you can reproduce the issue in the very latest Slicer Preview Release.</p>

---

## Post #5 by @franbuemi (2021-09-10 21:28 UTC)

<p>Thank you very much for your answer! I will try the Slicer preview release as you have suggested. I made the liver segmention with the AI assisted segmentation tool. I do know if this can be useful to explain this issue.</p>

---

## Post #6 by @lassoan (2021-09-10 23:19 UTC)

<aside class="quote no-group" data-username="franbuemi" data-post="5" data-topic="19568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/franbuemi/48/67915_2.png" class="avatar"> franbuemi:</div>
<blockquote>
<p>I made the liver segmention with the AI assisted segmentation tool. I do know if this can be useful to explain this issue.</p>
</blockquote>
</aside>
<p>I’ve segmented a liver CT using AIAA extension using the latest Slicer Preview Release and everything worked well for me.</p>

---

## Post #7 by @franbuemi (2021-09-14 07:45 UTC)

<p>I’ve tried the preview release today. Same issue <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=10" title=":thinking:" class="emoji" alt=":thinking:"> I do know what to do.</p>

---
