# Saving T1-weighted image and segmentation labels as one file

**Topic ID**: 2042
**Date**: 2018-02-07
**URL**: https://discourse.slicer.org/t/saving-t1-weighted-image-and-segmentation-labels-as-one-file/2042

---

## Post #1 by @Clara_Korting (2018-02-07 11:40 UTC)

<p>Hi,<br>
I am segmenting muscles in the lower leg to later use these segmented volumes to combine them with DTI fascicle tracts and calculate muscle parameters of fascicles within the muscle volume.</p>
<p>For doing the fascicle tracking I am using DSI studio which uses a T1-weighted image and DTI image to do the tracking. It is difficult choosing the right muscle compartment from only the T1 image. I was now wondering if there is a way to overlay the T1 weighted image and segmentation map and save them together as .nii image so that I could use only this file for the DTI tracking.</p>
<p>Any help or hints would be very much appreciated! Thank you very much in advance!</p>
<p>Kind regards,<br>
Clara</p>
<p>Operating system: Mac OS High Sierra 10.13.3<br>
Slicer version: 4.8.0<br>
Expected behavior: T1 weighted image and label map saved in one file to use for DTI tracking<br>
Actual behavior: Both are separate files. I am able to load the segmentation file into the DTI software (DSI studio) but with only the labels a registration between DTI image and segmentation is not possible.</p>

---

## Post #2 by @lassoan (2018-02-07 15:07 UTC)

<p>You can export segments into labelmap volume and then use LabelOverlayImageFilter in <code>Simple Filters</code> module to combine these images. You may also try scale the labelmap volume and then add it to the T1 volume.</p>
<p>There are some limitations in color image support in Simple Filters module, so you need to do the followings:</p>
<ul>
<li>If the input T1 volume is not unsigned char then you need to convert it to <code>unsigned char</code> using <code>Cast scalar volume</code> (if your volume contained values &lt;0 or &gt;255 then before casting to unsigned char, use IntensityWindowingImageFilter in Simple Filters module, to fit a intensity range of your image data in the 0-255 output range)</li>
<li>After LabelOverlayImageFilter is completed, the resulting color image will not be displayed correctly in Slicer. You need to save the volume to file and then if you load the file into Slicer (or into DSI studio) then it should appear correctly.</li>
</ul>
<p>Output of LabelOverlayImageFilter is a color image, so if DSI studio cannot load color images then you may need to combine the T1 and labelmap volumes by simply scaling the labelmap and adding it to the T1 volume.</p>
<p>Upgrade your Slicer to 4.8.1. There were many fixes in the 4.8.1 patch release.</p>

---

## Post #3 by @Clara_Korting (2018-02-07 20:05 UTC)

<p>Thank you so much Andras for the extensive reply! How would I scale the labelmap and add it to the volume? I tried the LabelOverlayImageFilter you suggested but I get an error, that both images don’t match type or dimension.</p>
<p>Thank you again!</p>

---

## Post #4 by @lassoan (2018-02-07 20:07 UTC)

<p>After you saved LabelOverlayImageFilter output to file and loaded it into Slicer, did the image show up correctly? When you tried to load the same file into DSI studio, then did DSI studio report some errors?</p>

---

## Post #5 by @Clara_Korting (2018-02-07 20:45 UTC)

<p>It was an error in the LabelOverlayImageFilter. But I realised it was related to the segmentation label and volume not having the same size. I tried it on another segmentation and now it works! Thank you very much!</p>
<p>Is there a way to easily adjust the dimensions of the T1 image and segmentation labels to the same size?</p>

---

## Post #6 by @lassoan (2018-02-07 21:00 UTC)

<aside class="quote no-group" data-username="Clara_Korting" data-post="5" data-topic="2042">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/clara_korting/48/813_2.png" class="avatar"> Clara_Korting:</div>
<blockquote>
<p>Is there a way to easily adjust the dimensions of the T1 image and segmentation labels to the same size?</p>
</blockquote>
</aside>
<p>By default they have the same size if the T1 image was the first volume that you selected as master volume when you created the segmentation node in Segment Editor module.</p>
<p>You can also resample the segmentation to match any image by selecting that image as “Reference volume” in Segmentations module / Export/import… / Advanced section.</p>

---
