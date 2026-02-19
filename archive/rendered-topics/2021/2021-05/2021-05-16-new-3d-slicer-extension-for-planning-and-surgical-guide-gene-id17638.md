---
topic_id: 17638
title: "New 3D Slicer Extension For Planning And Surgical Guide Gene"
date: 2021-05-16
url: https://discourse.slicer.org/t/17638
---

# New 3D Slicer extension for planning and surgical guide generation for mandibular bone reconstruction

**Topic ID**: 17638
**Date**: 2021-05-16
**URL**: https://discourse.slicer.org/t/new-3d-slicer-extension-for-planning-and-surgical-guide-generation-for-mandibular-bone-reconstruction/17638

---

## Post #1 by @mau_igna_06 (2021-05-16 12:46 UTC)

<p>BoneReconstructionPlanner is a 3D Slicer extension for virtual surgical planning of mandibular reconstruction with vascularized fibula free flap and generation of patient-specific surgical guides.</p>
<p>BoneReconstructionPlanner is now available in the Extensions Manager for Slicer latest preview release.</p>
<p>Here is a preview video:</p><div class="youtube-onebox lazy-video-container" data-video-id="wsr_g_1E_pw" data-video-title="Mandible reconstruction on Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=wsr_g_1E_pw" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/wsr_g_1E_pw/hqdefault.jpg" title="Mandible reconstruction on Slicer" width="" height="">
  </a>
</div>

<p>And the link to the project:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://repository-images.githubusercontent.com/316575529/fc6f0980-7e9e-11eb-9a53-5c1e41ae1245" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerIGT/SlicerBoneReconstructionPlanner: 3D Slicer module for...</a></h3>

  <p>3D Slicer module for planning mandible reconstruction surgery using fibula flap - GitHub - SlicerIGT/SlicerBoneReconstructionPlanner: 3D Slicer module for planning mandible reconstruction surgery u...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @mau_igna_06 (2021-05-25 16:25 UTC)

<p>This extension wasn’t working due to an issue with the CMakeLists file.<br>
The problem has been solved. Please reinstall the extension since tomorrow and it will work</p>

---

## Post #3 by @mau_igna_06 (2021-09-29 22:33 UTC)

<p>There was a bug that made BoneReconstructionPlanner not work on the preview release. Now it has been solved. So it works well in both stable and preview releases of Slicer.</p>
<p>A videotutorial of use is available here:</p><aside class="quote quote-modified" data-post="1" data-topic="19754">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/how-to-design-3d-printed-surgical-guide-for-mandible-reconstruction/19754">How to design 3D-printed surgical guide for mandible reconstruction</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    This video shows how to get started with the Bone Reconstruction planner, an 3D Slicer extension for virtual surgical planning of mandibular reconstruction with vascularized fibula-free flap and generation of patient-specific surgical guides. 

  <a href="https://www.youtube.com/watch?v=g9Vql5h6uHM" target="_blank" rel="noopener nofollow ugc">
    [Mandible reconstruction | 3D Slicer Tutorial]
  </a>
  </blockquote>
</aside>


---

## Post #4 by @mau_igna_06 (2022-05-28 18:50 UTC)

<p>There was a hard to replicate bug that caused Slicer to crash while doing some BoneReconstructionPlanner processing.</p>
<p>This faulty behavior has been fixed by the latest commit to the main branch.</p>
<p>Thanks for using BRP</p>

---

## Post #5 by @mau_igna_06 (2022-06-18 17:07 UTC)

<p>The bug that some times made BRP crash while creating miterBoxes and holesCylinders was solved.</p>
<p>Probably it had something to do with that Polydata was created and then transformed very fast and some how it produced an exception.<br>
See details here:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/1ee7c6e5cb178dea4ce4e95c835555b482295fa3">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/1ee7c6e5cb178dea4ce4e95c835555b482295fa3" target="_blank" rel="noopener">github.com/SlicerIGT/SlicerBoneReconstructionPlanner</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/1ee7c6e5cb178dea4ce4e95c835555b482295fa3" target="_blank" rel="noopener">ENH: fix bug that made slicer crash on miterBox or Cylinders creation</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-06-18" data-time="16:59:35" data-timezone="UTC">04:59PM - 18 Jun 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/mauigna06" target="_blank" rel="noopener">
          <img alt="mauigna06" src="https://avatars.githubusercontent.com/u/19158307?v=4" class="onebox-avatar-inline" width="20" height="20">
          mauigna06
        </a>
      </div>

      <div class="lines" title="changed 1 files with 4 additions and 4 deletions">
        <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/1ee7c6e5cb178dea4ce4e95c835555b482295fa3" target="_blank" rel="noopener">
          <span class="added">+4</span>
          <span class="removed">-4</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @mau_igna_06 (2022-07-21 17:29 UTC)

