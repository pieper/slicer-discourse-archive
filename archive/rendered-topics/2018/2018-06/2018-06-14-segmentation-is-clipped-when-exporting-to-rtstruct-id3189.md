# Segmentation is clipped when exporting to RTstruct

**Topic ID**: 3189
**Date**: 2018-06-14
**URL**: https://discourse.slicer.org/t/segmentation-is-clipped-when-exporting-to-rtstruct/3189

---

## Post #1 by @ferhue (2018-06-14 22:39 UTC)

<p>Hi,<br>
I am importing an STL file (couch, in green) as segmentation on top of a DICOM CT (which has its own contour, in gray). In the attached picture you see the three central CT slices, the CT contour (gray) and the STL file (green).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72134d633470cbf6f4a0075d673edb66f2e54c5e.png" data-download-href="/uploads/short-url/gh9MLIACFbRTZQ4NuH7BYEOCtPw.PNG?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72134d633470cbf6f4a0075d673edb66f2e54c5e_2_690x416.PNG" alt="Capture" data-base62-sha1="gh9MLIACFbRTZQ4NuH7BYEOCtPw" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72134d633470cbf6f4a0075d673edb66f2e54c5e_2_690x416.PNG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72134d633470cbf6f4a0075d673edb66f2e54c5e_2_1035x624.PNG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72134d633470cbf6f4a0075d673edb66f2e54c5e_2_1380x832.PNG 2x" data-dominant-color="7B7B80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1920×1160 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would like to export the segmentation as a RTSTRUCT contour on top of this CT, even if it is outside the field of view of the CT. Thus, in the data hierarchy, I move the segmentation into the DICOM Study and then export.</p>
<p>That works well so far, with the exception that the green STL contour is clipped along the slice axis (not on the other axes). See on the second image, obtained when I reimport in Slicer the exported dicom.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c61053110e6377740e05b2a6c54dc9ab39478830.png" data-download-href="/uploads/short-url/sg9vSwpNUgkic0h0Kv1ACTLBulW.PNG?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c61053110e6377740e05b2a6c54dc9ab39478830.png" alt="2" data-base62-sha1="sg9vSwpNUgkic0h0Kv1ACTLBulW" width="673" height="500" data-dominant-color="8D90BA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">721×535 12.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would like to ask for a feature (check-box advanced option) where one could enable saving contours outside of the first/last slice. I guess this should be possible as the RTSTRUCT contours are specified as 3D coordinates. Thus, one could add the out of range contours by adding them recursively to the last CT slice but using a different z coordinate.</p>
<p>Do you think this is doable? Thanks in advance.<br>
Thanks.</p>

---

## Post #2 by @lassoan (2018-06-14 23:56 UTC)

<p>You can expand the CT volume using Crop volume module to include the complete segmentation (you may need to enable interpolation). Then use this expanded CT volume for DICOM export.</p>

---

## Post #3 by @ferhue (2018-06-15 15:20 UTC)

<p>It works! Thanks for the fast reply.</p>
<p>It adds however some storage overhead of the new CT slices (514kB per slice). As these are all with a fixed HU zero-value, do you know if there is an option in Slicer to compress these .dcm files when exporting?</p>

---

## Post #4 by @lassoan (2018-06-15 16:48 UTC)

<p>Slicer does not support compressed DICOM export. It is not a common need, as usually compatibility is more important than some saved disk space or network bandwidth. You can of course zip the files and save on storage. You may be able to apply compression on the image data inside the DICOM file by using <a href="https://dcmtk.org/">DCMTK toolkit</a>.</p>

---
