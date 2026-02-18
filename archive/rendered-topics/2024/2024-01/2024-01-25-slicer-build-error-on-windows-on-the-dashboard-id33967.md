# Slicer build error on Windows on the dashboard

**Topic ID**: 33967
**Date**: 2024-01-25
**URL**: https://discourse.slicer.org/t/slicer-build-error-on-windows-on-the-dashboard/33967

---

## Post #1 by @lassoan (2024-01-25 14:51 UTC)

<p>Since January 21, Slicer build on Windows has been failing (4 out of 5 cases) - <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2024-01-01&amp;end=2024-01-25&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=site&amp;compare1=63&amp;value1=overload&amp;field2=buildname&amp;compare2=63&amp;value2=Windows10">see dashbaord</a> with this error:</p>
<pre><code>LINK : fatal error LNK1104: cannot open file 'D:\D\P\S-0-build\DCMTK-build\bin\Release\ofstd.dll' [D:\D\P\S-0-build\DCMTK-build\ofstd\libsrc\ofstd.vcxproj] [D:\D\P\S-0-build\DCMTK.vcxproj]
</code></pre>
<p>There was a huge CTK update for the DICOM visual browser, but it should not affect DCMTK build. It is also odd that one build succeeded.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> OR <a class="mention" href="/u/jcfr">@jcfr</a> could you have a look? Does the file exist? Does restarting the build fixes the problem? Has anything been changed on the factory machine around January 21?</p>

---

## Post #2 by @Sam_Horvath (2024-01-25 15:00 UTC)

<p>Looking at it now, will post back soon.</p>

---

## Post #3 by @Sam_Horvath (2024-01-25 15:11 UTC)

<p>So, looking at the factory, the file exists, but there appears to be an executable hanging in the background that is holding the DLL:</p>
<p><code>dcmqrscp.exe</code><br>
Killing that allows DCMTK to proceed.  I will make sure we get a full build with extensions out today.<br>
The build that succeeded coincides with a reboot of the machine I think.</p>
<p>Now looking into why that process is remaining open.</p>

---

## Post #4 by @Sam_Horvath (2024-01-25 15:29 UTC)

<p>Suspicious commit:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/commontk/CTK/commit/05a858af00cf3ca51933da321bc708dfaf52936d">
  <header class="source">

      <a href="https://github.com/commontk/CTK/commit/05a858af00cf3ca51933da321bc708dfaf52936d" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/commit/05a858af00cf3ca51933da321bc708dfaf52936d" target="_blank" rel="noopener">BUG: Set test resource lock on all tests using "dcmqrscp" executable</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2024-01-18" data-time="07:17:41" data-timezone="UTC">07:17AM - 18 Jan 24 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 2 files with 7 additions and 0 deletions">
        <a href="https://github.com/commontk/CTK/commit/05a858af00cf3ca51933da321bc708dfaf52936d" target="_blank" rel="noopener">
          <span class="added">+7</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This will prevent the following test from all running in parallel with
a `dcmqrs<span class="show-more-container"><a href="https://github.com/commontk/CTK/commit/05a858af00cf3ca51933da321bc708dfaf52936d" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">cp` executable configured to listen on the same port.

Tests either using "dcmqrscp" executable directly or through the
`ctkDICOMTester` helper class:

