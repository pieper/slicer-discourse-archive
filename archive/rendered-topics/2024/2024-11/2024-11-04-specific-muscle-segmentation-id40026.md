---
topic_id: 40026
title: "Specific Muscle Segmentation"
date: 2024-11-04
url: https://discourse.slicer.org/t/40026
---

# Specific Muscle Segmentation

**Topic ID**: 40026
**Date**: 2024-11-04
**URL**: https://discourse.slicer.org/t/specific-muscle-segmentation/40026

---

## Post #1 by @kwonheokju (2024-11-04 22:50 UTC)

<p>Hi, I’m a graduate student and I’m splitting my thoracic muscles right now.<br>
For now, we are using thresholds provided by Slicer to divide the muscles, and then we are removing the skin muscles and internal organs.<br>
For detectors, we are removing them using Scissor.<br>
However, one patient has about 520 sheets of dcm, and it takes three to four days to process them all.<br>
I also tried Growseeds or Between Slide, but it was difficult to use as it was segmented to the areas I didn’t want.<br>
I hope you can let me know so that I can process it faster.<br>
Thank you in advance.</p>

---

## Post #2 by @pieper (2024-11-05 14:57 UTC)

<p>We have an nnU-Net based model that segments torso muscles automatically from CT but we haven’t yet published it so it’s not available yet.  It should be out in a few months if you can wait that long.</p>
<p><strong><img src="https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdFb4qm07FgSNVJH0lqNls0yOTF0kZG-4U4gyQT5Wa9-3k9UfA0_Y0xxG3MXy7m9QfuXY5J2p8ppW5jshZEyAiQB2MrJKB-yAF3MSq983vKY8bikIPnHTdGAAcH_OUXEdnHixbHToGmkDEehO3nAJvdhkrBWxzN=s2048?key=-HU6BxKgwmxMg2JL7uFu0Q" alt="|202px;x116px;" width="690" height="457"><img src="https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfPzAWuGlwdrA1F12aIzdGAYKSRAh01303pp0k_Fzfr5dERZFZWG_rhymq3KLqCOb27r_KZB3EpnIsoPmcaxgZDZRVcoxxEXrIaLcfPyatBMHKA_D3I6r7Hac06PCOwkz7X-Qa5LcNX74Aw4HR4itLmU_Kl0Hc=s2048?key=-HU6BxKgwmxMg2JL7uFu0Q" alt="|182px;x116px;" width="679" height="500"></strong></p>
<p><strong><img src="https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdFb4qm07FgSNVJH0lqNls0yOTF0kZG-4U4gyQT5Wa9-3k9UfA0_Y0xxG3MXy7m9QfuXY5J2p8ppW5jshZEyAiQB2MrJKB-yAF3MSq983vKY8bikIPnHTdGAAcH_OUXEdnHixbHToGmkDEehO3nAJvdhkrBWxzN=s2048?key=-HU6BxKgwmxMg2JL7uFu0Q" alt="|202px;x116px;" width="690" height="457"></strong></p>
<p><strong><img src="https://lh7-rt.googleusercontent.com/slidesz/AGV_vUe6W6A94z4BiE-7bPua5TT3f67ZOeoc8dZOUgZwzT4726Sn8fjkmIb1KjHZhM6ZpcytxVmmC0M7GuJABfMN62SBJfMo5Pdjdlqmt70Z_d8oKmGPVtGc3M_c_tXtBowcY1Z4sOogXDPNm7Bw68e9gGOWkbxyk8fv=s2048?key=-HU6BxKgwmxMg2JL7uFu0Q" alt="|229px;x116px;" width="690" height="404"></strong></p>
<p><strong><img src="https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfXRRqYe8hBNbG7RjnR6TnydLboeERqwf61uF8Xl0SZVR3kT9lBx9FGbVqyyUQ2p9AEsM9ws8Ew-4YPRAnIEJUkOt_GUu0BgECKOKPI1I4HMyC5KImXgmOOgdm9LLDa3ab6BB331aTv58qlp2Jv7LXf_gov5EK4=s2048?key=-HU6BxKgwmxMg2JL7uFu0Q" alt="|177px;x116px;" width="662" height="500"></strong></p>
<p><strong><img src="https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdJnQmYRTjJmW3LmKc4v1SXuXO2JmM2_7WWhWxy5MgjAr3fKhmn3kSUKqiKcpPtmtIa13W0cb08aiK_4wOVU8wziMx8gWqroQzNlHxWiFu80WdN7138ImtH-7FjpPBq8UhBRP61q8e_U5FaB2rjrpgYigSAGsE=s2048?key=-HU6BxKgwmxMg2JL7uFu0Q" alt="|265px;x213px;" width="622" height="500"></strong></p>
<p><strong><img src="https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeuHe_4iguR1aDflqfZmCqgIbWcqFCZRoRkrQZknfcYQ17r8OUIzy6wlbajeDgBQ0yqHFBjhccMVoTUaNpU45YQTdDMWDSOMcsIv1IHgJtPuvTMSQrLXTFHikjvOD_sVLXJuhPla2ssPuucVfAulixYt1Hg4sKh=s2048?key=-HU6BxKgwmxMg2JL7uFu0Q" alt="|201px;x194px;" width="517" height="500"></strong></p>

