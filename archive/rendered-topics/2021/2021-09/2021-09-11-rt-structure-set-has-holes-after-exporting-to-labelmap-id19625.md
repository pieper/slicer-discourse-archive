---
topic_id: 19625
title: "Rt Structure Set Has Holes After Exporting To Labelmap"
date: 2021-09-11
url: https://discourse.slicer.org/t/19625
---

# RT structure set has holes after exporting to labelmap

**Topic ID**: 19625
**Date**: 2021-09-11
**URL**: https://discourse.slicer.org/t/rt-structure-set-has-holes-after-exporting-to-labelmap/19625

---

## Post #1 by @liuhuaying (2021-09-11 08:02 UTC)

<p>Hi, I‘m facing another problem when I perform these operations. After export labelmap, the labelmap I got is missing some information. this picture is before export</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09286d916e339cf142b00bf949c91f28e4f02f96.jpeg" data-download-href="/uploads/short-url/1j0UEK9Kr6DD9ukqMjq4RbgGmUu.jpeg?dl=1" title="_before" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09286d916e339cf142b00bf949c91f28e4f02f96_2_690x415.jpeg" alt="_before" data-base62-sha1="1j0UEK9Kr6DD9ukqMjq4RbgGmUu" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09286d916e339cf142b00bf949c91f28e4f02f96_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09286d916e339cf142b00bf949c91f28e4f02f96_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09286d916e339cf142b00bf949c91f28e4f02f96_2_1380x830.jpeg 2x" data-dominant-color="A2A3A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">_before</span><span class="informations">1440×868 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>this one is after export</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5669ef71ca52a8fa915f9d3d0c2b5bfa6d43006.jpeg" data-download-href="/uploads/short-url/wJncIudXYbI8Y2prmQiiKGAXKQe.jpeg?dl=1" title="_after" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5669ef71ca52a8fa915f9d3d0c2b5bfa6d43006_2_690x415.jpeg" alt="_after" data-base62-sha1="wJncIudXYbI8Y2prmQiiKGAXKQe" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5669ef71ca52a8fa915f9d3d0c2b5bfa6d43006_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5669ef71ca52a8fa915f9d3d0c2b5bfa6d43006_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e5669ef71ca52a8fa915f9d3d0c2b5bfa6d43006_2_1380x830.jpeg 2x" data-dominant-color="A3A4A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">_after</span><span class="informations">1440×868 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>could u tell me why? Thanks a lot.</p>

---

## Post #2 by @lassoan (2021-09-12 00:38 UTC)

<p>It looks like that the RT structure set is invalid (multiple contours are specified for the same slice). What software did you use to create this? Can you send a download link to the anonymized data set so that we can have a look?</p>

---

## Post #3 by @liuhuaying (2021-09-12 01:45 UTC)

<p>Thank you, you are right, a slice does have multiple contours. I have found a python package called “dcmrtstruct2nii”, it can convert DICOM-RTSTRUCT format to Nifti format.</p>

---

## Post #4 by @lassoan (2021-09-12 01:54 UTC)

<p>What software created this contour?</p>
<p>dcmrtstruct2nii uses an incorrect algorithm for contour conversion, based on a misinterpretation of the DICOM standard. If the software that created the RT structure set similarly misinterpreted the DICOM standard then the result may be good (the two errors cancel out each other). However, in general, you should not use neither the software that created these invalid contour, nor dcmstruct2nii.</p>

---

## Post #5 by @liuhuaying (2021-09-12 03:25 UTC)

<p>sorry, I don’t know what software created this contour. After I converted rtstru with dcmrtstruct2nii and opened it with ITK-SNAP software, it seemed to be correct. As shown in this picture<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2802e274445715df6918bcb028db6e8ed8eb989c.png" alt="1631417109(1)" data-base62-sha1="5HXhixnDfO4Bx0Xl3KBg8GE9Ct6" width="368" height="313"><br>
. Is it the case you mention? (the two errors cancel out each other)       .</p>

---

## Post #6 by @liuhuaying (2021-09-12 05:13 UTC)

<p>Another strange thing happened, some rtstruct can use 3d slicer to export to labelmap without holes, but its image dimension become smaller. As show in the picture<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c2ebe7334a90f13d7f87d706a4cdd900ef8d1a1.png" data-download-href="/uploads/short-url/8AoNoojgaovUZVTMwJrxFL66Cgp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c2ebe7334a90f13d7f87d706a4cdd900ef8d1a1.png" alt="image" data-base62-sha1="8AoNoojgaovUZVTMwJrxFL66Cgp" width="690" height="113" data-dominant-color="8E8F90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">958×158 2.66 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
It’s original size should be 512<em>512</em>227</p>
<p>These questions really bother me. Hope can get your help. thanks!</p>

---

## Post #7 by @lassoan (2021-09-12 11:42 UTC)

<p>We enabled this feature (automatic cropping of the voxel array to minimize file size) by default in earlier Slicer versions. However, this caused complications when people wanted to press these images in software that ignored physical space information. So, we changed the behavior and in current Slicer Stable Release and Slicer Preview Release we don’t crop the exported labelmaps to the minimum necessary size by default anymore.</p>

