# Covariate significance testing - What is it?

**Topic ID**: 12118
**Date**: 2020-06-19
**URL**: https://discourse.slicer.org/t/covariate-significance-testing-what-is-it/12118

---

## Post #1 by @quentin_devignes (2020-06-19 16:46 UTC)

<p>Dear SlicerSALT team,</p>
<p>We are analyzing parkinsonian patients with different cognitive profiles (4 groups in total) and we are interesting in studying shape deformations of subcortical structures between these groups. We were using shapeAnalysisMANCOVA but then we discovered SlicerSALT and the Covariate Significance Testing module. Hence, our first question: why is this module more “efficient”, more “appropriate” than the older one?</p>
<p>We managed to get p-values, etc. from Covariate Significance Testing analysis. However, it is not clear what this analysis does… What are the statistical tests applied? In shapeAnalysisMANCOVA, it was quite clear and one could choose between Wilks Test, Hotelling Test, etc. and it was a permutation method.</p>
<p>Moreover, there are many different p-values (we have 4 covariates (Center, Sex, Age, Education), thus 5 different p-values (i.e. pvalue_Group Center Sex Age Education, pvalue_1, pvalue_2, etc.). What are they related to? How should we interpret these?</p>
<p>Finally, with the older shapeAnalysisMANCOVA analysis, we got deformation vectors which allowed us to know the direction of the deformation cluster (inward or outward). Is it possible to get the same vectors in your new tool?</p>
<p>Thank you for your reply,<br>
Best regards,<br>
Quentin</p>

---

## Post #2 by @styner (2020-06-19 18:02 UTC)

<p>Thanks Quentin, I will wait to hear from others in the team about the exact meaning of the different p-values.</p>
<p>The Covariance significance testing is based on the Multivariate Functional Shape Data Analysis (MFSDA) : “A multivariate varying coefficient model is introduced to build the association between the multivariate shape measurements and demographic information and other clinical variables. Statistical inference, i.e., hypothesis testing, is also included in this package, which can be used in investigating whether some covariates of interest are significantly associated with the shape information.”</p>
<p>also look at the MFSDA section here: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6494085/" rel="nofollow noopener">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6494085/</a></p>
<p>The deformation vectors in shapeAnalysisMANCOVA are simply the differences between the mean surfaces. You can can create these manually using the Population Analysis toolbox or the MeshMath tool that is distributed with SlicerSALT</p>
<p>Martin</p>

---

## Post #3 by @quentin_devignes (2020-06-24 08:15 UTC)

<p>Dear Martin,</p>
<p>Thank you for your reply. I’m not a statistician and the MFSDA seems quite complicated. Moreover, I used shapeAnalysisMANCOVA first, then I tried MFSDA and the results are really different (i.e. most of my comparisons are not significant anymore with the MFSDA). Thus, I’m a little bit confused and I don’t know which one I should use. Finally, it is quite complicated to explain in an article (and to my colleagues) a method that I don’t really understand. Do you have a more detailed and more affordable explanation on what is the MFSDA and why did you choose it to replace shapeAnalysisMANCOVA? I didn’t find any article using this method and we plan to submit our paper this summer…</p>
<p>Wish you a pleasant day,</p>

---

## Post #4 by @styner (2020-06-24 20:18 UTC)

<p>Hi Quentin, for simple analyses where covariates have limited interaction the two tools should generate similar results. But for strong interactions (e.g. if “age” as covariate interacts strongly with shape), shapeAnalysisMANCOVA will generate less correct results as these cannot be modeled well with the permutation tests used in shapeAnalysisMANCOVA.</p>
<p>We are aware that a tutorial for Covariance Significance Testing module is very much needed.</p>
<p>Btw, for your shapeAnalysisMANCOVA results, are you referring to the raw p-values or the multiple comparison corrected results?</p>
<p>Best<br>
Martin</p>

---

## Post #5 by @quentin_devignes (2020-06-25 12:03 UTC)

<p>Thank you Martin for your reply. For my shapeAnalysisMANCOVA results, I am referring to multiple comparison corrected results (with FDR fixed at 0.05).</p>
<p>Based on my MFSDA primary results, I looked at the different p-values (guessing that pvalue_Group Center Sex Age Education = p-values for group comparison corrected with the four covariates; pvalue_1 = interaction test (maybe as interaction test in shapeAnalysisMANCOVA) between shape and covariate <span class="hashtag-raw">#1</span> corrected with the 3 other covariates;  etc.) and found that Sex was the covariate which interacted the lesser with shape. So, I launched MFSDA and MANCOVA analyses with only this covariate (I tried without any covariate, but MFSDA led to no result if no covariate is given; I think it is normal as long as MFSDA is called “Covariate significance testing” in SlicerSALT, implying at least one covariate should be given. However, it may be useful to other users to know it). The results (attached files) are quite different… Of course, Sex was the covariate which interacted the lesser with shape among my covariates, it doesn’t mean it interacted weakly with shape. However, it seems that MANCOVA leads to more frequent and extensive deformation clusters. I read that SPHARM-PDM seems to be quite inconsistent. Maybe, using more powerful statistical analysis like MFSDA could provide more reliable results, but it is still to be understood and MFSDA seems quite complicated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9411f4f33225a5edbd688cf280727406cd17a9df.png" data-download-href="/uploads/short-url/l7T8ym5r3AVGNP3PWajoGkdN5Dh.png?dl=1" title="Comparison_MFSDA_MANCOVA_OneCovar copie" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9411f4f33225a5edbd688cf280727406cd17a9df_2_561x500.png" alt="Comparison_MFSDA_MANCOVA_OneCovar copie" data-base62-sha1="l7T8ym5r3AVGNP3PWajoGkdN5Dh" width="561" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9411f4f33225a5edbd688cf280727406cd17a9df_2_561x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9411f4f33225a5edbd688cf280727406cd17a9df_2_841x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9411f4f33225a5edbd688cf280727406cd17a9df_2_1122x1000.png 2x" data-dominant-color="9188A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Comparison_MFSDA_MANCOVA_OneCovar copie</span><span class="informations">1129×1005 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a statistical correction applied in the MFSDA? Or maybe it is not needed with this method? Having 4 different groups, it leads to 6 comparisons for each structure (8 structures in total). If there is no statistical correction in MFSDA, maybe I should at least apply a correction for these 48 comparisons. What do you think? And, if needed, how to compute it?</p>
<p>Finally, how to compute partial correlation between shape results and a cognitive z-score when we use MFSDA analyses? Do I have to launch Covariate significance test with the Z-score as a new covariate and look at the p-value associated with it?</p>
<p>Thank you very much for your help.<br>
Wish you a pleasant day,</p>
<p>Quentin</p>

---

## Post #6 by @styner (2020-07-06 17:01 UTC)

<p>Hi Quentin<br>
Not sure I was able to follow everything</p>
<ol>
<li>
<p>you have 5 variables in total: group (4 different groups of PD patients), center/site, sex, age and education. Of these, group (4 valued), center (how many values?) and sex (binary) are group variables (i.e. categorical variables). age and education are continuous variables. Is that correct?</p>
</li>
<li>
<p>how did you structure the input for shapeAnalysisMANCOVA? All groups/categorical variables need to be binary, mutually exclusive variables for shapeAnalysisMANCOVA. So, you would need to somehow be able to separate the analysis into different sets where you have only binary associations. That’s one of the downsides of using shapeAnalysisMANCOVA. If there is an order to your diagnosis (e.g. severity of disease groups) then you could group them into binary sets of increasing order. Alternatively, e.g. for the centers, you can have a binary variable for each center (so called one-shot variables), i.e. center1 (0/1), center2 (0/1) etc</p>
</li>
<li>
<p>you mentioned you did an interaction test. But, if I understand correctly, you want to do a group difference test. Interaction tests with shapeAnalysisMANCOVA only work with continuous variables, e.g. if you are interested in the association of age with shape, correcting for the other co-variates.</p>
</li>
<li>
<p>in a complex setting, such as yours with 3 categorical variables (2 of them being non-binary), shapeAnalysisMANCOVA is likely not going to yield correct results (there are just too many distinct sets to permute over).</p>
</li>
<li>
<p>how did you set up the MFSDA analysis exactly. MFSDA may interpret your group variable (with 4 values) as a continuous variable. I will need to double-check, but I am quite sure that also MFSDA needs binary categorical variables.</p>
</li>
</ol>

---

## Post #8 by @Lyndon_Pardo (2020-08-23 03:31 UTC)

<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a>, <a class="mention" href="/u/styner">@styner</a><br>
Hi! I’m relatively new to slicerSALT. I have input two sets of shapes of hippocampus, one for control group, and another for alzheimer’s group. I coded 0 for the control and 1 for the alzheimer’s. I know the p values are the significance values for the corresponding points of the shapes. But I also get 6 sets of attributes containing b values: betavalues_0_1, betavalues_0_group, betavalues_1_1, betavalues_1_group, betavalues_2_1, and betavalues_2_group.</p>
<p>I just want to ask what do the beta values mean? How do I interpret these? Thanks a lot!</p>

---

## Post #9 by @ikhsannk (2021-02-24 12:00 UTC)

<p>Hi <a class="mention" href="/u/styner">@styner</a></p>
<p>May I ask about the multiple covariate testing in the Covariate Significance Testing module?</p>
<p>I have 3 variables; group (categorical, controls vs patients), age (continuous), and center/site (categorical). When I conducted the analysis one-by-one (i.e. group only, age only) it exhibits a reasonable p-value result. However, when I tried to add another column (age) in my CSV file, only the p-value result for age shows up while the group p-value result shows plain colour.</p>
<p>Is there anything that I can do to fix this problem(s)? Thank you in advance.</p>
<p>Best,<br>
Ikhsan</p>

---

## Post #10 by @lili-yu22 (2025-01-15 05:33 UTC)

<p>I have the same result.who can  explain  the 6 betavalues.thanks</p>

---

## Post #11 by @lili-yu22 (2025-01-23 12:54 UTC)

<p>why can’t  the  developer  answer  me  the question  the  six  betavalue  mean？I have read a lot of papers and can not  find  the answer.Idoubt the module has been abandoned?</p>

---

## Post #12 by @muratmaga (2025-01-23 17:25 UTC)

<p><a class="mention" href="/u/lili-yu22">@lili-yu22</a></p>
<p>There is no guarantee that the developer of that functionality is tracking this forum. And your questions is very vague, you are saying that you have the same problem from a question four years ago.</p>
<p>I don’t think SlicerSALT has been abandoned, but I don’t think the development is particularly active.</p>

---

## Post #13 by @lili-yu22 (2025-01-23 18:15 UTC)

<p>Hi.I look all the similar issues. no expert  answer.The reason why I did not describe it clearly.because one person@Lyndon in this topic has already  described . I also try  send email  to the developer .but I found failed to send to the email address<br>
Can  you help  me?<br>
I have two groups.coded 0 for the control and 1 for the other one. no other variables .The results in population  viewers show the six beta values.I dont known  I have only two group  why  betavalues_2_1  appear. What do the 0,1, 2and group behind  the betavalue represent?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1584b73f13e1ca8e51cf8a277ecb2ca343497253.jpeg" data-download-href="/uploads/short-url/34mmT8CVJlKwrO080G4HNdX3MfV.jpeg?dl=1" title="mmexport1737656058049" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1584b73f13e1ca8e51cf8a277ecb2ca343497253_2_224x500.jpeg" alt="mmexport1737656058049" data-base62-sha1="34mmT8CVJlKwrO080G4HNdX3MfV" width="224" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1584b73f13e1ca8e51cf8a277ecb2ca343497253_2_224x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1584b73f13e1ca8e51cf8a277ecb2ca343497253_2_336x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1584b73f13e1ca8e51cf8a277ecb2ca343497253_2_448x1000.jpeg 2x" data-dominant-color="878A8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mmexport1737656058049</span><span class="informations">1920×4267 475 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @muratmaga (2025-01-23 20:08 UTC)

<aside class="quote no-group" data-username="lili-yu22" data-post="13" data-topic="12118">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/dbc845/48.png" class="avatar"> lili-yu22:</div>
<blockquote>
<p>I have two groups.coded 0 for the control and 1 for the other one. no other variables .The results in population viewers show the six beta values.</p>
</blockquote>
</aside>
<p>I am not familiar with this extension. Perhaps <a class="mention" href="/u/imbeatriz">@imbeatriz</a> can chime in?</p>

---

## Post #15 by @kmadi (2025-01-25 00:40 UTC)

<p>Hello,</p>
<p>I’m not a developer of MFSDA or SlicerSALT but I’ve used this software a lot recently. The way I’ve come to understand it is that the betavalues_0, betavalues_1, and betavalues_2 refer to the beta values (i.e., beta coefficients) for the x, y, and z directions, respectively. And the beta values/coefficients themselves refer to the slopes of the x, y, and z linear regressions, i.e., how much shape difference (in that direction) does each “unit” of your independent variable produce. So basically, the x, y, and z beta values show the directionality of your shape differences for that variable.</p>
<p>The “_Group” refers to your variable name (“Group”) and the “1” at the end (betavalues_0_1, betavalues_1_1, etc.) refers to the intercept…I think. But I would have the SlicerSALT devs confirm, just to be sure.</p>
<p>Hope that helps!</p>

---

## Post #16 by @lili-yu22 (2025-01-25 01:54 UTC)

<p>Thank you very much for your reply, this is very important to me.<br>
According to your analysis I think it is very reasonable, I still have a little question, 1.Is this interaction  the interaction between the group and the direction of the axis? after all, I only have one variable.2. which value should I choose to indicatethe difference between the two groups?<br>
thank you most sincerely</p>

---

## Post #17 by @kmadi (2025-01-25 03:52 UTC)

<p>I’m not sure I quite understand your first question, but yes, it’s the interaction between the group and the direction along that axis. The three beta values (0, 1, 2) for your variable “Group” represent the unique contribution of “Group” to the dependent variable (x, y, or z direction), controlling for all other variables in the model.</p>
<p>So:</p>
<p>“betavalues_0_Group” = directionality of shape difference in the x-direction going from Group 1 to Group 2<br>
“betavalues_1_Group” = directionality of shape difference in the y-direction going from Group 1 to Group 2<br>
“betavalues_2_Group” = directionality of shape differences in the z-direction going from Group 1 to Group 2</p>
<p>Basically, the beta values (0, 1, or 2) will give you how much in each direction (x, y, or z, respectively) that shape difference is as you go from Group 1 to Group 2. It’s up to you to decide which direction best explains the results/interpretation you want, but all three are generally useful. As far as I know, SlicerSALT/MFSDA doesn’t give you the option to show directionality in a way that combines x, y, and z into a resolved vector; you can only show them as x, y, and z components (one workaround is using the PCA module to create average models for each group, then using Model to Model Distance to show vector distances between the average models).</p>
<p>However, I don’t know the specifics of the analysis you’re performing. If your “Group” variable has only two possible values, then what I said above is true (and you can code the values as 0 or 1, as if they are ordinal variables). But if your “Group” variable has more than one value (Group 1, Group 2, Group 3, etc.), then a completely different interpretation applies, since now you’re dealing with categorical variables. I’m not a qualified statistician so I can’t really give you a good explanation myself, but ChatGPT can help with that <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> You’ll also want to consider including covariates/control variables in your analysis as well.</p>
<p>Hope that helps!</p>

---

## Post #19 by @lili-yu22 (2025-01-27 05:39 UTC)

<p>Thank you again for your patient and detailed explanation <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #20 by @lili-yu22 (2025-04-04 10:14 UTC)

<p>In SlicerSALT, when using the covariate significance testing module to analyze the “spharm_pdm.vtk” matrix file for the right condyle, Group 0 (Treatment Method A) and Group 1 c (Treatment Method B). Time points are 0 (pre-treatment) and 1 (post-treatment). After running the module, outputs include beta values (e.g., <code>betavalues_0_2</code>, <code>betavalues_0_groups</code>, <code>betavalues_0_time</code>, etc.) and p-values (<code>pvalue_group</code>, <code>pvalue_time</code>), but no p-value for the **group-time interaction，i found the  error log show“adding pvalue (4002,2)”this  mean no interaction，please Provide a code snippet to calculate the interaction p-value."</p>

---
