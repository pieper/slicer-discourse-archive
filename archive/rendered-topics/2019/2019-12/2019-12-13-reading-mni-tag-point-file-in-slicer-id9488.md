# Reading MNI Tag point file in Slicer

**Topic ID**: 9488
**Date**: 2019-12-13
**URL**: https://discourse.slicer.org/t/reading-mni-tag-point-file-in-slicer/9488

---

## Post #1 by @Tina_Kapur (2019-12-13 18:30 UTC)

<p>Are there any converters from MNI Tag point file format to any fiducial format supported by Slicer?<br>
Here is an example file I am trying to read from the RESECT dataset of intraoperative (brain tumor resection) ultrasound images.</p>
<p>MNI Tag Point File<br>
Volumes = 2;<br>
% Case 1: beforeUS-afterUS landmarks</p>
<p>Points =<br>
43.050327 -19.574389 28.646246 41.457959 -16.079460 31.171195 “”<br>
38.000286 -19.310701 35.832615 35.130024 -14.587492 37.726655 “”<br>
51.176403 -17.693413 24.917555 49.881248 -13.153977 28.732701 “”<br>
38.861774 -20.050928 25.793882 37.478477 -16.680896 28.096297 “”<br>
50.099995 -26.474323 29.119776 47.648433 -20.993724 32.975789 “”<br>
31.413071 -26.502275 36.817249 29.273389 -23.599029 37.123024 “”<br>
43.039112 -25.471384 33.563751 41.368420 -18.605544 35.046250 “”<br>
40.093475 -18.521191 32.495602 37.222461 -13.863806 35.037693 “”<br>
53.474316 -16.070513 21.060978 53.456625 -11.780752 24.582612 “”<br>
49.392509 -21.698021 23.596071 46.805256 -18.661988 28.095797 “”<br>
52.977638 -44.353401 36.864697 49.909545 -38.577435 39.135014 “”<br>
47.454781 -24.305759 35.963745 43.864646 -20.316818 39.355339 “”<br>
40.226463 -15.148485 31.796501 37.364169 -10.662443 33.880712 “”;</p>

---

## Post #2 by @pieper (2019-12-13 19:15 UTC)

<p>I don’t know of any, but it looks pretty straightforward (better if you also have a screenshot or similar way of knowing that you get the coordinate system assumptions correct - do you have that?)</p>

---

## Post #3 by @Tina_Kapur (2019-12-13 21:56 UTC)

<p>We manually put the coordinates into an fcsv file and the fiducials show up in sensible places (relative to the underlying ultrasound) so I think that the coordinate system assumptions are correct.</p>

---

## Post #4 by @pieper (2019-12-14 14:46 UTC)

<p>I guess this is the format spec:</p>
<p><a href="https://en.wikibooks.org/wiki/MINC/SoftwareDevelopment/Tag_file_format_reference" class="onebox" target="_blank">https://en.wikibooks.org/wiki/MINC/SoftwareDevelopment/Tag_file_format_reference</a></p>
<p>To be honest it doesn’t look like a great format, but if you need to read a bunch of files it should be simple to write a little python script to read them or even register “.tag” to load them automatically.</p>

---
