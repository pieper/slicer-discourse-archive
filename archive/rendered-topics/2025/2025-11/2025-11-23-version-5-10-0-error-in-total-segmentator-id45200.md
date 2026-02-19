---
topic_id: 45200
title: "Version 5 10 0 Error In Total Segmentator"
date: 2025-11-23
url: https://discourse.slicer.org/t/45200
---

# Version 5.10.0, error in total segmentator

**Topic ID**: 45200
**Date**: 2025-11-23
**URL**: https://discourse.slicer.org/t/version-5-10-0-error-in-total-segmentator/45200

---

## Post #1 by @hepato (2025-11-23 22:33 UTC)

<p>processing started</p>
<p>Writing input file to /private/var/folders/0c/gpzkc1r575xdc6jdzv6v_s6h0000gn/T/Slicer-cy/__SlicerTemp__2025-11-24_06+19+55.287/total-segmentator-input.nii</p>
<p>Creating segmentations with TotalSegmentator AI…</p>
<p>Total Segmentator arguments: [‘-i’, ‘/private/var/folders/0c/gpzkc1r575xdc6jdzv6v_s6h0000gn/T/Slicer-cy/__SlicerTemp__2025-11-24_06+19+55.287/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/0c/gpzkc1r575xdc6jdzv6v_s6h0000gn/T/Slicer-cy/__SlicerTemp__2025-11-24_06+19+55.287/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]</p>
<p>No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ or the `–roi_subset` option can help to reduce runtime.</p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator”, line 8, in</p>
<pre><code class="lang-auto">sys.exit(main())

         ^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/bin/TotalSegmentator.py”, line 155, in main</p>
<pre><code class="lang-auto">totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/python_api.py”, line 142, in totalsegmentator</p>
<pre><code class="lang-auto">from totalsegmentator.nnunet import nnUNet_predict_image  # this has to be after setting new env vars

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/nnunet.py”, line 29, in</p>
<pre><code class="lang-auto">from totalsegmentator.custom_trainers import nnUNetTrainer_MOSAIC_1k_QuarterLR_NoMirroring
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/totalsegmentator/custom_trainers.py”, line 2, in</p>
<pre><code class="lang-auto">from nnunetv2.training.nnUNetTrainer.variants.data_augmentation.nnUNetTrainerNoMirroring import nnUNetTrainerNoMirroring
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/training/nnUNetTrainer/variants/data_augmentation/nnUNetTrainerNoMirroring.py”, line 26, in</p>
<pre><code class="lang-auto">from nnunetv2.training.nnUNetTrainer.nnUNetTrainer import nnUNetTrainer
</code></pre>
<p>File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/nnunetv2/training/nnUNetTrainer/nnUNetTrainer.py”, line 43, in</p>
<pre><code class="lang-auto">from torch import GradScaler
</code></pre>
<p>ImportError: cannot import name ‘GradScaler’ from ‘torch’ (/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/torch/_<em>init</em>_.py)</p>
<p>Traceback (most recent call last):</p>
<p>File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3392, in tryWithErrorDisplay</p>
<pre><code class="lang-auto">yield
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py”, line 309, in onApplyButton</p>
<pre><code class="lang-auto">self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py”, line 1054, in process</p>
<pre><code class="lang-auto">self.processVolume(inputFile, inputVolume,
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py”, line 1121, in processVolume</p>
<pre><code class="lang-auto">self.logProcessOutput(proc)
</code></pre>
<p>File “/Applications/Slicer.app/Contents/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py”, line 900, in logProcessOutput</p>
<pre><code class="lang-auto">raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
</code></pre>
<p>subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/0c/gpzkc1r575xdc6jdzv6v_s6h0000gn/T/Slicer-cy/__SlicerTemp__2025-11-24_06+19+55.287/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/0c/gpzkc1r575xdc6jdzv6v_s6h0000gn/T/Slicer-cy/__SlicerTemp__2025-11-24_06+19+55.287/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @hepato (2025-11-23 22:35 UTC)

<aside class="quote no-group" data-username="hepato" data-post="1" data-topic="45200">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/3da27b/48.png" class="avatar"> hepato:</div>
<blockquote>
<p>ImportError: cannot import name ‘GradScaler’ from ‘torch’</p>
</blockquote>
</aside>
<p>ImportError: cannot import name ‘GradScaler’ from ‘torch’</p>

---

## Post #3 by @jamesobutler (2025-11-24 00:02 UTC)

<p>This appears to be an issue introduced by NNunetv2 developers. This package is a dependency of TotalSegmentator.</p>
<p>A possible workaround is to open the NNunet Slicer module which is used for installing versions of the package. Choose to install nnunetv2&lt;2.6 as it seems like the nnunetv2 2.6.0 version introduced this error that requires torch 2.6.0 and later for the CPU version of GradScaler.</p>
<p>Unfortunately, on macOS Slicer factory builds are still x86_64 builds with no native arm64 build. The latest version of torch supported on x86_64 macOS is torch 2.2.x. Slicer developers have been actively working to update a whole list of dependencies to be able to support native arm64 builds. Things are still in progress, but hopefully these type of issues on macOS will be resolved soon for users of macOS on Apple Silicon M based Macs.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6811">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6811" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6811" target="_blank" rel="noopener nofollow ugc">Support for building/testing/packaging Slicer on Apple arm64</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-02-02" data-time="00:01:58" data-timezone="UTC">12:01AM - 02 Feb 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is meta issues aiming to organize the sub-tasks associated with arm64 suppo<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rt. See Sub-issues listed below.


Related issues and pull requests:
* https://github.com/Slicer/Slicer/issues/5944
* https://github.com/Slicer/Slicer/issues/6705
* https://github.com/Slicer/Slicer/issues/6490
* https://github.com/Slicer/Slicer/pull/8097

Related discourse posts:
* https://discourse.slicer.org/t/issues-running-slicer-on-macbook-m1-max/23974/3
* https://discourse.slicer.org/t/slicer-quit-unexpectedly-on-macbook-with-m1-chip/25989
* https://discourse.slicer.org/t/build-arm-32-openssl/31204
* https://discourse.slicer.org/t/developing-for-slicer-on-apple-silicon-build-targeting-x86-64/40686</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @hepato (2025-11-24 11:16 UTC)

<p>Thanks for your reply. I  reinstall  slicer of version 5.8.1 again and problems resolved.</p>

---
