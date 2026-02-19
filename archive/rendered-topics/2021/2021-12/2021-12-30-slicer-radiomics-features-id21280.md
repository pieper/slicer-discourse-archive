---
topic_id: 21280
title: "Slicer Radiomics Features"
date: 2021-12-30
url: https://discourse.slicer.org/t/21280
---

# Slicer radiomics-features

**Topic ID**: 21280
**Date**: 2021-12-30
**URL**: https://discourse.slicer.org/t/slicer-radiomics-features/21280

---

## Post #1 by @MPhilip (2021-12-30 14:49 UTC)

<p>Operating system:Windows 10 enterprise<br>
Slicer version:3D slicer 4.13.0-2021-12-15<br>
Hi</p>
<p>I was extracting features using the Slicer radiomics module from GTV of RTStruct. But when I see the table containing the features most of the GLCM and NGTDM features give ‘zero’ as the output as seen in the image, I am not sure where I am going wrong. Some of the feature values look identical too.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f27458d9dbe2b4eb6df173fda362356d7a3ae9dd.jpeg" data-download-href="/uploads/short-url/yAQORfNSmBeUdyjPdN5e2Y4gLut.jpeg?dl=1" title="manual-rtstruct" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f27458d9dbe2b4eb6df173fda362356d7a3ae9dd_2_142x500.jpeg" alt="manual-rtstruct" data-base62-sha1="yAQORfNSmBeUdyjPdN5e2Y4gLut" width="142" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f27458d9dbe2b4eb6df173fda362356d7a3ae9dd_2_142x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f27458d9dbe2b4eb6df173fda362356d7a3ae9dd_2_213x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f27458d9dbe2b4eb6df173fda362356d7a3ae9dd_2_284x1000.jpeg 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">manual-rtstruct</span><span class="informations">1024×3586 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Python interactor displays the below message:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c338df2c2ca53cc735435a21c693be472683e5f8.png" data-download-href="/uploads/short-url/rR0X8WaalTcgScRPx1DHvg9cBRu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c338df2c2ca53cc735435a21c693be472683e5f8.png" alt="image" data-base62-sha1="rR0X8WaalTcgScRPx1DHvg9cBRu" width="690" height="378" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1541×846 57.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ef021ba84bd8fa63f20d6f23b7ef1bc69424440.png" data-download-href="/uploads/short-url/289acjfh3VYfGgxXMSSejC7L596.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ef021ba84bd8fa63f20d6f23b7ef1bc69424440.png" alt="image" data-base62-sha1="289acjfh3VYfGgxXMSSejC7L596" width="690" height="100" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1400×204 10.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer radiomics window is as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdba0c20d5f15b066cd372ff44d941b776344dab.png" data-download-href="/uploads/short-url/tlWu8ASkbKneQZyBejT7FijrPBh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdba0c20d5f15b066cd372ff44d941b776344dab_2_690x369.png" alt="image" data-base62-sha1="tlWu8ASkbKneQZyBejT7FijrPBh" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdba0c20d5f15b066cd372ff44d941b776344dab_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdba0c20d5f15b066cd372ff44d941b776344dab_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdba0c20d5f15b066cd372ff44d941b776344dab_2_1380x738.png 2x" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1902×1018 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be appreciated.</p>
<p>Thanks</p>

---

## Post #2 by @JoostJM (2022-01-11 11:51 UTC)

<p>Firstorder: range is 9, while your binwidth is set to 64. This means that after discretization, all pixels are assigned to the same bin, resulting in a ‘flat region’. Your features reflect this.</p>

---

## Post #3 by @MPhilip (2022-01-11 11:57 UTC)

<p>Thanks for your response and I appreciate it.<br>
Then if possible could you please suggest the ideal bin width that gives me accurate feature values?<br>
Also if I won’t set resampled voxel size, still I get an answer, so is there a default voxel size value?</p>
<p>Thanks in advance</p>

---

## Post #4 by @JoostJM (2022-01-11 12:02 UTC)

