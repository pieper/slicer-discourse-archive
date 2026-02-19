---
topic_id: 8141
title: "Slicer Application Settings User"
date: 2019-08-23
url: https://discourse.slicer.org/t/8141
---

# Slicer Application Settings: User

**Topic ID**: 8141
**Date**: 2019-08-23
**URL**: https://discourse.slicer.org/t/slicer-application-settings-user/8141

---

## Post #1 by @RayCui (2019-08-23 01:37 UTC)

<p>I found that there are user settings in the Application Settings of Slicer, which can record Name, Login, Email, Organization, etc. How can these user information be used? Will the user information be saved to a file when saving the data? No instructions were found in the user manual of the community. In addition, I found that these user settings do not seem to be mandatory, and will not be reminded to restart after the settings.<br>
Can anyone give me some information? Thank you.</p>

---

## Post #2 by @lassoan (2019-08-23 03:29 UTC)

<aside class="quote no-group" data-username="RayCui" data-post="1" data-topic="8141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/raycui/48/4517_2.png" class="avatar"> RayCui:</div>
<blockquote>
<p>I found that there are user settings in the Application Settings of Slicer, which can record Name, Login, Email, Organization, etc. How can these user information be used?</p>
</blockquote>
</aside>
<p>User information is not used by Slicer core, only by certain extensions, such as Quantitative Reporting (to record who performed certain operations and record it in the exported DICOM structured report.</p>
<p>You can access the information like this: <code>slicer.app.applicationLogic().GetUserInformation()</code>.</p>

---

## Post #3 by @RayCui (2019-08-23 08:36 UTC)

<p>Thanks for your reply, what should I do if I want to save the user information to the Annotation module’s save data file(such as *.acsv) and Segmentation data(such as *.seg.nrrd)? Should I modify the code of the slicer core(the part of save data)? Or use the Quantitative Reporting Extension feature that you mentioned to save user information? Do you have any suggestions?</p>
<p>In addition, I installed the Quantitative Reporting extension, but found that nothing happens when I click the “Retrieve and lost data” button.</p>

---

## Post #4 by @lassoan (2019-08-23 16:35 UTC)

<aside class="quote no-group" data-username="RayCui" data-post="3" data-topic="8141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/raycui/48/4517_2.png" class="avatar"> RayCui:</div>
<blockquote>
<p>Thanks for your reply, what should I do if I want to save the user information to the Annotation module’s save data file(such as *.acsv) and Segmentation data(such as *.seg.nrrd)?</p>
</blockquote>
</aside>
<p>You can save information to the name or description of points in .acsv file and custom segment tags in .seg.nrrd file.</p>
<aside class="quote no-group" data-username="RayCui" data-post="3" data-topic="8141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/raycui/48/4517_2.png" class="avatar"> RayCui:</div>
<blockquote>
<p>Should I modify the code of the slicer core(the part of save data)?</p>
</blockquote>
</aside>
<p>No Slicer core changes are needed. You can create a module that adds an observer to each loaded annotation / segmentation node and updates point description / adds custom segment tag that contains user information. You can also save the information in the scene (.mrml file) or additional text file if user information does not need to be saved inside the annotation/segmentation files.</p>

---

## Post #5 by @RayCui (2019-08-29 01:34 UTC)

<p>Thank you, Lassoan.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="8141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can access the information like this: <code>slicer.app.applicationLogic().GetUserInformation()</code> .</p>
</blockquote>
</aside>
<p>I think this suggestion really helped me. But now I want to get user information from loadable module, what should I do? Can you give me some examples, such as Quantitative Reporting for python.</p>

---

## Post #6 by @lassoan (2019-08-29 01:47 UTC)

<p>Search for <code>applicationLogic</code> in Slicer source code to see how it can accessed from various parts of a module.</p>

---
