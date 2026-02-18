# Export NRRD image to DICOM

**Topic ID**: 946
**Date**: 2017-08-25
**URL**: https://discourse.slicer.org/t/export-nrrd-image-to-dicom/946

---

## Post #1 by @george1 (2017-08-25 08:28 UTC)

<p>The problem is that my files are in the “.nrrd” format and I cannot open them with DICOM browser. Could I convert them from NRRD to DICOM?</p>

---

## Post #2 by @lassoan (2017-08-25 11:38 UTC)

<p>You can use DICOM module’s export feature: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export</a>. Use the latest nightly version of Slicer.</p>

---

## Post #3 by @pwang (2017-08-25 13:52 UTC)

<p>That one doesn’t work. Create a DICOM Series works!</p>

---

## Post #4 by @pwang (2017-08-25 13:53 UTC)

<p>Try Create a DICOM Series in the nightly built version</p>

---

## Post #5 by @lassoan (2017-08-25 14:06 UTC)

<aside class="quote no-group" data-username="pwang" data-post="3" data-topic="946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/73ab20/48.png" class="avatar"> pwang:</div>
<blockquote>
<p>That one doesn’t work.</p>
</blockquote>
</aside>
<p>Can you be a bit more specific? What version did you try that did not work? What did you do, what did you expect to happen, and what happened?</p>

---

## Post #6 by @pwang (2017-08-25 15:41 UTC)

<p>Nightly built 4.7.0 for Windows.<br>
My steps: 1. Create a project, 2. Drag the nrrd file under the project, 3.<br>
export to DICOM, 4. error meesage: <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3609d131532f78ad8caa4db8fbb2518c2e8d0853.png" alt="image" data-base62-sha1="7I2OCTx7fdu9NRSBsmr7HovoR0f" width="400" height="306"></p>

---

## Post #7 by @lassoan (2017-08-25 16:35 UTC)

<p>Thanks for the feedback. The instructions did not explain that you need to add a parent subject and study to your node before you can export it. I’ve added instructions to the wiki page. Please try it and let us know if the export works if you follow these steps: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export</a></p>

---

## Post #8 by @pwang (2017-08-28 01:34 UTC)

<p>It works. Thanks a lot.</p>
<p>But it doesn’t work on the version of MAC.</p>
<p>BTW, how I can change the Cost Function Convergence Factor, seen below? [image:<br>
Inline image 1]</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87aaf10b7a28fdbd3b10a963462437e2e3701430.png" alt="image" data-base62-sha1="jmaHlzjLGw5yO6WhKao3F1HvVks" width="317" height="75"></p>

---

## Post #9 by @lassoan (2017-08-28 02:26 UTC)

<aside class="quote no-group" data-username="pwang" data-post="8" data-topic="946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/73ab20/48.png" class="avatar"> pwang:</div>
<blockquote>
<p>It works. Thanks a lot.</p>
<p>But it doesn’t work on the version of MAC.</p>
</blockquote>
</aside>
<p>What is working?<br>
What is not working on Mac?</p>
<aside class="quote no-group" data-username="pwang" data-post="8" data-topic="946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/73ab20/48.png" class="avatar"> pwang:</div>
<blockquote>
<p>BTW, how I can change the Cost Function Convergence Factor, seen below? [image:<br>
Inline image 1]</p>
</blockquote>
</aside>
<p>This topic is about DICOM export. If the question is not about DICOM export then please post in a new topic. Add essential information, such as what module you are using and what you are trying to achieve.</p>

---

## Post #10 by @Yuri_Disaro_Amado (2020-07-02 05:58 UTC)

<p>I have been trying with no success to go through the described method and convert nrrd files from <a href="https://www.embodi3d.com/" rel="nofollow noopener">https://www.embodi3d.com/</a> into dicom.  Notably, the field “Input volume” only shows "Rename… " and “delete current node” as options, which can’t even be selected. Does that already explain what I could be doing wrong? I’m using Slicer 4.10.2 r28257</p>

---

## Post #11 by @lassoan (2020-07-06 03:07 UTC)

<aside class="quote no-group" data-username="Yuri_Disaro_Amado" data-post="10" data-topic="946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yuri_disaro_amado/48/7325_2.png" class="avatar"> Yuri_Disaro_Amado:</div>
<blockquote>
<p>the field “Input volume” only shows "Rename… " and “delete current node” as options, which can’t even be selected.</p>
</blockquote>
</aside>
<p>In what part of which module? Can you post a screenshot?</p>
<p>Do you want to export a segmentation or a CT/MRI image?</p>
<p>What Slicer version are you using? Please try with the latest Slicer Preview Release.</p>

---
