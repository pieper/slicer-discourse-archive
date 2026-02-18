# Fail to upload DICOM data

**Topic ID**: 24292
**Date**: 2022-07-13
**URL**: https://discourse.slicer.org/t/fail-to-upload-dicom-data/24292

---

## Post #1 by @zmm-slicer (2022-07-13 09:35 UTC)

<p>When I upload a file, it cannot be uploaded successfully, and the display is:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87f544c3cf70f7159c85f23f13e16d3c50dced8e.png" data-download-href="/uploads/short-url/joJWx56qSNXATQlxA42dMgsPmiO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87f544c3cf70f7159c85f23f13e16d3c50dced8e_2_690x227.png" alt="image" data-base62-sha1="joJWx56qSNXATQlxA42dMgsPmiO" width="690" height="227" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87f544c3cf70f7159c85f23f13e16d3c50dced8e_2_690x227.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87f544c3cf70f7159c85f23f13e16d3c50dced8e_2_1035x340.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87f544c3cf70f7159c85f23f13e16d3c50dced8e_2_1380x454.png 2x" data-dominant-color="F7F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1645×543 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The format of the data is as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef41957e407823e787c75acb6a026456ee2e3837.png" data-download-href="/uploads/short-url/y8yCXDLe4jbAnY22LLmXZVqLvsH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef41957e407823e787c75acb6a026456ee2e3837_2_465x500.png" alt="image" data-base62-sha1="y8yCXDLe4jbAnY22LLmXZVqLvsH" width="465" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef41957e407823e787c75acb6a026456ee2e3837_2_465x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef41957e407823e787c75acb6a026456ee2e3837_2_697x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef41957e407823e787c75acb6a026456ee2e3837_2_930x1000.png 2x" data-dominant-color="F6F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1100×1181 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
What can I do for sovling this problem？ Thank you very much</p>

---

## Post #2 by @lassoan (2022-07-13 12:33 UTC)

<p>Do yoy use the latest version of Windows10 or use Windows11? If not then both Slicer and the folder you are importing DICOM from must be stored in a path that only contains ASCII characters (no special characters).</p>
<p>If this does not help then check out all the other possible root causes listed <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#i-try-to-import-a-directory-of-dicom-files-but-nothing-shows-up-in-the-browser">here</a>.</p>

---

## Post #3 by @pieper (2022-07-13 20:38 UTC)

<p>Also, as the dialog indicates, you may need the Quantitative Reporting extension to read DICOM Structured Reports (SR).  Be aware though that SR is a broad category and only certain formats are readable in Slicer (e.g. ones that contain certain line Markups for example).</p>

---
