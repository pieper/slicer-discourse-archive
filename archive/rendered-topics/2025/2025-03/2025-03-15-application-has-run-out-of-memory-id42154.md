---
topic_id: 42154
title: "Application Has Run Out Of Memory"
date: 2025-03-15
url: https://discourse.slicer.org/t/42154
---

# "Application has run out of memory"

**Topic ID**: 42154
**Date**: 2025-03-15
**URL**: https://discourse.slicer.org/t/application-has-run-out-of-memory/42154

---

## Post #1 by @TChild (2025-03-15 16:01 UTC)

<p>Operating system: Microsoft Windows<br>
Slicer version: 5.8.1<br>
Expected behavior: File saving when “Save” is pressed; able to edit/mark scene<br>
Actual behavior: On four different normally working computers, an error message appears reading “Slicer has caught an application error, please save your work and restart.<br>
The application has run out of memory. Increasing virtual memory size in system settings or adding more RAM may fix this issue.<br>
If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a><br>
The message detail is:<br>
Exception thrown in event: bad allocation” when anything is clicked.  Computers have been restarted, I have made sure I have enough available RAM, and this has been occurring over multiple weeks when this was not an issue before.  Any help would be greatly appreciated!</p>

---

## Post #2 by @pieper (2025-03-15 17:44 UTC)

<p>What are you actually trying to save?  To get specific help, please provide the steps you followed and what data you are using.</p>

---

## Post #3 by @TChild (2025-03-20 06:22 UTC)

<p>I don’t come from a tech background so hopefully this is the right information.  I have a series of several thousand pictures from micro-CT scans of sea slugs and I’m tracking organ regeneration using this.  My “volume” is saved as an MHA file, and the current organ system/segmentation I’m working on is saved as an NRRD file.  Currently, I have the above error message when saving (“Save Data” and selecting my desired folder) and when trying to mark the organs in the digestive system (“Segment Editor” and “Paint”).  I do not have any issue loading the data.  Thank you in advance!</p>

---

## Post #4 by @pieper (2025-03-20 16:04 UTC)

<p>Okay, yes, that’s helpful info.  As the error message says, the program detects that it doesn’t have enough memory to complete the task.  It’s possible this is an error, perhaps due to something unique to the data you have or the way you are using it.</p>
<p>The easiest thing is to try a bigger computer and see if you are really running out of memory.</p>
<p>If the issue happens consistently or is otherwise unsolved, it would help for you to share the exact procedure, ideally with data leads to the problem.  If you can’t share the data, you can try to replicate the issue using data that is already public.</p>

---

## Post #5 by @muratmaga (2025-03-20 16:15 UTC)

<aside class="quote no-group" data-username="TChild" data-post="1" data-topic="42154">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tchild/48/79771_2.png" class="avatar"> TChild:</div>
<blockquote>
<p>On four different normally working computers, an error message appears reading “Slicer has caught an application error, please save your work and restart.<br>
The application has run out of memory. Increasing virtual memory size in system settings or adding more RAM may fix this issue.</p>
</blockquote>
</aside>
<p>You may want to run your data on MorphoCloud where there is ample memory. See the instructions at <a href="https://instances.morpho.cloud" rel="noopener nofollow ugc">https://instances.morpho.cloud</a></p>

---
