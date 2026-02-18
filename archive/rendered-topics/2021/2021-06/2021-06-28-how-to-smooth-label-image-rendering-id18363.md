# How to smooth label image rendering?

**Topic ID**: 18363
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/how-to-smooth-label-image-rendering/18363

---

## Post #1 by @MachadoL (2021-06-28 03:00 UTC)

<p>Hello, Fellows.</p>
<p>I’ve done it previous 3D Slice versions, but now, I seem not to find the options anymore. (Below an example)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27242eba042f390eee83738a89fd966c6d13c632.png" alt="image" data-base62-sha1="5Ag8O2TCCwRRikXTXEf78hHJg9s" width="335" height="196"><br>
Any help, please?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2021-06-28 15:18 UTC)

<p>This is an inherent issue with volume rendering of labelmap volumes. The simplest solution is to render it as segmentation. In latest Slicer Preview Release you can do this in Data module: right-click on the labelmap and choose “Convert labelmap to segmentation node”, then right-click on the segmentation node and choose “Create closed surface representation”.</p>
<p>If you must render this labelmap using volume rendering then you can convert it to scalar volume (in Volumes module) and apply slight Gaussian smoothing (using “Gaussian blur image filter”).</p>

---
