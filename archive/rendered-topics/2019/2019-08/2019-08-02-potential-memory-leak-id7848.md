---
topic_id: 7848
title: "Potential Memory Leak"
date: 2019-08-02
url: https://discourse.slicer.org/t/7848
---

# Potential memory leak

**Topic ID**: 7848
**Date**: 2019-08-02
**URL**: https://discourse.slicer.org/t/potential-memory-leak/7848

---

## Post #1 by @GiulioBen (2019-08-02 13:32 UTC)

<p>Dear community, thank you all for this nice piece of software!!</p>
<p>I’m using it with dicom images.</p>
<p>However I noticed a sort of bug:<br>
After opening a couple of images (multislice MR), even though I close the scene, I find the slicer process being using a lot of RAM.<br>
Here you are a screen.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e93194f0ca20022cc545b69830c8598d9487c27.png" data-download-href="/uploads/short-url/mCOB5ru8XWSunqGbCoXZUq2pzkH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e93194f0ca20022cc545b69830c8598d9487c27.png" alt="image" data-base62-sha1="mCOB5ru8XWSunqGbCoXZUq2pzkH" width="690" height="391" data-dominant-color="ECECED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">801×454 31.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Furthermore, when I close the program it seems like a destructor has not been invoked.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60de56b4aa9724a57f141285793513568a937d6b.png" alt="image" data-base62-sha1="dOWc7Xo8gXTlcCTitpoI4T23cp5" width="372" height="159"></p>
<p>I’m using the latest nightly version!</p>
<p>Best regards</p>

---

## Post #2 by @pieper (2019-08-02 13:47 UTC)

<p>Thanks for the report - yes, we’d like to fix that.</p>
<p>Can you provide the exact steps to reproduce? (ideally using Slicer SampleData or some data you can share).</p>

---

## Post #3 by @lassoan (2019-08-02 14:11 UTC)

<p>Working set is the size of memory pages recently used by the application. If the application releases memory, working set size may remain the same until the memory is needed for another process. So, this may be normal. If memory usage keep increasing when you repeatedly load a data and close the scene (e.g., working set is 2GB then 3GB, 4GB, 5GB, …) then that may indicate that there is a memory leak.</p>

---

## Post #4 by @pieper (2019-08-02 14:32 UTC)

<p>But the unfreed collections should not happen, so we should track down how to reproduce that.</p>

---

## Post #5 by @GiulioBen (2019-08-04 09:00 UTC)

<p>Dear all, thank you for your support.<br>
Indeed, as you told, in my windows PC the unfreed RAM is reallocated when needed automatically.</p>
<p>NB: During the weekend I have only a Macbook Mojave to work, so I’ll post the steps to reproduce the error on monday. However I noticed that opening the same images on Slicer for MacOS the required RAM is much less (less than 1GB…). Could this be normal?</p>
<p>At the moment I can post a RT structure which is causing a slicer crash on MacOS. Probably it’s something similar to the problem found on Windows 7 but here the process closes.</p>
<p><a href="https://www.dropbox.com/sh/isk9pv2422zxd0s/AABwBwFVrpyYFNT1OcFZNKgBa?dl=0" rel="nofollow noopener">Here you can find the RT file and the crash log.</a></p>
<ol>
<li>I load it on the DCM database.</li>
<li>Select the node and load it</li>
</ol>
<p>nothing more.</p>
<p>Thank you!!</p>

---

## Post #6 by @GiulioBen (2019-08-05 13:08 UTC)

<p>Here I am.</p>
<p>Windows 7 Ultimate, SP1.</p>
<p>Nightly build 4.11.0-2019-07-10 r28371</p>
<ol>
<li>Download the <a href="http://wiki.slicer.org/slicerWiki/images/c/c2/DCE_series.zip" rel="noopener nofollow ugc">DICOM zip file</a>  from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/MultiVolumeExplorer" rel="noopener nofollow ugc">MultiVolumeExplorer documentation page</a>.</li>
<li>Load it on the DICOM browser (It took to me more than 15 mins to load on the database…i’m not sure it’s normal…) and import it as “MultiVolume by TriggerTime”</li>
<li>Open the MultiVolumeExplorer plugin and set the <em>input multivolume</em> to the sample data and the <em>input secondary volume</em> to None.</li>
<li>Select a frame (E.g. frame 20) and click <em>Copy frame</em></li>
<li>Quit the program without saving.</li>
</ol>
<p>Here you are the problem.</p>
<p>I worked for 1h importing and copying frames, converting them into nrrd and saving them. At the end, I had tons of errors. I report here a couple of messages (not all)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a6edb80b80e93bed4470fd314caa7b4d7a5c8db.png" alt="error" data-base62-sha1="8kVcF6eFpXPONEkqa5nTbPDKSBJ" width="485" height="304"></p>
<p>Thank you for the help!!</p>

