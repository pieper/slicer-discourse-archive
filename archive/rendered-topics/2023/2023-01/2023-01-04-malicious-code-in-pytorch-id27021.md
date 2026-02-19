---
topic_id: 27021
title: "Malicious Code In Pytorch"
date: 2023-01-04
url: https://discourse.slicer.org/t/27021
---

# Malicious code in pyTorch

**Topic ID**: 27021
**Date**: 2023-01-04
**URL**: https://discourse.slicer.org/t/malicious-code-in-pytorch/27021

---

## Post #1 by @muratmaga (2023-01-04 00:45 UTC)

<p>Should we be concerned about this?</p>
<blockquote>
<p>If you installed PyTorch-nightly on Linux via pip between December 25, 2022 and December 30, 2022, please uninstall it and torchtriton immediately, and use the latest nightly binaries (newer than Dec 30th 2022).</p>
</blockquote>
<p><code>https://pytorch.org/blog/compromised-nightly-dependency/</code></p>

---

## Post #2 by @pieper (2023-01-04 00:51 UTC)

<p>Thanks for posting, that’s a scary precedent.</p>
<p>Maybe someone can confirm, but I believe our installers would only have provided the stable releases and not the nightlies for PyTorch.</p>

---
