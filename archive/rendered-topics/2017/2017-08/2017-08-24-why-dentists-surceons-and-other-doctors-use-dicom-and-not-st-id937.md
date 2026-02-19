---
topic_id: 937
title: "Why Dentists Surceons And Other Doctors Use Dicom And Not St"
date: 2017-08-24
url: https://discourse.slicer.org/t/937
---

# Why dentists, surceons and other doctors use DICOM and not STL?

**Topic ID**: 937
**Date**: 2017-08-24
**URL**: https://discourse.slicer.org/t/why-dentists-surceons-and-other-doctors-use-dicom-and-not-stl/937

---

## Post #1 by @j.avdeev (2017-08-24 17:57 UTC)

<p>Hello.<br>
Does anyone know the reasons - why doctors use DICOM viewers for analysis and diagnosis.<br>
In respect that during this analysis doctor need to create some surfaces, lines, measure angles between lines and between points - all this activities much more easier to do in any CAD software, also results of this STL are ready to manufacturing, for example for 3D printing.</p>
<p>Why processes, when doctors use DICOM for analysis are so popular, why not to convert DICOM to STL before this analysis.</p>
<p>One of possible reasons is some error - during DICOM-&gt;STL conversion we loose some small details.<br>
Are there any other reasons?</p>

---

## Post #2 by @muratmaga (2017-08-24 18:15 UTC)

<p>If all you need to do is what you describe, yes, models probably will suffice.</p>
<p>However, that’s not what most people use DICOMs for. Volumetric data is more information-rich than models that are generated from them. Intensities can be used to distinguish structures, tumors, and help them conduct  all sort of complicated analyses to separate or measure anatomical regions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
