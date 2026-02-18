# TotalSegmentator ERROR failed to compute result - returned non-zero exit status 120

**Topic ID**: 29600
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/totalsegmentator-error-failed-to-compute-result-returned-non-zero-exit-status-120/29600

---

## Post #1 by @cmjones (2023-05-23 11:06 UTC)

<p>When I run totalsegmentator on 3D slicer using the CTA Abdomen (panoramix) sample data it comes with the following error. I have tried uninstalling 3D slicer/PyTorch/totalsegmentator numerous times with no luck.</p>
<p>Operating system: macOS Monterey 12.5.1 (Apple M1 chip)<br>
Slicer version: 5.2.2<br>
Expected behavior: totalsegmentator<br>
Actual behavior: ERROR when running apply</p>
<p>"Processing started<br>
Writing input file to /private/var/folders/n4/_8hf03v543x_q3b0k017wbfm0000gp/T/Slicer-mosc7cj2/__SlicerTemp__2023-05-23_10+25+00.631/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘/private/var/folders/n4/_8hf03v543x_q3b0k017wbfm0000gp/T/Slicer-mosc7cj2/__SlicerTemp__2023-05-23_10+25+00.631/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/n4/_8hf03v543x_q3b0k017wbfm0000gp/T/Slicer-mosc7cj2/__SlicerTemp__2023-05-23_10+25+00.631/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/torch/cuda/amp/grad_scaler.py:116: UserWarning: torch.cuda.amp.GradScaler is enabled, but CUDA is not available.  Disabling.<br>
warnings.warn(“torch.cuda.amp.GradScaler is enabled, but CUDA is not available.  Disabling.”)<br>
/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/torch/cuda/amp/autocast_mode.py:118: UserWarning: torch.cuda.amp.autocast only affects CUDA ops, but CUDA is not available.  Disabling.<br>
warnings.warn(“torch.cuda.amp.autocast only affects CUDA ops, but CUDA is not available.  Disabling.”)<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator”, line 93, in <br>
main()<br>
File “/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator”, line 86, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/totalsegmentator/python_api.py”, line 173, in totalsegmentator<br>
seg = nnUNet_predict_image(input, output, task_id, model=model, folds=folds,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/totalsegmentator/nnunet.py”, line 255, in nnUNet_predict_image<br>
nnUNet_predict(tmp_dir, tmp_dir, task_id, model, folds, trainer, tta)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/totalsegmentator/nnunet.py”, line 106, in nnUNet_predict<br>
predict_from_folder(model_folder_name, dir_in, dir_out, folds, save_npz, num_threads_preprocessing,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/nnunet/inference/predict.py”, line 668, in predict_from_folder<br>
return predict_cases_fastest(model, list_of_lists[part_id::num_parts], output_files[part_id::num_parts], folds,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/nnunet/inference/predict.py”, line 493, in predict_cases_fastest<br>
res = trainer.predict_preprocessed_data_return_seg_and_softmax(d, do_mirroring=do_tta,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/nnunet/training/network_training/nnUNetTrainerV2.py”, line 211, in predict_preprocessed_data_return_seg_and_softmax<br>
ret = super().predict_preprocessed_data_return_seg_and_softmax(data,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/nnunet/training/network_training/nnUNetTrainer.py”, line 516, in predict_preprocessed_data_return_seg_and_softmax<br>
ret = self.network.predict_3D(data, do_mirroring=do_mirroring, mirror_axes=mirror_axes,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/nnunet/network_architecture/neural_network.py”, line 147, in predict_3D<br>
res = self._internal_predict_3D_3Dconv_tiled(x, step_size, do_mirroring, mirror_axes, patch_size,<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/nnunet/network_architecture/neural_network.py”, line 348, in _internal_predict_3D_3Dconv_tiled<br>
gaussian_importance_map[gaussian_importance_map == 0] = gaussian_importance_map[<br>
RuntimeError: “min_all” not implemented for ‘Half’<br>
Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x1b765f5b0&gt;<br>
AttributeError: ‘DummyFile’ object has no attribute ‘flush’</p>
<p>If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" rel="noopener nofollow ugc">https://doi.org/10.48550/arXiv.2208.05868</a></p>
<p>No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ option can help to some extend.<br>
Using ‘fast’ option: resampling to lower resolution (3mm)<br>
Resampling…<br>
Resampled in 4.13s<br>
Predicting…"</p>

---

## Post #2 by @lassoan (2023-05-23 11:08 UTC)

<p>Could you please go to Pytorch Utils module and copy here the installed pytorch version?</p>

---

## Post #3 by @cmjones (2023-05-23 11:10 UTC)

<p>Pytorch version 1.8.1</p>

---

## Post #4 by @lassoan (2023-05-23 13:13 UTC)

<p>Could you also write us the NVIDIA driver version (line below PyTorch version in PyTorch Utils module).</p>
<p>The problem is that TotalSegmentator requires pytorch&gt;=2 (see more information <a href="https://github.com/fepegar/SlicerPyTorch/issues/9">here</a>). You can fix this by installing pytorch manually as described <a href="https://pytorch.org/get-started/locally/">here</a> - just use <code>PythonSlicer</code> executable instead of <code>pip3</code>.</p>

---

## Post #5 by @cmjones (2023-05-23 18:53 UTC)

<p>NVIDIA driver: not found</p>

---

## Post #6 by @lassoan (2023-05-23 19:43 UTC)

<p>Thanks for the information. I was wondering if pytorch-1.8.1 is enforced by some old GPU driver, but apparently not.</p>
<p>Anyway, until we figure out why an old pytorch version is installed on some computers, you can install pytorch-2.x in your Slicer to make TotalSegmentator work.</p>

---

## Post #7 by @cmjones (2023-06-05 12:59 UTC)

<p>I still don’t seem to be able to upgrade PyTorch on 3D slicer. Could you help troubleshoot?</p>

---

## Post #8 by @lassoan (2023-06-05 15:26 UTC)

<p>I’ve submitted a pull request to make it easier to select pytorch version in PyTorch Utils module. Hopefully it will be merged today or tomorrow. You can track its status here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/fepegar/SlicerPyTorch/pull/11">
  <header class="source">

      <a href="https://github.com/fepegar/SlicerPyTorch/pull/11" target="_blank" rel="noopener">github.com/fepegar/SlicerPyTorch</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/fepegar/SlicerPyTorch/pull/11" target="_blank" rel="noopener">Allow specifying pytorch version for installation</a>
      </h4>

    <div class="branches">
      <code>fepegar:main</code> ← <code>lassoan:configurable-torch-version</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-06-05" data-time="15:23:07" data-timezone="UTC">03:23PM - 05 Jun 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 36 additions and 13 deletions">
          <a href="https://github.com/fepegar/SlicerPyTorch/pull/11/files" target="_blank" rel="noopener">
            <span class="added">+36</span>
            <span class="removed">-13</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The main motivation for this is that on some computers when installing PyTorch w<span class="show-more-container"><a href="https://github.com/fepegar/SlicerPyTorch/pull/11" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ith default options, a very old version (1.8.1) is installed. The new API and GUI allows specifying a requirement (e.g., "&gt;=1.12" or "&gt;=2").

While this does not address the question of why old version is installed by default, it allows modules to automatically install correct pytorch version and allows users to manually specify a version, if effectively fixes #9</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You need to use the lateset Slicer Stable Release or latest Slicer Preview Release to get the update (the update is available automatically in the Extensions Manager the day after the pull request is merged).</p>

---

## Post #9 by @cmjones (2023-06-05 17:37 UTC)

<p>Despite install PyTorch via Anaconda it still fails. When I then tried to run totalsegmentator it advised that I needed to install PyTorch which is then did however it installed version 1.8.1.</p>
<p>See screenshots.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66306567f36e5cad72f0e5a3431605c709823f3f.png" data-download-href="/uploads/short-url/eA0obT087o2WnyGxjzHPkDbak3R.png?dl=1" title="Screenshot 2023-06-05 at 18.33.30.png" rel="noopener nofollow ugc"><img width="437" height="170" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66306567f36e5cad72f0e5a3431605c709823f3f_2_437x170.png" data-base62-sha1="eA0obT087o2WnyGxjzHPkDbak3R" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66306567f36e5cad72f0e5a3431605c709823f3f_2_437x170.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66306567f36e5cad72f0e5a3431605c709823f3f_2_655x255.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66306567f36e5cad72f0e5a3431605c709823f3f_2_874x340.png 2x" data-dominant-color="CACBCA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-05 at 18.33.30.png</span><span class="informations">874×340 83.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20bb8c7d914530053005ce447fdd76fd11fa983f.png" data-download-href="/uploads/short-url/4Fz6egBKMg9xoMjKSruNQf9YZJl.png?dl=1" title="Screenshot 2023-06-05 at 18.33.45.png" rel="noopener nofollow ugc"><img width="437" height="278" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20bb8c7d914530053005ce447fdd76fd11fa983f_2_437x278.png" data-base62-sha1="4Fz6egBKMg9xoMjKSruNQf9YZJl" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20bb8c7d914530053005ce447fdd76fd11fa983f_2_437x278.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20bb8c7d914530053005ce447fdd76fd11fa983f_2_655x417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20bb8c7d914530053005ce447fdd76fd11fa983f_2_874x556.png 2x" data-dominant-color="E5E5E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-05 at 18.33.45.png</span><span class="informations">874×556 97.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/321df22ff5ec7169395cd114edfec523421dac5f.jpeg" data-download-href="/uploads/short-url/79m21pOjatitJ3cetaVUxNKVOXl.jpeg?dl=1" title="Screenshot 2023-06-05 at 18.34.03.jpg" rel="noopener nofollow ugc"><img width="690" height="450" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/321df22ff5ec7169395cd114edfec523421dac5f_2_690x450.jpeg" data-base62-sha1="79m21pOjatitJ3cetaVUxNKVOXl" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/321df22ff5ec7169395cd114edfec523421dac5f_2_690x450.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/321df22ff5ec7169395cd114edfec523421dac5f_2_1035x675.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/321df22ff5ec7169395cd114edfec523421dac5f_2_1380x900.jpeg 2x" data-dominant-color="E7E6E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-05 at 18.34.03.jpg</span><span class="informations">1420×928 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here’s a copy of the console:</p>
<p>Collecting torch<br>
Using cached <a href="https://download.pytorch.org/whl/cpu/torch-2.0.1-cp39-none-macosx_10_9_x86_64.whl" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cpu/torch-2.0.1-cp39-none-macosx_10_9_x86_64.whl</a> (143.4 MB)<br>
Collecting torchvision<br>
Using cached <a href="https://download.pytorch.org/whl/torchvision-0.9.1-cp39-cp39-macosx_10_9_x86_64.whl" rel="noopener nofollow ugc">https://download.pytorch.org/whl/torchvision-0.9.1-cp39-cp39-macosx_10_9_x86_64.whl</a> (13.1 MB)<br>
Collecting jinja2<br>
Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB)<br>
Collecting filelock<br>
Using cached filelock-3.12.0-py3-none-any.whl (10 kB)<br>
Requirement already satisfied: typing-extensions in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (4.6.0)<br>
Collecting sympy<br>
Using cached sympy-1.12-py3-none-any.whl (5.7 MB)<br>
Requirement already satisfied: networkx in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (3.1)<br>
Collecting torch<br>
Using cached <a href="https://download.pytorch.org/whl/cpu/torch-1.8.1-cp39-none-macosx_10_9_x86_64.whl" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cpu/torch-1.8.1-cp39-none-macosx_10_9_x86_64.whl</a> (119.6 MB)<br>
Requirement already satisfied: pillow&gt;=4.1.1 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torchvision) (9.4.0)<br>
Requirement already satisfied: numpy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torchvision) (1.23.4)<br>
Collecting MarkupSafe&gt;=2.0<br>
Using cached MarkupSafe-2.1.3-cp39-cp39-macosx_10_9_x86_64.whl (13 kB)<br>
Collecting mpmath&gt;=0.19<br>
Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)<br>
Installing collected packages: torch, torchvision<br>
WARNING: The scripts convert-caffe2-to-onnx and convert-onnx-to-caffe2 are installed in ‘/Applications/Slicer.app/Contents/lib/Python/bin’ which is not on PATH.<br>
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.<br>
Successfully installed torch-1.8.1 torchvision-0.9.1</p>
<p>[notice] A new release of pip is available: 23.0 → 23.1.2<br>
[notice] To update, run: python-real -m pip install --upgrade pip<br>
[Python] Failed to compute results.<br>
[Python] Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/n4/_8hf03v543x_q3b0k017wbfm0000gp/T/Slicer-mosc7cj2/__SlicerTemp__2023-06-05_18+35+07.399/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/n4/_8hf03v543x_q3b0k017wbfm0000gp/T/Slicer-mosc7cj2/__SlicerTemp__2023-06-05_18+35+07.399/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “/Applications/Slicer.app/Contents/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 762, in process<br>
self.logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 655, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/…/bin/PythonSlicer’, ‘/Applications/Slicer.app/Contents/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/private/var/folders/n4/_8hf03v543x_q3b0k017wbfm0000gp/T/Slicer-mosc7cj2/__SlicerTemp__2023-06-05_18+35+07.399/total-segmentator-input.nii’, ‘-o’, ‘/private/var/folders/n4/_8hf03v543x_q3b0k017wbfm0000gp/T/Slicer-mosc7cj2/__SlicerTemp__2023-06-05_18+35+07.399/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.</p>

---

## Post #10 by @jamesobutler (2023-06-05 18:04 UTC)

<p>It appears that for some reason <code>torchvision</code> 0.9.1 is getting installed which is compatible with <code>torch</code> 1.8. See chart at <a href="https://github.com/pytorch/vision/tree/main#installation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pytorch/vision: Datasets, Transforms and Models specific to Computer Vision</a>.</p>
<p>I’m not sure why it is not getting the latest <code>torchvision</code>, but that does appear to explain why torch 1.8.x would get installed.</p>

---

## Post #11 by @lassoan (2023-06-05 19:11 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="10" data-topic="29600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I’m not sure why it is not getting the latest <code>torchvision</code>, but that does appear to explain why torch 1.8.x would get installed.</p>
</blockquote>
</aside>
<p>It’s interesting, maybe it is related to torchvision. Anyway, if the <a href="https://github.com/fepegar/SlicerPyTorch/pull/11">pull request</a> gets merged (hopefully tomorrow) then it’ll be really easy to upgrade/downgrade pytorch.</p>

---

## Post #12 by @rbumm (2023-06-05 19:41 UTC)

<p>Have you tried <a href="https://pytorch.org/get-started/locally/">this page with the various script installer</a> options?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09e2bf7a5e8784c58525eb9bb6ff62e2190f9c19.png" data-download-href="/uploads/short-url/1ps6m0AGvlLFZZ2OlX08cdGAosh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e2bf7a5e8784c58525eb9bb6ff62e2190f9c19_2_690x452.png" alt="image" data-base62-sha1="1ps6m0AGvlLFZZ2OlX08cdGAosh" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e2bf7a5e8784c58525eb9bb6ff62e2190f9c19_2_690x452.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09e2bf7a5e8784c58525eb9bb6ff62e2190f9c19_2_1035x678.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09e2bf7a5e8784c58525eb9bb6ff62e2190f9c19.png 2x" data-dominant-color="F9EFEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1132×743 54.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @lassoan (2023-06-05 19:47 UTC)

<p>Yes, indeed, <a class="mention" href="/u/cmjones">@cmjones</a> if you don’t want to wait a day then you can run the command that you get from the official pytorch website that <a class="mention" href="/u/rbumm">@rbumm</a> showed above. You just need to use <code>PythonSlicer</code> instead of <code>pip3</code>.</p>

---

## Post #14 by @cmjones (2023-06-05 20:17 UTC)

<p>I’ve installed PyTorch using Conda but when I try to import or install in Slicer it seems to only install version 1.8.1.</p>
<blockquote>
<blockquote>
<blockquote>
<p>import PyTorchUtils</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>torch = PyTorchUtils.PyTorchUtilsLogic().torch</p>
</blockquote>
</blockquote>
</blockquote>
<p>Collecting torch</p>
<p>Using cached <a href="https://download.pytorch.org/whl/cpu/torch-2.0.1-cp39-none-macosx_10_9_x86_64.whl" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cpu/torch-2.0.1-cp39-none-macosx_10_9_x86_64.whl</a> (143.4 MB)</p>
<p>Collecting torchvision</p>
<p>Using cached <a href="https://download.pytorch.org/whl/torchvision-0.9.1-cp39-cp39-macosx_10_9_x86_64.whl" rel="noopener nofollow ugc">https://download.pytorch.org/whl/torchvision-0.9.1-cp39-cp39-macosx_10_9_x86_64.whl</a> (13.1 MB)</p>
<p>Collecting sympy</p>
<p>Using cached sympy-1.12-py3-none-any.whl (5.7 MB)</p>
<p>Collecting jinja2</p>
<p>Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB)</p>
<p>Requirement already satisfied: networkx in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (3.1)</p>
<p>Requirement already satisfied: typing-extensions in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (4.6.3)</p>
<p>Collecting filelock</p>
<p>Using cached filelock-3.12.0-py3-none-any.whl (10 kB)</p>
<p>Requirement already satisfied: pillow&gt;=4.1.1 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torchvision) (9.4.0)</p>
<p>Requirement already satisfied: numpy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torchvision) (1.24.2)</p>
<p>Collecting torch</p>
<p>Using cached <a href="https://download.pytorch.org/whl/cpu/torch-1.8.1-cp39-none-macosx_10_9_x86_64.whl" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cpu/torch-1.8.1-cp39-none-macosx_10_9_x86_64.whl</a> (119.6 MB)</p>
<p>Collecting MarkupSafe&gt;=2.0</p>
<p>Using cached MarkupSafe-2.1.3-cp39-cp39-macosx_10_9_x86_64.whl (13 kB)</p>
<p>Collecting mpmath&gt;=0.19</p>
<p>Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)</p>
<p>Installing collected packages: torch, torchvision</p>
<p>WARNING: The scripts convert-caffe2-to-onnx and convert-onnx-to-caffe2 are installed in ‘/Applications/Slicer.app/Contents/lib/Python/bin’ which is not on PATH.</p>
<p>Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.</p>
<p>Successfully installed torch-1.8.1 torchvision-0.9.1</p>
<p>[notice] A new release of pip is available: 23.0.1 → 23.1.2</p>
<p>[notice] To update, run: python-real -m pip install --upgrade pip</p>

