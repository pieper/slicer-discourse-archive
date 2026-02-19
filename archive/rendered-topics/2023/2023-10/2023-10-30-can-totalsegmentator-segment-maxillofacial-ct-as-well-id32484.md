---
topic_id: 32484
title: "Can Totalsegmentator Segment Maxillofacial Ct As Well"
date: 2023-10-30
url: https://discourse.slicer.org/t/32484
---

# Can TotalSegmentator segment maxillofacial CT as well?

**Topic ID**: 32484
**Date**: 2023-10-30
**URL**: https://discourse.slicer.org/t/can-totalsegmentator-segment-maxillofacial-ct-as-well/32484

---

## Post #1 by @Tijl (2023-10-30 12:17 UTC)

<p>Is it segmenting maxillofacial ct as well?</p>
<p>Met vriendelijke groeten,</p>
<p>T.H. van den Berg, Parodontoloog NVvP, Implantoloog NVOI</p>
<p>Zijlweg 144<br>
2015 BH Haarlem</p>
<p>+31 23 542 01 88</p>

---

## Post #2 by @rbumm (2023-10-30 14:13 UTC)

<p>Please contact the developers on the <a href="https://github.com/wasserth/TotalSegmentator" rel="noopener nofollow ugc">TotalSegmentator Github</a>. You may add an issue with sample data there.</p>

---

## Post #3 by @lassoan (2023-10-30 15:43 UTC)

<p>If you have segmented sample data then contacting TotalSegmentator developers would make sense. They may be able to train a network based on your data and make it openly available.</p>
<p>If you are looking for openly available automated segmentation tools for CMF images then you might find these Slicer extensions useful:</p>
<ul>
<li><a href="https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools/tree/main#readme">AutomatedDentalTools</a></li>
<li><a href="https://github.com/DCBIA-OrthoLab/SlicerDentalModelSeg/blob/main/readme.md">DentalModelSeg</a></li>
<li><a href="https://cmf.slicer.org/">SlicerCMF</a></li>
</ul>

---

## Post #4 by @diazandr3s (2023-11-02 12:06 UTC)

<p>Hi <a class="mention" href="/u/tijl">@Tijl</a>,</p>
<p>Great question. Have you considered using <a href="https://github.com/Project-MONAI/MONAILabel" rel="noopener nofollow ugc">MONAI Label</a> for this?</p>
<p>Here is a project we’ve created with MONAI Label that may be of interest: <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MultistageTeethSegmentation/" class="inline-onebox" rel="noopener nofollow ugc">NA-MIC Project Weeks | Website for NA-MIC Project Weeks</a></p>
<p><a class="mention" href="/u/dgmato">@dgmato</a> can also comment on this</p>

---

## Post #5 by @lassoan (2023-11-02 12:42 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> need to figure out a way to run MONAILabel (at least inference) by a single click in Slicer. Many users would never even consider running commands in a terminal or install docker. For all these people MONAILabel is inaccessible now. The same way as nnunet can be installed in Slicer’s Python environment, we could install MONAI and its dependencies in the Slicer module; then select a model and download it and start a server - all using the GUI, by a few clicks. What do you think? Do you know about any plans in this direction?</p>

---

## Post #6 by @rbumm (2023-11-02 13:01 UTC)

<p>It is not quite what you are aiming for <a class="mention" href="/u/lassoan">@lassoan</a> but we have successfully used  MONAI bundle to integrate models from MONAI model ZOO during the last PW in Montreal.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/MONAIBundleIntegrationTutorial/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/MONAIBundleIntegrationTutorial/" target="_blank" rel="noopener nofollow ugc">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/MONAIBundleIntegrationTutorial/" target="_blank" rel="noopener nofollow ugc">Project Description</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @diazandr3s (2023-11-02 14:13 UTC)

<p>This is a good idea, <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>Having MONAI Label and the <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models" rel="noopener nofollow ugc">Bundle models</a> available for inference only should be possible.</p>
<p>We could use a modified version of the Slicer’s MONAI Label module to run the inference commands in the background.</p>
<p>As <a class="mention" href="/u/rbumm">@rbumm</a> suggested, Bundles and the MONAI Label models can be easily run with a single command.</p>
<p>For the full experience (inference, training and active learning), users can be directed to the instructions for starting the MONAI Label server.</p>
<p>What do you think, <a class="mention" href="/u/lassoan">@lassoan</a>? We could start with the models for single modality</p>

---

## Post #8 by @lassoan (2023-11-02 14:22 UTC)

<p>It all sounds good.</p>
<p>Could you provide a complete list of steps that users need to do manually now for a specific model? I would check what would it take to perform those steps automatically, in Slicer’s Python environment.</p>

---

## Post #9 by @diazandr3s (2023-11-03 00:51 UTC)

<p>Sure!  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>The steps are the following:</p>
<blockquote>
<ol>
<li>Create a Python env and install MONAI Label<br>
<em>pip install monailabel</em></li>
<li>Download the apps: radiology and/or monaibundle<br>
<em>monailabel apps --download --name monaibundle --output ./</em></li>
<li>Within the app folder, execute the main Python file specifying the model and folder where the image(s) are located<br>
Example command for the radiology app:<br>
<em>python main.py -s /tmp/MONAILabelTest/sampleTest/ --model segmentation --test infer</em></li>
<li>show the predictions saved in <strong>test_labels</strong> folder</li>
</ol>
</blockquote>
<p>Here I created two videos showing how this can be done. I assumed the env with MONAI Label is already created.</p>
<p><em>For the radiology app:</em><br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0eeb21f6f96b0f87edb6e339460e6ca0be9908b.mp4">
  </div><p></p>
<p><em>For the monaibundle app:</em></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7de9fb9eaf33e48d030f42d289b3d306356fe09.mp4">
  </div><p></p>
<p>In addition to the typical MONAI Label models (deepedit, segmentation, vertebra), users can also run the following models from the Model Zoo:</p>
<pre><code class="lang-auto">spleen_ct_segmentation 
pancreas_ct_dints_segmentation 
spleen_deepedit_annotation 
swin_unetr_btcv_segmentation 
renalStructures_UNEST_segmentation 
wholeBrainSeg_Large_UNEST_segmentation 
prostate_mri_anatomy 
lung_nodule_ct_detection 
wholeBody_ct_segmentation
</code></pre>
<p>Please let me know your thoughts. Happy to explain more about any of the steps presented here in the videos.</p>

---
