---
topic_id: 14697
title: "Dicom File From Slicer Viewed Differently In Materialise Mim"
date: 2020-11-20
url: https://discourse.slicer.org/t/14697
---

# DICOM file from Slicer viewed differently in Materialise Mimics

**Topic ID**: 14697
**Date**: 2020-11-20
**URL**: https://discourse.slicer.org/t/dicom-file-from-slicer-viewed-differently-in-materialise-mimics/14697

---

## Post #1 by @Asees_Kaur (2020-11-20 00:45 UTC)

<p>I am having an issue where I have exported a volume as a DICOM file from Slicer. I then import this same DICOM file into Materialise Mimics and am getting completely different scalar values. I was wondering if anyone had any thoughts on this??</p>

---

## Post #2 by @lassoan (2020-11-20 02:09 UTC)

<p>What values do you get if you load the exported files into Slicer or ITK-snap?</p>

---

## Post #3 by @Asees_Kaur (2020-11-20 16:45 UTC)

<p>Within slicer I’m getting the proper HU range for bone. However within Mimics I get highly negative density values. I was wondering if you knew what could change ?</p>

---

## Post #4 by @lassoan (2020-11-20 22:55 UTC)

<p>Please try with a couple of other software as well and see if they can load the image correctly.</p>
<p>We can investigate your finding if you can reproduce it with a data set that you can share with us (for example, data sets in Sample Data module or from open data repositories, such as TCIA).</p>

---

## Post #5 by @Asees_Kaur (2020-11-22 20:23 UTC)

<p>So, I imported a sample DICOM set from Slicer’s Tutorial page to Mimics and it worked fine. I think I am exporting my image data (volume node) as a DICOM incorrectly. I was wondering if you could take a look at my data, and my exported DICOM?</p>
<p>Sincerely,</p>
<p>Asees Kaur</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" alt="77C3A3DB5AF54B56A741600A3E5A8000.png" data-base62-sha1="eLzkAGZovUCazoJL65K1uagmWFJ" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2020-11-22 20:33 UTC)

<p>Yes, sure you can upload the dataset somewhere and post the link here. Make sure you don’t disclose any patient information.</p>

---

## Post #7 by @Asees_Kaur (2020-11-22 22:03 UTC)

<p>Yes, I have included my original image data file (linear_mesh_8_FINAL.vtk) and the DICOM file I exported from it (Scalar_Volume_9.zip) within the OneDrive link.<br>
<a href="https://onedrive.live.com/?id=9088EDA038297212%211452&amp;cid=9088EDA038297212" rel="noopener nofollow ugc">https://onedrive.live.com/?id=9088EDA038297212%211452&amp;cid=9088EDA038297212</a></p>
<p>Thank you very much.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" alt="77C3A3DB5AF54B56A741600A3E5A8000.png" data-base62-sha1="eLzkAGZovUCazoJL65K1uagmWFJ" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2020-11-22 23:58 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a> you are an expert in this field. Could you have a look at the exported DICOM data set to see if something is wrong with how the values are scaled?</p>

---

## Post #9 by @issakomi (2020-11-23 05:34 UTC)

<p>Thank you. Unfortunately the link doesn’t work for me. “This item might not exist or is no longer available”</p>

---

## Post #11 by @Asees_Kaur (2020-11-23 17:38 UTC)

<p>Here <a class="mention" href="/u/issakomi">@issakomi</a>  this link should work, <a href="https://1drv.ms/u/s!AhJyKTig7YiQiyyPr_Z-1sc3dgkt?e=oOCwzb" rel="noopener nofollow ugc">https://1drv.ms/u/s!AhJyKTig7YiQiyyPr_Z-1sc3dgkt?e=oOCwzb</a></p>
<p>Thank you I appreciate your help!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" alt="77C3A3DB5AF54B56A741600A3E5A8000.png" data-base62-sha1="eLzkAGZovUCazoJL65K1uagmWFJ" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @issakomi (2020-11-23 20:05 UTC)

