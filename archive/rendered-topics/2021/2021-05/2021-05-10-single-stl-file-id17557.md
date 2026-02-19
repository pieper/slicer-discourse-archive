---
topic_id: 17557
title: "Single Stl File"
date: 2021-05-10
url: https://discourse.slicer.org/t/17557
---

# Single STL file

**Topic ID**: 17557
**Date**: 2021-05-10
**URL**: https://discourse.slicer.org/t/single-stl-file/17557

---

## Post #1 by @Valentina_Mejia_Gall (2021-05-10 23:38 UTC)

<p>Hello, i have tree bones in stl format, i want to save this as one to later opened in solidworks or a CAD program (saved it as one file allows me to preserve the coordinate system and relative positions between the bones) I would like to know if there is a way to save this as an assembly or anything that allows me to open this in a CAD software but being everithing separated parts in one single file.</p>
<p>This STL are not from a segmentation but i imported to 3DSlicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe00614d455c17087ff5ea2e7d077c2b54a7884c.png" data-download-href="/uploads/short-url/Af05GY0IxSUyO3zfcatRRDx3E7y.png?dl=1" title="Anotación 2021-05-10 183239" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe00614d455c17087ff5ea2e7d077c2b54a7884c_2_690x414.png" alt="Anotación 2021-05-10 183239" data-base62-sha1="Af05GY0IxSUyO3zfcatRRDx3E7y" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe00614d455c17087ff5ea2e7d077c2b54a7884c_2_690x414.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe00614d455c17087ff5ea2e7d077c2b54a7884c_2_1035x621.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe00614d455c17087ff5ea2e7d077c2b54a7884c_2_1380x828.png 2x" data-dominant-color="9B9B9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Anotación 2021-05-10 183239</span><span class="informations">1678×1009 97.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-05-11 02:53 UTC)

<p>You can merge models using Dynamic modeler module’s Append tool (it can merge any number of models, dynamically); or Merge models module (simpler to run from the command-line).</p>
<p>Software that is designed to work with dense meshes coming from medical images should be able to import meshes respecting their position. Applications that are not designed to work with such meshes will probably struggle with doing anything with them, so positioning correctly will not be your biggest challenge. What is your overall goal? What CAD software do you use?</p>

---
