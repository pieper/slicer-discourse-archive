---
topic_id: 30583
title: "Hd Bet Does Not Work In Latest Slicer Preview Release"
date: 2023-07-13
url: https://discourse.slicer.org/t/30583
---

# HD_BET does not work in latest Slicer Preview Release

**Topic ID**: 30583
**Date**: 2023-07-13
**URL**: https://discourse.slicer.org/t/hd-bet-does-not-work-in-latest-slicer-preview-release/30583

---

## Post #1 by @Muhammed_Fatih_Talu (2023-07-13 13:24 UTC)

<p>While the code below works without any errors in the stable version, it gives an error in the preview version.</p>
<pre><code class="lang-auto">import HDBrainExtractionTool             
        
HDBetLogic = HDBrainExtractionTool.HDBrainExtractionToolLogic()                            
        
brainNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')        
brainSegNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
HDBetLogic.process(masterVolumeNode,brainNode ,brainSegNode ,0)
slicer.util.setSliceViewerLayers(background=brainNode)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbfdf42c0a39df88ec8f9b5a8771f376a5fd5cf5.png" alt="image" data-base62-sha1="qP3nAxM51CC1I3M63C0kU5xzd1H" width="510" height="108"></p>
<pre><code class="lang-auto">  File "C:/ProgramData/slicer.org/Slicer5.3.0/slicer.org/Extensions-31866/HDBrainExtraction/lib/Slicer-5.3/qt-scripted-modules/HDBrainExtractionTool.py", line 346, in process
    from HD_BET.run import run_hd_bet
ModuleNotFoundError: No module named 'HD_BET'
</code></pre>

---

## Post #2 by @pieper (2023-07-13 13:57 UTC)

<p>Please post the exact error.</p>
<p>Also, it could help to post a fully reproducible example that someone can easily paste into the python console to reproduce what you are seeing.  E.g. us the sample data methods to load data, etc.</p>

---

## Post #3 by @lassoan (2023-07-16 01:42 UTC)

<p><a class="mention" href="/u/muhammed_fatih_talu">@Muhammed_Fatih_Talu</a> You need to install prerequisite packages (pytorch and hd_bet). You can do that by running the module once using the GUI. If you install and run the module from script, make sure you call <code>HDBetLogic.setupPythonRequirements()</code> before <code>HDBetLogic.process(...)</code>.</p>

---

## Post #4 by @cnaehle (2025-01-18 22:20 UTC)

<p>Hi,<br>
I am running into similar issue:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37741aa3aa09a890caa98413b47d9372e6833461.jpeg" data-download-href="/uploads/short-url/7Uz0MIXjmCNTrHzvRe759qg91Wp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37741aa3aa09a890caa98413b47d9372e6833461_2_690x297.jpeg" alt="image" data-base62-sha1="7Uz0MIXjmCNTrHzvRe759qg91Wp" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37741aa3aa09a890caa98413b47d9372e6833461_2_690x297.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/37741aa3aa09a890caa98413b47d9372e6833461_2_1035x445.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37741aa3aa09a890caa98413b47d9372e6833461.jpeg 2x" data-dominant-color="414040"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1242×536 94.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/HDBrainExtraction/lib/Slicer-5.6/qt-scripted-modules/HDBrainExtractionTool.py”, line 237, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputVolumeSelector.currentNode(),<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/HDBrainExtraction/lib/Slicer-5.6/qt-scripted-modules/HDBrainExtractionTool.py”, line 346, in process<br>
from HD_BET.run import run_hd_bet<br>
ModuleNotFoundError: No module named ‘HD_BET.run’</p>
<p>Now, PyTorch is installed, but how do I do add the suggested hd_bet package?</p>
<p>Help is appreciated…</p>

---

## Post #5 by @jamesobutler (2025-01-20 02:52 UTC)

<p>The Slicer HDBrainExtension currently specifies to use the latest code of the HD_BET Python package, but the developer has refactored the code resulting in API compatibility issues. I have written up the following GitHub issue to track the work associated with updating the Slicer extension to use an older version of HD_BET that would be compatible.</p>
<p>cc: <a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/lassoan/SlicerHDBrainExtraction/issues/2">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerHDBrainExtraction/issues/2" target="_blank" rel="noopener nofollow ugc">github.com/lassoan/SlicerHDBrainExtraction</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerHDBrainExtraction/issues/2" target="_blank" rel="noopener nofollow ugc">Extension fails to run with latest master branch of HD_BET package</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-01-20" data-time="02:46:42" data-timezone="UTC">02:46AM - 20 Jan 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This extension has broken following the developer of HD_BET refactoring the code<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> as part of creating a HD_BETv2 version. This occurred in https://github.com/MIC-DKFZ/HD-BET/commit/27414b2ef60167bce8a5ae5a1a34e8b02bb2d7d6 where `nnunetv2` became a new dependency along as requiring Python 3.10+.

The issue was originally discovered by a user that posted on the Slicer discourse forum. See https://discourse.slicer.org/t/hd-bet-does-not-work-in-latest-slicer-preview-release/30583/4.
```
Traceback (most recent call last):
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3255, in tryWithErrorDisplay
yield
File “/Applications/Slicer.app/Contents/Extensions-32448/HDBrainExtraction/lib/Slicer-5.6/qt-scripted-modules/HDBrainExtractionTool.py”, line 237, in onApplyButton
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputVolumeSelector.currentNode(),
File “/Applications/Slicer.app/Contents/Extensions-32448/HDBrainExtraction/lib/Slicer-5.6/qt-scripted-modules/HDBrainExtractionTool.py”, line 346, in process
from HD_BET.run import run_hd_bet
ModuleNotFoundError: No module named ‘HD_BET.run’
```

The following code that installs HD_BET
https://github.com/lassoan/SlicerHDBrainExtraction/blob/71a4f021c8f200e88707cf411445848858bde2d4/HDBrainExtractionTool/HDBrainExtractionTool.py#L285
could be updated to https://github.com/MIC-DKFZ/HD-BET/archive/0dcab33233e991b9f7a7cb33052b164eb50062bd.zip which was a version 1.1 commit just prior to the refactoring for version 2. I have opened a separate issue https://github.com/lassoan/SlicerHDBrainExtraction/issues/3 for making things compatible with version 2.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
