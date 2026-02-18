# 📢 New 3D Slicer Extensions: KonfAI & IMPACT-Synth Reliable AI Synthetic CT and Segmentation with Integrated QA

**Topic ID**: 46032
**Date**: 2026-02-02
**URL**: https://discourse.slicer.org/t/new-3d-slicer-extensions-konfai-impact-synth-reliable-ai-synthetic-ct-and-segmentation-with-integrated-qa/46032

---

## Post #1 by @vboussot (2026-02-02 14:55 UTC)

<p>Dear All,</p>
<p>We are happy to announce the release of <strong>two new open-source 3D Slicer extensions</strong>, <strong><a href="https://github.com/vboussot/SlicerKonfAI" rel="noopener nofollow ugc">KonfAI</a></strong> and <strong><a href="https://github.com/vboussot/SlicerImpactSynth" rel="noopener nofollow ugc">IMPACT-Synth</a></strong>, which provide graphical interfaces to run AI tasks (such as <strong>segmentation</strong> and <strong>synthetic CT generation</strong>) through <strong>KonfAI Apps</strong> directly inside Slicer.</p>
<p>With <strong>KonfAI</strong>, you can load patient images, select a <strong>KonfAI App</strong>, run inference, and immediately visualize the results as <strong>volumes or segmentations</strong>.</p>
<p>You can then perform <strong>quality assurance</strong> by evaluating predictions when a reference is available, or <strong>estimate uncertainty</strong> when no reference is available using <strong>test-time augmentation (TTA)</strong>, <strong>Monte Carlo dropout</strong>, or <strong>model ensembling</strong>.</p>
<h3><a name="p-131713-what-is-konfai-1" class="anchor" href="#p-131713-what-is-konfai-1" aria-label="Heading link"></a><strong><img src="https://emoji.discourse-cdn.com/twitter/wrench.png?v=15" title=":wrench:" class="emoji" alt=":wrench:" loading="lazy" width="20" height="20"> What is KonfAI?</strong></h3>
<p>The KonfAI extension is the graphical interface built on top of KonfAI, a modular and fully configurable deep learning framework for medical imaging, where complete training, inference, and evaluation pipelines are defined declaratively through YAML configuration files.</p>
<p>This design enables reproducible, transparent, and flexible AI workflows, with native support for advanced strategies such as patch-based processing, test-time augmentation, model ensembling, and multi-output supervision, and has been successfully applied to segmentation and image synthesis tasks.</p>
<p>Reference:</p>
<p>Boussot, V., Dillenseger, J.-L., KonfAI: A Modular and Fully Configurable Framework for Deep Learning in Medical Imaging, arXiv:2508.09823, 2025.</p>
<h3><a name="p-131713-built-in-konfai-apps-2" class="anchor" href="#p-131713-built-in-konfai-apps-2" aria-label="Heading link"></a><strong><img src="https://emoji.discourse-cdn.com/twitter/package.png?v=15" title=":package:" class="emoji" alt=":package:" loading="lazy" width="20" height="20"> Built-in KonfAI Apps</strong></h3>
<p>KonfAI comes with several <strong>ready-to-use Apps</strong> covering <strong>segmentation</strong> and <strong>synthesis</strong>, all with <strong>built-in evaluation and uncertainty estimation</strong>.</p>
<h4><a name="p-131713-segmentation-apps-3" class="anchor" href="#p-131713-segmentation-apps-3" aria-label="Heading link"></a><strong><img src="https://emoji.discourse-cdn.com/twitter/brain.png?v=15" title=":brain:" class="emoji" alt=":brain:" loading="lazy" width="20" height="20"> Segmentation Apps</strong></h4>
<p><strong><a href="https://github.com/vboussot/KonfAI/blob/main/apps/mrsegmentator" rel="noopener nofollow ugc">MRSegmentator</a></strong></p>
<ul>
<li><strong>Evaluation</strong>: Dice, error maps</li>
<li><strong>Uncertainty</strong>: uncertainty maps (via model ensembling)</li>
<li><strong>Optimized variant of the original MRSegmentator</strong>:
<ul>
<li>~<strong>3–4× faster inference</strong></li>
<li>~<strong>2.8× lower RAM usage</strong> (≈ 30 GB vs ≈ 83 GB)</li>
<li><strong>Input volume size</strong>: 512 × 512 × 366</li>
</ul>
</li>
</ul>
<p><strong><a href="https://github.com/vboussot/KonfAI/blob/main/apps/totalsegmentator" rel="noopener nofollow ugc">TotalSegmentator</a></strong></p>
<ul>
<li><strong>Evaluation</strong>: Dice, error maps</li>
<li><strong>Optimized variant of the original TotalSegmentator</strong></li>
<li><strong>Available models</strong>:
<ul>
<li>total</li>
<li>total 3mm</li>
<li>total-mr</li>
<li>total-mr 3mm</li>
</ul>
</li>
</ul>
<p>These segmentation Apps reuse pretrained checkpoints from the original tools, while adding <strong>built-in evaluation and uncertainty estimation</strong> and <strong>significantly improving inference speed</strong>, enabling their use as <strong>downstream tasks</strong>, for example for <strong>synthetic CT evaluation</strong>.</p>
<h4><a name="p-131713-synthesis-appshttpsgithubcomvboussotkonfaitreemainappsimpact_synth-4" class="anchor" href="#p-131713-synthesis-appshttpsgithubcomvboussotkonfaitreemainappsimpact_synth-4" aria-label="Heading link"></a><strong><img src="https://emoji.discourse-cdn.com/twitter/test_tube.png?v=15" title=":test_tube:" class="emoji" alt=":test_tube:" loading="lazy" width="20" height="20"> <a href="https://github.com/vboussot/KonfAI/tree/main/apps/impact_synth" rel="noopener nofollow ugc">Synthesis Apps</a></strong></h4>
<p><strong>CBCT → CT and MR → CT synthesis</strong></p>
<p>Shared features:</p>
<ul>
<li><strong>Evaluation</strong>: MAE, PSNR, SSIM</li>
<li><strong>Downstream evaluation</strong>: Dice (via automatic segmentation)</li>
<li><strong>Uncertainty</strong>: uncertainty maps and conformity maps (via TTA and model ensembling)</li>
</ul>
<p>These synthesis Apps are primarily intended for <strong>domain adaptation</strong>, enabling task pipelines originally designed for <strong>CT</strong> to be applied to <strong>MRI or CBCT</strong> data via synthetic CT generation, with direct applications in <strong>radiotherapy dose calculation</strong> or segmentation.</p>
<p>The two synthesis and segmentations Apps are integrated into a <strong>dedicated 3D Slicer extension, IMPACT-Synth</strong>, which provides an <strong>end-to-end environment</strong> for synthetic CT generation, evaluation, and quality assurance.</p>
<p>We also plan to <strong>further develop and release more robust synthesis models</strong> as part of this extension.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e1b62dbef02a7e8b9fe723bc6d4eec050a6d4ef.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52bb8ca9dffa1f117fc321986c13c61d7e790318.jpeg" data-video-base62-sha1="8RqhdIIA0epYYxQLP7AzYWIwOOb.mp4">
  </div><p></p>
<p><strong><img src="https://emoji.discourse-cdn.com/twitter/books.png?v=15" title=":books:" class="emoji" alt=":books:" loading="lazy" width="20" height="20"> Training and methodology</strong></p>
<p>The synthesis models were <strong>trained on the SynthRAD2025 dataset</strong>, following the methodology described in our recent work:</p>
<p>Boussot, V., Hémon, C., Nunes, J.-C., Dillenseger, J.-L., <em>Why Registration Quality Matters: Enhancing sCT Synthesis with IMPACT-Based Registration</em>, arXiv:2510.21358, 2025.</p>
<p>Training relies on the <strong>IMPACT-Synth loss</strong> to enforce semantic and structural consistency, and uses <strong>IMPACT-Reg–based registration</strong> to pre-align multimodal training pairs, improving anatomical fidelity and robustness of the generated synthetic CTs.</p>

---
