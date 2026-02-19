---
topic_id: 15538
title: "Creating Teaching Overlays"
date: 2021-01-15
url: https://discourse.slicer.org/t/15538
---

# Creating teaching overlays

**Topic ID**: 15538
**Date**: 2021-01-15
**URL**: https://discourse.slicer.org/t/creating-teaching-overlays/15538

---

## Post #1 by @arumiat (2021-01-15 11:47 UTC)

<p>I saw this very nice resource that, as you scroll through images, shows overlays to demonstrate anatomy / pathology etc.</p>
<p><a href="/uploads/short-url/lW1CjdSxLaZolr9qsfeOILrxyAG.gif">labelling|1x1</a></p>
<p>I’m curious, is there a way to do this in Slicer?</p>
<p>And if not, would it be a matter of editing the underlying images in a program like photoshop to add the annotations, and then somehow saving as .dcm images, &amp; loading them in Slicer?</p>

---

## Post #2 by @cpinter (2021-01-15 11:48 UTC)

<p>I do not see the resource you are mentioning. Can you please give a link?</p>

---

## Post #3 by @arumiat (2021-01-15 11:54 UTC)

<p>Odd, trying to add a gif, here is as a link <a href="https://gifyu.com/image/FiTG" class="inline-onebox" rel="noopener nofollow ugc">labelling - Gifyu</a></p>

---

## Post #4 by @cpinter (2021-01-15 11:57 UTC)

<p>Thanks! I think the Markups fiducials feature could be potentially used for this purpose: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html" class="inline-onebox">Markups — 3D Slicer documentation</a> (see <code>F-1</code> etc instead of which you can have any label you want)</p>

---

## Post #5 by @arumiat (2021-01-15 12:01 UTC)

<p>That’s great <a class="mention" href="/u/cpinter">@cpinter</a> thank you.</p>
<p>And if I wanted to modify the underlying data so that the annotations ‘travel with’ the imaging study, would my approach of editing in an image editor the relevant images &amp; combining back into a stack work do you think?</p>

---

## Post #6 by @cpinter (2021-01-15 14:52 UTC)

<p>You mean “burning in” the annotations into the DICOM image? I’m sure it is possible but we don’t have tools doing that and also I wouldn’t recommend it.</p>
<p>If you want to have annotated images in a DICOM database I think you have two better options than that:</p>
<ul>
<li>Use the <a href="https://qiicr.gitbook.io/quantitativereporting-guide/">Quantitative Reporting extension</a> to export a standard DICOM Structured Reporting (SR) object in your DICOM database. The advantage of this is that it is 100% DICOM compliant, but I’m not sure about the current state of the extension nor whether it supports the necessary use case. <a class="mention" href="/u/fedorov">@fedorov</a> can you please give a heads up whether QR can export a DICOM-SR containing labelled points in an easy way?</li>
<li>Export the entire Slicer scene into a secondary capture. The advantage is that you can load your annotated data the very same way into Slicer as you exported, and you can store the whole thing in your usual DICOM database. The downside is that only Slicer will be able to open it.</li>
</ul>
<p>Not sure if I was able to help.</p>

---

## Post #7 by @fedorov (2021-01-15 22:19 UTC)

<p>I would think screen recording and export combined with Markups and some customs scripting should be the best approach for this task. There was some module or capability to record sections of Slicer application in the past, but it was a while ago, and I have not used it myself, so I do not have all the details.</p>

---

## Post #8 by @lassoan (2021-01-15 23:45 UTC)

<p>I would suggest to use a 3D viewer with slice and 3D views.</p>
<p>Slicer would be the obvious choice. It is free and it should not take more than 10 minutes to download and install. You can create “scene views” - predefined annotated views with predefined layouts and node visibility.</p>
<p>If installing a desktop application is absolutely impossible for your students then you can use web viewers, such as the <a href="https://www.openanatomy.org/atlas-pages/">OpenAnatomy viewer</a>. You can embed such web viewers into your training webpages. All the atlases that you see there were exported from Slicer using some scripts. We are working on making this export fully automatic, but if you want to do it now then <a class="mention" href="/u/mhalle">@mhalle</a> should be able to give more information.</p>

---

## Post #9 by @arumiat (2021-01-19 18:27 UTC)

<p>Thank you very much all :).</p>
<p>We were thinking about playing the studies in our own medical imaging viewer based on OHIF so the Slicer approach isn’t ideal. But you have given us plenty to think about! Appreciate it.</p>

---

## Post #10 by @lassoan (2021-01-19 18:30 UTC)

<aside class="quote no-group" data-username="arumiat" data-post="9" data-topic="15538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f05b48/48.png" class="avatar"> arumiat:</div>
<blockquote>
<p>We were thinking about playing the studies in our own medical imaging viewer based on OHIF so the Slicer approach isn’t ideal.</p>
</blockquote>
</aside>
<p>Did you mean “the Slicer approach <strong>is</strong> ideal”? Because it is (or at least it is pretty good). In Slicer, you can export the segmentation to DICOM segmentation object and load it into OHIF viewer right away! You can even directly upload the DICOM segmentation object to the DICOMweb server (that the OHIF viewer uses) directly from Slicer. It all works really well.</p>

---

## Post #11 by @arumiat (2021-01-20 10:59 UTC)

<p>Oh how cool! I will definitely take another look at this then. Thanks!</p>

---
