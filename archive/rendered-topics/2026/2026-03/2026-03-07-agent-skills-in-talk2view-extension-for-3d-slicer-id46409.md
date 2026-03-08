---
topic_id: 46409
title: "Agent Skills In Talk2View Extension For 3D Slicer"
date: 2026-03-07
url: https://discourse.slicer.org/t/46409
---

# Agent Skills in Talk2View Extension for 3D Slicer

**Topic ID**: 46409
**Date**: 2026-03-07
**URL**: https://discourse.slicer.org/t/agent-skills-in-talk2view-extension-for-3d-slicer/46409

---

## Post #1 by @benzwick (2026-03-07 17:14 UTC)

<p>We have integrated <a href="https://agentskills.io" rel="noopener nofollow ugc">Agent Skills</a> into our Talk2View extension for 3D Slicer to automate complex workflows.</p>
<p>The Talk2View extension for 3D Slicer can be downloaded from our website here: <a href="https://talk2view.com/download" rel="noopener nofollow ugc">https://talk2view.com/download</a></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/229a635a17c9096c8d026b51c2e31b86fdb1395c.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42314d19276c6f9975a77aaa4a6f02f24f928acb.jpeg" data-video-base62-sha1="4W70yrpKLiQvePRQepZ0l4Q4zko.mp4">
  </div><p></p>
<p>This is an example of a skill that can be used to automate the segmentation of multiple datasets (in this case two images from the Slicer sample data):</p>
<pre><code class="lang-auto">---
name: my-segment-skill
description: Segmentation workflow for brain MRI datasets.
metadata:
    skill-author: Talk2View
---

# My Segment Skill

## Datasets

Process these datasets from Slicer sample data in order:

- MR Brain Tumor 1
- MR Brain Tumor 2

## Segments

For each dataset, create these segments:

| Name       | Color |
| ---------- | ----- |
| Tumor      | red   |
| Ventricles | blue  |

## How to segment

### Tumor

Adaptive Brush with MRI T1+GD enhancing tumor preset, paint at RAS [-5, 27, 28] with 20 mm radius

### Ventricles

First, jump to RAS [18, 21, 1] in all slice views, which is close to where the ventricles are.
Then use Adaptive Brush with simple threshold algorithm, radius of 7 mm, threshold zone of 30%.

## Workflow

Ensure that the scene is empty before you create a new segmentation.

For each dataset:

1. Download the sample data
2. Create a segmentation with the first segment from the table
3. Activate the tool with the specified preset or algorithm, then apply any extras
4. Show the segmentation in 3D, and if the segment has already been painted and is not empty, jump to the segment in all slice views
5. Tell the user they can now refine the segment, and wait until they are done
6. When the user is finished, add the next segment and repeat from step 3
7. When all segments are done, report the volume of each segment,
   save the scene, and clear the scene before
   moving to the next dataset
</code></pre>
<p>The skills and tools editor inside the Talk2View Slicer extension can be used to create and edit new and existing skills (natural language descriptions of workflows as above) and connectors that contain tools that the AI can use to manipulate the 3D Slicer scene.</p>
<p>If anyone has ideas for new workflows to try we would be very happy to hear about them.</p>

---
