---
topic_id: 29659
title: "Paintbrush In Segment Editor Not Leaving A Trace Of My Brush"
date: 2023-05-26
url: https://discourse.slicer.org/t/29659
---

# Paintbrush in Segment Editor not leaving a trace of my brush stroke

**Topic ID**: 29659
**Date**: 2023-05-26
**URL**: https://discourse.slicer.org/t/paintbrush-in-segment-editor-not-leaving-a-trace-of-my-brush-stroke/29659

---

## Post #1 by @Fullcalf42 (2023-05-26 01:26 UTC)

<p>I’ve updated to the latest stable version of Slicer and then on to the most recent preview version seeking a solution. Actually got some trace of feedback from the paint brush in the preview version but inconsistent. I’d like to segment out the airway on a CT lung data set. I’ve done this before with other body parts but having trouble this time around. I saw there is a Airway Segmentation Extension that could be perfect for my needs but will seek a tutorial in order to utilize it. Any tips are appreciated.</p>

---

## Post #2 by @cpinter (2023-05-26 11:23 UTC)

<p>There are many questions but little information. What do you expect to happen with the paintbrush? What happens instead? What operating system do you use? Any other information that may help. Screenshots or screen recordings are appreciated. Thanks!</p>

---

## Post #3 by @Fullcalf42 (2023-05-26 12:16 UTC)

<p>I expect the paintbrush to leave a mark in the same color as the assigned segment. When I try to paint an area, there is no mark left to indicate where I have painted to distinguish one segment from the other.</p>
<p>I’m on a M1 Mac Mini OS 13.4 Ventura.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e231c1b039874c31695ba70c0820f1edae61a17d.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e231c1b039874c31695ba70c0820f1edae61a17d.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e231c1b039874c31695ba70c0820f1edae61a17d.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #4 by @pieper (2023-05-26 12:31 UTC)

<p>The video helps.  It appears you have “Enable intensity range” checked - try unselecting that.</p>

---

## Post #5 by @Fullcalf42 (2023-05-26 13:02 UTC)

<p>I just tried that. I did not see “Enable intensity range” but I did uncheck “Editable intensity range”. No difference. Thanks for trying.</p>

---

## Post #6 by @Fullcalf42 (2023-05-26 21:57 UTC)

<p>I went back to version 4.11.20210226 and got the results I needed.</p>

---

## Post #7 by @lassoan (2023-05-27 03:53 UTC)

<p>There is no need to go back to that really old Slicer version.</p>
<p>If masking settings are all correct but you cannot paint it is most likely due to that you are painting outside the segmentation’s extents. See how to adjust that <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">here</a>.</p>

---
