---
topic_id: 20366
title: "Rt Struct Available Would Like To Try A Different Segmentati"
date: 2021-10-26
url: https://discourse.slicer.org/t/20366
---

# RT STRUCT available. Would like to try a different segmentation on the CT images.

**Topic ID**: 20366
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/rt-struct-available-would-like-to-try-a-different-segmentation-on-the-ct-images/20366

---

## Post #1 by @MPhilip (2021-10-26 18:55 UTC)

<p>Operating system:<br>
Edition	Windows 10 Enterprise<br>
Version	20H2<br>
OS build	19042.1288<br>
Experience	Windows Feature Experience Pack 120.2212.3920.0<br>
Processor: Intel(R) Core™ i5-10310U CPU @ 1.70GHz   2.21 GHz<br>
System type: 64-bit operating system, x64-based processor</p>
<p>Slicer version:4.11.20210226 r29738 / 7a593c8<br>
Expected behavior: I have head and neck cancer PET/CT dicom images from TCIA(The Cancer Imaging Archive)(298 patient images). The images are manually segmented. The RT struct is also available. Now I would like to try a different segmentation method on these images. I loaded RT STRUCT and PET/CT images and could figure out the GTV needed(BY hiding all other segmented regions). (There are many different ROIs segmented in the RTSTRUCT, but I need only GTVs). The problem is I am unable to use ‘segment editor’ when the RTSTRUCT is loaded. If I load the CT images alone, I have trouble identifying the GTV for segmentation. Is there a way to do thiS? I am a new 3D slicer user<br>
Also, could you please advice me on, once segmented how to import these images to Pyradiomics for feature extraction?. I am trying to verify feature stability across different segmentation methods.<br>
Many thanks in advance.</p>

---

## Post #2 by @cpinter (2021-10-26 19:43 UTC)

<p>It would be helpful to hear what it means exactly that you are unable to use Segment Editor. I guess it says that you cannot edit the segmentation because the master representation is not labelmap. Is this correct?</p>
<p>In any case, in order to edit the structure set, I would</p>
<ol>
<li>Clone the segmentation in the Data module to preserve the original data for the session</li>
<li>Go to Segmentations module, select the cloned node, then in the Representations section, in the line of Binary labelmap click Make master</li>
<li>Go to Segment Editor and select the cloned segmentation, which you could now edit</li>
</ol>

---

## Post #3 by @MPhilip (2021-10-26 20:03 UTC)

<p>Thanks for your response.<br>
What you said is correct. I can’t find it as a binary label map. All I can find is planar contour. When I tried to create a binary label map from RTstruct, 3d slicer was not responding. Maybe I did a mistake there. When I select segment editor,<br>
the Segmentation appears as ‘RTSTRUCT’ and Master Volume as ‘CT IMAGES’.<br>
I will try what you suggested.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e898c7e907c803c5d639ba7305beaa54d873b45.png" data-download-href="/uploads/short-url/8VeiBGrbOqZ9z8BEklqlGjyur4h.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e898c7e907c803c5d639ba7305beaa54d873b45.png" alt="image" data-base62-sha1="8VeiBGrbOqZ9z8BEklqlGjyur4h" width="690" height="182" data-dominant-color="EFEFEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">862×228 6.82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6416676549c344718dec6d1267ce4c6169b94bf5.png" data-download-href="/uploads/short-url/ehpKk4gRUHZTjf6RFCGyl20Go3H.png?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6416676549c344718dec6d1267ce4c6169b94bf5.png" alt="Capture1" data-base62-sha1="ehpKk4gRUHZTjf6RFCGyl20Go3H" width="690" height="207" data-dominant-color="F1F1F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1049×316 13.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f655a87f79544f90faf28c0c1bba2524ffb4f9b5.jpeg" data-download-href="/uploads/short-url/z9aYJsgaKv2FKcQHu8FcODZ2BnL.jpeg?dl=1" title="Capture2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f655a87f79544f90faf28c0c1bba2524ffb4f9b5_2_690x297.jpeg" alt="Capture2.PNG" data-base62-sha1="z9aYJsgaKv2FKcQHu8FcODZ2BnL" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f655a87f79544f90faf28c0c1bba2524ffb4f9b5_2_690x297.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f655a87f79544f90faf28c0c1bba2524ffb4f9b5_2_1035x445.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f655a87f79544f90faf28c0c1bba2524ffb4f9b5_2_1380x594.jpeg 2x" data-dominant-color="616B73"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2.PNG</span><span class="informations">1873×808 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-10-26 20:20 UTC)

<p>Please try with the latest Slicer Preview Release. After clicking “Create” for binary labelmap, be patient, conversion may take a while if you have many segments or your computer is low on memory.</p>
<p>Which TCIA data set is this?</p>

---

## Post #5 by @MPhilip (2021-10-26 20:26 UTC)

