---
topic_id: 7980
title: "Inconsistency Between Slicer 3 6 And Slicer 4 10 2 In Mhd He"
date: 2019-08-11
url: https://discourse.slicer.org/t/7980
---

# Inconsistency between Slicer 3.6 and Slicer 4.10.2 in mhd header

**Topic ID**: 7980
**Date**: 2019-08-11
**URL**: https://discourse.slicer.org/t/inconsistency-between-slicer-3-6-and-slicer-4-10-2-in-mhd-header/7980

---

## Post #1 by @Xiaogai_Li (2019-08-11 10:40 UTC)

<p>Dear all,</p>
<p>When <strong>open</strong> exactly the same image (hdr + img format), and <strong>save</strong> into <strong>mhd</strong> format using Slicer 3.6 and Slicer 4.10.2 gives different .<strong>mhd</strong> file regarding RAI VS RPI and transformation Matrix as below and attached pic.</p>
<p>Slicer 3: RPI, 1,-1,1 matrix<br>
Slicer 4: RAI, 1,1,1 matrix<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c283282c1f24da957614439300fa77eec5849159.png" data-download-href="/uploads/short-url/rKJDaaQ24dHBgdUI4rW1Gi6s1JL.png?dl=1" title="41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c283282c1f24da957614439300fa77eec5849159_2_690x205.png" alt="41" data-base62-sha1="rKJDaaQ24dHBgdUI4rW1Gi6s1JL" width="690" height="205" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c283282c1f24da957614439300fa77eec5849159_2_690x205.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c283282c1f24da957614439300fa77eec5849159_2_1035x307.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c283282c1f24da957614439300fa77eec5849159.png 2x" data-dominant-color="EDEDEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">41</span><span class="informations">1211×360 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The <strong>paired info above becomes consistent</strong> indeed for the raw data reading order.</p>
<p>But <strong>my confusion</strong> is, when viewing the image, <strong>Slicer 3.6 shows differently than Slicer 4.10.2</strong>.</p>
<p>So my questions are:</p>
<ul>
<li>Why Slicer 3 and Slicer 4 has this difference when saving .mhd? any motivation for the update?</li>
<li>Why exactly the same image shows differently in Slicer 3 and 4?</li>
</ul>
<p>Any advices are highly appreciated! Thank you very much.</p>
<p>Best regards, Xiaogai</p>

---

## Post #2 by @lassoan (2019-08-11 12:20 UTC)

<p>Slicer4 header is compliant to the metaIO standard. Both files encode the same information. Maybe Slicer3 did not read AnatomicalOrientation tag but assumed to be RAI.</p>
<p>We tried to provide backward compatibility (you can read old scene files with new Slicer versions), but no forward compatibility (read scene files saved with older version of Slicer). Since Slicer3 is about 10 years old, it is a wonder that it can still run on a current computer.</p>

---

## Post #3 by @Xiaogai_Li (2019-08-11 13:15 UTC)

<p>Thank you very much for your answer! I understand Slicer 3 is a bit too old, the reason still use it is due to some earlier work done years ago used Slicer 3, and now when using Slicer 4 found the difference.</p>
<p>Have done further test, seems to me that Slicer 4 always save mhd to <strong>AnatomicalOrientation</strong> RAI plus TransformationMatrix Identity, no matter what orientation was. But Slicer 3.6 indeed distinguish. Seems to me Slicer 3.6 is doing more correct things than Slicer 4. I also saved to nhdr format and compared Slicer 3.6 and Slicer 4.10, also seems Slicer 3.6 is more correct. See following capture tested with a image oriented not RAI.</p>
<p>Please correct me if I am wrong. Thanks a lot for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f5a20b83542c6c5416aee6fd8932d1027e3b6fc.png" data-download-href="/uploads/short-url/ks9nkblGhsmo7mK5kGjBAd2Dlww.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f5a20b83542c6c5416aee6fd8932d1027e3b6fc_2_690x439.png" alt="image" data-base62-sha1="ks9nkblGhsmo7mK5kGjBAd2Dlww" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f5a20b83542c6c5416aee6fd8932d1027e3b6fc_2_690x439.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f5a20b83542c6c5416aee6fd8932d1027e3b6fc_2_1035x658.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f5a20b83542c6c5416aee6fd8932d1027e3b6fc.png 2x" data-dominant-color="EDEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1096×698 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2019-08-11 14:43 UTC)

<p>Those nhdr files are describing different geometry (the AP directions are flipped).  I see from your original post that you loaded these from Analyze format (.img and .hdr).  Unfortunately Analyze format has well documented ambiguity about orientation and has mostly fallen out of use in favor of NIfTI or NRRD.</p>
<p>Probably the ITK code Slicer uses to read Analyze has been debugged over the years to better match the most common conventions, but realistically there no “correct” answer given that different packages have used the format differently.</p>
<p>You probably need to manually correct this flipping based on some extra knowledge about the source of the image files in question.</p>
<p>Hope that helps.</p>

---

## Post #5 by @Xiaogai_Li (2019-08-11 19:44 UTC)

<p>Thanks indeed very helpful!</p>
<p>Yes the image was loaded from Analyze format (.img and .hdr). What you said seems a good explanation why Slicer4 and Slicer4 saved to flipped image: Due to ITK Analyze reader Slicer uses are different.</p>
<p>Then back to the mhd format which I am most interested in. As mentioned earlier no matter what orientation the original source of image is (RAI, LPS or others), when saved into mhd using Slicer4, the mhd header always write: RAI+TransformMatrix as Identity matrix. I would guess then the .zraw image order is adjusted accordingly to its original image. I will test more to confirm. At least now it is clear Slicer3 and Slicer4 behaves differently when save to mhd file for a good reason.</p>
<p>Thanks again for all the valuable discussions.</p>

---

## Post #6 by @lassoan (2019-08-12 01:19 UTC)

<p>A couple of years ago we asked Kitware (developer and maintainer of metaimage file format) about Anatomical Orientation tag and they responded that it is informational only and it <a href="https://issues.slicer.org/view.php?id=2173#c5796" rel="nofollow noopener">should not be used for updating direction cosines</a>. We updated Slicer accordingly.</p>
<p>Interestingly, recently Kitware has revised this decision and now considering using AnatomicalOrientation tag to update axis directions after all. If Kitware ends up updating MetaIO library and mha reader/writer in ITK then Slicer’s behavior maybe become more similar to the Slicer3.</p>
<p>All these of course for your information only. To make your scenes usable in current Slicer, you need to follow <a class="mention" href="/u/pieper">@pieper</a>’s recommendation above and fix up the header or apply a transform to your images as needed.</p>

---

## Post #7 by @Xiaogai_Li (2019-08-12 08:15 UTC)

<p>Thanks a lot for all the info! Now all seems clear to me.</p>

---
