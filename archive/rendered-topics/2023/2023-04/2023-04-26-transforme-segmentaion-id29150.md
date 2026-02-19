---
topic_id: 29150
title: "Transforme Segmentaion"
date: 2023-04-26
url: https://discourse.slicer.org/t/29150
---

# Transforme segmentaion

**Topic ID**: 29150
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/transforme-segmentaion/29150

---

## Post #1 by @Thirawat (2023-04-26 20:31 UTC)

<p>I annotated a big dataset (for me), but the Dicom file of the CT scan has transformed (I get this from start).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/419e1112319f6bddf5fc398bcd536314b330144c.png" alt="image" data-base62-sha1="9mtGTCaftfDwhVwawS4CU3j5TfC" width="437" height="91"></p>
<p>when I <a href="https://discourse.slicer.org/t/reads-dcm-volume-with-grid-transform-with-python/28998">use this segment in Python by simpleITK [The problem post]</a> it will not match with the CT image because the CT image that simpleITK can read is raw Dicom file not Dicom transformed.</p>
<p>so I want to fix this problem by doing something with the segment after trying to do something with Dicom.<br>
but I can’t find a way to transform segmentation.</p>
<p>Thank you.<br>
Thirawat</p>

---

## Post #2 by @pieper (2023-04-26 20:47 UTC)

<p>The <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#basic-usage">acquisition transform</a>  accounts for irregularity in the spacing and other <a href="https://github.com/Slicer/Slicer/commit/3328b81211cb2e9ae16a0b49097744171c8c71c0">issues with the geometry</a>.  You can right click on the icon in the transform column and pick the “Harden transform” option to resample.  You probably want also apply the transform and harden the segmentation.</p>

---

## Post #3 by @Thirawat (2023-04-26 21:59 UTC)

<p><strong>I think this way will work.</strong><br>
I try on one Dicaom and on Segment<br>
<strong>but</strong> when ‘Harden transform’ on Dicom some side of the image is out of  ‘View Box’, and some side do not reach the side of the box. then when I read it the shape is (80, 613, 512)</p>
<p>for more context, I draw a little thing.<br>
<strong>How to crop this?</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b08f59c6875955f134509bbd193e1c9904625382.png" data-download-href="/uploads/short-url/pbVa3B5yGMre3gAhWS4vvJlralI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b08f59c6875955f134509bbd193e1c9904625382.png" alt="image" data-base62-sha1="pbVa3B5yGMre3gAhWS4vvJlralI" width="573" height="500" data-dominant-color="FDFBFC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">737×643 5.66 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><strong>[Edit]</strong><br>
First CT Dicom shape → (82, 512, 512)<br>
Segment shape → (82, 512, 512)<br>
CT Dicom Harden transform’ shape → (80, 613, 512)</p>
<p>Need to fix:</p>
<ol>
<li>missing slide</li>
<li>crop slide in to Box</li>
</ol>

---

## Post #4 by @pieper (2023-04-26 22:48 UTC)

<p>Probably you can use CropVolume for this.  If you can sort it out please include some screenshots to illustrate what’s not working for you.</p>

---

## Post #5 by @Thirawat (2023-04-28 04:31 UTC)

<p>Thank you very much now I find a way to manage with this problem.</p>
<p>my problem: Creating a segmentation dataset with CT has transformed. but Python cant read the CT transform and can only read raw CT.</p>
<p>so I solve it by creating an inverted transform segmentation.<br>
for more details:</p>
<ul>
<li>I have CT .dcm with transformed. and have segmentation nrrd.</li>
<li>Import segmentation as volume.</li>
<li>Clone transform form CT to segmentation volume.</li>
<li>Invert transform and Edit properties to apply to segmentation volume.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f860f6198cc3cbf0419739e4043978744152989.png" alt="image" data-base62-sha1="93XiMTfczChXo3bymKsus3WLZIB" width="642" height="206">
</li>
<li>then “Harden transform” segmentation.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02fb00f97f50d5c20cd3962c52d4a263b3b32d8a.png" alt="image" data-base62-sha1="qmJ8SJqVEVKmwGayKB3UeYyM1s" width="461" height="158"><br>
and save it as dicom.</li>
</ul>
<p>for the shape problem that will change I slove in Python (just cut it off):</p>
<pre><code class="lang-auto"># read dicom filse (CT, mask)
ct_image_array = readCT(dir_ct_paths[n])
label_image_array = readLabel(dir_label_paths[n])

# preprocess mass
label_image_array = label_image_array[:ct_image_array.shape[0], :512, :512]
</code></pre>

---