<p>The ‘ideal’ bin width is a bit tricky. See also the documentation of PyRadiomics.<br>
Generally, my advice would be to run an extraction using just firstorder on your entire dataset. Then, choose a binwidth so, that you would get between 10 and 100 bins for the largest part of your dataset. (use the feature range. If the values of this features are between, say, 50 and 500, choose bin width of 5).</p>
<p>As to size resampling, this is mainly to make your dataset more homogeneous and isotropic. See also the documentation. Try not to oversample too much (i.e. don’t resample to .5 if you have a slice thickness &gt; 2). In your case, I’d suggest 3x3x3 or 3.5x3.5x3.5. Again, this depends on your entire dataset. Is there much variation in spacing? Choose a good compromise.</p>

---

## Post #5 by @MPhilip (2022-01-11 12:26 UTC)

<p>Thanks for your suggestions.<br>
Actually, I intended to set the number of grey levels as 64 which may correspond to a binwidth of 0.47? Please correct me if I am wrong.</p>
<p>Regarding the resampling, I don’t think there is much variation in spacing. It is mostly 3.52mm x 3.52mm x3.27mm.<br>
Even if I don’t set a value for spatial resampling and bin width why I am getting feature values?</p>
<p>Thanks</p>

---

## Post #6 by @JoostJM (2022-01-11 12:30 UTC)

<p>Even if you don’t set a bin width, a default value is applied. If you don’t set a resampling size, no resampling is performed.</p>
<p>If you want a specific number of bins, you can set the binCount to 64. This is not recommended as this imposes a normalization on the ROI, which can remove valuable information. (Consider 2 cases where 1 has a very heterogeneous tumor with a range of 300, and a very homogeneous one with a range of 10. Using a fixed bin count will make both tumors seem more or less equally heterogeneous, as the meaning of a discretized gray value is different between the 2 tumors. In the first case it will likely reflect true difference, whereas in the second it will mostly reflect noise).</p>

---

## Post #7 by @MPhilip (2022-01-11 12:52 UTC)

<p>Thanks very much for your detailed reply.<br>
What would be the default bin width set? Is it 25, as I can read <a href="https://pyradiomics.readthedocs.io/en/latest/customization.html" rel="noopener nofollow ugc">here</a>? The difference between bin count and bin width is something related to absolute and relative quantisation?<br>
In which scenario a bin width of 64 can be applied? Does it depend on the feature values obtained as you suggested before?<br>
So it is advised to specify bin width than bin count for CT/PT images.</p>
<p>Than you</p>

---

## Post #8 by @MPhilip (2022-01-12 15:09 UTC)

<p>Hi <a class="mention" href="/u/joostjm">@JoostJM</a><br>
I was finding the first order range of my entire data set to find the ideal bin width. But with a particular patient data, I have the following values of the first order.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9140feac69517ff57dd83f071f2f60dcb91b25f2.jpeg" data-download-href="/uploads/short-url/kIYu0nRhNz2ycEcDgmcsZ38bSkW.jpeg?dl=1" title="Merged_document" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9140feac69517ff57dd83f071f2f60dcb91b25f2_2_531x500.jpeg" alt="Merged_document" data-base62-sha1="kIYu0nRhNz2ycEcDgmcsZ38bSkW" width="531" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9140feac69517ff57dd83f071f2f60dcb91b25f2_2_531x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9140feac69517ff57dd83f071f2f60dcb91b25f2_2_796x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9140feac69517ff57dd83f071f2f60dcb91b25f2_2_1062x1000.jpeg 2x" data-dominant-color="F8F8F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Merged_document</span><span class="informations">1908×1794 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Most of the first-order feature values are zero.<br>
The Dicom tree appears as below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48a7263c8782d15d831f434dba223d9dc6f616a5.jpeg" data-download-href="/uploads/short-url/amIuBSWlNEOl8PNbX0CPiqrTaEl.jpeg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a7263c8782d15d831f434dba223d9dc6f616a5_2_594x500.jpeg" alt="Capture2" data-base62-sha1="amIuBSWlNEOl8PNbX0CPiqrTaEl" width="594" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a7263c8782d15d831f434dba223d9dc6f616a5_2_594x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48a7263c8782d15d831f434dba223d9dc6f616a5_2_891x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48a7263c8782d15d831f434dba223d9dc6f616a5.jpeg 2x" data-dominant-color="E4EDF4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1054×886 81.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
The loaded image is as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5f19f988cacf6683fb36100840e585769c1d3d9.jpeg" data-download-href="/uploads/short-url/uwDnnbkMWYlkV9xa3qGnYpmTE0N.jpeg?dl=1" title="capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f19f988cacf6683fb36100840e585769c1d3d9_2_690x340.jpeg" alt="capture1" data-base62-sha1="uwDnnbkMWYlkV9xa3qGnYpmTE0N" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f19f988cacf6683fb36100840e585769c1d3d9_2_690x340.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f19f988cacf6683fb36100840e585769c1d3d9_2_1035x510.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d5f19f988cacf6683fb36100840e585769c1d3d9_2_1380x680.jpeg 2x" data-dominant-color="C3C3C3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture1</span><span class="informations">1918×946 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hope you would be able to help with your suggestions.</p>
<p>Thanks</p>

