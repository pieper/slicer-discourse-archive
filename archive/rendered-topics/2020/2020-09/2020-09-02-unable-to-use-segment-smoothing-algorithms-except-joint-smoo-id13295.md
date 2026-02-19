---
topic_id: 13295
title: "Unable To Use Segment Smoothing Algorithms Except Joint Smoo"
date: 2020-09-02
url: https://discourse.slicer.org/t/13295
---

# Unable to use segment smoothing algorithms except joint smoothing when using imported segments from "partial_lung_label_map" create by chest imaging platform

**Topic ID**: 13295
**Date**: 2020-09-02
**URL**: https://discourse.slicer.org/t/unable-to-use-segment-smoothing-algorithms-except-joint-smoothing-when-using-imported-segments-from-partial-lung-label-map-create-by-chest-imaging-platform/13295

---

## Post #1 by @vishnu_vardhan (2020-09-02 12:25 UTC)

<p>Operating system: Mac OS<br>
Slicer version: Slicer-4.11.0-2020-08-31-macosx-amd64<br>
Expected behavior: All smoothing algorithms should be working<br>
Actual behavior: As soon as any  smoothing algorithm except joint smoothing is applied, the segment disappears</p>

---

## Post #2 by @lassoan (2020-09-02 12:28 UTC)

<p>Thanks for reporting this. Could you upload somewhere the application log (menu: Help / Report a bug) and preferably also a sample segmentation file, and post the link here?</p>

---

## Post #3 by @vishnu_vardhan (2020-09-02 16:05 UTC)

<p><a href="https://fromsmash.com/HRAmtRiUKf-dt" rel="nofollow noopener">https://fromsmash.com/HRAmtRiUKf-dt</a></p>
<p>this is link to error log and .mrb bundle with an example</p>

---

## Post #4 by @lassoan (2020-09-02 16:52 UTC)

<p>Thank you, I was able to reproduce the problem with this scene. Probably it is due to the unexpected scalar type or range.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you investigate it further/fix it?</p>

---

## Post #5 by @vishnu_vardhan (2020-09-02 17:08 UTC)

<p>This doesn’t happen with the stable release by the way.</p>

---

## Post #6 by @lassoan (2020-09-03 12:38 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> fixed this issue yesterday (it was due to the unexpected scalar type of the input labelmap). Smoothing effect should work well in Slicer Preview Release you download today or later.</p>

---

## Post #7 by @vishnu_vardhan (2020-09-03 15:01 UTC)

<p>Sure thing.<br>
Will check it out.<br>
Thank you</p>

---
