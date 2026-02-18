# Additional module path disappears after restart

**Topic ID**: 45357
**Date**: 2025-12-03
**URL**: https://discourse.slicer.org/t/additional-module-path-disappears-after-restart/45357

---

## Post #1 by @fedorov (2025-12-03 19:12 UTC)

<p>I am adding a new module directory via application settings, but after restart, the added directory disappears. There are no errors relevant to this during application startup. I observe this with both 5.10 and nightly. I am on a mac. I tried this with an empty directory, and the behavior is the same, so it is not related to the specific module.</p>

---

## Post #2 by @lassoan (2025-12-03 19:40 UTC)

<p>Additional module paths are checked at application startup and if the folder does not exist then it is removed. Could you have a look at the Slicer-NNN.ini file and see what paths are listed there, how they are defined (with relative path?) and if they can be found on your system? Are the folders on a physical disk or some virtual/network drive?</p>

---

## Post #3 by @muratmaga (2025-12-03 20:22 UTC)

<p>It is not very useful but I want to add that I have seen this, and couple other variants, such as drag and dropping a module folder onto the Slicer windows not bringing the “add these python scripts to module paths” option, or extension wizard not recognizing some module folders, sporadically on MacOS. Never managed to consistently replicate though.</p>

---

## Post #4 by @fedorov (2025-12-03 21:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="45357">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Additional module paths are checked at application startup and if the folder does not exist then it is removed.</p>
</blockquote>
</aside>
<p>The folder definitely exists. I created the folder, and selected that folder from the file picker. I confirm the folder itself remains in place after Slicer restart.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="45357">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you have a look at the Slicer-NNN.ini file and see what paths are listed there, how they are defined (with relative path?) and if they can be found on your system?</p>
</blockquote>
</aside>
<p>When I look at the <code>~/.config/slicer.org/Slicer.ini</code> file, I do not see the added folder anywhere before or after the restart. Is this the right file to check?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="45357">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are the folders on a physical disk or some virtual/network drive?</p>
</blockquote>
</aside>
<p>Physical drive, main drive on a mac mini.</p>
<p>I do not see this issue on linux.</p>

---

## Post #5 by @lassoan (2025-12-03 22:02 UTC)

<p>The Slicer-NNN.ini file is the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#user-and-revision-specific-settings">revision-specific config file</a> in the application’s install path. You can get the path by typing this into the Slicer Python console:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.app.slicerRevisionUserSettingsFilePath
</code></pre>
<p>If the path is not added to this .ini file then there may be some macOS permission issues. <a class="mention" href="/u/pieper">@pieper</a> have you experienced something like this lately?</p>

---

## Post #6 by @pieper (2025-12-03 23:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="45357">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> have you experienced something like this lately?</p>
</blockquote>
</aside>
<p>I don’t usually use the settings files for this.  I use the <code>--additional-module-paths</code> command line argument (this helps isolate different experiments using the same Slicer version).</p>

---

## Post #7 by @fedorov (2025-12-09 19:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="45357">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If the path is not added to this .ini file then there may be some macOS permission issues.</p>
</blockquote>
</aside>
<p>I checked, and this is the file:</p>
<pre><code class="lang-auto">ls -lat /Applications/Slicer-20251129.app/Contents/bin/../slicer.org/Slicer-34291.ini
-rw-r–r–@ 1 rsna2023  admin  1686 Dec  1 15:37 /Applications/Slicer-20251129.app/Contents/bin/../slicer.org/Slicer-34291.ini
</code></pre>
<p>To add more detail, on this system I installed Slicer under a different account, and then have been using it under the <code>rsna2023</code> user account. I confirmed <code>rsna2023</code> user can write to this file, but the file is unchanged before or after the restart if I try to remove a path in the Application module settings.</p>
<p>To me, the unresolved questions are:</p>
<ol>
<li>Why is that file remaining unchanged?</li>
<li>The way permissions are set up for that file, since application is shared across users on the system, it will definitely be problematic, since it is readable only by one user. Is this a bug?</li>
<li>There does not seem to be any error at any point that would indicate failure to modify that settings file. Is this a bug?</li>
</ol>
<p>Here’s the full contents of the file.</p>
<pre><code class="lang-auto">[Extensions]
[Extensions]
FrontendServerUrl=https://extensions.slicer.org
InstallPath=Extensions-34291
LastServerAPI=Girder_v1
ManagerEnabled=true
MetadataFromServerUpdateTime=2025-12-01T02:52:59Z
MetadataFromServerUrl=https://slicer-packages.kitware.com
ServerUrl=https://slicer-packages.kitware.com

