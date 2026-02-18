# Import OsiriX ROI as segmentation

**Topic ID**: 10719
**Date**: 2020-03-17
**URL**: https://discourse.slicer.org/t/import-osirix-roi-as-segmentation/10719

---

## Post #1 by @esrasmr (2020-03-17 14:10 UTC)

<p>Hello,<br>
I have ima files and their segmentation data as xml / rois_seris file formats. How can I import segmentations to 3D Slicer and create 3D models out of them? Are these file formats supported in the segmentation module?<br>
Thanks,</p>

---

## Post #2 by @pieper (2020-03-18 00:28 UTC)

<p>I’m not familiar with those formats.  Any of the volume or model formats can be used to represent segmentations.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat</a></p>

---

## Post #3 by @esrasmr (2020-03-23 09:20 UTC)

<p>Thank you for reply,<br>
However, I could not import xml and rois_series segmentations into 3D Slicer. The segmentations that I want to import  were created using Osirix. 3D Slicer doesn’t respond to these data. Is there any suggestions that I can implement to solve this problem.<br>
Thank you !</p>

---

## Post #4 by @lassoan (2020-03-23 14:36 UTC)

<p>Segmentation format of Osirix is really, really bad. I don’t know if the choice of proprietary file format and poor design is intentional (to lock in users so that they can only Osirix) or just for historical reasons, but anyway, the end result is that it is really hard to export the ROIs from Osirix. If you paid for Osirix then I would recommend to ask them that they provide segmentation export tools (e.g., to standard DICOM segmentation object).</p>
<p>There has been an attempt to write an importer module for Slicer, based on reverse engineering of native Osirix ROI files - see here: <a href="https://github.com/VASST/SlicerOsirix">https://github.com/VASST/SlicerOsirix</a>. <a class="mention" href="/u/adamrankin">@adamrankin</a> what’s the status of this extension? What can it do and what are its limitations?</p>

---

## Post #5 by @esrasmr (2020-03-23 20:50 UTC)

<p>Thank you for your quick reply, I will try your suggestion to solve the problem.</p>

---

## Post #6 by @lassoan (2020-03-24 00:58 UTC)

<p>SlicerOsirix extension seems to be just an empty placeholder extension.</p>
<p>However, I gave it a try and was able to create a simple module to import OsiriX ROI to segmentation. It will be available for download tomorrow for Slicer Preview Release, in Sandbox extension. The module name is “Import OsiriX ROI”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a00ff25ed54d64508bb14aa3790f2dc35afd0aec.png" data-download-href="/uploads/short-url/mPYyMF6XdoRdGGUw0ic7nAafa7G.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a00ff25ed54d64508bb14aa3790f2dc35afd0aec_2_690x406.png" alt="image" data-base62-sha1="mPYyMF6XdoRdGGUw0ic7nAafa7G" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a00ff25ed54d64508bb14aa3790f2dc35afd0aec_2_690x406.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a00ff25ed54d64508bb14aa3790f2dc35afd0aec_2_1035x609.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a00ff25ed54d64508bb14aa3790f2dc35afd0aec_2_1380x812.png 2x" data-dominant-color="B2AFB1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2011×1186 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Give it a try and let me know if it works for you.</p>

---

## Post #7 by @esrasmr (2020-03-24 12:17 UTC)

<p>That is great, thank you for your help. I will try and give feedback to you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #8 by @esrasmr (2020-03-25 11:57 UTC)

<p>Hello Dr Lasso,<br>
I have installed and tried your module but acceptable input data type is just *json. I tried to convert xml file to json however ‘import OsiriX ROI module’ gave an error.</p>

---

## Post #9 by @lassoan (2020-03-25 12:34 UTC)

<p>Could you please upload the xml and json file to somewhere (Dropbox, OneDrive, Google drive) and post the link?</p>

---

## Post #11 by @lassoan (2020-03-25 15:36 UTC)

<p>Thank you, I’ve added code to parse XML files, too. I’ve only tested it with the data set you provided. You can get it from the extension manager tomorrow or download the updated file from <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ImportOsirixROI/ImportOsirixROI.py">here</a>.</p>

