# Save new segmentation from PET/CT images

**Topic ID**: 8658
**Date**: 2019-10-03
**URL**: https://discourse.slicer.org/t/save-new-segmentation-from-pet-ct-images/8658

---

## Post #1 by @Nora (2019-10-03 11:46 UTC)

<p>Hi all,</p>
<p>I tried to segment and export it as DICOM following the stepts on that video (<a href="https://www.youtube.com/watch?v=nzWf4xHy1BM" rel="noopener nofollow ugc">Create DICOM files from CT volume and segmentation</a>). I can reopen it on 3D slicer. but I can’t use to on other software. I loss patient information (dose, weight, etc).</p>
<p>This how my saved file look like: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36df9e455534fe00c763da1f71f8dea67f4899a2.jpeg" data-download-href="/uploads/short-url/7PqSLlFsCT1ARnjbMiWJDRRLe82.jpeg?dl=1" title="06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36df9e455534fe00c763da1f71f8dea67f4899a2_2_500x500.jpeg" alt="06" data-base62-sha1="7PqSLlFsCT1ARnjbMiWJDRRLe82" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36df9e455534fe00c763da1f71f8dea67f4899a2_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36df9e455534fe00c763da1f71f8dea67f4899a2_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36df9e455534fe00c763da1f71f8dea67f4899a2_2_1000x1000.jpeg 2x" data-dominant-color="EAECEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">06</span><span class="informations">1266×1264 313 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>how I can maintain the image information for further analysis?<br>
Really appreciate your help .</p>
<p>Cheers,</p>

---

## Post #2 by @lassoan (2019-10-03 13:17 UTC)

<p>You don’t need to save all the patient information into the exported DICOM series that you had in the original study. You can set some of the most commonly used fields in the DICOM export dialog.</p>
<p>How do you export the segmentation? As RT structure set or as DICOM segmentation object? What do you do with the exported DICOM files?</p>

---

## Post #3 by @Nora (2019-10-03 14:32 UTC)

<p>Hi Andras,</p>
<p>My apologies for my very basic questions. Really admire your quick reply.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="8658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How do you export the segmentation? As RT structure set or as DICOM segmentation object?</p>
</blockquote>
</aside>
<p>This is what I did:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2460a70ceb0e26caee6d7599f4b7f1d4c01cb89e.png" data-download-href="/uploads/short-url/5bOguH9krSIIXvtUTU1KveBDMnQ.png?dl=1" title="00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2460a70ceb0e26caee6d7599f4b7f1d4c01cb89e_2_690x273.png" alt="00" data-base62-sha1="5bOguH9krSIIXvtUTU1KveBDMnQ" width="690" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2460a70ceb0e26caee6d7599f4b7f1d4c01cb89e_2_690x273.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2460a70ceb0e26caee6d7599f4b7f1d4c01cb89e_2_1035x409.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2460a70ceb0e26caee6d7599f4b7f1d4c01cb89e.png 2x" data-dominant-color="E0E9EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">00</span><span class="informations">1096×434 42.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d33c729e9848af5e039908c75af0231974f6d5e4.png" data-download-href="/uploads/short-url/u8GfNXYqFELJsZUGLOLLhK2Ayqg.png?dl=1" title="21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d33c729e9848af5e039908c75af0231974f6d5e4_2_690x331.png" alt="21" data-base62-sha1="u8GfNXYqFELJsZUGLOLLhK2Ayqg" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d33c729e9848af5e039908c75af0231974f6d5e4_2_690x331.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d33c729e9848af5e039908c75af0231974f6d5e4_2_1035x496.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d33c729e9848af5e039908c75af0231974f6d5e4.png 2x" data-dominant-color="E3EBF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">21</span><span class="informations">1114×536 70.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="8658">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What do you do with the exported DICOM files?</p>
</blockquote>
</aside>
<p>I tried to do lots of things:</p>
<p>1- to apply radiomics extension to extarct some features in 3D slicer.<br>
but I got an empty table:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5e3ba6a4edd98f3fca7fed7911280b206ab0cda.png" alt="45" data-base62-sha1="nFwGEHV94ERTCT34XtaeMNOtPsK" width="652" height="472"></p>
<p>2- Then I tried to upload the file in LIFEx to see if it works there. It gave me an error.</p>
<p>3- I tried also to use the pyradiomics open source on python. but it won’t go through.</p>

---

## Post #4 by @lassoan (2019-10-03 14:42 UTC)

<p>You can use SlicerRadiomics in Slicer to compute radiomics features, you don’t need DICOM export for this. If you have problems with SlicerRadiomics then describe that in detail in a new forum topic.</p>
<p>If the problem is that some software cannot read the DICOM files exported by Slicer then report the error to the maintainer of that software or give us more information about the error you get there. It should not matter what optional study information is included in the exported DICOM files.</p>

---

## Post #5 by @JoostJM (2019-10-11 08:31 UTC)

<p><a class="mention" href="/u/nora">@Nora</a>,<br>
It looks to me you tried to extract the features using the SlicerRadiomics extension, but did not get any results.</p>
<p>When this happens, PyRadiomics (working as the backend for SlicerRadiomics) should report why it is not giving you any results. This is included in the logging of Slicer. Can you share the log? You can do so via Help&gt;&gt;Report A Bug</p>

---
