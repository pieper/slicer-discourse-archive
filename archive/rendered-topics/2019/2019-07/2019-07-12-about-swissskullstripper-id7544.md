# About SwissSkullStripper

**Topic ID**: 7544
**Date**: 2019-07-12
**URL**: https://discourse.slicer.org/t/about-swissskullstripper/7544

---

## Post #1 by @otanit (2019-07-12 02:26 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 4.10.1<br>
Expected behavior: Install SwissSkullStripper and calculate intracranial content volume with it.<br>
Actual behavior: Cannot install SwissSkullStripper and use the necessary modules in it.</p>
<p>I’m trying to calculate intracranial content volumes using SwissSkullStripper. However, I don’t know how to install it.<br>
I appreciate any advice and Information on its installation and usage.<br>
Thanks a lot.</p>

---

## Post #2 by @cyufu (2019-07-12 05:03 UTC)

<p>Crtl + 4 open Extensions Manager</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2dcca82df07f7f3966806c19dfeced193c2e29d.png" data-download-href="/uploads/short-url/wmUWXAh8YOyu9znq7DSq4CzTsmx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2dcca82df07f7f3966806c19dfeced193c2e29d_2_690x497.png" alt="image" data-base62-sha1="wmUWXAh8YOyu9znq7DSq4CzTsmx" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2dcca82df07f7f3966806c19dfeced193c2e29d_2_690x497.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2dcca82df07f7f3966806c19dfeced193c2e29d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2dcca82df07f7f3966806c19dfeced193c2e29d.png 2x" data-dominant-color="EFF1F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">897×647 51.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>More</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/SwissSkullStripper" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/4.10/Modules/SwissSkullStripper</a></p>

---

## Post #3 by @otanit (2019-07-14 10:21 UTC)

<aside class="quote no-group" data-username="cyufu" data-post="2" data-topic="7544">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cyufu/48/1779_2.png" class="avatar"> cyufu:</div>
<blockquote>
<p>Extensions Manager</p>
</blockquote>
</aside>
<p>Thank you very much for your kind advice.<br>
Could you please inform me how can I go to the Extensions Manager web site?<br>
I tried to find it but I couldn’t.</p>
<p>I am trying to use 3D slicer and Skull Stripper on the windows OS (not Linux).<br>
I appreciate your kind information and advice.</p>
<p>Best,</p>

---

## Post #4 by @lassoan (2019-07-14 13:42 UTC)

<aside class="quote no-group" data-username="otanit" data-post="3" data-topic="7544">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/ea666f/48.png" class="avatar"> otanit:</div>
<blockquote>
<p>Could you please inform me how can I go to the Extensions Manager web site?</p>
</blockquote>
</aside>
<p>You don’t need to open the website manually, but use the extension manager from Slicer as <a class="mention" href="/u/cyufu">@cyufu</a></p>
<p>If for some reason you were interested in how to access the extension manager from outside Slicer, you can find instructions here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager" class="inline-onebox">Documentation/Nightly/SlicerApplication/ExtensionsManager - Slicer Wiki</a></p>

---

## Post #5 by @otanit (2019-07-14 22:33 UTC)

<p>Following your kind information, I could download SwissSullStripper and add it to 3D Slicer.<br>
Then, I input all the necessary files in the SwissSkullStripper module following the instruction of SwissSkullStripper (please see the attached photo).<br>
In this process, I could not select Atlas Mask Volume at first.<br>
Therefore, I chose Rename current LabelMapVolume and rename it as “atlasMask”, and click “Apply”.<br>
However, the following error message appeared after that.<br>
What should I do to address this problem?<br>
I appreciate your kind instruction and advice.</p>
<p>ERROR MESSAGE shown in the SwissSkullStripper module.</p>
<hr>
<p>Failed to read input atlas label volume.<br>
itk::ExceptionObject (00000028C6DDA100)<br>
Location: “unknown”<br>
File: D:\D\S\Slicer-4101-build\ITK\Modules\IO\ImageBase\src\itkImageIOBase.cxx<br>
Line: 378<br>
Description: itk::ERROR: MRMLIDImageIO(00000028CB555940): Unknown component type: 0</p>
<hr>
<p>H<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e28fc9af170df076793970570a410d4c96795a5.jpeg" data-download-href="/uploads/short-url/mz9fKqPSlybZyVmby4aBxI646RT.jpeg?dl=1" title="Question%20photo%20about%20SwissSkullStripper" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e28fc9af170df076793970570a410d4c96795a5_2_690x388.jpeg" alt="Question%20photo%20about%20SwissSkullStripper" data-base62-sha1="mz9fKqPSlybZyVmby4aBxI646RT" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e28fc9af170df076793970570a410d4c96795a5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e28fc9af170df076793970570a410d4c96795a5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e28fc9af170df076793970570a410d4c96795a5_2_1380x776.jpeg 2x" data-dominant-color="666C7B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Question%20photo%20about%20SwissSkullStripper</span><span class="informations">5504×3096 3.47 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2019-07-16 13:01 UTC)

<p>It seems that you have not loaded the mask image as a labelmap. I’ve updated <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper" rel="nofollow noopener">Swiss skull stripper module documentation</a> to make this step more clear. Please follow the steps described there and let us know if you have any problems.</p>

---

## Post #7 by @otanit (2019-07-22 22:34 UTC)

<p>Thank you for your kind advice.<br>
Following your advice and module documentation, I could use mask image as a labelmap and create Patient Mask Label by SwissSkullStripper.</p>
<p>I have another consultation here.<br>
I need to calculate intracranial content volume.</p>
<ol>
<li>To my understanding, the Patient Mask Label volume is the same as intracranial content  volume.</li>
<li>Since the Mask Label is not segmented, I have to use Label Statistics in order to calculate Patient Mask Label volume (intracranial content volume) in this case.<br>
Is my understanding above correct?<br>
I would like to receive your advice, if I have some misunderstanding or there is other necessary steps for calculating intracranial volume.<br>
I appreciate your kind advice.</li>
</ol>

---

## Post #8 by @lassoan (2019-07-23 18:46 UTC)

<p>The steps are correct, you can compute the intracranial volume like that.</p>
<p>For more metrics, you can convert “Patient Mask Label volume” to segmentation in Data module (right-click on the label volume and choose to convert to segmentation) and use Segment Statistics module.</p>

---

## Post #9 by @otanit (2019-07-24 01:09 UTC)

<p>I greatly appreciate your kind advice.<br>
I could calculate ICC volume with your and Dr. cyufu’s instruction.<br>
Thanks a lot.</p>

---