[LibraryPaths]
1\path=Extensions-34291/QuantitativeReporting/lib/Slicer-5.11
2\path=Extensions-34291/SlicerDevelopmentToolbox/lib/Slicer-5.11
3\path=Extensions-34291/IDCBrowser/lib/Slicer-5.11
4\path=Extensions-34291/DCMQI/lib/Slicer-5.11
5\path=Extensions-34291/DCMQI/lib/Slicer-5.11/cli-modules
6\path=Extensions-34291/PETDICOMExtension/lib/Slicer-5.11
7\path=Extensions-34291/PETDICOMExtension/lib/Slicer-5.11/cli-modules
size=7

[Modules]
AdditionalPaths=Extensions-34291/QuantitativeReporting/lib/Slicer-5.11/qt-scripted-modules, Extensions-34291/SlicerDevelopmentToolbox/lib/Slicer-5.11/qt-scripted-modules, Extensions-34291/DCMQI/lib/Slicer-5.11/cli-modules, Extensions-34291/PETDICOMExtension/lib/Slicer-5.11/cli-modules, Extensions-34291/PETDICOMExtension/lib/Slicer-5.11/qt-scripted-modules
IgnoreModules=@Invalid()

[PYTHONPATH]
1\path=Extensions-34291/QuantitativeReporting/lib/Slicer-5.11/qt-scripted-modules
2\path=Extensions-34291/SlicerDevelopmentToolbox/lib/Slicer-5.11/qt-scripted-modules
3\path=Extensions-34291/IDCBrowser/lib/Slicer-5.11/qt-scripted-modules
4\path=Extensions-34291/PETDICOMExtension/lib/Slicer-5.11/qt-scripted-modules
size=4

[Paths]
1\path=Extensions-34291/DCMQI/lib/Slicer-5.11/cli-modules
2\path=Extensions-34291/PETDICOMExtension/lib/Slicer-5.11/cli-modules
size=2

[QT_PLUGIN_PATH]
size=0
</code></pre>

---

## Post #8 by @lassoan (2025-12-09 21:50 UTC)

<p>I’m not sure how much this behavior is expected in a multi-user environment, but not giving the user any feedback when the .ini file update is failed is definitely a bug that should be fixed. I’ve created an issue for it:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8896">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8896" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8896" target="_blank" rel="noopener">No error message is displayed when additional module path cannot be added</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-12-09" data-time="21:48:13" data-timezone="UTC">09:48PM - 09 Dec 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When the adding "additional module paths" to the Slicer-NNN.ini file fails (e.g.<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">, due to file permission issues) then the user should get a meaningful error message about it.

See more information here: https://discourse.slicer.org/t/additional-module-path-disappears-after-restart/45357/7</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/fedorov">@fedorov</a> Could <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> work on this as part of his IDC activities?</p>

---

## Post #9 by @fedorov (2025-12-09 22:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="45357">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> work on this as part of his IDC activities?</p>
</blockquote>
</aside>
<p>Only if this is a trivial fix. There are IDC tasks outside of Slicer development that I need to get Kyle to start working on, once the already assigned Slicer tasks are completed.</p>

---

## Post #10 by @lassoan (2025-12-09 22:08 UTC)

<p>OK, makes sense, thank you for the clarification.</p>

---

## Post #11 by @fedorov (2025-12-09 22:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="45357">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’m not sure how much this behavior is expected in a multi-user environment</p>
</blockquote>
</aside>
<p>Until today, I always installed Slicer into the Applications folder on Mac. I moved the app into one of my user folders, and now everything works as expected.</p>
<p>I think the conclusion is that if there is any chance Slicer can be used in a multi-user setting, it should not be installed into the Applications folder on Mac.</p>

---

## Post #12 by @pieper (2025-12-10 00:02 UTC)

<p>We could change the dmg file to include a link to the user’s local Applications folder rather than the system one.</p>

---
