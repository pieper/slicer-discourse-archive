# Reconstructing a 3D volume from 2D slices

**Topic ID**: 37846
**Date**: 2024-08-12
**URL**: https://discourse.slicer.org/t/reconstructing-a-3d-volume-from-2d-slices/37846

---

## Post #1 by @Trung_L_i_Quang (2024-08-12 17:36 UTC)

<p>Dear community,<br>
I am a newbie to 3D Slicer and I’m hoping to get some advice!</p>
<p>I have a dataset consisting of 1700 2D image slices (60GB total) originally in 16-bit TIFF format. I converted these to 8-bit JPEGs (400MB total) using Photoshop software for easier handling.</p>
<p>Using the SlicerMorph extension, I reconstructed a 3D volume from these JPEG slices (attached image). My goal is to segment this volume into regions based on intensity values:</p>
<ul>
<li>Silica: High intensity values (210-255)</li>
<li>High Organic Matter: Intermediate intensity values (110-200)</li>
<li>Low Organic Matter: Lower intensity values (50-110)</li>
<li>Air: Intensity values below 50</li>
</ul>
<p>I’ve attempted to use the Segment Editor’s Threshold function to accomplish it. However, the threshold value range is limited to 0 to 16 rather than 0 to 255.</p>
<p>Could you please advise me on how to proceed?<br>
Any assistance you can provide would be greatly appreciated!<br>
Best regards,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb20901e61cbe4f243ce0be124f85639b21c1cc1.jpeg" data-download-href="/uploads/short-url/qHp3gY7RGZIIXAX8awXyvg4tbDb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb20901e61cbe4f243ce0be124f85639b21c1cc1_2_690x373.jpeg" alt="image" data-base62-sha1="qHp3gY7RGZIIXAX8awXyvg4tbDb" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb20901e61cbe4f243ce0be124f85639b21c1cc1_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb20901e61cbe4f243ce0be124f85639b21c1cc1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb20901e61cbe4f243ce0be124f85639b21c1cc1.jpeg 2x" data-dominant-color="B6B8CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">945×511 82.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e276847e56f563b8575045f42844db6d2a42d394.png" data-download-href="/uploads/short-url/wjnPwoivirgjivGsT4XL5GN0A1S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e276847e56f563b8575045f42844db6d2a42d394_2_405x500.png" alt="image" data-base62-sha1="wjnPwoivirgjivGsT4XL5GN0A1S" width="405" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e276847e56f563b8575045f42844db6d2a42d394_2_405x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e276847e56f563b8575045f42844db6d2a42d394_2_607x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e276847e56f563b8575045f42844db6d2a42d394_2_810x1000.png 2x" data-dominant-color="F0F0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">945×1166 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cbb8a663edaea282238e245e7fed3f9709fde33.png" data-download-href="/uploads/short-url/mmwhW9hMW9Yvoe6v8CiwCzxYzm3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cbb8a663edaea282238e245e7fed3f9709fde33_2_405x500.png" alt="image" data-base62-sha1="mmwhW9hMW9Yvoe6v8CiwCzxYzm3" width="405" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cbb8a663edaea282238e245e7fed3f9709fde33_2_405x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cbb8a663edaea282238e245e7fed3f9709fde33_2_607x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cbb8a663edaea282238e245e7fed3f9709fde33_2_810x1000.png 2x" data-dominant-color="F1F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">945×1166 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-08-12 19:00 UTC)

<aside class="quote no-group" data-username="Trung_L_i_Quang" data-post="1" data-topic="37846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/trung_l_i_quang/48/70377_2.png" class="avatar"> Trung_L_i_Quang:</div>
<blockquote>
<p>I converted these to 8-bit JPEGs (400MB total) using Photoshop software for easier handling.</p>
</blockquote>
</aside>
<p>Tha’ts probably your initial problem. At this point you don’t know what happened to the intensities during that conversion.</p>
<p>Instead you can import the your original TIFF at lower resolution (preview option), and see what the original intensity distribution looked like. You can use this script to do that: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#slicer-plots-displayed-in-view-layout" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<aside class="quote no-group" data-username="Trung_L_i_Quang" data-post="1" data-topic="37846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/trung_l_i_quang/48/70377_2.png" class="avatar"> Trung_L_i_Quang:</div>
<blockquote>
<ul>
<li>Silica: High intensity values (210-255)</li>
<li>High Organic Matter: Intermediate intensity values (110-200)</li>
<li>Low Organic Matter: Lower intensity values (50-110)</li>
<li>Air: Intensity values below 50</li>
</ul>
</blockquote>
</aside>
<p>How do you know these values correspond to those materials? Air should be just around 0.</p>
<p>I would just look at the intensity distribution plot and see if you can make out four peak as you expected to see, and use the values around those peaks to do my segmentation.</p>

