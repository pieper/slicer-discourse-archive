---
topic_id: 253
title: "Changetracker Is Broken"
date: 2017-05-03
url: https://discourse.slicer.org/t/253
---

# ChangeTracker is broken

**Topic ID**: 253
**Date**: 2017-05-03
**URL**: https://discourse.slicer.org/t/changetracker-is-broken/253

---

## Post #1 by @finetjul (2017-05-03 12:36 UTC)

<p>Hi,</p>
<p>I tested the ChangeTracker extension in Slicer 4.6.2 and it appears to be broken.</p>
<p>Problem <span class="hashtag">#1:</span> Test data fails to be loaded</p>
<p>Problem <span class="hashtag">#2:</span> There are Python errors at step 3</p>

---

## Post #2 by @fedorov (2017-05-03 14:58 UTC)

<aside class="quote no-group" data-username="finetjul" data-post="1" data-topic="253">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/finetjul/48/146_2.png" class="avatar"> finetjul:</div>
<blockquote>
<p>Problem <span class="hashtag-raw">#1:</span> Test data fails to be loaded</p>
</blockquote>
</aside>
<p>This appears to be a regression (or deprecation of functionality in Slicer?). This returns <code>None</code>, although dataset URL is valid:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; vl=slicer.modules.volumes.logic()
&gt;&gt;&gt; vl.AddArchetypeVolume('http://www.slicer.org/slicerWiki/images/e/e3/RegLib_C01_2.nrrd','Test',0)
</code></pre>
<aside class="quote no-group" data-username="finetjul" data-post="1" data-topic="253">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/finetjul/48/146_2.png" class="avatar"> finetjul:</div>
<blockquote>
<p>Problem <span class="hashtag-raw">#2:</span> There are Python errors at step 3</p>
</blockquote>
</aside>
<p>Surprisingly to myself (I have not used this module for years!), it completed successfully on mac with the latest nightly, no python errors, and here’s the proof!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/a09e9c1af9a8491e7212f11c39a9ffa8caa95e23.jpg" data-download-href="/uploads/short-url/mUUdl7C4cCowoWPSYYq4su4ySbN.jpg?dl=1" title="image.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a09e9c1af9a8491e7212f11c39a9ffa8caa95e23_2_689x419.jpg" width="689" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a09e9c1af9a8491e7212f11c39a9ffa8caa95e23_2_689x419.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/a09e9c1af9a8491e7212f11c39a9ffa8caa95e23_2_1033x628.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a09e9c1af9a8491e7212f11c39a9ffa8caa95e23.jpeg 2x" data-dominant-color="AFACAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1194×726 376 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @fedorov (2017-05-03 15:17 UTC)

<aside class="quote no-group" data-username="finetjul" data-post="1" data-topic="253">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/finetjul/48/146_2.png" class="avatar"> finetjul:</div>
<blockquote>
<p>Problem <span class="hashtag-raw">#1:</span> Test data fails to be loaded</p>
</blockquote>
</aside>
<p>should be resolved in the tomorrow’s nightly</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/fedorov/ChangeTrackerPy/commit/ea508e804a5a317037ddbc1e884d44dbc53018b9">
  <header class="source">

      <a href="https://github.com/fedorov/ChangeTrackerPy/commit/ea508e804a5a317037ddbc1e884d44dbc53018b9" target="_blank" rel="noopener">github.com/fedorov/ChangeTrackerPy</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/fedorov/ChangeTrackerPy/commit/ea508e804a5a317037ddbc1e884d44dbc53018b9" target="_blank" rel="noopener">BUG: fix test data download</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2017-05-03" data-time="15:16:30" data-timezone="UTC">03:16PM - 03 May 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/fedorov" target="_blank" rel="noopener">
          <img alt="fedorov" src="https://avatars.githubusercontent.com/u/313942?v=4" class="onebox-avatar-inline" width="20" height="20">
          fedorov
        </a>
      </div>

      <div class="lines" title="changed 1 files with 14 additions and 4 deletions">
        <a href="https://github.com/fedorov/ChangeTrackerPy/commit/ea508e804a5a317037ddbc1e884d44dbc53018b9" target="_blank" rel="noopener">
          <span class="added">+14</span>
          <span class="removed">-4</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @finetjul (2017-05-03 19:06 UTC)

<p>Hi Andrey,</p>
<p>Here is the error I have when I enter step 3.</p>
<pre><code>Traceback (most recent call last):
  File "C:\Users\Julien\AppData\Roaming\NA-MIC\Extensions-25516\ChangeTracker\lib\Slicer-4.6\qt-scripted-modules\ChangeTrackerWizard\ChangeTrackerSegmentROIStep.py", line 173, in onEntry
    Helper.InitVRDisplayNode(self.__vrDisplayNode, roiVolume.GetID(), roiNodeID)
  File "C:\Users\Julien\AppData\Roaming\NA-MIC\Extensions-25516\ChangeTracker\lib\Slicer-4.6\qt-scripted-modules\ChangeTrackerWizard\Helper.py", line 108, in InitVRDisplayNode
    propNode = vrDisplayNode.GetVolumePropertyNode()
AttributeError: 'NoneType' object has no attribute 'GetVolumePropertyNode'
</code></pre>
<p>You will find below the content of the downloaded ChangeTracker.s4ext file.</p>
<pre><code>arch amd64
archivename 25516-win-amd64-ChangeTracker-gitd91e870-2015-06-04.zip
category Wizards
contributors Andrey Fedorov (SPL), Kilian Pohl (SPL), Peter Black (BWH), Jean-Christophe Fillion-Robin (Kitware), Ron Kikinis (SPL)
description ChangeTracker is a software tool for quantification of the subtle changes in pathology. The module provides a workflow pipeline that combines user input with the medical data. As a result we provide quantitative volumetric measurements of growth/shrinkage together with the volume rendering of the tumor and color-coded visualization of the tumor growth/shrinkage.
enabled 1
extension_id 137168
homepage http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/ChangeTracker
iconurl http://www.slicer.org/slicerWiki/images/b/b9/ChangeTracker_logo.png
md5 fb0a61860be06b57f5139eff2801dd19
os win
release 
revision d91e870
scm git
scmurl https://github.com/fedorov/ChangeTrackerPy.git
screenshots http://www.slicer.org/slicerWiki/images/8/8e/Slicer4_ChangeTracker_Ad.png
slicer_revision 25516
status</code></pre>

---

## Post #5 by @finetjul (2017-05-03 19:18 UTC)

<p>Please note that I don’t have any error with Slicer 4.7.0 nightly</p>

---

## Post #6 by @fedorov (2017-05-03 19:23 UTC)

<p>Thanks <a class="mention" href="/u/finetjul">@finetjul</a>. I can reproduce it, but I can’t see immediately what is wrong.  I am not sure though how valuable “stable” Slicer is, so I am a bit reluctant to spend time on fixing this, considering it works in nightly.</p>

---
