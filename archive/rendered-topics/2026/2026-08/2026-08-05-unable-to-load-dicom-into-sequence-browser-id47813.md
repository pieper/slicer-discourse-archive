---
topic_id: 47813
title: "Unable to load DICOM into sequence browser"
date: 2026-08-05
url: https://discourse.slicer.org/t/47813
last_bumped: 2026-08-05T21:05:07.354Z
---

# Unable to load DICOM into sequence browser

**Topic ID**: 47813
**Date**: 2026-08-05
**URL**: https://discourse.slicer.org/t/unable-to-load-dicom-into-sequence-browser/47813

---

## Post #1 by @Rene_Mazuela (2026-08-05 20:15 UTC)

<p>We’re having an inconsistent issue in 3D Slicer with loading DICOM data as a sequence. Some team members can load a DICOM series into the Sequence Browser and select the proper frame, but others do not see the option to load it into the Sequence Browser at all.</p>
<p>When we try the MultiVolumeExplorer module instead, we can view the frames, but during annotation we cannot annotate the selected frame.</p>
<p>What are the common causes of this behavior in Slicer, and what is the recommended workflow for loading multi-frame DICOM so that a specific frame can be selected and annotated? We’d also appreciate any settings, module versions, or import options we should check.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52dd529b755069786b9942575f9498c6d768c7cf.jpeg" data-download-href="/uploads/short-url/bP3kIP9s4Yx1oaUzst9p7dZmofd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52dd529b755069786b9942575f9498c6d768c7cf_2_690x236.jpeg" alt="image" data-base62-sha1="bP3kIP9s4Yx1oaUzst9p7dZmofd" width="690" height="236" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52dd529b755069786b9942575f9498c6d768c7cf_2_690x236.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52dd529b755069786b9942575f9498c6d768c7cf_2_1035x354.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52dd529b755069786b9942575f9498c6d768c7cf_2_1380x472.jpeg 2x" data-dominant-color="72728E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×656 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-08-05 21:04 UTC)

<p>Slicer should run the same on all machines on the same data so maybe it’s configured differently for different users.  If you toggle Advanced mode in the dicom browser you can see if the Sequence plugin is enabled and see which plugin is used to load.  Maybe somebody turned of the sequence plugin.</p>
<p>Also check that everyone is using the same version (we only really provide support for the latest release).</p>

---

## Post #3 by @mikebind (2026-08-05 21:05 UTC)

<p>Probably most important is to have MultiVolumeImporterPlugin checked in the DICOM plugins section of the Add DICOM Data module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05eb4f096a61093ed57b991ad19fb7c364a0c834.png" data-download-href="/uploads/short-url/Qmx6Gs5ZjckPzcuYUnoBgxM31q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05eb4f096a61093ed57b991ad19fb7c364a0c834.png" alt="image" data-base62-sha1="Qmx6Gs5ZjckPzcuYUnoBgxM31q" width="578" height="311"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">578×311 4.61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then, after clicking “Examine”, make sure you choose to load the data as a “Volume Sequence” rather than a “MultiVolume” (both options will show the “MultiVolume” in the “Reader” column, you need to look in the “DICOM Data” column, and there you often need to expand that column or to be able to read it, it is too narrow by default; hovering the mouse over it also shows the full string in the hovertext).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0282cad2a5fc489e5f4a4919ef8f4876eb51abe1.png" data-download-href="/uploads/short-url/mdaUVU8cAaZwXwVVfLk24AT1hT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0282cad2a5fc489e5f4a4919ef8f4876eb51abe1.png" alt="image" data-base62-sha1="mdaUVU8cAaZwXwVVfLk24AT1hT" width="690" height="483" data-dominant-color="ECF1F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×576 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think the most likely source of inconsistency between colleagues is choosing different loading methods here.  If the data is not loaded as a Volume Sequence, the sequence browser will not work with it. If there is no option to load as a Volume Sequence, then the importer plugin is not recognizing that data as able to be loaded as a sequence.  In that case you may need to either update the plugin or modify the data so that it is recognizable by the plugin.</p>

---
