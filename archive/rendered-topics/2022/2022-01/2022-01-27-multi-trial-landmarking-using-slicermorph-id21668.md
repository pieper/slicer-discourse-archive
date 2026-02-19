---
topic_id: 21668
title: "Multi Trial Landmarking Using Slicermorph"
date: 2022-01-27
url: https://discourse.slicer.org/t/21668
---

# Multi-trial landmarking using SlicerMorph

**Topic ID**: 21668
**Date**: 2022-01-27
**URL**: https://discourse.slicer.org/t/multi-trial-landmarking-using-slicermorph/21668

---

## Post #1 by @anromero (2022-01-27 22:33 UTC)

<p>Hello there, I’m doing a study on cranial fluctuating asymmetry and the Procrustes ANOVA that is common for statistical analysis of FA requires at minimum two landmarking trials (I typically use the geomorph package in R and/or MorphoJ). I have used the PseudoLMGenerator to create a template for the specimen in my sample that was closest to the average shape, and then I used this template to apply landmarks to the remaining specimens. I’m looking for suggestions on how to do a second landmarking trial because applying the landmark template via ALPACA a second time provides the same results.</p>
<p>Thanks,<br>
Ashly</p>

---

## Post #2 by @muratmaga (2022-01-28 01:49 UTC)

<p>FA in itself does not require you have replicates. However, most of the times the amount of L/R deviations you are measuring for FA is so small that, it is important to know the measurement error associated with manual landmarking and evaluate the results in that context. That’s where replicates come in. You should be able to write your statistical model with only IND + SIDE terms.</p>
<p>There is no measurement error in ALPACA in that sense.</p>
<p>This might be of use to you:</p>
<p>Klingenberg, C. P. (2015). Analyzing Fluctuating Asymmetry with Geometric Morphometrics: Concepts, Methods, and Applications. <em>Symmetry</em> , <em>7</em> (2), 843–934. <a href="https://doi.org/10.3390/sym7020843" rel="noopener nofollow ugc">https://doi.org/10.3390/sym7020843</a></p>

---

## Post #3 by @anromero (2022-01-28 17:31 UTC)

<p>So to make sure I’m understanding, writing the model to only have IND + SIDE terms is not the same as removing the replicate option in the model already in geomorph? I tried running it without the replicate option and these are the results I received from the Procrustes ANOVA:</p>
<p>Call:<br>
bilat.symmetry(A = LMs, ind = Classifiers.batch$Individual, object.sym = TRUE,<br>
land.pairs = LM.pairs.batch)</p>
<p>Symmetry (data) type: Object</p>
<p>Type I (Sequential) Sums of Squares and Cross-products<br>
Randomized Residual Permutation Procedure Used<br>
1000 Permutations</p>
<h2><a name="p-73177-shape-anova-df-ss-ms-rsq-f-z-prf-ind-24-005579-000232-011156-43707-40962-0001-side-1-043151-043151-086292-8114024-39471-0001-indside-24-001276-000053-002552-total-49-050005-1" class="anchor" href="#p-73177-shape-anova-df-ss-ms-rsq-f-z-prf-ind-24-005579-000232-011156-43707-40962-0001-side-1-043151-043151-086292-8114024-39471-0001-indside-24-001276-000053-002552-total-49-050005-1" aria-label="Heading link"></a>Shape ANOVA<br>
Df      SS      MS     Rsq        F      Z Pr(&gt;F)<br>
ind      24 0.05579 0.00232 0.11156   4.3707 4.0962  0.001 **<br>
side      1 0.43151 0.43151 0.86292 811.4024 3.9471  0.001 **<br>
ind:side 24 0.01276 0.00053 0.02552<br>
Total    49 0.50005</h2>
<p>Signif. codes:  0 ‘<em><strong>’ 0.001 ‘</strong>’ 0.01 ‘</em>’ 0.05 ‘.’ 0.1 ‘ ’ 1</p>
<p>The problem here is that there is no significance value for the ind:side interaction (FA).</p>

---

## Post #4 by @muratmaga (2022-01-28 18:39 UTC)

<p>I am not sure why that would be the case.<br>
That’s a geomorph and R question. Perhaps ask in their forum?<br>
<a href="https://groups.google.com/g/geomorph-r-package?pli=1" class="onebox" target="_blank" rel="noopener nofollow ugc">https://groups.google.com/g/geomorph-r-package?pli=1</a></p>

---

## Post #5 by @anromero (2022-01-28 18:56 UTC)

<p>Okay, thank you! Will do.</p>

---

## Post #6 by @anromero (2022-01-31 19:29 UTC)

<p>Just an update for anyone looking for answers here. I reached out to the geomorph forum and this was the reply:</p>
<p>“By definition, there is no test of significance of the interaction of the bilateral symmetry model without the replicates. Put more statistically, the interaction term is tested against replicate variation (see basic theory papers for bilateral symmetry designs for more detail).”</p>

---

## Post #7 by @muratmaga (2022-01-31 21:12 UTC)

<p>That’s because of the reason I explained above. Author’s of geomorph use manual landmarks, and without replications you cannot tease out your digitization errors from the analysis for FA. hence they require replication. That issue doesn’t happen in automated methods that generate repeatable results.</p>
<p>FYI, you can replicate things in ALPACA, by just swapping out your template and rerunning the analysis. That would be analogous to their replication. You will be replicating the entire pipeline, not just the digitization step. However, your main issue is that I think instead of anatomical landmarks, you used pseudoLMs, which is depended on the geometry of the source mesh, and if you choose a different source mesh, you will get a different set of pseudoLMs (both in position and numbers).</p>
<p>You can restrict yourself to the manual LMs, you can generate replicates in ALPACA by using different templates. That way you will satisfy their requirement.</p>

---

## Post #8 by @anromero (2022-01-31 21:18 UTC)

<p>That makes sense. I do have a template of manual anatomically-based LMs that I can use. I will try that option as well. Thank you for your help!</p>

---
