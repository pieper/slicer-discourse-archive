# New module: Extract Centerline (in SlicerVMTK extension)

**Topic ID**: 12117
**Date**: 2020-06-19
**URL**: https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117

---

## Post #1 by @lassoan (2020-06-19 16:45 UTC)

<p>We added a completely new module that makes vessel (or airway or any other tree structure) centerline extraction much faster, flexible, and robust. It can quickly extract a network, determine branch endpoints automatically, allows editing of endpoints, computing centerlines, branches, and quantitative metrics (radius, curvature, torsion, etc). The new “Extract Centerline” module is available in SlicerVMTK extension for latest Slicer-4.11 release (it replaces the old “Centerline Computation” module).</p>
<p>Video demonstrating vessel segmentation, centerline extraction, centerline curve editing, curved planar reformatting (straightening), branch extraction and quantification:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>

<p>The video uses these modules:</p>
<ul>
<li>SlicerVMTK extension (for “Extract Centerline” module)</li>
<li>SegmentEditorExtraEffects extension (for “Local threshold” Segment Editor effect)</li>
<li>Sandbox extension (for “Curved Planar Reformat” module)</li>
</ul>

---

## Post #2 by @Romeo_Guevara (2020-06-20 02:56 UTC)

<p>wonderful but the “sandbox” extension does not appear to me in the Slicer version 4.11.0 2020-06-17</p>

---

## Post #3 by @lassoan (2020-06-20 03:00 UTC)

<p>Sandbox extension shows up in Examples category. You only need that if you want to use the Curved Planar Reformatting module.</p>

---

## Post #4 by @Romeo_Guevara (2020-06-21 04:16 UTC)

<p>Fabulous, the “curved planar reformat” and “extract centerline” modules are the best, but there is some way to make the “fudicial” that are placed in the “curved planar reformat” be recognized or appear in the centerline of the segmentation ?, this in order to have more accurate measurements, as there are cases in which I need to perform the centerline from the lowest renal artery and for that I rely on the “curved planar reformat” but the fudicials do not appear in the centerline of the segmentation to be able to use the automatic centerline modules with branch recognition.</p>

---

## Post #5 by @lassoan (2020-06-21 16:59 UTC)

<p>These should be doable. Can you describe with a bit more details and sketches or screenshots about what exactly you would like to show and measure? Create a new topic.</p>

---

## Post #6 by @jguy-aiu (2020-07-02 18:09 UTC)

<p>I followed this video step by step and got stuck at making the centerline. I was unable to select a surface input in the Extract Centerline module. I believe it has something to do with the endpoints and centerline curve shown at <a href="https://youtu.be/yi07mjr3JeU?t=62" rel="noopener nofollow ugc">1:02</a>. Can anyone care to explain what step I’m missing? I’m using 3d Slicer 4.11.0-2020-06-27 on Windows 10 and I have MarkupsToModel, SegementEditorExtraEffects, and SlicerVMTK extentions installed.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b30ff185159f91e48ff8c6e30dd5f9eb2037c2cd.jpeg" data-download-href="/uploads/short-url/py3CNPw3yaxj6FTifWaso6LazKZ.jpeg?dl=1" title="greyed_endpoints.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b30ff185159f91e48ff8c6e30dd5f9eb2037c2cd_2_690x373.jpeg" alt="greyed_endpoints.PNG" data-base62-sha1="py3CNPw3yaxj6FTifWaso6LazKZ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b30ff185159f91e48ff8c6e30dd5f9eb2037c2cd_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b30ff185159f91e48ff8c6e30dd5f9eb2037c2cd_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b30ff185159f91e48ff8c6e30dd5f9eb2037c2cd_2_1380x746.jpeg 2x" data-dominant-color="808087"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">greyed_endpoints.PNG</span><span class="informations">1920×1040 336 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b62c77fc4f42feff6bd6d4acfdfe84219836da8.jpeg" data-download-href="/uploads/short-url/3UgwzuuPIzdEO2KUSlkNjJmWGQU.jpeg?dl=1" title="no_endpoints.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b62c77fc4f42feff6bd6d4acfdfe84219836da8_2_690x373.jpeg" alt="no_endpoints.PNG" data-base62-sha1="3UgwzuuPIzdEO2KUSlkNjJmWGQU" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b62c77fc4f42feff6bd6d4acfdfe84219836da8_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b62c77fc4f42feff6bd6d4acfdfe84219836da8_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b62c77fc4f42feff6bd6d4acfdfe84219836da8_2_1380x746.jpeg 2x" data-dominant-color="808087"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">no_endpoints.PNG</span><span class="informations">1920×1040 326 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db075b92a2b366e28ca7d432aca08e10447627d4.png" data-download-href="/uploads/short-url/vfCkrUoZGBXLoeYTw7jhjUtwwOE.png?dl=1" title="installed_extentions" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db075b92a2b366e28ca7d432aca08e10447627d4_2_690x376.png" alt="installed_extentions" data-base62-sha1="vfCkrUoZGBXLoeYTw7jhjUtwwOE" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db075b92a2b366e28ca7d432aca08e10447627d4_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db075b92a2b366e28ca7d432aca08e10447627d4_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db075b92a2b366e28ca7d432aca08e10447627d4_2_1380x752.png 2x" data-dominant-color="FAFBFC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">installed_extentions</span><span class="informations">1922×1049 68.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2020-07-02 18:54 UTC)

