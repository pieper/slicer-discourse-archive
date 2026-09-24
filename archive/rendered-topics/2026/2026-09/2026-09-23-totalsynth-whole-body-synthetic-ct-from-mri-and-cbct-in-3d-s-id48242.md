---
topic_id: 48242
title: "TotalSynth: whole-body synthetic CT from MRI and CBCT in 3D Slicer (IMPACT-Synth and KonfAI updated)"
date: 2026-09-23
url: https://discourse.slicer.org/t/48242
last_bumped: 2026-09-23T14:23:25.698Z
---

# TotalSynth: whole-body synthetic CT from MRI and CBCT in 3D Slicer (IMPACT-Synth and KonfAI updated)

**Topic ID**: 48242
**Date**: 2026-09-23
**URL**: https://discourse.slicer.org/t/totalsynth-whole-body-synthetic-ct-from-mri-and-cbct-in-3d-slicer-impact-synth-and-konfai-updated/48242

---

## Post #1 by @vboussot (2026-09-23 14:23 UTC)

<p>Dear all,</p>
<p>In February we announced the <a href="https://github.com/vboussot/SlicerKonfAI" rel="noopener nofollow ugc">KonfAI</a> and <a href="https://github.com/vboussot/SlicerImpactSynth" rel="noopener nofollow ugc">IMPACT-Synth</a> extensions. Here is what is new.</p>
<p><strong>TotalSynth models</strong></p>
<p>We released <strong>TotalSynth</strong>, pretrained models for <strong>synthetic CT from MRI and from CBCT</strong>, from the head to the pelvis (<a href="https://arxiv.org/abs/2609.13838" rel="noopener nofollow ugc">arXiv:2609.13838</a>). They were trained on 1450 quality-controlled pairs of the SynthRAD2023 and SynthRAD2025 challenges plus four prostate cohorts, with the planning CT registered to each input by IMPACT-Reg. Three 5-fold families are available on <a href="https://huggingface.co/VBoussot/ImpactSynth" rel="noopener nofollow ugc">Hugging Face</a>:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Model</th>
<th>Input</th>
<th>MAE (HU)</th>
<th>SSIM</th>
<th>PSNR (dB)</th>
</tr>
</thead>
<tbody>
<tr>
<td>MRI-to-CT</td>
<td>MRI</td>
<td>67.5</td>
<td>0.920</td>
<td>29.3</td>
</tr>
<tr>
<td>CBCT-to-CT</td>
<td>CBCT</td>
<td>53.6</td>
<td>0.939</td>
<td>32.1</td>
</tr>
<tr>
<td>Unified</td>
<td>MRI or CBCT</td>
<td>67.7 / 54.2</td>
<td>0.920 / 0.938</td>
<td>29.2 / 31.9</td>
</tr>
</tbody>
</table>
</div><p>On an external whole-body Dixon MRI dataset (BIC-MAC), fine-tuning on 45 local cases brought the MAE from 100.9 to 62.2 HU. Each app ships its training configuration, so <code>konfai-apps fine-tune</code> starts from the released weights on your own pairs.</p>
<p><strong>IMPACT-Synth</strong></p>
<p>The extension runs these models on a loaded MRI or CBCT and checks the result:</p>
<ul>
<li><strong>Synthesis</strong>: pick the model, the checkpoints to ensemble and the test-time augmentations, click Run. The sCT is loaded over the input, in HU. About 15 s per checkpoint on a 24 GB GPU.</li>
<li><strong>Evaluation with a reference CT</strong>: MAE map, PSNR, SSIM, and the Dice of TotalSegmentator structures on the sCT and on the CT.</li>
<li><strong>Evaluation without reference</strong>: uncertainty map from the ensemble and TTA spread, conformity map from the disagreement of the segmentations.</li>
<li><strong>Segmentation tab</strong>: TotalSegmentator, MRSegmentator and IMPACT-Seg on the input or on the sCT.</li>
</ul>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09b1d53eaa7ff8a85620d8d5f5d8d6e8c9904e4d.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca8ffa2c385eb170e26e09cdf1e28391a98521d3.jpeg" data-video-base62-sha1="1nLiLoyTJRN0q9pWTf5vENtzOa1.mp4">
  </div><p></p>
<p><a href="https://github.com/vboussot/SlicerImpactSynth/blob/main/Screenshots/SlicerImpactSynth-tutorial.mp4" rel="noopener nofollow ugc">Video (2 min)</a> and <a href="https://github.com/vboussot/SlicerImpactSynth/blob/main/TUTORIAL.md" rel="noopener nofollow ugc">tutorial</a>.</p>
<p><strong>KonfAI</strong></p>
<p>The generic extension runs any KonfAI App on the volumes of the scene. Since February: apps added from any Hugging Face repository or local folder, with per-checkpoint download; an <strong>Advanced</strong> dialog for patch size, batch size and the parameters an app exposes, saved as a local app if you want; <strong>remote servers</strong> (<code>konfai-apps-server</code> on a GPU machine, its GPUs and memory shown in the panel); live RAM and VRAM gauges; fine-tuning setup; a launcher for KonfAI Studio. ImpactSynth and ImpactReg are built on the same library and get all of it.</p>
<p>Three videos of about a minute: <a href="https://github.com/vboussot/SlicerKonfAI/blob/main/Screenshots/SlicerKonfAI-inference.mp4" rel="noopener nofollow ugc">run a published app</a>, <a href="https://github.com/vboussot/SlicerKonfAI/blob/main/Screenshots/SlicerKonfAI-qa.mp4" rel="noopener nofollow ugc">quality assurance</a>, <a href="https://github.com/vboussot/SlicerKonfAI/blob/main/Screenshots/SlicerKonfAI-apps.mp4" rel="noopener nofollow ugc">apps and remote servers</a>; <a href="https://github.com/vboussot/SlicerKonfAI/blob/main/TUTORIAL.md" rel="noopener nofollow ugc">tutorial</a>.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8bf1194f350f70a07973692eed83e588cc9a667.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6fac561673caaefe33deda72772a3e8d7a1364d.jpeg" data-video-base62-sha1="sDSR7Iz43YSZTVUkrLpIbrholXp.mp4">
  </div><p></p>
<p><strong>Install</strong></p>
<p>View → Extensions Manager → <strong>ImpactSynth</strong> or <strong>KonfAI</strong> (Slicer 5.10 or newer). PyTorch comes from the SlicerPyTorch extension; a GPU with 8 GB of VRAM is enough.</p>
<p>Feedback and requests for other models are welcome.</p>
<p>Valentin Boussot, Cédric Hémon</p>
<p>Boussot V. et al., <em>TotalSynth: Robust Whole-Body Synthetic CT from MRI and CBCT</em>, arXiv:2609.13838, 2026.<br>
Boussot V., Dillenseger J.-L., <em>KonfAI: A Modular and Fully Configurable Framework for Deep Learning in Medical Imaging</em>, arXiv:2508.09823, 2025.</p>

---
