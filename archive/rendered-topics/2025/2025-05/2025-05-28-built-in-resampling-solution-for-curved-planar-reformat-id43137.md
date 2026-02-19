---
topic_id: 43137
title: "Built In Resampling Solution For Curved Planar Reformat"
date: 2025-05-28
url: https://discourse.slicer.org/t/43137
---

# Built-in Resampling Solution for Curved Planar Reformat

**Topic ID**: 43137
**Date**: 2025-05-28
**URL**: https://discourse.slicer.org/t/built-in-resampling-solution-for-curved-planar-reformat/43137

---

## Post #1 by @MarkLiu (2025-05-28 14:01 UTC)

<p>Dear Community,<br>
I’m currently using the curved planar reformat to re-sample the CT images. And it normally takes about 10 seconds to finish the execution, which is a little bit long to my application. I briefly checked the execution details, and it seems that the Resample Scalar/Vector/DWI volume takes most of the time. I think maybe the standalone execution method takes additional time on the read/write of image files. Are there any build-in methods which can be used to do the similar work with Resample Scalar/Vector/DWI volume module? Or the Resample Scalar/Vector/DWI volume module can be used in a more efficient way?</p>
<p>Thanks in advance!</p>

---
