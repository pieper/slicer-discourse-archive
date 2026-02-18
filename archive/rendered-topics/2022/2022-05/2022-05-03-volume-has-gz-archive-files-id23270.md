# volume has Gz archive files

**Topic ID**: 23270
**Date**: 2022-05-03
**URL**: https://discourse.slicer.org/t/volume-has-gz-archive-files/23270

---

## Post #1 by @pmabz (2022-05-03 21:49 UTC)

<p>Operating system: ubuntu<br>
Slicer version:5.1.0<br>
Expected behavior: read files<br>
Actual behavior: no DICOM data<br>
i have 514  fo;es, of type Gzip archive and one test file thus</p>
&lt;?xml version="1.0" encoding="utf-8"?&gt;

  -921167223
  20.546511810615367
  1.9429095730933224E-05
  29.573675835020598
  13.884745762711864
  -3.3146820809248556
  3
  1.5
  0
  512
  2945
  0.16
  0.08
  {19962BC9-2744-4642-ACEA-4F1CA3EDB043}
  0000292ed04ea9f3
  202204261135

<p>i have spent hours looking for a solution …</p>
<p>many thanks</p>

---

## Post #2 by @lassoan (2022-05-03 23:13 UTC)

<p>You need to start with unzipping the archive files. If they contain DICOM files then you can load them as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#dicom-data">here</a>.</p>

---
