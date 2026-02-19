---
topic_id: 518
title: "Quantitative Features With Heterogeneitycad"
date: 2017-06-16
url: https://discourse.slicer.org/t/518
---

# Quantitative features with HeterogeneityCad

**Topic ID**: 518
**Date**: 2017-06-16
**URL**: https://discourse.slicer.org/t/quantitative-features-with-heterogeneitycad/518

---

## Post #1 by @mtamponi (2017-06-16 10:47 UTC)

<p>Operat Window 7 :<br>
Slicer 7.0 nightly build 10 march 2017:</p>
<ol>
<li>If we calculate the entropy in the homogeneus region of a “volume-label” for a lesion with only one gray level, we wait for “entropy” a value equal to 0…</li>
<li>Using a CT-scan volume,  for  the “Autocorrelation” calculated in a tumor lesion we wait a value less than 1.</li>
<li>For other features, calculated on CT scan volumes using “volume-label” to descibe the lesion (we did for 9 patients with T1-T2 lung cancer lesions), we wait normal values<br>
Instead for a lesion with a volume of 2634.724 mm^3 (about 3 cc) we obtained:</li>
<li>the “entropy” value greater than 8000 in “volume-label”  with only one gray level;</li>
<li>the “Autocorrelation” equal to 322607190 in CT-Scan volume ofe lesion;</li>
<li>the  “Correlation”  equal to 55006886.<br>
Some features, as for example, the “median intesity” they seem OK; some other feature do not seem Ok, as for example the “Autocorrelation”. We are looking for the mathematical description of the features implemented in “HetereogeneityCAD” of 3DSlicer, as for example that one given by by Parmar et al. (Robust Radiomics Feature Quantification Using Semiautomatic Volumetric Segmentation, Plos one, 2014, V 9, I. 7) in the supplement of their paper.</li>
</ol>

---

## Post #2 by @pieper (2017-06-16 13:06 UTC)

<p>Thanks for reporting this - you may also be interested in trying the SlicerRadiomics extension, which is a fresh implementation of some of these feature calculations.  We’d be curious to hear how these work on your data.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/Radiomics/SlicerRadiomics" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/13385545?s=400&amp;v=4" class="thumbnail onebox-avatar" width="400" height="400">

<h3><a href="https://github.com/Radiomics/SlicerRadiomics" target="_blank">Radiomics/SlicerRadiomics</a></h3>

<p>A Slicer extension to provide a GUI around pyradiomics - Radiomics/SlicerRadiomics</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mtamponi (2017-06-17 06:19 UTC)

<p>Thank You very much,<br>
we are try to install Radiomics in 3DSlicer and We hope to give You good feedback. Also, if it will be possible, for us it is also useful to have news about HeterogeneityCad,<br>
Sincerely,<br>
Matteo Tamponi</p>

---

## Post #4 by @mtamponi (2017-06-17 08:32 UTC)

<p>To Kind Attention of 3DSlicer Staff<br>
I tried to install Radiomics extension  after installation of Slicer 4.7.0 nightly build on 17-june-2017 following the instruction in the github site in the <a href="http://read.me" rel="nofollow noopener">read.me</a> file. I tried following the user way, not downloading from the source. It looked all ok, but after Slicer restart, Radiomics is not in the Slicer Applications list. The installation of other applications was OK (As Registrations and SLICER RT ones). Before to install the 3d Slicer 4.7.0 Nightbuild for windows 64 bit (Windows 7 in my PC), I have removed the 4.6.2 stable version an the previously 4.7.0 version of 3dSlicer from my PC.<br>
What can I do, without to install 3dslicer from the source file?<br>
Sincerely,<br>
Matteo Tamponi</p>

---

## Post #5 by @lassoan (2017-06-17 14:14 UTC)

