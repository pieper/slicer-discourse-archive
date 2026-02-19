---
topic_id: 13644
title: "Import Dicom Data Through Series"
date: 2020-09-23
url: https://discourse.slicer.org/t/13644
---

# Import DICOM Data through series

**Topic ID**: 13644
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/import-dicom-data-through-series/13644

---

## Post #1 by @Chintha_Siva_Prasad (2020-09-23 05:26 UTC)

<p>I am trying to load volumes using the series names of the patient. This is my current code to load the volume of a patient.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69ea7d27a69810e0ba5c682ad44f744e5bc67f5c.png" data-download-href="/uploads/short-url/f6YwwfyQLt0jRHW3ce7gVjodaWM.png?dl=1" title="Screenshot from 2020-09-23 10-42-32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69ea7d27a69810e0ba5c682ad44f744e5bc67f5c_2_690x123.png" alt="Screenshot from 2020-09-23 10-42-32" data-base62-sha1="f6YwwfyQLt0jRHW3ce7gVjodaWM" width="690" height="123" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69ea7d27a69810e0ba5c682ad44f744e5bc67f5c_2_690x123.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69ea7d27a69810e0ba5c682ad44f744e5bc67f5c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69ea7d27a69810e0ba5c682ad44f744e5bc67f5c.png 2x" data-dominant-color="EBEBEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-09-23 10-42-32</span><span class="informations">780×140 22.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
How can I load the volume using the series description as slicer do?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6519c72d99595e59c480d1137788913342d56843.png" data-download-href="/uploads/short-url/eqns83SvL9MvL0jLAzSjViMDLSH.png?dl=1" title="Screenshot from 2020-09-23 10-45-49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6519c72d99595e59c480d1137788913342d56843_2_690x320.png" alt="Screenshot from 2020-09-23 10-45-49" data-base62-sha1="eqns83SvL9MvL0jLAzSjViMDLSH" width="690" height="320" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6519c72d99595e59c480d1137788913342d56843_2_690x320.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6519c72d99595e59c480d1137788913342d56843.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6519c72d99595e59c480d1137788913342d56843.png 2x" data-dominant-color="DCE4F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-09-23 10-45-49</span><span class="informations">819×381 52.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
How can I load the volume that corresponds the series in python program?<br>
Or can I import this whole UI into my program?</p>

---

## Post #2 by @lassoan (2020-09-23 14:56 UTC)

<p>You can read series description from the database, see this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_top_level_tags_of_DICOM_images_imported_into_Slicer.3F_For_example.2C_to_print_the_first_patient.27s_first_study.27s_first_series.27_.220020.2C0032.22_field%3A">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_top_level_tags_of_DICOM_images_imported_into_Slicer.3F_For_example.2C_to_print_the_first_patient.27s_first_study.27s_first_series.27_.220020.2C0032.22_field%3A</a></p>
<p>You can of course display the DICOM browser in your module, either as it is done in the DICOM module (in the view layout) or as a popup window (by instantiating a new <code>ctk.ctkDICOMBrowser()</code> widget).</p>

---
