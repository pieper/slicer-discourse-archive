---
topic_id: 23940
title: "Compile Slicer In Ubuntu 20 04 Fails"
date: 2022-06-19
url: https://discourse.slicer.org/t/23940
---

# Compile Slicer in Ubuntu(20.04) fails

**Topic ID**: 23940
**Date**: 2022-06-19
**URL**: https://discourse.slicer.org/t/compile-slicer-in-ubuntu-20-04-fails/23940

---

## Post #1 by @SteveLiu (2022-06-19 11:07 UTC)

<p>Operating system: Ubuntu20.04 (VirtualBox)<br>
Slicer version: latest version<br>
Expected behavior: make the project<br>
Actual behavior: make the project failure</p>
<p>git: git version 2.25.1<br>
cmake: cmake version 3.16.3</p>
<p>I created a new Ubuntu20.04 system in virtualbox. Downloaded the pre-requisites and made the project accroding to: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#any-distribution" rel="noopener nofollow ugc">GNU/Linux systems — 3D Slicer documentation</a></p>
<p>I am quite pointless about how to solve the error because of so many dependencies.<br>
This is the output from terminal: <a href="https://drive.google.com/file/d/1y3Khxtt8afd8uRKwjc61vx8_Caf9RFS1/view?usp=sharing" rel="noopener nofollow ugc">ubuntu make slicer.txt - Google Drive</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/923098bf8e8869486420bc7895a5ca1c0cf0cf94.png" data-download-href="/uploads/short-url/kRfPn37RnSnAtRLtbQ0tLPo3EUs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/923098bf8e8869486420bc7895a5ca1c0cf0cf94.png" alt="image" data-base62-sha1="kRfPn37RnSnAtRLtbQ0tLPo3EUs" width="690" height="146" data-dominant-color="422036"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">902×191 37.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mau_igna_06 (2022-06-19 15:00 UTC)

<p>Is dcmtk on your cmake variables?</p>

---

## Post #3 by @SteveLiu (2022-06-19 15:09 UTC)

<p>Yes I didn’t change the default variables for Cmake. I was building release version and according to “common error” set git protocol=false</p>

---

## Post #4 by @mau_igna_06 (2022-06-19 15:10 UTC)

<p>Did you try not doing that second thing?</p>

---

## Post #5 by @SteveLiu (2022-06-19 15:14 UTC)

<p>Yes. I tried but did not work.<br>
Btw I use make -jN -k to use more cpu. I don’t know is it the problem. I am trying to use just make to build it again.</p>

---

## Post #6 by @pieper (2022-06-19 19:03 UTC)

<p>I did a fresh build on ubuntu 20.04 and did not run into this error so it’s possibly something with your virtual box maybe running out of disk space or memory.  I did <code>make -j20</code> on a 12 core machine.  Try completely deleting your superbuild directory and starting from scratch in case there were any failed build files left behind by accident.</p>

---
