---
topic_id: 17641
title: "Dwi Adc Calculation"
date: 2021-05-16
url: https://discourse.slicer.org/t/17641
---

# DWI ADC calculation

**Topic ID**: 17641
**Date**: 2021-05-16
**URL**: https://discourse.slicer.org/t/dwi-adc-calculation/17641

---

## Post #1 by @RO786 (2021-05-16 17:06 UTC)

<p>Operating system:Windows 10<br>
Slicer version: 4.11.2020</p>
<p>Hello everyone,<br>
I’m quite new to the 3D slicer platform so very much appreciate any advice. This is not my field of expertise.<br>
I want to measure the ADC of the extraocular muscles. I have DICOM T1/T2W images, along with the corresponding DWI traces and ADC maps from the scanner.<br>
I wanted to know if it’s possible to segment a volume in the T1/T2 images and transpose this onto the  ADC map I have, in order to calculate the mean ADC of that volume?</p>
<p>I have downloaded the DWI extension but am unsure about how to start the process.<br>
I would be very grateful for some guidance!</p>
<p>Many thanks</p>

---

## Post #2 by @lassoan (2021-05-16 23:38 UTC)

<p>Yes, this should be no problem at all. You can segment the T1/T2W images using Segment Editor module then get mean ADC in the segmented regions using Segment Statistics module.</p>

---

## Post #3 by @RO786 (2021-05-17 11:28 UTC)

<p>Thank you very much.<br>
I have segmented in T1 image and used the segment statistics module to get the quantitative measurements. However, I only get volume. How would I go about overlaying the segmentation on the ADC trace so I could re-edit it if needed and then calculate the mean ADC?</p>
<p>Thank you very much for your time</p>

---

## Post #4 by @lassoan (2021-05-17 12:58 UTC)

<p>To get statistics about voxel values, select the ADC volume as reference volume in Segment Statistics module.</p>

---

## Post #5 by @RO786 (2021-05-17 18:13 UTC)

<p>Thank you. I’m still having a little difficulty -</p>
<ol>
<li>
<p>I save the ROIs I have segmented from the T1 images (thresh hold label maps) and re-open these as ‘segmentations’ using the ‘add data function’ ‘description’ drop down.</p>
</li>
<li>
<p>Create a master volume (ADC trace) in segment editor and from here go to the segmentations module where I can see the overlay of the ROI on the ADC trace.</p>
</li>
<li>
<p>In the segment statistics module I set the scalar volume to the ADC trace, however, only volume is calculated.  No ADC.</p>
</li>
</ol>
<p>I feel as though I’m missing a step somewhere but can’t quite work out what it is from the documents</p>
<p>Thank you so much for your time</p>

---

## Post #6 by @pieper (2021-05-17 18:59 UTC)

<p>Be sure that the Scalar Volume Statistics options are enabled:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85b5fcbb82663487f1b83fe660481b0f0fbff803.jpeg" data-download-href="/uploads/short-url/j4RpnPr7f4wuirM4rPuRYEr6IhR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85b5fcbb82663487f1b83fe660481b0f0fbff803_2_690x294.jpeg" alt="image" data-base62-sha1="j4RpnPr7f4wuirM4rPuRYEr6IhR" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85b5fcbb82663487f1b83fe660481b0f0fbff803_2_690x294.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85b5fcbb82663487f1b83fe660481b0f0fbff803_2_1035x441.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85b5fcbb82663487f1b83fe660481b0f0fbff803.jpeg 2x" data-dominant-color="DCDCDF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1135×484 84.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @RO786 (2021-05-17 19:18 UTC)

<p>Yes, all scalar volume statistics are enabled but no ADC output. Thank you</p>

---

## Post #8 by @lassoan (2021-05-17 20:03 UTC)

<p>I’ve just tested it with the latest Slicer Stable Release and it works well. Make sure you scroll right to see all the columns of the table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66917f8780180d15da9c89becb087a653ff16d22.png" data-download-href="/uploads/short-url/eDmqGixCA5qseTWfdrLUMXVv3Zo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66917f8780180d15da9c89becb087a653ff16d22_2_690x451.png" alt="image" data-base62-sha1="eDmqGixCA5qseTWfdrLUMXVv3Zo" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66917f8780180d15da9c89becb087a653ff16d22_2_690x451.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66917f8780180d15da9c89becb087a653ff16d22_2_1035x676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66917f8780180d15da9c89becb087a653ff16d22_2_1380x902.png 2x" data-dominant-color="C0BFBF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2276×1489 497 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @RO786 (2021-05-17 20:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7d0470c2ba63434cece29278d42f8543eefea0.png" data-download-href="/uploads/short-url/bcl5Eh4UBbOZEEkReFvLSOEXhAY.png?dl=1" title="Screenshot 2021-05-17 21.18.17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7d0470c2ba63434cece29278d42f8543eefea0_2_690x387.png" alt="Screenshot 2021-05-17 21.18.17" data-base62-sha1="bcl5Eh4UBbOZEEkReFvLSOEXhAY" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7d0470c2ba63434cece29278d42f8543eefea0_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7d0470c2ba63434cece29278d42f8543eefea0_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7d0470c2ba63434cece29278d42f8543eefea0.png 2x" data-dominant-color="CFCFD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-05-17 21.18.17</span><span class="informations">1366×768 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So very much appreciated.<br>
This is my screenshot. ADC map and ROI. Below are my statistics. I assumed that because it says ‘volume’ that the ‘mean calculation’ was pertaining to ‘mean volume’ rather than mean ADC. Is this incorrect?</p>

---

## Post #10 by @pieper (2021-05-17 20:32 UTC)

<p>Yes, it means the statistics are calculated for the node you have selected as the “Scalar volume” in the module interface at the time the Apply button is pressed (e.g. you could get statistics over the same region for different MR contrasts).</p>

---

## Post #11 by @RO786 (2021-05-17 21:22 UTC)

<p>Oh goodness, I had the ADC all along. Steep learning curve for me.<br>
Thank you for your attention and help!</p>

---

## Post #12 by @dszimatore (2022-03-11 11:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e77a15cbe3fae9ed0b465cebfe1f877f04cb9d00.jpeg" data-download-href="/uploads/short-url/x1JRr5jo1ms2Qr1LedWTJ5Gb2zm.jpeg?dl=1" title="dwi.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e77a15cbe3fae9ed0b465cebfe1f877f04cb9d00_2_690x457.jpeg" alt="dwi.PNG" data-base62-sha1="x1JRr5jo1ms2Qr1LedWTJ5Gb2zm" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e77a15cbe3fae9ed0b465cebfe1f877f04cb9d00_2_690x457.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e77a15cbe3fae9ed0b465cebfe1f877f04cb9d00_2_1035x685.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e77a15cbe3fae9ed0b465cebfe1f877f04cb9d00.jpeg 2x" data-dominant-color="9A9A9C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dwi.PNG</span><span class="informations">1256×833 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
So the values “minimum”, “maximum”, “mean”, “median” and “standard deviation” refer all to ADC? But<br>
<strong>x 10-3 mm2/s OR x 10-6 mm2/s ?</strong><br>
Is there an easy way to obtain histogram values for the volume segmented?<br>
I tried with python scripts but still I make some mistake and I don’t understand how and if python language interact with GUI.</p>
<p>Many thanks"</p>

---
