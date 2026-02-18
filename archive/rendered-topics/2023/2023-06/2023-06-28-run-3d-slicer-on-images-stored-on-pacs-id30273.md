# Run 3D Slicer on images stored on PACS

**Topic ID**: 30273
**Date**: 2023-06-28
**URL**: https://discourse.slicer.org/t/run-3d-slicer-on-images-stored-on-pacs/30273

---

## Post #1 by @mazurkin.daniel (2023-06-28 08:00 UTC)

<p>Hello, how can I make it so that when launching 3D Slicer, it opens an application with research from the PACS server? What extensions are available for this? Currently, we have only found the Sandbox extension. What arguments do we need to pass using the Sandbox extension?</p>

---

## Post #2 by @lassoan (2023-06-28 14:20 UTC)

<p>If the PACS supports DICOMweb protocol then you can use the DICOMwebBrowser extension for this (you can choose that module as startup module or use the startup script to show it at startup).</p>
<p>If the PACS only supports classic DIMSE networking (C-FIND, C-MOVE, C-GET) then you can use the DICOM module to query/retrieve images (in DICOM networking / Query and retrieve).</p>
<p>We are also working on a new-generation visual DICOM browser that will automatically query and retrieve thumbnails from the PACS and show remote and locally cached results together. It will be available around September.</p>

---

## Post #3 by @mazurkin (2023-06-29 01:54 UTC)

<p>Thank you for reply <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @ebrahim (2023-07-04 14:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="30273">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We are also working on a new-generation visual DICOM browser that will automatically query and retrieve thumbnails from the PACS and show remote and locally cached results together. It will be available around September.</p>
</blockquote>
</aside>
<p>This is very interesting! Is there any place where I can learn more about these efforts? E.g. who is working on it, whether there is a git branch that contains the current work, etc.</p>

---

## Post #5 by @lassoan (2023-07-04 15:04 UTC)

<p>Here is the git branch:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Punzo/CTK/commits/addDICOMVisualNavigation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Punzo/CTK/commits/addDICOMVisualNavigation" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/8c30502b49ec217bc9865b5c324f885f8ba0d4627be3fc5bf27630222665383a/Punzo/CTK" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Punzo/CTK/commits/addDICOMVisualNavigation" target="_blank" rel="noopener">Commits · Punzo/CTK</a></h3>

  <p>A set of common support code for medical imaging, surgical navigation, and related purposes. - Commits · Punzo/CTK</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It is already functional but the background networking tasks slow down the main thread (probably due to some unwanted synhronization in logging or database access), so it is not ready for user testing yet. However, you can have a look at it or give it a try. The main developer is <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>. He’ll continue to work on it from mid August and we expect that he’ll fix the remaining issues by early September. Any contribution, feedback, bugfixes, etc. are welcome.</p>

---
