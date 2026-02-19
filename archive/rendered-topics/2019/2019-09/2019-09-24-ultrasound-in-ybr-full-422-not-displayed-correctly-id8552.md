---
topic_id: 8552
title: "Ultrasound In Ybr Full 422 Not Displayed Correctly"
date: 2019-09-24
url: https://discourse.slicer.org/t/8552
---

# Ultrasound in YBR_Full_422 not displayed correctly?

**Topic ID**: 8552
**Date**: 2019-09-24
**URL**: https://discourse.slicer.org/t/ultrasound-in-ybr-full-422-not-displayed-correctly/8552

---

## Post #1 by @hina-shah (2019-09-24 19:40 UTC)

<p>Hello,</p>
<p>I have an ultrasound image dicom that has a PhotometricInterpretation as YBR_FULL_422. Hence loading it results in a display like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2a33140100f3a436e6613ec6a688d767887272e.png" alt="image" data-base62-sha1="ncKZgXnGDnqSjoIXrrjZ8x9qQ10" width="244" height="224"></p>
<p>Is there anything that I can do to display it correctly? I’m trying to get to the actual RGB data in python to process the image, and this is a multi-frame ultrasound dicom.</p>
<p>Thanks!<br>
Hina</p>

---

## Post #2 by @pieper (2019-09-24 19:53 UTC)

<p>Hi <a class="mention" href="/u/hina-shah">@hina-shah</a> - you can probably read it directly with pydicom (<code>import dicom</code> in slicer).  We don’t have a direct importer for this, but a dicom plugin that detects and loads as vector volume would be feasible.</p>

---

## Post #3 by @lassoan (2019-09-24 20:01 UTC)

<p>As far as I remember, this is a bug in ITK’s color image reader (color components are mixed up). It seems that you have a B-mode image, which is a single scalar, so you can ignore this appearance and use “Vector to scalar volume” module to create a scalar image.</p>
<p>I agree with <a class="mention" href="/u/pieper">@pieper</a> that it would be nice to address this automatically in a custom DICOM plugin (but even better, in ITK).</p>

---

## Post #4 by @Chris_Rorden (2019-09-24 21:25 UTC)

<p><a class="mention" href="/u/hina-shah">@hina-shah</a> is this an image you can share? It would be nice to test, but I am pretty sure dcm2niix can convert this.Slicer supports RGB NIfTI images. With this route, you install the “SlicerDcm2nii” extension into slicer. After that, you would have the Dcm2niixGUI module installed and you could import images. I agree with <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/pieper">@pieper</a> that it would be more elegant to integrate this directly into slicer.</p>

---

## Post #5 by @hina-shah (2019-09-25 02:56 UTC)

<p>Thank you everyone for your suggestions!<br>
<a class="mention" href="/u/pieper">@pieper</a>: reading with pydicom, uncompresses, but does not convert to rgb - unless I’m doing something wrong. I tried normal YCbCr-&gt;rgb conversion, but am getting some sort of noise.<br>
<a class="mention" href="/u/lassoan">@lassoan</a>: the ultrasound actually loads fine with ITK-snap. Might have to see how the image is loaded there. Also, my aim is to read the tags embedded in the cine (which is yellow in color) - so I think I’d like to keep the rgb?<br>
<a class="mention" href="/u/chris_rorden">@Chris_Rorden</a>: I’ll have to double check if I can share the image. But thanks for the tip!</p>

---

## Post #6 by @issakomi (2019-09-25 07:45 UTC)

<p>It is known problem with GDCMIO, ITK-snap opens image as gray by default, if you’ll try set RGB it will be greenish blue too (Tools-&gt;Image Information-&gt;General-&gt;Display Mode).</p>
<p>There is one closed <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/822" rel="nofollow noopener">PR</a> (sorry i gave up) and it is currently <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/1240" rel="nofollow noopener">re-opened</a> again, but seems to be frozen.<br>
Generally, Ultrasound support in GDCM is very minimal, it doesn’t distinguish 2D+t and 3D, opens it as volume with fake geometry, cine frame time is not read, calibrated regions are not supported, <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/75615f60381ef74bf8d22d39c982380fbdc65fa9/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmImageHelper.cxx#L347" rel="nofollow noopener">spacing in GDCM is a kind of hack (reading 1st calibrated reagion)</a> and it is overriden with <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/75615f60381ef74bf8d22d39c982380fbdc65fa9/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L500" rel="nofollow noopener">another hack in GDCMIO</a>.</p>
<p><strong>Edit</strong>: BTW, currently that actual PR will not work, there was an attempt to use GDCM’s change photometric interpretation, but it crashes. If someone wants to try the working one i could re-created branch or just take from that <a href="https://github.com/InsightSoftwareConsortium/ITK/pull/1240#issuecomment-529763848" rel="nofollow noopener">post</a></p>

