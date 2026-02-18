# Segment statistics problem

**Topic ID**: 3363
**Date**: 2018-07-03
**URL**: https://discourse.slicer.org/t/segment-statistics-problem/3363

---

## Post #1 by @Ash_Alarfaj (2018-07-03 15:07 UTC)

<p>Problem report for Slicer 4.8.1 macosx-amd64: [please describe expected and actual behavior]</p>
<p>When I’ve finished the segmentation and go to segment statistics the apply icon didn’t work and I need to close the programme and run it again to get it. this problem is repeating. I’ve shown  the correct node.</p>

---

## Post #2 by @cpinter (2018-07-03 16:05 UTC)

<p>Is this issue present in 4.9.0? Please install a recent nightly and check.</p>

---

## Post #3 by @Ash_Alarfaj (2018-07-05 15:26 UTC)

<p>Actually version 4.9 have some other problems. So I’ve decided to use the stable one 4.8 it works nicely just when I’ve spent long time segment then shift to segment statics the segment statics apply icon didn’t work unless I have to close the programme then open it again.</p>

---

## Post #4 by @cpinter (2018-07-05 16:20 UTC)

<p>What are the “some problems” with 4.9.0? That’s the version we actively maintain, so it would be important to know.<br>
Please install a recent nightly, and try to do your workflow. If you encounter problems, please send us detailed description about the steps you took and what worked differently than you expected.</p>

---

## Post #5 by @Ash_Alarfaj (2018-07-06 12:26 UTC)

<p>hi<br>
the one I’ve faced yesterday. the shift scroll to control the size of paint and eraser in version 4.9 mac os. and when I’ve used Windows version it was very slow to open save etc. Now I am using MAC OS, VERSION 4.8  and only I’ve faced this minor problem(need to close and open the programme when I need to calculate the segmentation.</p>

---

## Post #6 by @cpinter (2018-07-06 12:44 UTC)

<p>We won’t fix 4.8 bugs, because it is almost a year ago, and the new stable is coming up. If you’d like us to help you, help us fix the problems in 4.9.</p>
<p>However, you give us way too little information still, so I cannot possibly understand what the exact problem is. Please describe all the steps you take in order to reproduce the issue. Also explain what you expect instead. Something like this:<br>
1, Start Slicer<br>
…<br>
N. Click button<br>
Instead of X, Y happened.</p>

---

## Post #7 by @Ash_Alarfaj (2018-07-06 13:04 UTC)

<p>Hi</p>
<p>I would really to help you fix the programme. I will try my best to explain the issue</p>
<p>MAC OS version 4.9</p>
<ol>
<li>segment editor</li>
</ol>
<p>instead of controlling the size of the spheral brush using (shift+mouse wheel), it did not work, the spheral brush size did not change.</p>

---

## Post #8 by @cpinter (2018-07-06 13:50 UTC)

<p>On Mac it’s a different combination. I believe it’s shift + option + wheel, but I don’t have access to a Mac now so cannot confirm it. What I know is that it’s a double modifier combination.</p>

---

## Post #9 by @pieper (2018-07-06 14:45 UTC)

<p>On mac it’s command-shift-scroll to adjust the radius.</p>

---

## Post #10 by @Ash_Alarfaj (2018-07-13 10:37 UTC)

<p>No, it same Windows، the version 4.8 which I have worked on but the problem I have found in MAC OS 4.9 . the brush size doesn’t change with the shift scroll.</p>

---

## Post #11 by @lassoan (2018-07-13 19:18 UTC)

<p>I’ve just tried on a Mac and Shift + two-finger-swipe up/down changed the brush radius. You may need to click (right-click works, too) in a slice view to activate that view first.</p>

---
