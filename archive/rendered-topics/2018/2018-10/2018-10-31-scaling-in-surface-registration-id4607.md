# Scaling in Surface Registration

**Topic ID**: 4607
**Date**: 2018-10-31
**URL**: https://discourse.slicer.org/t/scaling-in-surface-registration/4607

---

## Post #1 by @Marzieh_Golabbakhsh (2018-10-31 18:03 UTC)

<p>Hi<br>
I use the following module:</p>
<p>Registration/ CMF Registration/ Surface Registration to register two stl models.</p>
<p>My understanding(after looking up the linearTransform marices) is here it only uses Rotation and Translation in calculating linearTransforms either with affine or RigidBody transforms.</p>
<p>but I need scaling too!</p>
<p>What should I do?</p>

---

## Post #2 by @lassoan (2018-10-31 19:04 UTC)

<p>There are other modules for surface registration:</p>
<ul>
<li>SlicerIGT extension’s <em>Model registration</em> module: uses ICP and supports rigid and similarity (rigid+scaling) transforms</li>
<li>
<em>SegmentRegistration</em> extension’s <em>Segment registration</em> module: uses distance map based registration and supports rigid and deformable (warping) transforms. You need to import your models into segmentation node using Segmentations module (takes 3-4 mouse clicks).</li>
</ul>

---

## Post #3 by @Marzieh_Golabbakhsh (2018-11-01 18:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>uses distance map based registration</p>
</blockquote>
</aside>
<p>Thanks for your reply. I found “Distance Map Based Registration” in Registration/Label Registration. Is this the one you referred?<br>
I think I can not use stl files and maybe I have to use LabelMapVolume? Is there a way I can convert stl or wrl files to LabelMappVolume in Slicer?</p>

---

## Post #4 by @lassoan (2018-11-01 21:08 UTC)

<aside class="quote no-group" data-username="Marzieh_Golabbakhsh" data-post="3" data-topic="4607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e95f7d/48.png" class="avatar"> Marzieh_Golabbakhsh:</div>
<blockquote>
<p>Thanks for your reply. I found “Distance Map Based Registration” in Registration/Label Registration</p>
</blockquote>
</aside>
<p>You need “Segment registration” module (in Registration category). The module is provided by SegmentRegistration extension.</p>
<aside class="quote no-group" data-username="Marzieh_Golabbakhsh" data-post="3" data-topic="4607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e95f7d/48.png" class="avatar"> Marzieh_Golabbakhsh:</div>
<blockquote>
<p>I think I can not use stl files and maybe I have to use LabelMapVolume? Is there a way I can convert stl or wrl files to LabelMappVolume in Slicer?</p>
</blockquote>
</aside>
<p>You need to import your models into segmentation node using Segmentations module (takes 3-4 mouse clicks). Then you can use Segment Registration module to register them.</p>

---

## Post #5 by @Marzieh_Golabbakhsh (2018-11-05 20:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="4607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Segment Registration module</p>
</blockquote>
</aside>
<p>After using this module, when I go to save the files:<br>
I have for example: PreAlignmentMoving2FixedLinearTransform_3.h file.<br>
However, Affine Transform and Deformable Transform have status “Not Modified”</p>
<p>And I am not even sure if the modification that I see is results of a complete alignment or not!</p>

---

## Post #6 by @lassoan (2018-11-05 22:13 UTC)

<p>Are the segments aligned before registration? Do they look aligned after the registration?</p>
<p>What are the next steps of your workflow? Do you want to save the transforms and/or the transformed segments? In what format (nrrd, ITK, DICOM,…)?</p>

---

## Post #7 by @Marzieh_Golabbakhsh (2018-11-06 14:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="4607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are the segments aligned before registration? Do they look aligned after the registration?</p>
</blockquote>
</aside>
<p>The segments move close to each other after registration but they are not aligned. I feel they are only rotated and translated. They are on top of each other after registration.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="4607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What are the next steps of your workflow? Do you want to save the transforms and/or the transformed segments? In what format (nrrd, ITK, DICOM,…)?</p>
</blockquote>
</aside>
<p>I need to save the transform and be able to apply it to new data. Also I want to save the transformed segments too. I prefer nrrd for now but I can also work with other formats as long as I can open them with Slicer and work with them.</p>
<p>It is helpful also if I have access to parameters of the Transform and Registration and can understand how parameters will affect my registration.</p>
<p>Thanks</p>

---

## Post #8 by @Marzieh_Golabbakhsh (2018-11-12 16:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="4607" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are the segments aligned before registration? Do they look aligned after the registration?</p>
<p>What are the next steps of your workflow? Do you want to save the transforms and/or the transformed segments? In what format (nrrd, ITK, DICOM,…)?</p>
</blockquote>
</aside>
<p>To clarify my problem:</p>
<p>I think I don’t have scaling in my transformed model although I used segment registration module.<br>
I think they are just pre-aligned with translation and rotation and not aligned with deformed or affine transformation.<br>
I want to know why this happens?</p>

---

## Post #9 by @cpinter (2018-11-12 19:03 UTC)

<p>Rigid registration by definition does not include scaling. Segment Registration however performs deformable registration as well, which does. You need to make sure that the deformable transform is applied on your segmentation.</p>
<p>It is also possible that the registration fails. If you open the Python Interactor do you see any red text in there? If so, can you please post the log? You can find it in About / Report a problem.</p>

---

