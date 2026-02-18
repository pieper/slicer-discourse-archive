# Unable to connect Slicer to ORTHANC

**Topic ID**: 41051
**Date**: 2025-01-13
**URL**: https://discourse.slicer.org/t/unable-to-connect-slicer-to-orthanc/41051

---

## Post #1 by @lennart81 (2025-01-13 08:13 UTC)

<p>Hi Slicer Users,</p>
<p>I’m a frequent user of 3D Slicer and rely on it weekly for evaluating PET/CT and SPECT/CT images. I truly appreciate this fantastic tool!</p>
<p>As the volume of data I’m handling continues to grow, I decided to set up an external server for DICOM storage. I installed the Orthanc DICOM server within our intranet and successfully uploaded image series via the web browser interface.</p>
<p>Now, I’m trying to streamline my workflow by directly accessing the Orthanc server from Slicer’s DICOM browser. While I can establish a connection between Slicer and Orthanc, none of the patient scans I’ve uploaded appear in the DICOM browser in Slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6434bd21ee8f9c46f0ee156093130e37b448001a.png" data-download-href="/uploads/short-url/eisJQfSHIe2NqyHXdc7nnA6rcHU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6434bd21ee8f9c46f0ee156093130e37b448001a_2_690x98.png" alt="image" data-base62-sha1="eisJQfSHIe2NqyHXdc7nnA6rcHU" width="690" height="98" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6434bd21ee8f9c46f0ee156093130e37b448001a_2_690x98.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6434bd21ee8f9c46f0ee156093130e37b448001a_2_1035x147.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6434bd21ee8f9c46f0ee156093130e37b448001a_2_1380x196.png 2x" data-dominant-color="F7F7F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2785×397 11.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89e793306ac5d22517a9748ab343f76e2f579e7a.png" data-download-href="/uploads/short-url/jFXyKBbEXCI75RidzfrAktsZ5xM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89e793306ac5d22517a9748ab343f76e2f579e7a_2_690x50.png" alt="image" data-base62-sha1="jFXyKBbEXCI75RidzfrAktsZ5xM" width="690" height="50" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89e793306ac5d22517a9748ab343f76e2f579e7a_2_690x50.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89e793306ac5d22517a9748ab343f76e2f579e7a_2_1035x75.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89e793306ac5d22517a9748ab343f76e2f579e7a_2_1380x100.png 2x" data-dominant-color="B4D2DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2422×177 7.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Has anyone encountered a similar issue or successfully integrated Orthanc with Slicer? I’d greatly appreciate any guidance on how to resolve this problem.</p>
<p>Thank you so much for your time and help!</p>
<p>Best regards,<br>
Jan</p>

---

## Post #2 by @pieper (2025-01-13 16:00 UTC)

<p>Slicer’s dicom networking is based on DCMTK under the hood, so one thing to try is using the command line tools to figure out all the right options and then copy them to Slicer.  This way you can make sure the AETITLEs and IP info is configured right on both ends.</p>

---