---

## Post #9 by @JoostJM (2022-01-18 12:37 UTC)

<p>In this case, the image you use for feature extraction only contains 0’s, so of course no valid binwidth can be computed. This is also visible in your screenshot, the image is completely white…</p>

---

## Post #10 by @MPhilip (2022-01-18 12:56 UTC)

<p>Thank you very much for your reply. But the provider of this dataset on The Cancer Imaging Archive used this image for feature extraction using Matlab package(developed by the same provider) and it worked.<br>
I was trying to make it work on 3Dslicer, but I am not sure why it behaves differently.<br>
Would you mind giving me a suggestion for binwidth if my first order range varies between 1 and 30?</p>
<p>Many thanks</p>

---

## Post #11 by @JoostJM (2022-01-21 09:49 UTC)

<p>I cannot provide a suggestion of binwidth as I mentioned above. The image you are using is invalid and would compute wrong answers with the matlab package too. As you can see in the visualization in Slicer and the diagnostics feature “diagnostics_image-original_minimum” and “diagnostics_image-original_maximum”, this <strong>image</strong> contains only 0’s. I.e. there is no information in this image. Maybe you have selected the wrong image as input or something failed in a conversion step?</p>
<p>A very important step of any radiomics or AI workflow is the validation of your dataset. Garbage in = garbage out</p>

---

## Post #12 by @JoostJM (2022-01-21 09:51 UTC)

<p>I’m noticing your image is a SUV image. Those usually have very small values and require a floating point datatype. Is it possible you force a conversion to an integer datatype somewhere? That would be a possible cause for the error in your image.</p>

---

## Post #13 by @MPhilip (2022-01-21 12:16 UTC)

<p>Hi <a class="mention" href="/u/joostjm">@JoostJM</a><br>
Thanks for your reply in detail.</p>
<p>I had asked for a suggestion of binwidth based on the first-order range I could find for other patient images (not for the image given above which contains only 0’s, and as you said the SUV values for these kind of images are small )</p>
<p>Is the binwidth of 0.2 is appropriate to accommodate first-order range varying between 1 and 30?</p>
<p>Thank you</p>

---

## Post #14 by @JoostJM (2022-01-21 13:52 UTC)

<p>Sounds appropriate yes</p>

---

## Post #15 by @MPhilip (2022-01-27 16:36 UTC)