---

## Post #8 by @lassoan (2021-09-12 12:21 UTC)

<aside class="quote no-group" data-username="liuhuaying" data-post="5" data-topic="19625">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/4bbf92/48.png" class="avatar"> liuhuaying:</div>
<blockquote>
<p>I don’t know what software created this contour</p>
</blockquote>
</aside>
<p>Where did you get the data sets from? I would contact them and tell them to either fix their data sets or offer them in other formats.</p>

---

## Post #9 by @liuhuaying (2021-09-13 01:40 UTC)

<p>I use Slicer 4.11.20210226 and Slicer 4.13.0-2021-09-07 versions, they both automatically crop the labelmap without holes to minimize the file size.</p>

---

## Post #10 by @liuhuaying (2021-09-13 01:44 UTC)

<p>The data came from a hospital. The doctor said they used commercial software, but I had no way to get these commercial software. Can I use the data transferred from dcmrtstruct2nii? Will using them cause any other problems?</p>

---

## Post #11 by @lassoan (2021-09-13 14:09 UTC)

<aside class="quote no-group" data-username="liuhuaying" data-post="9" data-topic="19625" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/4bbf92/48.png" class="avatar"> liuhuaying:</div>
<blockquote>
<p>I use Slicer 4.11.20210226 and Slicer 4.13.0-2021-09-07 versions, they both automatically crop the labelmap without holes to minimize the file size.</p>
</blockquote>
</aside>
<p>These Slicer versions use the segmentation geometry as output, which is determined from the first selected master volume. If you want to use a specific volume’s geometry in the segmentation then you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume">choose that volume as reference volume</a>.</p>
<aside class="quote no-group" data-username="liuhuaying" data-post="10" data-topic="19625" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/4bbf92/48.png" class="avatar"> liuhuaying:</div>
<blockquote>
<p>The data came from a hospital. The doctor said they used commercial software, but I had no way to get these commercial software. Can I use the data transferred from dcmrtstruct2nii? Will using them cause any other problems?</p>
</blockquote>
</aside>
<p>Let us know if you get to know what software they are using exactly and how. Maybe they do some conversion or anonymization step that messes up the original data or the segmentation tool is not used properly or not DICOM compliant.</p>

---

## Post #12 by @issakomi (2021-09-13 16:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19625">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It looks like that the RT structure set is invalid (multiple contours are specified for the same slice).</p>
</blockquote>
</aside>
<p>Interesting. IMHO, ROI for something concave that looks like e.g. tooth with two roots will have several slices with one contour, several with two. Do you think it is invalid? BTW, there is new type <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.8.6.3.html#figure_C.8.8.6-2" rel="noopener nofollow ugc">CLOSEDPLANAR_XOR</a>, it works only with multiple contours of one ROI per slice, per definition. Or do you mean “duplicated contours are specified for the same slice”, i have seen such data sets, it were bad, of course.</p>

---

## Post #13 by @gcsharp (2021-09-13 16:45 UTC)

<p>What the O.P. is seeing looks like a display bug.  I have seen similar.</p>
<p>You are correct, it’s totally fine to have multiple closed contours on a single slice. Or even not on a slice.  And thank you for the reference about CLOSEDPLANAR_XOR, this is new to me.  3D Slicer (plastimatch) uses XOR rather than keyholing for export, but with the CLOSED_PLANAR.  I wonder which systems would recognize and use CLOSEDPLANAR_XOR.</p>

---

## Post #14 by @lassoan (2021-09-13 17:26 UTC)

<p>I meant that overlapping planar contours are invalid - or at least they were, until CLOSEDPLANAR_XOR has been introduced. I have never seen CLOSEDPLANAR_XOR before and I would be really sad if vendors chose to put another twist on an already horrible segmentation representation instead of adopting DICOM Segmentation Object.</p>
<p>The <a href="http://dicom.nema.org/Dicom/News/September2020/docs/cpack108/cp2037.pdf">correction proposal that introduced CLOSEDPLANAR_XOR</a> - submitted by Varian and BrainLab engineers - indicates that the goal is to manage the misuse of the DICOM standard by “current implementation base of RT Structure Set” (it is unclear what software they refer to), by making it easier for treatment planning systems to reject XOR-style overlapping contours:</p>
<blockquote>
<p>For safety reasons, it should be possible to express this different technique, while assuring that systems that do not support this can still operate safely and not consume contours using this different technique.</p>
</blockquote>
<p>Probably we’ll need to wait for several more years to see if treatment planning system developers will start generating or accepting CLOSEDPLANAR_XOR themselves or they go and adopt second-generation DICOM RT objects (<a href="https://www.dicomstandard.org/news/supplements/view/2g-rt-objects-prescription-and-segment-annotation">2G RT</a>) instead. 2G RT promotes using common DICOM segmentation representations for “conceptual volume” definition in contrast to just locking into RT structure sets:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/470cf22642efb45f150b298d94a0925548ba43e7.png" data-download-href="/uploads/short-url/a8xDu4OBM2DmCezdenKzDq1lg11.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/470cf22642efb45f150b298d94a0925548ba43e7_2_690x162.png" alt="image" data-base62-sha1="a8xDu4OBM2DmCezdenKzDq1lg11" width="690" height="162" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/470cf22642efb45f150b298d94a0925548ba43e7_2_690x162.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/470cf22642efb45f150b298d94a0925548ba43e7_2_1035x243.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/470cf22642efb45f150b298d94a0925548ba43e7.png 2x" data-dominant-color="D9C9C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1071×252 67.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(<em><a href="https://www.dicomstandard.org/docs/librariesprovider2/dicomdocuments/news/ftsup/docs/sups/sup1475b81dad3499240fb8d4df9d98e4c29b0.pdf">source</a></em>)</p>

