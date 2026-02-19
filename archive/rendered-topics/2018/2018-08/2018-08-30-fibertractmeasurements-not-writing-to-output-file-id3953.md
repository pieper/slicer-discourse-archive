---
topic_id: 3953
title: "Fibertractmeasurements Not Writing To Output File"
date: 2018-08-30
url: https://discourse.slicer.org/t/3953
---

# FiberTractMeasurements not writing to output file

**Topic ID**: 3953
**Date**: 2018-08-30
**URL**: https://discourse.slicer.org/t/fibertractmeasurements-not-writing-to-output-file/3953

---

## Post #1 by @Saba_Shahab (2018-08-30 16:04 UTC)

<p>Operating system:<br>
NAME=“Ubuntu”<br>
VERSION=“16.04.3 LTS (Xenial Xerus)”<br>
ID=ubuntu<br>
ID_LIKE=debian<br>
PRETTY_NAME=“Ubuntu 16.04.3 LTS”<br>
VERSION_ID=“16.04”</p>
<p>Slicer version:<br>
slicer nightly version (updated as of 2018-08-20)</p>
<p>Hi,</p>
<p>I’m running the following code - it runs through without error but it doesn’t write the output in the output file.</p>
<p><code>FiberTractMeasurements --outputfile $outputfolder/FiberMeasurements/$filename/$hemisphere --inputdirectory $outputfolder/AppendClusters/'OutliersPerSubject_'$filename/$hemisphere -i Fibers_File_Folder --separator Tab -f Column_Hierarchy</code></p>

---

## Post #2 by @Saba_Shahab (2018-08-30 16:25 UTC)

<p>I just realized that the script doesn’t work properly when the parent directory does not exist. I just created the parent directory and the code is running successfully. I think the code should be modified to either give an error message or create the directory if it does not exist.</p>

---

## Post #3 by @ihnorton (2018-09-04 19:56 UTC)

<aside class="quote no-group" data-username="Saba_Shahab" data-post="2" data-topic="3953" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/df705f/48.png" class="avatar"> Saba_Shahab:</div>
<blockquote>
<p>I just realized that the script doesn’t work properly when the parent directory does not exist. I just created the parent directory and the code is running successfully. I think the code should be modified to either give an error message or create the directory if it does not exist.</p>
</blockquote>
</aside>
<p>Fixed <a href="https://github.com/SlicerDMRI/SlicerDMRI/commit/c5bd757caef622c1d2e402e64473535a86b0b7c9">here</a>. From the next nightly version, it should raise an error.</p>
<p>I don’t think there is a good way to check/create intermediate paths before opening a file in the current C++ version we are using (<s>without adding a new library dependency</s> edit: actually I guess we could use vtksys, but the second point still applies), and in any case, doing so without warning might be unwelcome in some circumstances.</p>
<p>Thanks for the report.</p>

---
