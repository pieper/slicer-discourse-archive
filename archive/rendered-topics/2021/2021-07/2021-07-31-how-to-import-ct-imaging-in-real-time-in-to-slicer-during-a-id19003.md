# How to import CT imaging in real-time in to Slicer during a procedure?

**Topic ID**: 19003
**Date**: 2021-07-31
**URL**: https://discourse.slicer.org/t/how-to-import-ct-imaging-in-real-time-in-to-slicer-during-a-procedure/19003

---

## Post #1 by @ocho87 (2021-07-31 18:39 UTC)

<p>Hi,</p>
<p>I am looking to important CT imaging directly from the scanner as it is obtained during an Interventional Radiology biopsy procedure. I cannot wait for it to be pushed to PACS, I need to grab the data as the DICOM files are obtained while scanning. How can I do this? We are using a Siemens CT scanner and also have a GE scanner available. Thanks</p>

---

## Post #2 by @pieper (2021-07-31 19:15 UTC)

<p>The details vary a lot based on the scanner, but generally if you have administrative rights you should be able configure Slicer to pull from the scanner using the Query/Retrieve feature of the DICOM module (using CFIND and CGET) or you can have the scanner push to Slicer as images arrive (CMOVE).  You need to find out all the IP addresses, ports, and AETITLES specific to your installation.  It will be important to get an expert from your local site.  Once you figure it all out it should work reliably.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#dicom-networking" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#dicom-networking</a></p>

---

## Post #3 by @lassoan (2021-07-31 23:38 UTC)

<p>We often experienced that hospital IT administrators were reluctant to add “research” computers to the “clinical” DICOM network. In these cases we ended up setting up DICOM file export to a shared network drive on the CT/MRI console, and the research computer (Slicer) got access to that shared folder. Automatic checking of a folder for new files can be implemented in a Python scripted module quite easily (as it is done in <a href="https://github.com/SlicerProstate/SliceTracker">SlicerTracker extension</a>).</p>
<p>If you need even more real-time connection, then you can use <a href="http://openigtlink.org/">OpenIGTLink</a> with some Siemens MRI scanners. It allows Slicer to get live cine-MRI slices as they are being acquired, and Slicer can even control the scan plane. This can be used for example for implementing visual tracking of a needle during insertion.</p>

---
