---
topic_id: 26996
title: "Loss Of Model Resolution Upon Applying Threshold To Segmenta"
date: 2023-01-01
url: https://discourse.slicer.org/t/26996
---

# Loss of model resolution upon applying threshold to segmentation in 5.0.3 version

**Topic ID**: 26996
**Date**: 2023-01-01
**URL**: https://discourse.slicer.org/t/loss-of-model-resolution-upon-applying-threshold-to-segmentation-in-5-0-3-version/26996

---

## Post #1 by @mdileo (2023-01-01 00:12 UTC)

<p>For years, I have been using an older Slicer version (4.11 and earlier) to make models for surgical applications using CT scan DICOM data which I subsequently import into Meshmixer for further refinement. I recently updated to the Slicer 5.0.3. In the 5.0.3 version the steps/modules to make the models have changed. It appears that I am losing significant resolution in the model when I perform/apply the threshold affect to isolate the bone. After repeatedly attempting to change some of the settings in the modules to correct this issue, I am unable to determine what is the difference in the 4.11 versus 5.0.3 versions that is causing the loss in model resolution. Any thoughts?</p>
<p>Exact steps are: import/load DICOM, Volume Rendering Module, CT Bone preset, Crop enabling, Crop Module/Apply, Segment Editor Module, Add, Threshold with lower limit 300 / Apply, Data Module, Export visible segments of binary labelmap to model, Save model in STL.</p>

---

## Post #2 by @pieper (2023-01-01 19:51 UTC)

<p>You should be able to get the same mesh resolution with either version.  Maybe post some screenshots so we have a better idea what you are referring to.</p>

---

## Post #3 by @mdileo (2023-01-05 20:26 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea64212131265102388dfb68fcd25354a785ecea.jpeg" data-download-href="/uploads/short-url/xrwfLLGXyReIoCn98Ciz1cOBAh4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea64212131265102388dfb68fcd25354a785ecea_2_690x385.jpeg" alt="image" data-base62-sha1="xrwfLLGXyReIoCn98Ciz1cOBAh4" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea64212131265102388dfb68fcd25354a785ecea_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea64212131265102388dfb68fcd25354a785ecea_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea64212131265102388dfb68fcd25354a785ecea.jpeg 2x" data-dominant-color="706F6F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1355×758 77.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I have included the side-by-side dicom uploads processed by Slicer 4.11 on the left and 5.0.3 on the right as imported into Meshmixer.  The 4.11 one on the left has much better definition of foramina then the right. The image on the right appears to be over smoothed from the original. After I submitted the initial post, I did continue to investigate the problem in the 5.0.3 version. It appears in the Segment Editor module there is a drop-down to the right of the “Show 3D” button which has “Surface Smoothing” as the default with a “Smoothing Factor” of 0.5. If I adjust the smoothing factor down to 0.25, it seems to get a model more consistent with the one I have been making in the 4.11 version. This Surface Smoothing option and factor is nowhere in the workflow when I create models in the 4.11 version so I am not sure how it automatically gets into the process in the 5.0.3 version. This appears to be causing my differences between the 2 versions. Are you aware of how the two different versions do and do not implement this default smoothing process that I have in the newer version. I currently create the model in the 4.11 version just using the “Editor” module and do not use the “Segment Editor” module, at all. This is older “Editor” module not available in the new 5.0.3 version.</p>

---

## Post #4 by @pieper (2023-01-05 21:01 UTC)

<p>Thanks for the image and the extra context.  Yes, the defaults have changed but you should be able to get the exact same results but the interface and the defaults are different.</p>
<p>We did retire the old Editor module to focus support and development on the Segment Editor, which has proven to be a good strategy as it has more features and continues to improve.</p>
<p>The old Editor’s model button had a similar functionality to the Show 3D feature, just with different defaults.  Under the hood it used the Model Maker module, which is still available.  If you want to replicate the old behavior you can export the Segmentation as a LabelMap Volume and use the Model Maker and get essentially identical results.  Or, as you’ve found you can change the settings of the closed surface representation of Segmentations.  There are also advanced options in the Representations section of the Segmentations Module.</p>
<p>Let us know if this doesn’t give you what you need.</p>

---

## Post #5 by @mdileo (2023-01-05 21:15 UTC)

<p>Thank you for the explanation and assistance. I will work with the newer version to optimize the model settings.</p>
<p>Thank you,</p>

---
