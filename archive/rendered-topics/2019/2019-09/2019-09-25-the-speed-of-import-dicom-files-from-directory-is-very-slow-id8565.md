---
topic_id: 8565
title: "The Speed Of Import Dicom Files From Directory Is Very Slow"
date: 2019-09-25
url: https://discourse.slicer.org/t/8565
---

# The speed of import dicom files from directory is very slow. How to solve the problem?

**Topic ID**: 8565
**Date**: 2019-09-25
**URL**: https://discourse.slicer.org/t/the-speed-of-import-dicom-files-from-directory-is-very-slow-how-to-solve-the-problem/8565

---

## Post #1 by @Tangtangyinghuochong (2019-09-25 16:08 UTC)

<p>Hi Dear developers and users.</p>
<p>I am delineating the ROI（Tumor） in abdominal MRIs and then extract the radiomics features for further search.</p>
<p>When import dicom files from directory, I found the speed is very slow. And it spent a lot of time on “updating displayed fields”,which needs more than 2 hrs importing one patient MRI data.</p>
<p>How to solve the problem?</p>
<p>The screen print is below.<br>
Thanks!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d533d626b8951b35bf94f7bbb20ecb4eb7c296eb.png" data-download-href="/uploads/short-url/uq4L9bOCNtDN29nTrsVpfGEBfqb.png?dl=1" title="updating%20displayed%20fields" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d533d626b8951b35bf94f7bbb20ecb4eb7c296eb_2_690x387.png" alt="updating%20displayed%20fields" data-base62-sha1="uq4L9bOCNtDN29nTrsVpfGEBfqb" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d533d626b8951b35bf94f7bbb20ecb4eb7c296eb_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d533d626b8951b35bf94f7bbb20ecb4eb7c296eb_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d533d626b8951b35bf94f7bbb20ecb4eb7c296eb.png 2x" data-dominant-color="65676C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">updating%20displayed%20fields</span><span class="informations">1366×768 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-09-25 17:38 UTC)

<p>How many files do you have indexed in the database? You may find that updates are faster if you process one of few patients at a time.</p>
<p>I’m currently working on DICOM browser improvements. I’ll have a look at displayed fields update, probably it can be made faster.</p>

---

## Post #3 by @pieper (2019-09-25 18:54 UTC)

<p>It would be good to profile things - my sense is that the gui is being updated more than needed, but it could also be something in the database indexing.</p>

---

## Post #4 by @lassoan (2019-09-25 19:20 UTC)

<p>I have already found a couple of issues around indexing (for example, the file system watcher triggered very frequent database view updates) and already fixed them in my branch.</p>
<p>I may do some more profiling with a large DICOM data set before I send the pull request.</p>

---

## Post #5 by @Tangtangyinghuochong (2019-09-26 00:51 UTC)

<p>Thanks! I usually add 10 patients data into the database and the database now have more than 150 files.</p>

---

## Post #6 by @Tangtangyinghuochong (2019-09-26 00:52 UTC)

<p>Thanks！How to check？Or how to solve？</p>

---

## Post #7 by @lassoan (2019-09-26 01:07 UTC)

<p>Just wait 1-2 weeks until my updates get into the Slicer Preview Release.</p>

---