<p>Thank you.<br>
Negative values are from original VTK file, -10000 for background (padding ?) probably. There is some loss in precision at export (original data is <em>float</em>, exported is <em>signed short</em>).</p>
<pre><code>linear_mesh_8_FINAL.vtk (float)
397 x 220 x 163
min. -10000, max. 1549.63000488281

DICOM (signed short)
397 x 220 x 163
min. -10000, max. 1549
</code></pre>
<p>I can only guess about Materialize, i don’t have the software, re-scale intercept is 1, slope is 0, so Modality LUT can not be a problem. May be Materialize doesn’t like signed scalars in CT, not sure, in DICOM files Pixel Presentation (0x0028,0x0103) value is 1 (signed, 2’s complement), it is valid too. So far DICOM export was not bad, IMHO. Geometry is correct too.<br>
The scalar range is large, to visualize details window width / level could be adjusted, e.g. (threshold off, s. histogram, width, level)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10bef015f6199d2cf28b68cabe76392188933a74.png" data-download-href="/uploads/short-url/2o8ILbqF7ek2Ym5iI2pZLivm3FW.png?dl=1" title="Screenshot at 2020-11-23 20-57-43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10bef015f6199d2cf28b68cabe76392188933a74_2_690x449.png" alt="Screenshot at 2020-11-23 20-57-43" data-base62-sha1="2o8ILbqF7ek2Ym5iI2pZLivm3FW" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10bef015f6199d2cf28b68cabe76392188933a74_2_690x449.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10bef015f6199d2cf28b68cabe76392188933a74_2_1035x673.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10bef015f6199d2cf28b68cabe76392188933a74.png 2x" data-dominant-color="7B7A7E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2020-11-23 20-57-43</span><span class="informations">1188×774 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @Asees_Kaur (2020-11-23 20:20 UTC)

<p>Thank you.<br>
Is there any way to export it as a float as opposed to signed short?<br>
Additionally, when I import the DICOM file I have created I receive this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a35ec595739dd64a88d843c0a36c271dbe03c77.png" data-download-href="/uploads/short-url/3JRWxE3JGnfYniV6YkXDoM8qdNR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a35ec595739dd64a88d843c0a36c271dbe03c77.png" alt="image" data-base62-sha1="3JRWxE3JGnfYniV6YkXDoM8qdNR" width="690" height="108" data-dominant-color="E3E3F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1463×229 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My DICOM file also imports in looking like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6427ef2812a5408f6308167ecca384da42d4f8d3.png" data-download-href="/uploads/short-url/ei1iX3i02kBHos7kFEebkkKz5gn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6427ef2812a5408f6308167ecca384da42d4f8d3.png" alt="image" data-base62-sha1="ei1iX3i02kBHos7kFEebkkKz5gn" width="690" height="291" data-dominant-color="191714"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">987×417 11.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @issakomi (2020-11-23 20:29 UTC)

<p>Window width/level unfortunately vary for different slices in exported DICOM, in fact 0/-10000 (it is bug, width can not be 0) in IMG0163.dcm (last one, it was applied), e.g.  10311/-4844, in IMG0001.dcm not available. But anyway full range or approximately full range is bad for particular case.</p>

---

## Post #15 by @Asees_Kaur (2020-11-23 20:41 UTC)

<p>I see, so the error is caused by the varying window with/level for the slices. What tends to cause this, and is there a way to export a DICOM without this happening? Also, is this a major problem for the DICOM file?</p>

---

## Post #16 by @issakomi (2020-11-23 20:46 UTC)

<aside class="quote no-group" data-username="Asees_Kaur" data-post="15" data-topic="14697">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/asees_kaur/48/6850_2.png" class="avatar"> Asees_Kaur:</div>
<blockquote>
<p>Also, is this a major problem for the DICOM file?</p>
</blockquote>
</aside>
<p>probably not a very big problem, it is visualization issue, may be you can adjust window/level in Materialize. Different values for slices are rather common in original MR data sets. Honestly i don’t know, may it is possible to control it somehow during Slicer export, not sure.</p>

