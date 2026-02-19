---
topic_id: 36528
title: "Creating An Automated Pulmonary Vessel Quantitation System"
date: 2024-05-31
url: https://discourse.slicer.org/t/36528
---

# Creating an Automated Pulmonary Vessel Quantitation System

**Topic ID**: 36528
**Date**: 2024-05-31
**URL**: https://discourse.slicer.org/t/creating-an-automated-pulmonary-vessel-quantitation-system/36528

---

## Post #1 by @THartman (2024-05-31 20:14 UTC)

<p>The extension in its current state takes as an input a volume that has been processed to include two tones of vessel, where a 1 represents an artery and a 2 represents a vein.  With this being done, our extension is able to segment the vessels into each their own segment and then take advantage of the amazing tools provided by the Vascular Modelling ToolKit (VMTK) to automate the centerline extraction process.  This can be done as either the model or the table forms (or both), and will then go on to add additional information.</p>
<p>We are a small group of College students who started this project as a capstone project, but we have continued working to polish it into something that could be used for research purposes.  There are a couple of input buttons that currently don’t do anything (the default value for these is used).  This should be fixed in the next few days.  You can find our extension in its current version here: <a href="https://github.com/HartmanTA/Blood-Vessel-Image-Quantitation-System" rel="noopener nofollow ugc">https://github.com/HartmanTA/Blood-Vessel-Image-Quantitation-System</a></p>
<p>As for the direction of the project, we hope we can get it to the point where it will automatically export CSV data about the vessels for users to a file location provided by the user.  Currently, the default tables provided by VMTK are augmented with values including Horton-Strahler numbers and some other parent/child relationship information.</p>
<p>Does this seem like something that would be useful to anyone here?  Are there any feature recommendations?  Any insight would be useful on this front.</p>

---

## Post #2 by @Antoine1 (2024-06-06 14:18 UTC)

<p>Hello, I think your link doesn’t work for me</p>

---

## Post #3 by @THartman (2024-06-07 15:35 UTC)

<p>I fixed it.  I am going to ask the professor we have been working with about whether or not it’s cool for me to share the sample data, and if it is, I plan to add it to the repo.</p>

---
