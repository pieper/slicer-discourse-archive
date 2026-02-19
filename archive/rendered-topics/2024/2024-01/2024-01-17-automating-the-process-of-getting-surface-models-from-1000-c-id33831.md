---
topic_id: 33831
title: "Automating The Process Of Getting Surface Models From 1000 C"
date: 2024-01-17
url: https://discourse.slicer.org/t/33831
---

# Automating the process of getting surface models from 1000 CTs

**Topic ID**: 33831
**Date**: 2024-01-17
**URL**: https://discourse.slicer.org/t/automating-the-process-of-getting-surface-models-from-1000-cts/33831

---

## Post #1 by @paleomariomm (2024-01-17 16:19 UTC)

<p>Dear community.<br>
We have 1000 baboon scans in DICOM files.</p>
<p>In our research, we thought and tested a pipeline to work with each of them.</p>
<ul>
<li>First, we need to crop the volume as all of them show a platform placed centimeters below the mandible.</li>
<li>Second, we need to do a segmentation of the full skull by using Threshold and a specific set of parameters.</li>
<li>Third, we need to create a surface model from the segmented skull.</li>
<li>Fourth, we need to export the surface model in .ply format to run ALPACA/MALPACA (from SlicerMorph)</li>
<li>Fifth, we need to save all the scene of every skull.</li>
</ul>
<p>As this pipeline is well established, with parameters defined, is there a way to automate the process to be run over 1000 scans instead of doing this one by one?</p>
<p>Best</p>

---

## Post #2 by @muratmaga (2024-01-17 16:27 UTC)

<p>All of this is doable via python scripting. The only step is the ROI placement in your first one. If you are <strong>certain</strong> is always 1cm below, you can create fixed sized ROI with that dimensions, and use it with the crop tool.</p>
<p>Everything else is fairly straightforward, if you are familiar with python. You should start with the Python Script Repository, which would have examples of python codes for most of your tasks.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#script-repository" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#script-repository</a></p>

---

## Post #3 by @paleomariomm (2024-01-17 16:40 UTC)

<p>Thank you Murat. I am not that familiar with Python as with R, but will try. However, I found and extension (Pipeline creator) in the Extension manager. I installed it, but it only works in Slicer 5.2, but not in 5.4 or 5.6.1 <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @muratmaga (2024-01-17 17:05 UTC)

<p>Pipeline creator works for only some of the modules, specifically modules that use the command line interface. So i don’t think it will be much of use to you.</p>
<p>Python scripting is really not that difficult and it is also very valuable skill to have. Start with trying to crop your volumes with a specific ROI, and saving it a new volume to disk. Then move onto the next step and so forth, and finally put them together in a loop that will parse the files in a folder and execute the steps, and save them.</p>

---

## Post #5 by @paleomariomm (2024-01-18 12:34 UTC)

<p>Thank you for your tips. I will let you know how the process advances</p>

---