<p>Finally we tracked down the real reason of the bug that made Slicer crash sometimes while creating cylinders or miterBoxes…</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6469">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6469" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6469" target="_blank" rel="noopener">vtkTubeFilter has no input connection makes Slicer crash (markupsPlane)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-07-18" data-time="14:41:03" data-timezone="UTC">02:41PM - 18 Jul 22 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-07-19" data-time="23:52:29" data-timezone="UTC">11:52PM - 19 Jul 22 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/mauigna06" target="_blank" rel="noopener">
          <img alt="mauigna06" src="https://avatars.githubusercontent.com/u/19158307?v=4" class="onebox-avatar-inline" width="20" height="20">
          mauigna06
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary
BoneReconstructionPlanner crashes 70% of the time while using vtkTub<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">eFilter (in the latter part of the workflow).

Previously these kind of messages have appeared:
```
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AC40A620)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AC40A520) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2ACBE2960)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2ACBE5060) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AB3176F0)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AB3170F0) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AC40A620)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AC40A520) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2ACBE2960)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2ACBE5060) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AB3176F0)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AB3170F0) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AC40A620)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AC40A520) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2ACBE2960)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2ACBE5060) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AB3176F0)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AB3170F0) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AC40A620)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AC40A520) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2ACBE2960)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2ACBE5060) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AB3176F0)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AB3170F0) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AC40A620)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AC40A520) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2ACBE2960)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2ACBE5060) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AB3176F0)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AB3170F0) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AC40A620)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AC40A520) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2ACBE2960)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2ACBE5060) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AB3176F0)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AB3170F0) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AC40A620)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AC40A520) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2ACBE2960)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2ACBE5060) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AB3176F0)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AB3170F0) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AC40A620)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AC40A520) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2ACBE2960)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2ACBE5060) has 0 connections but is not optional.
[ERROR][VTK] 17.07.2022 19:48:27 [vtkCompositeDataPipeline (000001F2AB3176F0)] (D:\D\P\S-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000001F2AB3170F0) has 0 connections but is not optional.
```

The number of different memory directions matches the quantity of mandiblePlanes that are being observed. The error appears to print one per 3D view render. If you set the plane locked, that plane doesn't produce this error any more.

## Steps to reproduce

1. Follow BoneReconstructionPlanner tutorial till you have a mandible reconstruction simulation achieved. (Takes 15minutes or 5minutes if you already did the segmentations)
2. Look at the error log (those error will be there)
3. If you go on with the workflow, later when you have to use some cylinders (vtkTubes) Slicer has 70% probability of crashing. Losing all the surgical planning that wasn't saved.

## Expected behavior

Slicer does not crash

## Related

https://discourse.slicer.org/t/error-vtk-input-port-0-of-algorithm-vtktubefilter-has-0-connections-but-is-not-optional/22153/3

## Environment
- Slicer version: Slicer built today with current source (5.1.0 2022/07/08)
- Operating system: Windows 10

## Proposed reason

https://github.com/Slicer/Slicer/blob/57a9ad15f4948bda3698c9b57d56aa7abe07e97e/Modules/Loadable/Markups/VTKWidgets/vtkSlicerPlaneRepresentation3D.h#L92

https://github.com/Slicer/Slicer/blob/57a9ad15f4948bda3698c9b57d56aa7abe07e97e/Modules/Loadable/Markups/VTKWidgets/vtkSlicerPlaneRepresentation3D.cxx#L248-L251

Inside other function of the class:

https://github.com/Slicer/Slicer/blob/57a9ad15f4948bda3698c9b57d56aa7abe07e97e/Modules/Loadable/Markups/VTKWidgets/vtkSlicerPlaneRepresentation3D.cxx#L494

## Solution

https://github.com/Slicer/Slicer/pull/6468

## Additional info

I couldn't do backtrace analisys with Slicer in "debug mode" or in "release mode with debug info" on Visual Studio 2019. Slicer wouldn't launch saying there is some CTK .dll missing</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’m sure users will be glad to know this is now really fixed</p>

---

