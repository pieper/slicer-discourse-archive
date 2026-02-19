---
topic_id: 15696
title: "Convert Mhd Dose Volume To Rtdose File And Export"
date: 2021-01-27
url: https://discourse.slicer.org/t/15696
---

# Convert .mhd dose volume to RTDose file and export

**Topic ID**: 15696
**Date**: 2021-01-27
**URL**: https://discourse.slicer.org/t/convert-mhd-dose-volume-to-rtdose-file-and-export/15696

---

## Post #1 by @p4perz (2021-01-27 14:25 UTC)

<p>The output of my Monte Carlo simulations for the dose distributions are multiple .mha dose volumes.</p>
<p>I would aim to compare them to other dose distributions and overlap them with CT DICOMs.</p>
<p>There are many tools available for RTDose files and I think it is a good idea to convert my 3D .mha dose volumes to an RTDose file.</p>
<p>You can see the output format of my dose volumes in the Dropbox link below. There is one of many dose volumes “DoseVolume000_CP0000.mha” in the folder as well as an “example_RTDose”.</p>
<p><a href="https://www.researchgate.net/deref/https%3A%2F%2Fwww.dropbox.com%2Fhome%2FdoseExample" rel="noopener nofollow ugc">https://www.dropbox.com/home/doseExample</a></p>

---

## Post #2 by @cpinter (2021-01-27 15:13 UTC)

<p>You can export DICOM files like this:</p><div class="youtube-onebox lazy-video-container" data-video-id="nzWf4xHy1BM" data-video-title="Create DICOM files from CT volume and segmentation" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=nzWf4xHy1BM" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/nzWf4xHy1BM/maxresdefault.jpg" title="Create DICOM files from CT volume and segmentation" width="" height="">
  </a>
</div>

<p>To export RTDOSE:</p>
<ul>
<li>Have the SlicerRT extension installed</li>
<li>Have a Patient/Study in the Data module</li>
<li>In the Study have the CT and the dose volume</li>
<li>Convert the regular volume node (grayscale) to dose volume (colored) via the right-click menu</li>
<li>Export the study as you see in the video</li>
</ul>

---

## Post #3 by @sjagabattuni (2024-03-04 23:07 UTC)

<p>Hi, is there a way to export the RT Dose file without having to include the whole CT series?</p>

---
