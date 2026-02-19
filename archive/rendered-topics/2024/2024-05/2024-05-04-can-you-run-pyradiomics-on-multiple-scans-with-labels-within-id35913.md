---
topic_id: 35913
title: "Can You Run Pyradiomics On Multiple Scans With Labels Within"
date: 2024-05-04
url: https://discourse.slicer.org/t/35913
---

# Can you run PyRadiomics on multiple scans with labels within Slicer?

**Topic ID**: 35913
**Date**: 2024-05-04
**URL**: https://discourse.slicer.org/t/can-you-run-pyradiomics-on-multiple-scans-with-labels-within-slicer/35913

---

## Post #1 by @Numan_Kutaiba (2024-05-04 11:58 UTC)

<p>Hi,<br>
I have used Slicer to extract radiomics features from CT scans with segmentation masks (for liver and spleen); one scan and mask at a time.<br>
I want to know if I could do the same for a whole folder of multiple scans with their masks.<br>
I don’t have good coding skills. I want to know if this is possible before I try to learn how to do this using a code outside Slicer.<br>
Let me know if the question doesn’t make sense.<br>
Thanks</p>

---

## Post #2 by @pieper (2024-05-04 12:07 UTC)

<p>Here’s what our chatbot says based on searching this forum.  Looks like a reasonable answer:</p>
<p><a href="https://discourse.slicer.org/u/claude_3_opus_bot">claude_3_opus_bot</a>Forum Helper</p>
<p><a href="https://discourse.slicer.org/t/untitled-ai-bot-pm/35914/2">1m</a></p>
<p>SearchSearch</p>
<p>Based on the search results, it looks like it is possible to extract radiomics features from multiple scans and segmentations in a batch mode in Slicer. A few key points:</p>
<ol>
<li>You can use the PyRadiomics extension in Slicer to do batch processing and extract features from multiple images and segmentations. See this post for an example of using the PyRadiomics CLI module for batch processing:</li>
</ol>
<p><a href="https://discourse.slicer.org/t/radiomics-cli-parameters/32175">Radiomics cli parameters</a></p>
<ol start="2">
<li>Your input images and segmentations should be in a format like NRRD. You may need to convert from DICOM first. There are CLI modules in Slicer to convert DICOM to NRRD in a batch.</li>
</ol>
<p><a href="https://discourse.slicer.org/t/dicom-to-nrrd-conversion-in-command-line-for-pyradiomics/32306">DICOM to NRRD conversion in command line (for PyRadiomics)</a></p>
<ol start="3">
<li>There are various settings you can use to control the PyRadiomics feature extraction, like limiting to certain features, resampling, handling 2D/3D, etc. See posts like these for details:</li>
</ol>
<p><a href="https://discourse.slicer.org/t/issue-with-2d-extraction-and-resampling/9910">Issue with 2D extraction and resampling</a></p>
<p><a href="https://discourse.slicer.org/t/pet-normalisation-before-radiomics/12765">PET normalisation before Radiomics</a></p>
<p>So in summary, while it requires using the command line interface instead of the GUI, it is very possible to extract radiomics features from a batch of images and segmentations using Slicer and the PyRadiomics extension. Let me know if you have any other questions!</p>

---

## Post #3 by @Saima (2024-05-05 01:32 UTC)

<p>Hi<br>
It is possible to run pyradiomics to do batch processing. I have written a code for it not yet published but i can upload on github coming monday.</p>
<p>Regards,<br>
Saima</p>

---
