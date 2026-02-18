# Saving dicom to dicom, the exported and input do not match

**Topic ID**: 23173
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/saving-dicom-to-dicom-the-exported-and-input-do-not-match/23173

---

## Post #1 by @S_Arbabi (2022-04-28 15:08 UTC)

<p>I can’t understand this, can someone explain a bit?<br>
I open a dicom serie:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/effb6222185706eb1d0a6fa8e7096c2cdad25488.jpeg" data-download-href="/uploads/short-url/yeYHvvcgzCjyIPqP4ADC2U02O9y.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/effb6222185706eb1d0a6fa8e7096c2cdad25488_2_690x296.jpeg" alt="image" data-base62-sha1="yeYHvvcgzCjyIPqP4ADC2U02O9y" width="690" height="296" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/effb6222185706eb1d0a6fa8e7096c2cdad25488_2_690x296.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/effb6222185706eb1d0a6fa8e7096c2cdad25488_2_1035x444.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/effb6222185706eb1d0a6fa8e7096c2cdad25488_2_1380x592.jpeg 2x" data-dominant-color="8C8C92"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×824 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>then I right click on it and choose export to DICOM:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/734991ddc7a808a1917f777c28a195b451ab6779.jpeg" data-download-href="/uploads/short-url/grSwXFct84MkObHOY4l1wJmIN3r.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/734991ddc7a808a1917f777c28a195b451ab6779_2_690x299.jpeg" alt="image" data-base62-sha1="grSwXFct84MkObHOY4l1wJmIN3r" width="690" height="299" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/734991ddc7a808a1917f777c28a195b451ab6779_2_690x299.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/734991ddc7a808a1917f777c28a195b451ab6779_2_1035x448.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/734991ddc7a808a1917f777c28a195b451ab6779_2_1380x598.jpeg 2x" data-dominant-color="8B8C92"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1901×824 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and simply hitting export:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d50f85b5cb39b8c12640fe34a5a95ab8326e1a80.png" data-download-href="/uploads/short-url/uoOXmYMTpHxsxX4CX7qNuudDFJu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d50f85b5cb39b8c12640fe34a5a95ab8326e1a80_2_690x296.png" alt="image" data-base62-sha1="uoOXmYMTpHxsxX4CX7qNuudDFJu" width="690" height="296" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d50f85b5cb39b8c12640fe34a5a95ab8326e1a80_2_690x296.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d50f85b5cb39b8c12640fe34a5a95ab8326e1a80_2_1035x444.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d50f85b5cb39b8c12640fe34a5a95ab8326e1a80_2_1380x592.png 2x" data-dominant-color="BABBC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×824 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>what I expect is that the input and exported DICOM should be the same in image voxel data at least (DICOM tags can differ, that’s fine).<br>
BUT, it’s not the case! here, some statistics of the two DICOMs:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6023bce6d7fe25e21f71415cd9b0974ca883b0c.png" data-download-href="/uploads/short-url/wOKBqELxJEnxSswVnFL3nQemo7a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6023bce6d7fe25e21f71415cd9b0974ca883b0c.png" alt="image" data-base62-sha1="wOKBqELxJEnxSswVnFL3nQemo7a" width="687" height="500" data-dominant-color="DDDDDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1006×732 46.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance,<br>
Saeed</p>

---

## Post #2 by @mikebind (2022-04-28 16:44 UTC)

<p>Can you get a screenshot of what shows in the Slicer “Volume Information” section in the Volumes module?  Which does it agree with, the pre-import or post-export data?</p>

---

## Post #3 by @S_Arbabi (2022-04-28 17:20 UTC)

