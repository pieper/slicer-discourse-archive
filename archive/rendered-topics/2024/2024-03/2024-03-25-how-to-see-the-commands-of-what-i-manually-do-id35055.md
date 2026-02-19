---
topic_id: 35055
title: "How To See The Commands Of What I Manually Do"
date: 2024-03-25
url: https://discourse.slicer.org/t/35055
---

# How to see the commands of what I manually do

**Topic ID**: 35055
**Date**: 2024-03-25
**URL**: https://discourse.slicer.org/t/how-to-see-the-commands-of-what-i-manually-do/35055

---

## Post #1 by @ILB (2024-03-25 13:52 UTC)

<p>Hi!</p>
<p>Is there a way to see the commands that I execute while segmenting an image? For example, if I select a specific module or if I add a segment, I would like to know what would be the commands to introduce to automate the process (i.e, in a macro). I thought it would be in the Python console, but that’s is not what I’m looking for.</p>
<p>Thank you in advance!</p>
<p>Best</p>

---

## Post #2 by @pieper (2024-03-25 14:03 UTC)

<p>No, unfortunately there’s nothing like that.</p>

---

## Post #3 by @THartman (2024-03-27 22:29 UTC)

<p>The best I can recommend would be looking into how the segmentation is stored in slicer.  For volumes with no overlapping segments, this is pretty straightforward.  It’s pretty much a 3 dimensional color-by-number.  For example: I am presently segmenting volumes containing Blood Vessel trees and the solution that worked well for me was using a Breadth First Search algorithm on each non-zero point that would paint 1’s on the first vessel, 2’s on the second, etc. until it ran out of un-painted areas to check.  At the end of this, I was able to put the colored in segmentation into a labelmapNode and from there I was able to convert that labelmap into a segmentationNode.  I don’t know precisely what you are trying to segment, but if you approach it from a “what does the data look like” angle, you may find more efficient methods to achieve your endgoal.</p>

---

## Post #4 by @muratmaga (2024-03-27 22:47 UTC)

<p>Slicer does not offer GUI task automation like macros. What you can do is to get yourself familiar with python script to accomplish the same tasks through python console (this is often less complicated than trying to build the same automation through GUI, because all those button clicks and options quickly add up).</p>
<p>you can start reviewing the segmentation script samples, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>We have some annotated examples in SlicerMorph script tutorials as well:</p>
<p>e.g., <a href="https://github.com/SlicerMorph/Scripts?tab=readme-ov-file#2-run-an-image-processing-pipeline-on-a-folder-of-volumes" class="inline-onebox">GitHub - SlicerMorph/Scripts</a></p>

---

## Post #5 by @ILB (2024-04-01 07:21 UTC)

<p>Thank you for your response! I will check it out!</p>
<p>But if I undestood correctly, using this approach is not possible to automate the whole segmentation process right? Because although you can create a script with task such as importing and exporting files, the necessary manouvres performed to segment an element (such as moving through different slices) can not implemented.</p>
<p>I just want to make sure this is not a possibility, so I can explore other approaches.</p>
<p>Thank you again!<br>
Best,</p>

---

## Post #6 by @muratmaga (2024-04-01 15:22 UTC)

<p>I mean in general if you are going to interact with data, you can’t fully automate things anyways.</p>
<p>What are you expecting to do when you are moving through the slices? Explain what you want to do so that we can make better suggestions.</p>

---
