---
topic_id: 21404
title: "Visualisation Of Spectroscopy Data In 3Dslicer"
date: 2022-01-11
url: https://discourse.slicer.org/t/21404
---

# Visualisation of spectroscopy data in 3dslicer

**Topic ID**: 21404
**Date**: 2022-01-11
**URL**: https://discourse.slicer.org/t/visualisation-of-spectroscopy-data-in-3dslicer/21404

---

## Post #1 by @Haytham (2022-01-11 08:40 UTC)

<p>Operating system: window<br>
Hello everyone,<br>
I am a medical researcher, and my current project is about the visualisation of spectroscopy image data in 3Dslicer.<br>
I need to represent for every voxel, the spectrum.<br>
i want to represent the spectrum for each voxel in a graph. when I click on a voxel its spectrum must represent in a graph. It is possible to do it with slicer?  what is the code to follow?</p>

---

## Post #2 by @mikebind (2022-01-11 17:38 UTC)

<p>A quick search for existing Slicer extensions for spectroscopy didn’t yield anything, so you may need to develop something yourself. If you are willing to invest some time, this may not be too difficult, and this forum is a very supportive and helpful community.</p>
<p>Once you have the spectrum you want to show, you can generate plots using this infrastructure: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/plots.html" class="inline-onebox">Plots — 3D Slicer documentation</a></p>

---

## Post #3 by @pieper (2022-01-11 23:46 UTC)

<p>There’s been some work on this in the past with older Slicer versions but you could probably get some good ideas.</p>
<aside class="onebox pdf" data-onebox-src="https://radiology.ucsf.edu/sites/radiology.ucsf.edu/files/import/filemanager/Menze_Multi-Modal_MR_Spectroscopy_ISMRM_2011.pdf">
  <header class="source">

      <a href="https://radiology.ucsf.edu/sites/radiology.ucsf.edu/files/import/filemanager/Menze_Multi-Modal_MR_Spectroscopy_ISMRM_2011.pdf" target="_blank" rel="noopener">radiology.ucsf.edu</a>
  </header>

  <article class="onebox-body">
    <a href="https://radiology.ucsf.edu/sites/radiology.ucsf.edu/files/import/filemanager/Menze_Multi-Modal_MR_Spectroscopy_ISMRM_2011.pdf" target="_blank" rel="noopener"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://radiology.ucsf.edu/sites/radiology.ucsf.edu/files/import/filemanager/Menze_Multi-Modal_MR_Spectroscopy_ISMRM_2011.pdf" target="_blank" rel="noopener">Menze_Multi-Modal_MR_Spectroscopy_ISMRM_2011.pdf</a></h3>

  <p class="filesize">934.75 KB</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2022-01-18 02:48 UTC)

<p>If the spectrum is a 1D signal for each voxel then you can use plotting in either Multivolume Explorer or in Sequences module:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/MultiVolumeExplorer" class="inline-onebox">Documentation/Nightly/Modules/MultiVolumeExplorer - Slicer Wiki</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html" class="inline-onebox">Sequences — 3D Slicer documentation</a></li>
</ul>
<p>You can create a 4D nrrd file (that Sequences or MultiVolumeExplorer can read) using MultiVolumeImporter module, or concatenate multiple scalar volumes (each containing one value of the spectrum) into single volume sequence using Sequences module, or you can create it from a 4D numpy array using Python scripting as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-a-4d-volume-in-python-outside-slicer">here</a>.</p>

---

## Post #5 by @DanceWithFeathers (2025-01-02 09:55 UTC)

<p>Thanks for your paper, where can I find Slicer v3.6 and SIVIC-Slicer module?which are mentioned in this paper. The Oldest Slicer version I found now is 4.0.0</p>

---