---

## Post #17 by @Asees_Kaur (2020-11-23 20:52 UTC)

<p>Thank you for your assistance! I appreciate it, this helped clarify a lot!</p>

---

## Post #18 by @lassoan (2020-11-23 21:37 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a> Thanks a lot for your help with this.</p>
<p><a class="mention" href="/u/asees_kaur">@Asees_Kaur</a> Recommended window width/level value in exported DICOM images were improved a few weeks ago in Slicer, so if you use latest Preview Release then the default window/level values may be more meaningful. But as <a class="mention" href="/u/issakomi">@issakomi</a> wrote above, it is just a display issue, you should be able to set your preferred window/level value in Mimics anyway. By the way, if you already use Slicer, why do you need to export to Mimics? Is there anything that you miss from Slicer that Mimics can do?</p>

---

## Post #19 by @Asees_Kaur (2020-11-24 23:44 UTC)

<p><a class="mention" href="/u/issakomi">@issakomi</a>, so I found my Pixel representation is 1, meaning our data is represented at signed. However all attributes to do with image representation (group 0028 in metadata) are encoded as unsigned. So even though the pixel representation signifies that the data is signed, on displaying the DICOM image it is being incorrectly displayed as unsigned. is there a way within Slicer of exporting a DICOM with Pixel representation as unsigned.<br>
Here is the metadata of a DICOM file that works well<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa9f1a6f6c857a9206a5cf3e3d061962cec94d3b.png" data-download-href="/uploads/short-url/olo2VdRK6gWlVfJYCUmcLhIuKBt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa9f1a6f6c857a9206a5cf3e3d061962cec94d3b.png" alt="image" data-base62-sha1="olo2VdRK6gWlVfJYCUmcLhIuKBt" width="690" height="286" data-dominant-color="F3F4F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">983×408 13.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is my file that does not work well<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0262a0cf2cd49d175bde061e0bceced87148d249.png" data-download-href="/uploads/short-url/l6gpTGtCsMScEX88TPCht1Fqel.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/0262a0cf2cd49d175bde061e0bceced87148d249.png" alt="image" data-base62-sha1="l6gpTGtCsMScEX88TPCht1Fqel" width="690" height="190" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1044×288 9.78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #20 by @issakomi (2020-11-25 06:21 UTC)

<p>In fact, most original CT data sets use <em>PixelRepresentation</em> 0 (<em>unsigned</em>) and Modality LUT (re-scale intercept/slope) with negative <em>RescaleIntercept</em> to bring data into Hounsfield Units range (<em>RescaleType</em>=“HU”), as in your example above. But, AFAIK, <em>signed</em> is valid too, should work, s.</p>
<p><a href="https://dicom.innolitics.com/ciods/ct-image/image-pixel/00280103" rel="noopener nofollow ugc">dicom.innolitics.com/ciods/ct-image/image-pixel/00280103</a></p>

---

## Post #21 by @issakomi (2020-11-25 07:32 UTC)