## Post #7 by @mau_igna_06 (2022-10-09 21:21 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="6" data-topic="17638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Finally we tracked down the real reason of the bug that made Slicer crash sometimes while creating cylinders or miterBoxes…</p>
</blockquote>
</aside>
<p>There was another bug on Slicer (<a href="https://github.com/Slicer/Slicer/issues/6570" rel="noopener nofollow ugc">tracked here</a>) that made the crash happen and it will be solved soon since we found a way to make it reproducible.</p>
<p>The BRP team</p>

---

## Post #8 by @mau_igna_06 (2022-12-03 00:21 UTC)

<p>On the next weekends, since I do this ad-honorem, I’ll be creating BoneReconstructionPlanner self-tests that will allow other developers to maintain and improve this extension.</p>

---

## Post #9 by @mau_igna_06 (2022-12-15 19:21 UTC)

<p>The tests development for BoneReconstructionPlanner is moving forward.</p>
<p>Here is video of a Virtual Surgical Planning workflow for mandible reconstruction:<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fb85e3e487415e35fd3a2439af26baa789e09c9.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fb85e3e487415e35fd3a2439af26baa789e09c9.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fb85e3e487415e35fd3a2439af26baa789e09c9.mp4</a>
    </source></video>
  </div><p></p>
<p>Soon, probably, there will be tests for anatomical surgical guide creation also.</p>
<p>Best wishes,</p>
<p>MScEng Mauro I. Dominguez</p>

---

## Post #10 by @francesca_flore (2023-11-17 12:11 UTC)

<p>Hi!! I have problem with this plug in. I tried with different PCs but 3D slicer crashes when I use the plug-in. Any ideas? It would be very useful to be able to use it. Thanks.</p>

---

## Post #11 by @mau_igna_06 (2023-11-17 13:13 UTC)

<p>Hi.</p>
<p>I just made a Virtual Surgical Plan and could create the reconstructed neomandible and the fibula surgical guide yesterday. Be sure to be using “Slicer 5.2.2 Stable” release.</p>
<p>I’ll finish my planning today making the mandible surgical guide but I’m not expecting to find any problems. I did not experience any crash.</p>
<p>Please follow <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner#instructions" rel="noopener nofollow ugc">this instructions</a> and report where you get the crash or you get stuck. Then I can help further.</p>

---

## Post #12 by @mau_igna_06 (2023-11-18 13:34 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="11" data-topic="17638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I’ll finish my planning today making the mandible surgical guide but I’m not expecting to find any problems. I did not experience any crash.</p>
</blockquote>
</aside>
<p>I could finish the mandible surgical guide yesterday without problems</p>

---

## Post #13 by @francesca_flore (2023-11-20 14:57 UTC)

<p>Hi!! I uninstalled and reinstalled version 5.2.2 and it worked without any problems!  Thank you very much for helping!!</p>

---

## Post #14 by @mau_igna_06 (2023-11-20 15:16 UTC)

<p>Hi</p>
<p>Do you mean you could finish the virtual surgical planning and export the neomandible and personalized surgical guides by following the <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner#instructions" rel="noopener nofollow ugc">instructions</a> by yourself?</p>
<p>EDIT: <a class="mention" href="/u/francesca_flore">@francesca_flore</a> liked this comment so most probably she got it working</p>

---

## Post #15 by @francesca_flore (2023-11-20 15:24 UTC)

<p>Right! But it doesn’t work with subsequent versions… I have tried with 5.4.0 and 5.5.0</p>

---

## Post #16 by @mau_igna_06 (2023-11-20 15:37 UTC)

<p>Good to know. Thanks</p>
<p>This would be solved in future</p>

---

## Post #17 by @mau_igna_06 (2024-01-05 20:59 UTC)

<aside class="quote no-group" data-username="francesca_flore" data-post="15" data-topic="17638" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/francesca_flore/48/15307_2.png" class="avatar"> francesca_flore:</div>
<blockquote>
<p>Right! But it doesn’t work with subsequent versions… I have tried with 5.4.0 and 5.5.0</p>
</blockquote>
</aside>
<p>Since the commit below all appears working for me now on Slicer 5.6.1</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/a8eec0b588d59907c6440c098c5da2f033ec4076">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/a8eec0b588d59907c6440c098c5da2f033ec4076" target="_blank" rel="noopener nofollow ugc">github.com/SlicerIGT/SlicerBoneReconstructionPlanner</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/a8eec0b588d59907c6440c098c5da2f033ec4076" target="_blank" rel="noopener nofollow ugc">BUG: solve slicer crash during boolean operations to make surgical guide;</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-12-27" data-time="20:34:13" data-timezone="UTC">08:34PM - 27 Dec 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/mauigna06" target="_blank" rel="noopener nofollow ugc">
          <img alt="mauigna06" src="https://avatars.githubusercontent.com/u/19158307?v=4" class="onebox-avatar-inline" width="20" height="20">
          mauigna06
        </a>
      </div>

      <div class="lines" title="changed 1 files with 23 additions and 4 deletions">
        <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/a8eec0b588d59907c6440c098c5da2f033ec4076" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+23</span>
          <span class="removed">-4</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">BUG: increase point density of surgical guide objects to decrease chance of fail<span class="show-more-container"><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/a8eec0b588d59907c6440c098c5da2f033ec4076" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ing boolean operations;
