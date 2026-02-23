---
topic_id: 46243
title: "New Slicer Skill Ai Tool"
date: 2026-02-22
url: https://discourse.slicer.org/t/46243
---

# New slicer-skill ai tool

**Topic ID**: 46243
**Date**: 2026-02-22
**URL**: https://discourse.slicer.org/t/new-slicer-skill-ai-tool/46243

---

## Post #1 by @pieper (2026-02-22 16:35 UTC)

<p>After learning from <a href="https://github.com/pieper/slicer-skill?tab=readme-ov-file#related-projects">previous experiments, several productive discussions</a> at project week and at the <a href="https://github.com/pieper/slicer-skill?tab=readme-ov-file#related-projects">last developer meeting</a>, I put together this <a href="https://github.com/pieper/slicer-skill">slicer-skill</a> that can be used with coding agents like Claude code.</p>
<p>It involves pulling down all the source code from Slicer and libraries like VTK, ITK, etc, together with all the discourse archives and other material like the source code for all the extensions.  It also includes a new mcp server so that it can iterate on doing programming tasks.</p>
<p>I think this crosses a real threshold of utility where I could give it a pretty high-level description of a task and it accomplished it with no further intervention from me.</p>
<p>In this case I gave it two prompts.  First: “use the slicer mcp server connection to download the MRHead sample data and set it up to volume render in the 3d viewer.  Use the slicer-skill if you need to figure out how to do it.”</p>
<p>And then: “Can you use the screencapture module to generate a video that shows the MRHead volume rendering going through the range of settings of the shift slider in the volume rendering module?”</p>
<p>And it generated this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1abaedde94206d1a361b63daad0386747ba8ad66.gif" alt="shift_sweep" data-base62-sha1="3OsUiUYeOtpOuMqRQwUP3tcyCmG" width="424" height="178" class="animated"></p>
<p>The AI, Claude in this case, examined the source code and figured out how to implement this and even pulled back screenshots of the app to look and see if the volume rendering looks correct.</p>
<p>This is significantly advanced over similar experiments I tried a year ago, or even last week.  This is all new, so there are surely ways to improve it, but everything needed to experiment with this is in the slicer-skill repo.  I’m really excited to see what we can build with this.</p>

---

## Post #2 by @ralkalay (2026-02-22 16:42 UTC)

<p>Steve, that is great, or to paraphrase the Sargent in Lawrence of Arabia meeting with Alenbi, Bloody marvelous!  That would be very helpful for Alissa and musculoskeletal model integration.  R</p>
<p>Ron N Alkalay<br>
Associate Professor,<br>
Dept of Orthopedic Surgery, Harvard Medical School<br>
Center for Advanced<br>
Orthopedic Studies<br>
Beth Israel<br>
Deaconess Medical Center<br>
1 Overland Street<br>
Boston, MA, 02215<br>
Tel. 617-667-5185<br>
Fax. 617-667-7175<br>
email:<br>
rn_alkalay@bidmc.harvard.edu</p>

---

## Post #3 by @sdamirsa (2026-02-22 16:54 UTC)

<p>I was waiting for this for the past two weeks. I feel a bit sad for my selfishness level, but I’m happy that I waited. Thanks for sharing this.</p>

---

## Post #4 by @sulli419 (2026-02-23 02:45 UTC)

<p>This sounds very useful.  Could it be used to fixed bugs in extensions?  As an example task, I am finding the ANTs extension can no longer apply fixed masks (for hiding parts of the volume).  It would be interesting to see if Claude could nail the problem and provide a fix for the next version.</p>

---
