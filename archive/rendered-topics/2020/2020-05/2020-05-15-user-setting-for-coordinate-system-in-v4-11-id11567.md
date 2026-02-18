# User setting for coordinate system in v4.11?

**Topic ID**: 11567
**Date**: 2020-05-15
**URL**: https://discourse.slicer.org/t/user-setting-for-coordinate-system-in-v4-11/11567

---

## Post #1 by @Greydon_Gilmore (2020-05-15 23:16 UTC)

<p>Hi,</p>
<p>I am working with v4.11 and recently became aware that v4.11 has changed the default coordinate system (RAS -&gt; LPS). Wondering if there will be an option in settings for the user to select their preferred coordinate system? Most of our workflows and projects are using RAS system from v4.10.</p>
<p>Thank you,<br>
Greydon</p>

---

## Post #2 by @lassoan (2020-05-22 21:54 UTC)

<p>Sorry for not noticing this post until now (it was added to a developer resource subcategory, which is not monitored). This page should help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default</a>. If you have any remaining questions then let us know.</p>

---

## Post #3 by @jclauneuro (2020-05-25 00:35 UTC)

<p>Thanks <a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a> for posting and <a class="mention" href="/u/lassoan">@lassoan</a> for your comments!</p>
<p>Up until v4.10.2, RAS has been the default output coordinate system which is what our original markup placement protocol was developed on. We started noticing issues when placements in v4.11 were displayed in versions &lt; 4.11. That’s what led us to find this coordinate system change in markup files.</p>
<p>As a short term solution, we have made it pretty clear to our user base to only use up to v4.10.2 for placements.</p>
<p>The better solution would be to update our validator to perform more detailed checks of the header for the version and coordinate system. We created an issue for our project here: <a href="https://github.com/afids/afids-validator/issues/72" rel="nofollow noopener">https://github.com/afids/afids-validator/issues/72</a></p>
<p>Is there a rough timeline for a stable version of Slicer v5.0 so our team can plan accordingly?</p>
<p>Note: Our Markup files encodes details about the L and R sides of the coordinate space (based on the location of anatomical features in the brain), which could be useful for migration test cases.</p>

---

## Post #4 by @lassoan (2020-05-25 04:16 UTC)

<p>Slicer can read scenes created by previous software versions, but it is not feasible to make the Slicer compatible with all data created in future versions of the software. This means that you are not forced to upgrade your software, but if you do, then you may not be able to go back.</p>
<p>I would recommend to ask your users to use a specific Slicer version: either Slicer-4.10.2 or a selected Slicer-4.11.x release (you can get a download link by specifying a date or revision as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">here</a>).</p>
<p>We will release Slicer-5 when these issues are completed: <a href="https://github.com/Slicer/Slicer/milestone/1">https://github.com/Slicer/Slicer/milestone/1</a>. It is difficult to estimate when this will happen, but hopefully within 1-2 months. This should not be a blocking point, as Since-4.11 releases are generally very stable, so you can standardize on any of them if you want to take advantage of some new features before Slicer-5 is officially released.</p>

---