## Post #10 by @Marzieh_Golabbakhsh (2018-11-13 15:18 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="9" data-topic="4607" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Rigid registration by definition does not include scaling. Segment Registration however performs deformable registration as well, which does. You need to make sure that the deformable transform is applied on your segmentation.</p>
<p>It is also possible that the registration fails. If you open the Python Interactor do you see any red text in there? If so, can you please post the log? You can find it in About / Report a problem.</p>
</blockquote>
</aside>
<p>This is my log:</p>
<pre><code class="lang-auto">Python 2.7.13 (default, Dec 20 2017, 00:16:35)

[GCC 4.6.4] on linux2

&amp;gt;&amp;gt;&amp;gt;

Performing registration workflow

Cropping moving volume

Pre-aligning segmentations

Fixed segment bounds: [21.5, 87.5, 204.856399536133, 384.85639953613304, -139.567398071289, 84.432601928711]

Moving segment bounds: [18.5, 75.5, 65.85639953613301, 217.856399536133, 69.432601928711, 213.432601928711]

Moving to fixed segment translation: [7.5, 153.00000000000003, -169.0]

Resampling fixed volume

Creating contour labelmaps

Performing distance based registration

Traceback (most recent call last):

File &amp;quot;/home/marzieh/.config/NA-MIC/Extensions-26813/SlicerProstate/lib/Slicer-4.8/qt-scripted-modules/DistanceMapBasedRegistration.py&amp;quot;, line 249, in onApplyButton

logic.run(self.parameterNode)

File &amp;quot;/home/marzieh/.config/NA-MIC/Extensions-26813/SlicerProstate/lib/Slicer-4.8/qt-scripted-modules/DistanceMapBasedRegistration.py&amp;quot;, line 356, in run

(bbMin,bbMax) = self.getBoundingBox(fixedLabelNodeID, movingLabelNodeID)

File &amp;quot;/home/marzieh/.config/NA-MIC/Extensions-26813/SlicerProstate/lib/Slicer-4.8/qt-scripted-modules/DistanceMapBasedRegistration.py&amp;quot;, line 501, in getBoundingBox

unionLabelImage = (cast.Execute(fixedLabelImage) + cast.Execute(movingLabelImage)) &amp;gt; 0

File &amp;quot;/home/marzieh/Downloads/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/SimpleITK/SimpleITK.py&amp;quot;, line 4254, in __add__

return Add( self, other )

File &amp;quot;/home/marzieh/Downloads/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/SimpleITK/SimpleITK.py&amp;quot;, line 11002, in Add

return _SimpleITK.Add(*args)

RuntimeError: Exception thrown in SimpleITK Add: /home/kitware/Dashboards/Package/Slicer-481-package/ITKv4/Modules/Core/Common/include/itkImageToImageFilter.hxx:241:

itk::ERROR: AddImageFilter(0x7f469c0): Inputs do not occupy the same physical space!

InputImage Origin: [-9.4500000e+01, -5.3800000e+02, -3.0900000e+02], InputImage_1 Origin: [-8.2500000e+01, -3.7100000e+02, -1.6900000e+02]

Tolerance: 1.0000000e-06

Setting up result visualization

Performing registration workflow

Cropping moving volume

Pre-aligning segmentations

Fixed segment bounds: [29.0, 95.0, 357.85639953613304, 537.856399536133, -308.567398071289, -84.567398071289]

Moving segment bounds: [26.0, 83.0, 218.85639953613304, 370.85639953613304, -99.567398071289, 44.432601928710994]

Moving to fixed segment translation: [7.5, 153.0, -169.0]

Resampling fixed volume

Creating contour labelmaps

Performing distance based registration

Traceback (most recent call last):

File &amp;quot;/home/marzieh/.config/NA-MIC/Extensions-26813/SlicerProstate/lib/Slicer-4.8/qt-scripted-modules/DistanceMapBasedRegistration.py&amp;quot;, line 249, in onApplyButton

logic.run(self.parameterNode)

File &amp;quot;/home/marzieh/.config/NA-MIC/Extensions-26813/SlicerProstate/lib/Slicer-4.8/qt-scripted-modules/DistanceMapBasedRegistration.py&amp;quot;, line 356, in run

(bbMin,bbMax) = self.getBoundingBox(fixedLabelNodeID, movingLabelNodeID)

File &amp;quot;/home/marzieh/.config/NA-MIC/Extensions-26813/SlicerProstate/lib/Slicer-4.8/qt-scripted-modules/DistanceMapBasedRegistration.py&amp;quot;, line 501, in getBoundingBox

unionLabelImage = (cast.Execute(fixedLabelImage) + cast.Execute(movingLabelImage)) &amp;gt; 0

File &amp;quot;/home/marzieh/Downloads/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/SimpleITK/SimpleITK.py&amp;quot;, line 4254, in __add__

return Add( self, other )

File &amp;quot;/home/marzieh/Downloads/Slicer-4.8.1-linux-amd64/lib/Python/lib/python2.7/site-packages/SimpleITK/SimpleITK.py&amp;quot;, line 11002, in Add

return _SimpleITK.Add(*args)

RuntimeError: Exception thrown in SimpleITK Add: /home/kitware/Dashboards/Package/Slicer-481-package/ITKv4/Modules/Core/Common/include/itkImageToImageFilter.hxx:241:

itk::ERROR: AddImageFilter(0xa6c97a0): Inputs do not occupy the same physical space!

InputImage Origin: [-1.0200000e+02, -6.9100000e+02, -4.7800000e+02], InputImage_1 Origin: [-9.0000000e+01, -5.2400000e+02, -3.3800000e+02]

Tolerance: 1.0000000e-06

Setting up result visualization
</code></pre>

---
