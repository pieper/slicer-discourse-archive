---
topic_id: 28173
title: "Organization Name And Domain Changed From Na Mic To Slicer"
date: 2023-03-04
url: https://discourse.slicer.org/t/28173
---

# Organization name and domain changed from NA-MIC to Slicer

**Topic ID**: 28173
**Date**: 2023-03-04
**URL**: https://discourse.slicer.org/t/organization-name-and-domain-changed-from-na-mic-to-slicer/28173

---

## Post #1 by @jamesobutler (2023-03-04 19:59 UTC)

<p>Following the discussion below, the 3D Slicer application has updated the <code>Slicer_ORGANIZATION_NAME</code> from “NA-MIC” to “Slicer” and <code>Slicer_ORGANIZATION_DOMAIN</code> from <code>www.na-mic.org</code> to <code>www.slicer.org</code>. At the time of this change, 3D Slicer is developed primarily by the Slicer community rather than the NA-MIC community. Distribution of 3D Slicer is hosted at <a href="https://www.slicer.org/" rel="noopener nofollow ugc">www.slicer.org</a> rather than at <a href="https://www.na-mic.org/" rel="noopener nofollow ugc">www.na-mic.org</a>.</p>
<aside class="quote quote-modified" data-post="1" data-topic="26547">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/inconsistency-between-organization-name-used-for-settings-files-and-for-macos-bundle-identifier/26547">Inconsistency between organization name used for settings files and for macOS bundle identifier</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    There are inconsistencies between the organization associated with the <a href="https://slicer.readthedocs.io/en/5.2/user_guide/settings.html#settings-file-location" rel="noopener nofollow ugc">settings file location</a> and the value set as macOS bundle identifier. 




Settings file location
macOS bundle identifier




[image]
[image]



These correspond to the default values associated with the following variables: 




CMake variable
Default value




Slicer_ORGANIZATION_NAME
NA-MIC<a href="#footnote-86990-1" id="footnote-ref-86990-1">[1]</a>


Slicer_ORGANIZATION_DOMAIN
www.na-mic.org <a href="#footnote-86990-2" id="footnote-ref-86990-2">[2]</a>


Slicer_MACOSX_BUNDLE_GUI_IDENTIFIER
org.slicer.slicer<a href="#footnote-86990-3" id="footnote-ref-86990-3">[3]</a>



Question: Should we up…
  </blockquote>
</aside>

<p>This change does not mark an end to the NA-MIC relationship with 3D Slicer, but this change improves consistency of the application to identify its latest releases as being developed and published by the Slicer community.</p>
<p>Slicer settings will now be under a Slicer directory location rather than NA-MIC. Please review the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location" rel="noopener nofollow ugc">Settings File Location documentation</a> for details about the settings location on various platforms.</p>
<ul>
<li>Developers, you may need to update any scripts that you may have that include a NA-MIC reference to a filepath.</li>
<li>Existing settings files in the NA-MIC location are not currently planned to be migrated over to the new location. See the <a href="https://github.com/Slicer/Slicer/pull/6750#issuecomment-14451661730" rel="noopener nofollow ugc">discussion</a> about this topic for more details.</li>
</ul>
<p>Migration guide comment about this change:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.3:_Organization_name_and_domain_changed_from_NA-MIC_to_Slicer" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.3:_Organization_name_and_domain_changed_from_NA-MIC_to_Slicer</a></p>

---
