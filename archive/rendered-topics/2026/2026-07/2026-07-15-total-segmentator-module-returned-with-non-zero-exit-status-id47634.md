---
topic_id: 47634
title: "Total segmentator module returned with non-zero exit status 1 on to 5.12.1"
date: 2026-07-15
url: https://discourse.slicer.org/t/47634
last_bumped: 2026-07-19T01:59:45.653Z
---

# Total segmentator module returned with non-zero exit status 1 on to 5.12.1

**Topic ID**: 47634
**Date**: 2026-07-15
**URL**: https://discourse.slicer.org/t/total-segmentator-module-returned-with-non-zero-exit-status-1-on-to-5-12-1/47634

---

## Post #1 by @Cromwell (2026-07-15 12:22 UTC)

<p>I’m having problems with the execution of the total segmentator module, I thought it was something installation, as version 5.10 was running I updated to 5.12.1 but it keeps the same error only with this module. I saw that some people have already reported problems with it! Trying to run lung nodules or lung segment airway and vessels I received the same error message</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adcfa870ddd2e898d0ef0fc3f44c0a82ad77ab08.jpeg" data-download-href="/uploads/short-url/oNBvsZi9ixGQhvLETNWqeeRKKfe.jpeg?dl=1" title="IMG_9238" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adcfa870ddd2e898d0ef0fc3f44c0a82ad77ab08_2_666x500.jpeg" alt="IMG_9238" data-base62-sha1="oNBvsZi9ixGQhvLETNWqeeRKKfe" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adcfa870ddd2e898d0ef0fc3f44c0a82ad77ab08_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adcfa870ddd2e898d0ef0fc3f44c0a82ad77ab08_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adcfa870ddd2e898d0ef0fc3f44c0a82ad77ab08_2_1332x1000.jpeg 2x" data-dominant-color="74737D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_9238</span><span class="informations">1920×1440 784 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @madsmess (2026-07-15 16:28 UTC)

<p>My workaround for this problem was to uninstall Slicer, delete the app files from AppData, and reinstall Slicer inside the C drive (not in any subfolder, just inside the drive itself)</p>

---

## Post #3 by @Cromwell (2026-07-17 21:04 UTC)

<p>I tried this, but nothing done! Already do the same error</p>

---

## Post #4 by @lassoan (2026-07-18 15:24 UTC)

<p>Please follow these instructions: <a href="https://github.com/lassoan/SlicerTotalSegmentator#failed-to-compute-results-error-the-first-time-trying-to-use-this-slicer-module" class="inline-onebox">GitHub - lassoan/SlicerTotalSegmentator: Fully automatic total body segmentation in 3D Slicer using "TotalSegmentator" AI model · GitHub</a></p>

---

## Post #5 by @Cromwell (2026-07-18 20:52 UTC)

<p><strong>I would like to share the solution that worked for me, as it may help other users and possibly identify a compatibility issue.</strong></p>
<p>I was using:</p>
<ul>
<li><strong>3D Slicer 5.12.2 (Windows)</strong></li>
<li><strong>TotalSegmentator extension 2.13.0</strong></li>
<li><strong>CPU inference (AMD GPU, no CUDA)</strong></li>
</ul>
<p>The following tasks worked correctly:</p>
<ul>
<li><code>total</code></li>
</ul>
<p>However, the following tasks consistently failed:</p>
<ul>
<li><code>lung_nodules</code></li>
<li><code>lung_vessels</code></li>
</ul>
<p>The errors were:</p>
<pre><code class="lang-auto">
</code></pre>
<pre><code class="lang-auto">RuntimeError: Could not find requested nnUNetTrainer_MOSAIC_1k_QuarterLR_NoMirroring
</code></pre>
<p>and</p>
<pre><code class="lang-auto">
</code></pre>
<pre><code class="lang-auto">RuntimeError: Could not find requested nnUNetTrainerSkeletonRecall
</code></pre>
<p>I tried all of the following without success:</p>
<ul>
<li>Force reinstall of the TotalSegmentator extension</li>
<li>Re-downloading the model weights</li>
<li>Deleting and downloading the datasets again</li>
<li>Restarting Slicer multiple times</li>
</ul>
<p>The downloaded models were correct, and the standard <strong>total</strong> task always worked.</p>
<p>Checking the installed package versions revealed:</p>
<pre><code class="lang-auto">
</code></pre>
<pre><code class="lang-auto">TotalSegmentator: 2.13.0
nnunetv2: 2.8.1
</code></pre>
<p>The issue was resolved by downgrading <strong>nnunetv2</strong> to <strong>2.6.2</strong> from the Slicer Python Console:</p>
<pre><code class="lang-auto">
</code></pre>
<pre><code class="lang-auto">slicer.util.pip_install("nnunetv2==2.6.2")
</code></pre>
<p>After restarting Slicer:</p>
<pre><code class="lang-auto">
</code></pre>
<pre><code class="lang-auto">TotalSegmentator: 2.13.0
nnunetv2: 2.6.2
</code></pre>
<p>Everything worked correctly:</p>
<ul>
<li><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> total</li>
<li><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> lung_nodules</li>
<li><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> lung_vessels (vessels and airways)</li>
</ul>
<p>This suggests that <strong>TotalSegmentator 2.13.0 is currently not fully compatible with nnUNetv2 2.8.1 for tasks that rely on custom nnUNet trainers</strong>, while it works correctly with <strong>nnUNetv2 2.6.2</strong>.</p>
<p>Hopefully this information helps other users experiencing the same issue and assists the developers in tracking the version compatibility problem.</p>
<p>Thank you for the excellent extension.</p>