<p>Hi <a class="mention" href="/u/joostjm">@JoostJM</a></p>
<p>I was extracting features using the image which I have previously shared (HN-CHUS-030) using LIFEx <a href="https://www.lifexsoft.org/" rel="noopener nofollow ugc">https://www.lifexsoft.org/</a> and the series description( LOR-RAMLA and PTRTstruct)and the loaded image appears as given below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f091a88937f00e0855f698df218da6f264a4d515.png" data-download-href="/uploads/short-url/ykaFcdPaxQjuDqsUb3pgabVDdXv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f091a88937f00e0855f698df218da6f264a4d515_2_690x262.png" alt="image" data-base62-sha1="ykaFcdPaxQjuDqsUb3pgabVDdXv" width="690" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f091a88937f00e0855f698df218da6f264a4d515_2_690x262.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f091a88937f00e0855f698df218da6f264a4d515.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f091a88937f00e0855f698df218da6f264a4d515.png 2x" data-dominant-color="EBECEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">919×350 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a93870dd26462ecbea27a604fcce45938a40fb4a.jpeg" data-download-href="/uploads/short-url/o8ZCdUoAIBnNkp3BdDIK1GXuw0a.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a93870dd26462ecbea27a604fcce45938a40fb4a_2_690x325.jpeg" alt="image" data-base62-sha1="o8ZCdUoAIBnNkp3BdDIK1GXuw0a" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a93870dd26462ecbea27a604fcce45938a40fb4a_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a93870dd26462ecbea27a604fcce45938a40fb4a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a93870dd26462ecbea27a604fcce45938a40fb4a.jpeg 2x" data-dominant-color="E8E8E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">750×354 45.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I could calculate the features including PET SUV parameters using LIFEx.<br>
But the same image with the same series loaded to 3D slicer appears differently and I am not able to get the PET SUV parameter values as in the images shown below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3adc0463a992515fb091eca2e7c8769a8dc60499.png" data-download-href="/uploads/short-url/8oH4Pf3W58Y2Su6fffQxswtlbIt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3adc0463a992515fb091eca2e7c8769a8dc60499_2_690x410.png" alt="image" data-base62-sha1="8oH4Pf3W58Y2Su6fffQxswtlbIt" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3adc0463a992515fb091eca2e7c8769a8dc60499_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3adc0463a992515fb091eca2e7c8769a8dc60499.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3adc0463a992515fb091eca2e7c8769a8dc60499.png 2x" data-dominant-color="EEF3F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">900×535 60.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/733a04f6cfaa6b644bdc3e503886c6957b97c2bb.png" data-download-href="/uploads/short-url/grldkK4x8YyMJkd6VRpwhD522xl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/733a04f6cfaa6b644bdc3e503886c6957b97c2bb_2_690x297.png" alt="image" data-base62-sha1="grldkK4x8YyMJkd6VRpwhD522xl" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/733a04f6cfaa6b644bdc3e503886c6957b97c2bb_2_690x297.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/733a04f6cfaa6b644bdc3e503886c6957b97c2bb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/733a04f6cfaa6b644bdc3e503886c6957b97c2bb.png 2x" data-dominant-color="979396"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">866×374 83.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am not sure why it is this way and not sure whether I am doing everything correctly.</p>
<p>I am not trying to compare 3Dslicer with LIFEx but not clear why there are differences. I did explored these images using MATLAB radiomics package. That also gave me results.</p>
<p>Is there something I need to correct/load before PET statistics calculation on 3Dslicer?</p>
<p>Thank you</p>

---

## Post #16 by @JoostJM (2022-01-28 09:52 UTC)

<p>As far as I can see it looks like in Slicer, you are just loading in the CTAC/NAC data, without computing SUV values. I.e. you are computing the features based on the counts, not the SUV. I believe there are module in Slicer that can help you convert this.</p>
<p>I don’t know if LifeX does the SUV calculation automatically or not.</p>

---

## Post #17 by @MPhilip (2022-01-28 12:25 UTC)

<p>Thanks for your reply.<br>
I have these extensions already installed and it works fine with other patient images.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71758cbe52cb1702aa6f812ebaa3b885388e6e06.png" data-download-href="/uploads/short-url/gbHNOgWvzujRIwbNmcUKIDBnoNg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71758cbe52cb1702aa6f812ebaa3b885388e6e06_2_690x56.png" alt="image" data-base62-sha1="gbHNOgWvzujRIwbNmcUKIDBnoNg" width="690" height="56" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71758cbe52cb1702aa6f812ebaa3b885388e6e06_2_690x56.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71758cbe52cb1702aa6f812ebaa3b885388e6e06_2_1035x84.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71758cbe52cb1702aa6f812ebaa3b885388e6e06_2_1380x112.png 2x" data-dominant-color="ECEBF6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1518×124 35.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am not quite sure what is to be done.<br>
If you have any suggestions, please share.</p>
<p>Thanks</p>

---
