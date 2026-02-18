# What is the right way for loading 3D dose volumes from jupyter kernel

**Topic ID**: 17651
**Date**: 2021-05-17
**URL**: https://discourse.slicer.org/t/what-is-the-right-way-for-loading-3d-dose-volumes-from-jupyter-kernel/17651

---

## Post #1 by @meika_poika (2021-05-17 12:34 UTC)

<p>Hi!</p>
<p>I’m doing an AI-based RT-project with Slicer, but I’ve been stuck on trying to find a way to load 3D dose images to the scene from jupyter kernel. I want to do some image registration/resampling recursively, but my main problem is that I’m not able to load 3D Doses from RT-DOSE dicom file to the slicers scene using loadVolume.</p>
<blockquote>
<p>dose = glob.glob(os.path.join(patients[6], ‘RD*.dcm’))<br>
propD = {‘name’:‘Dose’}<br>
Doseimg = slicer.util.loadVolume(dose, propD)</p>
</blockquote>
<p>LoadVolume works perfectly with CT stacks, but this is something that I haven’t been able to figure out by myself. Hope someone can help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2021-05-17 13:05 UTC)

<p>You must to load DICOM data objects using DICOM module. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder">script repository</a>.</p>

---