---

## Post #15 by @Alex_Vergara (2023-06-05 21:05 UTC)

<p><code>slicer.util.pip_install("-U torch torchvision")</code> in python console worked for me</p>

---

## Post #16 by @cmjones (2023-06-06 05:34 UTC)

<aside class="quote no-group quote-modified" data-username="Alex_Vergara" data-post="15" data-topic="29600">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>slicer.util.pip_install(“-U torch torchvision”)</p>
</blockquote>
</aside>
<p>Thank you. I have finally managed to get it to work by running:</p>
<p>pip.main([‘install’, ‘–upgrade’, ‘torch’])<br>
pip.main([‘install’, ‘–upgrade’, ‘torchvision’])</p>
<p>and then install PyTorch via the Extensions Manager</p>
<p>Thank you for your help</p>

---

## Post #17 by @pssi_92 (2023-06-13 17:24 UTC)

<p>I have a Total segmentator running errors.<br>
My GPU is RTX 3070 (VRAM 8Gb). Cuda version 12.1. Slicer ver 5.2.2<br>
I have installed TotalSegmentator extension (ver. 9340dd7) and PyTorch (ver. fe2e92e) through Extension Manager.<br>
When I press Apply button of Total Segmentator with Fast option off, the Slicer 5.2.2 become frozen.<br>
With Fast option on, this error message appeared.<br>
What can I do to fix this issue?</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\Anatomy-Kim\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/Anatomy-Kim/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/Anatomy-Kim/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 762, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/Anatomy-Kim/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 655, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/Anatomy-Kim/AppData/Local/NA-MIC/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\Anatomy-Kim\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/Anatomy-Kim/AppData/Local/Temp/Slicer/__SlicerTemp__2023-06-13_14+50+31.409/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Anatomy-Kim/AppData/Local/Temp/Slicer/__SlicerTemp__2023-06-13_14+50+31.409/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>

