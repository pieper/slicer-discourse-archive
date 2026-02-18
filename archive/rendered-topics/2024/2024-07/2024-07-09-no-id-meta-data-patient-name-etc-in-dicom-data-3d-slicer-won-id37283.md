# No ID meta data (patient name etc) in dicom data - 3d slicer wont load data

**Topic ID**: 37283
**Date**: 2024-07-09
**URL**: https://discourse.slicer.org/t/no-id-meta-data-patient-name-etc-in-dicom-data-3d-slicer-wont-load-data/37283

---

## Post #1 by @Willa_Coultley (2024-07-09 14:03 UTC)

<p>Hi all,</p>
<p>first off: my data is <em>not</em> clinical (i.e., no patient information/sensitive data). I am analyzing a bird skull that is housed in a fair amount of limestone.</p>
<p>second off: i am very, very new to 3d slicer and uct analyses, so I may have some of my terminology wrong.</p>
<p>I can upload my DICOM data to the DICOM database, but not load the data to to view it in the node(?) module.</p>
<p>I am not sure how to proceed - I need to edit in the patient metadata, but from what I have been reading, 3D slicer does not allow this. Is there a work around I can do? From here on out, none of my data will have patient information because I am working on paleontological specimens.</p>
<p>Any help would be appreciated!!<br>
Below is a screenshot of my issue in 3D slicer.</p>
<p>Hardware:<br>
macbook pro m1 2022 w/ parallels to run windows 11<br>
slicer version 5.6.2<br>
dicom scans from a zeiss xray machine</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b372976a57929224aaf647547e771cfa81078f2f.png" data-download-href="/uploads/short-url/pBsYEz3z0YKMDEnECtJ6VxAhHYz.png?dl=1" title="Screenshot 2024-07-08 at 2.38.08 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b372976a57929224aaf647547e771cfa81078f2f_2_690x372.png" alt="Screenshot 2024-07-08 at 2.38.08 PM" data-base62-sha1="pBsYEz3z0YKMDEnECtJ6VxAhHYz" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b372976a57929224aaf647547e771cfa81078f2f_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b372976a57929224aaf647547e771cfa81078f2f_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b372976a57929224aaf647547e771cfa81078f2f_2_1380x744.png 2x" data-dominant-color="ECF0F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-07-08 at 2.38.08 PM</span><span class="informations">1902×1028 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-07-09 15:20 UTC)

<p>MicroCT scanners often produce very non-standard files.  You can try the suggestions here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="inline-onebox">DICOM — 3D Slicer documentation</a></p>
<p>If you are still stuck and don’t mind sharing the data via dropbox, google drive, etc then probably someone can have a look and make suggestions.</p>

---
