# How to create Markups Point List template with GUI

**Topic ID**: 20870
**Date**: 2021-12-01
**URL**: https://discourse.slicer.org/t/how-to-create-markups-point-list-template-with-gui/20870

---

## Post #1 by @jamesobutler (2021-12-01 20:55 UTC)

<p>How do I create a Markups Point List template using the Slicer GUI? For the template, I want it to be a template where there are templated control point names, but no coordinate positions yet defined. Is there a way to add control points to a Markups Point List using the Slicer GUI? I seem to only be able to place points randomly in the slice views and then clear all of their positions which wasn’t intuitive at first.</p>
<p>A Markups Point List template would look like the following where there are control points, but not coordinate positions yet defined for them.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/236bb708b28f91cd96563f69962eb5358a06b9d6.png" alt="image" data-base62-sha1="53lumynUDMA1AdQJoQ8AEgYNBJA" width="493" height="286"></p>

---

## Post #2 by @smrolfe (2021-12-01 21:38 UTC)

<p>Under the control points advanced options, there is a button to add an unplaced point. Previously, it was supposed to add a point at the origin, but it had been broken for a while. It’s not very easy to find, maybe it should be moved to the main control points menu?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/8798f10bd6d2f5a24e161c5f95d3e4f3e6f4942c.png" data-download-href="/uploads/short-url/jly8krcT5GlmjHANPdjXNQD5ERK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/8798f10bd6d2f5a24e161c5f95d3e4f3e6f4942c_2_434x500.png" alt="image" data-base62-sha1="jly8krcT5GlmjHANPdjXNQD5ERK" width="434" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/8798f10bd6d2f5a24e161c5f95d3e4f3e6f4942c_2_434x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/8798f10bd6d2f5a24e161c5f95d3e4f3e6f4942c_2_651x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/8798f10bd6d2f5a24e161c5f95d3e4f3e6f4942c_2_868x1000.png 2x" data-dominant-color="E7E9ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1134×1304 95 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @smrolfe (2021-12-01 21:54 UTC)

<p>I also made a <a href="https://www.youtube.com/watch?v=m-z9vNRIhxg" rel="noopener nofollow ugc">short video</a> showing the steps to create a template with the GUI.</p>

---

## Post #4 by @jamesobutler (2021-12-01 22:13 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="2" data-topic="20870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>Previously, it was supposed to add a point at the origin, but it had been broken for a while.</p>
</blockquote>
</aside>
<p>So is this tool tip out-of-date? Or is it supposed to add a point to the origin?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f1c3a360f1235ae0efd3de36016742b8b9d70e7.png" alt="image" data-base62-sha1="i8t7axzE8QUTsU8CZ4H6aA4KMm3" width="490" height="137"></p>
<aside class="quote no-group" data-username="smrolfe" data-post="2" data-topic="20870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>It’s not very easy to find, maybe it should be moved to the main control points menu?</p>
</blockquote>
</aside>
<p>I did not look there in the advanced section because I figured if there is a button to Delete a control point, then there would surely be the opposite button available nearby to add a new control point. I would have expected it to be one of the first buttons in the list of buttons above the control point table.</p>

---

## Post #5 by @smrolfe (2021-12-01 22:23 UTC)

<p>Thanks, the tooltip should be updated to read “Add a new control point with undefined position”. The button placement was carried over from the earlier version that placed a point at the origin. Given the new use case for templating I think it makes sense to move it near the delete control point button.</p>

---

## Post #6 by @jamesobutler (2021-12-06 00:31 UTC)

<p>I’ve been brainstorming designs of “Add” buttons for the control point table to go along side the delete buttons. The place button would add a point and go into editing mode. The menu option for this button would support the advanced case of adding an undefined point to the table. This seems to make more logical sense to me then, having it in an advanced section below the control point table. The Delete button would delete the highlighted control points, while the menu option for this button would support the advanced case of deleting all points in the table.</p>
<p>The “More Organization” brainstorming of options was done to reorganize to allow the “Add” and “Delete” to be the primary buttons to interact with the table and therefore would be the largest in size.</p>
<p>Thoughts on which version is liked here?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c39bedd3161c15b4b895985c430ccb6ed3aef98.png" data-download-href="/uploads/short-url/1K9rPJCTAnlLB5vp6ZqPcQiaeLK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c39bedd3161c15b4b895985c430ccb6ed3aef98_2_690x161.png" alt="image" data-base62-sha1="1K9rPJCTAnlLB5vp6ZqPcQiaeLK" width="690" height="161" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c39bedd3161c15b4b895985c430ccb6ed3aef98_2_690x161.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c39bedd3161c15b4b895985c430ccb6ed3aef98_2_1035x241.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0c39bedd3161c15b4b895985c430ccb6ed3aef98_2_1380x322.png 2x" data-dominant-color="F2F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1577×370 48.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2021-12-06 18:37 UTC)

