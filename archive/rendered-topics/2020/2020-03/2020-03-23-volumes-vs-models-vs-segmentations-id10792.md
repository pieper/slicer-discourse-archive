# Volumes vs models vs segmentations

**Topic ID**: 10792
**Date**: 2020-03-23
**URL**: https://discourse.slicer.org/t/volumes-vs-models-vs-segmentations/10792

---

## Post #1 by @jens-k (2020-03-23 14:23 UTC)

<p>Hey everyone,<br>
I’m new to slicer and I am a bit confused about all the different possible types of 3D data.</p>
<p>Terms used in the documentation and tutorial videos are volumes, models, and segmentations, as well as labelmaps, volumetric ROIs, subtraction maps, segmentation nodes, markups and masks. Is there documentation on what the differences between especially the first three are?</p>
<p>For example, some modules I have tried to segment the skull in an MRI image give me a volume, others give me a segmentation. Why and what does that mean to me in practice?</p>
<p>I seem unable to find information on this and other problems I have with 3D slicer. Am I using the wrong strategy (e.g. googling ‘3d slicer subtraction maps’)?</p>
<p>Thanks for any kind of help,<br>
Jens</p>

---

## Post #2 by @lassoan (2020-03-23 14:59 UTC)

<p>These are the basic data types in Sicer:</p>
<ul>
<li>Volume: 3D array of voxels, such as CT, MRI, PET, … images. It has a few subtypes, such as:
<ul>
<li>scalar volume: each voxel store a continuous value, such as intensity or density value</li>
<li>labelmap volume: each voxel value stores a discrete value, for example an index of a color in a color table; this can store segmentations (index value refers to segment number)</li>
<li>vector volume: each voxel contains a vector, can be used to store color images, displacement fields, etc.</li>
</ul>
</li>
<li>Model: surface mesh (such as an STL file), or volumetric mesh (such as a tetrahedral mesh for finitie element analysis)</li>
<li>Segmentation: stores a segmentation a.k.a. ROI, mask, contour. It can have various representations internally (binary labelmap, closed surface, etc.) and can be easily converted</li>
<li>Markups: points, lines, angles, curves, planes, etc. defined typically by a set of control points</li>
</ul>
<p><a class="mention" href="/u/jcfr">@jcfr</a> it would be great if you could set up ReadTheDocs for documentation - I would add the above information to an documentation page there.</p>

---

## Post #3 by @cpinter (2020-03-23 15:24 UTC)

<p>Here’s a page that could help. The figure on the bottom helps understand which data type takes part of which step.<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html" class="onebox" target="_blank">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a></p>

---

## Post #4 by @jens-k (2020-03-26 16:32 UTC)

<p>Cool, thank you very much!</p>

---

## Post #5 by @cpinter (2022-05-20 08:47 UTC)

<p>Update to those who find the answer above now: the figure has been moved to <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#review-loaded-data" class="inline-onebox">User Interface — 3D Slicer documentation</a></p>

---

## Post #6 by @bagginstyrone (2022-05-21 09:53 UTC)

<p>Thanks, everyone for clearing my concepts on Volumes, Models, and Segmentations. It has helped me very much.</p>

---

## Post #7 by @Young_Wang (2022-10-26 12:58 UTC)

<p>Thank you for the explanation, I wonder if you could expand on this topic in terms of the case uses of when is one data type preferred over another one.</p>

---

## Post #8 by @muratmaga (2022-10-26 16:54 UTC)

<p>You may want to refer to a biomedical image analysis handbook of sorts to understand what each data modality is preferred for. But in very broad terms you need:</p>
<p><strong>Volumes</strong> when the intensity information is relevant to your analysis (as different tissues may be represented by different intensity signals.<br>
<strong>Segmentation</strong> is the process of converting to intensity information to binary representation (e.g., you are segmenting a tumor. It doesn’t matter the intensity differences, as long as you identify the region as a tumor). You discard the intensity information. From segmentations, you can drive <strong>Label maps</strong> which are binary images that can be used to mask/crop regions, can be used to calculate volumes/masses or structure, Finally, you can drive <strong>3D models</strong> from segmentations, which are geometric representations of the structures.</p>
<p>Depending on the analysis, sometimes you want to work on the intensity volume, sometimes on the label map or sometimes on 3D model.</p>

---
