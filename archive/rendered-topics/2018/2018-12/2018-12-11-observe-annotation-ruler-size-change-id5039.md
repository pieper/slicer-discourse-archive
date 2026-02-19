---
topic_id: 5039
title: "Observe Annotation Ruler Size Change"
date: 2018-12-11
url: https://discourse.slicer.org/t/5039
---

# Observe annotation ruler size change

**Topic ID**: 5039
**Date**: 2018-12-11
**URL**: https://discourse.slicer.org/t/observe-annotation-ruler-size-change/5039

---

## Post #1 by @giancu (2018-12-11 12:30 UTC)

<p>Hi. I try to capture the change in size of a vtkMRMLAnnotationRulerNode. Is there any event (signal) which is triggered in such a situation? I am using the nice LineProfile example of Andras, but I would like to be able to update the line profile chart “on line” when changing the annotation ruler.<br>
Thanks in advance.<br>
Cheers Gheorghe</p>

---

## Post #2 by @lassoan (2018-12-11 21:12 UTC)

<p>A completely reworked version of the line profile plot module is available:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerLineProfile">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerLineProfile" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/791dc16c2e24a5668bfdf0c2ce39ac931afd78c759a98b5d6d78ce26de7f2629/lassoan/SlicerLineProfile" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerLineProfile" target="_blank" rel="noopener">GitHub - lassoan/SlicerLineProfile: Extension for 3D Slicer to compute...</a></h3>

  <p>Extension for 3D Slicer to compute intensity profile of a volume along a line - GitHub - lassoan/SlicerLineProfile: Extension for 3D Slicer to compute intensity profile of a volume along a line</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It can update the profile in real-time as you modify the ruler (just click the checkbox on the “Compute…” button). It also makes available the sampled intensity values in a table, and uses new plotting infrastructure.</p>
<p><a href="https://github.com/lassoan/SlicerLineProfile/blob/master/LineProfileScreenshot01.png?raw=true" class="onebox" target="_blank" rel="noopener">https://github.com/lassoan/SlicerLineProfile/blob/master/LineProfileScreenshot01.png?raw=true</a></p>
<p>It would be ready to be submitted to the extension manager (so that you can install using a single click) but I did not have time to create an icon for the extension. If anybody could draw a nice icon to replace the <a href="https://github.com/lassoan/SlicerLineProfile/blob/master/LineProfile.png">current placeholder</a> then please do and send a pull request. Thanks!</p>

---

## Post #3 by @giancu (2019-01-07 09:25 UTC)

<p>You’re the best. Work like a charm. Thank you.</p>

---

## Post #4 by @giancu (2019-01-07 09:40 UTC)

<p>Is looks like sometimes the update speed is not always the same. Moving the mouse does not always update the plot. Can I adapt the update parameters? Luckily the values saved in the table are always correct.</p>

---

## Post #5 by @lassoan (2019-01-07 13:48 UTC)

<aside class="quote no-group" data-username="giancu" data-post="4" data-topic="5039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/8797f3/48.png" class="avatar"> giancu:</div>
<blockquote>
<p>Can I adapt the update parameters?</p>
</blockquote>
</aside>
<p>Can you give more details about what you would like to do exactly?</p>

---
