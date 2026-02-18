# General registration_(ANTs)

**Topic ID**: 40333
**Date**: 2024-11-22
**URL**: https://discourse.slicer.org/t/general-registration-ants/40333

---

## Post #1 by @Bor_Antolic (2024-11-22 13:54 UTC)

<p>I used the general registration (ANTs) with success until a few days ago. It started reporting error: /AppData/Local/Temp/Slicer/CBGEE_vtkMRMLScalarVolumeNodeH.nrrd does not exist</p>
<p>I tried reinstaling the SlicerANTs plugin, also the whole 3d Slicer, but the issue remains.<br>
Any ideas?</p>

---

## Post #2 by @muratmaga (2024-11-22 19:41 UTC)

<p>There is a newer implementation of ANTs that is going to do more than pairwise registration (template creation, groupwise, jacobean analysis) etc… Not all the features are fully functional yet on all platform, but if you are on windows, you can give a try:<br>
<a href="https://github.com/SlicerMorph/SlicerANTS" rel="noopener nofollow ugc"><br>
httsp://github.com/SlicerMorph/SlicerANTs</a></p>
<p>You do have to manually clone and install package. Use a preview version.</p>

---
