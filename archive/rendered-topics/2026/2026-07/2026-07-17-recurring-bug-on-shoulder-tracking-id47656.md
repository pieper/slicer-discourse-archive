---
topic_id: 47656
title: "Recurring bug on Shoulder tracking"
date: 2026-07-17
url: https://discourse.slicer.org/t/47656
last_bumped: 2026-08-27T16:13:35.568Z
---

# Recurring bug on Shoulder tracking

**Topic ID**: 47656
**Date**: 2026-07-17
**URL**: https://discourse.slicer.org/t/recurring-bug-on-shoulder-tracking/47656

---

## Post #1 by @AlonsoFigueroa (2026-07-17 13:14 UTC)

<p>Hello SAM team,</p>
<p>We are encountering an issue while tracking a scapula in Autoscoper during an arm elevation task.</p>
<p>For one participant, Autoscoper consistently crashes when saving frames within specific ranges of motion. The crash occurs during tracking of the shoulder/scapula and is reproducible across multiple trials. We have attempted to process the same participant data on different computers and obtained the same result each time.</p>
<p>I found an older issue that appears to describe a very similar problem, although it does not seem to have been resolved:</p>
<p><a href="https://github.com/BrownBiomechanics/Autoscoper/issues/305" rel="noopener nofollow ugc">BrownBiomechanics/Autoscoper#305</a></p>
<p>System information:</p>
<p>3D Slicer version: 5.10.1<br>
Operating System: Windows<br>
GPU: NVIDIA RTX 3080 Ti</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cb90a5436921c99d7fcd2f5cf8672ebc0338cfc.gif" alt="Adobe Express - 2026-07-09_15-41-23" data-base62-sha1="6nDsg9GlDl8T0RCDrHwJ6aTYUs4" width="422" height="226" class="animated"></p>

---

## Post #2 by @John_Holtgrewe (2026-07-17 15:03 UTC)

<p>Hi Alonso,</p>
<p>Thanks for bringing this to our attention. My experience with SAM is limited to tracking the femur and tibia, and I have not encountered this issue. However, I know that other groups have used SAM to successfully track the scapula. <a class="mention" href="/u/cesar">@Cesar</a> Did you have this issue with any of your data?</p>
<p>Does this happen when processing data from other participants, or just this one?</p>

---

## Post #3 by @Cesar (2026-07-17 17:53 UTC)

<p>I remember running into a similar issue while using the optimization feature, but it was fixed fairly quickly. I haven’t seen this specific problem before. I wonder if the graphics card could be causing the crash. Alonso, are you running SAM on a remote computer?</p>

---

## Post #4 by @AlonsoFigueroa (2026-07-17 20:46 UTC)

<p>Hello Cesar and John,</p>
<p>Thank you for taking the time to investigate this issue.</p>
<p>We are currently running SAM on a local workstation. We’ve tested multiple computers and several different subjects, and it appears that approximately half of the subjects we upload to SAM encounter this issue.</p>
<p>The workstations we have been using for these trials have the following specifications:</p>
<ul>
<li>Dell Precision 5860</li>
<li>Intel Xeon W3-2423</li>
<li>NVIDIA RTX 3080 Ti</li>
</ul>
<p>I’d be happy to share the files with your team if you’d like to investigate further. However, the image files are too large to upload through this platform. Please let me know the best way to transfer them, and I’ll send them over.</p>

---

## Post #5 by @AlonsoFigueroa (2026-07-29 19:21 UTC)