BUG: correct very unrealistic shading of surgical guide boxes</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please report if not</p>
<p>Mauro</p>

---

## Post #18 by @Nolan_Bennett (2024-03-04 16:43 UTC)

<p>I’ve been using this extension on 5.6.1 and it seems to crash every time I perform the boolean operation. I’ve tried deleting and re-installing, same problem.</p>

---

## Post #19 by @mau_igna_06 (2024-03-04 16:46 UTC)

<p>If you can provide a video showing what happens and zipped file with a Slicer scene to reproduce the problem I’ll be able to fix it</p>

---

## Post #20 by @Nolan_Bennett (2024-03-04 23:40 UTC)

<p>Thank you for the timely response!</p>
<p>I can send a video but it does not show much, I’ve been following the tutorial in the README and have done everything up to the boolean operation for the fibula guide base. Slicer stops responding as soon as I click it. I have gotten it to run on slicer 5.2.2, but the boolean operation fails instead of crashing the program. I have a link to my zipped file</p>
<p><a href="https://uofnorthflorida-my.sharepoint.com/:u:/r/personal/n01449813_unf_edu/Documents/Spring%2024/Nolan%20Bennett%20Cutting%20Guide%20Test.zip?csf=1&amp;web=1&amp;e=9EkfUP" rel="noopener nofollow ugc">Nolan Bennett Cutting Guide Test.zip</a></p>

---

## Post #21 by @mau_igna_06 (2024-03-09 18:29 UTC)

<p>Hi</p>
<p>The software is working fine. There’s just a missing step on the text documentation I’ll fix soon, for the moment please see how it’s done on the <a href="https://youtu.be/g9Vql5h6uHM?t=904" rel="noopener nofollow ugc">videotutorial</a></p>

---

## Post #22 by @mau_igna_06 (2025-05-02 19:38 UTC)

<p><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner#bonereconstructionplanner" rel="noopener nofollow ugc">BoneReconstructionPlanner</a> extension is now compatible with Slicer 5.8.1 (stable) release and the documentation has been updated correspondingly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8baf2b0f167bc174d44f4e1c39135b10e4837708.jpeg" data-download-href="/uploads/short-url/jVHFcrB49YApzi0FUAGac3siyUw.jpeg?dl=1" title="screenshotPlanning" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8baf2b0f167bc174d44f4e1c39135b10e4837708_2_690x389.jpeg" alt="screenshotPlanning" data-base62-sha1="jVHFcrB49YApzi0FUAGac3siyUw" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8baf2b0f167bc174d44f4e1c39135b10e4837708_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8baf2b0f167bc174d44f4e1c39135b10e4837708_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8baf2b0f167bc174d44f4e1c39135b10e4837708_2_1380x778.jpeg 2x" data-dominant-color="9D9DB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshotPlanning</span><span class="informations">1920×1084 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ef1dbf4a87ec5c90b941cc21df11494895b8699.jpeg" data-download-href="/uploads/short-url/mG5CwcITBxYIO4T3hQgPvNFEUOJ.jpeg?dl=1" title="screenshotPatientSpecificSurgicalGuides" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ef1dbf4a87ec5c90b941cc21df11494895b8699_2_690x389.jpeg" alt="screenshotPatientSpecificSurgicalGuides" data-base62-sha1="mG5CwcITBxYIO4T3hQgPvNFEUOJ" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ef1dbf4a87ec5c90b941cc21df11494895b8699_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ef1dbf4a87ec5c90b941cc21df11494895b8699_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ef1dbf4a87ec5c90b941cc21df11494895b8699_2_1380x778.jpeg 2x" data-dominant-color="9FA0B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshotPatientSpecificSurgicalGuides</span><span class="informations">1920×1084 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
