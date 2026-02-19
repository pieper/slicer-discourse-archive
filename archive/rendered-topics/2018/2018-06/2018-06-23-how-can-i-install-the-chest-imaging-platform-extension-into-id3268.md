---
topic_id: 3268
title: "How Can I Install The Chest Imaging Platform Extension Into"
date: 2018-06-23
url: https://discourse.slicer.org/t/3268
---

# How can I install the Chest_Imaging_Platform extension into Slicer Nightly Releases manually?

**Topic ID**: 3268
**Date**: 2018-06-23
**URL**: https://discourse.slicer.org/t/how-can-i-install-the-chest-imaging-platform-extension-into-slicer-nightly-releases-manually/3268

---

## Post #1 by @huzi_pf (2018-06-23 11:58 UTC)

<p>Hello,</p>
<pre><code>I am new to Chest Imaging Platform and 3d slicer. I tried to intall CPI into Slicer Nightly Releases manually， But I couldn’t achieve it. May you help achieve it ,thanks you very much!
</code></pre>
<p>发送自 Windows 10 版<a href="https://go.microsoft.com/fwlink/?LinkId=550986">邮件</a>应用</p>

---

## Post #2 by @jonieva (2018-06-24 05:05 UTC)

<p>Hi Huzi,</p>
<p>Let us look into this issue, you should be able to install the extension from the Slicer Nightly Release.</p>
<p>In the meantime, you can download a version of Slicer with all the Chest Imaging Platform tools already preinstalled from our website: <a href="https://chestimagingplatform.org/download">https://chestimagingplatform.org/download</a></p>
<p>I hope that helps,</p>
<p>Jorge Onieva</p>

---

## Post #3 by @huzipf (2018-07-06 01:23 UTC)

<p>Thanks for your help!</p>

---

## Post #4 by @carnico (2020-04-21 13:38 UTC)

<p>Hi at all!</p>
<p>I’ve downloaded the latest Slicer Nightly (4.11.0, rev 28989), and I cannot find CIP modules under the extension manager.</p>
<p>Do I need to install manually?</p>
<p>Best Regards</p>

---

## Post #5 by @pieper (2020-04-21 19:12 UTC)

<p>Looks like there is a build error in the extension with the current nightly.</p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1889414" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1889414</a></p>
<p>Probably you want to get the pre-integrated version:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://chestimagingplatform.org/profiles/openscholar/themes/hwpi_basetheme/favicon.png" class="site-icon" width="16" height="16">
      <a href="https://chestimagingplatform.org/download" target="_blank">chestimagingplatform.org</a>
  </header>
  <article class="onebox-body">
    <img src="https://chestimagingplatform.org/" class="thumbnail onebox-avatar" width="16" height="16">

<h3><a href="https://chestimagingplatform.org/download" target="_blank">Download</a></h3>

<p>3D Slicer with SlicerCIP integrated  (recommended)</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @carnico (2020-04-22 06:43 UTC)

<p>Thanks Steve,</p>
<p>actually, I need I nightly updated version because I use some other plugins.</p>
<p>By the way, I’ve manage to install an older nightly version using offset value in the download page but, unfortunaltely, some modules of CIP don’t work (Parenchimal Analysis and Interactive Lobe Segmentation). If you select one of those, the left side panel remains blank.</p>
<p>Thank you.</p>
<p>P.s.: it isn’t the topic but, do you now how to adjust the result of segmentation?</p>

---

## Post #7 by @pieper (2020-04-22 12:31 UTC)

<p>It looks like CIP is not building with the latest ITK, so someone will need to dig into the C++ and sort it out.  I know the CIP team has a lot on their plates, so maybe someone with the right skillset can jump in to help?</p>
<p>Regarding adjusting the segmentation, you can just use the segment editor?</p>

---

## Post #8 by @carnico (2020-04-22 14:04 UTC)

<p>I hope in solution. In the mean time, I’ll use two 3D slicer version at the same time.</p>
<p>For the segmentation, the problem are distelectasic area near thoracic wall, like these:</p>
<p><a href="https://postimg.cc/CnDTh5hm" data-bbcode="true" rel="nofollow noopener"><img src="https://i.postimg.cc/CnDTh5hm/segmentation.jpg" alt width="180" height="88"></a></p>
<p>And if I jump in the segmentation editor, I do not found the label created by CIP. Or, at least, I cannot open the interactiveLobeSegmentation output of CIP in the segmentation editor.</p>
<p><a href="https://postimg.cc/9rZCV8zC" data-bbcode="true" rel="nofollow noopener"><img src="https://i.postimg.cc/9rZCV8zC/segment-editor.jpg" alt width="180" height="88"></a></p>
<p>Maybe it’s better to start a new thread.</p>
<p>In any case, thank you!</p>

---

## Post #9 by @pieper (2020-04-22 14:18 UTC)

<p>Yes, using two versions of Slicer makes sense for now.</p>
<p>In the new Slicer you can import labelmaps in the segmentations module.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0be7e025522106983e8902082e69cf85a7224ecb.png" alt="image" data-base62-sha1="1Hk2GpxAKIntErjA8PEN1DChbg7" width="689" height="111"></p>

---

## Post #10 by @carnico (2020-04-28 15:52 UTC)

<p>Thanks Steve,</p>
<p>I did what you suggest, but the modified labels were not considered in the lung parenchimal analysys module. Values (volume, density, etc.) were the same.</p>
<p>Best Regards</p>

---

## Post #11 by @ava_yektaeian (2020-08-20 12:33 UTC)

<p>Hi Steve thanks for your useful answers<br>
i really have trouble in using interactive lobe segmentation . i import chest ct as dicom and and  after following the CIP iterative lobe segmentation  tutorial I cant achieve 5 lobe segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef10c91782d0b11cff659af1f60b34332dcd1397.jpeg" data-download-href="/uploads/short-url/y6S4QK9o0g5ACHhWfajkWhLHDVR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef10c91782d0b11cff659af1f60b34332dcd1397_2_690x388.jpeg" alt="image" data-base62-sha1="y6S4QK9o0g5ACHhWfajkWhLHDVR" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef10c91782d0b11cff659af1f60b34332dcd1397_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef10c91782d0b11cff659af1f60b34332dcd1397_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef10c91782d0b11cff659af1f60b34332dcd1397.jpeg 2x" data-dominant-color="BFC1C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×720 262 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @ava_yektaeian (2020-08-20 12:35 UTC)

<p>can i ask how you segment cause i follow the instruction but I achieve this instead of 5 lobes<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a01f0ffff95c6981ed3ffbe1c47f8b4e2d49bb46.png" data-download-href="/uploads/short-url/mQuWFQxPCFQyokMJETYPmDpKDqu.png?dl=1" title="xdd" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a01f0ffff95c6981ed3ffbe1c47f8b4e2d49bb46_2_690x375.png" alt="xdd" data-base62-sha1="mQuWFQxPCFQyokMJETYPmDpKDqu" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a01f0ffff95c6981ed3ffbe1c47f8b4e2d49bb46_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a01f0ffff95c6981ed3ffbe1c47f8b4e2d49bb46_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a01f0ffff95c6981ed3ffbe1c47f8b4e2d49bb46.png 2x" data-dominant-color="C5C7CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">xdd</span><span class="informations">1225×667 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @pieper (2020-08-25 20:52 UTC)

<p>I’m not familiar with the algorithm in CIP, but I can say there’s something wrong with your dicom files because they should not be upside down like that.  That’s very likely to mess up any automated lobe segmentation.</p>

---
