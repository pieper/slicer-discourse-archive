# Problem with SlicerRT in Slicer version 4.11.20210226 r29738 / 7a593c8

**Topic ID**: 20510
**Date**: 2021-11-07
**URL**: https://discourse.slicer.org/t/problem-with-slicerrt-in-slicer-version-4-11-20210226-r29738-7a593c8/20510

---

## Post #1 by @shahrokh (2021-11-07 11:41 UTC)

<p><strong>Hello Dear Developers and Users</strong></p>
<p>I can load Structure (RTStructure), Plan (RTPlan) and CT images in dicom format with SlicerRT in Slicer version: 4.10.2 r28257 completely.</p>
<p>At now, I want to load these data in SlicerRT with Slicer version <strong>4.11.20210226 r29738 / 7a593c8</strong>. At this version, I can not the load of RTPlan. I get this message: <strong>Could not load: 4: RTPlan Beamsetup1CTDB as a RT</strong>.<br>
I tick the option of <em>Advanced</em> in <strong>DICOM</strong> module and then click on Examine as seen in the following scrennshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/772f19a5bb345973b5940bcd948f4e1fa5f7ad0e.png" data-download-href="/uploads/short-url/h0lJiFQ6Ze0jVyf9HQaNT1eyvro.png?dl=1" title="RT2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/772f19a5bb345973b5940bcd948f4e1fa5f7ad0e_2_690x388.png" alt="RT2" data-base62-sha1="h0lJiFQ6Ze0jVyf9HQaNT1eyvro" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/772f19a5bb345973b5940bcd948f4e1fa5f7ad0e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/772f19a5bb345973b5940bcd948f4e1fa5f7ad0e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/772f19a5bb345973b5940bcd948f4e1fa5f7ad0e_2_1380x776.png 2x" data-dominant-color="E2E6E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">RT2</span><span class="informations">1920×1080 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Please guide me to solve it.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2021-11-07 17:19 UTC)

<p>What kind of RT plan is this (external beam, HDR brachytherapy, …)? Does it work better in a recent Slicer Preview Release?</p>

---

## Post #3 by @shahrokh (2021-11-08 09:48 UTC)

<p>Thanks a lot for your guidance.</p>
<p>In response to your question about the kind of RT plan, I work with <strong>RT plan of external beam</strong>.<br>
As you mentioned, I download the last version of 3Dslicer, Preview Release (<strong>4.13.0-2021-11-05 r30381 / f46c474</strong>). Then, I install SlicerRT without any problem.</p>
<p>Unfortunately, I still have the same problem and I can not load RTPlan. I must mentioned that at this version of 3DSlicer, I can load RTStructure.<br>
As mentioned in the previous message (7 Nov), I can load completely RTStructure, RTPlan and CT in 3DSlicer version <strong>4.10.2 r28257</strong>, but at now I want to work with new version of 3DSlicer.</p>
<p>Please guide me.<br>
Best Regards<br>
Shahrokh.</p>

---

## Post #4 by @lassoan (2021-11-08 13:20 UTC)

<p>RT plan loading has hugely improved since Slicer-4.10 and external beam plans are fully supported, so please submit a bug report for this to SlicerRT repository and copy the link here. Provide an anonymized (or phantom or animal) study with an RT plan that you have trouble loading.</p>

---

## Post #5 by @shahrokh (2021-11-09 06:29 UTC)

<p>Dear Andras</p>
<p>Thanks a lot for your guidance. You told me that I report a bug report to <strong>SlicerRT repository</strong>. Then I submit my problems in SlicerRT in github with this <a href="https://github.com/SlicerRt/SlicerRT/issues/201" rel="noopener nofollow ugc">link</a>. I hope it is where you said it was.</p>
<p>Also, anonymized data that I have trouble loading (including as RTDOSE, RTSTRUCT, CT (74 images) and RTPLAN) can be downloaded via this <a href="https://www.dropbox.com/sh/e1d0yc24ghptslk/AADZyW550Q6geYbDuRn3hAMna?dl=0" rel="noopener nofollow ugc">link</a>.</p>
<p>At this anonymized data, as mentioned above I can load RTDOSE, RTSTRUCT, CT and <strong>can not load RTPLAN</strong> .</p>
<p>Best regards.<br>
Shharokh</p>

---

## Post #6 by @Mik (2021-11-09 20:20 UTC)

