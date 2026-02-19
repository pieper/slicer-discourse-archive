---
topic_id: 5997
title: "Segmentation Scissors"
date: 2019-03-02
url: https://discourse.slicer.org/t/5997
---

# segmentation: scissors

**Topic ID**: 5997
**Date**: 2019-03-02
**URL**: https://discourse.slicer.org/t/segmentation-scissors/5997

---

## Post #1 by @froth (2019-03-02 22:55 UTC)

<p>Hello everyone,<br>
I have problem we the tool scissors in segmentation menu. It started to be very laggy like minutes to do just simple cutting.</p>
<p>My workflow didn’t change, but i started experience these long waiting periods.<br>
I usually segment a vessel with fast marching (segmentationeditor extension), apply it, and try to cut off some parts in 3d view windows with the scissors tool, which takes form a few minutes to even half hour in more vast and complex cut. The workflow is similar to that presented on youtube: “make hollow” from ParkLab research. The problems occurred on version 4.9 and didn’t disappear after upgrade to 4.10.1</p>
<p>I work on iMac 2017y, Mojave OS; I7 4.2Ghz, 64GB ram; AMD Radeon 580 8gb<br>
In my opinion the hardware and software should be enough.<br>
What can I do with the issue?</p>

---

## Post #2 by @Amine (2019-03-04 08:19 UTC)

<p>Did you try disabling “smoothing” under show 3d? it significantly reduces the computing time <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1a48d4a00a783cb33bd3671ea0ce233e3c047b8.png" data-download-href="/uploads/short-url/rD2HyWvxdtT1zrerWRvT8Oy0BQI.png?dl=1" title="Capture%20d%E2%80%99%C3%A9cran%20(249)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1a48d4a00a783cb33bd3671ea0ce233e3c047b8_2_500x500.png" alt="Capture%20d%E2%80%99%C3%A9cran%20(249)" data-base62-sha1="rD2HyWvxdtT1zrerWRvT8Oy0BQI" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1a48d4a00a783cb33bd3671ea0ce233e3c047b8_2_500x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1a48d4a00a783cb33bd3671ea0ce233e3c047b8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1a48d4a00a783cb33bd3671ea0ce233e3c047b8.png 2x" data-dominant-color="F0F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture%20d%E2%80%99%C3%A9cran%20(249)</span><span class="informations">605×604 33.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @froth (2019-03-04 17:01 UTC)

<p>It used to work well but something changed. I always worked with smoothing and was fine. Moreover, turning off smoothing don’t help.<br>
The strange thing is that the same scans are working normally on slower computer (MacBook pro 2015y).<br>
Now it looks like during scissoring the slicer is not responding and it takes long minutes to deal with it. On the other computer just 2 seconds. I tried reinstalling slicer, cleaning disk, computer. The other things work super fast. Therefore I think it is something wrong with Slicer.</p>

---

## Post #4 by @lassoan (2019-03-04 17:13 UTC)

<p>Could you please send us a data set with that you can reproduce this issue? (upload to dropbox/onedrive/etc. and post the link)</p>

---

## Post #5 by @froth (2019-03-05 15:51 UTC)

<p>I enclose the dataset I discovered the problem. I do aorta segmentation with fast marching. I do some over segmentation that i have leakage on the spinal vertebra. When i cut the spine off in 3D view, Slicer is not responding for about 30 minutes. When I use scissors tool but in the saggital/axial view then cutting is very fast.<br>
Unfortunetly, the enclosed CT is not the only one. Currently, I have the same problem with all CTs when trying to cut the bigger surface. I worked fine 2-3 months ago. I don’t know what happened.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/kvkewbfqi2cqkjt/Vascular%20Aorta_Brzuszna%20%28Adult%29.zip?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="" height="">

      <a href="https://www.dropbox.com/s/kvkewbfqi2cqkjt/Vascular%20Aorta_Brzuszna%20%28Adult%29.zip?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/logo_catalog/dropbox_webclip_200_vis.png" class="thumbnail" width="" height="">

<h3><a href="https://www.dropbox.com/s/kvkewbfqi2cqkjt/Vascular%20Aorta_Brzuszna%20%28Adult%29.zip?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox - File Deleted</a></h3>

  <p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2019-03-05 16:37 UTC)

<p>I’ve tried the processing that you describe on your data. Cutting is fast for me in all views, on a 3-year old PC with 16GB RAM (see this video: <a href="https://1drv.ms/v/s!Arm_AFxB9yqHtvxvfwJOk1vLFwnv7Q" rel="nofollow noopener">https://1drv.ms/v/s!Arm_AFxB9yqHtvxvfwJOk1vLFwnv7Q</a>).</p>
<p>Do you see any errors in the application log?<br>
Do you have similar issues if you use simple thresholding to extract the vessel?</p>

---

## Post #7 by @froth (2019-03-05 18:36 UTC)

<p>. I recorded my screen, but the mac wheel of death is not being recorded (apple is clever:)))<br>
logs as on the movie. <a href="https://www.dropbox.com/s/ui4wsp6kk7enlis/Nagranie%20z%20ekranu%202019-03-5%20o%2019.23.50.mov?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/ui4wsp6kk7enlis/Nagranie%20z%20ekranu%202019-03-5%20o%2019.23.50.mov?dl=0</a></p>
<p>For treshold segmentation is the same. The method of segmentation doesn’t matter. Smth wrong when working on 3d rendering data. I tried 3d volume renderings on Horos and they work fine.</p>
<p>I reinstalled Slicer with removing ~/.config/NA-MIC, but without improvement. Are there any other files that slicer could left after uninstalling?</p>

