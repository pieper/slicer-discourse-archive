# What is the best way to iterate through DICOM image data with RTSTRUCT contours in a loadable module?

**Topic ID**: 8743
**Date**: 2019-10-11
**URL**: https://discourse.slicer.org/t/what-is-the-best-way-to-iterate-through-dicom-image-data-with-rtstruct-contours-in-a-loadable-module/8743

---

## Post #1 by @Mik (2019-10-11 09:55 UTC)

<p>Dear developers,</p>
<p>I have CT DICOM files and RTSTRUCT file which contains contours of the organs.<br>
SlicerRT module loads series and segmentation without errors, and i want to check<br>
what segment each pixel belongs to. This is similar to the information of the<br>
“Data Probe” module, but i wanted to store such information for each pixel as a<br>
std::bitset (each bit represents contour)<br>
and use it further in an external Monte-Carlo package.</p>
<p>For that purpose i create vtkMRMLLabelMapVolumeNode for visible segments<br>
and check if pixel of vtkMRMLScalarVolumeNode belongs to the labelmap<br>
segment or not. Labelmaps for some segments contain “artefacts”,<br>
while displayable nodes look good.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42cff19852108a9f87017ee75c16484596406a50.png" data-download-href="/uploads/short-url/9x31T06rLHNmYS8WHmHNsxtLzW0.png?dl=1" title="Segments" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42cff19852108a9f87017ee75c16484596406a50_2_690x305.png" alt="Segments" data-base62-sha1="9x31T06rLHNmYS8WHmHNsxtLzW0" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42cff19852108a9f87017ee75c16484596406a50_2_690x305.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42cff19852108a9f87017ee75c16484596406a50_2_1035x457.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42cff19852108a9f87017ee75c16484596406a50.png 2x" data-dominant-color="2F281E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segments</span><span class="informations">1035×458 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>May be there is another way to get such information for each pixel?</p>
<p>Best regards,<br>
Mikhail</p>

---

## Post #2 by @lassoan (2019-10-11 11:44 UTC)

<p>There are artifacts in rendering of slice intersections when representation is closed surface due to this bug in VTK.</p>
<p>Usually we show binary labelmap representation in slice views. You can create binary labelmap representation by going to Segmentations module / Representation section and clicking “Create” button next to “Binary labelmap”.</p>
<p>You can export segments to a labelmap node in Segmentations module’s Export/import section (or by right-clicking on the segmentation node in Data module).</p>

---
