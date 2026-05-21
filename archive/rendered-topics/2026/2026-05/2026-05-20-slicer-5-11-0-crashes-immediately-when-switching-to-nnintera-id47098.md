---
topic_id: 47098
title: "Slicer 5 11 0 Crashes Immediately When Switching To Nnintera"
date: 2026-05-20
url: https://discourse.slicer.org/t/47098
---

# Slicer 5.11.0 crashes immediately when switching to nnInteractive module

**Topic ID**: 47098
**Date**: 2026-05-20
**URL**: https://discourse.slicer.org/t/slicer-5-11-0-crashes-immediately-when-switching-to-nninteractive-module/47098

---

## Post #1 by @aabrown100-git (2026-05-20 18:27 UTC)

<p>Using Slicer 5.11.0 on 2026 Macbook pro, M5 Pro chip.</p>
<p>After installing the nnInteractive extension and restarting Slicer, when I switch to the nnInteractive module, it tries to install some dependencies. Almost immediately, Slicer quits.</p>
<p>No issue when performing the same steps in Slicer 5.10.0.</p>
<p>Perhaps related to recent version compatibility changes to nnUnet? <a href="https://discourse.slicer.org/t/nnunet-fails-with-modulenotfounderror-no-module-named-torchvision-ops/46802/5" class="inline-onebox">nnUNet fails with ModuleNotFoundError: No module named 'torchvision.ops' - #5 by lassoan</a></p>

---

## Post #2 by @lassoan (2026-05-20 19:14 UTC)

<p>nnInteractive extension barely installs any dependencies, so I’m surprised that it runs into issues. It just needs <code>requests_toolbelt</code>, <code>scikit-image</code>, and (for testing) <code>matplotlib</code>. Could you please install these manually, for example: <code>pip_install("requests_toolbelt")</code>, and see if any of them causing trouble?</p>

---
