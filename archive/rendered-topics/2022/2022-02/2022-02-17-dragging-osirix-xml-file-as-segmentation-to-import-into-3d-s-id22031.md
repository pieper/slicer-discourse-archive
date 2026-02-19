---
topic_id: 22031
title: "Dragging Osirix Xml File As Segmentation To Import Into 3D S"
date: 2022-02-17
url: https://discourse.slicer.org/t/22031
---

# Dragging OsiriX xml file as segmentation to import into 3D slicer

**Topic ID**: 22031
**Date**: 2022-02-17
**URL**: https://discourse.slicer.org/t/dragging-osirix-xml-file-as-segmentation-to-import-into-3d-slicer/22031

---

## Post #1 by @tenzin_kunkyab (2022-02-17 20:43 UTC)

<p>I have a file with dicom images (CT volume) and xml as the segmentation (just one xml file), when I drag the whole file into the slicer, only dicom image is shown, I couldn’t get the xml segmentation to be imported.</p>
<p>I checked the data as well and there is only the CT volume. I would like to ask how can I import the xml file. Eventually I would like to convert it to nrrd segmentation file.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2022-02-17 23:06 UTC)

<p>If the DICOM module is active then all drag-and-dropped file goes right into the DICOM database. If you want to load non-DICOM data, for example OsiriX segmentation files then switch to a different module before drag-and-dropping the data.</p>

---

## Post #3 by @tenzin_kunkyab (2022-02-18 06:18 UTC)

<p>Hi Andras,</p>
<p>I did do that but didn’t work.</p>
<p>I have a folder that contains the CT volume and one xml file as well, I tried to drag the folder but it didnt show the segmentation, only the CT volume.</p>
<p>best<br>
Tenzin</p>

---

## Post #4 by @lassoan (2022-02-18 16:10 UTC)

<p>What software did you use for creating this segmentation?<br>
Can you provide an example? (upload it to somewhere and post the link here; make sure no patient information is included)</p>

---

## Post #5 by @tenzin_kunkyab (2022-02-18 19:09 UTC)

<p>Hi,</p>
<p>For sure, I believe the data is annonymized so hopefully its ok to upload here.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://wetransfer.com/downloads/ee9783fc35128330c29acc9a47fdd88a20220218190529/95c989">
  <header class="source">
      <img src="https://prod-cdn.wetransfer.net/packs/media/images/favicon-a34a7465.ico" class="site-icon" width="64" height="64">

      <a href="https://wetransfer.com/downloads/ee9783fc35128330c29acc9a47fdd88a20220218190529/95c989" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://prod-cdn.wetransfer.net/packs/media/images/wt-facebook-9db47080.png" class="thumbnail onebox-avatar" width="200" height="200">

<h3><a href="https://wetransfer.com/downloads/ee9783fc35128330c29acc9a47fdd88a20220218190529/95c989" target="_blank" rel="noopener nofollow ugc">3000566.000000-NA-03192/069.xml and 133 more files</a></h3>

  <p>134 files sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>the link will expire…</p>
<p>best<br>
Tenzin</p>

---

## Post #6 by @tenzin_kunkyab (2022-02-18 21:43 UTC)

<p>not sure about the software which they used.</p>
<p><a href="https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI" class="onebox" target="_blank" rel="noopener nofollow ugc">https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI</a></p>
<p>the dataset was from here.</p>

---

## Post #7 by @pieper (2022-02-18 21:52 UTC)

