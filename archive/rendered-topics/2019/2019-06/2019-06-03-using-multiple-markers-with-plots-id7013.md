---
topic_id: 7013
title: "Using Multiple Markers With Plots"
date: 2019-06-03
url: https://discourse.slicer.org/t/7013
---

# Using multiple markers with Plots

**Topic ID**: 7013
**Date**: 2019-06-03
**URL**: https://discourse.slicer.org/t/using-multiple-markers-with-plots/7013

---

## Post #1 by @muratmaga (2019-06-03 20:42 UTC)

<p>Hello,</p>
<p>I am trying to manipulate a scatter plot. Data is stored in a table with bunch of classifiers like experimental groups, sex, etc, which I would like to show as different colors/markers. Unfortunately, I couldn’t figure out how to do it with the UI, is there a way to do it through python?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbfd3fe41cf4457533c718ea2ace99a160e5921a.png" data-download-href="/uploads/short-url/zXcqE7Ry1vZc4vDTRSnK1pqCYDE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbfd3fe41cf4457533c718ea2ace99a160e5921a_2_462x500.png" alt="image" data-base62-sha1="zXcqE7Ry1vZc4vDTRSnK1pqCYDE" width="462" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbfd3fe41cf4457533c718ea2ace99a160e5921a_2_462x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbfd3fe41cf4457533c718ea2ace99a160e5921a_2_693x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbfd3fe41cf4457533c718ea2ace99a160e5921a.png 2x" data-dominant-color="FAF9F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">773×836 15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-06-03 21:11 UTC)

<p>You can set marker style and color for each series.</p>

---

## Post #3 by @muratmaga (2019-06-03 21:28 UTC)

<p>Yes, I can do add another series and plot them together. But there doesn’t appear to be an option to subset the data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71bbb09ab67d2c879de3cc917a96998aed1aa741.png" data-download-href="/uploads/short-url/ge84PbJmRryOc4wy0L1rTRbPa1z.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71bbb09ab67d2c879de3cc917a96998aed1aa741.png" alt="image" data-base62-sha1="ge84PbJmRryOc4wy0L1rTRbPa1z" width="455" height="500" data-dominant-color="FCF9F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">630×691 14.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-06-03 21:58 UTC)

<p>Why would you change the marker style within one series? It should not be too hard to split your data set into multiple series.</p>
<p>You can select a subset of points, if you want to extract certain data points.</p>
<p>What is your use case?</p>

---

## Post #5 by @muratmaga (2019-06-04 02:53 UTC)

<p>My use case is a dataframe with bunch of PC scores from morphometric analysis of specimens and their associated covariates or classifiers such as sex, genotype, age, etc… I want to visually inspect, if any of the segregation along PC plots corresponds to one of these covariates (e.g., male vs female). Both for exploration and data vetting.</p>
<p>I know I can interactively select points on the plot, what I don’t know what to do with that selection and how to use that to subset from UI.</p>
<p>If it helps, here is a sample dataset:<br>
<a href="https://app.box.com/s/5n6xdtld331d2r1c8yqhskzhuzkj0568" class="onebox" target="_blank" rel="noopener">https://app.box.com/s/5n6xdtld331d2r1c8yqhskzhuzkj0568</a></p>
<p>If it explains any further, this is what I would have done in R with the same data (sorry box doesn’t let me read the data directly to R, you need to save the csv file locally, and read it).</p>
<blockquote>
<p>dat=read.csv(file=‘pcScores.csv’)<br>
plot(dat$PC1, dat$PC2, col=as.integer(dat$Group), pch=20, cex=2)</p>
</blockquote>
<p>Clearly based on morphometric results, one individual does not belong to the group it has been labeled with (either the label is wrong, or the experiment had no effect).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1a4c863720492cf588e451addbb528d08f952af.png" data-download-href="/uploads/short-url/plvyzSoF7qz4FY600W2QuVXYuFp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1a4c863720492cf588e451addbb528d08f952af_2_309x250.png" alt="image" data-base62-sha1="plvyzSoF7qz4FY600W2QuVXYuFp" width="309" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1a4c863720492cf588e451addbb528d08f952af_2_309x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1a4c863720492cf588e451addbb528d08f952af_2_463x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1a4c863720492cf588e451addbb528d08f952af_2_618x500.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">842×681 23.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2019-06-04 04:02 UTC)

<p>There tools specifically developed for general data mining/exploration (Knime, RapidMiner, etc.) and you can explore data by little generic Python or R coding. I would only use Slicer plots for implementing specific workflows already identified using these tools. For example, you could implement a Slicer module, which splits series in a table based on a selected column’s value and plots them.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="7013">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>if any of the segregation along PC plots corresponds to one of these covariates</p>
</blockquote>
</aside>
<p>If you are lucky then the first few principal components may coincide with some real-world (biologically, anatomically, clinically, …) meaningful values, but very often they do not (instead, each principal component may represent a mix of several real-world factors). Since you have labelled data, you can directly obtain optimal separation of groups by using a <em>supervised</em> classification/regression method (SVM, LDA, neural networks, etc.).</p>

---

## Post #7 by @muratmaga (2019-06-04 04:22 UTC)

<p>Those are good points, but a little beyond what I am trying to accomplish.</p>
<p>That’s a tutorial dataset, and I am just trying to showcase a simple use of PCA to catch a case of (1) either data mislabeling or (2) an interesting case where an 1 out of 20 experiments failed for some reason. I would like to do that in Slicer, through UI if possible.</p>
<p>While your comments about PCs are quite true for heteregenous populations, where you cannot control for confounding factors easily, things are a little different in the experimental realm, where we can have quite a bit of control at the very low level (as much as biology permits us). For example, those mice are genetically identical with the exception of a single mutation in one group, which causes haploinsufficiency (gene dosage effect). Granted, it is as good as it gets (with the exception of one data point), and hence it is a tutorial data.</p>
<p>This is not my dataset, how the investigator chases these results is up to them, I am just trying to make sure simple data vetting can be done within Slicer without having to export them into another platform. If I were them, I would have double checked the data labelling for that specimen, and if I am certain of all my experimental notes, then I would do a whole genome sequencing on that specimen.</p>

---

## Post #8 by @lassoan (2019-06-04 19:46 UTC)

<p>I think at this point the only way to do this in Slicer with a GUI is to create a small module that sets up the plot (takes a table and 2 independent variable columns, 1 dependent variable column; splits the series to two multiple series based on dependent variable values, and shows them in a plot). It could be a good example of how easy it is to create such a custom module.</p>

---
