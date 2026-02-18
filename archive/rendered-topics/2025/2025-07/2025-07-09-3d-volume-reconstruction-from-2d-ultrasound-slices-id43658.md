# 3D Volume Reconstruction from 2D Ultrasound Slices

**Topic ID**: 43658
**Date**: 2025-07-09
**URL**: https://discourse.slicer.org/t/3d-volume-reconstruction-from-2d-ultrasound-slices/43658

---

## Post #1 by @martina_paccini (2025-07-09 00:45 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.8.1<br>
Expected behavior: volume reconstruction and rendering<br>
Actual behavior: crash<br>
Hi everyone,</p>
<p>I’m quite new to 3D Slicer and this community. I’m trying to reconstruct a 3D volume from a sequence of 2D ultrasound slices. For each slice, I have the corresponding position and orientation as a 4x4 transformation matrix.</p>
<p>I’m currently using the Volume Reconstruction module from the SlicerIGT extension. I started from the code example provided in this <a href="https://discourse.slicer.org/t/segmentation-of-mitral-valve/14598">forum thread</a>, replacing the synthetic rotations with my actual 4x4 transform matrices. However, my code keeps crashing, and I suspect I’m not setting up the nodes correctly.</p>
<p>At the moment, I’m using an <code>.mha</code> volume as input, but I also have the original stack as individual <code>.png</code> files.</p>
<p>My main questions</p>
<p>Is it a good idea to start from the example linked above? Or would it be better to build everything from scratch?<br>
Could someone help me understand how to correctly set up the transform and image nodes for volume reconstruction?</p>
<p>Any guidance or sample code would be greatly appreciated!</p>
<p>Thank you,</p>

---

## Post #2 by @lassoan (2025-07-09 00:47 UTC)

<p>Volume reconstruction in SlicerIGT is very solid. The only known way it can crash is that if you run out of memory. You can run out of memory if you set a too small image spacing and/or set the reconstructed region too large. You can increase the virtual or physical memory in your computer, increase spacing, or reduce reconstructed region to avoid running out of memory.</p>

---

## Post #3 by @sohan.ranjan (2026-01-30 18:01 UTC)

<p>I am looking for a user guide for 3D Ultrasound Volume reconstruction from pre-stored 2D NiFTi slices using SlicerIGT in 3D Slicer 5.10. I did load the sliced using AddData, and then invoking Volume Reconstruction from SlicerIGT. But the “Start” button for reconstruction remained grayed.</p>

---

## Post #4 by @ungi (2026-01-30 18:04 UTC)

<p>The Volume Reconstruction module currently only works if the recorded data is saved in Slicer Sequences. To make it work with your data, you would need to write a python script that creates a sequence browser node, adds sequences to the browser for the image node and for the tracking (transform node), and loads your data in those containers.</p>

---

## Post #5 by @sohan.ranjan (2026-01-30 23:53 UTC)

<p>Can you please elaborate or suggest links which could help me understand what it means and how to go about it? Thanks.</p>

---

## Post #6 by @ungi (2026-01-31 01:31 UTC)

<p>You just need to specify for an LLM what format your data is currently in, and what format you would like to convert to. Most coding models or even ChatGPT creates (almost always) correct code to questions like “Write a python script for 3D Slicer that takes a 3D volume node and creates a sequence (time series) of 2D nodes from it.”<br>
I would start with simple examples, maybe only do the images or the transformations first.<br>
If you are not familiar with Slicer coding terminology, you can start the conversation by asking an LLM to explain the relevant terms.</p>
<p>I think it’s well worth doing the basic tutorials without AI help first, so you understand the data structure (MRML) of Slicer and how they are visualized: <a href="https://training.slicer.org/" rel="noopener nofollow ugc">3D Slicer Training Compendium | 3D Slicer</a></p>
<p>This is a good resource if you need script examples to learn from or provide them as context along with your question to your coding LLM: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>

---
