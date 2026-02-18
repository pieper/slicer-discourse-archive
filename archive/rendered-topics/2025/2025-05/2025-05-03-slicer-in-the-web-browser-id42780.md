# Slicer in the web browser

**Topic ID**: 42780
**Date**: 2025-05-03
**URL**: https://discourse.slicer.org/t/slicer-in-the-web-browser/42780

---

## Post #1 by @MikeSala (2025-05-03 15:08 UTC)

<p>Hi everyone,</p>
<p>I’d like to ask you a quick question, if I may. I’d be extremely grateful if you could point me in the right direction.</p>
<p>Here’s my current workflow: I segment organs using 3D Slicer, then export the .obj files and upload them to Sketchfab. This setup allows surgeons to visualize the 3D models in the OR with nothing more than an internet connection—no software installation required. It’s intuitive, and our clients love it.<br>
Here’s an example: <a href="https://sketchfab.com/3d-models/lst1120251-235cdc10793a4292a59564856d07be5f" class="inline-onebox" rel="noopener nofollow ugc">LST1120251 - Download Free 3D model by SurgiPrint [235cdc1] - Sketchfab</a></p>
<p>The issue is that Sketchfab doesn’t allow me to adjust opacity or toggle structures on and off.</p>
<p>I’m therefore looking for a web-based alternative to 3D Slicer, or any similar tool, that would allow users to interact with the models (adjust opacity, isolate structures, etc.)—without requiring any installation.</p>
<p>I hope I’ve explained my situation clearly.<br>
Thank you very much in advance for your help!</p>
<p>Dr. Mike Salavracos (radiologist)</p>

---

## Post #2 by @nagy.attila (2025-05-03 15:56 UTC)

<p>There is a similar topic, and you may find some relevant links in the post I posted there.<br>
You can run Slicer remotely, either from the cloud and access it in a browser, or from a desktop PC via some remote desktop solution.</p><aside class="quote quote-modified" data-post="1" data-topic="42772">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/software/48/79627_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/using-customized-3d-slicer-on-mobile-devices-app-or-web-hosting/42772">Using Customized 3D Slicer on Mobile Devices (App or Web Hosting)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi everyone, 
I’ve customized 3D Slicer using the Kitware template and am now exploring the possibility of using this setup on mobile devices, without needing to run the full desktop application on a PC or laptop. 
Specifically, I have two main questions: 

Is it possible to package or run 3D Slicer as a mobile app (Android/iOS)?
Alternatively, can 3D Slicer be hosted (e.g., on a server) and accessed via mobile browsers or lightweight client apps?

The goal is to allow users to interact with the…
  </blockquote>
</aside>

<p>Best,<br>
Attila</p>

---

## Post #3 by @cpinter (2025-05-06 11:27 UTC)

<p>You can export a set of models to GLTF, and then view them online, see</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/PerkLab/SlicerOpenAnatomy/tree/master/OpenAnatomyExport">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/PerkLab/SlicerOpenAnatomy/tree/master/OpenAnatomyExport" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/PerkLab/SlicerOpenAnatomy/tree/master/OpenAnatomyExport" target="_blank" rel="noopener">SlicerOpenAnatomy/OpenAnatomyExport at master · PerkLab/SlicerOpenAnatomy</a></h3>


  <p><span class="label1">3D Slicer extension for exporting Slicer scenes to use in the OpenAnatomy.org browser - PerkLab/SlicerOpenAnatomy</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
