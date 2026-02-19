---
topic_id: 5022
title: "Slicercochlea Cdash Test Keeps Failing"
date: 2018-12-09
url: https://discourse.slicer.org/t/5022
---

# SlicerCochlea: Cdash test keeps failing

**Topic ID**: 5022
**Date**: 2018-12-09
**URL**: https://discourse.slicer.org/t/slicercochlea-cdash-test-keeps-failing/5022

---

## Post #1 by @brhoom (2018-12-09 10:56 UTC)

<p><strong>Site Name:</strong>  <a href="http://slicer.cdash.org/viewSite.php?siteid=949" rel="nofollow noopener">metroplex.kitware </a><br>
<strong>Build Name:</strong>  27501-SlicerCochlea-git722d991-g+±64bits-Qt5.11-Release<br>
<strong>Stamp:</strong>  20181209-0300-Extensions-4.10-Nightly<br>
<strong>Time:</strong>  2018-12-09T05:37:17 UTC<br>
<strong>Type:</strong>  Extensions-4.10-Nightly<br>
<strong>OS Name:</strong>  Linux<br>
<strong>OS Platform:</strong>  x86_64<br>
<strong>OS Release:</strong>  3.10.0-514.6.1.el7.x86_64<br>
<strong>OS Version:</strong>  <span class="hashtag">#1</span> SMP Sat Dec 10 11:15:38 EST 2016<br>
<strong>CTest version:</strong>  ctest-3.12.1<br>
<strong>Test output</strong></p>
<pre><code> qt.qpa.screen: QXcbConnection: Could not connect to display :0 Could not connect to any X display.
</code></pre>
<p>What does this error mean?</p>
<p>Here is the <a href="http://slicer.cdash.org/viewTest.php?buildid=1457023" rel="nofollow noopener">link</a>.</p>

---

## Post #2 by @lassoan (2018-12-09 14:25 UTC)

<p>This is a configuration issue on the build&amp;test server: display is not configured correctly.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> could you have a look? Thanks!</p>

---
