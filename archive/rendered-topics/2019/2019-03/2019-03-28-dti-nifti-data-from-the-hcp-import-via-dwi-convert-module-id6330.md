# DTI Nifti data from the HCP import via DWI Convert Module

**Topic ID**: 6330
**Date**: 2019-03-28
**URL**: https://discourse.slicer.org/t/dti-nifti-data-from-the-hcp-import-via-dwi-convert-module/6330

---

## Post #1 by @Bebo (2019-03-28 16:36 UTC)

<p>Hello every one,</p>
<p>I’m using 3D Slicer 4.10.1. I’m currently trying to convert DTI Nifti data from the HCP import via DWI Convert Module (the data come from <a href="http://www.humanconnectomeproject.org/" rel="nofollow noopener">http://www.humanconnectomeproject.org/</a>).<br>
However I have this error message:</p>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard error:<br>
Error: ReadVolume: Unsupported source pixel type.<br>
Input volume:  float<br>
Output volume: short<br>
The only supported output type is . You may consider using allowLossyConversion option.<br>
However, use this option with caution! Conversion from images of a different type may cause data loss due to rounding or truncation.</p>
<p>The bval. and .bvec files originally came in .txt format<br>
Does someone have a clue ?</p>

---

## Post #2 by @zhangfanmark (2019-03-28 17:06 UTC)

<p>Hi,</p>
<p>Have you tried to use allowLossyConversion as suggested by DWIConvert.</p>
<p>For our processing of the HCP data, we use this option.</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @Bebo (2019-03-29 08:52 UTC)

<p>Hi <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a>,<br>
Yes I did, I even tried all possible combinations of options.<br>
I noticed that every time I used the lossy option, the DWIconvert window pops up explaining that it crashed but I have no longer the message explaning the possible sources of error<br>
“Diffusion-weighted DICOM Import (DWIConvert) standard error:<br>
Error: ReadVolume: Unsupported source pixel type…”</p>

---

## Post #4 by @ljod (2019-03-29 09:33 UTC)

<p>Hi what version of Slicer are you using?</p>

---

## Post #5 by @Bebo (2019-03-29 09:45 UTC)

<p>Hi <a class="mention" href="/u/ljod">@ljod</a>,<br>
I’m using Slicer 4.10.1 version</p>

---

## Post #6 by @ljod (2019-04-02 17:48 UTC)

<p>Hi I think Fan can get back to you about how he processed the data when his conference paper is submitted today.<a class="mention" href="/u/zhangfanmark">@zhangfanmark</a></p>

---

## Post #7 by @Bebo (2019-04-03 08:13 UTC)

<p>Hi <a class="mention" href="/u/ljod">@ljod</a>,<br>
I have no explanation about why it worked this time… Few days ago, I registered to the other human connectome project (<a href="https://www.humanconnectome.org/" rel="nofollow noopener">https://www.humanconnectome.org/</a>) and I did the same manipulations, using the “allowLossyConversion” option as <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a> mentionned.  Finally it worked this time…<br>
I don’t know if initially the data was corrupted, but in case <a class="mention" href="/u/ljod">@ljod</a> <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a> thank you for the advice!</p>

---

## Post #8 by @hercp (2020-08-10 03:14 UTC)

<p>Nicolas,</p>
<p>What exactly did you do to make this work?</p>
<p>HP</p>

---

## Post #9 by @Tamires_Zanao (2021-03-16 10:36 UTC)

<p>Hi! First, I also had this issue with DWIConvert, but it worked using allowLossyConversion. However, I cannot open the .nhdr file on Slicer. Do you know what could be wrong? Thanks!</p>
<p>Best,<br>
Tamires</p>

---

## Post #10 by @lassoan (2021-03-26 03:25 UTC)

<p>If you can provide an example .nhdr and corresponding .raw file then we can help investigating the issue.</p>

---
