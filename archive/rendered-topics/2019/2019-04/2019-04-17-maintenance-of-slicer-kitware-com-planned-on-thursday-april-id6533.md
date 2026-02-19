---
topic_id: 6533
title: "Maintenance Of Slicer Kitware Com Planned On Thursday April"
date: 2019-04-17
url: https://discourse.slicer.org/t/6533
---

# Maintenance of slicer.kitware.com planned on Thursday April 18th from 2 to 3pm EDT

**Topic ID**: 6533
**Date**: 2019-04-17
**URL**: https://discourse.slicer.org/t/maintenance-of-slicer-kitware-com-planned-on-thursday-april-18th-from-2-to-3pm-edt/6533

---

## Post #1 by @jcfr (2019-04-17 21:03 UTC)

<p>Download and upload of Slicer extensions will be unavailable on on Thursday April 18th (tomorrow) from 2 to 3pm EDT.</p>
<p>The operating system associated with the server will be updated.</p>
<p>For reference, earlier this week, we tried to upgrade the operating system using a snapshot of the system and it worked great.</p>
<p>Thanks for your patience,</p>

---

## Post #2 by @jcfr (2019-04-18 18:45 UTC)

<p>Maintenance of the server is on-going, extensions upload/download as well as sample data download are  not expected to work during that time.</p>

---

## Post #3 by @jcfr (2019-04-18 18:48 UTC)

<p>The upgrade is now complete and the server is expected to be working. Please, report any issues.</p>

---

## Post #4 by @jcfr (2019-04-19 17:38 UTC)

<p>To follow up, as you may have noticed, some of the packages failed to be uploaded.</p>
<p>The problem has been identified and php settings have been tweaked. We made use the <code>memory_limit</code>, <code>upload_max_filesize</code> and <code>post_max_size</code> were set appropriately.</p>
<p>We will continue monitor the upload and follow up here with updates.</p>

---

## Post #5 by @jcfr (2019-04-23 15:17 UTC)

<p><strong>Observation</strong></p>
<p>The upload of packages have been failing consistently for the past few days.</p>
<p><strong>Mitigation</strong></p>
<p>Until now, we have been increasing the memory allocated to the PHP process (this was an easy “band-aid” to work around <a href="https://github.com/midasplatform/Midas/issues/69" rel="nofollow noopener">this issue</a>, this approach is not working any more.</p>
<p>Waiting we have resources to finalize the transition to a robust <a href="https://girder.readthedocs.io/" rel="nofollow noopener">Girder</a>-based package manager infrastructure [1], I will look into patching the <a href="https://github.com/midasplatform/slicerpackages" rel="nofollow noopener">slicerpackages</a> and <a href="https://github.com/midasplatform/slicerappstore" rel="nofollow noopener">slicerappstore</a> midas plugins so that the upload of nightly packages for Slicer extensions and applications are into different folders each month.</p>
<p>[1] <a href="https://discourse.slicer.org/t/slicer-extension-manager-user-interface-feedback/2475" class="inline-onebox">Slicer Extension Manager: User Interface Feedback</a></p>

---

## Post #6 by @jcfr (2019-04-29 22:53 UTC)

<p>You should now expect the regular nightly packages to be available for both Slicer applications and extensions.</p>
<p>Tomorrow dashboard should be able to confirm this.</p>
<h3>More details</h3>
<ul>
<li>
<p>We were able to address what was causing the server to use a lot of memory when uploading packages.  It should be fixed by this <a href="https://github.com/Slicer/Midas/commit/0d609469f69e464080ee02dd0eaf6f615bc17ff9" rel="nofollow noopener">commit</a> which is now deployed on <a href="http://slicer.kitware.com" rel="nofollow noopener">slicer.kitware.com</a>.</p>
</li>
<li>
<p>We addressed remaining errors about:</p>
<ul>
<li>
<p>“Invalid date format” when uploading Slicer application packages. This was fixed in Slicer code base applying commits (<a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28191" rel="nofollow noopener">r28191</a> and <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28190" rel="nofollow noopener">r28190</a>). These commits make sure the dates are now explicitly formatted as “YYYY-MM-DD HH:MM” without any timezone info. Most likely a change in how the new version of mysql server handles dates.</p>
</li>
<li>
<p>missing default value for “development_status” field when uploading extension packages. It was fixed in this <a href="https://github.com/midasplatform/slicerpackages/commit/5c4c6cabd391609c57b4d2c4d06fc11658c8ebd5" rel="nofollow noopener">commit</a> and was most likely caused by change in <a href="https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-5.html#mysqld-5-7-5-sql-mode" rel="nofollow noopener">sql mode</a>.</p>
</li>
</ul>
</li>
</ul>

---
