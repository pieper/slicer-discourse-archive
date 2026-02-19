---
topic_id: 13012
title: "Developer Needed For Automatic Load Images Export Segmentati"
date: 2020-08-15
url: https://discourse.slicer.org/t/13012
---

# Developer needed for automatic load images, export segmentations

**Topic ID**: 13012
**Date**: 2020-08-15
**URL**: https://discourse.slicer.org/t/developer-needed-for-automatic-load-images-export-segmentations/13012

---

## Post #1 by @NoobForSlicer (2020-08-15 13:41 UTC)

<p>Hello, this is a thread for anyone who is interested to make some money and also develop a slicer script:</p>
<p>Here is the script description:</p>
<p>Script that goes through a $Mainfolder<br>
and opens every $Subfolder.</p>
<p>In each Subfolder there is a set of .PNG images to be loaded into a volume.</p>
<p>Based on the name of the first image (first image name is basically a int number separated from a string value by a comma, create transformation and apply it to the volume. the transformation should be made using the int number from the name of the image)</p>
<p>Create segmentation based on threshold parameters usind the threshold method.</p>
<p>Show 3D and smoothen by 0.3 instead of default 0.5</p>
<p>Export segmentation and rename the exported .obj file to hold ($stringvaluefromtheimage name, int value from the name of the first image, int value from the name of the last image)</p>
<p>How much would you require for such a script?<br>
Thank you  all &lt;3</p>

---

## Post #2 by @Alex_Vergara (2020-08-15 15:15 UTC)

<p>Some sample images would be nice to evaluate the feasibility of the job. Regards</p>

---

## Post #3 by @NoobForSlicer (2020-08-15 20:36 UTC)

<p>images are around 4000x2000 png format.<br>
Usually in the sets are anywhere from 30-400 images<br>
each image is around 3-4 mb.</p>
<p>the images contain already segmented specimen so there is usually only 1 color and it should entirely be painted, evenything else is black. so same treshold settings can be used for entire set of images.</p>
<p>I could post a sample on monday because its weekend but i don’t know what we could learn new from it. I can answer all details and questions you’d need by monday already.</p>
<p>So please ask whatever questions you have, I think I am ready to answer</p>

---

## Post #4 by @Alex_Vergara (2020-08-17 08:34 UTC)

<p>I would need a regular expression for the files inside folder, or an assertion that all files inside the folder shall be processed (no exceptions).</p>
<p>I need to know if all files in a folder are suppossed to be slices of a single 3d volume, in this case I will need the voxel size (width, height, depth) in mm.</p>
<p>How do I know the order of loading? The images are numbered, how?</p>
<p>Where do you want the output? (same folder, folder selection dialog)</p>

---

## Post #5 by @NoobForSlicer (2020-08-17 11:09 UTC)

<p>Image file names look like this:<br>
“0001, tumor.png”<br>
“0002, tumor.png”<br>
All files in the folder shall be processed. If subfolders present in that same folder with that set of images, they hold info data and shall not be processed further.</p>
<p>Yes I can get the voxel size i wuold have to check.</p>
<p>Order of loading the images because of their names.<br>
“0001, tumor.png”<br>
“0002, tumor.png”<br>
“0003, tumor.png”<br>
“0004, tumor.png”</p>
<p>Output on the Desktop folder called “Output”<br>
In this case output file name should be “tumor” not the numbers of the each image.</p>

---

## Post #6 by @Alex_Vergara (2020-08-17 11:41 UTC)

<p>Thanks, I will prepare a mockup and will let you know. it shall be ready today.</p>
<p>more details please write to me in pv</p>

---

## Post #7 by @Alex_Vergara (2020-08-17 13:31 UTC)

<p>I need a valid email from you to add you to the github project</p>

---
