# So weirdly slicer always erases 1 slice lower... WHY?!

**Topic ID**: 9697
**Date**: 2020-01-03
**URL**: https://discourse.slicer.org/t/so-weirdly-slicer-always-erases-1-slice-lower-why/9697

---

## Post #1 by @NoobForSlicer (2020-01-03 05:18 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11e6fd8e1cad2e89fce9cd9d550c874ad7548871.png" data-download-href="/uploads/short-url/2yn0JbeDZCCIgTm8APgqvcXACgF.png?dl=1" title="THE PROBLEM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11e6fd8e1cad2e89fce9cd9d550c874ad7548871.png" alt="THE PROBLEM" data-base62-sha1="2yn0JbeDZCCIgTm8APgqvcXACgF" width="690" height="381" data-dominant-color="B9C799"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">THE PROBLEM</span><span class="informations">755×417 4.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is always a problem, I set everything okay but for some unknown reason, slicer is painting 1 slice lower. Here is the image. Yellow line is my eraser tool. When I click as you can see, it erased one slice lower.</p>
<p>No matter what I do, I can’t get this to work properly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11e6fd8e1cad2e89fce9cd9d550c874ad7548871.png" data-download-href="/uploads/short-url/2yn0JbeDZCCIgTm8APgqvcXACgF.png?dl=1" title="THE PROBLEM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11e6fd8e1cad2e89fce9cd9d550c874ad7548871.png" alt="THE PROBLEM" data-base62-sha1="2yn0JbeDZCCIgTm8APgqvcXACgF" width="690" height="381" data-dominant-color="B9C799"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">THE PROBLEM</span><span class="informations">755×417 4.49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-01-03 06:22 UTC)

<p>Let us know if you can reproduce this issue with latest Slicer Preview Release.</p>

---

## Post #3 by @NoobForSlicer (2020-01-03 08:18 UTC)

<p>Yes, I have just downloaded it and tested it.</p>
<p>Same problem persists when all is imported in the newest 4.11 version from 17th 12</p>

---

## Post #4 by @NoobForSlicer (2020-01-03 08:20 UTC)

<p>this has been a common issue to be honest… IT has happened many times with different segmentations.</p>
<p>Sometimes all works okay and sometimes it just acts like this.</p>

---

## Post #5 by @NoobForSlicer (2020-01-03 08:30 UTC)

<p>okay so when i place this number on the red view to .500,<br>
the slice changes but segmentation REMAINS the same.</p>
<p>Then when I draw it deletes segmentation which I see in a good way.</p>
<p>So I put the segmentation in the transformation and move it half a milimeter down but now segmentation matches only half of the corresponding pixel, and half of it is overlapping the inferior pixel.</p>
<p>I am completely puzzled.<br>
now if the red is at S: 541.000mm I see it okay and it erases the exact slice of segmentation i see.</p>
<p>However if I move S:541.400m the segmentation changes while the underlying image remains the same and then when I paint the segmentation is not erased but it still erases in the lower segmentatin slice.</p>
<p>This is completely nuts and cofusing.</p>

---

## Post #6 by @NoobForSlicer (2020-01-03 08:33 UTC)

<p>the whole point is that when i approach .500 value the image changes and segmentation remains the same.<br>
if i add .501 the segmentation slice is still showing the same in the red.</p>
<p>and only when I write .502 the segmentation slice changes as well…</p>
<p>so i am thinking now maybe i should lower segmentation 0.002 down so it will maybe be ok idk…<br>
I will try</p>

---

## Post #7 by @NoobForSlicer (2020-01-03 08:54 UTC)

<p>this is getting weirder and weirder…</p>
<p>segmentation changes at 0.999<br>
then I lower it by 0.010</p>
<p>now it changes at 0.990.<br>
What the actual hell? How is this even possbible?</p>
<p>I literally moved it 0.010 mm down and it got pulled only 9 mm down.</p>
<p>I am baffled</p>

---

## Post #8 by @NoobForSlicer (2020-01-03 09:00 UTC)

<p>Now I completely matched it</p>
<p>both image and segmentation slice change exactly at 0.500 and still the very same problem persists.</p>
<p>It appears to me that nothing can change this problem. the yellow line in  Left-right view shows correctly in which slice I am hovering over with eraser tool<br>
but once I click on it, segmentation is painted on the slice lower than that.</p>
<p>Completely confused</p>

---

## Post #9 by @NoobForSlicer (2020-01-03 09:12 UTC)

<p>okay</p>
<p>now it only appears to delete  what I see in the red when i am between 0.498 and 0.499</p>
<p>any other number wont work.<br>
Further more the yellow line now is centered on the border between the two neighbouring slices. Meaning it is not covering only one as it used to before.<br>
Damn it…</p>

---

## Post #10 by @lassoan (2020-01-03 13:49 UTC)

<p>Don’t worry, these kind of problems can be addressed quickly if we understand what’s happening. For this, we need to be able to reproduce the issue.</p>
<p>Can you upload an example scene that reproduces this and send us the link? (make sure the data is anonymized) Posting a few screenshots with slice intersections displayed could help, too.</p>

---

## Post #11 by @NoobForSlicer (2020-01-03 16:12 UTC)

<p>Thank you for helping… I will have to anonymize the data and upload.</p>
<p>I haven’t managed to solve it</p>

---