---

## Post #7 by @pieper (2019-09-25 11:37 UTC)

<p>Thanks for digging into this <a class="mention" href="/u/issakomi">@issakomi</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Yes, it would be great if you can sort this out with the ITK team, as that would help Slicer and others.</p>
<p>Also, <a class="mention" href="/u/hina-shah">@hina-shah</a>  if you can share an example I’m sure the pydicom devs would also be interested.</p>

---

## Post #8 by @lassoan (2019-09-25 18:53 UTC)

<aside class="quote no-group" data-username="hina-shah" data-post="5" data-topic="8552">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hina-shah/48/695_2.png" class="avatar"> hina-shah:</div>
<blockquote>
<p>the ultrasound actually loads fine with ITK-snap. Might have to see how the image is loaded there. Also, my aim is to read the tags embedded in the cine (which is yellow in color) - so I think I’d like to keep the rgb?</p>
</blockquote>
</aside>
<p>ITK-snap just shows the first component by default. As I wrote above, you can use “Vector to scalar volume” module in Slicer to extract the first component, which contains the image intensity (and safely ignore the two chroma channels).</p>

---

## Post #9 by @hina-shah (2019-09-25 20:12 UTC)

<p>Thank you for pointing at the PR’s in ITK <a class="mention" href="/u/issakomi">@issakomi</a>. I didn’t notice that ITK-snap is a grayscale image but thanks for pointing to it! It looks like these changes will make their way into ITK in future if not immediately. I guess I’ll try to either work with the luminance channel as <a class="mention" href="/u/lassoan">@lassoan</a> suggested , or see if your conversions would give me non-noisy images.</p>
<p><a class="mention" href="/u/pieper">@pieper</a>: will share an anonymized data here.</p>
<p>Thank you all!</p>

---

## Post #10 by @lassoan (2019-09-26 00:18 UTC)

<p>If you don’t need color information then you should use the luminance channel, because in case of ybr_full_422 encoding, color channels have half the spatial resolution of the luminance channel so you would potentially introduce artifacts by creating RGB image and converting that back to luminance (and also small potential errors due to floating point to integer conversion).</p>

---

## Post #11 by @issakomi (2019-09-26 10:26 UTC)

<p>I totally agree. But i still think it is a problem with GDCMIO, because the information in those Ultrasound images is saved in colors, many Ultrasound images have a kind of color bar for easier interpretation, specially lossy Jpeg (YBR_FULL_422) is not very good to save shades of gray, IMHO<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61a7c7b4fa2d772149e5213f1621a71f43dcbec9.png" data-download-href="/uploads/short-url/dVTMtr208H4rOoZJ6UZK2cFuH21.png?dl=1" title="20190926-115629" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61a7c7b4fa2d772149e5213f1621a71f43dcbec9_2_483x375.png" alt="20190926-115629" data-base62-sha1="dVTMtr208H4rOoZJ6UZK2cFuH21" width="483" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61a7c7b4fa2d772149e5213f1621a71f43dcbec9_2_483x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61a7c7b4fa2d772149e5213f1621a71f43dcbec9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61a7c7b4fa2d772149e5213f1621a71f43dcbec9.png 2x" data-dominant-color="191C1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20190926-115629</span><span class="informations">691×535 70.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @issakomi (2019-09-26 12:09 UTC)

<p>In GDCM <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/2b82a99b888657fb5edcc7f02ae576860ac33b10/Modules/ThirdParty/GDCM/src/gdcm/Source/MediaStorageAndFileFormat/gdcmJPEGBITSCodec.hxx#L861" rel="nofollow noopener">these 2 lines: 861, 862</a> make a difference. If commented out - image colors for lossy Jpeg are correct. It not a request to change it now, just FYI.</p>

---
