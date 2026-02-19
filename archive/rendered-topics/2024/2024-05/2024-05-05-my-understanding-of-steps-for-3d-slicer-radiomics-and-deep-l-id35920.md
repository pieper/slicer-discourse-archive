---
topic_id: 35920
title: "My Understanding Of Steps For 3D Slicer Radiomics And Deep L"
date: 2024-05-05
url: https://discourse.slicer.org/t/35920
---

# My understanding of steps for 3D Slicer Radiomics and Deep learning

**Topic ID**: 35920
**Date**: 2024-05-05
**URL**: https://discourse.slicer.org/t/my-understanding-of-steps-for-3d-slicer-radiomics-and-deep-learning/35920

---

## Post #1 by @sapos93 (2024-05-05 00:31 UTC)

<p>Dear Users,<br>
I am a newbie in the realm of coding. I’m a physician-researcher who wants to do a project of developing a deep learning radiomics signature for a specific spinal anatomical variant. My understanding for the steps I need to do is the following:</p>
<ol>
<li>Obtain DICOMs of 200 cervical spine CT (computed tomography) scans with 400 sides (150 have the anatomical variant; 250 do not have it) - done  <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></li>
<li>Perform segmentation in 3D Slicer for each side of each patient (400 sides) - done <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></li>
<li>Extract radiomics features using 3D slicer module/extension ‘SlicerRadiomics’ (also called “Radiomics”). 107 features for each patient with features. The output is a table in .tsv file for each patient. Meaning there are 400 such tables. - done <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></li>
</ol>
<hr>
<p>What should I do now? Is it as follows:?<br>
4. Combine all those 400 tables into a single excel .csv file so that each side of each patient has its own row and columns are the extracted features. <img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji" alt=":question:" loading="lazy" width="20" height="20"><br>
5. Import to ‘RStudio’ and perform Z score normalization of all the features so that they have a standard scale or range <img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji" alt=":question:" loading="lazy" width="20" height="20"><br>
6. Divide data into a training and a test cohort using an 80/20 split<br>
7.  Perform radiomics feature selection using a LASSO regression model or Boruta package <img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji" alt=":question:" loading="lazy" width="20" height="20"><br>
8. Do unsupervised hierarchical clustering of normalized radiomics features using the package ComplexHeatmap in R <img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji" alt=":question:" loading="lazy" width="20" height="20"><br>
9. Do binary logistic regression analysis in R using the presence of the anatomical variant as the dependent variable and radiomics features as independent variables. <img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji" alt=":question:" loading="lazy" width="20" height="20"><br>
10. Draw receiver operating characteristic (ROC) curves and calculate areas under the ROC curve (AUC) including 95% confidence intervals. <img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji" alt=":question:" loading="lazy" width="20" height="20"></p>
<p>Are the steps correct? Are they in the correct order? Or should something be changed? I am not sure about the step <span class="hashtag-raw">#4</span> (combining the tables) and order of steps <span class="hashtag-raw">#5</span> to <span class="hashtag-raw">#8</span></p>
<p>Please, kindly use language that a layman without much coding experience will understand.<br>
Thank you<br>
kind regards,<br>
Tomasz</p>

---

## Post #2 by @pieper (2024-05-05 12:21 UTC)

<p>Maybe others here will have specific suggestions, but I don’t think there’s a well defined formula. The steps you outline look reasonable.  There are hundreds of papers about radiomic analysis so you could review them, or, maybe more efficiently you could ask one of the AI chatbots to summarize them for you.  There are several tools out there now that could help extract this kind of information from the academic literature.  Let us know how it goes.</p>

---