<p><a class="mention" href="/u/tenzin_kunkyab">@tenzin_kunkyab</a>: That data is famously hard to work with in its native form, but fortunately <a class="mention" href="/u/fedorov">@fedorov</a> has spent a lot of time making standard representations that are easy to work with in Slicer.  Please read this paper for details:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://aapm.onlinelibrary.wiley.com/doi/10.1002/mp.14445">
  <header class="source">
      <img src="https://aapm.onlinelibrary.wiley.com/favicon.ico" class="site-icon" width="48" height="48">

      <a href="https://aapm.onlinelibrary.wiley.com/doi/10.1002/mp.14445" target="_blank" rel="noopener">American Association of Physicists in Medicine (AAPM)</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:379/500;"><img src="https://aapm.onlinelibrary.wiley.com/cms/asset/3a89fc08-c7b5-434a-a8f9-29b3b4b8571d/mp.v47.11.cover.jpg" class="thumbnail" width="379" height="500"></div>

<h3><a href="https://aapm.onlinelibrary.wiley.com/doi/10.1002/mp.14445" target="_blank" rel="noopener">DICOM re‐encoding of volumetrically annotated Lung Imaging Database...</a></h3>

  <p>Purpose
The dataset contains annotations for lung nodules collected by the Lung Imaging Data Consortium and Image Database Resource Initiative (LIDC) stored as standard DICOM objects. The annotation...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @akmal871026 (2025-06-05 08:47 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>You said need to switch to a different module. May I know which module should use to drag xml file?</p>

---

## Post #9 by @lassoan (2025-06-05 15:07 UTC)

<p>It can be any module, the important thing is not to be in the DICOM module, because when you drag-and-drop files when the DICOM browser is shown and you have a mix of DICOM and non-DICOM files then I all the files may be attempted to be interpreted as DICOM.</p>
<p>To load OsiriX segmentation files, you can use the <code>Import OsiriX ROI</code> module (provided by <code>Sandbox</code> extension).</p>

---

## Post #10 by @akmal871026 (2025-06-05 15:34 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>I did. However, the file still cannot be loaded.</p>
<p>I did as below</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35efab361efc8c089632561690d3b7be9bf894ee.png" data-download-href="/uploads/short-url/7H8NdYq01P61yXHuF9N20tfxhyC.png?dl=1" title="Screenshot 2025-06-05 233011" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35efab361efc8c089632561690d3b7be9bf894ee_2_690x371.png" alt="Screenshot 2025-06-05 233011" data-base62-sha1="7H8NdYq01P61yXHuF9N20tfxhyC" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35efab361efc8c089632561690d3b7be9bf894ee_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35efab361efc8c089632561690d3b7be9bf894ee_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/35efab361efc8c089632561690d3b7be9bf894ee_2_1380x742.png 2x" data-dominant-color="DAD9D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-06-05 233011</span><span class="informations">1919×1034 73.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1b75246ca75874e28ffada6bd28ce86e8d4d348.png" data-download-href="/uploads/short-url/yujPKoCe53iVIiip2k3sKZjqq6I.png?dl=1" title="Screenshot 2025-06-05 233123" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b75246ca75874e28ffada6bd28ce86e8d4d348_2_690x370.png" alt="Screenshot 2025-06-05 233123" data-base62-sha1="yujPKoCe53iVIiip2k3sKZjqq6I" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b75246ca75874e28ffada6bd28ce86e8d4d348_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b75246ca75874e28ffada6bd28ce86e8d4d348_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1b75246ca75874e28ffada6bd28ce86e8d4d348_2_1380x740.png 2x" data-dominant-color="B7B6B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-06-05 233123</span><span class="informations">1919×1030 72.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The file as here: <a href="https://drive.google.com/drive/folders/1Rj5reDzavVmU3C3D0jZarqDfse9ygv-S?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1Rj5reDzavVmU3C3D0jZarqDfse9ygv-S?usp=sharing</a></p>

---

## Post #11 by @lassoan (2025-06-07 14:12 UTC)

<p>To load OsiriX segmentation files, you can use the <code>Import OsiriX ROI</code> module (provided by <code>Sandbox</code> extension). The module experimental (not many people use OsiriX, so it is not worth a lot of time investment to polish this feature), so it does not register a reader plugin and therefore instead of drag-and-drop you need use the module’s user interface.</p>

---
