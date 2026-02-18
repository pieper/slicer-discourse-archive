# Building slicer on the NVIDIA Jetsontx2 not working

**Topic ID**: 16913
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/building-slicer-on-the-nvidia-jetsontx2-not-working/16913

---

## Post #1 by @ryleyreid (2021-04-01 23:58 UTC)

<p>I am trying to build 3D slicer on a single board computer, specifically the Jetsontx2 for a case study. The goal is to run 3Dslicer on the computer with a trained neural net to do local calibrations. The build hasn’t been cooperating and I am relatively inexperienced with computer architecture. It is okay if I can’t get the build to happen as I can still move forward with my case study I am just unsure why the build won’t work and what might be the cause. The boards specs are here and I am trying to use slicer3</p>
<p>OS: Ubuntu 18.04<br>
R32 (release), REVISION: 3.1, GCID: 18284527, BOARD: t186ref, EABI: aarch64, DATE: Mon Dec 16 21:38:34 UTC 2019</p>
<p>I am inexperienced with 3Dslicer and maybe usiug something wrong</p>

---

## Post #2 by @lassoan (2021-04-02 00:07 UTC)

<p>Does Slicer run on this computer?</p>
<p>Ubuntu 18.04 is 3 years old, so we don’t have matching build instructions for the latest Slicer version, but with some small changes you should be able to make <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html">these linux build instructions</a> work. If you encounter any problems then upload the full build log somewhere and post the link here.</p>

---

## Post #3 by @ryleyreid (2021-04-02 00:33 UTC)

<p>for my current project, I was required to attempt the build on the NVIDIA jetsontx2 that has an ARM 64 architecture. From what I learned I would have to rebuild the binary on an AMD64 machine but for the ARM64(aarch64) system and transfer it over. Is it even possible to rebuild 3Dslicer this way? If it is would any substantial changes need to be made. My professor overseeing our project and I do not have in-depth knowledge of the challenges this may cause. Since I knew the most about computer architecture (or at least I thought I did) I took on this task and have been stuck for a while now.</p>

---

## Post #4 by @lassoan (2021-04-03 01:26 UTC)

<p>If it’s ARM then you definitely need to build Slicer yourself. I don’t expect any issues with Slicer code, but mostly with VTK and Qt.</p>
<p>So, first start with the most risky component - Qt. It can be built for many embedded systems, so I would expect that it is possible to build for this single-board computer, too, but it may require a lot of experimentation. If all Qt examples work well then build VTK9. If both Qt and VTK works well then building and running Slicer should be OK, too.</p>

---
