---
topic_id: 44916
title: "Us Segmentation Imaging Browsing"
date: 2025-10-30
url: https://discourse.slicer.org/t/44916
---

# US segmentation, imaging browsing

**Topic ID**: 44916
**Date**: 2025-10-30
**URL**: https://discourse.slicer.org/t/us-segmentation-imaging-browsing/44916

---

## Post #1 by @sunmichaelj (2025-10-30 03:03 UTC)

<p>Hello,</p>
<p>I am trying to segment some ultrasound images. I imported the whole DICOM into Slicer but the images are out of order.</p>
<p>Is there a way to sort the images so they are in order and if so, is there a way to scroll through and look at all of them to select the best image (most applicable image) to segment for the project?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abaefdceb2c0172058938fddfaa6a2f7bc130ffe.jpeg" data-download-href="/uploads/short-url/ouMz1lLYuMiG1ypMJdi2gSZgSDA.jpeg?dl=1" title="Screenshot 2025-10-29 at 3.46.06 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abaefdceb2c0172058938fddfaa6a2f7bc130ffe_2_690x388.jpeg" alt="Screenshot 2025-10-29 at 3.46.06 PM" data-base62-sha1="ouMz1lLYuMiG1ypMJdi2gSZgSDA" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abaefdceb2c0172058938fddfaa6a2f7bc130ffe_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abaefdceb2c0172058938fddfaa6a2f7bc130ffe_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abaefdceb2c0172058938fddfaa6a2f7bc130ffe_2_1380x776.jpeg 2x" data-dominant-color="555353"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-10-29 at 3.46.06 PM</span><span class="informations">1920×1080 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-10-30 03:14 UTC)

<p>It could make sense to sort ultrasound images based on instance number in <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMImageSequencePlugin.py">DICOMImageSequencePlugin.py</a>. You can find this file on your computer in the Slicer installation folder. You can modify it in any editor and your changes take effect when you restart Slicer. Only a few localized changes are needed in the file, so most AI chatbots should be able to do it. Once the plugin works well, you can contribute your changes to Slicer core by creating a pull request on github.</p>

---
