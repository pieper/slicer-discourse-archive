---
topic_id: 31110
title: "Aapm Tg 18 Tests Not Rendering Correct Luminance Values"
date: 2023-08-11
url: https://discourse.slicer.org/t/31110
---

# AAPM TG-18 tests not rendering correct luminance values

**Topic ID**: 31110
**Date**: 2023-08-11
**URL**: https://discourse.slicer.org/t/aapm-tg-18-tests-not-rendering-correct-luminance-values/31110

---

## Post #1 by @wayfarer3130 (2023-08-11 20:58 UTC)

<p>I was testing slicer using the AAPM TG-18 test dataset from here:<br>
<a href="https://deckard.duhs.duke.edu/~samei/samei_tg18/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://deckard.duhs.duke.edu/~samei/samei_tg18/</a><br>
looking at the luminance tests.  The RGB pixel value for the luminance 2 test should be <span class="hashtag-raw">#0F0F0F</span> (this is the value in the center of the image).  This can be seen by reading the raw pixel value in the center, which is 240, and then apply the window width/center of 4080/2040 using the formulas from the DICOM standard:<br>
y = ((x - (c - 0.5)) / (w-1) + 0.5) * (ymax- ymin) + ymin<br>
So, plugging in x=240, c=2040, w=4080, ymax=255, ymin=0, we get:<br>
y = ((240 - (2040 - 0.5)) / (4080-1) + 0.5) * 255 = 15.003<br>
which, when rounded should be 0F hex, but the value I’m seeing in 3D Slicer is 0D.  Interestingly, OHIF, also based on VTK, produces a 0E value, also incorrect.</p>

---

## Post #2 by @lassoan (2023-08-11 21:40 UTC)

<p>I’ve loaded <code>2: TG18-LN</code> series of <code>lumin-1k-dcm.zip</code> and the <strong>rendering in Slicer-5.2.2 was perfect</strong> (on Windows11, using Intel Integrated Graphics):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56694132633ddd124bbf3c5e355035f0f53b2336.png" data-download-href="/uploads/short-url/ckqzjo5YmTUf7r2ftiDJjvf2eQC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56694132633ddd124bbf3c5e355035f0f53b2336_2_641x500.png" alt="image" data-base62-sha1="ckqzjo5YmTUf7r2ftiDJjvf2eQC" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56694132633ddd124bbf3c5e355035f0f53b2336_2_641x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56694132633ddd124bbf3c5e355035f0f53b2336.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56694132633ddd124bbf3c5e355035f0f53b2336.png 2x" data-dominant-color="767976"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">756×589 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Numeric values (voxel HU is read from Data probe in Slicer; rendered pixel value is read from a screen capture):</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Voxel HU</th>
<th>Rendered pixel value</th>
</tr>
</thead>
<tbody>
<tr>
<td>4080</td>
<td>255</td>
</tr>
<tr>
<td>3840</td>
<td>240</td>
</tr>
<tr>
<td>3600</td>
<td>225</td>
</tr>
<tr>
<td>3360</td>
<td>210</td>
</tr>
<tr>
<td>3120</td>
<td>195</td>
</tr>
<tr>
<td>2880</td>
<td>180</td>
</tr>
<tr>
<td>2640</td>
<td>165</td>
</tr>
<tr>
<td>2400</td>
<td>150</td>
</tr>
<tr>
<td>2160</td>
<td>135</td>
</tr>
<tr>
<td>1920</td>
<td>120</td>
</tr>
<tr>
<td>1680</td>
<td>105</td>
</tr>
<tr>
<td>1440</td>
<td>90</td>
</tr>
<tr>
<td>1200</td>
<td>75</td>
</tr>
<tr>
<td>960</td>
<td>60</td>
</tr>
<tr>
<td>720</td>
<td>45</td>
</tr>
<tr>
<td>480</td>
<td>30</td>
</tr>
<tr>
<td>240</td>
<td>15</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>
</div><p>What positions you measured at? Interpolation is enabled by default, so if you are not at the exact center of the slice then you’ll get values interpolated between neighbor slices. See rendering with interpolation enabled:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f447ee24886c759fad16d5f79120cb05ba7bcf34.png" data-download-href="/uploads/short-url/yR0BYWynaJuDcNsjMDt9TWKcIcs.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f447ee24886c759fad16d5f79120cb05ba7bcf34.png" alt="image" data-base62-sha1="yR0BYWynaJuDcNsjMDt9TWKcIcs" width="677" height="500" data-dominant-color="7E807D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">747×551 19.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve checked the result with interpolation enabled and at slice center positions all the rendered pixel values were perfect.</p>
<p>What operating system do you use? Have you enabled any night light/blue light filter or HDR display, or performed any kind of screen calibration on your computer? On some operating systems or when using some third-party applications, appearance of screenshots may be affected by such settings.</p>

---

## Post #3 by @wayfarer3130 (2023-08-12 15:17 UTC)

<p>Looks like this has been resolved in 5.2.2 - I upgraded (but forgot to check which version I was running), and it is now displaying the right values for the luminance.</p>

---

## Post #4 by @alireza (2023-08-12 19:45 UTC)

