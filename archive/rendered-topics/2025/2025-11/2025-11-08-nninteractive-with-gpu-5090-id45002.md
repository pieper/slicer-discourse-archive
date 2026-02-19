---
topic_id: 45002
title: "Nninteractive With Gpu 5090"
date: 2025-11-08
url: https://discourse.slicer.org/t/45002
---

# nnInteractive with GPU 5090

**Topic ID**: 45002
**Date**: 2025-11-08
**URL**: https://discourse.slicer.org/t/nninteractive-with-gpu-5090/45002

---

## Post #1 by @rakshrma (2025-11-08 06:49 UTC)

<p>Hi -</p>
<p>I am interested to use nnInteractive extension on Nvidia 5090 series laptop. Unfortunately, whenever I try to use Totalsegmentator or nnInteractive, it re-installs an older version of pytorch which is incompatible with Cuda 13.0. Could you please help?</p>

---

## Post #2 by @muratmaga (2025-11-08 07:06 UTC)

<p>If you are using the PyTorch extension to install the torch, I think it doesn’t bring anything newer than cuda 12.6 (at least that has been my experience).</p>
<p>If you need torch with cuda 13.0, you probably need to manually install it using the command from torch site:</p>
<pre><code class="lang-auto">pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu130
</code></pre>
<p>So perhaps something like this in Slicer’ python:</p>
<pre><code class="lang-auto">slicer.util.pip_install(['torch', 'torchvision', '--index-url', 'https://download.pytorch.org/whl/cu130'])
</code></pre>

---
