---
topic_id: 30684
title: "Unable To Import Brainlab Seg To Slicer"
date: 2023-07-19
url: https://discourse.slicer.org/t/30684
---

# Unable to import Brainlab SEG to Slicer

**Topic ID**: 30684
**Date**: 2023-07-19
**URL**: https://discourse.slicer.org/t/unable-to-import-brainlab-seg-to-slicer/30684

---

## Post #1 by @Michele_Bailo (2023-07-19 16:34 UTC)

<p>Hi everyone,<br>
I regularly export Slicer segmentations into the Brainlab Elements and Neuronavigation system (using the QuantitativeReporting feature). However, I’ve been experiencing many difficulties in importing segmentations generated from the Brainlab Elements into 3D Slicer (I only succeeded a few times, expecially for manually segmented volume, but never for automatically segmented anatomical structures); usually 3D Slicer come out with this error: “Could not load: Objects as a DICOMSegmentation”<br>
This feature would be extremely helpful for me since Brainlab Anatomical Mapping is extremely fast and reliable (at least most of the times) in automatically segmenting multiple cerebral structures; however, I always prefer to analyze the preoperative planning and postoperative results in the 3D Slicer environment since it offers many additional features and possibilities (for both clinical and research settings)<br>
I previously checked other thread in this community, but I was not able to find a solution.</p>
<p>I generated an anonymous dataset in the case someone is able to check the SEG files and understand why they are not read by Slicer. It is possible to download it from this link:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/uarbr72zu60gbrr/EFASQF-Anonymous.zip?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/s/uarbr72zu60gbrr/EFASQF-Anonymous.zip?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-file-zip-landscape.png" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://www.dropbox.com/s/uarbr72zu60gbrr/EFASQF-Anonymous.zip?dl=0" target="_blank" rel="noopener nofollow ugc">EFASQF-Anonymous.zip</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thank you very much in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a02959e1dc28720b4d8843671974fb4a9ffeaad.png" data-download-href="/uploads/short-url/1qyjkKAUEzkYT91xzXJDjnLtGUd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a02959e1dc28720b4d8843671974fb4a9ffeaad_2_690x374.png" alt="image" data-base62-sha1="1qyjkKAUEzkYT91xzXJDjnLtGUd" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a02959e1dc28720b4d8843671974fb4a9ffeaad_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a02959e1dc28720b4d8843671974fb4a9ffeaad_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a02959e1dc28720b4d8843671974fb4a9ffeaad_2_1380x748.png 2x" data-dominant-color="FAFAFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×2086 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-07-21 04:55 UTC)

<p>It’s great that you find useful for analyzing your surgeries using Slicer.</p>
<p>Importing of the DICOM Segmentation object fails due to this error (shown in application log in Slicer):</p>
<pre><code class="lang-auto">ERROR: No sufficient information to derive slice spacing! Unable to interpret the data.
Fatal error encountered.
</code></pre>
<p>This is a known error in BrainLab’s software. See solution for fixing the DICOM data set here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="23737">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/unable-to-load-dicom-segmentation-missing-slice-thickness/23737">Unable to load DICOM segmentation - missing slice thickness</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’m unable to load a DICOM segmentation. 
The segmentation was created by the Brainlab Curve navigation system in the AMIGO suite. 
I unfortunately cannot share the file. 
Tested on the latest preview version (version 5.1.0, revision 30987, built 2022-06-02) and the stable release. 
I was tempted to ignore this and just assume that the file was faulty, but: 

this was the case for more than one file
I could open the segmentation with other software (<a href="https://www.imfusion.com/resources/download" rel="noopener nofollow ugc">ImFusion Suite Demo Version</a> to be specific)

T…
  </blockquote>
</aside>

<p><a class="mention" href="/u/fedorov">@fedorov</a> do you know if they have fixed this in later BrainLab software versions?</p>

---

## Post #3 by @fedorov (2023-07-21 14:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="30684">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a> do you know if they have fixed this in later BrainLab software versions?</p>
</blockquote>
</aside>
<p>Unfortunately, I do not, and I do not have any current contact at BrainLab.</p>
<p><a class="mention" href="/u/michele_bailo">@Michele_Bailo</a> I assume you are a paying customer of BrainLab - did you try reaching out to them to ask to fix this issue? I am happy to join the conversation to help explain the technical details. I could also try reaching out to the contacts I used to have - they may not be at BrainLab anymore, but should know folks. Also - <a class="mention" href="/u/koeglfryderyk">@koeglfryderyk</a> (the author of the post above and an alum of SPL!) is now at BrainLab - we can try reaching out to him. But best would be if the contact is initiated by you <a class="mention" href="/u/michele_bailo">@Michele_Bailo</a>, since you are a customer, and I am a random person from the street as far as BrainLab is concerned.</p>

---

## Post #4 by @Michele_Bailo (2023-07-25 08:03 UTC)

