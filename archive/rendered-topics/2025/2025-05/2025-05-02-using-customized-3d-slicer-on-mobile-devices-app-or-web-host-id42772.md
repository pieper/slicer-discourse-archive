---
topic_id: 42772
title: "Using Customized 3D Slicer On Mobile Devices App Or Web Host"
date: 2025-05-02
url: https://discourse.slicer.org/t/42772
---

# Using Customized 3D Slicer on Mobile Devices (App or Web Hosting)

**Topic ID**: 42772
**Date**: 2025-05-02
**URL**: https://discourse.slicer.org/t/using-customized-3d-slicer-on-mobile-devices-app-or-web-hosting/42772

---

## Post #1 by @software (2025-05-02 14:44 UTC)

<p>Hi everyone,</p>
<p>I’ve customized 3D Slicer using the Kitware template and am now exploring the possibility of using this setup on mobile devices, without needing to run the full desktop application on a PC or laptop.</p>
<p>Specifically, I have two main questions:</p>
<ol>
<li><strong>Is it possible to package or run 3D Slicer as a mobile app (Android/iOS)?</strong></li>
<li><strong>Alternatively, can 3D Slicer be hosted (e.g., on a server) and accessed via mobile browsers or lightweight client apps?</strong></li>
</ol>
<p>The goal is to allow users to interact with the customized Slicer features directly on their mobile devices.</p>
<p>Any suggestions or guidance would be greatly appreciated!</p>
<p>Thanks!</p>

---

## Post #2 by @nagy.attila (2025-05-03 15:44 UTC)

<p>Slicer can be run and accessed from the cloud or from a remote desktop solution. You can find descriptions on hot to run it from AWS, for example. You may even be able to access these from a web browser.<br>
A few links (some may be outdated but still may give a hint)</p><aside class="quote quote-modified" data-post="1" data-topic="21431">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/running-slicer-in-a-web-browser-via-amazon-appstreams/21431">Running Slicer in a web browser via Amazon AppStreams</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    At today’s MONAILabel workshop 100+ people could see how amazingly well Slicer works in a web browser using Amazon AppStream. For those who missed, here is a short demo: 

  <a href="https://www.youtube.com/watch?v=u3t5twSV6NE" target="_blank" rel="noopener nofollow ugc">
    [3D Slicer in a web browser - using Amazon AppStream]
  </a>


Questions are already coming in if this is generally available and about how this can be set up. <a class="mention" href="/u/pieper">@pieper</a> can you answer this question or ask someone from AWS to answer here?
  </blockquote>
</aside>
<aside class="quote" data-post="1" data-topic="11659">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lennymartinez/48/6918_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/install-slicer-on-aws-ec2-instance/11659">Install Slicer on AWS EC2 instance</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Anybody have experience installing Slicer on an AWS EC2 instance? I want to be able to send folders of Dicom images to be processed by a Slicer plugin (already made) in an EC2 instance but I’m not sure what the best way of going about this would be.
  </blockquote>
</aside>
<aside class="quote" data-post="1" data-topic="24649">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/mza/48/16225_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/best-easiest-web-service-to-run-3d-slicer/24649">Best &amp; easiest web service to run 3d slicer.</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi everyone, 
What is the easiest appstream or cloud web service I can use to run 3d slicer 5.0.3 for segmentation (files with extension .seg.nrrd &amp; .nii). My laptop cannot run versions beyond 4.8.1 and the segmentation files I have are not working on this version. 
I am asking the (easiest) because I am not an expert, I just want to run version 5.0.3. 
Any advice. 
Thanks in advance.
  </blockquote>
</aside>

<p>Porting Slicer to ARM64 is under way, but going one step even further and compiling it for a mobile OS is a totally different league. Not easily doable at all, but it of course depends on the resources <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
A few pages that may give you a hint on this topic:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/BuildsOfSlicerForArmBasedSystemsMacAndLinux/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/BuildsOfSlicerForArmBasedSystemsMacAndLinux/" target="_blank" rel="noopener nofollow ugc">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/BuildsOfSlicerForArmBasedSystemsMacAndLinux/" target="_blank" rel="noopener nofollow ugc">Project Description</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/SlicerOnAndroid/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/SlicerOnAndroid/" target="_blank" rel="noopener nofollow ugc">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/SlicerOnAndroid/" target="_blank" rel="noopener nofollow ugc">NA-MIC Project Weeks</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/ITKForAndroidProj/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/ITKForAndroidProj/" target="_blank" rel="noopener nofollow ugc">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/ITKForAndroidProj/" target="_blank" rel="noopener nofollow ugc">Project Description</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Edit: there is a VTK repo for Android, that may come handy too:</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/blueebrain/VTKAndroid">
  <header class="source">

      <a href="https://github.com/blueebrain/VTKAndroid" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/a0a548498f924701a85f1f0df61a6137/blueebrain/VTKAndroid" class="thumbnail">

  <h3><a href="https://github.com/blueebrain/VTKAndroid" target="_blank" rel="noopener nofollow ugc">GitHub - blueebrain/VTKAndroid</a></h3>

    <p><span class="github-repo-description">Contribute to blueebrain/VTKAndroid development by creating an account on GitHub.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
via:</p><aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/i-want-to-publish-vtk-to-android-qt-quick/14060/16">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/i-want-to-publish-vtk-to-android-qt-quick/14060/16" target="_blank" rel="noopener nofollow ugc" title="10:06AM - 15 July 2024">VTK – 15 Jul 24</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/i-want-to-publish-vtk-to-android-qt-quick/14060/16" target="_blank" rel="noopener nofollow ugc">I want to publish VTK to Android (Qt Quick)</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #F7941D;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Support</span>
        </span>
      </span>
  </div>
</div>

  <p>this MR should fix Volume Rendering for VTK with GLES indeed, should it be WASM or mobile platforms.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope this helps,<br>
Attila</p>

---

## Post #3 by @finetjul (2025-05-04 20:52 UTC)

<p>You might also want to consider <a href="https://github.com/KitwareMedical/trame-slicer" rel="noopener nofollow ugc">trame-slicer</a>.</p>
<p>We are still (as of spring 2025) ironing things out and will eventually communicate more about it.</p>
<p>Some didn’t wait and have already started using it.</p>

---
