# Export images from DICOM images

**Topic ID**: 6324
**Date**: 2019-03-28
**URL**: https://discourse.slicer.org/t/export-images-from-dicom-images/6324

---

## Post #1 by @ZiyunLiang (2019-03-28 08:31 UTC)

<p>Hi, I’m having some problems reading a dicom file. I wish to find a certain image from the dicom file. The image came from the sagittal(yellow) slice, and the coordinate has the smallest absolute value. (What I mean by ‘the coordinate’ is shown in this picture:)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e362f4f5e4e5351d71edbcbea5728c03642b2838.png" data-download-href="/uploads/short-url/wryoNiTHCNolPAEJahoVPJ2Nhbi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e362f4f5e4e5351d71edbcbea5728c03642b2838_2_690x138.png" alt="image" data-base62-sha1="wryoNiTHCNolPAEJahoVPJ2Nhbi" width="690" height="138" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e362f4f5e4e5351d71edbcbea5728c03642b2838_2_690x138.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e362f4f5e4e5351d71edbcbea5728c03642b2838.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e362f4f5e4e5351d71edbcbea5728c03642b2838.png 2x" data-dominant-color="706D57"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">889×179 36.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I want to display it in 2D slice, get it’s array and save it as a jpg file. (later I’m going to use that image to help with diagnose)<br>
I looked this up but couldn’t find the way of doing this. Can anyone help with this problem!</p>
<p>Thanks for your time!</p>

---

## Post #2 by @pieper (2019-03-28 13:48 UTC)

<p>Hi -</p>
<p>The slice views are in patient space (<a href="https://www.slicer.org/wiki/Coordinate_systems" rel="nofollow noopener">https://www.slicer.org/wiki/Coordinate_systems</a>) but you can look at the DataProbe to see the voxel indices (ijk space).  If you imported the data through the DICOM module then the InstanceUIDs for the slices will be stored as attributes of the volume node (available via python but also you can see them in the Data module).</p>

---
