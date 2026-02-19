---
topic_id: 7648
title: "Use Segment Editor From Python"
date: 2019-07-17
url: https://discourse.slicer.org/t/7648
---

# Use segment editor from Python

**Topic ID**: 7648
**Date**: 2019-07-17
**URL**: https://discourse.slicer.org/t/use-segment-editor-from-python/7648

---

## Post #1 by @jazlynn21100 (2019-07-17 22:48 UTC)

<p>Good Afternoon!<br>
I have another line of questioning. I’m not someone that is proficient in coding (and has never had a reason to use python). I was hoping that I would be able to manipulate Segment Editor with the least amount of coding possible. Macros seemed promising, but it doesn’t work for any situations that aren’t exactly the same as the original, so that doesn’t help me much in my automating journey.</p>
<p>I was hoping that there is a way to control the Segment Editor completely from the CLI.<br>
To be more specific;<br>
I have masks of the brain, and 2 ROIs and I am making 3 segments in 3D, then making the entire segmentation about 20% opacity so all 3 areas can be seen (all of the parameters are the same for every set of images). Although it is incredibly simple, it can be time consuming for someone else In my lab that doesn’t know what they’re doing, or wants to do this for multiple different patients. However, since this is so sample, I feel like going through the source code for these modules to find what I use and make it streamlined that way is not the way to go.</p>
<p>I also haven’t been able to find what commands would be used for Segment Editor in the command line if I chose to go that way. The documentation around this kind of information is just very dense for someone that has never coded, but I am more than willing to learn!</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2019-07-18 02:24 UTC)

<p>This examples should help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>
<p>If you have any specific questions then let us know.</p>

---