* ctkDICOMApplicationTest1
* ctkDICOMQueryTest2
* ctkDICOMRetrieveTest2
* ctkDICOMTesterTest1
* ctkDICOMTesterTest2</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Sam_Horvath (2024-01-25 15:35 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Do we need to add a similar commit to this one to ensure that <code>dcmqrscp</code> is killed?</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/commontk/CTK/commit/5b502aa7160d96d09e4819138065bd32cd5534e2">
  <header class="source">

      <a href="https://github.com/commontk/CTK/commit/5b502aa7160d96d09e4819138065bd32cd5534e2" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/commit/5b502aa7160d96d09e4819138065bd32cd5534e2" target="_blank" rel="noopener">BUG: Update ctkDICOMTester to always kill "storescp" process on destruction</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2024-01-18" data-time="07:17:41" data-timezone="UTC">07:17AM - 18 Jan 24 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 1 files with 4 additions and 2 deletions">
        <a href="https://github.com/commontk/CTK/commit/5b502aa7160d96d09e4819138065bd32cd5534e2" target="_blank" rel="noopener">
          <span class="added">+4</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Since the DCMTK executable do not seem to configure a termination handler on
win<span class="show-more-container"><a href="https://github.com/commontk/CTK/commit/5b502aa7160d96d09e4819138065bd32cd5534e2" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">dows (using `SetConsoleCtrlHandler()`) or on Unix (using `sigaction()`),
we speed up testing by simply killing the process.

&gt; On Windows, terminate() posts a WM_CLOSE message to all top-level
&gt; windows of the process and then to the main thread of the process
&gt; itself. On Unix and macOS the SIGTERM signal is sent.
&gt;
&gt; Console applications on Windows that do not run an event loop, or whose
&gt; event loop does not handle the WM_CLOSE message, can only be terminated
&gt; by calling kill().

Source: https://doc.qt.io/qt-5/qprocess.html#terminate</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jcfr (2024-01-25 15:41 UTC)

<p>I also had to kill the process earlier this week. I originally thought the process was running due to tests I ran while testing CTK manually.</p>
<p>Since when Slicer is built, we do not explicitly run the CTK tests, I am not sure the linked commit is the culprit.</p>
<p>I will follow-up when I have an update.</p>

---

## Post #7 by @jcfr (2024-01-25 17:13 UTC)

<p>We may have to look into the following:</p>
<pre><code class="lang-plaintext">Modules/Scripted/DICOMLib/DICOMProcesses.py
Applications/SlicerApp/Testing/Python/JRC2013Vis.py
</code></pre>
<p>That are both starting the <code>dcmqrscp</code> process, I will further review later this evening.</p>
<p>Independently of addressing this, we will also look into updating the dashboard script so that it makes sure all instance of DCMTK application are “terminated” before initiating the next cycle of nightly build.</p>

---

## Post #8 by @lassoan (2024-01-25 17:20 UTC)

<p>Thanks for the investigations!</p>
<p>If you have the chance, it would be great if you could trigger a Slicer build/package/upload for the Slicer Preview Release so that users get a chance to test out Davide’s latest DICOM browser features and fixes.</p>

---

## Post #9 by @Sam_Horvath (2024-01-25 17:42 UTC)

<p>Yep, a build has been started and is in progress.</p>

---

## Post #10 by @lassoan (2024-01-25 18:07 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="33967">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>That are both starting the <code>dcmqrscp</code> process, I will further review later this evening.</p>
</blockquote>
</aside>
<p>dcmqrscp is a server and Windows firewall may show a popup asking the user for permission to open the port. This popup may interfere with the test exiting cleanly. If the user gave the permission once then I think it is not asked again for the same executable file (full path).</p>
<p>You can have a look at the list of allowed apps in the Control Panel\System and Security\Windows Defender Firewall\Allowed apps:</p>
<p></p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13e6c04f9a9fd876f98e16de739dbd8c6dc742ff.png" data-download-href="/uploads/short-url/2Q3s9HiiqLwwCL6WnMisdjKcYI7.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13e6c04f9a9fd876f98e16de739dbd8c6dc742ff_2_690x435.png" alt="image" data-base62-sha1="2Q3s9HiiqLwwCL6WnMisdjKcYI7" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13e6c04f9a9fd876f98e16de739dbd8c6dc742ff_2_690x435.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13e6c04f9a9fd876f98e16de739dbd8c6dc742ff_2_1035x652.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13e6c04f9a9fd876f98e16de739dbd8c6dc742ff_2_1380x870.png 2x" data-dominant-color="DEDFE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1511×953 70.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><p></p>

---

## Post #11 by @Davide_Punzo (2024-01-26 08:12 UTC)

<p>Today windows build has failed as well <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"> and the last available Windows download is from 23. Would be possible for you to check again <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> ? thanks in advance.</p>

---

## Post #12 by @Sam_Horvath (2024-01-26 15:20 UTC)

<p>Will do. I think it is the same issue, just not yet resolved.</p>
<p>Re: latest build, the download page for me has the build I triggered yesterday,  and that should have the latest changes from the visual DICOM browser.</p>
<p>I did note during that build yesterday that it was taking o very long time for the download page to update.</p>
<p>Another way to get the most recent package is from the cdash site: <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2024-01-25" class="inline-onebox">CDash</a>, the yellow package next to the build name.</p>

---

## Post #13 by @Davide_Punzo (2024-01-26 17:07 UTC)

<p>Ah yes, now it is the latest version (this morning it was still the 23th). thanks for looking into it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #14 by @jcfr (2024-01-26 18:06 UTC)

<p>It is indeed a server, we need to also understand which test is starting the server.</p>
<p>Away from computer travelling, i didn’t have a chance to further look into this.</p>

---

## Post #15 by @jcfr (2024-01-26 23:38 UTC)

<blockquote>
<p>This popup may interfere with the test exiting cleanly. If the user gave the permission once then I think it is not asked again for the same executable file (full path).</p>
<p>You can have a look at the list of allowed apps in the Control Panel\System and Security\Windows Defender Firewall\Allowed apps:</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks for the detailed instructions, the settings have been updated accordingly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebb6ee48d62c3e1f8e7ae9299dec9f66a4adbd64.png" data-download-href="/uploads/short-url/xDe8fbXoj0DHbakHIQUeQd3gmJm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebb6ee48d62c3e1f8e7ae9299dec9f66a4adbd64_2_690x181.png" alt="image" data-base62-sha1="xDe8fbXoj0DHbakHIQUeQd3gmJm" width="690" height="181" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebb6ee48d62c3e1f8e7ae9299dec9f66a4adbd64_2_690x181.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebb6ee48d62c3e1f8e7ae9299dec9f66a4adbd64_2_1035x271.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebb6ee48d62c3e1f8e7ae9299dec9f66a4adbd64.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1173×309 30.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @jcfr (2024-01-27 20:51 UTC)

<p>Today’s dasboard didn’t report any issues related  to the <code>dcmqrscp</code> process <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></p>
<p>Thanks everyone for your input and help to sort this out <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #17 by @jcfr (2024-01-31 02:50 UTC)

<p>After inspecting the process explorer (following similar error reported on the dashboard), the <code>dcmqrscp</code> process still persists once the Slicer (or Slicer extension ?) tests have been executed:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dc84ca2eb5f8acb4c365c7999df211680ce32cd.png" data-download-href="/uploads/short-url/6x0CMHihUpZibA2u4ibJuyejOZT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dc84ca2eb5f8acb4c365c7999df211680ce32cd_2_477x375.png" alt="image" data-base62-sha1="6x0CMHihUpZibA2u4ibJuyejOZT" width="477" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dc84ca2eb5f8acb4c365c7999df211680ce32cd_2_477x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2dc84ca2eb5f8acb4c365c7999df211680ce32cd_2_715x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dc84ca2eb5f8acb4c365c7999df211680ce32cd.png 2x" data-dominant-color="ECECED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">771×605 88.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will investigate and report back.</p>

---

## Post #18 by @jcfr (2024-02-02 07:19 UTC)

<p>Until we further improve the lifecycle associated with the execution of the <code>dcmqrscp</code>, a daily job has been setup to kill the process using  before the the Preview build is started.</p>
<p>For reference, the following is executed:</p>
<pre><code class="lang-plaintext">taskkill /F /T /IM dcmqrscp.exe
</code></pre>

---
