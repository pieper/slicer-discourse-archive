---
topic_id: 21475
title: "About Building The Netstim Extension"
date: 2022-01-15
url: https://discourse.slicer.org/t/21475
---

# About building the NetStim extension

**Topic ID**: 21475
**Date**: 2022-01-15
**URL**: https://discourse.slicer.org/t/about-building-the-netstim-extension/21475

---

## Post #1 by @Lin (2022-01-15 12:48 UTC)

<p>Operating system: win 10<br>
Slicer version: 4.13<br>
Expected behavior:  expect to build NetStim<br>
Actual behavior: failed<br>
Hi everyone, I am Dr. Lin. I have to seek for help here because I have been stuck in building of Slicer and extension for a month.<br>
I am interested in the new software Lead OR which is developed by the famous lead DBS team. Lead OR is part of the NetStim extension. So I first built Slicer from source, and Slicer can run without an error, and it seems standard functions and modules are installed. Then I built the NetStim extension according to instructions on its website. I also installed the SDK provided by our local Alpha Omega distributor. However, I can only see the NetStim extension, with Import Atlas, Lead OR, Stereotactic plan, Warp Drive modules, which is similar to the functions installed directly from the extension manager. The most important Alpha Omega module is missing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/b/b37e785721ae5d36fbb2669f2b5e153f476df9b5.png" data-download-href="/uploads/short-url/pBSqxDFyrDOxjR9ONOTTURT8tOl.png?dl=1" title="slicer-netstim" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b37e785721ae5d36fbb2669f2b5e153f476df9b5_2_690x431.png" alt="slicer-netstim" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b37e785721ae5d36fbb2669f2b5e153f476df9b5_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b37e785721ae5d36fbb2669f2b5e153f476df9b5_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b37e785721ae5d36fbb2669f2b5e153f476df9b5_2_1380x862.png 2x" data-dominant-color="A5A6B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer-netstim</span><span class="informations">2560×1600 323 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We start Slicer using SlicerWithSlicerNetstim.exe, install depend extension(MarkupsToModel, SlicerRT), wrapDriver could be selected, but could not find the alphaomega entry.<br>
log shows " Cannot load library C:\D\E\NetstimReleaseWithAlphaomega\lib\Slicer-4.13\qt-loadable-modules\Release\qSlicerAlphaOmegaModule.dll"<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fd62f81d0553442dd95c296137cad388091563d.png" data-download-href="/uploads/short-url/mNYO71oDdot2Yr57PMhNHHRu8MZ.png?dl=1" title="alphaomega-couldnot-load" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fd62f81d0553442dd95c296137cad388091563d_2_690x342.png" alt="alphaomega-couldnot-load" data-base62-sha1="mNYO71oDdot2Yr57PMhNHHRu8MZ" width="690" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fd62f81d0553442dd95c296137cad388091563d_2_690x342.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fd62f81d0553442dd95c296137cad388091563d_2_1035x513.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fd62f81d0553442dd95c296137cad388091563d_2_1380x684.png 2x" data-dominant-color="111111"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">alphaomega-couldnot-load</span><span class="informations">1716×853 32.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We tried to rebuild the NetStim extension, with shorter folder path (C:\D\E\SNSR), but the error still exists when running SlicerWithSlicerNetstim.exe.<br>
Error(s):<br>
Cannot load library C:\D\E\SNSR\lib\Slicer-4.13\qt-loadable-modules\Release\qSlicerAlphaOmegaModule.dll</p>
<p>In the plugin modules dir, I get some dll files include qSlicerAlphaOmegaModule, Did I build alphaomega plugin correctly?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ea5a0da8d1b47956d6bd1c83b65b8b0eb3c45f.png" data-download-href="/uploads/short-url/rFsfnT9eG8cUW8rZBVFcLZY6utN.png?dl=1" title="slicernetstimalp(01-11-13-49-24)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1ea5a0da8d1b47956d6bd1c83b65b8b0eb3c45f_2_690x452.png" alt="slicernetstimalp(01-11-13-49-24)" data-base62-sha1="rFsfnT9eG8cUW8rZBVFcLZY6utN" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1ea5a0da8d1b47956d6bd1c83b65b8b0eb3c45f_2_690x452.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1ea5a0da8d1b47956d6bd1c83b65b8b0eb3c45f_2_1035x678.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ea5a0da8d1b47956d6bd1c83b65b8b0eb3c45f.png 2x" data-dominant-color="EFEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicernetstimalp(01-11-13-49-24)</span><span class="informations">1214×797 78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any suggestions for me on how to enable Alpha Omega function, or how to proceed from here?<br>
Thanks a lot!</p>