---

## Post #6 by @jamesobutler (2026-07-19 01:59 UTC)

<p>Thanks for the information. It looks like the issue was resolved in TotalSegmentator 2.14.0.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/wasserth/TotalSegmentator/commit/33a8cf2ff64a51eec9a1c148229985dd993d1d11">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/commit/33a8cf2ff64a51eec9a1c148229985dd993d1d11" target="_blank" rel="noopener nofollow ugc">github.com/wasserth/TotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/wasserth/TotalSegmentator/commit/33a8cf2ff64a51eec9a1c148229985dd993d1d11" target="_blank" rel="noopener nofollow ugc">fix nnunet trainer patching to work with newer nnunet versions</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2026-06-08" data-time="13:32:54" data-timezone="UTC">01:32PM - 08 Jun 26 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/wasserth" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/26226563?v=4" class="onebox-avatar-inline" width="20" height="20">
          wasserth
        </a>
      </div>

      <div class="lines" title="changed 1 files with 31 additions and 10 deletions">
        <a href="https://github.com/wasserth/TotalSegmentator/commit/33a8cf2ff64a51eec9a1c148229985dd993d1d11" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+31</span>
          <span class="removed">-10</span>
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

<p>SlicerTotalSegmentator will need to be updated to a newer version:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/blob/bded9731643c684f2b930d9e480d458a5b0b680b/TotalSegmentator/TotalSegmentator.py#L429">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/bded9731643c684f2b930d9e480d458a5b0b680b/TotalSegmentator/TotalSegmentator.py#L429" target="_blank" rel="noopener nofollow ugc">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/bded9731643c684f2b930d9e480d458a5b0b680b/TotalSegmentator/TotalSegmentator.py#L429" target="_blank" rel="noopener nofollow ugc">TotalSegmentator/TotalSegmentator.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/bded9731643c684f2b930d9e480d458a5b0b680b/TotalSegmentator/TotalSegmentator.py#L429" rel="noopener nofollow ugc"><code>bded97316</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="419" style="counter-reset: li-counter 418 ;">
          <li>"""</li>
          <li></li>
          <li>def __init__(self):</li>
          <li>    """</li>
          <li>    Called when the logic class is instantiated. Can be used for initializing member variables.</li>
          <li>    """</li>
          <li>    from collections import OrderedDict</li>
          <li></li>
          <li>    ScriptedLoadableModuleLogic.__init__(self)</li>
          <li></li>
          <li class="selected">    self.totalSegmentatorPythonPackageDownloadUrl = "https://github.com/wasserth/TotalSegmentator/archive/98d57a19400703dd87fa07483d15b8e85b4cf4ed.zip"  # v2.13.0</li>
          <li></li>
          <li>    # Custom applications can set custom location for weights.</li>
          <li>    # For example, it could be set to `sysconfig.get_path('scripts')` to have an independent copy of</li>
          <li>    # the weights for each Slicer installation. However, setting such custom path would result in extra downloads and</li>
          <li>    # storage space usage if there were multiple Slicer installations on the same computer.</li>
          <li>    self.totalSegmentatorWeightsPath = None</li>
          <li></li>
          <li>    self.logCallback = None</li>
          <li>    self.clearOutputFolder = True</li>
          <li>    self.useStandardSegmentNames = True</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
