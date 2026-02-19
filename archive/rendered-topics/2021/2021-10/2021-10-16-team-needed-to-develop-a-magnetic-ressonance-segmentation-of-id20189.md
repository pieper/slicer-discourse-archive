---
topic_id: 20189
title: "Team Needed To Develop A Magnetic Ressonance Segmentation Of"
date: 2021-10-16
url: https://discourse.slicer.org/t/20189
---

# Team needed to develop a Magnetic Ressonance segmentation of the spinal column

**Topic ID**: 20189
**Date**: 2021-10-16
**URL**: https://discourse.slicer.org/t/team-needed-to-develop-a-magnetic-ressonance-segmentation-of-the-spinal-column/20189

---

## Post #1 by @Ricardoneuro (2021-10-16 23:43 UTC)

<p>I have been using a very efficient column volumetric magnetic resonance protocol for the past 5 years. I’m looking for a group of people interested in a segmentation protocol that can extract and segment bone tissue from a volumetric MRI file. I can see a very important use for this technology, specifically in the infant population, in order to generate volumetric reconstructions of the spine without exposure to ionizing radiation.</p>

---

## Post #2 by @robertsoakes (2021-10-17 17:24 UTC)

<p>Hi Ricardo, this sounds like a fascinating project. MRI is a wonderful modality that is underutilized for procedure planning (at least in my opinion). Can you elaborate on the technical aims of what you are trying to accomplish?</p>
<p>It sounds like you’ve already accumulated a pretty good dataset, do you also have masks or models for some of them? Would a reference set need to be generated and validated as a starting point?</p>
<p>What degree of automation is needed? Is the goal to have a model that can create accurate masks without supervision or would operators be able to refine the masks before they are used downstream?</p>
<p>Is the goal purely research, or do you have specific applications (procedure planning, surgical navigation, 3D printing) which should be taken into account as part of the protocol design?</p>

---

## Post #3 by @S_Arbabi (2021-10-17 19:14 UTC)

<p>Dear <a class="mention" href="/u/ricardoneuro">@Ricardoneuro</a>,</p>
<p>Great idea. I know of a company doing this task as a commercial software. That might be interesting for your question.<br>
My PhD supervisor (Dr. Peter Seevinck) started working on the idea of generating synthetic CT images from MR images 5 years ago and the deep learning-based softwate product recently has extended CE marks for spine as well.<br>
Here’s one study evaluating usage of this sCT spine for surgical planning:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://thejns.org/focus/view/journals/neurosurg-focus/50/1/article-pE13.xml">
  <header class="source">
      <img src="https://thejns.org/focus/fileasset/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://thejns.org/focus/view/journals/neurosurg-focus/50/1/article-pE13.xml" target="_blank" rel="noopener nofollow ugc" title="12:00AM - 01 January 2021">focus – 1 Jan 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:373/500;"><img src="https://thejns.org/focus/cover/journals/neurosurg-focus/50/1/cover.jpg" class="thumbnail" width="373" height="500"></div>

<h3><a href="https://thejns.org/focus/view/journals/neurosurg-focus/50/1/article-pE13.xml" target="_blank" rel="noopener nofollow ugc">Magnetic resonance imaging–based synthetic computed tomography of the lumbar...</a></h3>

  <p>OBJECTIVE Computed tomography scanning of the lumbar spine incurs a radiation dose ranging from 3.5 mSv to 19.5 mSv as well as relevant costs and is commonly necessary for spinal neuronavigation. Mitigation of the need for treatment-planning CT scans...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The company is MRIGuidance:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://mriguidance.com/bonemri-now-available-for-lower-back/">
  <header class="source">
      <img src="https://mriguidance.com/wp-content/uploads/2017/01/mriguidance_favicon.png" class="site-icon" width="64" height="64">

      <a href="https://mriguidance.com/bonemri-now-available-for-lower-back/" target="_blank" rel="noopener nofollow ugc" title="11:37AM - 03 September 2021">MRIguidance – 3 Sep 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/387;"><img src="https://mriguidance.com/wp-content/uploads/2021/09/BoneMRI_of_the_lower_back.jpg" class="thumbnail" width="690" height="387"></div>

<h3><a href="https://mriguidance.com/bonemri-now-available-for-lower-back/" target="_blank" rel="noopener nofollow ugc">BoneMRI now available for lower back - MRIguidance</a></h3>

  <p>For the first time the involvement of both the vertebra and the soft tissue of the spine, in patients with chronic back pain, can be examined from a single medical imaging exam. MRIguidance has extended its CE certificate of BoneMRI for usage in the...</p>

  <p>
    <span class="label1">Est. reading time: 9 minutes</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Best,<br>
Saeed</p>

---

## Post #4 by @diazandr3s (2021-10-17 20:48 UTC)

<p>This is an interesting task. Have you considered utilising MONAI Label with the DeepEdit App (<a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/deepedit" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/sample-apps/deepedit at main · Project-MONAI/MONAILabel · GitHub</a>)?</p>

---

## Post #5 by @Lucas_Formighieri (2021-10-31 20:13 UTC)

<p>Hi. I´ve been doing segmentation and 3D printing of medical exams for some time. I would surely like to help in anyway I can.<br>
Best regards,<br>
Lucas</p>

---
