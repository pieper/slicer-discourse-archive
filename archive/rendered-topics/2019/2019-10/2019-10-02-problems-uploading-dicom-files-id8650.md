---
topic_id: 8650
title: "Problems Uploading Dicom Files"
date: 2019-10-02
url: https://discourse.slicer.org/t/8650
---

# Problems uploading DICOM files

**Topic ID**: 8650
**Date**: 2019-10-02
**URL**: https://discourse.slicer.org/t/problems-uploading-dicom-files/8650

---

## Post #1 by @Nichola0155 (2019-10-02 11:28 UTC)

<p>Operating system: windows<br>
Slicer version: 4.10.1<br>
Expected behavior: Loading DICOM files<br>
Actual behavior: Files will not load. Receiving the error: Irregular volume geometry detected (maximum error of 0.00282662 mm is above tolerance threshold of 0.001 mm).  Regularization transform is not added, as the option is disabled.</p>
<p>Hi all</p>
<p>I have been using 3D Slicer for a few months now for foot and ankle CT segmentation. Previously I have had no problems with the software and have found it excellent to use however recently I am unable to upload any DICOM files successfully. The critical error I receive is Irregular volume geometry detected (maximum error of 0.00282662 mm is above tolerance threshold of 0.001 mm).  Regularization transform is not added, as the option is disabled. I haven’t changed any of the files or settings and even files which previously worked smoothly will no longer load.</p>
<p>Any advice on how I can correct this would be great as I’m at a loss of how to fix it.</p>
<p>Thanks</p>
<p>Nichola</p>

---

## Post #2 by @lassoan (2019-10-02 11:32 UTC)

<p>Irregular geometry message is just a warning. The reported slice distance variation (0.0028mm) is very small and will not cause any issues. Do you have problems with loading images that previously could be loaded correctly? Could you copy the application log of a failed loading? (menu: Help / Report bugs) please also try upgrading Slicer to the latest stable version (currently 4.10.2).</p>

---

## Post #3 by @Nichola0155 (2019-10-04 10:40 UTC)

<p>I’ve updated to the newest version and the problem seems to have been resolved.</p>
<p>Thanks for the help and response</p>
<p>Nichola</p>

---
