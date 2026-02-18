# Burn colorful models into 3d volume and export as DICOM series

**Topic ID**: 42316
**Date**: 2025-03-26
**URL**: https://discourse.slicer.org/t/burn-colorful-models-into-3d-volume-and-export-as-dicom-series/42316

---

## Post #1 by @Bahram_Zargar (2025-03-26 16:43 UTC)

<p>Using 3rd party software, I get some volumes and then import them to Slicer as models indifferent colors. I get them all as following in slicer;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8004814358e8e31e4d8a795a68131f7bd5dd680b.jpeg" data-download-href="/uploads/short-url/iguLCaqK80PIBgwu9BvCZ6G2TBF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8004814358e8e31e4d8a795a68131f7bd5dd680b_2_671x499.jpeg" alt="image" data-base62-sha1="iguLCaqK80PIBgwu9BvCZ6G2TBF" width="671" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8004814358e8e31e4d8a795a68131f7bd5dd680b_2_671x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8004814358e8e31e4d8a795a68131f7bd5dd680b_2_1006x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8004814358e8e31e4d8a795a68131f7bd5dd680b_2_1342x998.jpeg 2x" data-dominant-color="76767E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1632×1216 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How could I can export a colorful dicom series with all of those models burn in to the T1 volume?</p>

---

## Post #2 by @muratmaga (2025-03-26 16:49 UTC)

<ol>
<li>You need to convert the models to segmentation objects.</li>
<li>You need to install the Sandbox extension and obtain “Colorize Volume” module</li>
<li>Create a colorized volume by selecting the segmentation and the T1 volume.</li>
<li>Right click on the “Colored Volume” object in the data module and choose to export DICOM. (I don’t use DICOM that often, so there might be a few additional steps to create the correct metadata structure, but they should be in the user guide).</li>
</ol>

---

## Post #3 by @pieper (2025-03-26 17:12 UTC)

<p>Also note that color dicom files are very rare (outside of secondary capture screengrabs, which typically don’t have geometry support) and I’m not sure that the slicer exporters will create them.  You can try, but you may need to create grayscale exports or else write a short python script to create custom files.  What you may choose to do depends a lot on where you intend to send the files and what system will try to ingest them.</p>

---