---

## Post #3 by @Trung_L_i_Quang (2024-08-13 15:51 UTC)

<p>Dear Mr. Muratmaga,</p>
<p>I have constructed a 3D volume from the original .tiff format data. However, the density range of this volume is limited to 0-15 instead of the expected 0-255 range.</p>
<p>It’s important to note that this density range aligns with previous research on the material of my sample.</p>
<p>The desired intensity ranges for segmentation are as follows:</p>
<ul>
<li>Silica: High intensity values (210-255)</li>
<li>High Organic Matter: Intermediate intensity values (110-200)</li>
<li>Low Organic Matter: Lower intensity values (50-110)</li>
<li>Air: Intensity values below 50</li>
</ul>
<p>I am facing challenges in achieving this segmentation due to the limited density range of my 3D volume.</p>
<p>Could you please suggest potential solutions or alternative approaches?</p>
<p>Thank you for your time and assistance.</p>
<p>Best regards,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/899eeb84c7e9f4f6098e569dd76a06927b519cf5.jpeg" data-download-href="/uploads/short-url/jDrTFNqsKzl01mJQgA694t6amDX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/899eeb84c7e9f4f6098e569dd76a06927b519cf5_2_391x500.jpeg" alt="image" data-base62-sha1="jDrTFNqsKzl01mJQgA694t6amDX" width="391" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/899eeb84c7e9f4f6098e569dd76a06927b519cf5_2_391x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/899eeb84c7e9f4f6098e569dd76a06927b519cf5_2_586x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/899eeb84c7e9f4f6098e569dd76a06927b519cf5_2_782x1000.jpeg 2x" data-dominant-color="F3F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1530×1956 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d599001e39154fe170539b3c2d7e9729c214284.jpeg" data-download-href="/uploads/short-url/8KJ0MalJBFjoaZLQECU233YA7e4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d599001e39154fe170539b3c2d7e9729c214284_2_690x373.jpeg" alt="image" data-base62-sha1="8KJ0MalJBFjoaZLQECU233YA7e4" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d599001e39154fe170539b3c2d7e9729c214284_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d599001e39154fe170539b3c2d7e9729c214284_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d599001e39154fe170539b3c2d7e9729c214284_2_1380x746.jpeg 2x" data-dominant-color="B2B4C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1038 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-08-13 17:20 UTC)

<aside class="quote no-group" data-username="Trung_L_i_Quang" data-post="3" data-topic="37846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/trung_l_i_quang/48/70377_2.png" class="avatar"> Trung_L_i_Quang:</div>
<blockquote>
<p>I have constructed a 3D volume from the original .tiff format data. However, the density range of this volume is limited to 0-15 instead of the expected 0-255 range.</p>
<p>It’s important to note that this density range aligns with previous research on the material of my sample.</p>
</blockquote>
</aside>
<p>If used the original data, then it means your dataset is reconstructed with those values. Slicer doesn’t do anything but the report the values stored in those files. You should really check with the lab that did the imaging why that’s the case.</p>
<p>You can rescale the intesities in Slicer (SimpleFilters-&gt;RescaleIntensity), but it is better option to reconstruct the cross-sectional slices with proper intensity values in the first place.</p>

---

## Post #5 by @lassoan (2024-08-13 19:22 UTC)

<p>In Volumes module / Volume information section, what are the number of scalars, scalar type and scalar range values?</p>
<p>Do the slice views look as you expect? If you hover over various regions with your mouse in slice views do the intensity values in the data probe (lower left corner) look good?</p>
<p>Does everything work as you expect if you use the latest Slicer Preview Release?</p>

---

## Post #6 by @Trung_L_i_Quang (2024-08-14 01:23 UTC)

<p>The volume information section shows the number of Scalars equal to 1, with a scalar range of 1 to 15 (see attached image). The data probe’s intensity values are limited to 0 to 15, rather than the intended range of 0 to 255.<br>
Could you kindly provide any viable answers or alternative approaches to my problem?<br>
Thank you for your time and help.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fa0fd1d92734fcb0b148341d4e14880b4d33a48.jpeg" data-download-href="/uploads/short-url/fVvUN3H9kMlrLR59Uvi2DCCwVBe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fa0fd1d92734fcb0b148341d4e14880b4d33a48_2_690x373.jpeg" alt="image" data-base62-sha1="fVvUN3H9kMlrLR59Uvi2DCCwVBe" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fa0fd1d92734fcb0b148341d4e14880b4d33a48_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fa0fd1d92734fcb0b148341d4e14880b4d33a48_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fa0fd1d92734fcb0b148341d4e14880b4d33a48_2_1380x746.jpeg 2x" data-dominant-color="C1C1C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1038 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2024-08-14 03:58 UTC)