<p>I personally liked the third one. It provides a verbal explanation of what most of the icons are (particularly the new functionality ones), and doesn’t look too cluttered.</p>

---

## Post #8 by @smrolfe (2021-12-06 20:15 UTC)

<p>I also like the “more organization” version, the layout seems more intuitive.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="20870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The place button would add a point and go into editing mode.</p>
</blockquote>
</aside>
<p>I can see a benefit for consistency, but entering placement mode would be less efficient if the goal is just to create a list of named, uninitialized points.</p>
<p>Sequential, group edit for highlighted points isn’t currently supported, but I think would be a nice addition.</p>

---

## Post #9 by @jamesobutler (2021-12-06 20:21 UTC)

<p>Creating a list of named, uninitialized points would utilize an advanced option in the menu of the “Add” button as a replacement to the button that has been in the “Advanced” section below the control point table. Is clicking into the menu of the “Add” button too cumbersome for this advanced task?</p>

---

## Post #10 by @smrolfe (2021-12-06 21:10 UTC)

<p>It could be tedious if you need to expand the menu each time and are placing a large number of points. I’m not sure if it’s possible to keep the menu visible after expanding? Navigating to the advanced menu is inconvenient, but only needs to be done once.</p>
<p>Given that there are two other, easily accessible GUI options for entering placement mode, I would suggest making this button more convenient for the templating use case.</p>

---

## Post #11 by @jamesobutler (2021-12-06 22:10 UTC)

<p>For creating templates are you adding one point, changing the name, adding another point, etc? Or is the number of points already known to support something like “Add 20 undefined points” where you can enter a number?</p>

---

## Post #12 by @smrolfe (2021-12-06 22:33 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="11" data-topic="20870">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Or is the number of points already known to support something like “Add 20 undefined points” where you can enter a number?</p>
</blockquote>
</aside>
<p>The number of points is known in advance, so something like this would work well.</p>

---

## Post #13 by @lassoan (2021-12-10 20:17 UTC)

<p>For filtering and search, please use the same UI as for the segment list (can be enabled by right-clicking on the segment list and choose “Show filter bar”):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/970e3ae3617ec7fe6edf43bf19ebbfaa63bc12c1.png" data-download-href="/uploads/short-url/lyiAjAs31GtHJupmMsYEX5gJ87T.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970e3ae3617ec7fe6edf43bf19ebbfaa63bc12c1_2_690x419.png" alt="image" data-base62-sha1="lyiAjAs31GtHJupmMsYEX5gJ87T" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/970e3ae3617ec7fe6edf43bf19ebbfaa63bc12c1_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/970e3ae3617ec7fe6edf43bf19ebbfaa63bc12c1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/970e3ae3617ec7fe6edf43bf19ebbfaa63bc12c1.png 2x" data-dominant-color="DCE1E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">924×562 47.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It should be a feature of the control point list widget, which should be created by factoring out the control point list into a new reusable widget. It would be similar to the qSlicerSimpleMarkupsWidget; probably the qSlicerSimpleMarkupsWidget should use this new control point list widget.</p>

---

## Post #14 by @jcfr (2022-02-15 19:56 UTC)

<p>Looking into using the template capabilities, I was wondering if updating one of these pages would make sense:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html">https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html">https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html</a></li>
</ul>
<p>Currently the only reference to the word “template” is in the <code>Definition of columns:</code>  associate with the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-control-points-table-file-format-csv-tsv"> Markups control points table file format (.csv, .tsv)</a> section.</p>
<p>It would be helpful to provide a bit more guidance.</p>
<p>Is there any text in this thread that could be added to the documentation ?</p>

---

## Post #15 by @jamesobutler (2022-02-15 20:00 UTC)

<p>All the templating and edit/restore/skip/clear states for control points will need to be updated in the documentation as well with the new Markups toolbar. These updates were primarily led by <a class="mention" href="/u/smrolfe">@smrolfe</a>’s group. Will need updated documentation for this work which is being captured by <a href="https://github.com/Slicer/Slicer/issues/5916" class="inline-onebox" rel="noopener nofollow ugc">Markups: Documentation of Markups module has not been updated to reflect latest changes · Issue #5916 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #16 by @smrolfe (2022-02-15 20:20 UTC)

<p>Now that the updates are stable, I can help update the documentation. I’m also planning to redo the template/Markups toolbar YouTube videos since there have been some changes to the interface.</p>

---
