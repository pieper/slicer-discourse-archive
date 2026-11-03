---
topic_id: 48679
title: "Use torchvulkan to enable gpu segmentations in totalsegmentator"
date: 2026-11-02
url: https://discourse.slicer.org/t/48679
last_bumped: 2026-11-02T20:35:23.601Z
---

# Use torchvulkan to enable gpu segmentations in totalsegmentator

**Topic ID**: 48679
**Date**: 2026-11-02
**URL**: https://discourse.slicer.org/t/use-torchvulkan-to-enable-gpu-segmentations-in-totalsegmentator/48679

---

## Post #1 by @Alex_Vergara (2026-11-02 20:35 UTC)

<p>This is very specific to totalsegmentator, please <a class="mention" href="/u/wasserth">@wasserth</a> read the following</p>
<p>Currently, Total Segmentator uses torch that can use a nvidia card, if the user doesn’t have it it default to slow CPU. But there is a marvelous package <a href="https://github.com/zainsharief/torchvulkan" class="inline-onebox" rel="noopener nofollow ugc">GitHub - zainsharief/torchvulkan: Cross-Platform Vulkan Backend for PyTorch · GitHub</a> that I have tested it works really good, that adds Vulkan computation capabilities to torch, ENABLING ALL GPUs, not just nvidia. Two changes required:</p>
<pre data-code-wrap="python"><code class="lang-python">import torchvulkan
device = torch.device("vulkan" if torchvulkan.is_available() else "cpu")
</code></pre>
<p>That’s it, it would run a lot faster in AMD cards for instance, it also allows the use of MoltenVk in macos.</p>

---
