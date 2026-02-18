# DICOM MRI error

**Topic ID**: 40350
**Date**: 2024-11-23
**URL**: https://discourse.slicer.org/t/dicom-mri-error/40350

---

## Post #1 by @supalaplic (2024-11-23 16:08 UTC)

<p>I recently had a cerebral MRI scan, and I’m trying to open and process the DICOM files. However, I encountered the following error:</p>
<p>99: PhoenixZIPReport [Scalar Volume]: Reference image in series does not contain geometry information. Please use caution.</p>

---

## Post #2 by @pieper (2024-11-23 16:14 UTC)

<p>That means it’s probably a text report or similar so it can’t be loaded in Slicer as a volume.</p>

---

## Post #3 by @supalaplic (2024-11-25 16:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8196f689c39017085e7182d1e2f762736b94d3b0.png" data-download-href="/uploads/short-url/iup1Th3BmFqlQlRbdyNegBjCTHa.png?dl=1" title="1dicom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8196f689c39017085e7182d1e2f762736b94d3b0_2_690x451.png" alt="1dicom" data-base62-sha1="iup1Th3BmFqlQlRbdyNegBjCTHa" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8196f689c39017085e7182d1e2f762736b94d3b0_2_690x451.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8196f689c39017085e7182d1e2f762736b94d3b0_2_1035x676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/8196f689c39017085e7182d1e2f762736b94d3b0_2_1380x902.png 2x" data-dominant-color="E9EEF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1dicom</span><span class="informations">1391×911 55.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46d2c9971c2b5b12b02a95796988fb4015c94ce8.png" data-download-href="/uploads/short-url/a6x22NtU5v4ou0Alh2XF5BRtR2g.png?dl=1" title="2dicom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46d2c9971c2b5b12b02a95796988fb4015c94ce8_2_690x441.png" alt="2dicom" data-base62-sha1="a6x22NtU5v4ou0Alh2XF5BRtR2g" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46d2c9971c2b5b12b02a95796988fb4015c94ce8_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46d2c9971c2b5b12b02a95796988fb4015c94ce8_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46d2c9971c2b5b12b02a95796988fb4015c94ce8_2_1380x882.png 2x" data-dominant-color="9D9EA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2dicom</span><span class="informations">1502×960 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But i ve imported the whole CD and i got only a slice of the brain that works lol</p>

---

## Post #4 by @pieper (2024-11-25 17:16 UTC)

<p>It’s hard to say, but there have been reports of <a href="https://discourse.slicer.org/t/windows-unable-to-import-dicom-files-that-are-in-a-onedrive-backed-up-folder/36153">strange behavior with OneDrive</a>.  It definitely appears you are missing a lot of data.</p>

---
