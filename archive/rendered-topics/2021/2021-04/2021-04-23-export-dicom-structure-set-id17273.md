# Export Dicom Structure Set

**Topic ID**: 17273
**Date**: 2021-04-23
**URL**: https://discourse.slicer.org/t/export-dicom-structure-set/17273

---

## Post #1 by @m4l7 (2021-04-23 12:27 UTC)

<p>Operating system: WIndows 10<br>
Slicer version: 4.11<br>
Expected behavior: When modifiying an existing or creating a new segmentation set with respect to a master volume (e.g. CT) and saving it back (doing the described export dicom workflow) I expect that the RT Stucture file is linked to the actual master volume.<br>
Actual behavior: During the Export Dicom step a “new” CT image is generated automatically. The RT Struct Set File is not linked to the original Master Volume which has been used for segmentation.</p>

---

## Post #2 by @cpinter (2021-04-23 13:47 UTC)

<p>This is a limitation of the current implementation of DICOM export in Plastimatch, that it always create a new CT with new UIDs.</p>
<p>We are actually starting a maintenance project on Plastimatch quite soon now, which will first focus on burning infrastructure and modernization, but it is not impossible that we will work on issues like this. Please add an issue here</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://gitlab.com/assets/favicon-7901bd695fb93edb07975966062049829afb56cf11511236e61bcf425070e36e.png" class="site-icon" width="16" height="16">
      <a href="https://gitlab.com/plastimatch/plastimatch/-/issues" target="_blank" rel="noopener">GitLab</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:67/68;"><img src="https://assets.gitlab-static.net/uploads/-/system/project/avatar/1421987/p.png" class="thumbnail" width="67" height="68"></div>

<h3><a href="https://gitlab.com/plastimatch/plastimatch/-/issues" target="_blank" rel="noopener">Issues · plastimatch / plastimatch</a></h3>

<p>Plastimatch is an open source software for image computation. Our main focus is high-performance volumetric registration, segmentation, and image processing of volumetric medical images.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<p>
and describe your use case.</p>

---

## Post #3 by @m4l7 (2021-04-23 14:07 UTC)

<p>Thanks for your reply! I will open up an issue there.</p>
<p>But for now. Do you know if there is a workaround to reconnect the RT Structure Set to the original Master Image?</p>
<p>Thanks again!</p>

---

## Post #4 by @cpinter (2021-04-23 15:01 UTC)

<p>It should be possible to use <code>dcmodify</code> from DCMTK to set the reference to the original CT. Maybe pydicom can do it also if that’s more convenient for you but I haven’t used it yet.</p>

---
