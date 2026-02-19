---
topic_id: 42625
title: "Request To Add The Function Of Importing Perkinelmers Vox Fo"
date: 2025-04-19
url: https://discourse.slicer.org/t/42625
---

# Request to add the function of importing PerkinElmer's .vox format data

**Topic ID**: 42625
**Date**: 2025-04-19
**URL**: https://discourse.slicer.org/t/request-to-add-the-function-of-importing-perkinelmers-vox-format-data/42625

---

## Post #1 by @ggg (2025-04-19 13:09 UTC)

<p>Hello everyone, my English level is not high, so many contents are translated by software, please forgive me if there are mistakes.<br>
I am currently using Bruker’s CTAn software to analyze data. Since I need to contact and analyze a lot of data from different CT manufacturers, sometimes I can’t import data in a specific format, which will cause me a lot of trouble. At present, it has perfectly compatible with nii data, vol format data of GE CT instruments, etc. through the support of 3D slicer and Fiji, but what is missing is perkinelmer’s .vox format data. Although I know that their software can be converted into dicom, my colleagues gave me vox format, so I can’t help them analyze the data. I hope everyone can help solve this problem and provide a method to import this kind of data.<br>
I uploaded a compressed package, which contains the data exported by the PE instrument and the data viewer. One data is the scan data of a tube of water, and the other data is the scan data of a density phantom. I will put the link below. I hope you can help me. Thank you.<br>
大家好，我的英语水平不高，所以很多内容是软件翻译的，有错漏的话请原谅。<br>
我目前使用的是布鲁克的CTAn软件分析数据，由于需要接触到跟分析不同CT厂商数据比较多，有些时候不能导入特定格式的数据会让我有很大的麻烦。目前已经通过3D slicer以及Fiji的支持下完美地兼容了nii数据，GE CT仪器的vol格式数据等等，但是缺少的是perkinelmer的 .vox格式数据，虽然我知道他们的软件可以转换成dicom,但是我的同事们给我的都是vox格式，所以我就没法帮他们分析数据。我希望大家能帮忙解决一下这个问题，提供一下导入这种数据的方法。<br>
我上传了一个压缩包，里面包含了PE仪器导出的数据以及数据查看器，一个数据是一管水的扫描数据，另一个数据是密度体模的扫描数据，链接我会放在下面，希望能得到帮助，感谢你们。</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1i6n4WxaYo2AFKF-1LXJSoPBtE9bOS38j/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1i6n4WxaYo2AFKF-1LXJSoPBtE9bOS38j/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1i6n4WxaYo2AFKF-1LXJSoPBtE9bOS38j/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1i6n4WxaYo2AFKF-1LXJSoPBtE9bOS38j/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">20250228standsample.rar</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2025-04-19 17:00 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> maybe someone at your company knows?</p>

---

## Post #3 by @jamesobutler (2025-04-19 20:40 UTC)

<p>Yes, Revvity InVivo imaging is developing a Slicer custom application that can load Vox files from our Quantum microCT instruments including our latest <a href="https://www.revvity.com/product/quantum-gx3-microct-system-cls158459" rel="noopener nofollow ugc">Quantum GX3</a>. As of right now, this application is currently unavailable.</p>
<p>The Quantum software has a viewer that can read the Vox files and export to dicom, but unfortunately it sounds like you do not currently have access to it.</p>
<p>It is great to hear that folks are interested in a solution to read the Vox files. I can ask about open-sourcing our reader to provide to the 3D Slicer community. The open source community has developed the <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess" rel="noopener nofollow ugc">RawImageGuess</a> extension which can be used to guess parameters to read any file format.</p>

---

## Post #4 by @muratmaga (2025-04-19 20:53 UTC)

