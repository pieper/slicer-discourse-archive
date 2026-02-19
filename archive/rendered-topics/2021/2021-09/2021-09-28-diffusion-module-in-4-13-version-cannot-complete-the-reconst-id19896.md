---
topic_id: 19896
title: "Diffusion Module In 4 13 Version Cannot Complete The Reconst"
date: 2021-09-28
url: https://discourse.slicer.org/t/19896
---

# Diffusion module in 4.13 version cannot complete the reconstruction of fiber bundle

**Topic ID**: 19896
**Date**: 2021-09-28
**URL**: https://discourse.slicer.org/t/diffusion-module-in-4-13-version-cannot-complete-the-reconstruction-of-fiber-bundle/19896

---

## Post #1 by @slicer365 (2021-09-28 13:36 UTC)

<p>Win10 64</p>
<p>I don’t know if this is a mistake</p>
<p>My friend and I have tried multiple versions of 4.13 Slicer</p>
<p>But in the last step, when setting the seed to display the fiber bundle, it can’t be displayed.</p>
<p>The same data, the same steps, the fiber bundle can be displayed normally in version 4.11.</p>
<p>Can the developer test whether the fiber bundle can be rebuilt in the latest 4.13 version？</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/406c0f226d4a90f8732cf1ca6cd246c98f4a0637.jpeg" data-download-href="/uploads/short-url/9bU4zjD3VUV5ukVx951OVAK49PV.jpeg?dl=1" title="捕获.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/406c0f226d4a90f8732cf1ca6cd246c98f4a0637_2_517x271.jpeg" alt="捕获.PNG" data-base62-sha1="9bU4zjD3VUV5ukVx951OVAK49PV" width="517" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/406c0f226d4a90f8732cf1ca6cd246c98f4a0637_2_517x271.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/406c0f226d4a90f8732cf1ca6cd246c98f4a0637_2_775x406.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/406c0f226d4a90f8732cf1ca6cd246c98f4a0637_2_1034x542.jpeg 2x" data-dominant-color="9C9DA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获.PNG</span><span class="informations">1366×718 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>This is the same mrb file in 4.11 Version</strong><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e54c3aa3a74e514688afed31169a31bc93a372d0.png" data-download-href="/uploads/short-url/wIsEXSP3Vtgb4HBPHpHWDxO0c7K.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54c3aa3a74e514688afed31169a31bc93a372d0_2_517x275.png" alt="捕获" data-base62-sha1="wIsEXSP3Vtgb4HBPHpHWDxO0c7K" width="517" height="275" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54c3aa3a74e514688afed31169a31bc93a372d0_2_517x275.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54c3aa3a74e514688afed31169a31bc93a372d0_2_775x412.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54c3aa3a74e514688afed31169a31bc93a372d0_2_1034x550.png 2x" data-dominant-color="97999B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1366×728 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @zhangfanmark (2021-09-30 18:01 UTC)

<p>Hi!</p>
<p>Thank you for reporting this. We are able to reproduce this issue.</p>
<p>For my initial test, I guess there is an issue in the tract VTK writer. I can see point data is being output but not the cell data. Thank you <a class="mention" href="/u/pieper">@pieper</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd9bcf839c38d6ccb9a2d6e9b69c183c3af52c72.png" data-download-href="/uploads/short-url/AbwCBExQfJiU7tR9JHFSxeukplU.png?dl=1" title="PastedGraphic-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd9bcf839c38d6ccb9a2d6e9b69c183c3af52c72_2_551x500.png" alt="PastedGraphic-1" data-base62-sha1="AbwCBExQfJiU7tR9JHFSxeukplU" width="551" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd9bcf839c38d6ccb9a2d6e9b69c183c3af52c72_2_551x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd9bcf839c38d6ccb9a2d6e9b69c183c3af52c72_2_826x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd9bcf839c38d6ccb9a2d6e9b69c183c3af52c72_2_1102x1000.png 2x" data-dominant-color="C2C1DD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1</span><span class="informations">2029×1839 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @slicer365 (2021-09-30 22:59 UTC)

<p>This problem will be solved, right？ <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #4 by @ljod (2021-10-01 01:07 UTC)

<p>Hi yes we are looking into it and it will be solved. Thank you for letting us know! In the meantime please use the release version of Slicer if that is possible.</p>

---

## Post #5 by @pieper (2021-10-11 22:39 UTC)