---

## Post #15 by @liuhuaying (2021-09-14 02:48 UTC)

<p>Thank you all, I will try to discuss with the hospital to see what’s going on.</p>

---

## Post #16 by @issakomi (2021-09-18 02:48 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="13" data-topic="19625">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>3D Slicer (plastimatch) uses XOR rather than keyholing for export, but with the CLOSED_PLANAR. I wonder which systems would recognize and use CLOSEDPLANAR_XOR.</p>
</blockquote>
</aside>
<p>Probably Varian may use CLOSEDPLANAR_XOR in a near future or uses already (Varian and BrainLab submitted the correction proposal). It looks like a kind of legalization of the technique they used already, e.g. screenshot with Varian’s ROI (CLOSED_PLANAR), blue (“Bones”)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e812207271ef5a2e651b1f7c517871431bfa0b0.jpeg" data-download-href="/uploads/short-url/bctUl3wR2ExAJhVriifUmu9BsS4.jpeg?dl=1" title="20210913-183532" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e812207271ef5a2e651b1f7c517871431bfa0b0_2_381x375.jpeg" alt="20210913-183532" data-base62-sha1="bctUl3wR2ExAJhVriifUmu9BsS4" width="381" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e812207271ef5a2e651b1f7c517871431bfa0b0_2_381x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e812207271ef5a2e651b1f7c517871431bfa0b0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e812207271ef5a2e651b1f7c517871431bfa0b0.jpeg 2x" data-dominant-color="424248"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20210913-183532</span><span class="informations">544×534 78.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have created <a href="https://drive.google.com/file/d/1hNH4NQfOuBGVHtfW4P5I8IqYopKxdTJ1/view?usp=sharing" rel="noopener nofollow ugc">test data set</a>, seems that SlicerRT has no problem with the new contour type, at least at a first look.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53ec1cabb242e4d4ca39ca6646c1c57c405e201f.png" data-download-href="/uploads/short-url/bYpuR15z1GTOU3lYWQFvKgSf6cT.png?dl=1" title="Screenshot at 2021-09-18 00-53-41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53ec1cabb242e4d4ca39ca6646c1c57c405e201f_2_517x357.png" alt="Screenshot at 2021-09-18 00-53-41" data-base62-sha1="bYpuR15z1GTOU3lYWQFvKgSf6cT" width="517" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53ec1cabb242e4d4ca39ca6646c1c57c405e201f_2_517x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53ec1cabb242e4d4ca39ca6646c1c57c405e201f_2_775x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53ec1cabb242e4d4ca39ca6646c1c57c405e201f_2_1034x714.png 2x" data-dominant-color="A69B94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2021-09-18 00-53-41</span><span class="informations">1047×725 82.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @gcsharp (2021-09-20 19:26 UTC)

<p>Thanks!  The result looks good.</p>

---

## Post #18 by @David_Clunie (2023-10-11 10:50 UTC)

<p>The link to the test dataset illustrated doesn’t seem to work - can you repost the test data or link to a persistent location for it please?</p>

---

## Post #19 by @Mik (2023-10-11 11:08 UTC)

<p>XOR test data set</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://disk.yandex.ru/d/iy2UnV0spDCLvA">
  <header class="source">
      <img src="https://yastatic.net/s3/psf/disk-public/_/5hb_sU044zVfPgNsMKf8pNs2_6H.png" class="site-icon" width="16" height="16">

      <a href="https://disk.yandex.ru/d/iy2UnV0spDCLvA" target="_blank" rel="noopener nofollow ugc">Яндекс&nbsp;Диск</a>
  </header>

  <article class="onebox-body">
    <img width="158" height="158" src="https://yastatic.net/s3/psf/disk-public/_/3DH63Jsqer9gW4U0rqWJpym3Kpn.png" class="thumbnail onebox-avatar">

<h3><a href="https://disk.yandex.ru/d/iy2UnV0spDCLvA" target="_blank" rel="noopener nofollow ugc">xor_test.7z</a></h3>

  <p>Посмотреть и скачать с Яндекс&nbsp;Диска</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #20 by @David_Clunie (2023-10-11 11:26 UTC)

<p>Thanks.</p>
<p>This reminds me that I need to add CP 2037 CLOSEDPLANAR_XOR Contour Geometric Type to dicom3tools dciodvfy.</p>

---
