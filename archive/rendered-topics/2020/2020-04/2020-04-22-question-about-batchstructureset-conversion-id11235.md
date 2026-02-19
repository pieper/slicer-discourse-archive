---
topic_id: 11235
title: "Question About Batchstructureset Conversion"
date: 2020-04-22
url: https://discourse.slicer.org/t/11235
---

# Question about batchstructureset conversion

**Topic ID**: 11235
**Date**: 2020-04-22
**URL**: https://discourse.slicer.org/t/question-about-batchstructureset-conversion/11235

---

## Post #1 by @codecrazer (2020-04-22 00:26 UTC)

<p>Dear colleague, I have used the batchstructuresetconversion script, it is very convenience. However, the output file or NRRD didn’t contain the origin patinet ID, how could I do it? Thanks for your help!</p>

---

## Post #2 by @cpinter (2020-04-22 08:51 UTC)

<p>You could change the code <a href="https://github.com/SlicerRt/SlicerRT/blob/master/BatchProcessing/BatchStructureSetConversion.py#L330">here</a> so that the folder name contains the DICOM patient ID and not the database patient UID.</p>

---

## Post #3 by @codecrazer (2020-04-22 09:50 UTC)

<p>I solved it! Thanks a lot!!!</p>

---

## Post #4 by @cpinter (2020-04-22 10:47 UTC)

<p>If you think that your solution can be useful for others, than please create a pull request and we can incorporate it in the official repository. Thanks!</p>

---

## Post #5 by @codecrazer (2020-04-22 12:41 UTC)

<p>I send my pull request! Thanks!</p>

---
