# Mammographic tumer identification

**Topic ID**: 15254
**Date**: 2020-12-28
**URL**: https://discourse.slicer.org/t/mammographic-tumer-identification/15254

---

## Post #1 by @gabrielasliwa (2020-12-28 18:59 UTC)

<p>I’m biomedical engineering student and I’m new in slicer and I don’t know a lot of funcions.<br>
My biggest isue is that i don’t know how identificate a tumer on mammographic picture. Which function should i use? Should I search in segmant editor?</p>
<p>If someone is polish it would be much easier, thank you.</p>

---

## Post #2 by @lassoan (2020-12-28 21:48 UTC)

<p>There is only a small subset of tumors that you can identify from mammography. Many tumors do not show up at all in X-ray mammography images, while others may look suspicious but not end up being malignant lesions. So, identification of of tumors on mammo images is not really a software issue, but a hard, probably unsolvable clinical problem (using mammography alone is just not enough to identify tumors).</p>
<p>Of course you can still train a neural network to identify suspicious lesions on mammo images, and even though it is not perfect, can still be practically useful. I would assume that there are lots of training data sets available to train your network and probably there are dozens of solutions already proposed for this. So, I would recommend to start with some web and literature search and try to reproduce results reported by others.</p>

---