<p>For me it is 0D on Mac M2 GPU on Slicer 5.2.2</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e369bbfe3f068593c7c5a6f5c3b808f35b79dbb7.png" data-download-href="/uploads/short-url/wrMV4JXALQMx9YpfKQhycVwCx6f.png?dl=1" title="CleanShot 2023-08-12 at 15.45.13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e369bbfe3f068593c7c5a6f5c3b808f35b79dbb7_2_690x421.png" alt="CleanShot 2023-08-12 at 15.45.13" data-base62-sha1="wrMV4JXALQMx9YpfKQhycVwCx6f" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e369bbfe3f068593c7c5a6f5c3b808f35b79dbb7_2_690x421.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e369bbfe3f068593c7c5a6f5c3b808f35b79dbb7_2_1035x631.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e369bbfe3f068593c7c5a6f5c3b808f35b79dbb7_2_1380x842.png 2x" data-dominant-color="767680"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CleanShot 2023-08-12 at 15.45.13</span><span class="informations">1591×973 45.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> can you test this dicom <a href="https://www.dropbox.com/scl/fi/hxzbtacfugtkv1i38ta1c/TG18-LN-1k-02.dcm?rlkey=rf3cb0ec8yh6m1l05sahrgjq3&amp;dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - TG18-LN-1k-02.dcm - Simplify your life</a></p>

---

## Post #5 by @lassoan (2023-08-13 05:59 UTC)

<p>This is a volume and by default you see interpolated values, so it matters where you do the probing.</p>
<p>What is the RAS position and the voxel value where the rendered pixel is 0x0d?</p>
<p>If you disable interpolation and probe each slice do you see the same voxel and rendered pixel values as in the table above?</p>

---

## Post #6 by @gcsharp (2023-08-13 21:53 UTC)

<p>Hi all,  Let’s back up a second.  Any Medical Physicist who thinks to use 3D Slicer in fulfilling regulatory testing, he or she needs to do testing and keep records as to how they verified said software.</p>
<p><a class="mention" href="/u/wayfarer3130">@wayfarer3130</a>,  <a class="mention" href="/u/alireza">@alireza</a>, where are you going with this?</p>

---

## Post #7 by @alireza (2023-08-14 13:57 UTC)

<p>I’m not picking the color on the edge of grey/black to get affected with the interpolation. Although I turned it off and it is still showing 0D (maybe it is only on Mac?)</p>
<p>Just note that we are talking about a color picker and not talking about the color lookup table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c668f580761c321a357189a092b82f703aafcc1e.png" data-download-href="/uploads/short-url/sjdpAC6aPC2OihghewK4mNzM6F8.png?dl=1" title="CleanShot 2023-08-14 at 09.54.48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c668f580761c321a357189a092b82f703aafcc1e_2_690x307.png" alt="CleanShot 2023-08-14 at 09.54.48" data-base62-sha1="sjdpAC6aPC2OihghewK4mNzM6F8" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c668f580761c321a357189a092b82f703aafcc1e_2_690x307.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c668f580761c321a357189a092b82f703aafcc1e_2_1035x460.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c668f580761c321a357189a092b82f703aafcc1e.png 2x" data-dominant-color="A8A1A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CleanShot 2023-08-14 at 09.54.48</span><span class="informations">1163×518 76.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/gcsharp">@gcsharp</a> Bill showed this to me that we (at Cornerstone3D) are off by 0.5 in window level (PR here <a href="https://github.com/cornerstonejs/cornerstone3D/pull/736" class="inline-onebox" rel="noopener nofollow ugc">Fix an off by 0.5/1 error in window level calculations by wayfarer3130 · Pull Request #736 · cornerstonejs/cornerstone3D · GitHub</a>) and I was interested to see what are other softwares doing regarding this and here we are</p>

---

## Post #8 by @lassoan (2023-08-14 21:55 UTC)

<p>Currently, in Slicer we don’t request any specific color space in the surface format, so the <a href="https://doc.qt.io/qt-5/qsurfaceformat.html#ColorSpace-enum"><code>default, unspecified color space</code></a> is used. This could either mean “monitor RGB” value or some standard color space, such as sRGB. If your display’s color profile is different from the color profile of the sceenshot you take then the pixel values may be slightly modified.</p>
<p><a class="mention" href="/u/wayfarer3130">@wayfarer3130</a>, <a class="mention" href="/u/alireza">@alireza</a>, what is the purpose of the testing? Do you expect to have your calculated 8-bit value to match the monitor RGB value or some standard color RGB value (e.g., sRGB)? Do you expect the 8-bit value to match perceptual lightness, luminance, luminosity,…?</p>
<aside class="quote no-group" data-username="gcsharp" data-post="6" data-topic="31110">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Let’s back up a second. Any Medical Physicist who thinks to use 3D Slicer in fulfilling regulatory testing, he or she needs to do testing and keep records as to how they verified said software.</p>
</blockquote>
</aside>
<p>Agreed. In the <a href="https://aapm.onlinelibrary.wiley.com/doi/full/10.1118/1.1861159">AAPM TG-18 test document</a> the testing is performed by calibrated instruments, not by inspecting screenshots. For example, how the TG18-LN pattern is supposed to be used:</p>
<blockquote>
<p>luminance is measured using a calibrated luminance meter at the center of the 18 TG18-LN test patterns, corresponding to 18 distinct digital driving levels</p>
</blockquote>

---
