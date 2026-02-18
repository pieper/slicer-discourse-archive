# Trying to export nrrd file segmentation to DICOM

**Topic ID**: 13375
**Date**: 2020-09-07
**URL**: https://discourse.slicer.org/t/trying-to-export-nrrd-file-segmentation-to-dicom/13375

---

## Post #1 by @Gabriel_T (2020-09-07 14:29 UTC)

<p>I am using version 4.11.0-2020-08-09<br>
I have converted some segmentation from numpy format to nrrd, I also converted my CT volume from numpy to nrrd, I am able to load them fine in slicer 3d, but I wanted to convert this to dicom format so that the segmentations as well as the CT can be read by dicom viewers.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a1280f89fcff032f379568ab41c8146a1bdcacd.jpeg" data-download-href="/uploads/short-url/jHrxaZoK99Fh4E5HzaMK67ynRc9.jpeg?dl=1" title="correct_loading" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a1280f89fcff032f379568ab41c8146a1bdcacd_2_690x379.jpeg" alt="correct_loading" data-base62-sha1="jHrxaZoK99Fh4E5HzaMK67ynRc9" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a1280f89fcff032f379568ab41c8146a1bdcacd_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a1280f89fcff032f379568ab41c8146a1bdcacd_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a1280f89fcff032f379568ab41c8146a1bdcacd_2_1380x758.jpeg 2x" data-dominant-color="7E808A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">correct_loading</span><span class="informations">2024×1113 390 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Seems like RTStruct is the only way or are there better ways to do this ?<br>
I tried to convert to dicom RTSTruct by following the steps below</p><aside class="quote quote-modified" data-post="2" data-topic="543">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/convert-image-and-segmentation-to-dicom/543/2">Convert image and segmentation to DICOM</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You are trying to convert nrrd files into a RT Structure Set using 3D Slicer?  By coincidence, I documented this procedure earlier today. 

Load all images. At time of load, click “Labelmap” checkbox for each structure
Go to Segmentation module
For “Active segmentation”, choose “Create new segmentation”
For each structure, repeat: 
4a) In “Export/Import segments”, choose structure, and import as labelmap
Click on one of the segments, and then click “Edit selected”
Set the “Master volume” to your…
  </blockquote>
</aside>

<p>But after I convert to RTStruct I get images that dont display any contours.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c0aacfa443ff795e43ad7312b4165746e70782d.jpeg" data-download-href="/uploads/short-url/mgpmbZwr7Vs46Wb53Wcw3itcYdD.jpeg?dl=1" title="radiant_view" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c0aacfa443ff795e43ad7312b4165746e70782d_2_689x463.jpeg" alt="radiant_view" data-base62-sha1="mgpmbZwr7Vs46Wb53Wcw3itcYdD" width="689" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c0aacfa443ff795e43ad7312b4165746e70782d_2_689x463.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c0aacfa443ff795e43ad7312b4165746e70782d_2_1033x694.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c0aacfa443ff795e43ad7312b4165746e70782d_2_1378x926.jpeg 2x" data-dominant-color="383737"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">radiant_view</span><span class="informations">2613×1757 292 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there something that I am doing wrong ?</p>

---

## Post #2 by @lassoan (2020-09-07 14:53 UTC)

<p>The RT structure set does not even show up in the series list in the screenshot. What viewer are you trying to use?</p>
<p>I would recommend to use DICOM Segmentation Object (instead of the archaic and very limited RT structure set). This option shows up after you install Quantitative reporting extension. For future reference, see list of supported DICOM information objects <a href="https://slicer.readthedocs.io/en/latest/user_guide/supported_data_formats.html">here</a>.</p>

---

## Post #3 by @Gabriel_T (2020-09-07 15:15 UTC)

<p>Thank you for the suggestion,</p>
<p>I was using RadiAnt DICOM Viewer to view the folder containing the exported dicom files and the RTstruct but for some reason the RTStruct doesnt show up.</p>
<p>When I try to export to DICOM Segmentation Object using the Quantitative reporting extension I get two errors. I had loaded the segmentation nrrd as label map and the primary CT volume is also an nrrd object.</p>
<p>Error 1 -<br>
Could not retrieve DICOM tag value from input parameter None<br>
Error 2 -<br>
Traceback (most recent call last):<br>
File “”, line 2, in <br>
File “C:/Users/gabri/AppData/Roaming/NA-MIC/Extensions-29335/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 350, in export<br>
exporter.export(exportable.directory, segFileName, metadata)<br>
File “C:/Users/gabri/AppData/Roaming/NA-MIC/Extensions-29335/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 499, in export<br>
absolutePaths=True)<br>
File “C:/Users/gabri/AppData/Roaming/NA-MIC/Extensions-29335/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 575, in getDICOMFileList<br>
instanceUIDs = volumeNode.GetAttribute(attributeName)<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetAttribute’</p>

---

