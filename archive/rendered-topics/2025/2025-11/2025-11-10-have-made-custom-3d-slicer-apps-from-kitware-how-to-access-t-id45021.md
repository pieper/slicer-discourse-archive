# Have Made Custom 3D Slicer Apps from Kitware – How to Access Them via Web Browser?

**Topic ID**: 45021
**Date**: 2025-11-10
**URL**: https://discourse.slicer.org/t/have-made-custom-3d-slicer-apps-from-kitware-how-to-access-them-via-web-browser/45021

---

## Post #1 by @software (2025-11-10 11:32 UTC)

<p>Hi everyone,</p>
<p>I have created some <strong>custom 3D Slicer apps</strong> using Kitware’s platform, and now I want to access them through a <strong>web browser</strong>.</p>
<p>I’m looking for the <strong>easiest technique</strong> or approach to do this. Should I use a specific server setup, web deployment tool, or something like Jupyter/VTK.js?</p>
<p>Any guidance, tutorials, or examples would be greatly appreciated!</p>

---

## Post #2 by @ebrahim (2025-11-10 14:31 UTC)

<p>Not sure if this is the easiest or if it still works, but folks have looked at using Amazon Appstream; you can check out these posts:</p>
<aside class="quote quote-modified" data-post="1" data-topic="21431">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/running-slicer-in-a-web-browser-via-amazon-appstreams/21431">Running Slicer in a web browser via Amazon AppStreams</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    At today’s MONAILabel workshop 100+ people could see how amazingly well Slicer works in a web browser using Amazon AppStream. For those who missed, here is a short demo: 

  <a href="https://www.youtube.com/watch?v=u3t5twSV6NE" target="_blank" rel="noopener nofollow ugc">
    [3D Slicer in a web browser - using Amazon AppStream]
  </a>


Questions are already coming in if this is generally available and about how this can be set up. <a class="mention" href="/u/pieper">@pieper</a> can you answer this question or ask someone from AWS to answer here?
  </blockquote>
</aside>

<aside class="quote" data-post="1" data-topic="24649">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/mza/48/16225_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/best-easiest-web-service-to-run-3d-slicer/24649">Best &amp; easiest web service to run 3d slicer.</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Hi everyone, 
What is the easiest appstream or cloud web service I can use to run 3d slicer 5.0.3 for segmentation (files with extension .seg.nrrd &amp; .nii). My laptop cannot run versions beyond 4.8.1 and the segmentation files I have are not working on this version. 
I am asking the (easiest) because I am not an expert, I just want to run version 5.0.3. 
Any advice. 
Thanks in advance.
  </blockquote>
</aside>


---
