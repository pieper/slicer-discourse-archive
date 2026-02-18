# Vertebral Foramen Segmentation with Fill between Slices

**Topic ID**: 25994
**Date**: 2022-11-01
**URL**: https://discourse.slicer.org/t/vertebral-foramen-segmentation-with-fill-between-slices/25994

---

## Post #1 by @dav (2022-11-01 01:39 UTC)

<p>Trying to segment the vertebral space in this image where I’ve already segmented out the lumbar spine.</p>
<p>I found that fill between slices works moderately well, (see image)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9425197f13b10ad4fc2da31fbefd412dc3b472d.png" alt="fill_btwn_slices1" data-base62-sha1="xhvkWBDr9tWhZ8UrfzBphMRqATb" width="326" height="401"></p>
<p>however upon initializing  you can see how the rest of the segments grow, and I can’t select islands to remove this growth and I don’t know how to lock those segments so only the vertebral space grows.</p>
<p>Unfortunately I can’t always segment out the space as it’s not always straight (seen here)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b12a54ef8e8b0b2a31ec69624f75a3e1b3419786.png" alt="fill_btwn_slices2" data-base62-sha1="phhcSmtYNyUjun52bLlbu1IOvoG" width="283" height="394"></p>
<p>and the CT data isn’t the best resolution for segmenting out the spinal column as some other form of help here.</p>
<ul>
<li>How can I fill slices on just one segmentation without influencing the others?</li>
<li>Or what other tricks can I use to get this segmentation nicely?</li>
</ul>

---