---

## Post #2 by @pieper (2022-01-15 18:30 UTC)

<p>I don’t think there are a lot of people who have experience building that particular extension  so you will probably need to ask the extension developers directly.  One thing you might try is to use <a href="https://docs.microsoft.com/en-us/sysinternals/downloads/procmon">Process Monitor</a> to track what it’s trying to access right before the error message.  It might be looking for another dependency that’s not in the path.  Otherwise it might perhaps be a locale issue if something in the path has non-latin characters.</p>

---

## Post #3 by @lassoan (2022-01-15 21:03 UTC)

<p>You need to manually enable building of the AlphaOmega module by uncommenting this line:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/netstim/SlicerNetstim/blob/a98391a8b5f2f088eed09e93f2a908c900de93b0/CMakeLists.txt#L23">
  <header class="source">

      <a href="https://github.com/netstim/SlicerNetstim/blob/a98391a8b5f2f088eed09e93f2a908c900de93b0/CMakeLists.txt#L23" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/netstim/SlicerNetstim/blob/a98391a8b5f2f088eed09e93f2a908c900de93b0/CMakeLists.txt#L23" target="_blank" rel="noopener">netstim/SlicerNetstim/blob/a98391a8b5f2f088eed09e93f2a908c900de93b0/CMakeLists.txt#L23</a></h4>



  <pre class="onebox">    <code class="lang-txt">
      <ol class="start lines" start="13" style="counter-reset: li-counter 12 ;">
          <li>set(EXTENSION_DEPENDS "NA") # Specified as a list or "NA" if no dependencies</li>
          <li>
          </li>
<li>#-----------------------------------------------------------------------------</li>
          <li># Extension dependencies</li>
          <li>find_package(Slicer REQUIRED)</li>
          <li>include(${Slicer_USE_FILE})</li>
          <li>
          </li>
<li>#-----------------------------------------------------------------------------</li>
          <li># Extension modules</li>
          <li>add_subdirectory(LeadOR)</li>
          <li class="selected">#add_subdirectory(AlphaOmega) # don't add for slicer</li>
          <li>add_subdirectory(StereotacticPlan)</li>
          <li>add_subdirectory(ImportAtlas)</li>
          <li>add_subdirectory(WarpDrive)</li>
          <li>add_subdirectory(NetstimPreferences)</li>
          <li>## NEXT_MODULE</li>
          <li>
          </li>
<li>#-----------------------------------------------------------------------------</li>
          <li>include(${Slicer_EXTENSION_GENERATE_CONFIG})</li>
          <li>include(${Slicer_EXTENSION_CPACK})</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Probably you have figured this out already, because you have the qSlicerAlphaOmegaModule.dll.</p>
<p>The module folder should only contain module DLLs. Third-party DLLs can go to the module’s <code>bin</code> folder in the install tree. In the build tree, you can make sure a third-party DLL (NeuroOmega_x64.dll) is found by copying it in the same folder as SlicerApp-real.exe (c:\D\S4R\Slicer-build\bin\Release).</p>
<p>Next week is <a href="https://projectweek.na-mic.org/PW36_2022_Virtual/">Slicer Project Week</a>. It is exactly for solving this kind of problems. I would recommend to contact Simon Oxenford <a class="mention" href="/u/simonoxen">@simonoxen</a> to see if he can help you during the week.</p>