<p>The link to TCIA which has the head and neck cancer dataset  -<a>https://wiki.cancerimagingarchive.net/display/Public/Head-Neck-PET-CT</a><br>
Thanks for your response. I was trying to follow what <a class="mention" href="/u/cpinter">@cpinter</a> suggested. But in the segment editor module, I am unable to find the cloned GTV. Could you please suggest on where can I find it?<br>
What I could see was the below snippet when I tried to change ‘Master Volume’ from CT images to GTV. Is this needed?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d6682cd4424975e22a91b862f6c790cfa942992.png" data-download-href="/uploads/short-url/kaSX1yQ4YMYHMwfOTo9w3qdzdK2.png?dl=1" title="Capture3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d6682cd4424975e22a91b862f6c790cfa942992.png" alt="Capture3" data-base62-sha1="kaSX1yQ4YMYHMwfOTo9w3qdzdK2" width="690" height="188" data-dominant-color="E8EAEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture3</span><span class="informations">954×261 13.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thank you!</p>

---

## Post #7 by @MPhilip (2021-10-26 21:32 UTC)

<p>Just downloaded the latest slicer preview release. But everything seems so slow and not working as in the stable version(it remains stuck). Close button seems to not appear in some cases. Any suggestions would be highly appreciated. Thanks!</p>

---

## Post #8 by @lassoan (2021-10-26 23:26 UTC)

<p>Which data set you have problem with exactly? Can you tell the patient ID or study ID?</p>

---

## Post #9 by @lassoan (2021-10-27 03:21 UTC)

<p>I’ve tested loading a few TCIA Head-Neck-PET-CT data sets, editing the structure sets and exporting the modified segment to DICOM and it all worked without issues, using latest Slicer Preview Release.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F9AhoerSgdc" data-video-title="TCIA H&amp;N RTSTRUCT editing" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F9AhoerSgdc" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F9AhoerSgdc/maxresdefault.jpg" title="TCIA H&amp;N RTSTRUCT editing" width="" height="">
  </a>
</div>

<p>I don’t see any significant time difference between Slicer Preview Release and latest Slicer Stable Release when loading or editing segments.</p>

---

## Post #10 by @MPhilip (2021-10-27 09:07 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> for the video shared. I’m sure it will be of great help to me.<br>
I will try again on the preview release.<br>
As I have manually segmented images, I would like to try a different segmentation on the images, for eg: Otsu method. Do I have to clone the segment as Csaba mentioned before to try another segmentation method, to segment only the GTV? May I know how can I do that? And later I want to extract features from this.</p>
<p>This is the screen I see:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfe7c165726e356ca88b8a52ec92fc3671c4ff33.png" data-download-href="/uploads/short-url/tFdmWRY3m42farppNBZWsET2F91.png?dl=1" title="Capture4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfe7c165726e356ca88b8a52ec92fc3671c4ff33_2_690x365.png" alt="Capture4" data-base62-sha1="tFdmWRY3m42farppNBZWsET2F91" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfe7c165726e356ca88b8a52ec92fc3671c4ff33_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfe7c165726e356ca88b8a52ec92fc3671c4ff33_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfe7c165726e356ca88b8a52ec92fc3671c4ff33_2_1380x730.png 2x" data-dominant-color="DAE7EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture4</span><span class="informations">1910×1013 78.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks in advance</p>

---

## Post #11 by @cpinter (2021-10-27 10:31 UTC)

<p>I would not use thresholding for segmentation, but Otsu method is available in the Threshold effect in Segment Editor.</p>
<p>You don’t need to clone, only if it makes your workflow easier. I recommend that you try all the things we suggeted, take a look at the Segment Editor effects and documentation (<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#segment-editor-module-overview">here</a> and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">here</a>), as well as the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">tutorials</a>, and find the tools that fit your exact needs.</p>

---

## Post #12 by @MPhilip (2021-10-27 10:39 UTC)

<p>Thank you very much <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
I will try all the things you suggested and will see how it works. Thanks again.</p>

---

## Post #14 by @MPhilip (2021-11-04 15:06 UTC)

<p>In continuation to the question I asked previously, I have ~300 PET/CT images of head and neck cancer patients got from TCIA with its RTSTRUCT. The region of interest is different in each case eg: GTV, GTV_67.5Gy, GTV_70Gy. I wish to extract features from these ROIs(from manually segmented images) and also from the ROIs obtained by trying a different segmentation method on these images(both PET and CT). Is there a way to automate this task using Python script or so? It would have been a time saver. I found something like this here[<a href="https://discourse.slicer.org/t/is-there-a-way-to-build-a-macro-script-out-of-segment-editor-steps/4170/5" class="inline-onebox">Is there a way to build a macro/script out of segment editor steps? - #5 by pieper</a>]<br>
Thanks</p>

---

## Post #15 by @lassoan (2021-11-04 19:51 UTC)

<p>Yes, all the steps that you perform in the GUI can be automated using Python scripting. The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">Slicer script repository</a> is a good starting point but if you cannot find an example for anything that you would like to do then you can search this forum and ask us here, too.</p>

---
