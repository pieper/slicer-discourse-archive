---
topic_id: 14357
title: "Error In Time Stamp Of Multivolume Data"
date: 2020-11-01
url: https://discourse.slicer.org/t/14357
---

# Error in time stamp of multivolume data

**Topic ID**: 14357
**Date**: 2020-11-01
**URL**: https://discourse.slicer.org/t/error-in-time-stamp-of-multivolume-data/14357

---

## Post #1 by @Selva (2020-11-01 10:10 UTC)

<p>Hi all,</p>
<p>I have a dynamic CT data set, saved as individual frames. when I  load them in the order they appear , the order of the frames (the sequence) is wrong- Appear interlaced.</p>
<p>How do I make the order according to correct time sequence please.</p>
<p>Series time appear the same in the series time column, so I cant sort by that</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d322a98dc0bcc7ccac3d192a24daf17c1a06fc53.png" alt="Screenshot 2020-11-01 at 21.08.54" data-base62-sha1="u7N0CdgqrrJcxuOhBFDRWUj7lkL" width="556" height="302"></p>

---

## Post #2 by @lassoan (2020-11-01 19:19 UTC)

<aside class="quote no-group" data-username="Selva" data-post="1" data-topic="14357">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/13edae/48.png" class="avatar"> Selva:</div>
<blockquote>
<p>I have a dynamic CT data set, saved as individual frames.</p>
</blockquote>
</aside>
<p>Do you mean that you extracted 3D volumes from a 4D acquisition with some software and now you are trying to create a volume sequence from it in Slicer?</p>
<p>It would be better if you loaded the dynamic CT directly, using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#read-dicom-files-into-the-scene">DICOM module</a>. We have tested dynamic CT import with dozens of scanners, so there is a good chance that it will work well.</p>
<p>What kind of images do you work with (cardiac, MSK, …)? What kind of analysis are you planning to do once the data is loaded (cardiac device placement evaluation, blood flow dynamic analysis, …)?</p>

---

## Post #3 by @Selva (2020-11-01 22:32 UTC)

<p>Hi Andras,</p>
<p>Thanks, I directly added that via DICOM module. This is MSK images for segmentation at each time point, hence the content time is important.</p>
<p>Is there any way that I can access metadata and sort this into an order</p>
<p>Thanks</p>
<p>Kind regards</p>
<p>Selva</p>

---

## Post #4 by @lassoan (2020-11-02 19:00 UTC)

<p>To investigate, we would need more information about the DICOM files - either the files or just information in the file header + application log. See details how to obtain these information here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#i-try-to-import-a-directory-of-dicom-files-but-nothing-shows-up-in-the-browser">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#i-try-to-import-a-directory-of-dicom-files-but-nothing-shows-up-in-the-browser</a></p>

---
