---
topic_id: 3950
title: "Command Line Conversion Of Dicom Images And Rtstruct To Nrrd"
date: 2018-08-30
url: https://discourse.slicer.org/t/3950
---

# Command line conversion of DICOM images and RTStruct to NRRD

**Topic ID**: 3950
**Date**: 2018-08-30
**URL**: https://discourse.slicer.org/t/command-line-conversion-of-dicom-images-and-rtstruct-to-nrrd/3950

---

## Post #1 by @Daniel_Marcus (2018-08-30 13:59 UTC)

<p>Hey all,</p>
<p>We’re looking to convert DICOM images and associated RTStructs to NRRD from the command line (actually as an automation in XNAT). Before we dig in, I just wanted to check on the state of the art for doing this with Slicer/SlicerRT.  It looks like <a href="https://github.com/Radiomics/pyradiomics/issues/263" rel="nofollow noopener">Steve was making progress on this</a> via pyradiomics as was <a href="https://github.com/QIICR/dcmheat/blob/master/docker/SlicerConvert.py" rel="nofollow noopener">Andrei via QIICR</a>.  Are those the best examples for us to be working from? Or is there other code around that we haven’t come across yet?</p>
<p>Thanks in advance,<br>
Dan</p>

---

## Post #2 by @pieper (2018-08-30 21:03 UTC)

<p>Howdy Dan -</p>
<p>Did you look at <a href="http://plastimatch.org/">plastimatch</a>?  I’ve heard it works well and would be good for batches.</p>
<p>The SlicerRT based one you linked to was also working well for me.  It turned out the data I was trying to convert was fundamentally flawed so I didn’t end up using it (something about the table being moved during therapy but not recorded in the files).  Other than that I believe it works well and it can sometimes be useful to load the original RT data in Slicer anyway for QC before exporting the labelmaps.</p>
<p>Best,<br>
Steve</p>

---
