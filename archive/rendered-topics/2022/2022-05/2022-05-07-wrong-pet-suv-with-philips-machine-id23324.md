---
topic_id: 23324
title: "Wrong Pet Suv With Philips Machine"
date: 2022-05-07
url: https://discourse.slicer.org/t/23324
---

# Wrong PET SUV with Philips machine

**Topic ID**: 23324
**Date**: 2022-05-07
**URL**: https://discourse.slicer.org/t/wrong-pet-suv-with-philips-machine/23324

---

## Post #1 by @tristan421 (2022-05-07 22:27 UTC)

<p>Hello.</p>
<p>There seems to be an issus with the way PETDICOM module operate on PET images taken from a a phillips machine.</p>
<p>The computed SUV are way too low. By looking into the hood, it seems the right way to compute SUV values in this case would be to multiplicate each pixels by the value inside the private DICOM tag 7053|1000. But I guess the PETDICOM extension doesn’t take that into account ?</p>
<p>Does anyone have experience with this ?</p>
<p>Thank you all for your good work</p>

---

## Post #2 by @tristan421 (2022-05-07 22:54 UTC)

<p>yeah, I can more or less confirm that the PETDICOM module compute a wrong (but coherent) suv normalisation factor when feeded with phillips images.</p>
<p>The way to do it is to load the unweighted scalar volume and multiply everything by the value found in the private dicom tag 7053 | 1000. By doing this i find coherent SUV value for the liver.</p>
<p>Maybe it could be added as an option inside the module ?</p>

---

## Post #3 by @pieper (2022-05-09 01:15 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">   It’s very possible that Philips encodes PET differently than the examples used in developing the extension.  If you could file an issue (either in the Slicer github, or if you used one of the PET extensions, then in the appropriate repository), and ideally include an anonymous sample study for development and testing that would be great.  Even better, if you are a coder you could probably easily add a branch to handle the special cases for this kind of acquisition.</p>
<p>As you probably know, vendors often have very specific and non-standard ways of encoding data.  In this case, the group (7053) is an odd number, meaning this is a so-called “private tag” that is not part of the dicom standard and needs to be handled as a custom-coded special case.</p>

---

## Post #4 by @issakomi (2022-05-09 01:53 UTC)

<p>It is known schema, the Units (0x0054,0x1001) should be CNTS, BTW. <em>SUVbwScaleFactor</em> is in fact already calculated and saved in that Philips private tag and, as correctly mentioned above, SUV should be calculated:<br>
<code>SUVbw = ((stored pixel value in Pixel Data (0x7FE0,0x0010) * Rescale Slope (0x0028,0x1053) + Rescale Intercept (0x0028,0x1052) ) * SUVbwScaleFactor</code></p>
<p>S. <a href="https://qibawiki.rsna.org/images/8/86/SUV_vendorneutral_pseudocode_20180626_DAC.pdf" rel="noopener nofollow ugc">Vendor-neutral pseudo-code for SUV calculation</a> from <a href="https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)" rel="noopener nofollow ugc"> QIBA FDG-PET/CT Standardized Uptake Value (SUV) Technical Subcommittee</a> .</p>
<p>IMHO, it is mentioned somewhere in comment in PETDICOM code.</p>

---

## Post #5 by @issakomi (2022-05-09 09:38 UTC)

<p>Readme of <a href="https://github.com/QIICR/Slicer-PETDICOMExtension" rel="noopener nofollow ugc">Slicer-PETDICOMExtension</a> explains<br>
<code>The PET DICOM Extension provides tools to import PET Standardized Uptake Value (SUV) images from DICOM into 3D Slicer. SUV computation is based on the vendor-neutral "happy path only" calculation described on the Quantitative Imaging Biomarkers Alliance (QIBA) wiki page Standardized Uptake Value (SUV)</code></p>
<p>“happy path only”</p>

---

## Post #6 by @Farkhat_Bayembayev (2022-08-25 08:48 UTC)

<p>Dear Tristan. I’m a NM doctor from Qazaqstan using 3D slicer to segment and calculate PET scans. All patients scanned with Phillips machines and in some patients SUV calculated incorrect. Some patients have additional files like on image.</p>
<p>Can you please help me to manage it?<br>
<a>Uploading: For 3D -2.jpg…</a></p>
<p>My email: <a href="mailto:farkhat.kz@gmail.com">farkhat.kz@gmail.com</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76c81382bd6e0cb3c6fb43f49e41b0244490c338.jpeg" data-download-href="/uploads/short-url/gWN0aR00QF5EzDcuoYjKuSpciJq.jpeg?dl=1" title="For 3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76c81382bd6e0cb3c6fb43f49e41b0244490c338_2_690x249.jpeg" alt="For 3D" data-base62-sha1="gWN0aR00QF5EzDcuoYjKuSpciJq" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76c81382bd6e0cb3c6fb43f49e41b0244490c338_2_690x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76c81382bd6e0cb3c6fb43f49e41b0244490c338_2_1035x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76c81382bd6e0cb3c6fb43f49e41b0244490c338_2_1380x498.jpeg 2x" data-dominant-color="3D4247"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">For 3D</span><span class="informations">1906×690 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/616285e07f22bb1d7f33b0772c2f9bd73e11e2b5.jpeg" data-download-href="/uploads/short-url/dTvoK7vzKQ6xicJigtwpTbxeMPr.jpeg?dl=1" title="For 3D -2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/616285e07f22bb1d7f33b0772c2f9bd73e11e2b5_2_690x185.jpeg" alt="For 3D -2" data-base62-sha1="dTvoK7vzKQ6xicJigtwpTbxeMPr" width="690" height="185" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/616285e07f22bb1d7f33b0772c2f9bd73e11e2b5_2_690x185.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/616285e07f22bb1d7f33b0772c2f9bd73e11e2b5_2_1035x277.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/616285e07f22bb1d7f33b0772c2f9bd73e11e2b5_2_1380x370.jpeg 2x" data-dominant-color="3A454E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">For 3D -2</span><span class="informations">1920×516 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @Farkhat_Bayembayev (2022-08-25 08:49 UTC)

<p>Dear Isaakomi.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76c81382bd6e0cb3c6fb43f49e41b0244490c338.jpeg" data-download-href="/uploads/short-url/gWN0aR00QF5EzDcuoYjKuSpciJq.jpeg?dl=1" title="For 3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76c81382bd6e0cb3c6fb43f49e41b0244490c338_2_690x249.jpeg" alt="For 3D" data-base62-sha1="gWN0aR00QF5EzDcuoYjKuSpciJq" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76c81382bd6e0cb3c6fb43f49e41b0244490c338_2_690x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76c81382bd6e0cb3c6fb43f49e41b0244490c338_2_1035x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76c81382bd6e0cb3c6fb43f49e41b0244490c338_2_1380x498.jpeg 2x" data-dominant-color="3D4247"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">For 3D</span><span class="informations">1906×690 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’m a NM doctor from Qazaqstan using 3D slicer to segment and calculate PET scans. All patients scanned with Phillips machines and in some patients SUV calculated incorrect. Some patients have additional files like in image.</p>
<p>Can you please help me to manage it? In a more or less simple way, since I’m not an IT guy))</p>
<p>My email: <a href="mailto:farkhat.kz@gmail.com">farkhat.kz@gmail.com</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/616285e07f22bb1d7f33b0772c2f9bd73e11e2b5.jpeg" data-download-href="/uploads/short-url/dTvoK7vzKQ6xicJigtwpTbxeMPr.jpeg?dl=1" title="For 3D -2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/616285e07f22bb1d7f33b0772c2f9bd73e11e2b5_2_690x185.jpeg" alt="For 3D -2" data-base62-sha1="dTvoK7vzKQ6xicJigtwpTbxeMPr" width="690" height="185" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/616285e07f22bb1d7f33b0772c2f9bd73e11e2b5_2_690x185.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/616285e07f22bb1d7f33b0772c2f9bd73e11e2b5_2_1035x277.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/616285e07f22bb1d7f33b0772c2f9bd73e11e2b5_2_1380x370.jpeg 2x" data-dominant-color="3A454E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">For 3D -2</span><span class="informations">1920×516 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @AGGDor (2023-04-02 07:41 UTC)