<p>Hi <a class="mention" href="/u/john_holtgrewe">@John_Holtgrewe</a>,  I wanted to provide a brief update on the Autoscoper-CUDA crashes we previously reported. We have now reproduced the issue with multiple scapular models from different patients and CT scans. The crash is also reproducible across several computers with different hardware configurations, including RTX 3080 and 3080 Ti GPUs, different Intel processors, and at least 64 GB of RAM. This suggests that the issue is not isolated to a particular dataset or workstation.</p>
<p>Further testing suggests that the crash may be related to the size or extent of the scapular model. If we crop the model to approximately half of the scapula, excluding the inferior portion, the crash no longer occurs. However, this is not a practical solution for our application because excluding the inferior scapula removes landmarks that we use for tracking and reduces the reliability and capability of the autotracking function.</p>
<p>We have also been investigating the source of the crash on our side and have found the following:</p>
<p>Windows Reliability Monitor initially reported exception code <code>0xc0000409</code> in <code>ucrtbase.dll</code>. We therefore configured Windows Error Reporting to capture a full crash dump and analyzed it with WinDbg. The dump indicates that, following the relevant button click in Autoscoper, the application throws an unhandled native C++ exception (<code>0xe06d7363</code>). The C++ runtime then calls <code>terminate()</code> and <code>abort()</code>, producing the final <code>FAST_FAIL_FATAL_APP_EXIT</code> (<code>0xc0000409</code>). The first identifiable Autoscoper frame is <code>autoscoper-CUDA+0x660c7</code>, but without the corresponding debug symbols we cannot resolve it to a specific function.</p>
<p>I can provide the complete WinDbg output, crash dump, and additional reproduction details if helpful.</p>

---

## Post #6 by @mikebind (2026-07-30 17:38 UTC)

<p>I’m not familiar with AutoScoper, but it sounds from your troubleshooting like the scapula model may just have too many points for the processing occurring and the memory problems are leading to the crash (running out of memory is probably the most common reason for Slicer crashes).  For models, the typical best solution is decimation.  For models with a high density of points, you can often reduce the number of points very dramatically (&gt;90%) without much loss of detail.  So, rather than cropping, perhaps you can decimate the model to stay within memory limits. Interactively, you can do this using the SurfaceToolbox module, and it is also possible via python/VTK if it needs to be integrated into the workflow more deeply.</p>

---

## Post #7 by @John_Holtgrewe (2026-08-07 18:01 UTC)

<p>Hi Alonso,</p>
<p>I apologize for just now getting back to you. The size of the volumes possibly causing the crash is interesting. We have only worked with relatively smaller volumes (distal end of the femur and proximal end of tibia). Could you share the following details about the volumes that you are trying to load in: dimensions of the tiff stack (including number of slices), voxel size, and file size?</p>
<p>Yes, any additional reproduction details you can provide will be helpful with documenting this issue.</p>
<p>Thanks!</p>
<p>John</p>

---

## Post #8 by @AlonsoFigueroa (2026-08-10 15:32 UTC)

<p>Hello John,</p>
<p>Thank you so much for getting back to us.</p>
<p>We followed <a class="mention" href="/u/mikebind">@mikebind</a>  advice and decimated both the STL models and the TIFF stacks, but unfortunately, the issue persists. Thank you as well, Mike, we’ll report back as soon as we resolve it. I am adding the details of the data that we are using, but I am happy to share the volumes and images if you’d like.</p>
<p>Please find the details of our data below:</p>
<p><strong>Original CT scan</strong></p>
<ul>
<li>Dimensions: 512 × 512 × 411</li>
<li>Voxel spacing: 0.48828125 × 0.48828125 × 0.6 mm</li>
</ul>
<p><strong>X-ray images</strong></p>
<ul>
<li>File size: 2 MB per frame</li>
<li>Bit depth: 16-bit</li>
<li>Dimensions: 1024 × 1024</li>
</ul>
<p><strong>Scapula</strong></p>
<ul>
<li>TIFF: 20.5 MB; 229 × 239 × 241; VoxelSize 0.488 0.488 0.6; 16-bit</li>
<li>STL: 16.2 MB; 231,301 vertices</li>
</ul>
<p><strong>Clavicle</strong></p>
<ul>
<li>TIFF: 715 KB; 328 × 166 × 80; VoxelSize 0.488 0.488 0.6; 16-bit</li>
<li>STL: 5.3 MB; 94,912 vertices</li>
</ul>
<p><strong>Humerus</strong></p>
<ul>
<li>TIFF: 2 MB; 110 × 140 × 285; VoxelSize 0.488 0.488 0.6; 16-bit</li>
<li>STL: 9.3 MB; 94,912 vertices</li>
</ul>

---

## Post #9 by @John_Holtgrewe (2026-08-13 13:58 UTC)

