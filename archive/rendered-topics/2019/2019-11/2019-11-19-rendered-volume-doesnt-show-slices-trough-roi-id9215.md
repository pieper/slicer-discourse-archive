# Rendered volume doesn't show slices trough ROI

**Topic ID**: 9215
**Date**: 2019-11-19
**URL**: https://discourse.slicer.org/t/rendered-volume-doesnt-show-slices-trough-roi/9215

---

## Post #1 by @Carolsv (2019-11-19 13:19 UTC)

<p>Dear all,</p>
<p>I have been trying to see patterns of variation in bone structures. For that, I am rendering a volume by using the Segment Editor module and applying ‘Threshold’ in a new added segment. After that, I am able to render the 3d image.<br>
Then in the Volume Rendering module, I selected the CAA preset (but I didn’t see any difference) and clicked on the Display ROI function. I see the box and “vectors” indicating the function, but in any of them I am able to see through the rendered volume. It stays as a solid skeleton as the box travels through the image.<br>
Can anyone help me with that? Should I render the volume differently so I can see through the slices in the rendered volume?</p>
<p>Thanks!</p>
<p>-Carolina</p>
<p>Operating system: Windows 10<br>
Slicer version:  4.10.2</p>

---

## Post #2 by @lassoan (2019-11-19 13:34 UTC)

<p>You can either show structures using by segmenting them using Segment Editor; or directly, without segmentation, using Volume rendering. If you show them both at the same time then most likely segmentation result occludes volume rendering result, so in order to see volume rendering, you need to hide the segmentation.</p>

---

## Post #3 by @Carolsv (2019-11-22 00:22 UTC)

<p>Thanks for the reply, but I’m still having trouble with that.<br>
I have a bitmap stack files, and when I try to import them as a Scalar volume for taking the steps to the Volume rendering, my data doesn’t load and I end up with all black windows where the slices should appear.</p>

---

## Post #4 by @muratmaga (2019-11-22 00:38 UTC)

<p>Slicer does not import bmp stacks as a scalar volume, it reads them RGB (vector volume). Once you imported your image stack you to invoke to vectortoscalar module.<br>
Alternatively,</p>
<ol>
<li>you can use SlicerMorph SkyscanReconImport (if your data is coming from a Bruker/Skyscan microCT. All you have to do is to point to the *_Rec.log file in the reconstruction folder). SlicerMorph is available as an extension for the preview builds.</li>
<li>You can use <a href="https://github.com/pieper/SlicerImageStacks" rel="nofollow noopener">https://github.com/pieper/SlicerImageStacks</a> as shown on the webpage (copy and paste the python code)</li>
</ol>

---

## Post #5 by @Carolsv (2019-12-02 00:37 UTC)

<p>Thank you!</p>
<p>I’ve downloaded the lastest preview version and was able to add SlicerMorph as an extension, but it didn’t solve my problem. Neither the Vector to Scalar module.<br>
The link to GitHub did the trick, and I was able to render one of my many datasets.</p>
<p>In another one, I have the slices availabe in .tiff format. I run the script, and after loading the files to create the volume file, I get the following message:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/Acer/AppData/Local/Temp/Slicer/SlicerImageStacks/SlicerImageStacks-master/ImageStacks/ImageStacks.py”, line 235, in onLoadButton<br>
self.logic.loadByPaths(paths, self.currentNode(), properties)<br>
File “C:/Users/Acer/AppData/Local/Temp/Slicer/SlicerImageStacks/SlicerImageStacks-master/ImageStacks/ImageStacks.py”, line 331, in loadByPaths<br>
volumeArray[sliceIndex] = sliceArray<br>
ValueError: could not broadcast input array from shape (700,316) into shape (805,1199)</p>
<p>Any idea what might be the issue? Thank you again for the help!</p>
<hr>
<p>Carolina</p>

---

## Post #6 by @pieper (2019-12-02 01:25 UTC)

<p>It looks like you have a mix of Image sizes in the selection.  Probably you only want to load equal sized images of the goal is to have a volume.  Often there is something in the filename that indicates which ones go together.</p>

---

## Post #7 by @flyingbird55 (2020-07-01 13:47 UTC)

<p>Choose the option that suits your computer in Rendering. With or without GPU.</p>
<p>Because my computer doesn’t have a discrete graphics card, I can only select VTK CPU Ray Casting.<br>
If you have a discrete graphics card, try the Rendering VTK GPU Ray Casting.<br>
As the following figure.</p>
<details>
<summary>
The above message was created using Google translate. Click here to see original text in Chinese.</summary>
<p>在Rendering里选择适合自己电脑的选项。With or without GPU。</p>
<p>因为我的电脑没有独立显卡，只能选择 VKT CPU Ray Casting。<br>
如果有独立显卡，可以试一试rendering VKT GPU Ray Casting。<br>
As the following figure.</p>
</details>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42c43680090ff2a19e1cf46151b4ffbe43e7d2dd.jpeg" data-download-href="/uploads/short-url/9wDTCX4qA4nDnPLWNmpqwSyLkM5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42c43680090ff2a19e1cf46151b4ffbe43e7d2dd_2_690x431.jpeg" alt="image" data-base62-sha1="9wDTCX4qA4nDnPLWNmpqwSyLkM5" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42c43680090ff2a19e1cf46151b4ffbe43e7d2dd_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42c43680090ff2a19e1cf46151b4ffbe43e7d2dd_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42c43680090ff2a19e1cf46151b4ffbe43e7d2dd_2_1380x862.jpeg 2x" data-dominant-color="8A8A8F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1600 530 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
