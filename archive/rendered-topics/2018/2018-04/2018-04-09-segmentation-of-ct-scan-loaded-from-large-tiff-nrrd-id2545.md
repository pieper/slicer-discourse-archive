---
topic_id: 2545
title: "Segmentation Of Ct Scan Loaded From Large Tiff Nrrd"
date: 2018-04-09
url: https://discourse.slicer.org/t/2545
---

# Segmentation of CT scan loaded from large .tiff/.nrrd

**Topic ID**: 2545
**Date**: 2018-04-09
**URL**: https://discourse.slicer.org/t/segmentation-of-ct-scan-loaded-from-large-tiff-nrrd/2545

---

## Post #1 by @r_baumgarten (2018-04-09 16:02 UTC)

<p>Hello,</p>
<p>first of sorry, I know that this topic has been answered before, but the solutions don’t work for me.</p>
<p>Version: 3D Slicer 4.8.1<br>
Windows 10</p>
<p>I have a CT scan in individual .tiff images. If I try this method <a href="https://www.slicer.org/wiki/Documentation/4.8/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.8/FAQ - Slicer Wiki</a> either just one picture is loaded or none. Or everything is a single volume.</p>
<p>I have generated a .nrrd of my tiff-stack in hopes of using this, but the file won’t load.<br>
This is the Error Massage for the .nrrd file.</p>
<blockquote>
<p>Exception from vtkITK MegaMacro:<br>
itk::MemoryAllocationError (00000005DC4F8F58)<br>
Location: “unknown”<br>
File: d:\d\p\slicer-481-package\itkv4\modules\core\common\include\itkImportImageContainer.hxx<br>
Line: 199<br>
Description: Failed to allocate memory for image.</p>
<p>Algorithm vtkITKArchetypeImageSeriesScalarReader(000001F7F8403B10) returned failure for request: vtkInformation (000001F782BB4F40)<br>
Debug: Off<br>
Modified Time: 896388<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_DATA<br>
FROM_OUTPUT_PORT: 0<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1</p>
<p>ReadData: Cannot read file as a volume of type DiffusionTensorVolume[fullName = F:/filepath]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 1 files.<br>
File reader used the archetype file name of F:/filepath [reader 0th file name = F:/filepath]<br>
FileFormatError</p>
<p>ReadData: MRMLVolumeNode does not match file kind</p>
<p>ReadData: Failed to instantiate a file reader</p>
<p>ReadData: Cannot read file as a volume of type Volume[fullName = F:/filepath]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 1 files.<br>
File reader used the archetype file name of F:/filepath[reader 0th file name = F:/filepath]<br>
FileFormatError</p>
</blockquote>
<p>If someone has an idea or can point out what I did wrong it would be greatly appreciated.</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2018-04-09 17:00 UTC)

<aside class="quote no-group" data-username="r_baumgarten" data-post="1" data-topic="2545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/47e85d/48.png" class="avatar"> r_baumgarten:</div>
<blockquote>
<p>Or everything is a single volume</p>
</blockquote>
</aside>
<p>Isn’t loading all the tiff files as a single volume what you want?</p>

---

## Post #3 by @lassoan (2018-04-09 18:39 UTC)

<aside class="quote no-group" data-username="r_baumgarten" data-post="1" data-topic="2545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/47e85d/48.png" class="avatar"> r_baumgarten:</div>
<blockquote>
<p>Description: Failed to allocate memory for image.</p>
</blockquote>
</aside>
<p>You don’t have enough memory space to load this image. You may need to increase the amount of physical RAM or virtual memory or load a smaller version of the image.</p>
<p>How big is one frame? How many frames makes up the volume? How much physical and virtual memory do you have? (reported in first few lines of the application log in Help / Report a bug)</p>

---

## Post #4 by @r_baumgarten (2018-04-09 19:53 UTC)

<p>Ah sorry, I wasn’t clear enough in that description. So what I meant is, that i get image1.tiff, image2.tiff, etc. as a volume that I can choose from and not all images in a single volume</p>

---

## Post #5 by @r_baumgarten (2018-04-09 20:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="2545">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How big is one frame? How many frames makes up the volume? How much physical and virtual memory do you have? (reported in first few lines of the application log in Help / Report a bug)</p>
</blockquote>
</aside>
<p>One frame is 16091 KB and I have approximatly 5000 in a volume. The Laptop I’m currently using has 8GB RAM and 689 GB virtual memory.</p>
<p>So if memory space and RAM is a problem I can work with a more powerful PC.</p>

---

## Post #6 by @r_baumgarten (2018-04-11 11:34 UTC)

<p>I tested my file on another Computer with 129 RAM. I could only open a single tiff-file, otherwise the programm would crash.</p>
<p>Does someone have another idea?</p>

---

## Post #7 by @lassoan (2018-04-11 18:47 UTC)

<p>You could try to have just a few ten or few hundred files in the folder to see if loading succeeds then.</p>

---

## Post #8 by @r_baumgarten (2018-04-13 12:49 UTC)

<p>It isn’t. But even if it were I want to look at my whole scan, not just images. Thanks anyways.</p>

---

## Post #9 by @lassoan (2018-04-13 13:07 UTC)

<p>Can you share 10-20 subsequent images of your data set? If not then please copy 10 subsequent images to a separate folder, drag-and-drop the first one to the application window, uncheck single file option in the add data dialog, and post here the application log (menu: Help / Report a bug).</p>

---

## Post #10 by @r_baumgarten (2018-04-16 12:21 UTC)

<p>I don’t know what happend but it’s working know with the tiff files. So thank you all for your help :).</p>

---
