# Load DICOM in Slicer UI and in Jupyter Docker container

**Topic ID**: 25372
**Date**: 2022-09-21
**URL**: https://discourse.slicer.org/t/load-dicom-in-slicer-ui-and-in-jupyter-docker-container/25372

---

## Post #1 by @Katya_Stansfield (2022-09-21 09:31 UTC)

<p>Hello – may I please ask for some guidance in using Slicer via Jupyter in a Docker container? I am trying to load some of my DICOM data files, which load with no problem in a local Slicer UI<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c82fb72f0953b5a2526273b51589e868c8894003.jpeg" data-download-href="/uploads/short-url/syVITReet16w5j9R8eVdB4UIVIn.jpeg?dl=1" title="Screenshot 2022-09-21 111950" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c82fb72f0953b5a2526273b51589e868c8894003_2_690x378.jpeg" alt="Screenshot 2022-09-21 111950" data-base62-sha1="syVITReet16w5j9R8eVdB4UIVIn" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c82fb72f0953b5a2526273b51589e868c8894003_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c82fb72f0953b5a2526273b51589e868c8894003_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c82fb72f0953b5a2526273b51589e868c8894003_2_1380x756.jpeg 2x" data-dominant-color="2D3135"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-09-21 111950</span><span class="informations">1784×979 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, when I follow instructions for loading DICOM using python scripts, my Docker Jupyter notebook does not see the individual’s UID and hence loads nothing:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/827425a48864874b50fd432cbcf31272eaf0d12b.jpeg" data-download-href="/uploads/short-url/iC2UJrw5hdHWKklOwMDvmliNAf1.jpeg?dl=1" title="Screenshot 2022-09-21 111837" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/827425a48864874b50fd432cbcf31272eaf0d12b_2_690x228.jpeg" alt="Screenshot 2022-09-21 111837" data-base62-sha1="iC2UJrw5hdHWKklOwMDvmliNAf1" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/827425a48864874b50fd432cbcf31272eaf0d12b_2_690x228.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/827425a48864874b50fd432cbcf31272eaf0d12b_2_1035x342.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/827425a48864874b50fd432cbcf31272eaf0d12b.jpeg 2x" data-dominant-color="F2F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-09-21 111837</span><span class="informations">1234×408 73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f99fb438606a633443d0dfc75c4bf55518c448.jpeg" data-download-href="/uploads/short-url/5HDr9xzTDIv1ZvwYDOTnC5jzDC0.jpeg?dl=1" title="Screenshot 2022-09-21 111916" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f99fb438606a633443d0dfc75c4bf55518c448_2_690x252.jpeg" alt="Screenshot 2022-09-21 111916" data-base62-sha1="5HDr9xzTDIv1ZvwYDOTnC5jzDC0" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f99fb438606a633443d0dfc75c4bf55518c448_2_690x252.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f99fb438606a633443d0dfc75c4bf55518c448_2_1035x378.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f99fb438606a633443d0dfc75c4bf55518c448.jpeg 2x" data-dominant-color="ECEDEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-09-21 111916</span><span class="informations">1264×463 75.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I fix this?</p>
<p>Thank you in advance<br>
KS</p>

---
