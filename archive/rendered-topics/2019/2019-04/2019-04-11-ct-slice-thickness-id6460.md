---
topic_id: 6460
title: "Ct Slice Thickness"
date: 2019-04-11
url: https://discourse.slicer.org/t/6460
---

# CT Slice Thickness

**Topic ID**: 6460
**Date**: 2019-04-11
**URL**: https://discourse.slicer.org/t/ct-slice-thickness/6460

---

## Post #1 by @andrewreilly (2019-04-11 00:06 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.1</p>
<p>Hi,</p>
<p>I’m a newbie to Slicer so apologies in advance if what I’m asking is obvious to some of you. Please be gentle!</p>
<p>I have a dataset that is a stack of CT slices, each of which is 512 pixels x 512 pixels. The slice thickness is very fine (of the order of a 0.25 mm) and I’d like reformat the stack to a thicker slice thickness (e.g. 2.0 mm). Very crudely, this would be roughly equivalent to reducing the number of slices by replacing every 8 slices with the average pixel value across all of the 8 slices. (I appreciate the physics of the imaging process means that generating a thick slice isn’t as simple as plain averaging, yet this is still a reasonable first order approximation.)</p>
<p>Having followed the various tutorials to get my head around how to use Slicer, importing my dataset, ensuring the orientation is correct, etc. I’ve been trying to work out how to modify slice thickness. My reading has led me to various resampling options. However, resampling at a coarser slice separation just generates a new slice with the pixel values interpolated from slices either side in the stack. Reading further I’m beginning to understand this is expected behaviour - resampling is exactly that, determining new pixel values through more or less sophisticated methods of interpolation.</p>
<p>I do understand the difference between slice thickness and slice spacing, and it’s definitely slice thickness I’d like to manipulate. However, I can’t find any obvious way to do that, and I can also find hardly any mention of the concept anywhere in the Slicer or ITK literature, yet this is standard functionality in many clinical image viewing systems. Indeed, in my experience it’s more likely that resampling in a clinical system will actually result in slice or section thickness changing rather than the pure resampling I’m finding in Slicer. This makes me think I may just be unfamiliar with the lexicon and searching for the wrong term.</p>
<p>Would anyone be able to point me in the right direction? If this functionality truly doesn’t exist I’d be open to trying to write something to develop it.</p>
<p>Thanks!</p>
<p>Andrew</p>

---

## Post #2 by @lassoan (2019-04-11 00:34 UTC)

<p>Slice thickness characterizes how sharply focused your image slice is, which is not relevant information for resampling. When you resample an image, you compute output voxel from multiple voxels in the neighborhood of the sampled position, using a kernel function. In most cases, linear kernel is good, and it is fast; but in some cases (for example for resampling very thin structures), higher order kernels work better.</p>
<p>For most image processing operations, having isotropic input volume is ideal. If you want to create such a volume then probably the most convenient module for that is “Crop volume” module.</p>

---