## Post #4 by @lassoan (2020-09-07 15:17 UTC)

<p>You need to set the referenced image before you can export a DICOM Segmentation Object. To do this, you can go to Segment Editor module and choose the referenced image as Master volume. We’ll update the exporter to make this requirement more clear.</p>

---

## Post #5 by @Gabriel_T (2020-09-07 15:27 UTC)

<p>I had selected the CT volume as the master volume in segment editor<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/466f791b1763d34f1534de0e92888593a47df8f1.png" data-download-href="/uploads/short-url/a36fG4MbAJebou3Kxgasv6MM1CV.png?dl=1" title="segmenteditor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/466f791b1763d34f1534de0e92888593a47df8f1_2_690x204.png" alt="segmenteditor" data-base62-sha1="a36fG4MbAJebou3Kxgasv6MM1CV" width="690" height="204" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/466f791b1763d34f1534de0e92888593a47df8f1_2_690x204.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/466f791b1763d34f1534de0e92888593a47df8f1_2_1035x306.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/466f791b1763d34f1534de0e92888593a47df8f1_2_1380x408.png 2x" data-dominant-color="DDE6EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmenteditor</span><span class="informations">1885×558 86.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Below is the subject hierarchy, is this correct ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12853f71327b14034897e94af0267ae0198a02da.png" data-download-href="/uploads/short-url/2DQ4KtOOvukRI2YLqiFjOmQP0Jc.png?dl=1" title="hierarchy" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12853f71327b14034897e94af0267ae0198a02da_2_690x117.png" alt="hierarchy" data-base62-sha1="2DQ4KtOOvukRI2YLqiFjOmQP0Jc" width="690" height="117" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12853f71327b14034897e94af0267ae0198a02da_2_690x117.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12853f71327b14034897e94af0267ae0198a02da_2_1035x175.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12853f71327b14034897e94af0267ae0198a02da_2_1380x234.png 2x" data-dominant-color="F1F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">hierarchy</span><span class="informations">1886×321 62.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But when I export this using DICOM seg it gives the same two errors</p>

---

## Post #6 by @adamaji (2021-11-29 14:38 UTC)

<p>Sorry to bring back this old issue, but was there any success here? Was trying to do something similar (export seg from NRRD to DICOM) without success.</p>
<p>Following <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database" class="inline-onebox" rel="noopener nofollow ugc">DICOM — 3D Slicer documentation</a> and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-segmentation-to-dicom-segmentation-object" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> do not work – even when the seg has a reference volume set manually, there are some missing DICOM tags/node attributes which prevent the export from proceeding.</p>
<p>I assume since <a href="https://github.com/QIICR/QuantitativeReporting/issues/247" class="inline-onebox" rel="noopener nofollow ugc">Slicer SEG export is failing when reference volume is not DICOM · Issue #247 · QIICR/QuantitativeReporting · GitHub</a> is still open without comment there hasn’t been any movement in this regard?</p>

---

## Post #7 by @lassoan (2021-11-29 16:05 UTC)

<p>DICOM Segmentation Object export works well, it just complicated because of required cross-references between DICOM files.</p>
<p>If you use a recent Slicer Preview Release then you will get detailed error message about what steps were missed.</p>
<p>If you don’t export to existing DICOM studies but you make up new ones then you need to create the patients, studies, image series first and then associate this DICOM volume with the existing segmentation:</p>
<ul>
<li>Export the volume to the DICOM database and then load the volume from the DICOM database.</li>
<li>Drag-and-drop the segmentation under the loaded DICOM volume’s study.</li>
<li>Go to Segment Editor and set the loaded DICOM volume as source geometry (by clicking the Specify geometry button and selecting the loaded DICOM volume as “source geometry”)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbcf842ba0f6aa920ed742b569d0079a3e1a38f3.png" data-download-href="/uploads/short-url/zVCrH3zb9dwH2bvp648EwotrlaX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbcf842ba0f6aa920ed742b569d0079a3e1a38f3_2_486x500.png" alt="image" data-base62-sha1="zVCrH3zb9dwH2bvp648EwotrlaX" width="486" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbcf842ba0f6aa920ed742b569d0079a3e1a38f3_2_486x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbcf842ba0f6aa920ed742b569d0079a3e1a38f3_2_729x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbcf842ba0f6aa920ed742b569d0079a3e1a38f3_2_972x1000.png 2x" data-dominant-color="DBDAD9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1324×1362 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After this, you can export the segmentation as DICOM segmentation object by right-clicking on the segmentation node in Data module.</p>
<p>You can find a script here that fully automates this process (even takes care of assigning DICOM terminologies, in case someone is just converting plain labelmaps and not segmentation nodes): <a href="https://github.com/lassoan/LabelmapToDICOMSeg" class="inline-onebox">GitHub - lassoan/LabelmapToDICOMSeg: Script for converting labelmap volumes to DICOM segmentation objects</a></p>

---
