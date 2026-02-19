---
topic_id: 14979
title: "Stl From Dicom Files Samsung Hs50"
date: 2020-12-10
url: https://discourse.slicer.org/t/14979
---

# STL from DICOM Files Samsung HS50

**Topic ID**: 14979
**Date**: 2020-12-10
**URL**: https://discourse.slicer.org/t/stl-from-dicom-files-samsung-hs50/14979

---

## Post #1 by @tdkmatt (2020-12-10 06:24 UTC)

<p>Hello</p>
<p>I’m new to DICOM universe so please be patient <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>i’m trying to help a company generate STLS from a 4D ultrasound machine (Samsung HS50) - They have the license to export 3D volume from via DICOM, ive had them export the files to a USB but they seem to still only be single frames i cant figure out how to import them or confirm if there is a 3D Volume attatched to the scan…</p>
<p>i have a DICOM server setup onsite that will be my next port of call to export directly to but i would not think it would cahnge things, on export the option of export volume is selected</p>
<p>i will link the files shortly</p>

---

## Post #2 by @lassoan (2020-12-12 06:39 UTC)

<p>I spoke to Samsung representatives about a year ago and at that time they told that their exported 3D/4D ultrasound data can only be read by their own software. They might have developed something since then but it is more likely that their exported DICOM images contain the 3D voxel data in private tags.</p>
<p>With a bit of manual work, you can still read them, as described here:<br>
</p><aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/SlicerHeart/SlicerHeart#samsung" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars3.githubusercontent.com/u/13080879?s=400&amp;amp;v=4" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/SlicerHeart/SlicerHeart#samsung" target="_blank" rel="noopener">SlicerHeart/SlicerHeart - Samsung</a></h3>


  <p><span class="label1">3D Slicer extension for cardiac analysis. Contribute to SlicerHeart/SlicerHeart development by creating an account on GitHub.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @tdkmatt (2020-12-15 04:41 UTC)

<p>Sorry for the late reply!</p>
<p>Thank you so much for the reply</p>

---

## Post #4 by @tdkmatt (2020-12-15 04:56 UTC)

<p>it doesnt seem to export as that file type you can see the below raw output scans of dicom with 3d volume</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1SGSaUp6awii17rT5pQuX_rliOJ11GoQp?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1SGSaUp6awii17rT5pQuX_rliOJ11GoQp?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1SGSaUp6awii17rT5pQuX_rliOJ11GoQp?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1SGSaUp6awii17rT5pQuX_rliOJ11GoQp?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">Meet Google Drive – One place for all your files</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