---

## Post #18 by @lassoan (2023-06-13 17:31 UTC)

<p><a class="mention" href="/u/pssi_92">@pssi_92</a> You have <code>returned non-zero exit status 120</code> in the log, which means that the installed PyTorch version is not compatible with TotalSegmentator. You can uninstall the current version of Pytorch and install a compatible version using PyTorch Utils module:</p>
<ul>
<li>Go to <code>PyTorch Utils</code> module</li>
<li>Click <code>Uninstall PyTorch</code>
</li>
<li>Restart Slicer</li>
<li>Go to <code>PyTorch Utils</code> module</li>
<li>Type <code>&gt;=2</code> in <code>PyTorch version requirement</code> (this forces installation of PyTorch version &gt;=2.0.0, which is compatible with TotalSegmentator)</li>
<li>Click <code>Install PyTorch</code>
</li>
</ul>

---

## Post #20 by @pssi_92 (2023-06-19 02:40 UTC)

<p>Thank you for advice.<br>
In my computer today, the total segmentator worked fine. I don’t know what happened exactly.<br>
I installed total segmentator same in other computer of my colleague, but it won’t work well.<br>
The error message was same “returned non-zero exit status 120”.</p>
<p>So I followed your advice but the result was same.<br>
Before I reinstall PyTorch, I checked the version but it was 2.0.1+cu118.<br>
I think it is higher version than 2.0.0.</p>
<p>The GPU was GTX 1070, Cuda version 12.1, Slicer 5.2.2. PyTorch verison 2.0.1+cu118.</p>

---

## Post #21 by @lassoan (2023-06-19 03:01 UTC)

<p>Maybe the installation on your colleague’s computer is corrupted (most likely due to insufficient disk space or network error during installation).</p>
<p>I would recommend to reinstall Slicer from scratch into an empty folder. Also remove the downloaded TotalSegmentator model from your user profile folder. When installing TotalSegmentator and its dependencies make sure to have at least 20GB of free disk space. If there is any error then</p>

---

## Post #22 by @rbumm (2023-06-19 06:20 UTC)

<p>If there is any error then please post the output of the TotalSegmentator extension text box</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb6d714714c6080de0e6b55b80f8b74de96dad25.png" data-download-href="/uploads/short-url/xAGGtbfCUA2arC6nakyvfDy98bz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb6d714714c6080de0e6b55b80f8b74de96dad25.png" alt="image" data-base62-sha1="xAGGtbfCUA2arC6nakyvfDy98bz" width="353" height="500" data-dominant-color="F0EFF0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">487×689 29.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
