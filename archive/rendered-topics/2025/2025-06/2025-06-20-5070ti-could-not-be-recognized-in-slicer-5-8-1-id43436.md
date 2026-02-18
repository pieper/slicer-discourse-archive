# 5070ti could not be recognized in slicer 5.8.1

**Topic ID**: 43436
**Date**: 2025-06-20
**URL**: https://discourse.slicer.org/t/5070ti-could-not-be-recognized-in-slicer-5-8-1/43436

---

## Post #1 by @reka_wolf (2025-06-20 14:47 UTC)

<p>5070ti could not be recognized in slicer 5.8.1.<br>
The newest cuda 12.8 is only for 50series, but it could not be supported in slicer 5.8.1 which cuda version is 12.6.<br>
Please help</p>

---

## Post #2 by @chz31 (2025-06-20 22:12 UTC)

<p>Is it possible to install it manually such as go to terminal, then go to Slicer-5.8.1./bin and run ./PythonSlicer -m pip install to install pytorch with cu128?</p>

---

## Post #4 by @jamesobutler (2025-06-20 23:19 UTC)

<p>There are indeed Python 3.9 whls for cu128 torch.</p>
<p>See <a href="https://download.pytorch.org/whl/torch/" rel="noopener nofollow ugc">https://download.pytorch.org/whl/torch/</a></p>
<blockquote>
<p>torch-2.7.1+cu128-cp39-cp39-manylinux_2_28_aarch64.whl<br>
torch-2.7.1+cu128-cp39-cp39-manylinux_2_28_x86_64.whl<br>
torch-2.7.1+cu128-cp39-cp39-win_amd64.whl</p>
</blockquote>

---

## Post #5 by @Mark_Ryan (2025-06-22 14:34 UTC)

<p>This is what I entered into python console in slicer. 4 GB download so takes a while:</p>
<p>slicer.util.pip_install(“torch torchvision torchaudio --index-url <a href="https://download.pytorch.org/whl/cu128" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cu128</a>”)</p>

---
