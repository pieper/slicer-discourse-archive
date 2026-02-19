---
topic_id: 33325
title: "2 Questions As A Newbie"
date: 2023-12-10
url: https://discourse.slicer.org/t/33325
---

# 2 questions as a newbie

**Topic ID**: 33325
**Date**: 2023-12-10
**URL**: https://discourse.slicer.org/t/2-questions-as-a-newbie/33325

---

## Post #1 by @JamesM (2023-12-10 04:40 UTC)

<p>Hello. I am currently measuring the brain tumor volumes of multiple patients using 3D Slicer and have encountered some issues that I hope you can help me resolve. Thank you in advance for your assistance.</p>
<ol>
<li><strong>Patient Recognition in DICOM Database:</strong> When I load DICOM files for multiple patients into the DICOM database in 3D Slicer, the software seems to recognize them as a single patient with multiple MRI studies. How can I load each patient with their respective MRI data separately?</li>
<li><strong>Measuring Tumor Volumes for Multiple MRI Series:</strong> When measuring tumor volumes for two MRI series (e.g., the initial MRI and follow-up MRI for the same patient) and checking the volumes using segmentation statistics, do I need to perform these measurements one by one? For instance, measuring the tumor volume of the initial MRI, checking the volume, and then repeating the same process for the follow-up MRI. If I measure all volumes first and then check the statistics, I am only able to see the volume of the last MRI, and cannot review volumes for the prior MRIs. How can I address this issue?</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c0db0f457d42257a066324a97adec17b2c8c54d.png" data-download-href="/uploads/short-url/d8lg9KX0Fe9rLG3shgxXOPza1jL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c0db0f457d42257a066324a97adec17b2c8c54d_2_690x491.png" alt="image" data-base62-sha1="d8lg9KX0Fe9rLG3shgxXOPza1jL" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c0db0f457d42257a066324a97adec17b2c8c54d_2_690x491.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c0db0f457d42257a066324a97adec17b2c8c54d_2_1035x736.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c0db0f457d42257a066324a97adec17b2c8c54d.png 2x" data-dominant-color="E2ECF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1242×884 63.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-12-10 15:58 UTC)

<p>It looks like all your studies have been given the same patient name and ID, which is why they are all treated as the same patient.  You would need to revisit your anonymization procedure to, for example, assign pseudonym IDs for each patient.</p>
<p>For the tumor metrics, the first calculation creates a table and this is re-used unless you create a new one.  One option is to create new tables for each calculation or you can copy-paste the results from the table into a spreadsheet or other document to track.  Or you could write some small python scripts to help work through a large number of studies and organize the results.</p>

---

## Post #3 by @JamesM (2023-12-11 11:44 UTC)

<p>Thank you for your help.<br>
Some point, I don’t understand…<br>
could you tell me more?</p>
<ol>
<li>Is the anonymization occurring during the process of downloading DICOM files?<br>
Because, I downloaded all the dicom data from different patients.</li>
<li>The main point of my question is whether it’s possible to measure tumor volumes in a continuous manner across multiple MRIs first and then obtain statistical values collectively.</li>
</ol>
<p>ThankS!</p>

---

## Post #4 by @pieper (2023-12-11 16:31 UTC)

<aside class="quote no-group" data-username="JamesM" data-post="3" data-topic="33325">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/9fc29f/48.png" class="avatar"> JamesM:</div>
<blockquote>
<p>Is the anonymization occurring during the process of downloading DICOM files?<br>
Because, I downloaded all the dicom data from different patients.</p>
</blockquote>
</aside>
<p>Yes, your anonymization process is assigning the same IDs to all patients.  It should assign different names to different patients.</p>
<aside class="quote no-group" data-username="JamesM" data-post="3" data-topic="33325">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/9fc29f/48.png" class="avatar"> JamesM:</div>
<blockquote>
<p>The main point of my question is whether it’s possible to measure tumor volumes in a continuous manner across multiple MRIs first and then obtain statistical values collectively.</p>
</blockquote>
</aside>
<p>It’s not clear to me what you mean by continuous.  You can segment each case one by one and record the statistics someplace like a spreadsheet or database.</p>

---