<p>I have been working on this module in the last couple of days. Please install the latest Slicer Preview Release (4.11.0-2020-06-30) and let me know if you run into any issues with this version.</p>

---

## Post #8 by @jguy-aiu (2020-07-06 17:01 UTC)

<p>I downloaded the 4.11.0-2020-07-04 preview release and now Extract Centerline is working as expected, thank you.</p>

---

## Post #9 by @Andreas (2020-07-07 19:14 UTC)

<p>Dear Mr. Lasso,<br>
I would like to have tested the newest module with the newest 3D-Slicer version (4.11.0), unfortunately the program keeps crashing immediately after starting. I have reinstalled it several times and tested it on different computers (Windows 10).<br>
I hope you can help me.</p>
<p>best regards</p>

---

## Post #10 by @lassoan (2020-07-07 19:15 UTC)

<p>Yes, sorry, today’s build is corrupted, it’ll be fixed by tomorrow. See more information and workaround here:</p>
<aside class="quote" data-post="2" data-topic="12424">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/issues-running-latest-preview-on-macos-windows-10/12424/2">Issues running latest preview on macOS/Windows 10</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Sure, you can access previous releases by specifying a date or number of days to go back. See details <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">here</a>. 
Good news: I can reproduce the problem, so it will be fixed by tomorrow.
  </blockquote>
</aside>


---

## Post #11 by @Andreas (2020-07-11 17:42 UTC)

<p>Thank you very much, I can now open the latest version of the 3D-Slicer (4.11.0), but I cannot load my CT-dataset with this version, although I do nothing else than with the stable version (4.10.2)</p>

---

## Post #12 by @lassoan (2020-07-11 17:57 UTC)

<p>Use the DICOM module to import and then load the CT. If it does not work then post the details (how did you try to load the data, what error message is displayed, etc) in a new topic.</p>

---

## Post #13 by @cherrygirl (2022-03-09 06:45 UTC)

<p>Excuse me, I have used this method to measure the vessel related morphology, and I feel it is very great. However, I have a question, does the radius measured here refer to the average radius of the vessel in this segment?</p>

---

## Post #14 by @lassoan (2022-03-13 05:48 UTC)

<p>I had a quick look at the code and it seems the radius in the “Centerline properties” table is computed as the mean of the maximum inscribed sphere radii in the branch.</p>

---

## Post #16 by @cherrygirl (2022-03-14 06:50 UTC)

<p>Thank you very much!</p>

---

## Post #17 by @tsinesh (2022-07-14 18:16 UTC)

<p>Hello to the community,</p>
<p>how are the “Curvature, Torsion, Tortuosity and StartPointPosition” defined in the “Extract Centerline” module? Which formula is the basis for the measured values?<br>
Unfortunately, I have not found this in my research.</p>
<p>Greetings<br>
Tamu</p>

---

## Post #18 by @lassoan (2022-07-14 19:31 UTC)

<p>These are all computed by VMTK library. You can find detailed description of all the algorithms in <a href="http://lantiga.github.io/media/AntigaPhDThesis.pdf">Luca Antiga’s PhD thesis</a>.</p>

---

## Post #20 by @mikbuch (2022-11-10 16:32 UTC)

<p>Hi, it seems that “Extract Centerline” has many more options than “Centerline Computation”. Is there a new/updated video available somewhere, presenting the functionalities, and a minimal use-case of the “Extract Centerline” module? I found only a video where “Centerline Computation” is used: <a href="https://youtu.be/caEuwJ7pCWs?t=137" class="inline-onebox" rel="noopener nofollow ugc">Vessel segmentation and centerline extraction using 3D Slicer and VMTK - YouTube</a> . I also asked this question in the section comments of the YouTube video as some people having similar problems may first find the video, then this post/message on the forum.</p>
<p>In short, my problem is that I have what seems like a legitimate segment, but I was unable to generate/extract a centerline.</p>

---

## Post #21 by @rbumm (2022-11-10 16:47 UTC)