---

## Post #4 by @simonoxen (2022-01-16 08:57 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a>. We’ve been in contact already and got to this point explained here. I suggested to post on discourse to get more suggestions. Wanted to comment this before but only read this now.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="21475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The module folder should only contain module DLLs. Third-party DLLs can go to the module’s <code>bin</code> folder in the install tree.</p>
</blockquote>
</aside>
<p>Thanks! perhaps this makes some kind of issue, I’ll fix it.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="21475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>One thing you might try is to use <a href="https://docs.microsoft.com/en-us/sysinternals/downloads/procmon" rel="noopener nofollow ugc">Process Monitor </a> to track what it’s trying to access right before the error message. It might be looking for another dependency that’s not in the path. Otherwise it might perhaps be a locale issue if something in the path has non-latin characters.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lin">@Lin</a> This is a good pointer to try to debug on your side.</p>
<p>Thanks again!</p>

---

## Post #5 by @Lin (2022-01-16 10:47 UTC)

<p>Thank you all for taking your time to give suggestions and share experiences. The reason I am so interested in this is that I think the software is amazing. I’ll try your advice and get back to you soon. Thanks a lot.</p>

---

## Post #6 by @Lin (2022-01-16 15:59 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> We used Process Monitor to track all loading behaviors of Slicer, including lib, exe and dll files, see Fig 1.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/079a8d160de87cfe32b154610402eb0a50a77abb.jpeg" data-download-href="/uploads/short-url/15gsVmymaDTwR9ej4jILznJJcUP.jpeg?dl=1" title="capture_20220116233508419" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/079a8d160de87cfe32b154610402eb0a50a77abb_2_556x500.jpeg" alt="capture_20220116233508419" data-base62-sha1="15gsVmymaDTwR9ej4jILznJJcUP" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/079a8d160de87cfe32b154610402eb0a50a77abb_2_556x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/079a8d160de87cfe32b154610402eb0a50a77abb_2_834x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/079a8d160de87cfe32b154610402eb0a50a77abb.jpeg 2x" data-dominant-color="EEF0EC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture_20220116233508419</span><span class="informations">953×857 86.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Yes, We’ve uncommented the line in the CmakeList file.</p>
<p>We also dumped the alphaomega dll file. See the files here.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48c26d2c9f07399f29327d66bc09128577fd806e.jpeg" data-download-href="/uploads/short-url/anEVWMnoWOpYuGFHBxHEpozTCh0.jpeg?dl=1" title="capture_20220116234220658" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48c26d2c9f07399f29327d66bc09128577fd806e.jpeg" alt="capture_20220116234220658" data-base62-sha1="anEVWMnoWOpYuGFHBxHEpozTCh0" width="651" height="499" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">capture_20220116234220658</span><span class="informations">931×714 44.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
and log (<a href="http://stella2018.myqnapcloud.cn:5000/share.cgi?ssid=3e53ae7011b843b790cb4e722bb35101" rel="noopener nofollow ugc">http://stella2018.myqnapcloud.cn:5000/share.cgi?ssid=3e53ae7011b843b790cb4e722bb35101</a>)<br>
We compared the results from the monitor and the results from dep lip (dump), and found that these files were not load in the Slicer.<br>
api-ms-win-crt-heap-l1-1-0.dll<br>
api-ms-win-crt-runtime-l1-1-0.dll<br>
api-ms-win-crt-math-l1-1-0.dll<br>
api-ms-win-crt-string-l1-1-0.dll<br>
We confirmed that these dll files exist in the windows we are using. And we copies these files to the folder of Alpha Omega module, but the issue resumed.<br>
We are not sure why these files are not loaded, and whether it is responsible to my issue here. Just to let you know what we found, hope useful.<br>
Many thanks to you all! <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/simonoxen">@simonoxen</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #7 by @lassoan (2022-01-17 00:37 UTC)

<p>Many DLL loading errors can be discovered using Dependency Walker. Launch Dependency Walker using <code>Slicer.exe --launch path/to/depends.exe</code> and drag-and-drop the DLL that fails to load. Dependency walker was created before side-by-side assemblies existed, so there are always some false positives (api-ms-win-crt… and the like are usually false positives, you don’t need to worry about them).</p>
<p>If Dependency Walker does not uncover anything useful then you need to use sxstrace tool. See instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">here</a>.</p>

---

## Post #8 by @Lin (2022-01-22 23:09 UTC)

<p>Hi all, after a long time of moving back and forth, with the help of my two friends,  Alpha Omega module is finally installed. There was a package missing, which was Microsoft Visuala C++ 2019, redistributiable package. We installed it manually, then it finally got through. I can now connect to Neuro Omega, although I still do not know how to use the software.<br>
Thank you all for suggestions! <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/simonoxen">@simonoxen</a></p>
<p>BTW, is there any sort of specification manual or similar?</p>

---

## Post #9 by @simonoxen (2022-01-23 16:29 UTC)

<aside class="quote no-group" data-username="Lin" data-post="8" data-topic="21475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lin/48/15559_2.png" class="avatar"> Lin:</div>
<blockquote>
<p>BTW, is there any sort of specification manual or similar?</p>
</blockquote>
</aside>
<p>Still working on a demonstrative video and better documentation. There is some info on the repo and the manuscript.</p>

---

## Post #10 by @DaviGi (2024-02-06 09:23 UTC)

<p>Hi all,</p>
<p>thank you for writing this! I also tried to install the NetStim extension (I would like to use WarpDrive). I installed the extension from the developer tool but WarpDrive does not show up (Only Lead-OR, StereotacticPlan and ImportAtlas?</p>
<p>My version of Slicer is 5.6.1</p>
<p>Thank you in advance!<br>
Davide</p>

---

## Post #11 by @simonoxen (2024-02-06 16:09 UTC)

<p>Hi Davide,</p>
<p>what do you mean by <em>from the developer tool</em>?</p>
<p>You can install the extension from the Extensions Manager from within Slicer.</p>
<p>Hope it helps</p>
<p>Simon</p>

---

## Post #12 by @DaviGi (2024-02-25 19:58 UTC)

<p>Dear Simon,</p>
<p>thank you so much for your help - I have installed it! Basically, my issue is that when I normalise postoperative T1s to the MNI space sometimes the resection cavity sags (and for example regions that are resected appear to be preserved). I would like to use WarpDrive to correct for this on the postoperative normalised T1 and then apply the transformation to correct the postoperative cavity. I tried to use the postoperative normalised T1 as input but this is not possible, would you have any advice? I looked at the tutorial in YouTube but I could not find how to do this.</p>
<p>Thank you in advance!!</p>
<p>Davide</p>

---

## Post #13 by @simonoxen (2024-02-26 09:34 UTC)

<p>Hi Davide, could you describe a bit more the issue? How are you setting the inputs in WarpDrive? Are you getting an error?</p>
<p>Thanks,<br>
Simon</p>

---

## Post #14 by @DaviGi (2024-02-26 15:49 UTC)

<p>Dear Simon,</p>
<p>Thank you for your quick answer. Basically, I can open WarpDrive, but in ‘input displacement field’ it is not possible to input any nifti - meaning that is not possible to change ’none’ (if that is what is supposed to do, as I imagine that a first imaged has to be displaced to a second image)</p>
<p>Thank you again!<br>
Davide</p>

---

## Post #15 by @simonoxen (2024-02-27 07:52 UTC)

<p>Hi Davide,</p>
<p>what Slicer version are you using? WarpDrive used to have <em>input displacement field</em> label, now it is <em>input</em>. I suggest you update Slicer and the extension.</p>
<p>The input can be either:</p>
<ul>
<li>A volume</li>
<li>A grid transform. In this case the grid transform (normalization output) should ideally be set to transform another volume.</li>
</ul>
<p>The output is a grid transform. You can use this to transform the input volume or transform.</p>

---
