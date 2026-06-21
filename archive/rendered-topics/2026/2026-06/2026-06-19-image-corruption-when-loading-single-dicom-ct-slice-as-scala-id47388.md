---
topic_id: 47388
title: "Image corruption when loading single DICOM CT slice as Scalar Volume"
date: 2026-06-19
url: https://discourse.slicer.org/t/47388
last_bumped: 2026-06-20T20:01:17.188Z
---

# Image corruption when loading single DICOM CT slice as Scalar Volume

**Topic ID**: 47388
**Date**: 2026-06-19
**URL**: https://discourse.slicer.org/t/image-corruption-when-loading-single-dicom-ct-slice-as-scalar-volume/47388

---

## Post #1 by @Martina_Caro95 (2026-06-19 12:32 UTC)

<p>Hi everyone,</p>
<p>I am currently working on building a retrospective clinical database, extracting body composition and radiomic data from thoracic CT scans specifically at the T4 level. Our historical workflow involved exporting these single, targeted CT slices directly from our hospital PACS and importing them into 3D Slicer. In the past, this worked seamlessly. However, with the latest batch of extracted single slices, the images appear completely corrupted upon loading.</p>
<p>What happens is that I import the single DICOM file via the DICOM Browser. Slicer correctly indexes the patient but highlights that there is only “1 image” in the series.</p>
<ol>
<li>Because standard loading fails or triggers missing-image warnings, I force the load via the <code>Advanced</code> tab → <code>Examine</code> → selecting <code>Scalar Volume</code> and clicking Load.</li>
<li>The volume loads without explicit error pop-ups, but the visualization shows a severe shearing/scrambling artifact. The pixel matrix appears completely misaligned and oblique.</li>
<li>I have already ruled out basic display issues (I applied the “Fit to window” centering and standard CT Window/Level presets, but the structural distortion remains).</li>
</ol>
<p>Has anyone encountered this specific artifact when working with isolated single slices? Are there any recommended workarounds (e.g., switching from GDCM to DCMTK reader), or can the <code>DICOM Patcher</code> module be configured to rebuild the matrix for these orphaned slices?</p>
<p>Thank you in advance for your time and expertise.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cb5c3d506253d5878c5f48024bff832f031dfe9.png" data-download-href="/uploads/short-url/45YNwFV4e6H3Kw6EZiWhZZ5q9pn.png?dl=1" title="Screenshot of the slice viewer in the main interface. It displays the final loaded volume, showing the severe shearing/scrambling artifact where the pixel matrix appears completely oblique and unreadable." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cb5c3d506253d5878c5f48024bff832f031dfe9_2_690x288.png" alt="Screenshot of the slice viewer in the main interface. It displays the final loaded volume, showing the severe shearing/scrambling artifact where the pixel matrix appears completely oblique and unreadable." data-base62-sha1="45YNwFV4e6H3Kw6EZiWhZZ5q9pn" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cb5c3d506253d5878c5f48024bff832f031dfe9_2_690x288.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cb5c3d506253d5878c5f48024bff832f031dfe9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cb5c3d506253d5878c5f48024bff832f031dfe9.png 2x" data-dominant-color="4E4C50"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot of the slice viewer in the main interface. It displays the final loaded volume, showing the severe shearing/scrambling artifact where the pixel matrix appears completely oblique and unreadable.</span><span class="informations">848×355 41.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c62a2a7932372ec4d2d560e840b45bab32b20e7.png" data-download-href="/uploads/short-url/6kEkHUzezS2MkVZ5X0pRN8WILK7.png?dl=1" title="Screenshot of the Advanced &quot;Examine&quot; dialog box. It shows the forced loading attempt by selecting the &quot;Scalar Volume&quot; plugin to bypass the missing images warning." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c62a2a7932372ec4d2d560e840b45bab32b20e7.png" alt="Screenshot of the Advanced &quot;Examine&quot; dialog box. It shows the forced loading attempt by selecting the &quot;Scalar Volume&quot; plugin to bypass the missing images warning." data-base62-sha1="6kEkHUzezS2MkVZ5X0pRN8WILK7" width="690" height="321" data-dominant-color="E5EBF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot of the Advanced "Examine" dialog box. It shows the forced loading attempt by selecting the "Scalar Volume" plugin to bypass the missing images warning.</span><span class="informations">821×383 11.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-06-20 20:01 UTC)

<p>Looks like compressed data not being uncompressed.  Did you check the logs (see Help-&gt;Report a bug menu).</p>
<p>Also you might try the latest Preview version of slicer, since it has some newer dicom codec support.</p>

---
