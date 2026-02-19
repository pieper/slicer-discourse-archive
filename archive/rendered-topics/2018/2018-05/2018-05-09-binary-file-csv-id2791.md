---
topic_id: 2791
title: "Binary File Csv"
date: 2018-05-09
url: https://discourse.slicer.org/t/2791
---

# Binary File CSV

**Topic ID**: 2791
**Date**: 2018-05-09
**URL**: https://discourse.slicer.org/t/binary-file-csv/2791

---

## Post #1 by @stevenagl12 (2018-05-09 20:22 UTC)

<p>How would you go about saving a csv file, or xml file for a binary labelmpa for use in other softwares, etc. Where every pixel with a 1 is tagged in the file with the x, y and z dimensions, etc.?</p>

---

## Post #2 by @pieper (2018-05-09 21:34 UTC)

<p>We usually don’t do that because the file would be quite large, but you could get the data which something like:</p>
<pre><code class="lang-auto">labelarray = array('MRHead-label')
import numpy
numpy.where(labelarray==1)
</code></pre>
<p>you’ll get three lists of coordinates that you can write out in whatever format you need.</p>

---

## Post #3 by @stevenagl12 (2018-06-04 13:54 UTC)

<p>What about reading in such a CSV file and creating a binary, is that possible?</p>

---

## Post #4 by @lassoan (2018-06-04 14:19 UTC)

<p>You easily can do all that in Python.</p>
<p>However, this file format of listing non-zero voxels only makes sense if you have a very low number of points (up to maybe a few ten thousands), because otherwise it would be very slow to read and write the file. Why do you consider using this file format? If the problem is that you have very sparse data and file storage is not efficient then you can store the labelmap volume with zip compression. Compressed nrrd file readers and writers are available in all relevant programming languages and environments.</p>

---
