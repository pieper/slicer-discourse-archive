---
topic_id: 5940
title: "Improvement Display 3D"
date: 2019-02-27
url: https://discourse.slicer.org/t/5940
---

# Improvement display 3d

**Topic ID**: 5940
**Date**: 2019-02-27
**URL**: https://discourse.slicer.org/t/improvement-display-3d/5940

---

## Post #1 by @dp1991 (2019-02-27 07:03 UTC)

<p>hi friends<br>
i segmented ct images, and output labeled as 50(Esophagus) 100(Heart) 150(Lung_L) 200(Lung_R) 250 (Spinal Cord)…<br>
now i will display any organ with one color ( for example  heart show red and Lung_L show blue  , etc)<br>
for this purpose, i use volume properties as attached image<br>
output display is not clear …<br>
how can i display output that any organ display exactly one color  with High transparency</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c6e7060926e829a1b2803a742f77b85e1f40480.png" data-download-href="/uploads/short-url/ftebeBlQDmWd2VUn5wC11PQNrck.png?dl=1" title="rfer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c6e7060926e829a1b2803a742f77b85e1f40480_2_690x431.png" alt="rfer" data-base62-sha1="ftebeBlQDmWd2VUn5wC11PQNrck" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c6e7060926e829a1b2803a742f77b85e1f40480_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c6e7060926e829a1b2803a742f77b85e1f40480_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c6e7060926e829a1b2803a742f77b85e1f40480_2_1380x862.png 2x" data-dominant-color="747276"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rfer</span><span class="informations">1680×1050 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2019-02-27 13:43 UTC)

<p>Hi -</p>
<p>You probably want to approach this differently.  You can import your label volume as a Slicer <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Segmentations" rel="nofollow noopener">Segmentation</a> and then enable the 3D display.</p>

---

## Post #3 by @cpinter (2019-02-27 13:56 UTC)

<p>To do that easily, right-click the labelmap node in the Data module, and select “Convert labelmap to segmentation node”. Then right-click on the new segmentation node, choose Edit properties (it will take you to the Segmentations module, same as <a class="mention" href="/u/pieper">@pieper</a> pointed to), and click Create in the Closed surface row in the Representations section. Then the 3D display will show up.</p>

---

## Post #4 by @dp1991 (2019-02-28 06:25 UTC)

<p>i have a series dicom image<br>
i segmented 5 organ with hand ( lung_L, lung_R ,heart,spinal cord , esophagus ) in vs2015<br>
and save output such as 3D.mha<br>
and open this volume with 3D Slicer 4.8.1<br>
and i try display output that one organ show with one color<br>
i chose volume rendering and show 3D output and i do volume properties<br>
on the 3d output, i see a dark line<br>
but i will,  can see a smooth surface ,<br>
for example lung_L being red, Without any black line<br>
<a class="mention" href="/u/pieper">@pieper</a> thanks for your answer, but a don’t understand your answer<br>
<a class="mention" href="/u/cpinter">@cpinter</a> i don’t find this option that you said, can u show me  steps with picture ??<br>
( my English is not well, i hope u understand my mean)</p>

---

## Post #5 by @dp1991 (2019-02-28 08:38 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> , <a class="mention" href="/u/pieper">@pieper</a>  thanks for your guidance<br>
i can solve this problem in slicer<br>
how to can i implement this operation in vtk or itk ??<br>
i segmented with my approach ( deep learning, region growing and etc)<br>
i write result output with itk in result folder<br>
final result save as 3D.mha file , any organ have one value (mention above)<br>
how can i display this output witk vtk in my C++ ( VS2015 ) code, such as  closed surface ??<br>
below link is 3D.mha<br>
<a href="https://ufile.io/n3cjh" class="onebox" target="_blank" rel="nofollow noopener">https://ufile.io/n3cjh</a></p>

---

## Post #6 by @cpinter (2019-02-28 14:53 UTC)

<p>You can use the convenience functions in the API. For example:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L197-L201" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L197-L201" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/Logic/vtkSlicerSegmentationsModuleLogic.h#L197-L201</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="197" style="counter-reset: li-counter 196 ;">
<li>/// Import all labels from a labelmap node to a segmentation node, each label to a separate segment.</li>
<li>/// The colors of the new segments are set from the color table corresponding to the labelmap volume.</li>
<li>/// \param insertBeforeSegmentId New segments will be inserted before this segment.</li>
<li>static bool ImportLabelmapToSegmentationNode(vtkMRMLLabelMapVolumeNode* labelmapNode,</li>
<li>  vtkMRMLSegmentationNode* segmentationNode, std::string insertBeforeSegmentId="");</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #7 by @dp1991 (2019-03-02 05:05 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a>  thank u for tour answer …<img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=6" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---

## Post #8 by @dp1991 (2019-03-04 09:09 UTC)

<p>hi<br>
my input is 3D.mha <a href="https://ufile.io/n3cjh" rel="noopener nofollow ugc">https://ufile.io/n3cjh</a><br>
my output is image1<br>
and i will to display as image2<br>
how to i do it ?<br>
what is equal VTK function for this process ??</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6324308cb574aa63c42621adbcdbfcc044a36739.jpeg" alt="image1" data-base62-sha1="e92NWtHzREKCmeEIRPTc2AudRwJ" width="507" height="445"></p>

---

## Post #9 by @lassoan (2019-03-04 13:46 UTC)

<aside class="quote no-group" data-username="dp1991" data-post="8" data-topic="5940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dp1991/48/3142_2.png" class="avatar"> dp1991:</div>
<blockquote>
<p>what is equal VTK function for this process ??</p>
</blockquote>
</aside>
<p>Slicer is open-source, you are free to inspect its code to see how it is implemented and even take any code and reuse it in another project.</p>

---

## Post #10 by @dp1991 (2019-03-05 12:25 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
hank you very much<br>
my previous problem solved by one example of VTK’s documentation<br>
( <a href="https://discourse.slicer.org/t/vtk-user-manual/6003" class="inline-onebox">VTK User Manual</a> )</p>

---