<p><a class="mention" href="/u/slicer365">@slicer365</a> thanks for reporting this.  There was an API change in the version of VTK we use.  The change below fixes it and will be available in the next preview build of Slicer tomorrow.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerDMRI/SlicerDMRI/pull/151">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/151" target="_blank" rel="noopener">github.com/SlicerDMRI/SlicerDMRI</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/151" target="_blank" rel="noopener">BUG: fix tracts for vtk9</a>
    </h4>

    <div class="branches">
      <code>SlicerDMRI:master</code> ← <code>SlicerDMRI:vtk9-fix-tracts</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-11" data-time="22:32:35" data-timezone="UTC">10:32PM - 11 Oct 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 8 additions and 0 deletions">
        <a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/151/files" target="_blank" rel="noopener">
          <span class="added">+8</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The behavior of vtkCellArray::GetData changed with vtk9 such
that is now return<span class="show-more-container"><a href="https://github.com/SlicerDMRI/SlicerDMRI/pull/151" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">s a copy of the data rather than the actual
array, so manipulating it has no effect.

Instead now we must have the cell array import the legacy format.

This operation is no doubt slower but is a minimal change to restore
funcationality.  This code should really be threaded and reworked to
use the new API if performance is critical.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @slicer365 (2021-10-11 22:53 UTC)

<p>Thank you very much for your work！ <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #7 by @slicer365 (2021-10-14 13:29 UTC)

<p>A new question is, when a new fiber bundle is created, after clicking update, it takes a long time to show the fiber bundle. Can the speed be increased?</p>
<p>There is a open software called DSI-studio, it can quickly show the fiber bundle, can it be integrated into Slicer?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2957eeed993f305179e6e3dd347cfcc0bc37a46b.png" alt="image" data-base62-sha1="5TJYis7MdpkARzNPdtBl2LBnpKH" width="410" height="193"></p>

---

## Post #8 by @pieper (2021-10-14 19:59 UTC)

<p>You might be able to load DSI-studio data into Slicer, but I’ve never tried.</p>
<p>The built-in tractography seeding in Slicer only uses a single CPU core.  You may get better results and better performance using the UKF tractography extension which uses multiple threads.</p>

---

## Post #9 by @lassoan (2021-10-17 21:27 UTC)

<p>You can also tune the UKF tractography parameters to get results faster. I can get nice results in a fraction of a second. Of course the speed depends on the size and quality of your input data and your accuracy requirements.</p>
<p>I don’t know why DSI Studio developers chose to maintain their own application. It should be no problem at all to use Slicer as a frontend for their algorithms and they would save a lot of time that they could then spend on improving their computational methods.</p>

---

## Post #10 by @slicer365 (2022-03-13 14:45 UTC)

<p>Hello ,Mr Pieper,I fond the module SlicerDMRI still doesn’t work in the Slicer 4.13 0312  win10.<br>
Problem is after I install it through the extention manager，but it doesn‘t appear in the slicer Module’s menu,can you help check it !  thank you very much！</p>

---

## Post #11 by @pieper (2022-03-13 16:29 UTC)

<p>Yes, a lot of extensions need to be updated to work with the current preview (upcoming Slicer5 version), so for now we need to use the older release 4.11 for DMRI.</p>
<aside class="onebox googledocs" data-onebox-src="https://docs.google.com/spreadsheets/d/1GC4DWDpOXhuDYdfYOjJ6PmjHTeMM3-K7SoiC5ZR1GYg/edit#gid=29807248">
  <header class="source">

      <a href="https://docs.google.com/spreadsheets/d/1GC4DWDpOXhuDYdfYOjJ6PmjHTeMM3-K7SoiC5ZR1GYg/edit#gid=29807248" target="_blank" rel="noopener">docs.google.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://docs.google.com/spreadsheets/d/1GC4DWDpOXhuDYdfYOjJ6PmjHTeMM3-K7SoiC5ZR1GYg/edit#gid=29807248" target="_blank" rel="noopener"><span class="googledocs-onebox-logo g-sheets-logo"></span></a>

<h3><a href="https://docs.google.com/spreadsheets/d/1GC4DWDpOXhuDYdfYOjJ6PmjHTeMM3-K7SoiC5ZR1GYg/edit#gid=29807248" target="_blank" rel="noopener">Slicer5-failing-extensions</a></h3>

<p>Sheet1

Name,Operating system,Build error root cause,Last successful build,Action
1=remove, 2=remove?
3=would be nice to fix
4=should be fixed
5=must fix,Responsive maintainers,Comments
SlicerIGSIO,Windows,long...</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
