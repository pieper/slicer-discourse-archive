---
topic_id: 26694
title: "Bad Alloc Error In Slicerfreesurfer On 5 2 1 Linux"
date: 2022-12-12
url: https://discourse.slicer.org/t/26694
---

# bad_alloc error in slicerfreesurfer on 5.2.1 Linux

**Topic ID**: 26694
**Date**: 2022-12-12
**URL**: https://discourse.slicer.org/t/bad-alloc-error-in-slicerfreesurfer-on-5-2-1-linux/26694

---

## Post #1 by @kytk (2022-12-12 05:51 UTC)

<p>Hi, I have trouble using FreeSurfer Importer provided with the SlicerFreSurfer extension.</p>
<p>Problem: When I try to load segmentation, it cuases bad_alloc error. The error message is below.</p>
<blockquote>
<p>“Slicer has caught an application error, please save your work and restart.\n\nThe application has run out of memory. Increasing swap size in system settings or adding more RAM may fix this issue.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: std::bad_alloc”<br>
QXcbConnection: XCB error: 3 (BadWindow), sequence: 4707, resource id: 14695233, major code: 40 (TranslateCoords), minor code: 0</p>
</blockquote>
<ul>
<li>
<p>I can load Volumes (e.g. brainmask.mgz) and Models (e.g. lh.pial) without any problem. I cannot load only Segmentations.</p>
</li>
<li>
<p>This problem occurs only in Linux version of Slicer 5.x. I tried with both 5.0.3 and 5.2.1, and got the same error.</p>
</li>
<li>
<p>My workstation has 192GB RAM. Though the error message says it has run out of memory, but I feel that is not the problem.</p>
</li>
</ul>
<p>The result of free:</p>
<pre><code class="lang-auto">$ free -h
              total        used        free      shared  buff/cache   available
Mem:          187Gi        41Gi       138Gi       328Mi       8.3Gi       144Gi
Swap:         2.0Gi          0B       2.0Gi
</code></pre>
<p>I feel there may be a bug in loading segmentation in SlicerFreeSurfer. If you have any workarounds, please let me know.</p>
<p>My circumstance is the following;</p>
<p>$ cat /etc/lsb-release<br>
DISTRIB_ID=Ubuntu<br>
DISTRIB_RELEASE=20.04<br>
DISTRIB_CODENAME=focal<br>
DISTRIB_DESCRIPTION=“Ubuntu 20.04.5 LTS”</p>
<p>$ uname -a<br>
Linux ubuntu 5.15.0-56-generic #62~20.04.1-Ubuntu SMP Tue Nov 22 21:24:20 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux</p>

---

## Post #2 by @lassoan (2022-12-12 06:08 UTC)

<p>Thanks for reporting this.</p>
<p><code>QXcbConnection: XCB error: 3 (BadWindow)...</code> message is just a warning (seems to be a <a href="https://bugreports.qt.io/browse/QTBUG-56893">known Qt bug</a>). Probably it is not the root cause of the serious <code>std::bad_alloc</code> error, but the <code>QXcbConnection</code> error may be triggered by the display of the modal error popup.</p>
<p>The memory allocation may fail because of the segmentation file contains some unexpected/misinterpreted content, which makes Slicer want to allocate an enormous amount of memory.</p>
<p>Can you share a data set that you have problem with and instructions for reproducing the issue?</p>

---

## Post #3 by @kytk (2022-12-12 06:50 UTC)

