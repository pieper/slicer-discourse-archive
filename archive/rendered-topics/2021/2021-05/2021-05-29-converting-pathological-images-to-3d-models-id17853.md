---
topic_id: 17853
title: "Converting Pathological Images To 3D Models"
date: 2021-05-29
url: https://discourse.slicer.org/t/17853
---

# Converting Pathological Images to 3D Models

**Topic ID**: 17853
**Date**: 2021-05-29
**URL**: https://discourse.slicer.org/t/converting-pathological-images-to-3d-models/17853

---

## Post #1 by @arif (2021-05-29 17:07 UTC)

<p>Hi dear Slicer community</p>
<p>I am trying to convert images of pathology (jpeg) to 3d models. Is it possible to do something like this in Slicer or should I look for other options ? Also I am open to any suggestions.</p>
<p>Best Regards</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea5393631b3941cb8414a71463a9cfdda5407107.jpeg" data-download-href="/uploads/short-url/xqWMS57FuP3QD0xs33OcKuYeGKH.jpeg?dl=1" title="9206" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea5393631b3941cb8414a71463a9cfdda5407107_2_690x487.jpeg" alt="9206" data-base62-sha1="xqWMS57FuP3QD0xs33OcKuYeGKH" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea5393631b3941cb8414a71463a9cfdda5407107_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea5393631b3941cb8414a71463a9cfdda5407107_2_1035x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea5393631b3941cb8414a71463a9cfdda5407107_2_1380x974.jpeg 2x" data-dominant-color="CFD7DF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">9206</span><span class="informations">2338×1653 905 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9b71be9baf4f56955ce7eb6f33f952440a4ad43.jpeg" data-download-href="/uploads/short-url/sMshpCwFZX5tZIOFsN3fNmLp3xh.jpeg?dl=1" title="9206_0003" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9b71be9baf4f56955ce7eb6f33f952440a4ad43_2_649x500.jpeg" alt="9206_0003" data-base62-sha1="sMshpCwFZX5tZIOFsN3fNmLp3xh" width="649" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9b71be9baf4f56955ce7eb6f33f952440a4ad43_2_649x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9b71be9baf4f56955ce7eb6f33f952440a4ad43_2_973x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c9b71be9baf4f56955ce7eb6f33f952440a4ad43_2_1298x1000.jpeg 2x" data-dominant-color="A6A9AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">9206_0003</span><span class="informations">4614×3554 1.26 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-05-29 19:40 UTC)

<p>You can render these slices directly directly in 3D, or segment them and create 3D model. The main challenge is to align the slices and you may need a strong computer if the resolution of the slices is very high.</p>

---

## Post #3 by @arif (2021-05-31 12:38 UTC)

<p>Hello Andras ,</p>
<p>I am trying to make the jpeg images work on slicer but when I try to load a jpeg bundle it only loads one image as a sequance. <a href="https://www.youtube.com/watch?v=BcnpzYE8VO8" class="inline-onebox" rel="noopener nofollow ugc">Load sequence of PNG files as a 3D volume into 3D Slicer - YouTube</a> I tried this tutorial and did not work for me. Do you have any suggestions.</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2021-05-31 21:26 UTC)

<p>Probably not all your images are exactly the same size. You will probably see an error message about this in the application log. If there is no error message or it indicates a different problem, then let us know.</p>

---

## Post #5 by @arif (2021-06-01 14:27 UTC)

<p>Hi Andras,</p>
<p>Recent log file is down below.</p>
<p><strong>Errors:</strong></p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\Yakup\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in <em>call_with_frames_removed<br>
File “C:/Users/Yakup/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/ChangeTracker/lib/Slicer-4.11/qt-scripted-modules/ChangeTracker.py”, line 4, in <br>
import ChangeTrackerWizard<br>
File "C:\Users\Yakup\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\ChangeTracker\lib\Slicer-4.11\qt-scripted-modules\ChangeTrackerWizard_<em>init</em></em>.py", line 2, in <br>
from ChangeTrackerStep import *<br>
ModuleNotFoundError: No module named ‘ChangeTrackerStep’<br>
loadSourceAsModule - Failed to load file “C:/Users/Yakup/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/ChangeTracker/lib/Slicer-4.11/qt-scripted-modules/ChangeTracker.py”  as module “ChangeTracker” !<br>
Fail to instantiate module  “ChangeTracker”<br>
libpng warning: iCCP: known incorrect sRGB profile<br>
The following modules failed to be instantiated:<br>
ChangeTracker<br>
When loading module  “ChangeTrackerSelfTest” , the dependency “ChangeTracker” failed to be loaded.</p>
<p><strong>Warnings:</strong></p>
<p>libpng warning: iCCP: known incorrect sRGB profile<br>
When loading module  “ChangeTrackerSelfTest” , the dependency “ChangeTracker” failed to be loaded.</p>
<p><strong>Messages:</strong></p>
<p>Session start time …: 2021-06-01 17:12:59</p>
<p>Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release</p>
<p>Operating system …: Windows / Professional / (Build 19041, Code Page 65001) - 64-bit</p>
<p>Memory …: 3978 MB physical, 15978 MB virtual</p>
<p>CPU …: GenuineIntel , 8 cores, 8 logical processors</p>
<p>VTK configuration …: OpenGL2 rendering, TBB threading</p>
<p>Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)</p>
<p>Developer mode enabled …: no</p>
<p>Prefer executable CLI …: yes</p>
<p>Application path …: C:/Users/Yakup/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin</p>
<p>Additional module paths …: NA-MIC/Extensions-29738/ChangeTracker/lib/Slicer-4.11/cli-modules, NA-MIC/Extensions-29738/ChangeTracker/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/PETTumorSegmentation/lib/Slicer-4.11/qt-loadable-modules, NA-MIC/Extensions-29738/PETTumorSegmentation/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/PET-IndiC/lib/Slicer-4.11/cli-modules, NA-MIC/Extensions-29738/PET-IndiC/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/cli-modules, NA-MIC/Extensions-29738/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules</p>
<p>Reversing DICOM dictionary so can look up tag from a keyword…</p>
<p>Scripted subject hierarchy plugin registered: Annotations</p>
<p>Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>Switch to module: “Welcome”</p>
<p>Loaded volume from file: C:/Users/Yakup/Desktop/Patoloji Deneme 3D/Prostate 1.jpg. Dimensions: 1041x969x1. Number of components: 3. Pixel type: unsigned char.</p>
<p>“Volume” Reader has successfully read the file “C:/Users/Yakup/Desktop/Patoloji Deneme 3D/Prostate 1.jpg” “[0.05s]”</p>
<p>Loaded volume from file: C:/Users/Yakup/Desktop/Patoloji Deneme 3D/Prostat 2.png. Dimensions: 1041x969x1. Number of components: 4. Pixel type: unsigned char.</p>
<p>“Volume” Reader has successfully read the file “C:/Users/Yakup/Desktop/Patoloji Deneme 3D/Prostat 2.png” “[0.05s]”</p>
<p>Thank you</p>

---

## Post #6 by @lassoan (2021-06-01 17:35 UTC)

<p>If you uncheck the “single file” option then the file reader will look for similarly named files in the folder and attempt to load them as one image stack. The logs do not indicate that loading of multiple files was attempted, which may indicate that the reader did not find similar files. What are the names of your other files in the folder?</p>
<p>You can also use <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">Image Stacks module</a> (provided by SlicerMorph extension), which allows you to explicitly specify a list of files or name matching pattern (and it has a number of additional useful features, such as downsampling and loading of the relevant region of a large image).</p>

---
