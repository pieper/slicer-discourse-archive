---
topic_id: 7306
title: "Open Dicom Files Having A Jpeg Transfert Syntax"
date: 2019-06-25
url: https://discourse.slicer.org/t/7306
---

# Open dicom files having a JPEG transfert syntax

**Topic ID**: 7306
**Date**: 2019-06-25
**URL**: https://discourse.slicer.org/t/open-dicom-files-having-a-jpeg-transfert-syntax/7306

---

## Post #1 by @Charles_Gueunet (2019-06-25 19:27 UTC)

<p>I have a DICOM file with RGB pixel data, using a Lossless JPEG transfer syntax and I do not get slicer to open it. Does Slicer handle this kind of transfer syntax ? I know GDCM can handle these files.</p>

---

## Post #2 by @lassoan (2019-06-26 02:30 UTC)

<p>I don’t think there is a DICOM plugin for loading color DICOM images. It should not be too difficult to add a new DICOM plugin or fix up the current scalar volume plugin (probably only a couple of lines would need to be modified). If you were interested in improving the DICOM importer then we would be happy to help with it.</p>
<p>In the meantime, you can also try to load the image using ITK: choose File / Add data in the menu and choose <em>one</em> of the files of the DICOM series.</p>

---

## Post #4 by @Charles_Gueunet (2019-06-26 07:47 UTC)

<blockquote>
<p>In the meantime, you can also try to load the image using ITK: choose File / Add data in the menu and choose <em>one</em> of the files of the DICOM series.</p>
</blockquote>
<p>Thank you very much, this method works.<br>
The loaded slice even has colors.</p>
<p>Do you know why the module to import DICOM cannot load this file ?</p>

---

## Post #5 by @lassoan (2019-06-27 05:13 UTC)

<aside class="quote no-group" data-username="Charles_Gueunet" data-post="4" data-topic="7306">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charles_gueunet/48/4043_2.png" class="avatar"> Charles_Gueunet:</div>
<blockquote>
<p>Do you know why the module to import DICOM cannot load this file ?</p>
</blockquote>
</aside>
<p>There does not seem to be much interest in loading color images. Most probably this is because color images are most often secondary captures (essentially screenshots) with  lower bit depth than the original (8 bit vs. 10-12 bits), with burnt-in annotations (patient information, rulers, region of interests, etc. drawn all over the image), missing essential information (such as position, orientation, and scale).</p>

---