<p>SlicerRadiomics extension is available for recent nightly builds on Windows and Mac. If you are in European time zone then you may wait until early afternoon for all extensions to become available (or <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">download an earlier nightly build</a> - for example: <a href="http://download.slicer.org/?offset=-1">download yesterday’s build</a>)</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a>  FYI, there is a <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1045149">packaging error of SlicerRadiomics on Linux</a>.</p>

---

## Post #6 by @fedorov (2017-06-18 02:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a>  FYI, there is a packaging error of SlicerRadiomics on Linux.</p>
</blockquote>
</aside>
<p>Yes, that is a known issue <a href="https://github.com/Radiomics/SlicerRadiomics/issues/16" class="inline-onebox">Slicer Linux dashboard issues · Issue #16 · AIM-Harvard/SlicerRadiomics · GitHub</a></p>

---

## Post #7 by @mtamponi (2017-06-19 08:23 UTC)

<p>To kind attention fo 3DSlicer Staff,<br>
Thank You very much for You help, in particulary to Andrey Fedorov, Andras Lasso and  Steve Pieper,<br>
This morning I installed again 3Dslicer 4.7.0. v 17 june 2017 and then, from estension utility, I installed “radiomics” and other extensions as those for segmentation (14 extensions) and those for registration and those for radiation therapy and many others. However, while the other extensions run, “radiomics” does not result in the list of modules and also looking for it, I cannot find it.<br>
I’d like to be able to use “radiomics”, while I hope to have some more informations about HerogeneityCad too.<br>
I’m using Windows 7 64 bit and 16 GB radiological workstation.<br>
Thank for Your Attention<br>
Sincerely,<br>
Matteo Tamponi</p>

---

## Post #8 by @pieper (2017-06-19 12:28 UTC)

<p>Hi Matteo -</p>
<p>Sorry, yes, that’s another ‘known issue’ that I’d thought was resolved.  I just posted instructions there to workaround around the issue and that should make things work for you.  Once I did this the Radiomics module was available on my recent windows nightly and works as expected.</p>
<p><a href="https://github.com/Radiomics/SlicerRadiomics/issues/23" class="onebox" target="_blank">https://github.com/Radiomics/SlicerRadiomics/issues/23</a></p>
<p>-Steve</p>

---

## Post #9 by @mtamponi (2017-06-21 09:37 UTC)

<p>To Kind Attention of Steve Pieper,</p>
<p>Steve,<br>
I tried to follow this instruction:<br>
"“C:/Users/username/AppData/Roaming/NA-MIC/Extensions-revision/SlicerRadiomics/lib/site-packages/radiomics/featureextractor.py<br>
Where revision is something like 26083 depending on the nightly version of Slicer.<br>
Line 9 should be changed from:<br>
import pykwalify.core”"</p>
<p>but I cannot find the directory "C:/Users/username/AppData/Roaming/NA-MIC/Extensions-revision/SlicerRadiomics/lib/site-packages/radiomics/"and the file “<a href="http://featureextractor.py" rel="nofollow noopener">featureextractor.py</a>” in my computer<br>
(“Users” is “Utenti” and “Username” is “Fisica” in my computer)</p>
<p>so I cannot have “radiomics” in my 3d-Slicer 4.7.0 extension on Window 7. What can I do?</p>
<p>Also for the features calculated with HeterogeneityCad, can I ask to Somebody?</p>
<p>Thank for Your Attention,<br>
Sincerely,<br>
Matteo</p>

---

## Post #10 by @pieper (2017-06-21 19:42 UTC)

<p>Hi Matteo -</p>
<p>The AppData folder may be hidden using regular browsing techniques on windows.  You can get to it with a cmd prompt (kind of low level, but not uncommon).</p>
<p><a class="mention" href="/u/jayender">@jayender</a> is probably the best contact for HeterogeneityCAD.</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #11 by @jayender (2017-06-21 19:43 UTC)

<p>Hi Matteo</p>
<p>Regarding the HeterogeneityCAD module, please follow the instructions on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/HeterogeneityCAD" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/HeterogeneityCAD</a></p>
<p>The references for the metric computation are included on the webpage. Please let me know if you have any questions.</p>
<p>Thanks<br>
Jay</p>

---

## Post #12 by @mtamponi (2017-06-22 06:37 UTC)

<p>Dear Steve,<br>
I followed Your indication, from “cmd” level. Now “Radiomics” run.<br>
Also I received a mail from Jayender. I hope to do some comparisons of some features with “Radiomics”  and “HeterogeneityCad” in 2dSlicer.,<br>
Thank You very much,<br>
Sincerely,<br>
Matteo</p>

---

## Post #13 by @pieper (2017-06-22 11:41 UTC)

<p>Great!  Let us know how it goes.</p>

---

## Post #14 by @mtamponi (2017-06-22 15:25 UTC)

<p>Yes, Steve,<br>
I’ll take time, but I’ll informe You about our experience with “radiomics”,<br>
Thank You,<br>
Matteo</p>

---

## Post #15 by @mtamponi (2017-06-22 16:00 UTC)

<p>To Kind Attention of Jay,<br>
Jay<br>
Yes, we followed the instructions in the site "<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/HeterogeneityCAD" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/HeterogeneityCAD</a>"<br>
and we were able to calculate all features in HeterogeneityCAD with 3D-Slicer 4.7.0 for about 10 patients with small lung cancer lesions.<br>
We observed that for small lung cancer lesions, HeteregeneityCad, in our PC (16 GB ram) is quite fast also for  Geometrical Measures and Renyi Dimensions that need more calculation time. The time grows up very rapidly, increasly the lesion  dimension for these kind of features (expecailly for Renyi Dimensions).<br>
We are trying to understand the meaning of the features. Some features for us seem more easy and the results of our calculation seem nice.<br>
But the mathematical definition for some features for us are not clear; In particular, we don’t understand some results, as for example those obtained for the “Entropy” and the Texture<br>
features: “Autocorrelation” and for “Correlation”.<br>
For example for the “Autocorrelation” we obtained 322607190 and for  the “Correlation”  55006886 for a volume lesion of 2635 mm3.<br>
Also,  for example if we calculate Entropy (first order features) in a homogeneus ROI, only on gray level, we obtained a value greater than 8000 instead of 0.<br>
To try to understand, we downloaded the supplement material of the paper of Coroller et al. on Radiotherapy and Oncology 114 (2015) 345–350, where there are some mathematical definitions of many features, as the Entropy for example.<br>
There is some mathematical definition of the features in HetereoneityCad  more detailed and if possible with Unit of Measure, possible minimum and maximum?<br>
Thak You very much for Your help and indicantions,<br>
Sincerely,<br>
Matteo</p>

---

## Post #16 by @lassoan (2017-06-22 16:03 UTC)

<aside class="quote no-group" data-username="mtamponi" data-post="15" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mtamponi/48/332_2.png" class="avatar"> mtamponi:</div>
<blockquote>
<p>To Kind Attention of Jay</p>
</blockquote>
</aside>
<p>Please use mention (<span class="mention">@someusername</span>) to bring something to someone’s attention. It is shorter and the mentioned person actually gets a personal notification.</p>

---

## Post #17 by @pieper (2017-06-22 17:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To Kind Attention of Jay</p>
<p>Please use mention (<span class="mention">@someusername</span>) to bring something to someone’s attention. It is shorter and the mentioned person actually gets a personal notification.</p>
</blockquote>
</aside>
<p>In this case <a class="mention" href="/u/jayender">@jayender</a></p>

---

## Post #18 by @fedorov (2017-06-22 19:08 UTC)

<p><a class="mention" href="/u/mtamponi">@mtamponi</a> you might want to look at this evolving document that summarizes community consensus about radiomics feature definitions: <a href="https://arxiv.org/abs/1612.07003">https://arxiv.org/abs/1612.07003</a></p>
<p>Speaking of pyradiomics <a href="http://pyradiomics.readthedocs.io/en/latest/">http://pyradiomics.readthedocs.io/en/latest/</a>, most of the features implemented there are implemented consistently with the formulas described in the paper I mentioned above. If you have specific questions about pyradiomics implementation, you can raise them on the pyradiomics forum (see documentation).</p>

---

## Post #19 by @mtamponi (2017-06-23 06:37 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>,<br>
Thank Andrey ,<br>
I look and download the arxiv evolving document and check the site of  pyradiomics that You indicated, They are very useful for our work. Thank You very much to You and also to Steve, Andras an Jay,<br>
Matteo</p>

---

## Post #20 by @mtamponi (2017-06-23 15:19 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a><br>
Andrey<br>
Attached to this mail You can find 3 screen shots with 3dSlicer, 2 using Radiomics and 1 using HeterogeneityCad for  the same lesion in . You can see that for: Entropy, Kurtosis and Uniformity, the calculates values are very different. For Energy, median intensity, Skewness, voxel count, variance are exactly equal.<br>
I could be some problems in the calculation of entropy, Kurtosis and Uniformity, probably in HeterogeneityCAD, but I don’t know.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/6f1c07e0770946da05a56c75b6f80b0456a9dbdc.jpg" data-download-href="/uploads/short-url/fQV3oTSu7Vt671J9scavyagBmAQ.jpg?dl=1" title="H-0028-smc-1stf.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6f1c07e0770946da05a56c75b6f80b0456a9dbdc_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6f1c07e0770946da05a56c75b6f80b0456a9dbdc_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6f1c07e0770946da05a56c75b6f80b0456a9dbdc_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6f1c07e0770946da05a56c75b6f80b0456a9dbdc_2_1380x636.jpg 2x" data-dominant-color="6D7788"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">H-0028-smc-1stf.jpg</span><span class="informations">4438×2048 637 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/72b2a510d5703d39cf88cdfd1bfc0d6e93dff6cb.jpg" data-download-href="/uploads/short-url/gmFaVN4p8mzQrd9kdNQOpul1sYb.jpg?dl=1" title="R-0028-smc-1stf-2a.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/72b2a510d5703d39cf88cdfd1bfc0d6e93dff6cb_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/72b2a510d5703d39cf88cdfd1bfc0d6e93dff6cb_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/72b2a510d5703d39cf88cdfd1bfc0d6e93dff6cb_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/72b2a510d5703d39cf88cdfd1bfc0d6e93dff6cb_2_1380x636.jpg 2x" data-dominant-color="556076"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">R-0028-smc-1stf-2a.jpg</span><span class="informations">4438×2048 439 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/cd71e88cba10f9ddb8d7a9d75933dfea2eee3f24.jpg" data-download-href="/uploads/short-url/tjrVBitVmErlK253uX20XDtZz3m.jpg?dl=1" title="R-0028-smc-1stf-1a.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cd71e88cba10f9ddb8d7a9d75933dfea2eee3f24_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cd71e88cba10f9ddb8d7a9d75933dfea2eee3f24_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cd71e88cba10f9ddb8d7a9d75933dfea2eee3f24_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/cd71e88cba10f9ddb8d7a9d75933dfea2eee3f24_2_1380x636.jpg 2x" data-dominant-color="556076"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">R-0028-smc-1stf-1a.jpg</span><span class="informations">4438×2048 465 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>Matteo</p>

---

## Post #21 by @fedorov (2017-06-23 15:54 UTC)

<aside class="quote no-group" data-username="mtamponi" data-post="20" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mtamponi/48/332_2.png" class="avatar"> mtamponi:</div>
<blockquote>
<p>I could be some problems in the calculation of entropy, Kurtosis and Uniformity, probably in HeterogeneityCAD, but I don’t know.</p>
</blockquote>
</aside>
<p>Definitely it could be. If you look at the implementations of both HeterogeneityCAD and pyradiomics, and find that one is incorrect, it will be interesting to know. You might find the public radiomics digital phantom helpful in your explorations: <a href="http://www.radiomics.org/?q=node/28">http://www.radiomics.org/?q=node/28</a>. I would be very interested to learn about the outcome! Joost, the lead developer of pyradiomics, I believe compared pyradiomics against that phantom (unfortunately, I don’t see him on this forum, so I will ask him by email to join and comment). I don’t know if it was ever eveluated with HeterogeneityCAD. <span class="mention">@Jayender_Jagadeesan</span> will be the best to comment on that!</p>

---

## Post #22 by @Jayender_Jagadeesan (2017-06-23 18:36 UTC)

<p>The definition of the metrics can be found in the Supplemental information of Hugo’s paper:</p>
<p>HJWL Aerts, ER Velazquez, RTH Leijenaar, et al., “Decoding tumour phenotype by noninvasive imaging using a quantitative radiomics approach”, vol. 5, Nat Communication, 2014.</p>
<p>Also please note, there are number of parameters that are set, for example the number of discrete intensity levels, discretization bin width, normalization constants etc., to compute the heterogeneity metrics.</p>
<p>Jay</p>

---

## Post #23 by @JoostJM (2017-06-23 19:35 UTC)

<p>Hi Matteo,</p>
<p>As <a class="mention" href="/u/fedorov">@fedorov</a> mentioned, I compared the output of PyRadiomics to a digitial phantom, but I’m not entirely sure this is the same as Andriy mentioned. It is the digital phantom used in the article with the feature definitions Andriy sent (The IBSI document).</p>
<p>That being said, I think the differences you’re experiencing may be in part explained by <a class="mention" href="/u/jayender">@jayender</a>’s comment, namely the discretization. For PyRadiomics, this is determined by a fixed bin width (as opposed to a fixed bin count) with a default value of 25 units. I’m not sure about how this is implemented in HeterogeneityCAD or what default settings are. More information on the exact method implemented in PyRadiomics can be found <a href="http://pyradiomics.readthedocs.io/en/latest/radiomics.html#radiomics.imageoperations.binImage" rel="nofollow noopener">here</a>.<br>
However, this only affects Entropy and Uniformity.</p>
<p>The exact cause of the difference in Kurtosis I do not know, but it strikes me that the difference is <em>exactly</em> 3. <a class="mention" href="/u/jayender">@jayender</a>, does the HeterogeneityCAD system implement a fixed offset? This would be a fixed value of 3, which centers kurtosis on 0 for normal distributions (PyRadiomics does not have this offset, which would explain the difference). In fact, this offset is also implemented in the IBSI document.</p>
<p>Cheers,</p>
<p>Joost</p>

---

## Post #24 by @mtamponi (2017-06-26 12:54 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>,<br>
Thank You Andrey,<br>
I downloaded the phantoms. I hope to work about and then say to You,<br>
Matteo</p>

---

## Post #25 by @mtamponi (2017-06-26 12:57 UTC)

<p><a class="mention" href="/u/jayender">@jayender</a>,<br>
Thank You Jay, I downloaded the supplement of the paper of H. Aerts et al. and I must work about slowly,<br>
Sincerely,<br>
Matteo</p>

---

## Post #26 by @mtamponi (2017-06-26 12:59 UTC)

<p><a class="mention" href="/u/joostjm">@JoostJM</a> ,<br>
Thank to You Joost, I must study slowly on the site that You indidicated,<br>
Sincerely,<br>
Matteo</p>

---

## Post #27 by @mtamponi (2017-06-27 10:59 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>,<br>
Dear Andrey I do some calculation on the phantom that You say me (PAT2) using 3DSlicer Radiomics and Heterogeneity CAD.<br>
Significative differences You can see on Entropy, Hunformity and Kurtosis on first order features.<br>
On shape features there are difference on surface area, sphericity, compactness 1 and 2 and other differences. The Volume is ok. On GLCM there many and apparently important differences, for example  autocorrelation, correlation, contrast, entropy,…<br>
Matteo<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/1496f3b772edbe58e12322ac4f32d655a43abfe4.jpg" data-download-href="/uploads/short-url/2W8XGijR6QOAsZWSPeZ2zj9ei4A.jpg?dl=1" title="pat2-glcm-to-Cluster Tendency.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1496f3b772edbe58e12322ac4f32d655a43abfe4_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1496f3b772edbe58e12322ac4f32d655a43abfe4_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1496f3b772edbe58e12322ac4f32d655a43abfe4_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1496f3b772edbe58e12322ac4f32d655a43abfe4_2_1380x636.jpg 2x" data-dominant-color="5E6063"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pat2-glcm-to-Cluster Tendency.jpg</span><span class="informations">4438×2048 738 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/aaa24cdfe965d308ccf758ff1c59ad4ceff96c5b.jpg" data-download-href="/uploads/short-url/oluTB61tl1UXAU9W2XdQLKr1hTt.jpg?dl=1" title="pat2-HCmedian-Kurtosis Uniformity-Skewness.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/aaa24cdfe965d308ccf758ff1c59ad4ceff96c5b_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/aaa24cdfe965d308ccf758ff1c59ad4ceff96c5b_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/aaa24cdfe965d308ccf758ff1c59ad4ceff96c5b_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/aaa24cdfe965d308ccf758ff1c59ad4ceff96c5b_2_1380x636.jpg 2x" data-dominant-color="505763"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pat2-HCmedian-Kurtosis Uniformity-Skewness.jpg</span><span class="informations">4438×2048 648 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/30e4b415f7bbbdcc814acd1e32b045c2f01be285.jpg" data-download-href="/uploads/short-url/6YwUDr6hebDd8SFkCmCuWIEkOEJ.jpg?dl=1" title="pat2-fo-to TotalEnergy.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30e4b415f7bbbdcc814acd1e32b045c2f01be285_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30e4b415f7bbbdcc814acd1e32b045c2f01be285_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30e4b415f7bbbdcc814acd1e32b045c2f01be285_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30e4b415f7bbbdcc814acd1e32b045c2f01be285_2_1380x636.jpg 2x" data-dominant-color="364259"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pat2-fo-to TotalEnergy.jpg</span><span class="informations">4438×2048 444 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/f8af42b76275347cb8857f00fe39677ea5e57709.jpg" data-download-href="/uploads/short-url/ztXUdJndJgE72oMUcragjiVgt8l.jpg?dl=1" title="pat2-HCmedia-entropy-energy.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f8af42b76275347cb8857f00fe39677ea5e57709_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f8af42b76275347cb8857f00fe39677ea5e57709_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f8af42b76275347cb8857f00fe39677ea5e57709_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/f8af42b76275347cb8857f00fe39677ea5e57709_2_1380x636.jpg 2x" data-dominant-color="4C5460"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pat2-HCmedia-entropy-energy.jpg</span><span class="informations">4438×2048 617 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/5ffdc438f7f4ef5d768c149ccf92ab9f0142beac.jpg" data-download-href="/uploads/short-url/dHb3dv1m7BayeBFMKeYmsVtyWxC.jpg?dl=1" title="pat2-HCshape.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5ffdc438f7f4ef5d768c149ccf92ab9f0142beac_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5ffdc438f7f4ef5d768c149ccf92ab9f0142beac_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5ffdc438f7f4ef5d768c149ccf92ab9f0142beac_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5ffdc438f7f4ef5d768c149ccf92ab9f0142beac_2_1380x636.jpg 2x" data-dominant-color="515863"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pat2-HCshape.jpg</span><span class="informations">4438×2048 685 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/10dfacbd527c39f9ba99aa2e7f355c12cc21081d.jpg" data-download-href="/uploads/short-url/2pgRlKTAmfwp2q0wXvn1zYtsd9b.jpg?dl=1" title="pat2-sh-to-maxim2DDiameterRow.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/10dfacbd527c39f9ba99aa2e7f355c12cc21081d_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/10dfacbd527c39f9ba99aa2e7f355c12cc21081d_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/10dfacbd527c39f9ba99aa2e7f355c12cc21081d_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/10dfacbd527c39f9ba99aa2e7f355c12cc21081d_2_1380x636.jpg 2x" data-dominant-color="5E6063"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pat2-sh-to-maxim2DDiameterRow.jpg</span><span class="informations">4438×2048 746 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e48461c02fb10b9845436fc59c33571e204ace86.jpg" data-download-href="/uploads/short-url/wByunJbhURTPO7PNksGP0tqEb0q.jpg?dl=1" title="pat2-glcm-to-InverseVariance.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e48461c02fb10b9845436fc59c33571e204ace86_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e48461c02fb10b9845436fc59c33571e204ace86_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e48461c02fb10b9845436fc59c33571e204ace86_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e48461c02fb10b9845436fc59c33571e204ace86_2_1380x636.jpg 2x" data-dominant-color="5E6063"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pat2-glcm-to-InverseVariance.jpg</span><span class="informations">4438×2048 727 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e1b66abed0c24d4fa3d06afc16cf22c08a444ac9.jpg" data-download-href="/uploads/short-url/wcKfXvlpBGL4awQp5fXq7MjurKV.jpg?dl=1" title="pat2-HCglcm-to-homogeneity2.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e1b66abed0c24d4fa3d06afc16cf22c08a444ac9_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e1b66abed0c24d4fa3d06afc16cf22c08a444ac9_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e1b66abed0c24d4fa3d06afc16cf22c08a444ac9_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e1b66abed0c24d4fa3d06afc16cf22c08a444ac9_2_1380x636.jpg 2x" data-dominant-color="515863"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pat2-HCglcm-to-homogeneity2.jpg</span><span class="informations">4438×2048 689 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/3b47d917460201bebc35df3e48b9e38d698202c7.jpg" data-download-href="/uploads/short-url/8sq6tm2ZtSt0AmKDuF0imTFY4GX.jpg?dl=1" title="pat2-fo-to mean.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3b47d917460201bebc35df3e48b9e38d698202c7_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3b47d917460201bebc35df3e48b9e38d698202c7_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3b47d917460201bebc35df3e48b9e38d698202c7_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/3b47d917460201bebc35df3e48b9e38d698202c7_2_1380x636.jpg 2x" data-dominant-color="5A5D60"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pat2-fo-to mean.jpg</span><span class="informations">4438×2048 686 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/5f5840a110676f0342aafb26a66509704bcc9cc0.jpg" data-download-href="/uploads/short-url/dBsrgftqDVYjjG6dl9OJTnviuY0.jpg?dl=1" title="pat2-HCglcm-to-Variance glcm.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5f5840a110676f0342aafb26a66509704bcc9cc0_2_690x318.jpg" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5f5840a110676f0342aafb26a66509704bcc9cc0_2_690x318.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5f5840a110676f0342aafb26a66509704bcc9cc0_2_1035x477.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5f5840a110676f0342aafb26a66509704bcc9cc0_2_1380x636.jpg 2x" data-dominant-color="515863"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pat2-HCglcm-to-Variance glcm.jpg</span><span class="informations">4438×2048 653 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #28 by @ShivR (2017-07-07 19:16 UTC)

<p>I’m a little confused about the installation of 3d slicer. I’ve followed the installation instructions on “read me”, downloading slicer, installing Radiomics, and restarting slicer. However, I’m unsure how to proceed from there. Where is <a href="http://featureextractor.py" rel="nofollow noopener">featureextractor.py</a> coming from? I see it in the python file from <a href="http://radiomics.io" rel="nofollow noopener">radiomics.io</a>, but does that mean I need to download everything from both pyradiomics and 3d slice for 3d slicer to work? Also, is there any way I can speak to a representative and work everything out?</p>
<p>Thanks in advance.</p>

---

## Post #29 by @pieper (2017-07-07 19:42 UTC)

<aside class="quote no-group" data-username="ShivR" data-post="28" data-topic="518" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c2a13f/48.png" class="avatar"> ShivR:</div>
<blockquote>
<p>I’m a little confused about the installation of 3d slicer. I’ve followed the installation instructions on “read me”, downloading slicer, installing Radiomics, and restarting slicer. However, I’m unsure how to proceed from there. Where is featureextractor.py coming from? I see it in the python file from <a href="http://radiomics.io">radiomics.io</a>, but does that mean I need to download everything from both pyradiomics and 3d slice for 3d slicer to work? Also, is there any way I can speak to a representative and work everything out?</p>
<p>Thanks in advance.</p>
</blockquote>
</aside>
<p>Did you find these instructions?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/d9d6a3e987eef15295d2f5c3aa4dcbc0ba740c37d9866cecf7b8e92b541ab0aa/AIM-Harvard/SlicerRadiomics" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/AIM-Harvard/SlicerRadiomics" target="_blank" rel="noopener">GitHub - AIM-Harvard/SlicerRadiomics: A Slicer extension to provide a GUI...</a></h3>

  <p>A Slicer extension to provide a GUI around pyradiomics - GitHub - AIM-Harvard/SlicerRadiomics: A Slicer extension to provide a GUI around pyradiomics</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Once you’ve done this install you need to load data and you can run the radiomics calculations within Slicer using the GUI (featureextractor.py is code used when developing your own script, but not directly exposed when using the SlicerRadiomics GUI).</p>

---

## Post #30 by @fedorov (2017-07-07 20:02 UTC)

<aside class="quote no-group" data-username="ShivR" data-post="28" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c2a13f/48.png" class="avatar"> ShivR:</div>
<blockquote>
<p>However, I’m unsure how to proceed from there.</p>
</blockquote>
</aside>
<p>If you want to get help on this forum, it probably makes sense to describe what you want to achieve.</p>
<aside class="quote no-group" data-username="ShivR" data-post="28" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c2a13f/48.png" class="avatar"> ShivR:</div>
<blockquote>
<p>is there any way I can speak to a representative and work everything out?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/shivr">@ShivR</a> 3D Slicer is an open source project, not a commercial platform with a dedicated support desk. Having said that, there are companies that provide paid support and consulting related to 3D Slicer - see for example Kitware consulting offers <a href="https://www.kitware.com/what-we-offer/#consulting">https://www.kitware.com/what-we-offer/#consulting</a>.</p>

---

## Post #31 by @ShivR (2017-07-07 21:05 UTC)

<p>Thank you for such quick responses Andrey and Steve!</p>
<p>My overall goal is to use Slicer to isolate ROIs on DICOM images and then extract first and second order features from them. However, my current issue is simply that I don’t get how to install the technology. I used the instructions Steve attached. I have the same question Matteo did about not being able to find the "C:/Users/username/AppData/Roaming/NA-MIC/Extensions-revision/SlicerRadiomics/lib/site-packages/radiomics/"and the file “<a href="http://featureextractor.py" rel="nofollow noopener">featureextractor.py</a>” files on my computer, but I don’t know what a cmd prompt is or what cmd is either. How can I find this file so that Slicer Radiomics will work? Also, .py is python, so do I also need to download python to change line 9?</p>

---

## Post #32 by @pieper (2017-07-07 21:25 UTC)

<aside class="quote no-group" data-username="ShivR" data-post="31" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c2a13f/48.png" class="avatar"> ShivR:</div>
<blockquote>
<p>I have the same question Matteo did about not being able to find the "C:/Users/username/AppData/Roaming/NA-MIC/Extensions-revision/SlicerRadiomics/lib/site-packages/radiomics/"and the file “featureextractor.py” files on my computer, but I don’t know what a cmd prompt is or what cmd is either.</p>
</blockquote>
</aside>
<p>Ah, sorry, I see what you were asking now.  The cmd prompt is also known as the command prompt or dos prompt in windows, but I found you can also get into the AppData folder by typing in the Address Bar of the windows explorer as shown here:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5aca4fc972adaba1884079f3300a881686d0b959.png" alt="image" data-base62-sha1="cXaqem09FTW1YC53JfGU81SymjT" width="640" height="215"></p>
<p>From there you can browse into the path to find the featureextractor.py file and make the edit described earlier in this thread.  Hope that works for you.</p>
<p><a class="mention" href="/u/joostjm">@JoostJM</a> maybe we should just comment out the yaml / pykwalify stuff until <a class="mention" href="/u/jcfr">@jcfr</a> is back.</p>

---

## Post #33 by @mtamponi (2017-07-08 06:23 UTC)

<p>With the help of Steve, Andrey and Andras and reading the documentations and papers from Joost and Jayender, We are improving in evaluating radiomics features in lung cancer using 3dSlicer.<br>
We calculated radiomics features with Radiomics and HeterogeneityCad for more about 10 patients with lung cancer.<br>
We use also phantom from prof Lambin.<br>
We think that there are some important software bugs in the calculation of some features in HeterogeneityCad in 3DSlicer 4.7.0 (begin of june) (Entropy, Autocorrelation, Corelation,… You can see my last mail). It could be useful to check it and put more warnings about using heterogeneityCad.<br>
At the moment the features calculated with Radiomics seem nice, but it is necessary do more extensive elaboration.<br>
Thanking very much for the help<br>
Sincely</p>
<p>cc<br>
<a class="mention" href="/u/shivr">@ShivR</a><br>
<a class="mention" href="/u/fedorov">@Fedorov</a><br>
<a class="mention" href="/u/joostjm">@JoostJM</a><br>
<a class="mention" href="/u/jayender">@jayender</a><br>
<a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #34 by @JoostJM (2017-07-10 07:59 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, I could comment out the import of pykwalify, however, this will break the parameter file parsing, which is not needed in the slicer extension, but is important in the stand alone version of PyRadiomics.</p>
<p>I have created a specific SlicerRadiomics branch in PyRadiomics, and updated the Cmake-lists in SlicerRadiomics to use this specific branch.</p>
<p>However, before this is available in the extension manager, it has to be rebuild and repackaged.(In fact, the version of SlicerRadiomics that is installed is 9e57f350709207df925cd0ce397dffbcb6f262b5 (commit from may 30th).</p>

---

## Post #35 by @JoostJM (2017-07-10 08:09 UTC)

<p>As to the significant differences in first order features, see the explanation above.<br>
As to the changes in volume, this is mainly due to the different manner of calculating a surface area. I don’t know what heterogeneityCAD uses, but pyradiomics implements a marching cubes algorithm, creating a surface mesh and summing up the surface area of the individual triangles.<br>
A different approach is to sum the surface area of the border faces of the voxels, but this overestimates surface area, especially in small volumes.<br>
The differences in many of the other features are also due to this difference, as the formulas are dependent on the surface area value.<br>
A possible exception to this is Compactness1; sometimes the exponent of A is flipped (i.e. 2/3 instead of 3/2). Pyradiomics has the 3/2 exponent, as this makes the formula dimensionless.</p>
<p>Differences in GLCM (and most likely the other texture matrices as well) are most likely due to a different method of gray level discretization (similar to the differences in Uniformity and Entropy).</p>

---

## Post #36 by @JoostJM (2017-07-10 08:15 UTC)

<p><a class="mention" href="/u/mtamponi">@mtamponi</a>, In addition, it is possible that there is a small bug in GLCM. This has been fixed in PyRadiomics, but the SlicerExtension uses a specific version of PyRadiomics, where this bugfix has not yet been applied.</p>

---

## Post #37 by @ShivR (2017-07-10 12:55 UTC)

<p>Thank you Steve, it works!</p>

---

## Post #38 by @ShivR (2017-07-11 03:11 UTC)

<p>Hi</p>
<p>I’m sorry to post such a basic question here again, but I’m seeing this window in front of me and it seems like the radiomics extension is working - I’ve checked off first and second order features. Could someone please explain how to select something like a node from the whole image and then get the features of that cropped area or point me towards a tutorial for the extension. I can’t seem to find one online. Thanks in advance!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/5d1f22b5ea5b4d758afc75ef41cce1335e3c6961.jpg" data-download-href="/uploads/short-url/dhN6Ye5HeRliJTvCp1bsnSLMwCZ.jpg?dl=1" title="3D slicer images.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5d1f22b5ea5b4d758afc75ef41cce1335e3c6961_2_690x377.jpg" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5d1f22b5ea5b4d758afc75ef41cce1335e3c6961_2_690x377.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5d1f22b5ea5b4d758afc75ef41cce1335e3c6961_2_1035x565.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5d1f22b5ea5b4d758afc75ef41cce1335e3c6961_2_1380x754.jpg 2x" data-dominant-color="6A6971"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D slicer images.jpg</span><span class="informations">1901×1040 310 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #39 by @fedorov (2017-07-11 15:42 UTC)

<p><a class="mention" href="/u/shivr">@ShivR</a> we recommend you use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentEditor">Segment Editor</a> module to segment the structure(s) of your interest, and then select that segmentation in the “Input Segmentation” selector of the module. Can you try this and let us know if this answers your question?</p>

---

## Post #40 by @ShivR (2017-07-13 18:04 UTC)

<p>Yes, it works! I have one more question, <a class="mention" href="/u/fedorov">@fedorov</a>. I was watching your video “Segmentation of Lung and Nodule in CT using 3D Slicer”, and I was wanted to confirm that in order to get the 1st and 2nd order features of a node from radiomics, I don’t have to get a 3-d representation of the node like you did in the video right? It is enough to simply paint over the node (2d) in Segment Editor and use that segment to extract the features from in Radiomics module?</p>

---

## Post #41 by @fedorov (2017-07-13 19:22 UTC)

<aside class="quote no-group" data-username="ShivR" data-post="40" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c2a13f/48.png" class="avatar"> ShivR:</div>
<blockquote>
<p>I was watching your video “Segmentation of Lung and Nodule in CT using 3D Slicer”</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/shivr">@ShivR</a> I assume you are talking about <a href="https://youtu.be/koHKAJWGNhU">this video</a>.</p>
<aside class="quote no-group" data-username="ShivR" data-post="40" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c2a13f/48.png" class="avatar"> ShivR:</div>
<blockquote>
<p>I was wanted to confirm that in order to get the 1st and 2nd order features of a node from radiomics, I don’t have to get a 3-d representation of the node</p>
</blockquote>
</aside>
<p>That is correct. The surface rendering is purely for the visualization purposes. In fact, you don’t need it for any of the radiomics features, not just 1st and 2nd order featurs.</p>
<p>You can also easily toggle visibility of a segment in 3d viewer from the Segment Editor interface, it is generated automatically.</p>

---

## Post #42 by @mtamponi (2017-07-15 07:28 UTC)

<p><a class="mention" href="/u/joostjm">@JoostJM</a><br>
cc <a class="mention" href="/u/jayender">@jayender</a>, <span class="mention">@Federeov</span> ,<a class="mention" href="/u/lassoan">@lassoan</a>,<a class="mention" href="/u/pieper">@pieper</a><br>
Thank You very much for Your observations, If it is possible I’d like to know when the small bugs will be fixed in radiomics for 3d Slicer, because I’like to re-run Radiomics in 3dSlicer on our lung cancer patients.<br>
3DSlicer is one of the Best enviroments tools for many applications in clinical research.</p>
<p>I hope to do some check too.<br>
Yes, in 3d Slicer, “Surface area” using HeterogeneityCad is only a little larger than in Radiomic, (Volume is always perfect equal) but the difference in “Autocorelation” and “Entropy” between HeterogeneityCad and Radiomics  are more important, always many orders of magnitude. I think there is other software bugs in heterogeneityCAD for 3dSlicer. I think It is necessary to make correction if these features remain in 3dSlicer. “Autocorrelation” must be less than 1 and Entropy of a perfect mono-intesity homogenus ROI must be 0. In HeterogenityCAD some features are Ok. But many other features are not ok in important way, not only for smal errors in surface calculation and canals setting. It is necessary to make a detailed check and put warning for users.<br>
Also I’d like to re-rerun heterogenityCad on our patients when these bugs on heterogenityCad will be fixed.</p>

---

## Post #43 by @mtamponi (2017-07-15 07:45 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>,<br>
Andrey<br>
Using Radiomics in 3dSlicer, I met a problem with a DICOM CT Volume. Using the same DICOM CT Volume, with HeterogeneityCAD, I was able to calulate the featuers on a label ROI Lesion. I cannot do the same with Radiomics.<br>
(I was able to do the kind of calculations with Radiomics and HeterogenityCAD for more than other 10 Patients).<br>
In this particular case, the calculation of radiomic don’t begin and compare only the name of some fields on the output-table. I have  signed the logfile in the radiomic menu, but I cannot find the log file in the directory of the computer.<br>
In which directory of 3dSlicer can I find this file?<br>
The problem is not on the lesion Label (It work in other CT volume with medium contrast), but just the dicom File. I tryed to use dicom filter, trying to limity the Hounsfield Unit or to crop the CT volume near the lesion, but it doesn’t work.<br>
So I’d like to see the logfile of radiomics to try to understand what happened.<br>
Matteo</p>

---

## Post #44 by @ShivR (2017-07-16 18:09 UTC)

<p>Thank you Andrey <a class="mention" href="/u/fedorov">@fedorov</a> for all your help. I’m just about to start taking the data for my study, but I wanted to check in before I start to make sure my data is accurate! In order to get the 1st and 2nd order features of my roi, I have to paint the roi in segment editor with the paint feature, as shown in the attached image (node on the right side of the image). Then, I can check off the radiomic features I want in the radiomics extension and apply them. Is that correct?</p>
<p>Also, I am making the assumption that the features will be incorrect if I accidentally paint outside the lines of my roi (say, my roi is the node and I accidentally paint a little into the the black space of the lungs or outside the node). Therefore, to avoid accidentally including unwanted elements inside my segment, is it ok to only paint a part of my roi. For example, if my roi is the whole node, will the features still be correct if I only paint a small circle inside the node instead of painting the whole node. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/d39cd75c9e7390855d798d74a21cb4d2575a1fd4.jpg" data-download-href="/uploads/short-url/uc0MbcCI9xVvatIhwveH85lrLQE.jpg?dl=1" title="Node.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d39cd75c9e7390855d798d74a21cb4d2575a1fd4_2_690x440.jpg" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/d39cd75c9e7390855d798d74a21cb4d2575a1fd4_2_690x440.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d39cd75c9e7390855d798d74a21cb4d2575a1fd4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d39cd75c9e7390855d798d74a21cb4d2575a1fd4.jpeg 2x" data-dominant-color="A7A5A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Node.jpg</span><span class="informations">875×559 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #45 by @fedorov (2017-07-17 01:46 UTC)

<aside class="quote no-group" data-username="mtamponi" data-post="43" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mtamponi/48/332_2.png" class="avatar"> mtamponi:</div>
<blockquote>
<p>I cannot find the log file in the directory of the computer.</p>
<p>In which directory of 3dSlicer can I find this file?</p>
</blockquote>
</aside>
<p>Radiomics module logging is added to the Slicer log. You can find the log in the “Help &gt; Report a bug” menu.</p>

---

## Post #46 by @fedorov (2017-07-17 01:53 UTC)

<aside class="quote no-group" data-username="ShivR" data-post="44" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c2a13f/48.png" class="avatar"> ShivR:</div>
<blockquote>
<p>In order to get the 1st and 2nd order features of my roi, I have to paint the roi in segment editor with the paint feature, as shown in the attached image (node on the right side of the image). Then, I can check off the radiomic features I want in the radiomics extension and apply them. Is that correct?</p>
</blockquote>
</aside>
<p>Yes</p>
<aside class="quote no-group" data-username="ShivR" data-post="44" data-topic="518">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c2a13f/48.png" class="avatar"> ShivR:</div>
<blockquote>
<p>I am making the assumption that the features will be incorrect if I accidentally paint outside the lines of my roi (say, my roi is the node and I accidentally paint a little into the the black space of the lungs or outside the node). Therefore, to avoid accidentally including unwanted elements inside my segment, is it ok to only paint a part of my roi. For example, if my roi is the whole node, will the features still be correct if I only paint a small circle inside the node instead of painting the whole node.</p>
</blockquote>
</aside>
<p>“Correctness” can only be applied to how error-free implementation of the feature calculation is. Correctness of the feature calculation is not affected by the ROI you pass. If the implementation is correct, it will calculate the numbers for any ROI.</p>
<p>A different question is how ROI definition affects your features. Even though they may be correct, you may be getting feature values that are drastically different depending on your ROI definition. You should conduct some experiments to evaluate consistency of the feature calculation as a function of your ROI to understand this better. You may also find this article helpful: <a href="http://www.spl.harvard.edu/publications/item/view/2504">http://www.spl.harvard.edu/publications/item/view/2504</a>. Yet another issue is whether these features will be able to answer the clinical question you are investigating. Implementation may be correct, and the features may be very stable with varying ROI, but they may not be helpful at all in predicting patient survival, for example. You should experiment and read existing publications on the subject.</p>

---

## Post #47 by @ShivR (2017-07-17 14:52 UTC)

<p>Thank you so much for your help!</p>

---

## Post #48 by @michaela_cellina (2017-11-09 19:40 UTC)

<p>Hi everyone!!!<br>
Talking about Radiomics in 3D slicer… has anyone use it for MR images analysis?<br>
How can I get the normalization of the signal intensity normalization?<br>
I don’t found specific instructions about it.<br>
Help me please!!!</p>
<p>Miky</p>

---

## Post #49 by @JoostJM (2018-01-17 13:25 UTC)

<p>PyRadiomics is a python package for extraction radiomics features, which also has a slicer extension (SlicerRadiomics). Check out the PyRadiomics documentation <a href="http://pyradiomics.readthedocs.io" rel="nofollow noopener">here</a><br>
or post a question on <a href="https://groups.google.com/forum/#!forum/pyradiomics" rel="nofollow noopener">google groups forum</a>.</p>

---

## Post #50 by @apaw (2019-11-11 09:59 UTC)

<p>Hello, everyone,</p>
<p>this discussion deals with a problem that we also stumbled upon during an evaluation: HeterogeneityCAD and pyradiomics provide different results. We are only interested in firstorder statistics, in particular entropy and uniformity.</p>
<p>Probably the setting are a (partial) explanation for this, as stated in the post of <a class="mention" href="/u/jayender">@jayender</a> (discrete intensity levels, discretization bin width, normalization constants).</p>
<p>What we would like to try now is to configure pyradiomics like HeterogeneityCAD (mainly the bin width). Only: We don’t find the parameters. A search in the source code didn’t lead - at least for us - to the goal… Maybe you can help us <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/joostjm">@JoostJM</a></p>
<p><a class="mention" href="/u/mtamponi">@mtamponi</a> What is your opinion? Can we use the results from HeterogenityCAD? Should we at least omit entropy?</p>
<p>Thank you very much in advance!</p>

---

## Post #51 by @JoostJM (2019-11-12 09:42 UTC)

<p>Hi <a class="mention" href="/u/apaw">@apaw</a>,</p>
<p>In SlicerRadiomics, there are currently 2 ways of configuring the extraction; Manually and through a parameter file. Manual configuration offers a limited set of the possible settings, but all configuration possible in PyRadiomics is also exposed in SlicerRadiomics when you use the parameter file.</p>
<p>An exhaustive list of all possible settings is available in the PyRadiomics documentation, found <a href="https://pyradiomics.readthedocs.io/en/latest/customization.html#settings" rel="nofollow noopener">here</a>, and examples of parameter files can be found on the github of PyRadiomics <a href="https://github.com/Radiomics/pyradiomics/tree/master/examples/exampleSettings" rel="nofollow noopener">here</a>.</p>
<p>As to differences between HeterogeneityCAD and PyRadiomics, these are partly explained in <a href="https://discourse.slicer.org/t/quantitative-features-with-heterogeneitycad/518/23">this</a> and <a href="https://discourse.slicer.org/t/quantitative-features-with-heterogeneitycad/518/35">this</a> comment, though additional changes in PyRadiomics changed the output of shape features, and SlicerRadiomics now uses the latest version of PyRadiomics (the bug in GLCM mentioned earlier has now also been fixed for the PyRadiomics used in Slicer).</p>
<p>I’m currently not really up to date on discretization settings in HeterogeneityCAD, but if it’s using a fixed bin count, you can use this by specifying it in the parameter file (not available in Manual customization). Still, we do not advise using a fixed bin count, as then the ‘meaning’ of the discretized gray values becomes dependent on the range found in the ROI, which differs between cases. For a more detailed answer, see <a href="https://pyradiomics.readthedocs.io/en/latest/faq.html#what-about-gray-value-discretization-fixed-bin-width-fixed-bin-count" rel="nofollow noopener">here</a>.</p>

---

## Post #52 by @JoostJM (2019-11-12 10:11 UTC)

<p>I took a quick look at the source code of HeterogeneityCAD and as far as I can see now is that it uses a fixed bin width of 1.</p>
<p>However, there also appears to be an issue with calculation of entropy and uniformity.<br>
This relies on bins calculated <a href="https://github.com/vnarayan13/Slicer-OpenCAD/blob/master/HeterogeneityCAD/HeterogeneityCAD.py#L542" rel="nofollow noopener">here</a>, which represent the <em>frequencies</em>, not the <em>probability</em> of gray values. These get passed to firstorder calculation <a href="https://github.com/vnarayan13/Slicer-OpenCAD/blob/master/HeterogeneityCAD/HeterogeneityCAD.py#L475" rel="nofollow noopener">here</a>, and are used, unaltered, for <a href="https://github.com/vnarayan13/Slicer-OpenCAD/blob/master/HeterogeneityCAD/FeatureExtractionLib/FirstOrderStatistics.py#L44" rel="nofollow noopener">Entropy</a> and <a href="https://github.com/vnarayan13/Slicer-OpenCAD/blob/master/HeterogeneityCAD/FeatureExtractionLib/FirstOrderStatistics.py#L120" rel="nofollow noopener">Uniformity</a> calculation. However, these formulas assume <em>probabilities</em>, not <em>frequencies</em> and therefore don’t result in the expected values.</p>
<p>In PyRadiomics, this is prevented by dividing the frequencies in each bin by the sum of frequencies <a href="https://github.com/Radiomics/pyradiomics/blob/master/radiomics/firstorder.py#L91" rel="nofollow noopener">here</a>, resulting in <code>p_i</code> representing the probability of gray values, rather than the frequency of gray values.</p>
<p>Of course, it’s possible I’m misreading something here, so I’ll differ to <a class="mention" href="/u/jayender">@jayender</a> for the final verdict.</p>

---

## Post #53 by @apaw (2019-11-25 14:26 UTC)

<p>Dear <a class="mention" href="/u/joostjm">@JoostJM</a>,</p>
<p>many thanks for the fast and profound feedback.</p>
<p>On the one hand it frustrates us because the results with HeterogeneityCAD were very good, on the other hand it reassures us because we now have certainty that there was actually something wrong with the calculation of the parameters.</p>

---