---

## Post #12 by @sfat (2023-12-11 08:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Sorry mate, I’m badly stuck for the past week trying to load Osirix xml to slicer. I know that because of the update to plistlib , the xml loading functionality seem to have stopped working in the sandbox extension. I’ve tried converting the file to json and then importing it using sandbox extension, but it just crashes 3dSlicer, so I don’t get to see what causes the error. I’m using slicer on linux<br>
I’ve tried writing my own code to just read the xml file and convert it to a mask with some success but the mask’s proportion is completely off.<br>
Any chance you could look at the extension and see if you can revive it ?</p>

---

## Post #13 by @lassoan (2023-12-11 13:24 UTC)

<p>Please provide an example file that does not load and I’ll investigate.</p>

---

## Post #14 by @sfat (2023-12-11 22:48 UTC)

<p>Thank you . i’ve attached the original xml and converted json</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://wetransfer.com/downloads/4de1abb66ea354119609530f9878486f20231211224741/cd88d7">
  <header class="source">
      <img src="https://wetransfer.com/favicon.ico" class="site-icon" width="" height="">

      <a href="https://wetransfer.com/downloads/4de1abb66ea354119609530f9878486f20231211224741/cd88d7" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://wetransfer.com/downloads/4de1abb66ea354119609530f9878486f20231211224741/cd88d7" target="_blank" rel="noopener nofollow ugc">example.zip</a></h3>

  <p>1 file sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #15 by @lassoan (2023-12-12 04:13 UTC)

<p>I’ve made the Osirix ROI importer module more robust in latest Slicer Preview Release, so there should be no more errors.</p>
<p>However, for the example data set you provided there are some warnings because contours are missing on some frames.</p>

---

## Post #16 by @sfat (2023-12-12 04:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="10719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>wever, for the example data set you provided there are some warnings because contours are missing on some frames.</p>
</blockquote>
</aside>
<p>That’s great ! I will switch to preview release ! really appreciate it</p>

---

## Post #17 by @lassoan (2023-12-12 04:43 UTC)

<p>The updated extension will be available in the next Slicer Preview Release build (that you can download in about 10 hours).</p>

---

## Post #18 by @sfat (2023-12-12 22:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="10719">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Osirix ROI importer module</p>
</blockquote>
</aside>
<p>So I’m assuming the importer module is the one in Sandbox extension; I’ve downloaded the latest preview release, and added the sandbox extension, restarted the app; When i try to load the xml file I get the package error again : “Import failed: module ‘plistlib’ has no attribute ‘readPlist’”. Any thoughts ?</p>

---

## Post #19 by @lassoan (2023-12-12 23:04 UTC)

<p>It seems that no new Slicer Preview Release was built last night (probably because the new 5.6.1 patch release was being prepared) so the extension update is not yet available for the latest Slicer Preview Release.</p>
<p>The good news is that in the meantime a new Slicer Stable Release was created, so you can now use that. If you install Slicer-5.6.1 and thr Sandbox extension then it will include the fix.</p>
<p>The missing contours may cause problems - if you find that the contours are not aligned with the underlying image then let me know. I can tune the behavior further but then I’ll need the input image, too (you can save the image as NRRD to remove all patient information from the image).</p>

---

## Post #20 by @sfat (2023-12-13 00:53 UTC)

<p>Looks good so far, contours are aligned correctly . They come out like this though which is likely due to missing contours ?<br>
Would it cause a problem when training with MONAI ?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07d325f70037d8cda4ef8ead61c40d06d7254373.png" alt="Screenshot from 2023-12-13 11-50-54" data-base62-sha1="17dIYADZ9YrCWAyW43Q9eLv0FYT" width="582" height="412"></p>

---

## Post #21 by @lassoan (2023-12-13 01:31 UTC)

<p>MONAILabel requires labelmap representation, which probably need to have the same geometry as the input image. So, I would recommend to load the input image, choose as source volume in Segment Editor module, and review and touch up the segmentation as needed.</p>

---
