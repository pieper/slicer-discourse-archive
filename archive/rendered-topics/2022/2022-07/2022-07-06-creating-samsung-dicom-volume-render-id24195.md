---
topic_id: 24195
title: "Creating Samsung Dicom Volume Render"
date: 2022-07-06
url: https://discourse.slicer.org/t/24195
---

# Creating Samsung DICOM Volume Render

**Topic ID**: 24195
**Date**: 2022-07-06
**URL**: https://discourse.slicer.org/t/creating-samsung-dicom-volume-render/24195

---

## Post #1 by @FlowDynamic (2022-07-06 03:54 UTC)

<p>Hi everyone.</p>
<p>I used to use 3D Slicer for Voluson GE Volume files, and now I work with two devices: Samsung HS40 and HS60.</p>
<p>When I drag and drop any file into 3D Slicer, the software joins everything into axial axis; sagittal and coronal axis seems to be the volume crushed into a thin line.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29ca2997bf345c3273de879423c70b7aee30849a.png" data-download-href="/uploads/short-url/5XGHRc0BOMVNrZtATEt85zi9iQ2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29ca2997bf345c3273de879423c70b7aee30849a_2_690x263.png" alt="image" data-base62-sha1="5XGHRc0BOMVNrZtATEt85zi9iQ2" width="690" height="263" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29ca2997bf345c3273de879423c70b7aee30849a_2_690x263.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/29ca2997bf345c3273de879423c70b7aee30849a_2_1035x394.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29ca2997bf345c3273de879423c70b7aee30849a.png 2x" data-dominant-color="3B363A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×522 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t know where to start.</p>
<p>The files are in this folder:<br>
<a href="https://drive.google.com/drive/folders/1v4l6hc1xGpm4wLwME-P6zp4kcaiEHGkY?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1v4l6hc1xGpm4wLwME-P6zp4kcaiEHGkY?usp=sharing</a></p>
<p>Thanks for reading.</p>

---

## Post #2 by @lassoan (2022-07-06 04:05 UTC)

<p>These images are just screenshots, they don’t contain any 3D information.</p>
<p>Samsung does not support exporting 3D ultrasound data in a standard file format and as far as I know nobody has reverse engineered their file format yet. But if you export a 3D data set then you can load it using a manual process as described <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#samsung">here</a>.</p>

---
