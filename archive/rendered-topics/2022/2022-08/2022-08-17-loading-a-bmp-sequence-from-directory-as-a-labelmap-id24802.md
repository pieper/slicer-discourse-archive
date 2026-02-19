---
topic_id: 24802
title: "Loading A Bmp Sequence From Directory As A Labelmap"
date: 2022-08-17
url: https://discourse.slicer.org/t/24802
---

# Loading a .bmp sequence from directory as a LabelMap

**Topic ID**: 24802
**Date**: 2022-08-17
**URL**: https://discourse.slicer.org/t/loading-a-bmp-sequence-from-directory-as-a-labelmap/24802

---

## Post #1 by @Windy (2022-08-17 10:27 UTC)

<p>Operating system: Windows 10 Education<br>
Slicer version: 5.0.2</p>
<p>Expected behavior:<br>
I have a set of segmented slices in a directory. It has 2 classes (0 and 255). The image format is .bmp. I want to load them as a segmentation.</p>
<p>Actual behavior:<br>
I was following the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file" rel="noopener nofollow ugc">official docs</a>. However, when I load as a volume and select <code>LabelMap</code> it gives the following error.</p>
<pre><code class="lang-auto">UpdateFromSeries: Unsupported number of components: 1 != 3

vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type LabelMapVolume [fullName = D:/roi_1_resampled/labelled/masks/dilate_roi_1_resampled_0476.bmp]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 816 files. File reader used the archetype file name of D:/roi_1_resampled/labelled/masks/dilate_roi_1_resampled_0476.bmp [reader 0th file name = D:/roi_1_resampled/labelled/masks/dilate_roi_1_resampled_0476.bmp].


vtkMRMLStorageNode::ReadData: Failed to read node dilate_roi_1_resampled_0476_2 (vtkMRMLLabelMapVolumeNode1) from filename='D:/roi_1_resampled/labelled/masks/dilate_roi_1_resampled_0476.bmp'
</code></pre>

---

## Post #2 by @pieper (2022-08-17 16:39 UTC)

<p>You can try using the ImageStacks module from SlicerMorph instead - it has more options and should work for you.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener">SlicerMorph/Docs/ImageStacks at master · SlicerMorph/SlicerMorph</a></h3>

  <p><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener">master/Docs/ImageStacks</a></p>

  <p><span class="label1">Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2022-08-17 23:30 UTC)

<aside class="quote no-group" data-username="Windy" data-post="1" data-topic="24802">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/91b2a8/48.png" class="avatar"> Windy:</div>
<blockquote>
<p>I was following the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file">official docs</a>. However, when I load as a volume and select <code>LabelMap</code> it gives the following error.</p>
</blockquote>
</aside>
<p>Labelmap conversion from image sequences is a two step process: IMport then convert. I don’t think you can directly import an image stack as a labelmap. (Instructions you shared are for volumes that are already in NRRD or other Slicer compatible volumetric formats like NRRD or NIFTI).</p>
<p>The simplest solution is to use the ImageStacks from SlicerMorph extension as <a class="mention" href="/u/pieper">@pieper</a> indicated. Once you import the volume, right click on it in the Data module, and choose “edit properties”, which wil take you to the volumes module. Expand the Volume Information tab, and click the button that says <strong>Convert</strong>.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34ba449b61169a7daee985a3ec21d6d9936f68f9.png" alt="image" data-base62-sha1="7wrU9UsQi8bckfFap2jB9LAacNr" width="571" height="435">.</p>
<p>Slicer does not use labelmaps for segmentations anymore. If you want to continue your segmentation in slicer (or create models out of these segmentations). You have one more step where you convert the labelmap to segmentation object. You can easily do that by right clicking the new labelmap object in the data module and choosing <strong>“Convert labelmap to Segmentation Node”.</strong></p>
<p>Remember to save these so that you don’t have to keep repeating these stesp.</p>

---

## Post #4 by @Windy (2022-08-18 04:42 UTC)

<p>Actually, the second part in that link says it works with any image format.</p>
<p>I followed the steps you mentioned. but I don’t get the convert button.</p>

---

## Post #5 by @pieper (2022-08-18 14:23 UTC)

<aside class="quote no-group" data-username="Windy" data-post="4" data-topic="24802">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/91b2a8/48.png" class="avatar"> Windy:</div>
<blockquote>
<p>I followed the steps you mentioned. but I don’t get the convert button.</p>
</blockquote>
</aside>
<p>What do you see instead in the window corresponding to what <a class="mention" href="/u/muratmaga">@muratmaga</a> posted?</p>

---

## Post #6 by @muratmaga (2022-08-18 16:58 UTC)

<aside class="quote no-group" data-username="Windy" data-post="4" data-topic="24802">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/91b2a8/48.png" class="avatar"> Windy:</div>
<blockquote>
<p>says it works with any image format</p>
</blockquote>
</aside>
<p>Thanks for point it out. That probably needs to be corrected, Slicer treats JPG/PNG/BMP as vector (RGB) images, whereas a labelmap is a scalar image. I expect that was the reason for the error you posted:</p>
<pre><code class="lang-auto">UpdateFromSeries: Unsupported number of components: 1 != 3
</code></pre>
<p>As for your current question, please provide a screenshot of the VOlumes module with the Volume Information tab expanded.</p>

---

## Post #7 by @Windy (2022-08-24 05:42 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02b40075453584c854a4b757f41984d7139499e7.png" alt="Capture23" data-base62-sha1="nUBDia87rU8vcclS1i5xUSeGvd" width="485" height="492"></p>

---

## Post #8 by @Windy (2022-08-24 05:54 UTC)

<p>Thank you for trying to help. I just went ahead and created a Nifti stack from the BMPs and imported as segmentations</p>

---

## Post #9 by @muratmaga (2022-08-24 14:53 UTC)

<p>From your screenshot above the issue is the same, if you look at the NUmber of Scalars you see it is 3 (implying a RGB volume), not 1. I suspect the voxel spacing is incorrect. Again, you can take care all of those using ImageStacks module.</p>

---
