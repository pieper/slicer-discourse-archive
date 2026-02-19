---
topic_id: 5360
title: "Non Rigid Registration Of Brain"
date: 2019-01-14
url: https://discourse.slicer.org/t/5360
---

# Non rigid registration of brain

**Topic ID**: 5360
**Date**: 2019-01-14
**URL**: https://discourse.slicer.org/t/non-rigid-registration-of-brain/5360

---

## Post #1 by @RadioQuest (2019-01-14 15:21 UTC)

<p>Hi…<br>
I want to register post surgical brain MRI images to presurgical baseline scan. Can someone please provide me with the links to tutorial or guidance as how to achieve this in most reliable way?<br>
Thanks</p>

---

## Post #2 by @spujol (2019-01-14 19:03 UTC)

<p>Hello,</p>
<p>The Slicer registration tutorial shows the basics of rigid and non-rigid registration using BRAINS:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Slicer4_Image_Registration" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.8/Training#Slicer4_Image_Registration</a></p>
<p>The Registration Case library provides examples of registration strategies for brain tumor and TBI follow-up:<br>
<a href="https://www.na-mic.org/wiki/Projects:RegistrationDocumentation:UseCaseInventory:BrainIntraMRI" class="onebox" target="_blank" rel="nofollow noopener">https://www.na-mic.org/wiki/Projects:RegistrationDocumentation:UseCaseInventory:BrainIntraMRI</a></p>
<p>Sonia</p>

---

## Post #3 by @RadioQuest (2019-01-15 09:56 UTC)

<p>Thank you very much. I had checked basic tutorial but needed help with customization of settings.<br>
I will try it now,<br>
Kind Regards,<br>
RQ</p>

---

## Post #4 by @RadioQuest (2019-01-16 15:26 UTC)

<p>Hi. I tried to work as per <a href="https://www.na-mic.org/wiki/Projects:RegistrationLibrary:RegLib_C37" rel="nofollow noopener">https://www.na-mic.org/wiki/Projects:RegistrationLibrary:RegLib_C37</a><br>
However, I am new to the slicer. I am unable to execute registration as I need more help with setting, selection of volume etc. is there any video for the whole tutorial with details of modules and stepwise instructions.<br>
(eg which volume to use in step3 ?)<br>
Thanks</p>

---

## Post #5 by @spujol (2019-01-18 17:38 UTC)

<p>The video tutorial below shows the steps for case <span class="hashtag">#37:</span></p>
<p><a href="https://spujol.github.io/3DSlicerTutorial-Registration/" class="onebox" target="_blank" rel="nofollow noopener">https://spujol.github.io/3DSlicerTutorial-Registration/</a></p>
<p>Sonia</p>

---

## Post #6 by @RadioQuest (2019-01-21 11:26 UTC)

<p>Dear Sonia<br>
Thank you very much. This is very useful.<br>
Kind Regards,<br>
RQ</p>

---

## Post #7 by @RadioQuest (2019-01-22 16:51 UTC)

<p>Dear Sonia,<br>
I have performed registration as per this tutorial.<br>
Could you please tell me what are the criteria to determine if my registration is accurate despite brain deformation?<br>
is there any publication to support this methodology? I need to validate my results.<br>
Thanks.<br>
Kind Regards,<br>
RQ</p>

---

## Post #8 by @spujol (2019-01-23 13:54 UTC)

<p>A simple approach is to use a dense set of anatomical landmarks.<br>
The General Registration module is based on the BRAINS library:<br>
<em>BRAINSFit: Mutual Information Registrations of Whole-Brain 3D Images, Using the Insight Toolkit, Johnson H.J., Harris G., Williams K., The Insight Journal, 2007.(<a href="http://hdl.handle.net/1926/1291" rel="noopener nofollow ugc">http://hdl.handle.net/1926/1291</a>)</em></p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/BRAINSia/BRAINSTools/tree/main/BRAINSFit">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/BRAINSia/BRAINSTools/tree/main/BRAINSFit" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/BRAINSia/BRAINSTools/tree/main/BRAINSFit" target="_blank" rel="noopener nofollow ugc">BRAINSTools/BRAINSFit at main · BRAINSia/BRAINSTools</a></h3>

  <p><a href="https://github.com/BRAINSia/BRAINSTools/tree/main/BRAINSFit" target="_blank" rel="noopener nofollow ugc">main/BRAINSFit</a></p>

  <p><span class="label1">A suite of tools for medical image processing focused on brain analysis</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
