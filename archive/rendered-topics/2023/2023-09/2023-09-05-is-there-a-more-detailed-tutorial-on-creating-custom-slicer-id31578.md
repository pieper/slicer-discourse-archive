---
topic_id: 31578
title: "Is There A More Detailed Tutorial On Creating Custom Slicer"
date: 2023-09-05
url: https://discourse.slicer.org/t/31578
---

# Is there a more detailed tutorial on creating custom slicer application?

**Topic ID**: 31578
**Date**: 2023-09-05
**URL**: https://discourse.slicer.org/t/is-there-a-more-detailed-tutorial-on-creating-custom-slicer-application/31578

---

## Post #1 by @iwangwangwang (2023-09-05 19:19 UTC)

<p>The examples provided on the official website are not detailed enough and hard to learn for me,<br>
so Is there a more detailed tutorial on creating custom slicer application? step by step tutorial and examples, video tutorial will be more better!</p>

---

## Post #2 by @moraleda (2023-09-06 11:15 UTC)

<p>There are some on youtube. For example this one:</p><div class="youtube-onebox lazy-video-container" data-video-id="zutiQtp90vU" data-video-title="How to create a new custom module -- Develop 3D Slicer Extension Tutorial #01" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=zutiQtp90vU" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/zutiQtp90vU/maxresdefault.jpg" title="How to create a new custom module -- Develop 3D Slicer Extension Tutorial #01" width="" height="">
  </a>
</div>


---

## Post #3 by @cpinter (2023-09-06 11:23 UTC)

<p>As far as I know there are no tutorials.<br>
<a class="mention" href="/u/moraleda">@moraleda</a> the video you linked is about creating an extension, which is different than the question was.</p>
<p><a class="mention" href="/u/iwangwangwang">@iwangwangwang</a> You need to follow the steps to create a Slicer custom app skeleton from the template</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/KitwareMedical/SlicerCustomAppTemplate">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/0e4285a6c416a969673326b03eaa5a971fed378010f27b0512fc4a0cd17367be/KitwareMedical/SlicerCustomAppTemplate" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" target="_blank" rel="noopener">GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a...</a></h3>

  <p>Template to be used as a starting point for creating a custom 3D Slicer application - GitHub - KitwareMedical/SlicerCustomAppTemplate: Template to be used as a starting point for creating a custom ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Then you need to build it just as a Slicer build. You need to add your own modules to the source tree in <code>Modules/</code> and add them to the main <code>CMakeLists.txt</code> file. Those modules will then be part of your application. You have all the freedom customizing the app, by hiding the toolbar etc.</p>

---

## Post #4 by @Sam_Horvath (2023-09-06 21:49 UTC)

<p>We have two blogs on the topic: <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a></p>
<p>and</p>
<p><a href="https://www.kitware.com/slicercat-and-python-creating-custom-slicer-applications-with-qt-stylesheets/" class="onebox" target="_blank" rel="noopener">https://www.kitware.com/slicercat-and-python-creating-custom-slicer-applications-with-qt-stylesheets/</a></p>

---
