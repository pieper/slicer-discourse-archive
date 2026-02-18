# An error was reported en route using AI（Lungmask R321） of Lungsegmentation

**Topic ID**: 28653
**Date**: 2023-03-29
**URL**: https://discourse.slicer.org/t/an-error-was-reported-en-route-using-ai-lungmask-r321-of-lungsegmentation/28653

---

## Post #1 by @zhenhua3 (2023-03-29 14:08 UTC)

<p>Dear development team of LungCTanalyzer or Dear Rudolf Bumm professor<br>
I have an error while using your AI program, can you please help me solve this problem？<br>
This is my error record：<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1079b6fde6e6ce4ffca626aa2c584c12645fd654.jpeg" data-download-href="/uploads/short-url/2lKpyUHhqTUGY3tVa5LoJOkpVRy.jpeg?dl=1" title="1680098506351" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1079b6fde6e6ce4ffca626aa2c584c12645fd654_2_666x500.jpeg" alt="1680098506351" data-base62-sha1="2lKpyUHhqTUGY3tVa5LoJOkpVRy" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1079b6fde6e6ce4ffca626aa2c584c12645fd654_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1079b6fde6e6ce4ffca626aa2c584c12645fd654_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1079b6fde6e6ce4ffca626aa2c584c12645fd654_2_1332x1000.jpeg 2x" data-dominant-color="A19D9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1680098506351</span><span class="informations">1920×1440 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<a class="mention" href="/u/rbumm">@rbumm</a></p>

---

## Post #2 by @zhenhua3 (2023-03-29 14:10 UTC)

<p>The following is the complete error record of Python：<br>
<strong>[Qt] QLayout::addChildLayout: layout “” already has a parent</strong></p>
<p><strong>[Qt] ctkSliderWidget::setSingleStep() 0 is out of bounds. 0 1000 1</strong></p>
<p><strong>[Qt] ctkSliderWidget::setSingleStep() 0 is out of bounds. 0 100 1</strong></p>
<p><strong>[Python] Failed to compute results: cannot import name '<em>marching_cubes_lewiner_cy’ from partially initialized module ‘skimage.measure’ (most likely due to a circular import) (D:\120\Slicer 5.2.2\lib\Python\Lib\site-packages\skimage\measure_<em>init</em></em>.py)</strong></p>
<p><strong>Traceback (most recent call last):</strong></p>
<p><strong>File “D:/120/Slicer 5.2.2/NA-MIC/Extensions-31382/LungCTAnalyzer/lib/Slicer-5.2/qt-scripted-modules/LungCTSegmenter.py”, line 927, in runProcessing</strong></p>
<p><strong>self.logic.applySegmentation()</strong></p>
<p><strong>File “D:/120/Slicer 5.2.2/NA-MIC/Extensions-31382/LungCTAnalyzer/lib/Slicer-5.2/qt-scripted-modules/LungCTSegmenter.py”, line 2066, in applySegmentation</strong></p>
<p><strong>from lungmask import mask</strong></p>
<p><strong>File “D:\120\Slicer 5.2.2\lib\Python\Lib\site-packages\lungmask\mask.py”, line 3, in </strong></p>
<p><strong>from lungmask import utils</strong></p>
<p><strong>File “D:\120\Slicer 5.2.2\lib\Python\Lib\site-packages\lungmask\utils.py”, line 2, in </strong></p>
<p><strong>import skimage.measure</strong></p>
<p><strong>File “D:\120\Slicer 5.2.2\lib\Python\Lib\site-packages\skimage\measure_<em>init</em>_.py”, line 2, in </strong></p>
<p><strong>from ._marching_cubes_lewiner import marching_cubes, mesh_surface_area</strong></p>
<p><strong>File “D:\120\Slicer 5.2.2\lib\Python\Lib\site-packages\skimage\measure_marching_cubes_lewiner.py”, line 6, in </strong></p>
<p><strong>from . import _marching_cubes_lewiner_cy</strong></p>
<p><strong>ImportError: cannot import name '<em>marching_cubes_lewiner_cy’ from partially initialized module ‘skimage.measure’ (most likely due to a circular import) (D:\120\Slicer 5.2.2\lib\Python\Lib\site-packages\skimage\measure_<em>init</em></em>.py)</strong></p>
<p><strong>[VTK] Warning: In D:\D\S\S-0\Libs\MRML\Core\vtkMRMLSegmentationDisplayNode.cxx, line 287</strong></p>
<p><strong>[VTK] vtkMRMLSegmentationDisplayNode (000002675058FDD0): vtkMRMLSegmentationDisplayNode::GetSegmentDisplayProperties: no display properties are found for segment ID=, return default</strong></p>

---

## Post #3 by @rbumm (2023-03-29 15:11 UTC)

<p>Hello,</p>
<p>The Lung CT Analyzer just wraps code around existent (great) AI tools like “lungmask” by Johannes Hofmanninger and “TotalSegmentator” by Jakob Wasserthal / “TotalSegmenator extension” by <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>“lungmask” works perfectly fine on two of my test systems as well as on an AWS EC2 cloud instance. All are equipped with Nvidia GPUs and low (6 GB) to moderate/high (24 GB) dedicated video RAM.<br>
Could you provide some details of your system?</p>
<ul>
<li>Operating system</li>
<li>3D Slicer version</li>
<li>Lung CT Analyzer version</li>
<li>Type and model of GPU</li>
<li>dedicated video RAM</li>
</ul>
<p>Thank you.</p>

---

## Post #4 by @zhenhua3 (2023-03-29 15:25 UTC)

<ul>
<li>Operating system：win11</li>
<li>3D Slicer version：5.22</li>
<li>Lung CT Analyzer version：Latest version<br>
RAM:24GB<br>
My computer hardware is for the use of AI,Because I have used it smoothly before,But I reinstalled Python on my computer, and then he got the above error and couldn’t use AI，I don’t know why it’s getting an error and how I can fix it？</li>
</ul>

---

## Post #5 by @rbumm (2023-03-29 15:29 UTC)

<p>You will probably just need to uninstall 3D Slicer and completely remove the 3D Slicer installation folder, then reinstall 3D Slicer as well as the Lung CT Analyzer extension and all dependencies. Somehow your Slicer Python seems to have been messed up.</p>

---

## Post #6 by @zhenhua3 (2023-03-29 15:30 UTC)

<p><a class="mention" href="/u/johannes">@Johannes</a> Hofmanninger<br>
Dear Johannes<br>
I would appreciate you if you could help me with a problem</p>

---

## Post #7 by @zhenhua3 (2023-03-29 15:32 UTC)

<p>Okay, I’ll try it tomorrow.thank you</p>

---
