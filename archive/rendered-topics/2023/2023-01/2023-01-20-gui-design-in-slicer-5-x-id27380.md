---
topic_id: 27380
title: "Gui Design In Slicer 5 X"
date: 2023-01-20
url: https://discourse.slicer.org/t/27380
---

# GUI Design in Slicer 5.x

**Topic ID**: 27380
**Date**: 2023-01-20
**URL**: https://discourse.slicer.org/t/gui-design-in-slicer-5-x/27380

---

## Post #1 by @MSK (2023-01-20 14:51 UTC)

<p>Despite not being very familiar to Slicer I am given the task of designing a custom GUI to ease the use of Slicer by physicians. I want this GUI to be run in Slicer 5.x. I read about Slicelets and my task is the exact definition of them. However, I am having trouble understanding the simple example provided by following link:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/lassoan/SlicerSimpleWorkflows/tree/master/QuickSegment">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerSimpleWorkflows/tree/master/QuickSegment" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/lassoan/SlicerSimpleWorkflows/tree/master/QuickSegment" target="_blank" rel="noopener nofollow ugc">SlicerSimpleWorkflows/QuickSegment at master · lassoan/SlicerSimpleWorkflows</a></h3>

  <p><a href="https://github.com/lassoan/SlicerSimpleWorkflows/tree/master/QuickSegment" target="_blank" rel="noopener nofollow ugc">master/QuickSegment</a></p>

  <p><span class="label1">Examples of simple application-specific workflows implemented using 3D Slicer</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Furthermore, I am not sure if it will work on Slicer 5.x. I am searching the new documentation however there is not an up-to-date page describing GUI design. I humbly ask for a guide that you think might be helpful for my relatively simple task.<br>
Thanks a lot in advance.</p>

---

## Post #2 by @rbumm (2023-01-22 00:14 UTC)

<aside class="quote no-group quote-modified" data-username="MSK" data-post="1" data-topic="27380">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/65b543/48.png" class="avatar"> MSK:</div>
<blockquote>
<p><a href="https://github.com/lassoan/SlicerSimpleWorkflows/tree/master/QuickSegment">https://github.com/lassoan/SlicerSimpleWorkflows/tree/master/QuickSegment</a></p>
</blockquote>
</aside>
<p>This is an important topic.</p>
<p>You can enable “Developer mode” in Slicer Settings:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39cba2ae7a594fd64392793a9569a771253cc44c.png" alt="image" data-base62-sha1="8fhvaNhUmbxa8EVadNVRVZFRzfm" width="463" height="318"></p>
<p>then use the QT designer to make a prototype of a GUI.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eba45c4d0f1e16d205ff07061f1ec5931324c1e7.png" data-download-href="/uploads/short-url/xCAltBAukOPqP7MM90y9RRdQu0v.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eba45c4d0f1e16d205ff07061f1ec5931324c1e7_2_690x366.png" alt="image" data-base62-sha1="xCAltBAukOPqP7MM90y9RRdQu0v" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eba45c4d0f1e16d205ff07061f1ec5931324c1e7_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eba45c4d0f1e16d205ff07061f1ec5931324c1e7_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eba45c4d0f1e16d205ff07061f1ec5931324c1e7_2_1380x732.png 2x" data-dominant-color="D2D3CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×1018 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You may also want to check out <a href="https://discourse.slicer.org/t/slicerqr-development/15954">this interesting thread dealing with Slicer QR</a>.</p>

---

## Post #3 by @MSK (2023-06-11 12:35 UTC)

<p>Thank you so much, QT designer indeed seems like the solution for the GUI design.</p>

---

## Post #4 by @MSK (2023-06-11 12:45 UTC)

<p>I would like to elaborate on my question further and share my findings. I ended up finding multiple options for my task, and the one I decided on is to write a python scripted module. In this module I customize my GUI, and add only the necessary widgets and functionalities. That will simplify the interface for the use of physicians. In my opinion, this amazing video series cannot be ignored when it comes to design of a python scripted module for the beginners:</p>
<p>            <iframe src="https://www.youtube.com/embed/f_gsm0GJ4_8?feature=oembed&amp;wmode=opaque&amp;list=PLTuWbByD80TORd1R-J7j7nVQ9fot3C2fK" width="480" height="360" frameborder="0" allowfullscreen="" class="youtube-onebox" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
</p>
<p>After following the tutorial, I have another question:</p>
<p>To design python scripted modules, is there a repository or a similar source that is providing basic scripts for the python? For instance, I want to have the option of loading DICOM files from a folder. I would like to have a basic GUI design along with its code provided only for this task. I know there are sources in following link but usually there are a lot of functions, all intertwined with each other, consuming a lot of time to understand:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted" target="_blank" rel="noopener nofollow ugc">Slicer/Modules/Scripted at main · Slicer/Slicer</a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted" target="_blank" rel="noopener nofollow ugc">main/Modules/Scripted</a></p>

  <p><span class="label1">Multi-platform, free open source software for visualization and image computing.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @rbumm (2023-06-11 14:11 UTC)

<p>The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">3D Slicer script repository</a> is what you should utilize for that.</p>

---