<p>Yes, the center I work in (San Raffaele Scientific Institute, Milan, Italy) is a paying customer of Brainlab. Actually, I’ve never tried to ask BrainLAB because I genuinely thought it was an issue on the Slicer side, but of course, I can try asking them to intervene in this post or to get in touch with you directly.</p>
<p>The ability to import/export SEG structures (as well as RT structure) from/to software like 3D Slicer was one of the main reasons (although certainly not the only one) why we switched from Medtronic to Brainlab. As I said, it does me an excellent service the fact that I’m already able to export my Slicer segmentations directly into the Brainlab neuronavigation system (since I always prefer to create and study my preplannings in the Slicer environment, due to the immense possibilities it provides). Still, It is frustrating not being able to turn back to Slicer after the procedure (I can do workarounds like using the “Burned-In” option for large volumes and generating RT-structures in the case of smaller ones, but it is time-consuming and entail some data-loss, which is not ideal for my purposes).</p>
<p>I’ll ask Brainlab then and let you know ASAP.</p>
<p>Thank you again for your kindness and help.</p>

---

## Post #5 by @Michele_Bailo (2023-07-26 12:57 UTC)

<p>I asked Brainlab and they seem interested in addressing the issue. Technicians in Munich are already analyzing in the dataset I uploaded. I also asked them to possibly get in touch with you.<br>
In the meanwhile, as a preliminary question, they asked me if Slicer has a “dedicated Conformance Dicom Statement”, since they would like to take a look at it. Since I’m not sure what that is, could you please help me with the answer?<br>
Thank you very much again!</p>

---

## Post #6 by @fedorov (2023-07-26 13:09 UTC)

<aside class="quote no-group" data-username="Michele_Bailo" data-post="5" data-topic="30684">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michele_bailo/48/67234_2.png" class="avatar"> Michele_Bailo:</div>
<blockquote>
<p>they asked me if Slicer has a “dedicated Conformance Dicom Statement”, since they would like to take a look at it. Since I’m not sure what that is, could you please help me with the answer?</p>
</blockquote>
</aside>
<p>To the best of my knowledge, the answer is “no”.</p>

---

## Post #7 by @pieper (2023-07-27 14:56 UTC)

<p><a class="mention" href="/u/michele_bailo">@Michele_Bailo</a> - Thanks for helping push this forward.  We agree that standards based interoperability is great for everyone.  <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> to Brainlab and we look forward to working with them on this.</p>
<p>Regarding a conformance statement, it’s common for commercial systems to have these since their code and their development processes are closed.  The Slicer code is open and the forum is active so in general this is way more useful than a static conformance statement (which are unfortunately often useless in practice for many products since they are either too vague or even incorrect).  That said, if it was important for someone that such a document exists for Slicer it could be done with some effort, I’m sure contributions would be welcome.</p>

---

## Post #8 by @Michele_Bailo (2023-08-08 13:24 UTC)

<p>Hi everyone,<br>
I worked together with Brainlab and we analyzed the problem.<br>
Here is what we found out:<br>
The version we had installed in 2020 at San Raffaele Hospital (Milan) has this sort of bug that prevent segmentations automatically generated with the Brainlab Elements Anatomical Mapping to be imported in 3D Slicer.<br>
However, this problem had (somehow) already been fixed in the newer versions, since the segmentations generated in Munich with the latest software version were correctly imported in my Slicer dataset.</p>
<p>Unfortunately for me, they are not going to fix this issue in my Brainlab version. They suggested me the following workaround (which is a little bit time consuming, but it’s better than nothing):</p>
<ol>
<li>
<p>Generate the automatic segmentations with the Anatomical Mapping software in the Elements environment</p>
</li>
<li>
<p>Then enter the SmartBrush application and create a new object (i.e. “Ventricles NEW”); then select the function “Threshold” and select “Ventricles” (generated with automatic segmentation) as reference ROI.</p>
</li>
<li>
<p>Then click apply.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69c14aaaddb4d6a91f3e76d231c243762dc48767.jpeg" data-download-href="/uploads/short-url/f5yg70XGQa9QgNpRyGsBsxtGAwT.jpeg?dl=1" title="Brainlab Smartbrush" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69c14aaaddb4d6a91f3e76d231c243762dc48767_2_690x388.jpeg" alt="Brainlab Smartbrush" data-base62-sha1="f5yg70XGQa9QgNpRyGsBsxtGAwT" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69c14aaaddb4d6a91f3e76d231c243762dc48767_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69c14aaaddb4d6a91f3e76d231c243762dc48767_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69c14aaaddb4d6a91f3e76d231c243762dc48767_2_1380x776.jpeg 2x" data-dominant-color="23201A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Brainlab Smartbrush</span><span class="informations">1920×1080 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>You have now a copy of the original automatically segmented object that can be correctly imported in Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec1ce1f35debe5640cb63218c15ddae6beb39836.jpeg" data-download-href="/uploads/short-url/xGKyX4d9hDJtgWEYlEMiywjmIDk.jpeg?dl=1" title="Object imported in Slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec1ce1f35debe5640cb63218c15ddae6beb39836_2_690x362.jpeg" alt="Object imported in Slicer" data-base62-sha1="xGKyX4d9hDJtgWEYlEMiywjmIDk" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec1ce1f35debe5640cb63218c15ddae6beb39836_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec1ce1f35debe5640cb63218c15ddae6beb39836_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec1ce1f35debe5640cb63218c15ddae6beb39836_2_1380x724.jpeg 2x" data-dominant-color="8F8682"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Object imported in Slicer</span><span class="informations">1920×1009 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>I hope this could be of help to somebody else.<br>
Thank you all again for your support!</p>

---

## Post #9 by @fedorov (2023-08-08 13:30 UTC)

<p><a class="mention" href="/u/michele_bailo">@Michele_Bailo</a> thank you so much for documenting the workaround and confirming it works for you!</p>

---
