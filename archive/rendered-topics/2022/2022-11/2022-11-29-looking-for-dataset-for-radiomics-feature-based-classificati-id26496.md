# Looking for dataset for radiomics feature based classification

**Topic ID**: 26496
**Date**: 2022-11-29
**URL**: https://discourse.slicer.org/t/looking-for-dataset-for-radiomics-feature-based-classification/26496

---

## Post #1 by @Devesh (2022-11-29 17:41 UTC)

<p>Hello everyone, I am a Computer science college student and new to radiomics and medical science.<br>
I want to build a radiomics feature-based classifier. I have to take CT scans Dicom images.</p>
<p>Firstly, I found a dataset NSCLC-Radiomics <a href="https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics" class="inline-onebox" rel="noopener nofollow ugc">NSCLC-Radiomics - The Cancer Imaging Archive (TCIA) Public Access - Cancer Imaging Archive Wiki</a>, where they labeled different regions of the body like left and right lung, esophagus, spine, and the abnormal tissue that is a tumor itself. From all these segments I choose the tumor segmentation and calculated the features. But these features are for Cancer patients only. For the non-cancer, I was unable to understand the ROI. Obviously, the non-cancer CT scan can’t have an ROI.</p>
<p>Is it possible to classify cancer and non-cancer patient with radiomics? If yes, then what about the ROI for the non-cancer patient? And the relevant dataset to do so.</p>
<p>After long research, I came across the dataset <strong>Data from The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A completed reference database of lung nodules on CT scans (LIDC-IDRI)</strong><br>
<a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=1966254" class="inline-onebox" rel="noopener nofollow ugc">Data from The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A completed reference database of lung nodules on CT scans (LIDC-IDRI) - The Cancer Imaging Archive (TCIA) Public Access - Cancer Imaging Archive Wiki</a>, where they mentioned that they have classified the nodules(abnormal tissue) based on their size. I read in their article <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3041807/" class="inline-onebox" rel="noopener nofollow ugc">The Lung Image Database Consortium (LIDC) and Image Database Resource Initiative (IDRI): A Completed Reference Database of Lung Nodules on CT Scans - PMC</a></p>
<blockquote>
<p>The Database contains 7371 lesions marked “nodule” by at least one radiologist. 2669 of these lesions were marked “nodule≥3 mm” by at least one radiologist, of which 928 (34.7%) received such marks from all four radiologists. These 2669 lesions include nodule outlines and subjective nodule characteristic ratings.</p>
</blockquote>
<p>and they scaled the nodule size from 1-5, (1,2 for small-size nodules, I will call them non-cancer, and 4,5 for large-size nodules, which I’ll treat as Cancer Data).<br>
I hoped that finally I found the right dataset but the dataset is so confusing.</p>
<p>I used their python package pylidc for preprocessing. After compiling it, I got multiple NumPy arrays which I don’t know how to use in pyradiomics.</p>
<p>They only accept that image with its mask. It is so confusing for me.</p>
<p>I don’t know whether to find a dataset to do so. I have spent almost a month reading about it. I have tried many datasets but found nothing relevant to my project. I really need help regarding this.</p>

---

## Post #2 by @lassoan (2022-12-01 02:33 UTC)

<aside class="quote no-group" data-username="Devesh" data-post="1" data-topic="26496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/devesh/48/17507_2.png" class="avatar"> Devesh:</div>
<blockquote>
<p>Is it possible to classify cancer and non-cancer patient with radiomics?</p>
</blockquote>
</aside>
<p>You can compute the radiomics features for any image. The basic idea is that some of the features may help in distinguishing cancer from non-cancer.</p>
<p>I would recommend to do some literature search before you dig very deep into radiomics features, because recent papers report better results with deep learning than with classic radiomics based classification.</p>
<aside class="quote no-group" data-username="Devesh" data-post="1" data-topic="26496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/devesh/48/17507_2.png" class="avatar"> Devesh:</div>
<blockquote>
<p>If yes, then what about the ROI for the non-cancer patient? And the relevant dataset to do so</p>
</blockquote>
</aside>
<p>You can randomly select regions in the same organ (away from regions that are marked as cancer) and use those as non-cancer regions. You probably don’t need a separate data set, but if you want to add some patients that don’t have cancer in the organ of interest, you can use patient data from other collections.</p>
<aside class="quote no-group" data-username="Devesh" data-post="1" data-topic="26496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/devesh/48/17507_2.png" class="avatar"> Devesh:</div>
<blockquote>
<p>I got multiple NumPy arrays which I don’t know how to use in pyradiomics</p>
</blockquote>
</aside>
<p>You can create a volume node from a numpy array using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.addVolumeFromArray">slicer.util.addVolumeFromArray</a>. Make sure you set the correct spacing in the created volume node (using <a href="https://apidocs.slicer.org/master/classvtkMRMLVolumeNode.html#aba811485373b79ecef790d32370b5ffd">SetSpacing</a>).</p>

---

## Post #3 by @Devesh (2022-12-01 03:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="26496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend to do some literature search before you dig very deep into radiomics features, because recent papers report better results with deep learning than with classic radiomics based classification.</p>
</blockquote>
</aside>
<p>Basically the motive of my project is to compare both deep learning and classic radiomics based classification. And also checking the performance of classification on both features combined.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="26496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can randomly select regions in the same organ (away from regions that are marked as cancer) and use those as non-cancer regions. You probably don’t need a separate data set</p>
</blockquote>
</aside>
<p>Sir I have tried it, I have other mask of the whole left and right lung that the data set has provided. I calculated the features by using that mask. I labelled them as non cancer. I got 100% accuracy when I tried the classification. I think this is because the size difference between the nodule and the whole left or right lung.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="26496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can create a volume node from a numpy array using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.addVolumeFromArray" rel="noopener nofollow ugc">slicer.util.addVolumeFromArray</a>. Make sure you set the correct spacing in the created volume node (using <a href="https://apidocs.slicer.org/master/classvtkMRMLVolumeNode.html#aba811485373b79ecef790d32370b5ffd" rel="noopener nofollow ugc">SetSpacing</a>).</p>
</blockquote>
</aside>
<p>I created the volume too. But the problem is those arrays after combining ended up with size of 8X512X512 or 7X512X512, whereas my original dicom series is of 120X512X512 or with some larger N slices that this generated volume node.</p>

---

## Post #5 by @lassoan (2022-12-01 05:37 UTC)

<aside class="quote no-group" data-username="Devesh" data-post="3" data-topic="26496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/devesh/48/17507_2.png" class="avatar"> Devesh:</div>
<blockquote>
<p>I have other mask of the whole left and right lung that the data set has provided. I calculated the features by using that mask. I labelled them as non cancer. I got 100% accuracy when I tried the classification. I think this is because the size difference between the nodule and the whole left or right lung.</p>
</blockquote>
</aside>
<p>You can extract regions from healthy lung tissue that has approximately the same as nodules.</p>
<aside class="quote no-group" data-username="Devesh" data-post="3" data-topic="26496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/devesh/48/17507_2.png" class="avatar"> Devesh:</div>
<blockquote>
<p>the problem is those arrays after combining ended up with size of 8X512X512 or 7X512X512, whereas my original dicom series is of 120X512X512 or with some larger N slices that this generated volume node</p>
</blockquote>
</aside>
<p>You can crop and resample to get consistent sizes.</p>
<p>For extracting patches, cropping, resampling, etc. you may find <a href="https://torchio.readthedocs.io/">torchio</a> useful.</p>

---
