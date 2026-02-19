---
topic_id: 22505
title: "Extraction Of Features From The T1 Phase Of Mri"
date: 2022-03-14
url: https://discourse.slicer.org/t/22505
---

# Extraction of features from the T1 phase of MRI

**Topic ID**: 22505
**Date**: 2022-03-14
**URL**: https://discourse.slicer.org/t/extraction-of-features-from-the-t1-phase-of-mri/22505

---

## Post #1 by @Helo (2022-03-14 20:15 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11</p>
<p>Hi!</p>
<p>I am trying to extract features from T1 phase images from MR using the pyRadiomics extension. However, when I select the “input image volume” it does not let me extract, but when I drag the file to the programme interface and change it in the description for “sequence”, the extraction is possible. This is not the case with the other phases (T2, Portal etc). Can anyone tell me what is the reason for this?<br>
I also have a problem when I select segmentation. The file is saved as .seg, but I always have to change it to -seg in the name and drag the file into the programme, otherwise, I can not extract the features either.</p>
<p>Thanks for the attention <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @pieper (2022-03-17 18:12 UTC)

<p>It sounds like you data is being loaded as a Sequence.  Try Advanced mode and select some of the non-default load options after the examination step.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#panels-and-their-use" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#panels-and-their-use</a></p>

---

## Post #4 by @Helo (2022-03-20 19:42 UTC)

<p>Hi!</p>
<p>Thank you for your attention and quick answer, that’s it!</p>
<p>Do you know if it is a problem for me to extract features from the T1 phase in this way? Or do I always have to read as a volume?</p>
<p>Thank you again!</p>

---

## Post #5 by @pieper (2022-03-20 19:51 UTC)

<aside class="quote no-group" data-username="Helo" data-post="4" data-topic="22505">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/helo/48/14661_2.png" class="avatar"> Helo:</div>
<blockquote>
<p>extract features from the T1 phase in this way?</p>
</blockquote>
</aside>
<p>Do you mean a T1 weighted MR?</p>

---

## Post #7 by @Helo (2022-03-20 20:25 UTC)

<p>Yes, it is T1 W. To extract features from the T2, Portal phases, I could select the original image in “input image volume” but not in T1 because it was read as a sequence. I would like to know if this affects the features because the input image is a sequence and not a volume, or is this just the way the programme reads the images?</p>
<p>Thanks</p>

---

## Post #8 by @pieper (2022-03-20 22:08 UTC)

<p>Yes, you should be able to use the single T1 weighted image for feature extraction.  Be aware though that radiomics on MR <a href="https://www.nature.com/articles/s41598-019-45766-z">may not be reproducible</a>.</p>

---

## Post #10 by @Helo (2022-03-21 13:36 UTC)

<p>Thank you so much for taking the time to help me!<br>
In your article you have normalised the intensity. In my case, I did normalisation in image processing by enabling the parameter in the yaml file I created according to the examples available on pyRadiomics GitHub, is it the same? My file looked like this:</p>
<h1><a name="p-75758-imagetype-1" class="anchor" href="#p-75758-imagetype-1" aria-label="Heading link"></a>imageType:</h1>
<pre><code class="lang-auto">Original: {}
Wavelet: {}     
</code></pre>
<h1><a name="p-75758-setting-2" class="anchor" href="#p-75758-setting-2" aria-label="Heading link"></a>setting:</h1>
<pre><code class="lang-auto">normalize: true
normalizeScale: 100    
</code></pre>
<h1><a name="p-75758-resampling-3" class="anchor" href="#p-75758-resampling-3" aria-label="Heading link"></a>Resampling:</h1>
<pre><code class="lang-auto">interpolator: 'sitkBSpline' 
resampledPixelSpacing: [2, 2, 2]  *
binWidth: 5  
</code></pre>
<h1><a name="p-75758-first-order-settings-4" class="anchor" href="#p-75758-first-order-settings-4" aria-label="Heading link"></a>First Order settings:</h1>
<pre><code class="lang-auto">voxelArrayShift: 300  
</code></pre>
<h1><a name="p-75758-misc-5" class="anchor" href="#p-75758-misc-5" aria-label="Heading link"></a>Misc</h1>
<pre><code class="lang-auto">label: 1
</code></pre>
<p>Furthermore, for resampledPixelSpacing I varied it depending on the slices taken and the features presented to me, e.g. for some data I gave 2x2x2 because the values for some features were 1.0 and 0 (“flat regions”), for others I gave 3x3x3, but the IBSI says: “Maintaining consistent isotropic voxel spacing across diferent measurements and devices is therefore important for reproducibility”. So should I choose the same resampling for the whole data set?</p>
<p>Thank you very much!</p>

---

## Post #11 by @pieper (2022-03-21 14:16 UTC)

<p>I don’t know for sure myself.  Maybe another pyradiomics user or developer can add some expertise here? <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/joostjm">@JoostJM</a></p>

---

## Post #12 by @fedorov (2022-03-21 15:10 UTC)

<p>The <a href="https://www.nature.com/articles/s41598-019-45766-z">manuscript</a> mentioned by <a class="mention" href="/u/pieper">@pieper</a> earlier is accompanied by this repository that contains all the details about how the features were extracted: <a href="https://github.com/QIICR/QIN-PROSTATE-Repeatability-Radiomics" class="inline-onebox">GitHub - QIICR/QIN-PROSTATE-Repeatability-Radiomics</a>. Maybe that can be helpful to you.</p>
<p>It is my understanding that, unfortunately, there are numerous choices that you have to make while extracting radiomics features, and there are few studies prescribing how to make those choices. I personally do believe that you would want to use the same resampling settings for all of your images (especially since this is what IBSI recommends), but I don’t claim to know what are the latest results in the literature.</p>

---

## Post #13 by @Helo (2022-03-21 15:41 UTC)

<p>Thank you for responding so quickly to my questions and trying to help me!</p>

---

## Post #14 by @Helo (2022-03-21 15:42 UTC)

<p>Thank you for taking the time to reply and help me!</p>
<p>I will take a look at the repository. As for the literature, I have not found much information for the MR yet, but I will keep looking. If I do not find a conclusion, I will probably follow the IBSI recommendations.</p>
<p>Thanks again!</p>

---
