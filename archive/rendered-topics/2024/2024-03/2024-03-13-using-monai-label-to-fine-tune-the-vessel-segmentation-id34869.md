# Using MONAI label to fine tune the vessel segmentation

**Topic ID**: 34869
**Date**: 2024-03-13
**URL**: https://discourse.slicer.org/t/using-monai-label-to-fine-tune-the-vessel-segmentation/34869

---

## Post #1 by @klc (2024-03-13 16:35 UTC)

<p>Hi, I have acheived robust and satisfactory segmentation result when using lungCTsegmenter before.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4e0da0b93de6f3ee8d6af42cc0dcdceffc82fc5.jpeg" alt="image" data-base62-sha1="yWifdocOKokLeSPY2BpxVyb2cip" width="549" height="485"></p>
<p>However, if i use other samples(LIDC-IDRI dataset), most of the results have lung/vessel leaks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/929651905bdbb6a62bac9a2c572fb8ca1061f3ae.jpeg" data-download-href="/uploads/short-url/kULLxEGek4kQni89dZCupTiHZHE.jpeg?dl=1" title="WhatsApp Image 2024-03-13 at 23.28.56_0857f222" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/929651905bdbb6a62bac9a2c572fb8ca1061f3ae_2_568x499.jpeg" alt="WhatsApp Image 2024-03-13 at 23.28.56_0857f222" data-base62-sha1="kULLxEGek4kQni89dZCupTiHZHE" width="568" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/929651905bdbb6a62bac9a2c572fb8ca1061f3ae_2_568x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/929651905bdbb6a62bac9a2c572fb8ca1061f3ae.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/929651905bdbb6a62bac9a2c572fb8ca1061f3ae.jpeg 2x" data-dominant-color="8C8AA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2024-03-13 at 23.28.56_0857f222</span><span class="informations">751×661 89.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7730cea4c95a27e8e88240af9589a38d0342c4de.jpeg" data-download-href="/uploads/short-url/h0po3cTIUBXUf5aeRMqnGMtmEFM.jpeg?dl=1" title="WhatsApp Image 2024-03-13 at 23.29.21_1eecf52d" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7730cea4c95a27e8e88240af9589a38d0342c4de_2_580x500.jpeg" alt="WhatsApp Image 2024-03-13 at 23.29.21_1eecf52d" data-base62-sha1="h0po3cTIUBXUf5aeRMqnGMtmEFM" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/7730cea4c95a27e8e88240af9589a38d0342c4de_2_580x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7730cea4c95a27e8e88240af9589a38d0342c4de.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/7730cea4c95a27e8e88240af9589a38d0342c4de.jpeg 2x" data-dominant-color="9097A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2024-03-13 at 23.29.21_1eecf52d</span><span class="informations">633×545 65.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Should I use MONAI label to finetune the vessel segmentation part, or this is not a good use case? Since I watch this demo:</p><div class="youtube-onebox lazy-video-container" data-video-id="wtiEe_jiUzg" data-video-title="MONAI Label Workshop - Project Week 37" data-video-start-time="5531s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=wtiEe_jiUzg&amp;t=5531s" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/wtiEe_jiUzg/maxresdefault.jpg" title="MONAI Label Workshop - Project Week 37" width="" height="">
  </a>
</div>
<p>
(1:35:27) and the segmentation results is not as good as the segmentation provided by lungCTsegmenter.</p>
<p>Can you give me a little bit suggestions on how should I fine tune the vessel segmentations? (e.g. the modelzoo from MONAI label contains many useful models, is there a model that I can utilize to produce accurate segmentations)</p>
<p>Thank you very mcuh</p>

---

## Post #2 by @rbumm (2024-03-13 17:01 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> , <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/eserval">@Eserval</a> and I are in the process of training a MONAI Auto3DSeg model for better vessel segmentation and simultaneous airway segmentation. Please try the MONAI Auto3DSeg extension and use the lungs 2.0.1 model for a first preview. Pulmonary artery and airway segmentation already work quite well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1622b1830437136a0278801e920d1a803df29733.jpeg" data-download-href="/uploads/short-url/39OPKjfVGWxsG96njxSE9IEkF3R.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1622b1830437136a0278801e920d1a803df29733_2_554x500.jpeg" alt="image" data-base62-sha1="39OPKjfVGWxsG96njxSE9IEkF3R" width="554" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1622b1830437136a0278801e920d1a803df29733_2_554x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1622b1830437136a0278801e920d1a803df29733.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1622b1830437136a0278801e920d1a803df29733.jpeg 2x" data-dominant-color="87778A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">617×556 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(CTChest sample volume)</p>
<p>If you cannot find the lungs 2.0.1 model in the extension within Slicer 5.6.1, please update the extension tomorrow and try again or use 3D Slicer 5.7.0 preview.</p>

---

## Post #3 by @klc (2024-03-13 17:29 UTC)

<p>Thank you for your prompt response. It is great to see such beautiful results.</p>
<p>May I know is it ok to have different slicer versions on the same machine in the same account? (e.g. 5.4.0 and 5.6.1)<br>
" * Slicer is generally simple to install on all platforms. It is possible to install multiple versions of the application on the same user account and they will not interfere with each other. If you run into mysterious problems with your installation you can try deleting the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location" rel="noopener nofollow ugc">application settings files</a>."</p>