<p>Also have this issue on DICOMs acquired with a Philips scanner and PETDICOMExtension, which is problematic because other modules use the calculated SUV values. Is there a reason that the “<a href="https://qibawiki.rsna.org/images/6/62/SUV_vendorneutral_pseudocode_happypathonly_20180626_DAC.pdf" rel="noopener nofollow ugc">happy path only</a>” SUV calculation option was used? Is it possible to choose the <a href="https://qibawiki.rsna.org/images/8/86/SUV_vendorneutral_pseudocode_20180626_DAC.pdf" rel="noopener nofollow ugc">alternative vendor neutral path</a> which first determines whether Units (0x0054,0x1001) are BQML or CNTS and then performs the appropriate calculation (with or without scale factor)? Alternatively is it possible to introduce an option for SUV calculation technique within the module? Thanks for great tool.</p>

---

## Post #9 by @pieper (2023-04-02 14:23 UTC)

<p>For the reasons described above it’s hard to test on the full spectrum of real-world PET data so the module implements best-efforts for the data and information the developers had at the time.  It would be great for the community to chip in and improve the code to work robustly on a broader range of data.</p>

---

## Post #10 by @AGGDor (2023-04-04 08:28 UTC)

<p>Hi Steve<br>
Very willing to take a crack at it though my coding is pretty shaky. I see the PETDICOMExtension calls SUVFactorCalculator, which I assume runs the happy path SUV calculation and returns the real-world values? I’m not sure that the calculator can be edited in Python? Would be grateful if you or <a class="mention" href="/u/fedorov">@fedorov</a> could advise? Thanks for assistance!</p>

---

## Post #11 by @fedorov (2023-04-04 21:50 UTC)

<p><a class="mention" href="/u/aggdor">@AGGDor</a> I believe that calculator is in C++ here: <a href="https://github.com/QIICR/Slicer-SUVFactorCalculator" class="inline-onebox">GitHub - QIICR/Slicer-SUVFactorCalculator: 3D Slicer CLI module to calculate Standardized Uptake Value conversion factors from DICOM</a>.</p>
<p>I do not know who, if anyone, from the original team is still supporting that extension (it’s been a long while since the grant funding that development finished), by let’s try pinging Christian <a class="mention" href="/u/chribaue">@chribaue</a>.</p>

---
