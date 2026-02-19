---
topic_id: 36139
title: "Coronary Artery Centerline Extraction Using Vmtk Slicer Exte"
date: 2024-05-14
url: https://discourse.slicer.org/t/36139
---

# Coronary artery centerline extraction using VMTK slicer extension

**Topic ID**: 36139
**Date**: 2024-05-14
**URL**: https://discourse.slicer.org/t/coronary-artery-centerline-extraction-using-vmtk-slicer-extension/36139

---

## Post #1 by @Kavita_C (2024-05-14 11:12 UTC)

<p>I am trying to extract centerline using extract centerline from VMTK module. But I’m able to extract only one part of branch ,not other part of branch of coronary vessels. How do I extract both branches centerlines. Can you suggest.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b82d6ae9bfd5141d58e8f771834899e9aca565dd.png" data-download-href="/uploads/short-url/qhja0mrjyA1MhcsCLzofrcB1Vkp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b82d6ae9bfd5141d58e8f771834899e9aca565dd_2_690x345.png" alt="image" data-base62-sha1="qhja0mrjyA1MhcsCLzofrcB1Vkp" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b82d6ae9bfd5141d58e8f771834899e9aca565dd_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b82d6ae9bfd5141d58e8f771834899e9aca565dd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b82d6ae9bfd5141d58e8f771834899e9aca565dd.png 2x" data-dominant-color="8F91C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×484 85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2024-05-14 11:19 UTC)

<p>You must use a distinct endpoint list for the left coronaries. It’s even better to create 2 distinct surfaces, you can do that using the ‘Islands’ effect.</p>

---
