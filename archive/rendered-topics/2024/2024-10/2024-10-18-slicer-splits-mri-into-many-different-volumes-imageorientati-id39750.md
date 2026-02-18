# Slicer splits MRI into many different volumes: imageOrientationPatient #1-6

**Topic ID**: 39750
**Date**: 2024-10-18
**URL**: https://discourse.slicer.org/t/slicer-splits-mri-into-many-different-volumes-imageorientationpatient-1-6/39750

---

## Post #1 by @waterbottle (2024-10-18 00:59 UTC)

<p>Hi all,</p>
<p>a lot of the MRIs I’m working on when loaded into 3d slicer split into multiple patient orientations. How can I modify settings to actually important as one big volume? I have searched this forum but haven’t encountered a solution. I tried DICOM patcher, and adjusting the settings in preferences (settings in Windows) for DICOM import, but nothing works.</p>
<p>I posted before about this topic before and ended up using Stitch Volumes but what I am finding is that stitching volumes does not always produce a great reconstruction when the MRI is split into 5+ volumes and I would prefer to address the problem when importing…</p>
<p>Thank you in advance</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31a028c57f5e7b83a559bc339e62f6167384748f.png" data-download-href="/uploads/short-url/750xdck3f1SqsqzmGlBSu4M40rB.png?dl=1" title="Screenshot 2024-10-17 at 8.57.21 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31a028c57f5e7b83a559bc339e62f6167384748f_2_690x185.png" alt="Screenshot 2024-10-17 at 8.57.21 PM" data-base62-sha1="750xdck3f1SqsqzmGlBSu4M40rB" width="690" height="185" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31a028c57f5e7b83a559bc339e62f6167384748f_2_690x185.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31a028c57f5e7b83a559bc339e62f6167384748f_2_1035x277.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31a028c57f5e7b83a559bc339e62f6167384748f_2_1380x370.png 2x" data-dominant-color="EFF0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-17 at 8.57.21 PM</span><span class="informations">1642×442 62.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-10-18 13:13 UTC)

<p>That’s really more of a property of how your images were acquired.  If you load them you can look at their orientations - probably they don’t form a coherent volume.</p>

---

## Post #3 by @waterbottle (2024-10-21 12:12 UTC)

<p>Thank you for your comment, this actually solved my problem. I realized I needed to find a way to align/orient them coherently before attempting to do a stitch. It’s improved the yielded volume massively.</p>

---
