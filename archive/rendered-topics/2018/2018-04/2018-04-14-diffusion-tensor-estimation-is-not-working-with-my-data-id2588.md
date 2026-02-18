# Diffusion Tensor Estimation is not working with my data

**Topic ID**: 2588
**Date**: 2018-04-14
**URL**: https://discourse.slicer.org/t/diffusion-tensor-estimation-is-not-working-with-my-data/2588

---

## Post #1 by @mali (2018-04-14 13:27 UTC)

<p>Hello everyone,</p>
<p>I hope some of you can help me with my problem. My diffusion scans (Siemens) have the volume type MRMLMulti. I used the ResampleScalar/Vector/DWI Volume command to get a DWI output and I can see its different components in the Volumes module. However, I am not able to get a DTI image using the DiffusionTensorEstimation command. It looks like if there were no directions at all.<br>
Does any of you have an idea how to fix this?</p>
<p>Thanks a lot in advance!</p>

---

## Post #2 by @ihnorton (2018-04-14 13:28 UTC)

<p>Hi <a class="mention" href="/u/mali">@mali</a>. You need to convert your data to a <code>vtkMRMLDiffusionWeightedVolumeNode</code> using the DWIConvert module. This will record the gradient information required to reconstruct tensors using the Tensor Estimation module (whereas MRMLMulti will not save that information).</p>
<p>Please see <a href="http://dmri.slicer.org/tutorials/Slicer-4.8/DWIConverterTutorial.pdf">http://dmri.slicer.org/tutorials/Slicer-4.8/DWIConverterTutorial.pdf</a></p>

---

## Post #3 by @mali (2018-04-14 16:32 UTC)

<p>Hi Isaiah,</p>
<p>thanks a lot for your reply! I did as you suggested but unfortunately, I am getting the following error description:</p>
<p>Description: itk::ERROR: ImageSeriesReader(0x106ed02d0): Size mismatch! The size of  /Volumes/INTENSO/dtiHNO/PROB01/DTI_HNO_PROB_01.MR.RESOLVE-EPI-DIFFUSION_HNO_ISLAND_STUDIE.0012.0001.2017.10.27.17.10.11.490963.131770703.IMA is [400, 512, 1] and does not match the required size [256, 256, 1] from file /Volumes/INTENSO/dtiHNO/PROB01/DTI_HNO_PROB_01.MR.RESOLVE-EPI-DIFFUSION_HNO_ISLAND_STUDIE.0010.0001.2017.10.27.17.10.11.490963.150815796.IMA</p>
<p>Do you know a way to solve this problem?<br>
Thanks a lot for your help!</p>

---

## Post #4 by @mali (2018-04-14 16:42 UTC)

<p>I tried the same with different data and now it is saying:</p>
<pre><code class="lang-auto">Description: ImageIO returns IO region that does not fully contain the requested regionRequested region: ImageRegion (0x7fff5fbf9c10)
  Dimension: 3
  Index: [0, 0, 0]
  Size: [400, 512, 1]
StreamableRegion region: ImageRegion (0x7fff5fbf9c48)
  Dimension: 3
  Index: [0, 0, 0]
  Size: [160, 160, 1]



Exception creating converter 
itk::InvalidRequestedRegionError (0x107001c08)
Location: "unknown" 
File: /Users/kitware/Dashboards/Package/Slicer-481-package/ITKv4/Modules/IO/ImageBase/include/itkImageFileReader.hxx
Line: 350
Description: ImageIO returns IO region that does not fully contain the requested regionRequested region: ImageRegion (0x7fff5fbf9c10)
  Dimension: 3
  Index: [0, 0, 0]
  Size: [400, 512, 1]
StreamableRegion region: ImageRegion (0x7fff5fbf9c48)
  Dimension: 3
  Index: [0, 0, 0]
  Size: [160, 160, 1]
</code></pre>
<p>Can you give me some advice?</p>

---

## Post #5 by @ihnorton (2018-04-16 16:42 UTC)

<p>Usually this error happens when the directory you are loading with DWIConvert contains DICOMs from different acquisitions. The DICOM needs to be sorted into directories by series.</p>
<p>You could try using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM">DICOM browser module</a>. Because of some issues with tag identification, please select <em>only</em> <strong>DICOMDiffusionVolumePlugin</strong>:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a17ab466d81cf7229fc20129c5904cb6aecea0f9.png" alt="image" data-base62-sha1="n2vLvNDXs8EjWjgz0NC8GzWLr9n" width="327" height="61"></p>
<p>Then click <strong>Examine</strong>; then try to <strong>Load</strong> your diffusion series. The DICOM browser should do the sorting (it copies the files into a temporary directory). It should recognize Siemens data using the standard tags, but may not recognize data from some scanners.</p>
<p>If that doesn’t work, you could try sorting with the tool mentioned here:</p>
<aside class="quote quote-modified" data-post="6" data-topic="2553">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/is-there-any-method-to-convert-volume-to-diffusiontensorvolume/2553/6">Is there any method to convert volume to DiffusionTensorvolume?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I think the most likely issue is still mis-sorting: DWIConvert requires that all files to be converted are from the same series (or at least identical acquisition parameters) and alone in one folder. You could try this script to do the sorting first: 


That said, if the data is from a Prisma or newer scanner, then I’m not sure if DWIConvert fully supports it yet. Please let us know the following tag information: (0008,0070) (0008,1090) (0018,1020) 
e.g.: 
(0008,0070) LO [SIEMENS]               …
  </blockquote>
</aside>


---

## Post #6 by @mali (2018-04-23 19:59 UTC)

<p>Hello Isaiah,</p>
<p>thanks a lot for your advice! I really appreciated it and it worked! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Best,<br>
Marlene</p>

---