<aside class="quote no-group" data-username="mikbuch" data-post="20" data-topic="12117">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mikbuch/48/17241_2.png" class="avatar"> mikbuch:</div>
<blockquote>
<p>Is there a new/updated video available somewhere</p>
</blockquote>
</aside>
<p>Yes, there is this good video showing the workflow which works fine:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-video-start-time="91s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU&amp;t=91s" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #22 by @mikbuch (2022-11-10 18:00 UTC)

<p>Thank you Rudolf. I followed the video and everything worked for my segment. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #23 by @Peter_Horvath (2022-11-11 17:27 UTC)

<p>Hi! I would like to use the vmtk library to extract centerline of airways. When I install the extension through the wizard, everything seems fine:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1719dc48c6d9109f7357fb968f372bf9d8433808.png" data-download-href="/uploads/short-url/3imo291O6VEDYXffqHDsRAG8cUE.png?dl=1" title="2022-11-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1719dc48c6d9109f7357fb968f372bf9d8433808_2_690x431.png" alt="2022-11-11" data-base62-sha1="3imo291O6VEDYXffqHDsRAG8cUE" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1719dc48c6d9109f7357fb968f372bf9d8433808_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1719dc48c6d9109f7357fb968f372bf9d8433808_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1719dc48c6d9109f7357fb968f372bf9d8433808_2_1380x862.png 2x" data-dominant-color="F5F7FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2022-11-11</span><span class="informations">1440×900 81.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, when I try to actualy use the module, the following happens:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26432f89492551a932fdf21f8ebad9057c84b989.png" data-download-href="/uploads/short-url/5su5uoaxpjPm2UxMa6ahneBQEbf.png?dl=1" title="2022-11-11 (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26432f89492551a932fdf21f8ebad9057c84b989_2_690x431.png" alt="2022-11-11 (1)" data-base62-sha1="5su5uoaxpjPm2UxMa6ahneBQEbf" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26432f89492551a932fdf21f8ebad9057c84b989_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26432f89492551a932fdf21f8ebad9057c84b989_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26432f89492551a932fdf21f8ebad9057c84b989_2_1380x862.png 2x" data-dominant-color="B3B3B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2022-11-11 (1)</span><span class="informations">1440×900 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I double-click the name of the extension, nothing happens. Same for the curve centerline extraction module. How can I load these modules? I have tried installing-deleting the modules and slicer itself, but it does not help.</p>

---

## Post #24 by @chir.set (2022-11-11 17:50 UTC)

<aside class="quote no-group" data-username="Peter_Horvath" data-post="23" data-topic="12117">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/peter_horvath/48/17295_2.png" class="avatar"> Peter_Horvath:</div>
<blockquote>
<p>Same for the curve centerline extraction module.</p>
</blockquote>
</aside>
<p>As for “Curve centerline extraction” module, it is a helper module, that combines and automates a segmentation process relative to an arbitrary curve, followed optionally by centerline extraction. It has a dependency  on ‘<a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" rel="noopener nofollow ugc">Slicer segmentation extra effects</a>’, that you should install separately from the ‘Extensions manager’.</p>
<p>Select ‘Centerline extraction’ module instead. If this one does not work, there’s another problem.</p>

---

## Post #25 by @Peter_Horvath (2022-11-11 19:27 UTC)

<p>Thank you, my bad. Centerline extraction works fine, and that is what I need.</p>

---

## Post #26 by @rbumm (2022-11-11 20:48 UTC)

<p>Set one point at the top of the trachea and autgenerate the others.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/987ad405dc37887303296f44fe1ba2ea22a33479.png" data-download-href="/uploads/short-url/lKTJuvJyrnIyO7cDWWeh6xvVEo1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/987ad405dc37887303296f44fe1ba2ea22a33479_2_690x309.png" alt="image" data-base62-sha1="lKTJuvJyrnIyO7cDWWeh6xvVEo1" width="690" height="309" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/987ad405dc37887303296f44fe1ba2ea22a33479_2_690x309.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/987ad405dc37887303296f44fe1ba2ea22a33479_2_1035x463.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/987ad405dc37887303296f44fe1ba2ea22a33479_2_1380x618.png 2x" data-dominant-color="B9BADC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1436×644 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Relatively easy</p>

---

## Post #27 by @Peter_Horvath (2022-11-11 20:51 UTC)

<p>Thanks, works as expected.</p>

---

## Post #28 by @lassoan (2023-03-22 16:24 UTC)

<p>4 posts were split to a new topic: <a href="/t/construct-a-model-of-coronaries-from-ccta-scans/28527">Construct a model of coronaries from CCTA scans</a></p>

---

## Post #29 by @Yuri_Cocati (2023-04-16 20:40 UTC)