---

## Post #7 by @lassoan (2019-08-05 15:18 UTC)

<p>You can safely ignore memory leak warnings at application exit. They are for developers only. I think they should not be displayed in releases that you download. Have you built Slicer yourself?</p>
<p>What would you like to achieve? Is your only problem that memory leaks are reported when you shut down the application?</p>

---

## Post #8 by @GiulioBen (2019-08-05 17:02 UTC)

<p>I’ve downloaded the execuitable installer which should be compiled every night. I’ve changed nothing.<br>
If you say it’s not a problem, for me it’s fine. It’s only a bit strange to have a page-long list of errors when you close the program. That’s why I made this post.</p>
<p>However I still have the crash problem I reported a couple o posts ago.</p>
<p>Best regards.</p>

---

## Post #9 by @jamesobutler (2019-08-05 17:09 UTC)

<p><a class="mention" href="/u/giulioben">@GiulioBen</a> Could you try downloading today’s Slicer preview release from <a href="https://download.slicer.org/" rel="nofollow noopener">https://download.slicer.org/</a> and let us know if you have the same issue of the memory leak warnings?</p>
<p>Those memory leak warnings displays are on by default when you manually build Slicer nightly. Maybe someone built Slicer manually, packaged it and then you installed it from that and not from the Slicer website.</p>

---

## Post #10 by @lassoan (2019-08-06 00:46 UTC)

<aside class="quote no-group" data-username="GiulioBen" data-post="8" data-topic="7848">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giulioben/48/4317_2.png" class="avatar"> GiulioBen:</div>
<blockquote>
<p>If you say it’s not a problem, for me it’s fine. It’s only a bit strange to have a page-long list of errors when you close the program.</p>
</blockquote>
</aside>
<p>It’s definitely a problem if it happens for the Stable Release. By default, we should probably not run memory leak check on Preview Releases either (if we do it now then we should probably change the build scripts), as this is debug information only intended for developers.</p>
<aside class="quote no-group" data-username="GiulioBen" data-post="8" data-topic="7848">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giulioben/48/4317_2.png" class="avatar"> GiulioBen:</div>
<blockquote>
<p>However I still have the crash problem I reported a couple o posts ago.</p>
</blockquote>
</aside>
<p>Importing that RTSTRUCT crashes Slicer, because it is invalid: number of values in <a href="https://dicom.innolitics.com/ciods/rt-dose/roi-contour/30060039/30060040/30060050">contour data</a> must be 3 x <a href="https://dicom.innolitics.com/ciods/rt-dose/roi-contour/30060039/30060040/30060046">number of contour points</a>, but in the file there are only 1 x number of contour points.</p>
<p>We’ve tested SlicerRT DICOM importer on thousands of data sets but never encountered such error, that’s why we did not notice that this can crash the application. Now I’ve added an extra check to avoid crash in the future and report this as an error.</p>
<p>Let developers of the software that created this RTSTRUCT file know that they produce non-compliant DICOM files. The incorrectly set “number of contour points” is just one of the many issues in the file (for example, usage of coded entries are completely misinterpreted by the developers).</p>

---

## Post #11 by @GiulioBen (2019-08-07 12:27 UTC)

<p>Thank you all. I downloaded and installed the last version of the nightly slicer and the same error message appears.</p>
<p>Anyway, if it’s just a debugging tool and a normal user can ignore it, i think we can close this post.</p>
<p>Thank you very much for the support!!</p>

---

## Post #12 by @cpinter (2019-08-07 13:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="7848">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve added an extra check to avoid crash in the future and report this as an error.</p>
</blockquote>
</aside>
<p>Thank you, Andras! .</p>

---

## Post #13 by @jamesobutler (2019-08-24 18:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="7848">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>By default, we should probably not run memory leak check on Preview Releases either (if we do it now then we should probably change the build scripts), as this is debug information only intended for developers.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I came back to this thread to test if memory leaks are displayed using preview releases built by the factory machines and indeed they are displayed.</p>
<p>Using “3D Slicer 4.11.0-2019-08-22” downloaded from Slicer’s website and creating a leak such as <code>a=slicer.mrmlScene.CreateNodeByClass("vtkMRMLScalarVolumeNode")</code> in the python interactor and then closing Slicer, I received a vtk debug leaks output window. This was tested using a Windows 7 machine which the original poster was also using.</p>
<p>Does anyone know if testing of preview releases is using memory leaks output to determine faults? As in will a memory leak introduced during a specific test cause that test to fail if on Slicer close there are memory leaks?</p>

---
