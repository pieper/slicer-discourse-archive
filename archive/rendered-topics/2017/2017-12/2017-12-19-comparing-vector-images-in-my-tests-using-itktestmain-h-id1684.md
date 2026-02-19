---
topic_id: 1684
title: "Comparing Vector Images In My Tests Using Itktestmain H"
date: 2017-12-19
url: https://discourse.slicer.org/t/1684
---

# Comparing Vector Images in my Tests (using itkTestMain.h)

**Topic ID**: 1684
**Date**: 2017-12-19
**URL**: https://discourse.slicer.org/t/comparing-vector-images-in-my-tests-using-itktestmain-h/1684

---

## Post #1 by @mschwier (2017-12-19 00:33 UTC)

<p>I am using itkTestMain.h as parent for module tests. However, I also need to compare Vector Images against their baseline and this is apparently not supported <a href="https://github.com/Slicer/Slicer/blob/1b713d1701dea926134ec6366134fa3e08caf21e/Base/CLI/Testing/itkTestMain.h#L263" rel="nofollow noopener">because the images are cast to double.</a></p>
<p>Did I overlook something or can you suggest an easy way to include Vector Image comparison in my tests?</p>

---

## Post #2 by @lassoan (2017-12-19 00:50 UTC)

<p>This should be available in ITK. I don’t know how they compare color images if they don’t have this. It could worth <a href="https://discourse.itk.org/">asking this from ITK people</a>.</p>
<p>A workaround could be to split the vector image to its components and compare each component separately.</p>

---

## Post #3 by @mschwier (2017-12-19 17:45 UTC)

<p>Thanks Andras, I asked there (they confirmed it is a limitation currently), and implemented the workaround you suggested. Currently I am doing this in a copy of itkTestMain.h in my project/slicer module. When I put the pull request up for that project, I could share it here, if you’d like to see if it is worth considering integrating it into Slicer!?</p>

---

## Post #4 by @mschwier (2017-12-19 18:13 UTC)

<p>In case you are interested in the workaround <a href="https://github.com/millerjv/PkModeling/pull/69/files#diff-c91316551f37754253eee5cb50c9e042" rel="nofollow noopener">follow this link</a>.</p>
<p>It’s a simple straight forward fix, not very sophisticated but better than before at least, since differences in Vector Images are now detected.</p>

---

## Post #5 by @lassoan (2017-12-20 18:26 UTC)

<p>Thank you. If you can get it integrated ITK then it is enough. Slicer regularly updates its ITK version, so your changes will eventually get into Slicer.</p>

---

## Post #6 by @mschwier (2017-12-20 18:51 UTC)

<p>Thing is, I only changed the itkTestMain.h, which is not part of ITK anymore (since 4 I think), but it was kept in Slicer for backwards compatibility (<a href="https://issues.slicer.org/view.php?id=2807" rel="nofollow noopener">see here</a>).</p>

---

## Post #7 by @lassoan (2017-12-20 18:54 UTC)

<p>If the file is not part of Slicer then please send us a pull request and we’ll merge your improvements. It would be great if you could also add a test somewhere that uses the new vector image compare feature (e.g., you could add a new test to one of the CLI modules).</p>

---
