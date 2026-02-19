---
topic_id: 5888
title: "Saving File Problems For Segmentation Project"
date: 2019-02-22
url: https://discourse.slicer.org/t/5888
---

# Saving File Problems for Segmentation Project

**Topic ID**: 5888
**Date**: 2019-02-22
**URL**: https://discourse.slicer.org/t/saving-file-problems-for-segmentation-project/5888

---

## Post #1 by @dekaya (2019-02-22 14:40 UTC)

<p><strong>Operating system:</strong> Mac OS<br>
<strong>Slicer version:</strong> 4.10.1<br>
<strong>Actual behavior:</strong> I have a problem with how Slicer saves my files. They either become too large as bundle (I.e., doubling in size for each iterative save) or they’re in multiple pieces sent to the destination I choose.</p>
<p>If I save :</p>
<p><strong>Normal (click save icon</strong>)- it gives me a TIFF, MRML, .seg.nrrd, .vp, .acsv<br>
<strong>As a bundle (MRB)</strong>- it seems to double in size with each iterative save even though I’ve barely modified it from the previous save.</p>
<p>I am doing segmenting on a prehistoric reptile skull for about 1500 TIFF files and creating separating label maps for each separate bone. I use some threshold painting to do the segmentation as the borders of each bone have nuances in them I have to refine—I can’t just do this automatically.</p>
<p>Ideally, I can save my file in the most straightforward way possible and then reload the file to continue my process without the file getting too large or turning into multiple pieces each time.</p>
<p>Thank you!</p>
<p>Deniz</p>

---

## Post #2 by @pieper (2019-02-22 19:55 UTC)

<p>The MRB is really just a .zip file, so if you change the file extension you can unzip and see what is inside and see what is getting bigger each time.  Probably this is related to using the TIFF files and it could be fixable.  In the meantime, maybe if you convert to nrrd files first and then save those in the MRB you could avoid this issue.</p>

---

## Post #3 by @dekaya (2019-02-23 02:52 UTC)

<p>Thank you! I only selected the .nrrd option and then used MRB and for some reason that seemed to work; the files don’t double each time now. I unzipped the files and yeah I think prior to just selecting the .nrrd, it was probably grabbing everything and doubling it.</p>

---
