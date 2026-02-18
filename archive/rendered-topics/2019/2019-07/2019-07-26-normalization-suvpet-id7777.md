# Normalization SUVPET

**Topic ID**: 7777
**Date**: 2019-07-26
**URL**: https://discourse.slicer.org/t/normalization-suvpet/7777

---

## Post #1 by @Mgi (2019-07-26 20:28 UTC)

<p>Dear,</p>
<p>How to normalize some PET images by SUVmax using the PETDICOM extension?</p>

---

## Post #2 by @fedorov (2019-07-29 16:52 UTC)

<p>Once you install DICOM PET extension, you should be able to load the DICOM PET series SUV-corrected by selecting the PET series in DICOM Browser, and loading it.</p>
<p>To calculate SUVmax, you will need to segment the region of interest, which you can do using Segment Editor module. Once you have segmentation ready, you can use <a href="http://qiicr.org/tool/PETIndiC/" rel="nofollow noopener">PET-IndiC extension</a> to calculate SUVmax for that region.</p>
<p>Note that Indi-C extension is not building at the moment for the nightly, you will need to use the latest stable build to access that functionality.</p>
<p>I am not sure though if we have a module to divide the image by SUVmax constant to do the normalization. I thought SimpleFilters can do this, but it looks like they only support operations between images, and not scaling image by constant. <a class="mention" href="/u/blowekamp">@blowekamp</a> am I correct?</p>
<p>cc: <a class="mention" href="/u/chribaue">@chribaue</a></p>

---

## Post #3 by @blowekamp (2019-07-29 17:56 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="2" data-topic="7777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I thought SimpleFilters can do this, but it looks like they only support operations between images, and not scaling image by constant. <a class="mention" href="/u/blowekamp">@blowekamp</a> am I correct?</p>
</blockquote>
</aside>
<p>In Python the SimpleITK filters are certainly able to multiply by a constant, but this functionality is not currently exposed in the SimpleFilter GUI module.</p>

---

## Post #4 by @Mgi (2019-07-29 18:16 UTC)

<p>Thank you!</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> When I load the DICOM PET series appear this message window: “Could not load (SUVbw) as a PET SUV plugin”.</p>

---

## Post #5 by @lassoan (2019-07-29 18:27 UTC)

<p>For simple arithmetic operations, such as applying an arbitrary function to each voxel value, you may also use numpy. You can get read/write access to voxel values as a numpy array as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" rel="nofollow noopener">here</a>.</p>

---

## Post #6 by @fedorov (2019-07-30 03:05 UTC)

<p>Just wanted to confirm there is no UI module for this functionality. Thanks <a class="mention" href="/u/blowekamp">@blowekamp</a> and <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #7 by @fedorov (2019-07-30 03:05 UTC)

<aside class="quote no-group" data-username="Mgi" data-post="4" data-topic="7777">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/b19c9b/48.png" class="avatar"> Mgi:</div>
<blockquote>
<p>When I load the DICOM PET series appear this message window: “Could not load (SUVbw) as a PET SUV plugin”.</p>
</blockquote>
</aside>
<p>Can you share deidentified dataset?</p>

---

## Post #8 by @Mgi (2019-07-30 17:56 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> Yes, could I send to you for e-mail? because in this post doesn´t possible</p>

---

## Post #9 by @fedorov (2019-08-02 02:38 UTC)

<p>I received the dataset, and I can reproduce the problem, but I don’t have a quick answer. For some reason it fails at the GDCM level. I also will need to build Slicer to debug this, I don’t have a built version right now.</p>
<p><a class="mention" href="/u/chribaue">@chribaue</a> do you have any suggestions? If you have a compiled Slicer, could you investigate this?</p>
<pre><code class="lang-auto">itk::ExceptionObject (0x7f8051b2eb40)
Location: "unknown" 
File: /Volumes/Dashboards/Stable/Slicer-4102-build/ITK/Modules/IO/GDCM/src/itkGDCMImageIO.cxx
Line: 233
Description: itk::ERROR: GDCMImageIO(0x7f8051b068a0): Failed to get the buffer!
</code></pre>

---
