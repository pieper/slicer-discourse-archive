---
topic_id: 8244
title: "Markups Angles Numerical Output"
date: 2019-08-30
url: https://discourse.slicer.org/t/8244
---

# Markups Angles - Numerical Output

**Topic ID**: 8244
**Date**: 2019-08-30
**URL**: https://discourse.slicer.org/t/markups-angles-numerical-output/8244

---

## Post #1 by @ramenegaz (2019-08-30 22:42 UTC)

<p>I am trying to measure an angle using the Markups tool. In the markups list, I have a series of three 3D points anchoring the angle but no output for the actual angle (in degrees). Where is the angle measurement saved?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b2b62b23ddfc30f12447c93448f2ada31d4b3a7.jpeg" data-download-href="/uploads/short-url/m8GXA3IG1fVcbBPgFza4Es48UpV.jpeg?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b2b62b23ddfc30f12447c93448f2ada31d4b3a7_2_690x332.jpeg" alt="screenshot" data-base62-sha1="m8GXA3IG1fVcbBPgFza4Es48UpV" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b2b62b23ddfc30f12447c93448f2ada31d4b3a7_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b2b62b23ddfc30f12447c93448f2ada31d4b3a7_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b2b62b23ddfc30f12447c93448f2ada31d4b3a7_2_1380x664.jpeg 2x" data-dominant-color="9A9AA9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">1920×924 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer version 4.11.10-2019-08-22</p>

---

## Post #2 by @lassoan (2019-09-01 03:13 UTC)

<p>Markups measurements (length, angle, area, etc.) are still work in progress. Currently angle is only displayed in 3D view but not saved anywhere. We plan to add a measurement section to Markups module GUI where all measurements for the selected markup would be displayed. We could also show selected measurements in a tree (similarly to the Data module, but with an extra column added for displaying one or a few values).</p>
<p>How many angles would you measure in a scene? How many cases do you plan to measure? How do you plan to use the angle values? Copy each value to Excel? Or go through a number of cases with CaseIterator extension to add a few angle markups to each case; then extract all the angle values using a Python script?</p>

---

## Post #3 by @timeanddoctor (2019-09-01 03:36 UTC)

<p>Actionly, you can compurter the angle by simple geomatric math with 3 points(RAS).</p>

---

## Post #5 by @smrolfe (2019-09-11 20:03 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, our group is also interested in saving a list of angle measurements. It would be great to be able to do this from the Markups module. Is there a plan for when this may be available? If it will be a while we may look into a temporary solution.</p>
<p>Thanks for your advice.</p>

---

## Post #6 by @lassoan (2019-09-12 14:55 UTC)

<p>I plan to replace the node selector combobox in Markups module with a subject hierarchy tree view (filtered to only show markups nodes). The tree view can show some measurement results (1-2 values) in a column. This is what I have now (everything works except measurement values are not yet written to the extra column, I just typed those there manually):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ae654c287142396d2ca8989dd0ff44fae7bf538.png" data-download-href="/uploads/short-url/ffG5Pb3ylpqLKYT4upXTcuawlTO.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ae654c287142396d2ca8989dd0ff44fae7bf538_2_365x500.png" alt="image" data-base62-sha1="ffG5Pb3ylpqLKYT4upXTcuawlTO" width="365" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6ae654c287142396d2ca8989dd0ff44fae7bf538_2_365x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ae654c287142396d2ca8989dd0ff44fae7bf538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6ae654c287142396d2ca8989dd0ff44fae7bf538.png 2x" data-dominant-color="BDBDBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">437×598 28.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you think this would work for you?</p>
<p>How would you use the measurement results? Copy to clipboard (so that it can be pasted into Excel) Saved to the scene file? Saved to a table node? Exported to some json/xml/csv file (not managed by the scene)?</p>

---

## Post #7 by @muratmaga (2019-09-12 16:19 UTC)

<p>Andras this looks great. Is it available to try in the preview version so that we can give feedback after testing a bit? Eg, is the “New Folder” option equivalent of compiling in all individual measurements in a single place?</p>
<p>We don’t use the scene files a lot, and especially not for storing results. Being able to export them to a csv file is necessary (either to a table export first, or directly saving them). Can we reload a measurement table to recreate them in the scene? Or is strictly values (not the points that will be saved)</p>

---

## Post #8 by @lassoan (2019-09-12 18:18 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="8244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>is the “New Folder” option equivalent of compiling in all individual measurements in a single place?</p>
</blockquote>
</aside>
<p>I just added the folder to show that you can organize your data in subject hierarchy folders (same as in Data module). You can use the folders any way you want. <a class="mention" href="/u/cpinter">@cpinter</a> works on allowing folders to override display properties of all nodes within it (e.g., you can temporarily show/hide or override color of all markup nodes within a folder).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="8244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>We don’t use the scene files a lot, and especially not for storing results. Being able to export them to a csv file is necessary</p>
</blockquote>
</aside>
<p>Is there a good approach/format that you would be confident to recommend?</p>
<p>Exporting measurements to a table node would not be difficult. There could be an “export” section in markups module GUI to create a table node from selected measurements from all selected markups.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="8244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Can we reload a measurement table to recreate them in the scene? Or is strictly values (not the points that will be saved)</p>
</blockquote>
</aside>
<p>Tables would be regular table nodes, so you could load them again into the scene. However, maintaining two-way links robustly between some original data (e.g., point sets) and measurements on them would require UUIDs and cross-references. Instead of reinventing the wheel, it could make sense to use DICOM for this.</p>

---

## Post #9 by @muratmaga (2019-09-16 03:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Is there a version I can give it a try? Some of your questions are better answered after testing a few things.</p>

---

## Post #10 by @lassoan (2019-09-16 18:59 UTC)

<p>I work in this branch: <a href="https://github.com/lassoan/Slicer/tree/markups-module-node-selector-tree" rel="nofollow noopener">https://github.com/lassoan/Slicer/tree/markups-module-node-selector-tree</a>. You can build it to try it on your computer (or I can create a Windows install package if you cannot easily build Slicer).</p>
<p>I planned to spend a bit more time, maybe 1-2 days with testing and tuning before I commit it to the master branch.</p>

---

## Post #11 by @muratmaga (2019-09-16 19:34 UTC)

<p>We (or at least I) currently have a certificate issue with our corporate proxy that limits our ability to do stuff that requires https, including cloning repos. If you don’t mind sending me a windows install package that will be great, or I can wait a couple days for you to commit to the master and hope by that time certificate issue is resolved.</p>

---

## Post #12 by @lassoan (2019-09-17 22:35 UTC)

<p>I’ve committed the markups module GUI to the master branch. It should be available in tomorrow’s Preview Release.</p>

---