<p>Thank you for the prompt reply.</p>
<p>I have this problem with even “bert” data shipped with FreeSurfer 7.3.2.<br>
(None of  aseg.mgz(s) cannot be loaded)</p>
<p>This is what I did.</p>
<ul>
<li>Copy bert to my home directory</li>
</ul>
<pre><code class="lang-auto">mkdir -p ~/freesurfer/7.3.2/subjects
cp -r $FRESURFER_HOME/subjects/bert ~/freesurfer/7.3.2/subjects
</code></pre>
<ul>
<li>
<p>Run Slicer</p>
</li>
<li>
<p>Modules → Utilities → FreSurferImporter</p>
<ul>
<li>FreeSurfer directory: ~/freesurfer/7.3.2/subjects/bert</li>
<li>Volumes: brainmask.mgz</li>
<li>Segmentation: aseg.mgz</li>
</ul>
</li>
<li>
<p>Click Load → Error</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d33237a2fe0df18844e5b116794603eda1d0486.png" data-download-href="/uploads/short-url/b0WkpbMyIq93Wprx9Cxdmg2VxUq.png?dl=1" title="slicer_setting" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d33237a2fe0df18844e5b116794603eda1d0486_2_331x500.png" alt="slicer_setting" data-base62-sha1="b0WkpbMyIq93Wprx9Cxdmg2VxUq" width="331" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d33237a2fe0df18844e5b116794603eda1d0486_2_331x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d33237a2fe0df18844e5b116794603eda1d0486_2_496x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d33237a2fe0df18844e5b116794603eda1d0486.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_setting</span><span class="informations">498×752 39.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>If I select only Volumes (brainmask.mgz) and Models (lh.pial), then it works fine.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65ddb8e8637ca76ea8651cdf6319b75ba9be4e33.png" data-download-href="/uploads/short-url/ex9ggrPqFbAKSukeaWa0piWVCQH.png?dl=1" title="slicer_wo_problem" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65ddb8e8637ca76ea8651cdf6319b75ba9be4e33_2_690x475.png" alt="slicer_wo_problem" data-base62-sha1="ex9ggrPqFbAKSukeaWa0piWVCQH" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65ddb8e8637ca76ea8651cdf6319b75ba9be4e33_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65ddb8e8637ca76ea8651cdf6319b75ba9be4e33_2_1035x712.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65ddb8e8637ca76ea8651cdf6319b75ba9be4e33.png 2x" data-dominant-color="9E9DA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_wo_problem</span><span class="informations">1107×763 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have no problems on Windows and macOS, so I feel something is wrong with Linux.</p>
<p>Thank you for your support!</p>
<p>Kiyotaka</p>

---

## Post #4 by @RafaelPalomar (2022-12-12 14:03 UTC)

<p>I have <strong>not</strong> been able to reproduce this issue using the steps above in<br>
the following setup:</p>
<ul>
<li>OS: Ubuntu 22.04</li>
<li>Slicer version: 5.3.0-2022-12-03 (self-built)</li>
<li>Slicer revision: 31346</li>
<li>SlicerFreeSurfer: master branch</li>
</ul>
<p><a class="mention" href="/u/kytk">@kytk</a>, you could give a try to the preview release (5.3.0) and see if it<br>
works. From all the changes you could do to approach a working<br>
environment, this is the easiest.</p>

---

## Post #5 by @kytk (2022-12-12 15:16 UTC)

<p>Thank you for checking. Now I know that something is wrong in my environment.<br>
Though the preview release resulted in the same error, I will try to build Slicer for my environment and see if it works.</p>

---

## Post #6 by @lassoan (2023-11-08 14:50 UTC)

<p>2 posts were split to a new topic: <a href="/t/error-loading-freesurfer-segmentation/32674">Error loading freesurfer segmentation</a></p>

---

## Post #7 by @Gabriel_St_Angel (2025-01-26 20:36 UTC)

<p>Chiming in late, but I am also getting this issue with 5.3.0 and Ubuntu 22.04.  I did not have this issue on Windows or Mac with the same dataset and Slicer Version.  It seems to throw the error specifically when loading Segmentations from FreeSurfer, I’m able to load Models and Volumes.  I have plenty of free ram and swap (32gb free memory)</p>
<pre><code class="lang-auto">"Slicer has caught an application error, please save your work and restart.\n\nThe application has run out of memory. Increasing swap size in system settings or adding more RAM may fix this issue.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at https://slicer.org\n\n\nThe message detail is:\n\nException thrown in event: std::bad_alloc"
ReferenceImageExtentOffset attribute was not found in NRRD segmentation file. Assume no offset.
</code></pre>

---

## Post #8 by @pieper (2025-01-26 22:11 UTC)

<p>Try the latest release and preview release (5.3.0 is old at this point).  Also, if the issue can be easily reproduced, please share data and exact steps that lead to the issue.</p>

---
