---
topic_id: 18629
title: "Slicer Dicom To Nrrd"
date: 2021-07-11
url: https://discourse.slicer.org/t/18629
---

# Slicer Dicom to NRRD

**Topic ID**: 18629
**Date**: 2021-07-11
**URL**: https://discourse.slicer.org/t/slicer-dicom-to-nrrd/18629

---

## Post #1 by @SyedaFatima123 (2021-07-11 13:30 UTC)

<p>Hello I need urgent help . I have a dataset of caner patients, every patient with an ID has a folder with 28 dcm MRI images . I am using slicer to convert it to NRRD format but I want to ask is there any way I can convert the dcm files of each patients to images and labels , so that i can use it in pyradiomics library to extract shape features ?<br>
Thank you . Any help is appreciated</p>

---

## Post #2 by @lassoan (2021-07-11 15:43 UTC)

<p>Do you have segmentations (labels) in your DICOM files or you need to segment the images?</p>

---

## Post #3 by @SyedaFatima123 (2021-07-11 16:58 UTC)

<p>I need to segment the images , but how do I segment the images in a way that I have both image and its label.<br>
I need it so that I can run pyradiomics library code available on github .</p>

---

## Post #4 by @SyedaFatima123 (2021-07-11 17:03 UTC)

<aside class="onebox githubfolder" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/tree/master/data">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/AIM-Harvard/pyradiomics/tree/master/data" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/AIM-Harvard/pyradiomics/tree/master/data" target="_blank" rel="noopener nofollow ugc">AIM-Harvard/pyradiomics</a></h3>

  <p><a href="https://github.com/AIM-Harvard/pyradiomics/tree/master/data" target="_blank" rel="noopener nofollow ugc">master/data</a></p>

  <p><span class="label1">Open-source python package for the extraction of Radiomics features from 2D and 3D images and binary masks. Support: https://discourse.slicer.org/c/community/radiomics</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
I need the data in this way (given in the provided folder link , cancer1_image.nrrd and caner1_label.nrrd ) I have converted to NRRD using Slicer what do i do next .<br>
Thank you</p>

---

## Post #5 by @pieper (2021-07-11 17:32 UTC)

<p>To answer your question, if you only have the original MR scans for most cases you will need to perform the segmentation of the structures of interest by hand using the Segment Editor, then you can export the MR and segmentation to nrrd files that work with pyradiomics.  Have a read through the tutorials and documentation and let us know if anything is unclear.</p>
<p>Just as a word of caution, extracting image-based radiomics from MRI can give results that are difficult to interpret because most kinds of MR acquisitions are not in standardized units.  Even for scans that are expected to have quantitative meaning the results can be mixed.</p>
<p>See this paper for more information:<br>
<a href="https://www.nature.com/articles/s41598-019-45766-z" class="onebox" target="_blank" rel="noopener">https://www.nature.com/articles/s41598-019-45766-z</a></p>

---

## Post #6 by @SyedaFatima123 (2021-07-11 18:44 UTC)

<p>All are MRI scans, if you can tell me what basically is the label.nrrd mentioned in the github directory …is the label name of image or is it something else ?<br>
Suppose if I have an MRI scan saved with patient ID’s … Would the patient ID be considered a label and MRI scan would be the image of course,</p>

---

## Post #7 by @pieper (2021-07-11 22:39 UTC)

<p>A label in this case means a labelmap volume like what is <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html?highlight=labelmap#export-segmentation-to-labelmap-volume-file">described here</a>.</p>

---

## Post #8 by @SyedaFatima123 (2021-07-12 14:00 UTC)

<p>thank you so much , the issue was resolved … one last question . can you please tell me about the data used in github repository …is the image already segmented ?<br>
actually I have dcm files(MRI scans) belonging to one patient what should i do next ? i want to convert them in same format as given in directory .<br>
I am thinking to first convert them to NRRD and then convert NRRD image to segment and label map? Is that right , if not please tell me what should i do then to obtain both label map and image from single NRRD file.</p>

---

## Post #9 by @pieper (2021-07-12 14:52 UTC)

<p>The labels in radiomics refer to spatial regions over which the features should be calculated.  For example, brain_image.nrrd has the MRI of the head and brain_label is the segmentation of the tumor region like in the picture below (the sample data from the pyradiomics repository).  The radiomics features can include things like size of the label, whether it’s generally spherical vs. flat, etc.  It can also include signal features, like bright vs dark, smooth vs speckled, etc, but as I mentioned this can not be valuable for MRI.</p>
<p>So if you have a new set of MRI, you need to segment it as appropriate for your use case and then calculate the features.  If you aren’t familiar with nrrd files, you might find the SlicerRadiomics extension  a good way to get going.  You can get it from the extension manager.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64fbb7b2ef62618770a1902972f231a4c0c805b8.jpeg" data-download-href="/uploads/short-url/epl347JFLvZBW2keXKu6KETK14Y.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64fbb7b2ef62618770a1902972f231a4c0c805b8_2_690x374.jpeg" alt="image" data-base62-sha1="epl347JFLvZBW2keXKu6KETK14Y" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64fbb7b2ef62618770a1902972f231a4c0c805b8_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64fbb7b2ef62618770a1902972f231a4c0c805b8_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64fbb7b2ef62618770a1902972f231a4c0c805b8_2_1380x748.jpeg 2x" data-dominant-color="797981"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1638×888 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @SyedaFatima123 (2021-07-13 15:44 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="18629">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>de things like size of the l</p>
</blockquote>
</aside>
<p>Got It! Thanks alot.</p>

---

## Post #11 by @SyedaFatima123 (2021-07-14 15:44 UTC)

<p>i have tried segmenting the t2 weighted images using thresholding but I don’t know where the tumor is present…Do i need to consult a radiologist because i need to find region of interest<br>
?Or will the pyradiomics library automatically calculate the  ROI from segmented parts.</p>

---

## Post #12 by @pieper (2021-07-14 18:15 UTC)

<p>To my knowledge there are currently no good fully automated tumor segmentation tools that work on generic data.  You may be able to find some research tools that give good results for some challenge datasets and you can try to see if they work on your data.  Reading up on <a href="https://www.med.upenn.edu/cbica/brats2021/">the BraTS challenge</a> should give you an idea what to expect.</p>

---

## Post #13 by @lassoan (2021-07-15 15:25 UTC)

<aside class="quote no-group" data-username="SyedaFatima123" data-post="11" data-topic="18629">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/syedafatima123/48/11567_2.png" class="avatar"> SyedaFatima123:</div>
<blockquote>
<p>Do i need to consult a radiologist because i need to find region of interest</p>
</blockquote>
</aside>
<p>Yes. This is key to the clinical success of most medical image computing project. You need to have a good working relationship with clinicians and meet them regularly, not just because of getting help on tasks like identifying tumors, but so that you can identify problems that are clinically relevant and technically feasible to solve.</p>

---