---

## Post #3 by @kwonheokju (2024-11-05 15:05 UTC)

<p>Hi Steve Piper, Thank you for your reply, and I hope the nnUnet you are making works out well.<br>
May I ask exactly how long it takes? We need your model within a month.<br>
And if you don’t mind, I would like to ask you to share the code after publishing.<br>
Thank you.</p>
<p>2024년 11월 5일 (화) 오후 11:57, Steve Pieper (Isomics Inc.) via 3D Slicer Community &lt;<a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a>&gt;님이 작성:</p>

---

## Post #4 by @CS1 (2025-08-19 12:55 UTC)

<p>Hi Pieper, this tool looks amazing and I’m hoping too see if your team has managed to publish it yet? Thank you!</p>

---

## Post #5 by @pieper (2025-08-19 13:00 UTC)

<p>Thanks <a class="mention" href="/u/cs1">@CS1</a></p>
<p>Yes, there’s a description here: <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11838942/" class="inline-onebox">Automated Segmentation of Trunk Musculature with a Deep CNN Trained from Sparse Annotations in Radiation Therapy Patients with Metastatic Spine Disease - PMC</a></p>
<p>A version of the model is also now available in TotalSegmentator: <a href="https://github.com/wasserth/TotalSegmentator#:~:text=sinus_maxillary%2C%20sinus_frontal%2C%20teeth_upper-,abdominal_muscles,-%3A%20pectoralis_major_right%2C%20pectoralis_major_left%2C%20rectus_abdominis_right" class="inline-onebox">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of &gt;100 important anatomical structures in CT and MR images</a></p>

---

## Post #6 by @CS1 (2025-08-19 13:58 UTC)

<p>Hi Pieper</p>
<p>Thanks so much for this! Silly questions from me, I can’t seem to be able to find <strong>abdominal_muscles</strong> subtask within the module and when I set my segmentation task as “total”, under fast mode with low resolution, it doesn’t quite give me the segmentation outcome as nicely displayed as the pictures you showed. How could I achieve what you achieved in those photos? Do I have to run totalsegmentator on python? Do I have to run it at full resolution? is <strong>abdominal_muscles</strong> a segmentation subtask (so we could shorten the time by not segmenting unwanted structures) or does it only come with total segmentation? Thank you!!</p>

---

## Post #7 by @pieper (2025-08-19 19:49 UTC)

<p>Hi <a class="mention" href="/u/cs1">@CS1</a> - It’s a good question, the abdominal muscle integration in TotalSegmentator is fairly new and I know Jakab said he retrained the model based on what we gave him so I guess maybe there are still some issues compared to the original.  It’s unfortunate because we were hoping that by centralizing the features we wouldn’t need to support multiple modules and implementations, with all the headaches of cuda drivers and whatnot.</p>
<p>I could dig up the code for the original model, which used a 2d model iteratively on the slices to make the images posted above as described in the paper.  I recall it did depend on a specific version of nnunet (exactly the sort of support issues I was trying to avoid by putting the model into TotalSegmentator).  If I put it all on github I guess you could maybe get that to work.</p>
<p>These deep learning tools are great when they work but all the tooling is still a bit hard to make available cleanly.</p>

---