<p>If you could share the volumes and images, just so I could replicate the issue on my end, that would be helpful. Your scapula volume is quite a bit bigger than our femur and tibia volumes, so we don’t have anything comparable to test.</p>
<p><a class="mention" href="/u/cesar">@Cesar</a> Can you comment on how the size of their volumes compares to the scapula volumes that you have tracked previously?</p>
<p>We currently have limited ability to address bugs in the software; however, we do have a student who will be joining us to specifically work on SlicerAutoscoper, and bug fixes (with this one as a priority) are at the top of the list for things to work on.</p>

---

## Post #11 by @AlonsoFigueroa (2026-08-17 15:49 UTC)

<p>Happy to share the volumes and images with your team. However, I think the folders are larger than what can be uploaded to Discourse, What would be your best alternative to share the data with you?</p>

---

## Post #13 by @John_Holtgrewe (2026-08-21 14:08 UTC)

<p><a class="mention" href="/u/alonsofigueroa">@AlonsoFigueroa</a>  I totally missed that you had shared the files on GitHub, so I was able to download them from there.</p>

---

## Post #14 by @John_Holtgrewe (2026-08-27 14:09 UTC)

<p>Hi <a class="mention" href="/u/alonsofigueroa">@AlonsoFigueroa</a> ,</p>
<p>Could you share a subset of the radiograph images for trial you are trying to track the scapula in (just 5-10 frames)? You can add them to the issue in Github, or if the files are too large we can figure something else out.</p>
<p>Thanks!</p>
<p>John</p>

---

## Post #15 by @AlonsoFigueroa (2026-08-27 16:13 UTC)

<p>Hi <a class="mention" href="/u/john_holtgrewe">@John_Holtgrewe</a></p>
<p>Thank you for continuing to investigate this issue. I’m glad you were able to download the files from GitHub.</p>
<p>We have assembled a dataset from a trial that consistently crashes. The dataset contains 10 continuous frames. On our systems, the first five frames track successfully, while the second half of the video causes the software to crash.</p>
<p>Unfortunately, I was unable to upload the files directly to this thread. However, the cropped trials have now been uploaded to the GitHub issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/BrownBiomechanics/SlicerAutoscoperM/issues/195">
  <header class="source">

      <a href="https://github.com/BrownBiomechanics/SlicerAutoscoperM/issues/195" target="_blank" rel="noopener nofollow ugc">github.com/BrownBiomechanics/SlicerAutoscoperM</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/BrownBiomechanics/SlicerAutoscoperM/issues/195" target="_blank" rel="noopener nofollow ugc">Autoscoper crashing when saving specific scapular ROM</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-07-09" data-time="21:13:11" data-timezone="UTC">09:13PM - 09 Jul 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/Alonso-Figueroa" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/301858893?v=4" class="onebox-avatar-inline" width="20" height="20">
          Alonso-Figueroa
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hello SAM team,

We are encountering an issue while tracking a scapula in Autosc<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">oper during an arm elevation task.

For one participant, Autoscoper consistently crashes when saving frames within specific ranges of motion. The crash occurs during tracking of the shoulder/scapula and is reproducible across multiple trials. We have attempted to process the same participant data on different computers and obtained the same result each time.

I found an older issue that appears to describe a very similar problem, although it does not seem to have been resolved:

https://github.com/BrownBiomechanics/Autoscoper/issues/305

System information:

3D Slicer version: 5.10.1
Operating System: Windows
GPU: NVIDIA RTX 3080 Ti

[Config Files.zip](https://github.com/user-attachments/files/29865648/Config.Files.zip)
[Video-evidence.zip](https://github.com/user-attachments/files/29865651/Video-evidence.zip)
[Maya Cams.zip](https://github.com/user-attachments/files/29865650/Maya.Cams.zip)
[Tracking Files.zip](https://github.com/user-attachments/files/29865649/Tracking.Files.zip)
[Volumes.zip](https://github.com/user-attachments/files/29865731/Volumes.zip)

(Image data is to large to upload in this post, I am happy to share these images)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’m also bringing <a class="mention" href="/u/sydney.wheaton">@sydney.wheaton</a>  into the conversation. Sydney is our research engineer who focuses on shoulder-related projects and has the most experience with this issue. If you have any specific questions about the crashes, she will be able to provide additional details and insight.</p>

---
