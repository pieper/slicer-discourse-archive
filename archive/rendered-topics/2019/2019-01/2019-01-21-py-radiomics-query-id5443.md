---
topic_id: 5443
title: "Py Radiomics Query"
date: 2019-01-21
url: https://discourse.slicer.org/t/5443
---

# Py RADIOMICS query

**Topic ID**: 5443
**Date**: 2019-01-21
**URL**: https://discourse.slicer.org/t/py-radiomics-query/5443

---

## Post #1 by @RadioQuest (2019-01-21 14:41 UTC)

<p>Hi…<br>
I am working on TA to study changes in a longitudinal study.<br>
I am doing 2 step registration process - 1. affine from A to B and later Bspline using this affine as a linear transform.<br>
However, I have following queries</p>
<ol>
<li>Is it necessary to select histogram matching for TA (I have already performed N4 bias correction)</li>
<li>If I have to select this option, shall I choose this during affine transformation or non-rigid part of registration?<br>
Please note brain scans B/C etc are distorted post surgery.</li>
<li>And does baseline scan (A) need any registration ? as it will be used as a template and also control?<br>
Thanks in advance.<br>
Kind Regards,<br>
RQ</li>
</ol>

---

## Post #2 by @pieper (2019-02-06 18:13 UTC)

<p>Hi -</p>
<p>Probably best to post to <a href="https://groups.google.com/forum/#!forum/pyradiomics" rel="nofollow noopener">the pyradiomics list</a> if you haven’t already.</p>
<p>My first guess at the answers are:</p>
<ol>
<li>still a good idea</li>
<li>probably use the untransformed data to make the histogram (or mask it if the post-surgery images have artifacts that would skew the histogram)</li>
<li>No, not if it’s the reference space.</li>
</ol>

---