<p>Tried to open the series in several DICOM viewers, seems to work (the only viewer failed to open the series at all, was Inobitec, don’t know why). May be (just guessing) it were better to skip DICOM export and create e.g. binary image or STL file in Slicer, if the purpose is 3D printing or mesh, may be it is possible to post-process or improve the file in Mimics later, not sure, of course.</p>
<p>Below screenshots (window level/width adjusted)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c429cddd61eec59969bc9c827f3a72e8c74c7f87.png" data-download-href="/uploads/short-url/rZl9fy0Y2JI3N8rNZNcJu5DrMEv.png?dl=1" title="microdicom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c429cddd61eec59969bc9c827f3a72e8c74c7f87_2_690x354.png" alt="microdicom" data-base62-sha1="rZl9fy0Y2JI3N8rNZNcJu5DrMEv" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c429cddd61eec59969bc9c827f3a72e8c74c7f87_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c429cddd61eec59969bc9c827f3a72e8c74c7f87_2_1035x531.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c429cddd61eec59969bc9c827f3a72e8c74c7f87_2_1380x708.png 2x" data-dominant-color="51555A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">microdicom</span><span class="informations">1440×740 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8584d408ae9a2eaf86c56af7ec8ff63fdfebf4b.jpeg" data-download-href="/uploads/short-url/sAkG8XJmJmvkgJNk2HN1KP94KiD.jpeg?dl=1" title="aliza" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8584d408ae9a2eaf86c56af7ec8ff63fdfebf4b_2_690x455.jpeg" alt="aliza" data-base62-sha1="sAkG8XJmJmvkgJNk2HN1KP94KiD" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8584d408ae9a2eaf86c56af7ec8ff63fdfebf4b_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8584d408ae9a2eaf86c56af7ec8ff63fdfebf4b_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8584d408ae9a2eaf86c56af7ec8ff63fdfebf4b.jpeg 2x" data-dominant-color="4C5157"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">aliza</span><span class="informations">1297×857 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c24a99c1aecc5bb93ee8ec7c01eaa4dcf8efb6e.png" data-download-href="/uploads/short-url/d98txjaOOuYwUJnplLXT5Wk3BpA.png?dl=1" title="Screenshot at 2020-11-25 09-04-07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c24a99c1aecc5bb93ee8ec7c01eaa4dcf8efb6e_2_690x458.png" alt="Screenshot at 2020-11-25 09-04-07" data-base62-sha1="d98txjaOOuYwUJnplLXT5Wk3BpA" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c24a99c1aecc5bb93ee8ec7c01eaa4dcf8efb6e_2_690x458.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c24a99c1aecc5bb93ee8ec7c01eaa4dcf8efb6e_2_1035x687.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c24a99c1aecc5bb93ee8ec7c01eaa4dcf8efb6e.png 2x" data-dominant-color="131413"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2020-11-25 09-04-07</span><span class="informations">1078×716 67.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f331e07b3cc1a19c30db6934d3c57c6d81bdc4dd.png" data-download-href="/uploads/short-url/yHoSVWLWLmB31ysmRGHOcMamzql.png?dl=1" title="Screenshot at 2020-11-25 09-06-44" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f331e07b3cc1a19c30db6934d3c57c6d81bdc4dd_2_690x453.png" alt="Screenshot at 2020-11-25 09-06-44" data-base62-sha1="yHoSVWLWLmB31ysmRGHOcMamzql" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f331e07b3cc1a19c30db6934d3c57c6d81bdc4dd_2_690x453.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f331e07b3cc1a19c30db6934d3c57c6d81bdc4dd_2_1035x679.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f331e07b3cc1a19c30db6934d3c57c6d81bdc4dd.png 2x" data-dominant-color="1E1D19"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2020-11-25 09-06-44</span><span class="informations">1186×779 91.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @Asees_Kaur (2020-11-25 21:53 UTC)

<p>Thank you all of that! <a class="mention" href="/u/issakomi">@issakomi</a> I have found that my issue was the Rescale Type (0028, 1054) is it set to US when it should be set to HU. I have found that the dcmodify tool works best for this from the DCMTK toolkit. Do you know how i can use the dcmodify tool in Slicer?</p>

---

## Post #23 by @issakomi (2020-11-25 22:13 UTC)

<p>IMHO, re-scale slope/intercept 1/0 and Unspecified type (US) was correct, Slicer could not know what kind of data was in VTK file. Anyway good if it worked. AFAIK, dcmodify is not packaged with Slicer.</p>

---

## Post #24 by @lassoan (2020-11-25 22:18 UTC)

<p>I think both dcmodify and pydicom are bundled with Slicer, but pydicom should be easier to use.</p>
<p>I can easily fix any issue in the exporter if I can confirm that it creates invalid output. I’ll check rescale type.</p>

---
