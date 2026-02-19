---
topic_id: 12968
title: "Any Way To Parallelize Radiomics Feature Extraction On Pytho"
date: 2020-08-12
url: https://discourse.slicer.org/t/12968
---

# Any way to parallelize radiomics feature extraction on python?

**Topic ID**: 12968
**Date**: 2020-08-12
**URL**: https://discourse.slicer.org/t/any-way-to-parallelize-radiomics-feature-extraction-on-python/12968

---

## Post #1 by @xlucox (2020-08-12 15:54 UTC)

<p>Hi, I’m dealing with the extraction of a large set of radiomics feature in a large set of data, It took to much running time doing it with a simple loop in Python. I wonder if there is any way to fast it up using GPU.</p>
<p>On the other hand is there some library to extract radiomics features in C.</p>
<p>Thank you !!!</p>

---

## Post #2 by @pieper (2020-08-12 16:27 UTC)

<p>Thanks for the inquiry - we have been exploring some options like that but nothing there’s concrete at the moment.  But it’s good to know there’s community interest.</p>
<p>For many radiomics use cases you can leverage subject-level parallelism because there are a large number of similar cases to analyze and you can run them on independent cores or compute nodes in a cluster.</p>

---

## Post #3 by @JoostJM (2020-08-12 16:32 UTC)

<p>In addition to Steve’s comment, subject-level parallelization is already available in PyRadiomics, via the commandline interface. To enable this, specify the <code>--jobs</code> argument with an integer value specifying how many cores to use.</p>

---

## Post #4 by @thewtex (2020-08-13 17:21 UTC)

<p>The <a href="https://github.com/InsightSoftwareConsortium/ITKTextureFeatures" rel="nofollow noopener">itk-texturefeatures</a> Python package provides parallelized, fast, computation of a few radiomics features in C++.</p>

---

## Post #5 by @xlucox (2020-08-15 23:15 UTC)

<p>Thank you!!!</p>
<p>It was very helpful.</p>

---
