---
topic_id: 4461
title: "Duplicate Data In Mrml Tree"
date: 2018-10-19
url: https://discourse.slicer.org/t/4461
---

# Duplicate data in MRML tree

**Topic ID**: 4461
**Date**: 2018-10-19
**URL**: https://discourse.slicer.org/t/duplicate-data-in-mrml-tree/4461

---

## Post #1 by @torquil (2018-10-19 10:39 UTC)

<p>Hi!</p>
<p>After loading a CT DICOM file, then saving the data, closing the scene, and then opening the data again, I seem to end up with duplicate data in the MRML tree, similar to what is described here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="2311">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drusmanbashir/48/1282_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-save-function-creating-copies-of-dataset-instead-of-overwrite/2311">Slicer save function creating copies of dataset instead of overwrite</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I am not sure if this is how it is supposed to work. But when i load the data folder i saved previously, slicer creates copies of all files and assigns them a suffix like ‘_1’ . If I were to save the data again after updating a few segmentations for example, everything gets saved along with suffixed duplicates, hence doubling storage and creating confusion, unless i manually unselect the suffixed duplicates. 
Screenshot showing contents of folder loaded into slicer, there are no duplicates …
  </blockquote>
</aside>

<p>The response to that question recommended to use “Close scene”, but this is something I always do, so that is not the solution in this case. In addition, I often get several “Default Scene Camera” items in the Data module.</p>
<p>Below is an example where I’m ending up with two copies of a volume initially called L_PreOp. The reason I’m asking about this is that when I worked on registration between two CTs, then saving data and loading data, I end up with duplicate data where half of the items have names with the suffix _1, as described in the link above.</p>
<p>Here are some screenshots of the process, showing the Data module between each step:</p>
<p>After Slicer startup:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fef3561de6cd7f3874095c353e2c3c6bdf2e1859.png" data-download-href="/uploads/short-url/AnoCE10lYT7JXVwn4Oy5HTK3Gat.png?dl=1" title="00_after_startup" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fef3561de6cd7f3874095c353e2c3c6bdf2e1859_2_413x500.png" alt="00_after_startup" data-base62-sha1="AnoCE10lYT7JXVwn4Oy5HTK3Gat" width="413" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fef3561de6cd7f3874095c353e2c3c6bdf2e1859_2_413x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fef3561de6cd7f3874095c353e2c3c6bdf2e1859.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fef3561de6cd7f3874095c353e2c3c6bdf2e1859.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">00_after_startup</span><span class="informations">509×615 9.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After loading the DICOM file:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaf87dd1065bc8cdc6e906da4f1cb15d4284a2fc.png" data-download-href="/uploads/short-url/xwE7lV45VhEMECMtL17zjY2JmWw.png?dl=1" title="01_after_dicom_load" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaf87dd1065bc8cdc6e906da4f1cb15d4284a2fc_2_431x500.png" alt="01_after_dicom_load" data-base62-sha1="xwE7lV45VhEMECMtL17zjY2JmWw" width="431" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaf87dd1065bc8cdc6e906da4f1cb15d4284a2fc_2_431x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaf87dd1065bc8cdc6e906da4f1cb15d4284a2fc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaf87dd1065bc8cdc6e906da4f1cb15d4284a2fc.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01_after_dicom_load</span><span class="informations">515×597 15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After saving the data:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/033b76c995229109543e8374fc49db0e2637a04b.png" data-download-href="/uploads/short-url/sAPFRPJg4vCi9i2TkMFRHq6gC7.png?dl=1" title="02_after_data_save" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/033b76c995229109543e8374fc49db0e2637a04b_2_420x500.png" alt="02_after_data_save" data-base62-sha1="sAPFRPJg4vCi9i2TkMFRHq6gC7" width="420" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/033b76c995229109543e8374fc49db0e2637a04b_2_420x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/033b76c995229109543e8374fc49db0e2637a04b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/033b76c995229109543e8374fc49db0e2637a04b.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02_after_data_save</span><span class="informations">512×609 14.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After File → Close scene:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b2558353b9e7281bb33924219bd3326ac82d06e.png" data-download-href="/uploads/short-url/69GxzQRsaetzUH3Kwq1WJLSNzQi.png?dl=1" title="03_after_close_scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b2558353b9e7281bb33924219bd3326ac82d06e_2_425x500.png" alt="03_after_close_scene" data-base62-sha1="69GxzQRsaetzUH3Kwq1WJLSNzQi" width="425" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/b/2b2558353b9e7281bb33924219bd3326ac82d06e_2_425x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b2558353b9e7281bb33924219bd3326ac82d06e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b2558353b9e7281bb33924219bd3326ac82d06e.png 2x" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">03_after_close_scene</span><span class="informations">515×605 10.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Adding the data that was saved:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a3fb3c542662919991ef4921a4d2f453f4eef7c.png" data-download-href="/uploads/short-url/8jiaPtvvQPjHIjbvTukeMqi1s4Y.png?dl=1" title="04_add_data" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a3fb3c542662919991ef4921a4d2f453f4eef7c_2_690x402.png" alt="04_add_data" data-base62-sha1="8jiaPtvvQPjHIjbvTukeMqi1s4Y" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a3fb3c542662919991ef4921a4d2f453f4eef7c_2_690x402.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a3fb3c542662919991ef4921a4d2f453f4eef7c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a3fb3c542662919991ef4921a4d2f453f4eef7c.png 2x" data-dominant-color="F2F2F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">04_add_data</span><span class="informations">748×436 27.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After adding the data:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1009e990549a0e8cab49fbea4d9d8d71e59743fd.png" data-download-href="/uploads/short-url/2hSSlS13CDCg2GL6ip2JdOvMLdH.png?dl=1" title="05a_after_add_data" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1009e990549a0e8cab49fbea4d9d8d71e59743fd_2_510x500.png" alt="05a_after_add_data" data-base62-sha1="2hSSlS13CDCg2GL6ip2JdOvMLdH" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1009e990549a0e8cab49fbea4d9d8d71e59743fd_2_510x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1009e990549a0e8cab49fbea4d9d8d71e59743fd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1009e990549a0e8cab49fbea4d9d8d71e59743fd.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">05a_after_add_data</span><span class="informations">614×601 19.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The nodes tab:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69f667eb5cb24947ebf816c64aeb6742b4d4b051.png" data-download-href="/uploads/short-url/f7o3vS23zYkw5YX3bOi6dXm9k4h.png?dl=1" title="05b_nodes" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69f667eb5cb24947ebf816c64aeb6742b4d4b051.png" alt="05b_nodes" data-base62-sha1="f7o3vS23zYkw5YX3bOi6dXm9k4h" width="475" height="500" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">05b_nodes</span><span class="informations">612×644 7.38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m using the latest Slicer 3d nightly build on Linux.</p>
<p>Best regards,<br>
Torquil Sørensen</p>

---

## Post #2 by @lassoan (2018-10-19 11:31 UTC)

<p>You add one instance of the volume by loading the scene (mrml file) and you add the second instance by loading the image (nrrd file).</p>
<p>If you want to load a saved scene then double-click the scene file or drag-and-drop the scene file (not the entire folder) to the application window.</p>

---