<p>The “Volume Information” section in Volume Module is shown in screenshot below:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/571a6438ca6516fa043db1ed16375265fd52953f.png" alt="image" data-base62-sha1="cqy5aJPXIgQZL5U67keBDqjfDwH" width="598" height="387"></p>
<p>I’m not sure which info I should look for, but from the information I can see in common between the statistics I shared before and the Volume Information is “Scalar Range” which seems to agree with Post-Export data (left side statistics window below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85ed16466d465275b13b8d2fca37590206d41cf1.png" data-download-href="/uploads/short-url/j6LswOKYdKXObyMi3QjFtj9W6Ih.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85ed16466d465275b13b8d2fca37590206d41cf1.png" alt="image" data-base62-sha1="j6LswOKYdKXObyMi3QjFtj9W6Ih" width="690" height="267" data-dominant-color="E7E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">990×384 9.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @mikebind (2022-04-28 17:40 UTC)

<p>Thanks. One other place to look would be to see if you got any errors or warnings when importing from DICOM.  You can see an error log by clicking on the “X” in the lower right of the Slicer window (which is red if there are any new messages there since the last time you opened it).</p>
<p>I agree this shouldn’t be happening.  My guess is that there is something which is either incorrect, inconsistent, or incorrectly interpreted by Slicer in the DICOM headers for this image volume.</p>
<p>Your problem is not the same, but there might be some helpful related info in this thread: <a href="https://discourse.slicer.org/t/the-slice-view-is-of-different-intensity-than-the-actual-object/">https://discourse.slicer.org/t/the-slice-view-is-of-different-intensity-than-the-actual-object/</a></p>

---

## Post #5 by @S_Arbabi (2022-04-28 17:47 UTC)

<p>No errors or warnings while importing DICOM:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db771b9f604cdd3eddf5e16a47c2457a045dd2c.png" data-download-href="/uploads/short-url/b5vN99CH21HxJcoqwBljo2yzkvi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db771b9f604cdd3eddf5e16a47c2457a045dd2c.png" alt="image" data-base62-sha1="b5vN99CH21HxJcoqwBljo2yzkvi" width="690" height="288" data-dominant-color="EAEAF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">898×376 23.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for the link, I look into it and let you know.</p>

---

## Post #6 by @lassoan (2022-04-28 17:57 UTC)

<p>In Slicer, is the scalar range the same is the same in the original image and in the image that has gone through DICOM export and import? If yes, then probably the difference is just in raw (manufacturer dependent) pixel values, which DICOM exporters are free to choose, along with the corresponding modality LUT (Rescale Slope (0028, 1053) and Rescale Intercept (0028, 1052)).</p>
<p>Maybe modality LUT was not applied when you loaded the data into Mevislab and you are comparing raw voxel values. It is normal to have difference in range of raw voxel values when you import and re-export DICOM.</p>

---

## Post #7 by @S_Arbabi (2022-04-28 18:16 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> interesting discussion in the link you shared.<br>
When I open my original dicom file in Mevislab, it’s type is unsigned int16 (right info box), while exported dicom is int16:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77daab872fb5ea61074a2e77f4d292de14ea95eb.png" data-download-href="/uploads/short-url/h6hjFX2iHDVC8gPmmeR7nRcyP7t.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77daab872fb5ea61074a2e77f4d292de14ea95eb_2_690x416.png" alt="image" data-base62-sha1="h6hjFX2iHDVC8gPmmeR7nRcyP7t" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77daab872fb5ea61074a2e77f4d292de14ea95eb_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77daab872fb5ea61074a2e77f4d292de14ea95eb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77daab872fb5ea61074a2e77f4d292de14ea95eb.png 2x" data-dominant-color="94999F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">691×417 30.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>when I check the dicom tags for original dicom, the Bits Stored is 12 and High Bit is 11 while Bits Allocated is 16 which baffles me:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/993f724f141dfa27209e640bde3c4812a712e607.png" alt="image" data-base62-sha1="lRGZab6Y5rUD09hI1fDlNMA6acD" width="520" height="129"></p>
<p>If I open the same tags for exported dicom, it seems to be more realistic:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91cbd8447ae9cb02c95b75934692ee0f994480e9.png" alt="image" data-base62-sha1="kNLY3A90HvVppZLTVHbzWsNYPLb" width="549" height="133"></p>
<p>So would you say I should try correcting my dicom headers? opening them in PyDicom and  saving Bits Stored and High Bit as 16 and 15?</p>

---

## Post #8 by @S_Arbabi (2022-04-28 18:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> scalar range is the same in slicer (although slicer sees the original as double and exported as short data type):<br>
original dicom:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/828cbdc6843b1af6dc95ba338575313c3f8276d2.png" alt="image" data-base62-sha1="iCTBHfqhPROURxyWBDa9Me5HBmO" width="599" height="389"></p>
<p>exported dicom:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc3b4cfbc4110e5c71e8e0e8a538bb26bbc01bb5.png" alt="image" data-base62-sha1="zZlnaHIcPE2UVOYU5JPMbeeW8zb" width="601" height="383"></p>

---

## Post #9 by @mikebind (2022-04-28 18:39 UTC)

<p>Here’s a page which does a good job of explaining the BitsAllocated, BitsStored, and HighBit tags: <a href="http://dicomiseasy.blogspot.com/2012/08/chapter-12-pixel-data.html" class="inline-onebox">DICOM is Easy: Chapter 12: Pixel Data</a></p>
<p>If your original data is 12-bit, then the maximum (raw) value possible should be 4096, and the imported version exceeds this.  This could be altered by the RescaleSlope and RescaleIntercept tags, so check those, but this suggests that perhaps one or more of the non-data bit values is being treated as if it were part of the data.</p>

---

## Post #10 by @lassoan (2022-04-28 18:46 UTC)

<p>This looks all good. Bits allocated, bits stored, high bit fields should be fine, as we don’t see any sign of overflow or saturation in the images. These bit fields were introduced when sometimes additional image masks were stored in unused bits of the pixel data, but these are very rarely used nowadays, and not used by Slicer’s DICOM exporter either, so it is OK to use up all the available 16 bits in the pixel data to store the raw voxel values.</p>
<p>It seems that the problem is that mevislab does not apply modality LUT on DICOM import. I’m very surprised that this is not already part of the DICOM importer, because without modality LUT you get raw pixels that are not usable for much. It seems that in mevislab you need to add a <a href="https://mevislabdownloads.mevis.de/docs/current/MeVisLab/Standard/Documentation/Publish/ModuleReference/DicomLUT.html">DicomLUT box</a> or <a href="https://mevislabdownloads.mevis.de/docs/current/FMEstable/ReleaseMeVis/Documentation/Publish/ModuleReference/ApplyDicomPixelModifiers.html#ApplyDicomPixelModifiers">ApplyDicomPixelModifier box</a> (or some other filters) for every DICOM importer box to get usable image voxel values.</p>

---
