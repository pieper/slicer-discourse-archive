# Failing py_RSNA2012ProstateDemo test

**Topic ID**: 9119
**Date**: 2019-11-12
**URL**: https://discourse.slicer.org/t/failing-py-rsna2012prostatedemo-test/9119

---

## Post #1 by @jamesobutler (2019-11-12 17:38 UTC)

<p>I have been fixing long time failing tests however I’m unable to replicate the failure of py_RSNA2012ProstateDemo test locally on my Windows machine.  The test only fails on Windows and doesn’t provide any helpful output as seen <a href="http://slicer.cdash.org/testDetails.php?test=9751329&amp;build=1745675" rel="nofollow noopener">here</a>.  The test has been failing since June 1st of this year. Looking at commits merged on May 31st, there doesn’t seem to be anything that would make this start to fail.</p>
<p>My suspicion is that the download of the MRB file used by the test got corrupted some how.</p>
<p>Maybe <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> you can delete the file on the build machine at “…\AppData\Local\Temp\Slicer-tmp\RemoteIO\RSNA2012ProstateDemo.mrb” to potentially fix it?</p>
<p>Anyone else able to replicate this failing test?</p>

---

## Post #2 by @Sam_Horvath (2019-11-12 18:15 UTC)

<p>I have deleted the file</p>

---

## Post #3 by @jamesobutler (2019-11-13 12:23 UTC)

<p>Unfortunately the test is still <a href="http://slicer.cdash.org/testDetails.php?test=9751329&amp;build=1746598" rel="nofollow noopener">failing</a> on the build machine.</p>
<p>Another guess would be simply a difference in the Qt version as I’m using 5.12.5 instead of 5.10.1 or maybe also since I’m using Windows 10 instead of Windows 7.</p>
<p>Could someone provide the LastTest.log with the detailed output of the test?</p>

---

## Post #4 by @jamesobutler (2019-11-19 02:54 UTC)

<p>The failing test is no longer and it has been passing since 11-16-2019. See <a href="http://slicer.cdash.org/testDetails.php?test=9231074&amp;build=1748752" rel="nofollow noopener">passed results</a>.</p>

---

## Post #5 by @lassoan (2019-11-20 18:25 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="9119">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The failing test is no longer</p>
</blockquote>
</aside>
<p>This is great, thank you very much.</p>
<p>How did you fix the py_RSNA2012ProstateDemo test?</p>

---

## Post #6 by @jamesobutler (2019-11-20 21:11 UTC)

<p>I personally did not make any changes on 11-15-2019, so not sure exactly why it began to pass.</p>

---

## Post #7 by @pieper (2019-11-20 22:07 UTC)

<p>I understood <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> was going to look at cleaning up something on the factory machine? Maybe that fixed it.</p>

---

## Post #8 by @jamesobutler (2019-11-21 00:41 UTC)

<p>I posted above in this thread where I checked the following day after Sam said she deleted the file and it didn’t fix the test. So I don’t believe it was that unless the file was actually deleted some days later.</p>

---

## Post #9 by @jamesobutler (2019-11-21 17:17 UTC)

<p>And the test is mysteriously failing again as of today. See <a href="http://slicer.cdash.org/testDetails.php?test=9751329&amp;build=1753213" rel="nofollow noopener">results</a>.</p>

---

## Post #10 by @Sam_Horvath (2019-11-21 18:28 UTC)

<p>So, I just ran the  test on the factory (both through ctest and direct from command line), and it completes without any errors.</p>
<pre><code>D:\D\P\Slicer-0-build\Slicer-build&gt;C:\cmake-3.15.1\bin\ctest.exe -R py_RSNA2012ProstateDemo -C Relea
se
Test project D:/D/P/Slicer-0-build/Slicer-build
    Start 651: py_RSNA2012ProstateDemo
1/1 Test #651: py_RSNA2012ProstateDemo ..........   Passed   52.51 sec

100% tests passed, 0 tests failed out of 1

Total Test time (real) =  52.74 sec</code></pre>

---
