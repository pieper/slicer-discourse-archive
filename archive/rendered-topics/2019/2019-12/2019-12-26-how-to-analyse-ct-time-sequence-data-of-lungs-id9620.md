---
topic_id: 9620
title: "How To Analyse Ct Time Sequence Data Of Lungs"
date: 2019-12-26
url: https://discourse.slicer.org/t/9620
---

# How to analyse CT time sequence data of lungs?

**Topic ID**: 9620
**Date**: 2019-12-26
**URL**: https://discourse.slicer.org/t/how-to-analyse-ct-time-sequence-data-of-lungs/9620

---

## Post #1 by @Shahid_Khan (2019-12-26 10:10 UTC)

<p>Hey, I am Shahid Khan and I am very new to 3-d slicer(started a week ago). I want to analyze CT data of lung cancer and want to generate Ktrans and Ve maps. I have data in Scalar volume but to use T1 mapping I need it in Multivolume mode? I am not able to understand this. Can anyone help me with this?</p>

---

## Post #2 by @pieper (2019-12-26 14:57 UTC)

<p>Hi -</p>
<p>If you are in Advanced mode (click the checkbox) then you will be given a list of different load options (scalar, multivolume, etc) for whatever loaders can handle your data.  Just check the option that corresponds to how you want the data to load.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/Modules/DICOM</a></p>

---

## Post #5 by @Shahid_Khan (2019-12-27 04:45 UTC)

<p>I did this step. It is showing only in scalar volume but to generate Ktrans maps I need it in multivolume then only I can generate them using T1 mapping extension. Please help.</p>

---

## Post #6 by @lassoan (2019-12-27 14:20 UTC)

<p>Are you sure you exported 4D CT data set (3D time sequence)? Can you attach a screenshot of your DICOM browser (scratch out patient name, ID, dates) so that we can see what kind of series are listed?</p>
<p>Also, try loading the data set using latest preview release of Slicer.</p>

---

## Post #7 by @Shahid_Khan (2019-12-28 03:57 UTC)

<p>I am not sure of that. I downloaded data from TCIA (QIN LUNG CT)<br>
Link to data-<a href="https://wiki.cancerimagingarchive.net/display/Public/QIN+LUNG+CT" class="inline-onebox" rel="noopener nofollow ugc">QIN LUNG CT - The Cancer Imaging Archive (TCIA) Public Access - Cancer Imaging Archive Wiki</a></p>
<p>Hers is the screenshot of the browser.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e863bd55aa9482a30f22de880c6ada7721248c9.png" data-download-href="/uploads/short-url/kkPovgLJIGT7PN30SEThtXKWRLz.png?dl=1" title="Screenshot (119)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e863bd55aa9482a30f22de880c6ada7721248c9_2_690x387.png" alt="Screenshot (119)" data-base62-sha1="kkPovgLJIGT7PN30SEThtXKWRLz" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e863bd55aa9482a30f22de880c6ada7721248c9_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e863bd55aa9482a30f22de880c6ada7721248c9_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e863bd55aa9482a30f22de880c6ada7721248c9.png 2x" data-dominant-color="CACFD5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (119)</span><span class="informations">1366×768 97.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2019-12-28 05:43 UTC)

<aside class="quote no-group" data-username="Shahid_Khan" data-post="7" data-topic="9620">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahid_khan/48/5459_2.png" class="avatar"> Shahid_Khan:</div>
<blockquote>
<p>I downloaded data from TCIA (QIN LUNG CT)</p>
</blockquote>
</aside>
<p>All CTs in TCIA “QIN LUNG CT” collection are simple 3D volumes, they are not time sequences. You can find 4D CTs in <a href="https://wiki.cancerimagingarchive.net/display/Public/4D-Lung">“4D -Lung” collection</a>.</p>

---

## Post #9 by @Shahid_Khan (2019-12-28 06:42 UTC)

<p>Thank you Dr. Lasso. I will download this data and try it with this.<br>
There is one more issue- Even if I get the data you mentioned in multi-volume node, I still won’t be able to generate permeability (Ktrans) and porosity (Ve) maps of the tumour using PK modeling and T1 mapping as they are compatible only with DCE-MRI data.<br>
How to generate the above-mentioned maps using the data which you mentioned?</p>

---
