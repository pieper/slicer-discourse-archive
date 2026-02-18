# Dicom PACS retrieve fail

**Topic ID**: 28270
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/dicom-pacs-retrieve-fail/28270

---

## Post #1 by @skyhsu (2023-03-10 03:21 UTC)

<p>Hi, We are using 3D Slicer to obtain dicom dataset via PACS system in Our Hospital,<br>
We are using version:5.2.1<br>
Windows 10 pro<br>
and we get some error message as below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc8eeef5a95bf0a867f1c0450a6ad13ceeed348c.jpeg" data-download-href="/uploads/short-url/tbBDwlcMpeFfe3aUMgq6CmU0Xmc.jpeg?dl=1" title="dicom1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8eeef5a95bf0a867f1c0450a6ad13ceeed348c_2_690x408.jpeg" alt="dicom1" data-base62-sha1="tbBDwlcMpeFfe3aUMgq6CmU0Xmc" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8eeef5a95bf0a867f1c0450a6ad13ceeed348c_2_690x408.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8eeef5a95bf0a867f1c0450a6ad13ceeed348c_2_1035x612.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8eeef5a95bf0a867f1c0450a6ad13ceeed348c_2_1380x816.jpeg 2x" data-dominant-color="68625D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dicom1</span><span class="informations">1920×1137 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ada970e8373b196f2157732e2266a1bacac58552.jpeg" data-download-href="/uploads/short-url/oMhCWBre2oyyoBdAiWB3nnNhVDk.jpeg?dl=1" title="dicom2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ada970e8373b196f2157732e2266a1bacac58552_2_690x336.jpeg" alt="dicom2" data-base62-sha1="oMhCWBre2oyyoBdAiWB3nnNhVDk" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ada970e8373b196f2157732e2266a1bacac58552_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ada970e8373b196f2157732e2266a1bacac58552_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ada970e8373b196f2157732e2266a1bacac58552_2_1380x672.jpeg 2x" data-dominant-color="696774"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dicom2</span><span class="informations">1920×935 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>it will cause some dicom file loss, maybe the slices has 313, but only retrieve 296,<br>
and delete the patient, then retrieve again, it’s will be OK.<br>
Is there any problem with our operation?</p>
<p>we use cget to do these function.</p>
<p>Thanks<br>
Sky</p>

---

## Post #2 by @pieper (2023-03-10 15:28 UTC)

<p>Thanks for reporting.  It’s hard to know for sure, but the <code>PermissionError</code> indicates it may be a something like an antivirus scanner or similar external issue causing occasional failures to read the files.</p>

---

## Post #3 by @skyhsu (2023-03-14 03:04 UTC)

<p>Hi pieper,<br>
Thank’s for reply,<br>
We will check the error status about reading file.</p>
<p>Many Thanks</p>

---