<aside class="quote no-group" data-username="Trung_L_i_Quang" data-post="6" data-topic="37846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/trung_l_i_quang/48/70377_2.png" class="avatar"> Trung_L_i_Quang:</div>
<blockquote>
<p>Could you kindly provide any viable answers or alternative approaches to my problem?</p>
</blockquote>
</aside>
<p>What you show in screenshots looks more like Xray projection images rather than cross-sectional slices. Please check it the lab that did the imaging and have them give you the correct dataset.</p>

---

## Post #8 by @Trung_L_i_Quang (2024-08-14 05:18 UTC)

<p>Yes, my data consists of synchrotron-based X-ray tomographic microscopy (SRXTM) images. However, I don’t understand the difference between X-ray projection and cross-sectional slices. I have no experience in this subject; could you kindly explain it in detail for me? Furthermore, can the 3D Slicer software help me reconstruct X-ray projections?<br>
Thank you for your time and help!</p>

---

## Post #9 by @muratmaga (2024-08-14 05:31 UTC)

<p>X-ray projection images are 2D images taken at many angles. These need to be run through an “reconstruction” algorithm to derive cross-section image that will help you create a virtual 3D representation of the scanned object. You can read this wikipedia topic. <a href="https://en.wikipedia.org/wiki/Cone_beam_reconstruction" class="inline-onebox" rel="noopener nofollow ugc">Cone beam reconstruction - Wikipedia</a></p>
<p>While there are software packages to do this (such as TomoPy, <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4181643/" class="inline-onebox" rel="noopener nofollow ugc">TomoPy: a framework for the analysis of synchrotron&nbsp;tomographic data - PMC</a>), this is normally done by the lab that conduct the imaging session. Your best option is to reach out to them and ask for the cross-sectional images.</p>

---

## Post #10 by @Trung_L_i_Quang (2024-08-15 10:00 UTC)

<p>Dear Mr. Muratmaga,</p>
<p>I have successfully resolved the issue with the density value display. The density values in my data were not within the expected range of 0-255 due to an error during the conversion from TIFF to JPEG format using Photoshop. I have since used a different software and successfully resolved this issue. The density values now correctly display from 0 to 255 (see attached image).</p>
<p>This image is a micro-CT scan of a grain sample. My goal is to segment the entire tomographic volume based on predefined intensity ranges: high values (210-255) for silica, intermediate values (110-200) for high organic matter, lower values (50-110) for low organic matter, and values below 50 for air.</p>
<p>However, the 3D image currently includes the sample holder. My objective is to isolate the volume of the sample itself before performing segmentation. Could you please suggest a method to achieve this?</p>
<p>Thank you for your time and help!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7ab57986797b57f541960e56c0f76595e931dc.jpeg" data-download-href="/uploads/short-url/bcg90pSD9uiIUluhE1TDVkmfrCk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7ab57986797b57f541960e56c0f76595e931dc_2_690x373.jpeg" alt="image" data-base62-sha1="bcg90pSD9uiIUluhE1TDVkmfrCk" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7ab57986797b57f541960e56c0f76595e931dc_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7ab57986797b57f541960e56c0f76595e931dc_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7ab57986797b57f541960e56c0f76595e931dc_2_1380x746.jpeg 2x" data-dominant-color="B7B7C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1038 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @pieper (2024-08-15 12:42 UTC)

<p>As <a class="mention" href="/u/muratmaga">@muratmaga</a> pointed out, the data you are displaying is the X-ray projection data, basically a series of shadows and what you need is the reconstructed volume data.  This reconstruction step is typically performed on the scanning device and so you should be able to request this reconstructed data from whoever gave you the scan.  Please follow the links that Murat provided to learn more.</p>

---

## Post #12 by @muratmaga (2024-08-15 15:49 UTC)

<aside class="quote no-group" data-username="Trung_L_i_Quang" data-post="10" data-topic="37846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/trung_l_i_quang/48/70377_2.png" class="avatar"> Trung_L_i_Quang:</div>
<blockquote>
<p>Could you please suggest a method to achieve this?</p>
</blockquote>
</aside>
<p>You cannot do what you want to do with this dataset. You have the wrong dataset. Obtain the cross-sections.</p>

---