---

## Post #4 by @klc (2024-03-21 17:22 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5624c0e91cc7aa602192720adb01a9f4cf2286c.png" data-download-href="/uploads/short-url/wJdWmkmXkBo49bZPABDrA3Ln7go.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5624c0e91cc7aa602192720adb01a9f4cf2286c_2_474x500.png" alt="image" data-base62-sha1="wJdWmkmXkBo49bZPABDrA3Ln7go" width="474" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5624c0e91cc7aa602192720adb01a9f4cf2286c_2_474x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5624c0e91cc7aa602192720adb01a9f4cf2286c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5624c0e91cc7aa602192720adb01a9f4cf2286c.png 2x" data-dominant-color="8E7499"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">682×718 245 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>HI professor, thank you for your recommendation. The attached pictures are the combination of applying lung 2.0.1 in MONAI Auto 3D Seg and MONAI model zoo’s lung nodule detection. The detection ROI-2 is correctly detected and markuped. But inside the box, it is blood vessel instead of lesion. May I know is there any possible way to make it at least not red and labelled it as a “lesion” in the segmentation ?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e03f15182f5d9219797b7365ce8d762087aa73cc.png" alt="image" data-base62-sha1="vZM6CxoQC3cFqYNfEcBXgf7g5K4" width="199" height="217"></p>
<p>FYI, the detection is very accurate in the CT scan and can outline the complete structure of the lesion but I dont know how to convert this to a segmentation. The right CT scan is labelled by radiologists whereas the left is labelled by MONAI label.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b561328b943cfadedead10955cba821c8bf8841.jpeg" data-download-href="/uploads/short-url/1ChFkFZCgOcU8JuKA9xI9DX9fWN.jpeg?dl=1" title="WhatsApp Image 2024-03-07 at 00.16.53_1b18bef4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b561328b943cfadedead10955cba821c8bf8841_2_690x355.jpeg" alt="WhatsApp Image 2024-03-07 at 00.16.53_1b18bef4" data-base62-sha1="1ChFkFZCgOcU8JuKA9xI9DX9fWN" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b561328b943cfadedead10955cba821c8bf8841_2_690x355.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b561328b943cfadedead10955cba821c8bf8841_2_1035x532.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b561328b943cfadedead10955cba821c8bf8841.jpeg 2x" data-dominant-color="A1A1A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2024-03-07 at 00.16.53_1b18bef4</span><span class="informations">1082×558 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you</p>

---

## Post #5 by @rbumm (2024-03-26 18:53 UTC)

<p>Could you please switch to “Data” and post the content of the resulting screen ?</p>

---

## Post #6 by @klc (2024-03-26 19:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed407530a37ffc5f4750253d704dab83c024901c.jpeg" data-download-href="/uploads/short-url/xQPg9TAl0OiAaJM6WJPhzKR7iWM.jpeg?dl=1" title="Screenshot 2024-03-27 at 3.01.36 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed407530a37ffc5f4750253d704dab83c024901c_2_690x315.jpeg" alt="Screenshot 2024-03-27 at 3.01.36 AM" data-base62-sha1="xQPg9TAl0OiAaJM6WJPhzKR7iWM" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed407530a37ffc5f4750253d704dab83c024901c_2_690x315.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed407530a37ffc5f4750253d704dab83c024901c_2_1035x472.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed407530a37ffc5f4750253d704dab83c024901c_2_1380x630.jpeg 2x" data-dominant-color="AEA4C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-03-27 at 3.01.36 AM</span><span class="informations">1920×879 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a6cc174a18501835b29b5aa153424dc723b4032.png" data-download-href="/uploads/short-url/jKyTJo5bbtSF3tkEIOq7SkPO7F8.png?dl=1" title="Screenshot 2024-03-27 at 3.01.47 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a6cc174a18501835b29b5aa153424dc723b4032_2_458x500.png" alt="Screenshot 2024-03-27 at 3.01.47 AM" data-base62-sha1="jKyTJo5bbtSF3tkEIOq7SkPO7F8" width="458" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a6cc174a18501835b29b5aa153424dc723b4032_2_458x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a6cc174a18501835b29b5aa153424dc723b4032_2_687x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a6cc174a18501835b29b5aa153424dc723b4032.png 2x" data-dominant-color="EDEFF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-03-27 at 3.01.47 AM</span><span class="informations">766×836 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Sure, thanks for looking into this</p>

---

## Post #7 by @rbumm (2024-03-26 20:47 UTC)

<p>Please right click Detection ROI-2 and "Rename " to anything you like.<br>
Please click the color to choose a different color for the box.<br>
You seem to get ROI for suspected tumor locations . The tumor should be within this ROI. If you need to segment it out, you could go to “Segment editor”, disable vilibility of “blood vessels”, then use “Local threshold” where you could CTRL left click into the nodule and segment it like it is <a href="https://www.youtube.com/watch?v=NmG16cSwUHg" rel="noopener nofollow ugc">shown here</a>.</p>

---