<p>I have made a <a href="https://github.com/SlicerRt/SlicerRT/pull/202" rel="noopener nofollow ugc">PR</a> to fix the RTPlan loading problem.</p>

---

## Post #7 by @issakomi (2021-11-09 21:22 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="5" data-topic="20510">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>anonymized data that I have trouble loading</p>
</blockquote>
</aside>
<p>i see that rather old Aliza was used to de-identify data sets, i would recommend to use newer version, there are many important improvement in de-identify, <a href="https://github.com/AlizaMedicalImaging/AlizaMS/releases" rel="noopener nofollow ugc">free</a> version is OK. Select the folder containing the study (all original data sets). The integrity of data sets will be maintained, applicable UIDs, IDs, PNs will be mapped consistently to randomly generated values across all series. If series are de-identified one by one such complicated study as RT will not work proper.</p>

---

## Post #8 by @shahrokh (2021-11-14 06:06 UTC)

<p>Dear issakomi<br>
Thank you very much for your explanation. Aliza is a very good software.</p>

---

## Post #9 by @shahrokh (2021-11-14 06:07 UTC)

<p>Thanks a lot for your guidance. I must mentioned that I try last preview version of 3DSlicer in <strong>Windows</strong> . I can import RT data (RTPLAN, RTSTRUCT, RTDOSE and CT) withount any problems in this version of 3DSlicer ; but my problem with loading RTPLAN in version 4.13.0-2021-11-05 r30381 / f46c474 of 3DSlicer in <strong>Ubuntu (18.04)</strong> is still unresolved.</p>
<p>However I found a trick to do this. I must mentioned that I want to work with <strong>DRR Image Computataion</strong> module. Apparently this module (with this GUI) is available in the latest version of 3DSlicer. I did not see this module in SlicerRT installed in the version 4.10.2 r28257 of 3DSlicer.</p>
<p>Before implementing this GUI, I compute DRR images from the Plastimatch command line. Thanks to the developers of this GUI.</p>
<p>My trick:<br>
As I mentioned I can load data exported from TPS (CT, RTPLAN, RTSTRUCT and RTDOSE) without any problems in version 4.10.2 r28257. Without doing anything, I save these in the format of <strong>Medical Reality Bundle</strong> . Then import the resulting file via <strong>Add Data</strong> in the version 4.13.0-2021-11-05 r30381 / f46c474 of 3DSlicer. So, by applying some transformations, I am able to import RT data and compute DRR.</p>
<p>Best regards.</p>
<p>Shahrokh.</p>

---

## Post #10 by @lassoan (2021-11-14 20:13 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="9" data-topic="20510">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>I can import RT data (RTPLAN, RTSTRUCT, RTDOSE and CT) withount any problems in this version of 3DSlicer ; but my problem with loading RTPLAN in version 4.13.0-2021-11-05 r30381 / f46c474 of 3DSlicer in <strong>Ubuntu (18.04)</strong> is still unresolved.</p>
</blockquote>
</aside>
<p>The fix for plan loading was not available in 2011-11-05 version. It was fixed on November 10.</p>

---

## Post #11 by @shahrokh (2021-11-16 04:05 UTC)

<p>Thank a lot. At now, I can load all data taken from TPS in 3DSlicer without any problems.<br>
Best regards.<br>
Shahrokh</p>

---

## Post #12 by @shahrokh (2021-11-16 06:14 UTC)

<p>I saw new modules added to SlicerRT. I would like to sincerely congratulate the development team of this module. I really enjoy the modules/features that 3DSlicer has in general.<br>
I also sincerely thank the development team and programmers who provide excellent support to users.</p>
<p>Wishing you good health and good luck.<br>
Shahrokh</p>

---

## Post #13 by @lassoan (2021-11-16 06:19 UTC)

<p>Thank you for the kind words. It would be great if you could write a few sentences (even just copy-paste what you wrote above) into the <a href="https://discourse.slicer.org/c/community/success-stories/29" class="inline-onebox">Success stories - 3D Slicer Community</a> category about your experiences with Slicer.</p>

---

## Post #14 by @shahrokh (2021-11-16 06:36 UTC)

<p>Dear Andras<br>
I will definitely do that.<br>
I have been working with 3DSlicer since about 2017. I really have fond memories of being with 3DSlicer and have received great tips from you and your colleagues.<br>
I am preparing a text containing my wonderful and sweet experiences.<br>
Best regards.<br>
Shahrokh</p>

---
