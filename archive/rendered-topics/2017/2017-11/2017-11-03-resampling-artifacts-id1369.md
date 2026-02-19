---
topic_id: 1369
title: "Resampling Artifacts"
date: 2017-11-03
url: https://discourse.slicer.org/t/1369
---

# Resampling artifacts

**Topic ID**: 1369
**Date**: 2017-11-03
**URL**: https://discourse.slicer.org/t/resampling-artifacts/1369

---

## Post #1 by @muratmaga (2017-11-03 22:28 UTC)

<p>Now that I can actually use resample scalar volume, this was my real issue:</p>
<p>I there are some strong artifacts that show up in the resample volume. Is there a way to deal with this? I tried using cosine bspline, WS as interpolators. They took much longer but didn’t necessarily do a better job.</p>
<p><strong>UNDER TRANSFORM</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b1e450814f728a68372f77d1be5d26605f1c2c3.png" alt="under_transform" data-base62-sha1="aIwF5uBZjrvTFhcJCIywuxJfvzl" width="514" height="404"><br>
<strong>RESAMPLED</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36afeb237a0049a3a2a370bb0f00c2e34b0077df.png" alt="resampled" data-base62-sha1="7NMGB6VOqtu5tbkAnV9LHlxI3qT" width="529" height="394"></p>

---

## Post #2 by @lassoan (2017-11-03 23:58 UTC)

<p>When you dynamically apply a transform, a high-resolution image is computed for the slice viewer. If you want to see similar image quality then you may need a higher resolution reference volume. Crop volume can transform and supersample the volume, so it is very convenient for this purpose. I would recommend isotropic spacing and you may try to decrease the spacing by a factor of 2 to 5.</p>

---
