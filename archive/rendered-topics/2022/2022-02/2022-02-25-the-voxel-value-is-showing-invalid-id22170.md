---
topic_id: 22170
title: "The Voxel Value Is Showing Invalid"
date: 2022-02-25
url: https://discourse.slicer.org/t/22170
---

# The voxel value is showing 'invalid'

**Topic ID**: 22170
**Date**: 2022-02-25
**URL**: https://discourse.slicer.org/t/the-voxel-value-is-showing-invalid/22170

---

## Post #1 by @parvaneh.a (2022-02-25 06:12 UTC)

<p>I have one image and one segmentation. When I load the image as volume and the segmentation as segmentation everything seems fine with both. There is no NAN voxel value in any of image or segmentation. I use the code below to mask the image with the segment. However, after that when i load the masked image I saw it as  below in slicer in which the voxel value shows ‘invalid’ in the left down. why this happening and what does it mean?</p>
<pre><code>inputpath='/home/ImgAve_RIPV_Aff.nii.gz'
newimg_path='/home/SegAve_RIPV_Aff_label_0.2.nii.gz'

img = sitk.ReadImage(inputpath)
img_arr=sitk.GetArrayFromImage(img)

seg = sitk.ReadImage(newimg_path)
seg_arr=sitk.GetArrayFromImage(seg)


img_arr[seg_arr==0]=0

newimg11 = sitk.GetImageFromArray(img_arr)

img_ave1 = copyImageParameters(newimg11,img, inputpath)
sitk.WriteImage(img_ave1,'/home/mmm.nii.gz')
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4e3587ade2b61843bc3b433217aefe247a114d7.jpeg" data-download-href="/uploads/short-url/wEPWQ1m2wGqkNPHPh310pbhW0vR.jpeg?dl=1" title="unnamed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4e3587ade2b61843bc3b433217aefe247a114d7_2_667x500.jpeg" alt="unnamed" data-base62-sha1="wEPWQ1m2wGqkNPHPh310pbhW0vR" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4e3587ade2b61843bc3b433217aefe247a114d7_2_667x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4e3587ade2b61843bc3b433217aefe247a114d7_2_1000x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4e3587ade2b61843bc3b433217aefe247a114d7_2_1334x1000.jpeg 2x" data-dominant-color="8E8778"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">unnamed</span><span class="informations">2100×1574 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @parvaneh.a (2022-02-25 06:36 UTC)

<p>I also checked that there is no NAN in none of the segment and image. The image is an average image of 50 cases.</p>

---

## Post #3 by @lassoan (2022-02-25 07:03 UTC)

<p>There is nothing wrong. <code>invalid</code> color name just means that the label value <code>1332</code> has no color name specified in the chosen color table.</p>

---

## Post #4 by @parvaneh.a (2022-02-25 12:24 UTC)

<p>Thank you for your answer but the image which is called “ImgAve_RIPV_Aff_label_0.2” is not a label map to have a color map. It is average of 50 CT images with voxel values 0 to more than 1332. so, it is not like a label map with only one voxel value of 1332. It was a CT image which was masked by a segment with the python code and after being masked, ‘invalid’ appeared in the resultant ct masked image.  I would be very grateful if you could help in clarifying.</p>

---

## Post #5 by @lassoan (2022-02-25 14:24 UTC)

<p>The image appears in the label layer (indicated by the <code>L</code> in the Data Probe), therefore it is a labelmap volume.</p>
<p>I think there is a heuristics that by default an image that has <code>label</code> in the filename is loaded as a labelmap, so if you want to load this image as a scalar volume instead then you need to change the default in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#non-dicom-data">“Add data” window</a> (or if you load it using Python then specify the <code>{"labelmap": 0}</code> property input of <code>slicer.util.loadVolume</code>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0861e0a42af95099f4795e51c401a4620a8834dd.png" data-download-href="/uploads/short-url/1c9wk4wtQvzpl81jZEOqkvSYIPP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0861e0a42af95099f4795e51c401a4620a8834dd_2_690x311.png" alt="image" data-base62-sha1="1c9wk4wtQvzpl81jZEOqkvSYIPP" width="690" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0861e0a42af95099f4795e51c401a4620a8834dd_2_690x311.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0861e0a42af95099f4795e51c401a4620a8834dd_2_1035x466.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0861e0a42af95099f4795e51c401a4620a8834dd_2_1380x622.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2044×923 26.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
