---
topic_id: 32957
title: "Error While Segmenting"
date: 2023-11-22
url: https://discourse.slicer.org/t/32957
---

# Error while segmenting

**Topic ID**: 32957
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/error-while-segmenting/32957

---

## Post #1 by @towfi_islam (2023-11-22 12:31 UTC)

<p>Hello,</p>
<p>I’m trying to segment a ct scan, while segmenting I get this error -</p>
<p>Slicer has caught an application error, please save your work and restart.</p>
<p>If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: vector</p>

---

## Post #2 by @lassoan (2023-11-22 12:33 UTC)

<p>Please test with the latest Slicer Preview Release. If you still experience any errors then provide screen capture video or step-by-step instructions (every click you make) that we can use to reproduce what you see.</p>

---

## Post #3 by @towfi_islam (2023-11-22 16:56 UTC)

<p>Tested it with 5.5, was using 5.4 before and the error remains. Here is the click by click -</p>
<p>Open Slicer - drag a mrml file into slicer and the scan loads up - click on segment editor - click on paint - click on one of the segments - click on the scan on axial view  to paint - error pops up.</p>
<p>Is this clear enough? If not I can make a screen recording.</p>

---

## Post #4 by @lassoan (2023-11-22 17:58 UTC)

<p>I cannot reproduce the problem by following the steps you described. No error for me.</p>
<p>Can you share the .mrml file? (upload somewhere and post the link here; make sure there is no patient information in it)</p>

---

## Post #5 by @Masahiro (2023-11-23 07:52 UTC)

<p>Almost same error occurred to me.<br>
Is there any solution?</p>

---

## Post #6 by @towfi_islam (2023-11-23 08:03 UTC)

<p>Found a fix, I just had to go back to slicer version 5.2.1 which solved it for me. 5.4 and 5.5 didnt work.</p>

---

## Post #7 by @chir.set (2023-11-23 08:25 UTC)

<aside class="quote no-group" data-username="towfi_islam" data-post="6" data-topic="32957">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/towfi_islam/48/68407_2.png" class="avatar"> towfi_islam:</div>
<blockquote>
<p>5.4 and 5.5 didnt work.</p>
</blockquote>
</aside>
<p>Could not reproduce this in 5.5 neither, with multiple saved scenes.</p>

---

## Post #8 by @lassoan (2023-11-23 12:13 UTC)

<p>Older Slicer versions do not get any feature updates or fixes, so going back is not a solution. There are so many updates and news features and so many more coming that you really don’t want to miss those.</p>
<p>All you need is to provide us information that allows us to reproduce the problem.</p>
<p>Most likely the issue is related to the content of the saved scene, so you could send us the scene files (upload somewhere and post the link here). We can also set up a meeting with you (with screen sharing) to see what you do and what the scene contains that may cause problems.</p>

---

## Post #9 by @Lin_Li (2023-11-24 03:11 UTC)

<p>I got this problem too. Exact the same thing. I solved it by changing header data in nrrd file from float32 to int32 and it’s fixed.</p>

---

## Post #10 by @pieper (2023-11-24 14:31 UTC)

<p>Please report the exact steps to reproduce the issue if the workflow was contained within Slicer.  Or if there was another program that generated a nrrd file with inconsistent header data please report to the maintainers of that program so the issue can be resolved.</p>

---

## Post #11 by @Lin_Li (2023-12-05 01:58 UTC)

<p>I’m not sure where the mask is generated. But I change the segmentation matrix element dtype from float32 to int32 and it’s solved. I didn’t change the header. I think some python package generate the classification label matrix by float32 but not int32 and that is the problem.</p>

---

## Post #12 by @da5ideber (2024-02-19 21:47 UTC)

<p>is everyone having this issue running on Mac? I am getting the same issue and the only clue I can seem to find is that it happens when the volume and the segmentation are in different types (float/short) and the sizes are different, however on windows, slicer seems to have no problem with the same files that crash on Mac - also worth noting is the issue happens only in the brush tool, not in the erase or other paint based tools for me</p>

---

## Post #13 by @da5ideber (2024-02-19 22:04 UTC)

<p>As an update, a colleague has found converting the segmentation node to a binary label map, then back to a segmentation node seems to fix the issue</p>

---

## Post #14 by @pieper (2024-02-19 22:42 UTC)

<p>This came up again recently and it seems there’s a floating point exception generated on the arm64 (apple silicon) when editing float segmentations.  It wasn’t the case with intel macs.  For now yes, converting to an integer format via the workaround suggested by <a class="mention" href="/u/da5ideber">@da5ideber</a> sounds like a good option.</p>

---

## Post #15 by @lassoan (2024-02-20 19:27 UTC)

<p>Using floating-point types for storing binary labelmaps is bad for performance and may result in additional complications. Therefore, never use float or double type for storing labelmaps and if you get data sets like this from somewhere then report it as an issue to the developers of that software.</p>
<p>Unfortunately, we cannot rely on other software producing valid output, so Slicer needs to detect and report this error (maybe even do an automatic conversion to a suitable integer type). We already have an issue for this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6941">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6941" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6941" target="_blank" rel="noopener">Segmentation closed surface representation generation fails for float voxels</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-04-16" data-time="13:30:01" data-timezone="UTC">01:30PM - 16 Apr 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Domain: Segmentation
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

When a seg.nrrd file uses `type: float` voxels then closed surface<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> representation is not generated (nothing appears or only a single segment's 3D representation appears).

See full error report here: https://discourse.slicer.org/t/only-one-of-28-segments-is-showing-in-3d/28934/3

## Steps to reproduce

- Load https://github.com/lassoan/PublicTestingData/releases/download/data/InvalidFloatSegmentationArterialAtlas.seg.nrrd into Slicer
- Create closed surface representation
- Only one segment appears in 3D

## Expected behavior

All segments should appear in 3D

## Environment
- Slicer version: Slicer-5.2.2
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