<p>It is actually fairly easy to read this data into Slicer via the RawImageGuess. The vif file provides image dimension (512^3), data type appears to be 16 bit unsigned. There is some kind of byte offset (480) seemed to work for me.</p>
<p>If the vif file contained explicitly those values (data type, offset and spacing), we could implement an imported module like we have for GE scanners in SlicerMorph: <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/GEVolImport/GEVolImport.py" class="inline-onebox" rel="noopener nofollow ugc">SlicerMorph/GEVolImport/GEVolImport.py at master · SlicerMorph/SlicerMorph · GitHub</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d622fcb2122bdd6531c7920351e2999edacf6e52.jpeg" data-download-href="/uploads/short-url/uyl8z92RFwDuQo9MZ1ENYoxRdpE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d622fcb2122bdd6531c7920351e2999edacf6e52_2_690x498.jpeg" alt="image" data-base62-sha1="uyl8z92RFwDuQo9MZ1ENYoxRdpE" width="690" height="498" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d622fcb2122bdd6531c7920351e2999edacf6e52_2_690x498.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d622fcb2122bdd6531c7920351e2999edacf6e52_2_1035x747.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d622fcb2122bdd6531c7920351e2999edacf6e52_2_1380x996.jpeg 2x" data-dominant-color="939194"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1697×1226 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @ggg (2025-04-19 21:00 UTC)

<p>Hi, my colleague said he can only give me VOX format. I also saw that there is an option to automatically convert to dicom format on the GX2 CT software, and there is also a dataviewer.exe that can view VOX when exporting data, but the data is not collected by it, so there is no way. Someone also told me that Dragonfly can open vox format. Vox is MagicaVoxel format, right? I also saw support for this format on a dragonfly support page, but I didn’t try it. Here is the link.</p><aside class="onebox allowlistedgeneric" data-onebox-src="http://www.theobjects.com/dragonfly/dfhelp/4-1/Content/Key%20Features/Supported%20File%20Formats.htm">
  <header class="source">

      <a href="http://www.theobjects.com/dragonfly/dfhelp/4-1/Content/Key%20Features/Supported%20File%20Formats.htm" target="_blank" rel="noopener nofollow ugc">theobjects.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="http://www.theobjects.com/dragonfly/dfhelp/4-1/Content/Key%20Features/Supported%20File%20Formats.htm" target="_blank" rel="noopener nofollow ugc">Supported File Formats</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @ggg (2025-04-19 21:01 UTC)

<p>Thanks. I’ll try it.</p>

---

## Post #7 by @ggg (2025-04-19 21:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adb579ac973e853ad8dbb1f872909d75424f06c7.jpeg" data-download-href="/uploads/short-url/oMHpvqOXn23uFnrTrch7kt11ZAP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adb579ac973e853ad8dbb1f872909d75424f06c7_2_690x374.jpeg" alt="image" data-base62-sha1="oMHpvqOXn23uFnrTrch7kt11ZAP" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adb579ac973e853ad8dbb1f872909d75424f06c7_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adb579ac973e853ad8dbb1f872909d75424f06c7_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adb579ac973e853ad8dbb1f872909d75424f06c7_2_1380x748.jpeg 2x" data-dominant-color="2C2C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1043 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92834fed5b429d0995d62b812404d37a15c0038a.png" data-download-href="/uploads/short-url/kU72Q5LdDf69Vpp3Xc1ROVz6bqO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92834fed5b429d0995d62b812404d37a15c0038a_2_643x500.png" alt="image" data-base62-sha1="kU72Q5LdDf69Vpp3Xc1ROVz6bqO" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92834fed5b429d0995d62b812404d37a15c0038a_2_643x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92834fed5b429d0995d62b812404d37a15c0038a_2_964x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92834fed5b429d0995d62b812404d37a15c0038a.png 2x" data-dominant-color="3E7D3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1264×982 70.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to open the vox format on ORS Dragonfly Pro 2021. It seems to be normal. There is also an option to export dicom, but there are only 4096 color ranges, 2 to the 12th power? Has it become 12-bit data? The exported dicom can also be opened and used in ctan, which is very strange.</p>

---

## Post #8 by @jamesobutler (2025-04-19 21:44 UTC)

<p>The Vox data is indeed 16 bit. The original Vox1999a file format was created by TeraRecon. The Quantum uses a superset of the format for Revvity (formerly PerkinElmer) that includes some extra metadata.</p>

---

## Post #9 by @ggg (2025-06-19 14:44 UTC)

<p>I found a software installation package QuantumGX_ImageAnalysis_Setup_V3.2.5.exe, which can solve my problem. In addition, thank you for your answer.</p>

---
