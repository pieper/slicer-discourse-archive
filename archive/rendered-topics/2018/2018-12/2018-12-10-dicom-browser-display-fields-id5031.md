---
topic_id: 5031
title: "Dicom Browser Display Fields"
date: 2018-12-10
url: https://discourse.slicer.org/t/5031
---

# DICOM browser display fields

**Topic ID**: 5031
**Date**: 2018-12-10
**URL**: https://discourse.slicer.org/t/dicom-browser-display-fields/5031

---

## Post #1 by @cpinter (2018-12-10 20:29 UTC)

<p>Hi core devs,</p>
<p>We have had this plan for several years now to customize the content of the fields that appear in the DICOM browser. We wanted to get rid of the ^ character in the patient name, show the time a patient/study/series was added, show number if images in a series, etc.</p>
<p>I created a branch during the 2014 CTK Hackfest in Kingston that never got integrated due to the different needs of the MITK and Slicer people. However I decided to resurrect that branch hoping that we can now change this part of CTK. Here is the rebased, merged, squashed, and fixed <a href="https://github.com/cpinter/CTK/tree/dicom-database-display-tables-3" rel="nofollow noopener">branch</a> that works with the latest Slicer and CTK.</p>
<p>In a nutshell, this is what it contains:</p>
<ul>
<li>For Patient, Study, Series tables there is a corresponging DisplayPatient, DisplayStudies, DisplaySeries table in the database that contain the fields we want to show in the DICOM browser</li>
<li>Plugins can generate fields from modality-specific data and user needs
<ul>
<li>A method calls the plugins to generate the display tables from regular tables when import ended</li>
</ul>
</li>
</ul>
<p>We talked to <a class="mention" href="/u/lassoan">@lassoan</a> about how we could continue from here, and this is what we think would be a good plan:</p>
<ul>
<li>Use the 3 tables (instead of 3+3), but add new columns for display fields (with prefix “Display”)
<ul>
<li>Easier synchronization on removal etc.</li>
</ul>
</li>
<li>New table for column properties
<ul>
<li>Table</li>
<li>FieldName</li>
<li>DisplayName</li>
<li>Order (-1 for not shown?)</li>
<li>Format (“last name, first name”, unit properties, etc. - rules can use these for generating displayed fields)</li>
<li>ViewID (in case there will be multiple property tables - can add later if needed)</li>
</ul>
</li>
<li>New columns
<ul>
<li>Number of slices for series (show number of files for simplicity)</li>
<li>Number of studies for patients</li>
<li>Insert timestamp for all three tables</li>
<li>Number of series for studies</li>
</ul>
</li>
<li>We need to still decide where the plugins would come from and how. Currently all plugins are C++ and are in CTK (that’s how I did it for easy implementation and testing), but we could use the DICOM plugins in Slicer to define these “rules”.</li>
</ul>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/nolden">@nolden</a></p>

---

## Post #2 by @fedorov (2018-12-11 15:28 UTC)

<p>These are great ideas to experiment with! Do you think there could be a way to develop this, at least initially, separately from CTK so it could be easier to prototype/iterate in Slicer nightlies (collect feedback from the users and developers, experiment with the plugins integration, UI customization etc) and later migrate into CTK? Or maybe we could build Slicer nightlies against your custom CTK branch for some time? I can definitely see how this potentially could be very useful, but it probably will take the time to refine the details.</p>

---

## Post #3 by @cpinter (2018-12-11 15:52 UTC)

<p>Yes this is a big change and we need to make sure it’s mature and accepted by everyone before making a change in CTK master. I think you’re right and probably the best way would be building Slicer against a CTK branch. All this after 4.10.1 of course.</p>

---

## Post #4 by @pieper (2018-12-11 19:16 UTC)

<p>Great to move ahead with this.  I like the idea of using the nightlies for experiments.  We are always free to fork CTK to meet our needs and even create a second variant widget in CTK if MITK still needs the existing structure to remain as-is.  <a class="mention" href="/u/nolden">@nolden</a> will be in Las Palmas so we can also go over options there as needed.</p>

---

## Post #5 by @nolden (2018-12-11 22:58 UTC)

<p>I’m very happy to see this initiative, and I can even remember the first discussions in Kingston. MITK is still using the current widget, but I’m sure we could manage any API changes and I assume all of our users would be very happy to see an update here, I’m not aware on anyone particulary dependent on the current look and feel.</p>
<p>I cannot promise anything, but I filed this for MITK (<a href="https://phabricator.mitk.org/T25745" rel="nofollow noopener">https://phabricator.mitk.org/T25745</a>) and think we can discuss a bit more latest at the Gran Canaria event. Thanks for your effort <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #6 by @cpinter (2018-12-13 19:34 UTC)

<p>FYI this is the current state</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4569d2a92af08a3a1394b95d1fab13c6038e67a8.png" data-download-href="/uploads/short-url/9U3Fxlulx483KS6q7E8eZ5IVtzy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4569d2a92af08a3a1394b95d1fab13c6038e67a8.png" alt="image" data-base62-sha1="9U3Fxlulx483KS6q7E8eZ5IVtzy" width="616" height="500" data-dominant-color="DFEBF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">981×796 21.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
