# Segmenting the skull base

**Topic ID**: 29143
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/segmenting-the-skull-base/29143

---

## Post #1 by @Tannadrake (2023-04-26 14:48 UTC)

<p>Hello Slicer Community</p>
<p>Background: I am a relatively new 3D slicer user. I am a neurosurgery resident with no programming experience. I am interested in using Slicer to segment neuroimaging for the purposes of 3D printing and education.</p>
<p>My question is, what is the best way you have found to segment the skull base from CT scans? I have tried a few methods but due to the extremely thin bone and generally poor image resolution in this region of the body, my models do not appear anatomically accurate. When using the threshold tool, if the threshold is too high, there are many holes where there should be bone (such as the orbital roof or posterior clinoids). However if the threshold is too low the small foramen disappear or there is “noise” that doesn’t resolve well with smoothing tools.</p>
<p>I am hopeful that an extension such as Total Segmenter could be created for the skull base and was curious if anyone is currently doing this work or at least knows of a better way to segment skull bases with improved anatomic accuracy.</p>

---

## Post #2 by @pieper (2023-04-26 15:01 UTC)

<p>I don’t think I’ve seen anything specific, but I would think that with some effort you could train <a href="https://monai.io/label.html">MONAI Label</a> to do that task.  It may take several dozen example segmentations to use for training.  If you find a public dataset maybe multiple people could contribute to a project.</p>

---

## Post #3 by @drnoorfatima (2026-02-17 09:38 UTC)

<aside class="quote no-group" data-username="Tannadrake" data-post="1" data-topic="29143">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ea5d25/48.png" class="avatar"> Tannadrake:</div>
<blockquote>
<p>Hello Slicer Community</p>
<p>Background: I am a relatively new 3D slicer user. I am a neurosurgery resident with no programming experience. I am interested in using Slicer to segment neuroimaging for the purposes of 3D printing and education.</p>
<p>My question is, what is the best way you have found to segment the skull base from CT scans? I have tried a few methods but due to the extremely thin bone and generally poor image resolution in this region of the body, my models do not appear anatomically accurate. When using the threshold tool, if the threshold is too high, there are many holes where there should be bone (such as the orbital roof or posterior clinoids). However if the threshold is too low the small foramen disappear or there is “noise” that doesn’t resolve well with smoothing tools.</p>
<p>I am hopeful that an extension such as Total Segmenter could be created for the skull base and was curious if anyone is currently doing this work or at least knows of a better way to segment skull bases with improved anatomic accuracy.</p>
</blockquote>
</aside>
<p>Hi, this post is a couple of years old but this problem comes up constantly so worth adding to.</p>
<p>The threshold issue you described is a fundamental limitation, not a technique problem. Skull base cortical bone in most CT protocols is simply too thin relative to voxel size, so you’re always trading foraminal definition against bone continuity. No threshold value solves that.</p>
<p>What works significantly better involves a multi-step approach that goes beyond what the threshold tool alone can do, and the right workflow depends on your CT acquisition parameters and what specific skull base structures matter most for your educational models.</p>
<p>I work on neuroimaging segmentation with a clinical neurology background. DM me if this is still something you’re working through, getting skull base models print-ready is very doable with the right approach.</p>

---
