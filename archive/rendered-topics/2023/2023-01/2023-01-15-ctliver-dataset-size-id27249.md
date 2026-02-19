---
topic_id: 27249
title: "Ctliver Dataset Size"
date: 2023-01-15
url: https://discourse.slicer.org/t/27249
---

# CTLiver dataset size

**Topic ID**: 27249
**Date**: 2023-01-15
**URL**: https://discourse.slicer.org/t/ctliver-dataset-size/27249

---

## Post #1 by @muratmaga (2023-01-15 23:21 UTC)

<p>Is there a reason why the CT Liver data type is float (as opposed to short)? I am not very familiar with medical imaging, but I always thought CT dicoms were only 12 bit and discrete? If it is not necessary, can we cast to short and update the sample data repo?</p>
<p>At 280MB it is one of the slower downloads from the sample data. ushort version is about 215MB.</p>

---

## Post #2 by @pieper (2023-01-16 18:17 UTC)

<p>Sure, if you think it’s worth the effort a PR would be welcome.</p>

---
