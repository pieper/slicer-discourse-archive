# Dependency conflict

**Topic ID**: 37038
**Date**: 2024-06-26
**URL**: https://discourse.slicer.org/t/dependency-conflict/37038

---

## Post #1 by @Aamir_Khan1 (2024-06-26 12:14 UTC)

<p>HI,</p>
<p>I have developed a custom 3d slicer module. It used to call a deep learning module and executes the code perfectly.<br>
This is the repo:<br>
<a href="https://github.com/AMK-AQ/CTPelvic1K" rel="noopener nofollow ugc">AMK-AQ/CTPelvic1K: Resources of the paper “Deep Learning to Segment Pelvic Bones: Large-scale CT Datasets and Baseline Models”. This version is compatible with Windows also. (github.com)</a></p>
<p>But as I upgraded my python to 3.12, it started to throw error, as standard library module disutils got deprecated in this version.</p>
<p>Now, if I install the CTPelvic1K with poetry and create a virtual environemnt with 3.10, everything works fine.</p>
<p>I wanted to ask, is there a way to activate a virtual environemnt through python , execute my deep learning code and exit the environment?</p>
<p>Or should I use some other option, like docker etc?</p>
<p>Thanks</p>

---
