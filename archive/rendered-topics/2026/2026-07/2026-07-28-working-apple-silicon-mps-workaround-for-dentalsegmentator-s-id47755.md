---
topic_id: 47755
title: "Working Apple Silicon MPS workaround for DentalSegmentator / SlicerNNUnet under Rosetta"
date: 2026-07-28
url: https://discourse.slicer.org/t/47755
last_bumped: 2026-07-28T13:10:03.775Z
---

# Working Apple Silicon MPS workaround for DentalSegmentator / SlicerNNUnet under Rosetta

**Topic ID**: 47755
**Date**: 2026-07-28
**URL**: https://discourse.slicer.org/t/working-apple-silicon-mps-workaround-for-dentalsegmentator-slicernnunet-under-rosetta/47755

---

## Post #1 by @Carlo_Strada (2026-07-28 13:10 UTC)

<p>I tested a proof of concept that allows DentalSegmentator to use Apple Silicon GPU acceleration through MPS, while the main 3D Slicer application continues running as x86_64 under Rosetta.</p>
<h2><a name="p-135153-environment-1" class="anchor" href="#p-135153-environment-1" aria-label="Heading link"></a>Environment</h2>
<ul>
<li>MacBook Pro with Apple M3 Pro</li>
<li>3D Slicer 5.12.3 stable, x86_64</li>
<li>DentalSegmentator with SlicerNNUnet</li>
<li>nnUNetv2 2.8.1</li>
<li>Slicer-bundled PyTorch 2.2.2</li>
</ul>
<h2><a name="p-135153-problem-2" class="anchor" href="#p-135153-problem-2" aria-label="Heading link"></a>Problem</h2>
<p>Slicer reports that MPS is built and available, and DentalSegmentator accepts <code>mps</code> as its device. However, inference fails with:</p>
<pre><code class="lang-plaintext">RuntimeError: Conv3D is not supported on MPS
</code></pre>
<p>The problem appears to be the older x86_64 PyTorch build bundled with Slicer, rather than DentalSegmentator or nnUNet itself.</p>
<h2><a name="p-135153-proof-of-concept-3" class="anchor" href="#p-135153-proof-of-concept-3" aria-label="Heading link"></a>Proof of concept</h2>
<p>I created a separate native arm64 Python environment containing:</p>
<ul>
<li>PyTorch 2.13.0</li>
<li>torchvision 0.28.0</li>
<li>nnUNetv2 2.8.1</li>
</ul>
<p>A Conv3D smoke test succeeds on <code>mps:0</code> in this environment.</p>
<p>SlicerNNUnet was then pointed to a small wrapper:</p>
<pre data-code-wrap="sh"><code class="lang-sh">#!/bin/sh
unset PYTHONHOME PYTHONPATH
export PYTORCH_ENABLE_MPS_FALLBACK=1
exec "/path/to/native-arm64-venv/bin/nnUNetv2_predict" "$@"
</code></pre>
<p>Clearing <code>PYTHONHOME</code> and <code>PYTHONPATH</code> is necessary because otherwise the external interpreter imports nnUNet and dependencies from Slicer’s x86_64 Python environment.</p>
<p>For the proof of concept, I overrode <code>SegmentationLogic._findUNetPredictPath</code> from <code>.slicerrc.py</code> so that it returned the wrapper path.</p>
<h2><a name="p-135153-result-4" class="anchor" href="#p-135153-result-4" aria-label="Heading link"></a>Result</h2>
<ul>
<li>Complete DentalSegmentator run from the normal Slicer interface</li>
<li>Device: MPS</li>
<li>252/252 inference patches completed</li>
<li>Approximately 1.28 seconds per patch</li>
<li>Approximately 7 minutes total</li>
<li>CPU execution on the same system was approximately 9 seconds per patch, with an estimated total of 39 minutes</li>
<li>The resulting segmentation was successfully loaded back into Slicer</li>
</ul>
<p>This was tested on one Apple M3 Pro and one dental CT volume, so these numbers should not be treated as a formal benchmark. No image or patient data are being shared.</p>
<h2><a name="p-135153-possible-upstream-improvement-5" class="anchor" href="#p-135153-possible-upstream-improvement-5" aria-label="Heading link"></a>Possible upstream improvement</h2>
<p>Would the maintainers consider adding a supported advanced setting or environment variable for overriding the <code>nnUNetv2_predict</code> executable path?</p>
<p>This would allow SlicerNNUnet-based extensions to delegate inference to a native arm64 environment without requiring a full native Apple Silicon build of Slicer. The current <code>_findUNetPredictPath</code> override is useful as a proof of concept but relies on an internal method.</p>
<p>Relevant references:</p>
<ul>
<li>DentalSegmentator: <a href="https://github.com/gaudot/SlicerDentalSegmentator" class="inline-onebox" rel="noopener nofollow ugc">GitHub - gaudot/SlicerDentalSegmentator: 3D Slicer extension for fully-automatic segmentation of CT and CBCT dental volumes. · GitHub</a></li>
<li>SlicerNNUnet: <a href="https://github.com/KitwareMedical/SlicerNNUnet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerNNUnet: 3D Slicer nnUNet integration to streamline usage for nnUNet based AI extensions. · GitHub</a></li>
<li>PyTorch MPS documentation: <a href="https://docs.pytorch.org/docs/stable/notes/mps.html" class="inline-onebox" rel="noopener nofollow ugc">Redirecting…</a></li>
<li>PyTorch 2.13 MPS convolution implementation: <a href="https://github.com/pytorch/pytorch/blob/v2.13.0/aten/src/ATen/native/mps/operations/Convolution.mm" class="inline-onebox" rel="noopener nofollow ugc">pytorch/aten/src/ATen/native/mps/operations/Convolution.mm at v2.13.0 · pytorch/pytorch · GitHub</a></li>
</ul>
<p>I can provide the complete installation commands and help test a cleaner implementation if the approach is considered useful.</p>

---
