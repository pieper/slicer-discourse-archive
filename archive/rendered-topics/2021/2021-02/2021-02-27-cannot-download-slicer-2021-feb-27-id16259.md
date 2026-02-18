# Cannot download Slicer 2021 Feb 27

**Topic ID**: 16259
**Date**: 2021-02-27
**URL**: https://discourse.slicer.org/t/cannot-download-slicer-2021-feb-27/16259

---

## Post #1 by @arevell (2021-02-27 13:30 UTC)

<h1>An error occurred</h1>
<p>All three OS’s download links at <a href="https://download.slicer.org" rel="noopener nofollow ugc">https://download.slicer.org</a> seem to have a SQL error. I have all three OS’s on different computers and irrespective on which computer I am on, I get this error:</p>
<p>The system has encountered the following error:</p>
<h3>SQLSTATE[HY000]: General error: 144 Table ‘./midas/bitstream’ is marked as crashed and last (automatic?) repair failed, query was: SELECT <code>bitstream</code>.* FROM <code>bitstream</code> WHERE (bitstream_id = ‘1340262’) LIMIT 1</h3>
<p>In /projects/src/Midas3/library/Zend/Db/Statement/Pdo.php, line: 235<br>
At 00:30:10 2021-02-27</p>
<p>Please notify your administrator with this information.</p>

---

## Post #2 by @jcfr (2021-02-27 13:53 UTC)

<p>Sysadmins have been notified, I will follow up when the issue is addressed.</p>

---

## Post #3 by @zuhaib_izhar (2021-02-27 20:06 UTC)

<p>Operating system:<br>
Slicer version:4.11.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #4 by @lassoan (2021-02-27 20:12 UTC)

<p>Thanks for reporting. The storage server behind the download site is down. Administrators are notified.</p>

---

## Post #5 by @jcfr (2021-02-28 01:15 UTC)

<p>Updates:</p>
<ul>
<li>database tables have been repaired</li>
<li>website <a href="https://download.slicer.org/">https://download.slicer.org/</a> is now working as expected</li>
</ul>

---
