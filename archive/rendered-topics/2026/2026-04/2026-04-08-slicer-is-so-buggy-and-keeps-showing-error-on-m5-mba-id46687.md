---
topic_id: 46687
title: "Slicer Is So Buggy And Keeps Showing Error On M5 Mba"
date: 2026-04-08
url: https://discourse.slicer.org/t/46687
---

# Slicer is so buggy and keeps showing error on M5 MBA

**Topic ID**: 46687
**Date**: 2026-04-08
**URL**: https://discourse.slicer.org/t/slicer-is-so-buggy-and-keeps-showing-error-on-m5-mba/46687

---

## Post #1 by @sathishbalachandran (2026-04-08 21:41 UTC)

<p><strong>Hello Slicer Support Team,</strong></p>
<p>I am a Radiation Oncologist (MD, DNB) attempting to use 3D Slicer for my daily clinical cases (1-2 cases/day). I recently moved from an old, basic Windows laptop to a new <strong>MacBook Air M5</strong>, but the experience has been very difficult and I am unable to use the software.</p>
<p><strong>The primary issues I am facing:</strong></p>
<ol>
<li>
<p><strong>Security/Verification Issues:</strong> Upon installation, macOS could not verify the software. I had to manually go into my system settings and select <strong>“Open Anyway”</strong> just to get the application to start.</p>
</li>
<li>
<p><strong>Frequent Hanging:</strong> Even for simple tasks like loading a CT scan or scrolling through slices, the software “hangs” and becomes unresponsive. I often see the jumping icon in my dock or the spinning wheel, and I have to force quit the app repeatedly.</p>
</li>
<li>
<p><strong>TotalSegmentator is Unusable:</strong> I am completely unable to get the TotalSegmentator extension to work. Every time I try to run a segmentation—even in “Fast” mode—I get red error messages (like <code>ImportError: cannot import name 'GradScaler'</code>).</p>
</li>
<li>
<p><strong>“Tetris-like” Quality:</strong> When I did manage to get one test case to run on my old machine, the contours looked like “bricks” or “Tetris blocks” rather than smooth organs. On this new Mac, I can’t even get that far because the AI simply fails to start.</p>
</li>
</ol>
<p><strong>My Background:</strong> I am a medical doctor, not a “techie.” I do not know how to use the Terminal or write code. I purchased this MacBook M5 because I thought it would be faster and more stable for my clinical work, but currently, it is much worse than my old, cheap PC.</p>
<p><strong>My Question:</strong> Is there a stable, simple version of Slicer meant for the M5 chip that doesn’t require technical knowledge to fix? I just need a tool that “vomits out” smooth, accurate contours for my patients without the software hanging every few minutes.</p>
<p>I am happy to provide logs if you can tell me where to find them in the menus.</p>

---

## Post #2 by @muratmaga (2026-04-08 21:48 UTC)

<aside class="quote no-group" data-username="sathishbalachandran" data-post="1" data-topic="46687">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sathishbalachandran/48/82192_2.png" class="avatar"> sathishbalachandran:</div>
<blockquote>
<p>Is there a stable, simple version of Slicer</p>
</blockquote>
</aside>
<p>Yes, there is download and use the Slicer 5.10 (stable) version. There are dozens of users on the form using Slicer daily on Mac books (I am using a Macbook pro with M3), and Slicer works perfectly fine without any of those issues you report.</p>

---

## Post #3 by @jamesobutler (2026-04-08 21:58 UTC)

<p>Summary - most of these issues are unique to latest macOS systems and are not problems for Windows machines. The Slicer development for macOS has lagged behind a little bit because there are just fewer developers using macOS to help support these platform specific issues. Reviewing the <a href="https://download.slicer.org/download-stats/" rel="noopener nofollow ugc">download statistics</a> in the past year, macOS accounts for roughly 23% of downloads compared to 68% for Windows. Unfortunately there is no firm timeline on when macOS on latest Apple hardware will be optimized in an easily downloadable Slicer installer from the Slicer website.</p>
<p>Regarding 1) Yes this is generally a known issue when running the Slicer Preview because it is not signed and notarized each night. Have you tried using the Slicer 5.10.0 stable instead?</p>
<p>Regarding 2) How much memory does your MacBook Air have and how large is the CT scan that you are loading and analyzing?</p>
<p>Regarding 3) There is an issue with a TotalSegmentator dependency requiring a newer torch version however Slicer on macOS is running an intel built version rather than a native Apple silicon ARM64 based version. The Torch dependency however hasn’t been providing latest versions for Intel built apps running on macOS. Slicer is running an intel version on your system through the Rosetta layer which you might have had to install when you got your new computer.</p>
<aside class="quote quote-modified" data-post="3" data-topic="45200">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/version-5-10-0-error-in-total-segmentator/45200/3">Version 5.10.0, error in total segmentator</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    This appears to be an issue introduced by NNunetv2 developers. This package is a dependency of TotalSegmentator. 
A possible workaround is to open the NNunet Slicer module which is used for installing versions of the package. Choose to install nnunetv2&lt;2.6 as it seems like the nnunetv2 2.6.0 version introduced this error that requires torch 2.6.0 and later for the CPU version of GradScaler. 
Unfortunately, on macOS Slicer factory builds are still x86_64 builds with no native arm64 build. The lat…
  </blockquote>
</aside>


---

## Post #4 by @pieper (2026-04-08 22:53 UTC)

<p>Oh, and <a class="mention" href="/u/sathishbalachandran">@sathishbalachandran</a>, don’t forget that slicer is free and supported by people who find it useful for themselves.</p>
<p>We’re happy to help you, but you get more flies with honey as they say : )</p>

---