<p>Hello everyone,</p>
<p>If anyone knows and can help me, I would like how the parameters (like torsion, curvature, radius, …) are obtained. For example, in this image, I applied Extract Centerline in the trachea, but the table with the parameters returned me just one value for each one. I did not understand if it is an average for the entire trachea or just the calculation of a specific region…</p>
<p>Thank you very much in advance</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfadb8498ed285b224b2902270b87897f93264ba.png" data-download-href="/uploads/short-url/rlFob1MzexsrrWufo7NG4qRG9EC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfadb8498ed285b224b2902270b87897f93264ba_2_690x292.png" alt="image" data-base62-sha1="rlFob1MzexsrrWufo7NG4qRG9EC" width="690" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfadb8498ed285b224b2902270b87897f93264ba_2_690x292.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfadb8498ed285b224b2902270b87897f93264ba_2_1035x438.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bfadb8498ed285b224b2902270b87897f93264ba_2_1380x584.png 2x" data-dominant-color="E1E2EC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1892×802 90 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #30 by @lassoan (2023-04-17 01:05 UTC)

<p>The values in the metrics table are summary statistics (one value is computed for each branch).</p>
<p>Radius, curvature, and torsion values are available as curve measurement data for each curve point. How would you like to use these values?</p>

---

## Post #31 by @Mudrika (2023-05-02 15:43 UTC)

<p>I have a similar query. I have a model of the aortic root dividing into the coronary arteries. I am able to calculate the parameters for the different centreline curves but is there any way to obtain these parameters for the whole geometry in the form of a contour where I can see the variation as a whole?</p>
<p>Thank you!</p>

---

## Post #32 by @lassoan (2023-05-02 19:05 UTC)

<p>What do you mean by the whole geometry? To the entire segmented tree?</p>
<p>What variation you would like to see? The radius, curvature, and torsion varies from point to point in a curve and you access these values in curve measurements. Radius is retrieved during centerline extraction; while torsion and curvature are computed from the curve on-the-fly.</p>
<p>Length and tortuosity only makes sense for a curve segment (a branch).</p>

---

## Post #33 by @Mudrika (2023-05-03 08:16 UTC)

<p>Yes, by the whole geometry I meant to say the whole segmented tree.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/619da8252e6a7072d19448de3f9f1d0400a518a9.jpeg" data-download-href="/uploads/short-url/dVy5KKtT6go9Lgl1KLZA73X5L8l.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/619da8252e6a7072d19448de3f9f1d0400a518a9_2_624x500.jpeg" alt="image" data-base62-sha1="dVy5KKtT6go9Lgl1KLZA73X5L8l" width="624" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/619da8252e6a7072d19448de3f9f1d0400a518a9_2_624x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/619da8252e6a7072d19448de3f9f1d0400a518a9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/619da8252e6a7072d19448de3f9f1d0400a518a9.jpeg 2x" data-dominant-color="F5F6F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">854×684 70.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This is taken from the article by Piccinelli <em>et al. <em>2009.</em></em></p>
<p>I want to obtain the variation in a similar way.</p>
<p>What I have done till now is: Imported my .vtp geometry and then the centerline extraction which creates a centerline model. For different centerline curves, I am able to see to the quantification in the tabular format but I want to study the variation in this format.</p>
<p>I hope, I am able to explain my problem!</p>
<p>Thank you!</p>

---

## Post #34 by @gdisalle (2023-06-30 15:12 UTC)

<p>Dear Mr. Lasso,<br>
How do I access the value of the curvature at a given point of the centerline? In the “curve measurements” section I can only see the mean and max curvature, which refer to the entire vessel. Thank you in advance.</p>

---

## Post #35 by @lassoan (2023-06-30 16:34 UTC)

<p>See this topic: <a href="https://discourse.slicer.org/t/exporting-curvature-data/23181" class="inline-onebox">Exporting Curvature Data</a></p>

---

## Post #36 by @Hamed_Yousefiroshan (2024-02-12 23:41 UTC)

<p>Hi, the new interface with the vertical segment editor looks nice, however, I am used to older versions where we could easily find MakeModeleffect and other effects. It would be appreciative if you put a new vid for this Centerline Exct module with the new editor. Thanks.</p>

---

## Post #37 by @lassoan (2024-02-13 05:29 UTC)

<p>Segmentations store labelmap and surface meshes and their content is synchronized in real-time, so times are long gone when you had to do manual export to models using Make model effect or Model maker module.</p>
<p>Once you segmented the vessels, you can go directly to Extract Centerline module and choose the segmentation as input.</p>
<p>There are several videos of this on [<a href="https://m.youtube.com/user/PerkLabResearch">https://m.youtube.com/user/PerkLabResearch</a>](our lab’s YouTube channel) and many more created by others. Can you send a couple of links to videos that you found to be so old that was hard to follow?</p>

---
