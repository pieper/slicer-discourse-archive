# Data structure and organization for efficient project workflow

**Topic ID**: 1993
**Date**: 2018-01-31
**URL**: https://discourse.slicer.org/t/data-structure-and-organization-for-efficient-project-workflow/1993

---

## Post #1 by @djqazi (2018-01-31 20:39 UTC)

<p>Hi everyone, I posted earlier about a machine learning project, but it was recommended to create a new thread about each topic rather than a single stream-of-concsiousness type post <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=5" title=":sweat_smile:" class="emoji" alt=":sweat_smile:">. So I’d like to start from the begining: data.</p>
<p>Problem:<br>
As stated in the previous post, we have ~15,000 knee MRI studies in DICOM format. I’m working with a sample of 30 studies to play around with. Six months ago, when I was even more clueless than I am now, I took the time to manually go through these 30 studies and create a directory tree as follows:</p>
<div class="lazyYT" data-youtube-id="36zJaxgqYMw" data-youtube-title="20180131 144050" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>I chose to do it this way 6 months ago because I thought it would be valuable to be able to know which planes or sequences we are dealing with however I am not sure if there is any value to this directory structure given that I can simply drag and drop the entire “Patients” folder into Slicer and it (DICOM module) will automatically organize (by patient, study, series) the data for me. I had orginally imagined some type of recursive code (base case == terminal folder i.e. folder with no folders in it) to loop through all of the folders starting at the top of the tree (Patients) and extracting the indvidual slices from each sequence and aggregate them into their respective volumes and feed them as inputs intro training a deep network for segmentation/classification purposes.</p>
<p>Questions:<br>
Given Slicer’s DICOM module, is there any utility/purpose in organizing imaging data into an arbitrary directory sructure (such as the one I made)? Do I need structure at all or can I simply have all of my DICOM files in a single folder? Generalizing this question a bit, when organizing a machine learning project such as this using 3D Slicer, how important is data (DICOM specifically) organization? Again, although I am working with a sample of 30, these questions are in the context of 15,000 studies. The reason I ask if for automation/efficiency purposes i.e. scripting the import, conversion, registration, etc. in Slicer with Python.</p>
<p>I have more questions in this topic e.g. after importing DICOM files, visualizing issues, converesion to NRRD issues, etc., but I think this is a good start (literally where I started 6 months ago).  Thanks!</p>

---

## Post #2 by @pieper (2018-02-01 16:24 UTC)

<p>A few thoughts:</p>
<ul>
<li>
<p>Slicer’s DICOM module might technically work for 15,000 studies but it wouldn’t be optimal.  It’s probably good for experiments and also you might use it as part of processing scripts for converting to nrrd.  Converting the DICOM into a directory tree that is conveniently designed to give you quick access to the data in the formats you need for your experiments is probably still a good idea.  Then you can have custom scripts that work for that organization of the data.</p>
</li>
<li>
<p>For that much data you will need to think about storing both the original and derived data on some kind of archive that spans multiple disks and has good backup.  Presumably your institution provides a file sharing service like this and then you can treat it as one logical directory for all your data.</p>
</li>
<li>
<p>Probably the analysis of that much data will need to be done on a cluster of some kind, so you’ll want to be able to launch jobs and track results.  In the end that usually ends up being done with custom script wrapped around whatever job submission system your cluster uses.</p>
</li>
</ul>
<p>HTH,<br>
Steve</p>

---