---

## Post #8 by @lassoan (2019-03-05 19:01 UTC)

<p>Can you run XCode instruments to see what the application is doing?<br>
How is the memory usage while the computation is in progress?<br>
Any messages in the application log (menu: Help/Report a bug)?</p>

---

## Post #9 by @froth (2019-03-05 19:29 UTC)

<p>my CPU and memory usage is as following : <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c39763506d7c07f7efa48385c9927b3e38ac0107.jpeg" data-download-href="/uploads/short-url/rUhs8QSCAfRhFmSEKHVLn0KkyJp.jpeg?dl=1" title="19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c39763506d7c07f7efa48385c9927b3e38ac0107_2_666x500.jpeg" alt="19" data-base62-sha1="rUhs8QSCAfRhFmSEKHVLn0KkyJp" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c39763506d7c07f7efa48385c9927b3e38ac0107_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c39763506d7c07f7efa48385c9927b3e38ac0107_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c39763506d7c07f7efa48385c9927b3e38ac0107_2_1332x1000.jpeg 2x" data-dominant-color="323232"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">19</span><span class="informations">1586×1190 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bf2d52b670a3baf992d2d38054e85febf57ddf4.jpeg" data-download-href="/uploads/short-url/1HHwalEL0NGjJdf8JGmoI2CB5oo.jpeg?dl=1" title="09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bf2d52b670a3baf992d2d38054e85febf57ddf4_2_667x500.jpeg" alt="09" data-base62-sha1="1HHwalEL0NGjJdf8JGmoI2CB5oo" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bf2d52b670a3baf992d2d38054e85febf57ddf4_2_667x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bf2d52b670a3baf992d2d38054e85febf57ddf4_2_1000x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bf2d52b670a3baf992d2d38054e85febf57ddf4_2_1334x1000.jpeg 2x" data-dominant-color="333333"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">09</span><span class="informations">1592×1192 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>bug report <a href="https://www.dropbox.com/s/z014esz86612si6/bug%20report.docx?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - bug report.docx - Simplify your life</a><br>
and there is nothing wrong in application log</p>

---

## Post #10 by @froth (2019-03-05 19:32 UTC)

<p>i tried Slicer under bootcamp Windows on the same iMac and it works pretty fine 4-5 sec lags when cutting big areas. So the problem is on MacOS</p>

---

## Post #11 by @lassoan (2019-03-05 19:47 UTC)

<p>Can you run XCode Instruments to see what the application is doing? It can tell in what function Slicer spends time, which can help a lot in narrowing down what the issue can be.</p>
<p><a href="https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/debugging_tools.html" class="onebox" target="_blank" rel="nofollow noopener">https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/debugging_tools.html</a></p>
<p><a href="https://help.apple.com/instruments/mac/current/#//apple_ref/doc/uid/TP40004652-CH6-SW11" class="onebox" target="_blank" rel="nofollow noopener">https://help.apple.com/instruments/mac/current/#//apple_ref/doc/uid/TP40004652-CH6-SW11</a></p>

---

## Post #12 by @froth (2019-03-05 20:24 UTC)

<p>I’ve downloaded Xcode app but I have no idea how to load in 3d slicer<br>
Could you help with that part?</p>

---

## Post #13 by @lassoan (2019-03-05 20:39 UTC)

<p>You start 3D Slicer as usual, then launch Instruments, choose <em>attach to process</em>, and select the Slicer process. I don’t have a Mac, so I cannot help with specific instructions, but you should be able to find them by searching the web and if you have questions then Mac users should be able to help.</p>
<p><a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #14 by @hherhold (2019-03-05 20:49 UTC)

<p>Disable (or uninstall) CleanMyMac X.</p>

---

## Post #15 by @froth (2019-03-05 21:25 UTC)

<p>disabling CleanMac X didn’t help.</p>
<p>i attached the Slicer process to Xcode Debugger. However I am not sure the data is correct<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d876cf74832eccffaa9704930ae7579596884c97.jpeg" data-download-href="/uploads/short-url/uSVGo0jdzyDmv7QdCI8kqo9Vzfx.jpeg?dl=1" title="22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d876cf74832eccffaa9704930ae7579596884c97_2_690x394.jpeg" alt="22" data-base62-sha1="uSVGo0jdzyDmv7QdCI8kqo9Vzfx" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d876cf74832eccffaa9704930ae7579596884c97_2_690x394.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d876cf74832eccffaa9704930ae7579596884c97_2_1035x591.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d876cf74832eccffaa9704930ae7579596884c97_2_1380x788.jpeg 2x" data-dominant-color="2A2A2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">22</span><span class="informations">3572×2040 356 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @pieper (2019-03-05 21:41 UTC)

<aside class="quote no-group" data-username="froth" data-post="12" data-topic="5997" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/da6949/48.png" class="avatar"> froth:</div>
<blockquote>
<p>I’ve downloaded Xcode app but I have no idea how to load in 3d slicer<br>
Could you help with that part?</p>
</blockquote>
</aside>
<p>Easiest is to select the Slicer entry in the mac Activity Monitor and then select Sample Process from the gear menu.  This gives you most of the same information as Xcode instruments.</p>

---

## Post #17 by @froth (2019-03-05 22:45 UTC)

<p>The Sample Process of not responding 3d Slicer looks like this <a href="https://www.dropbox.com/s/ghj54e8pqd9jauw/Slicer%20sample.docx?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/ghj54e8pqd9jauw/Slicer%20sample.docx?dl=0</a></p>

---

## Post #18 by @pieper (2019-03-06 00:51 UTC)

<p>Thanks for posting that - it does look like most of the time is spent executing the scissors, so maybe there’s a very inefficient code path that stalls on mac.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> is there a test for the scissors so we can compare the exact operation on multiple platforms?</p>
<pre><code class="lang-auto">    +                                                                     2564 qMRMLSegmentEditorWidget::processEvents(vtkObject*, unsigned long, void*, void*)  (in libqSlicerSegmentationsModuleWidgets.dylib) + 382  [0x128e29b5e]
    +                                                                       2564 qSlicerSegmentEditorScissorsEffect::processInteractionEvents(vtkRenderWindowInteractor*, unsigned long, qMRMLWidget*)  (in libqSlicerSegmentationsEditorEffects.dylib) + 445  [0x128fc1a2d]
    +                                                                         2564 qSlicerSegmentEditorScissorsEffectPrivate::paintApply(qMRMLWidget*)  (in libqSlicerSegmentationsEditorEffects.dylib) + 205  [0x128fbe1dd]
    +                                                                           2564 vtkStreamingDemandDrivenPipeline::Update(int, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 254  [0x11c3f3d8e]
    +                                                                             2564 vtkStreamingDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 1120  [0x11c3f39a0]
    +                                                                               2564 vtkDemandDrivenPipeline::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 1228  [0x11c3cd61c]
    +                                                                                 2564 vtkCompositeDataPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 107  [0x11c3c885b]
    +                                                                                   2564 vtkDemandDrivenPipeline::ExecuteData(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 61  [0x11c3cde9d]
    +                                                                                     2564 vtkExecutive::CallAlgorithm(vtkInformation*, int, vtkInformationVector**, vtkInformationVector*)  (in libvtkCommon-8.2.1.dylib) + 69  [0x11c3d32c5]
    +                                                                                       2564 vtkImageStencilAlgorithm::ProcessRequest(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkImaging-8.2.1.dylib) + 65  [0x11bade4a1]
    +                                                                                         2564 vtkPolyDataToImageStencil::RequestData(vtkInformation*, vtkInformationVector**, vtkInformationVector*)  (in libvtkImaging-8.2.1.dylib) + 139  [0x11bd0281b]
    +                                                                                           1284 vtkPolyDataToImageStencil::ThreadedExecute(vtkImageStencilData*, int*, int)  (in libvtkImaging-8.2.1.dylib) + 2523  [0x11bd01efb]
    +                                                                                           ! 1013 vtkAOSDataArrayTemplate&lt;float&gt;::GetTuple(long long, double*)  (in libvtkCommon-8.2.1.dylib) + 217,28,...  [0x11bfa8519,0x11bfa845c,...]
    +                                                                                           ! 271 vtkStructuredGrid::GetPoint(long long, double*)  (in libvtkCommon-8.2.1.dylib) + 0,11,...  [0x11c28bb90,0x11c28bb9b,...]
    +                                                                                           1147 vtkPolyDataToImageStencil::ThreadedExecute(vtkImageStencilData*, int*, int)  (in libvtkImaging-8.2.1.dylib) + 2595,2603,...  [0x11bd01f43,0x11bd01f4b,...]
    +                                                                                           131 vtkStructuredGrid::GetPoint(long long, double*)  (in libvtkCommon-8.2.1.dylib) + 26  [0x11c28bbaa]
    +                                                                                           2 vtkPolyDataToImageStencil::ThreadedExecute(vtkImageStencilData*, int*, int)  (in libvtkImaging-8.2.1.dylib) + 2250  [0x11bd01dea]
    +                                                                                             2 vtkAOSDataArrayTemplate&lt;float&gt;::GetTuple(long long, double*)  (in libvtkCommon-8.2.1.dylib) + 213,217  [0x11bfa8515,0x11bfa8519]

</code></pre>

---

## Post #19 by @lassoan (2019-03-14 00:21 UTC)

<p>There is no automated test for Scissors.</p>
<p>Most of the time is spent in vtkPolydataToImageFilter, which is a quite simple and robust filter, so I suspect that the input extent or resolution of the output image might not be computed correctly. Does the memory usage of Slicer jumps significantly when Scissors operation takes a long time?</p>

---
