# Update on Build factory status

**Topic ID**: 8146
**Date**: 2019-08-23
**URL**: https://discourse.slicer.org/t/update-on-build-factory-status/8146

---

## Post #1 by @Sam_Horvath (2019-08-23 14:42 UTC)

<p>Hello all  (<a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>) :</p>
<p>Mac and Windows builds have been failing for the past few days, without obvious errors.</p>
<p>Example: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2019-08-21" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2019-08-21</a> - Windows build</p>
<p>This appears to be due to the tests, which are all running to the timeout of  900s.  Logging into the factory machines through VNC (both mac and windows) show the tests hanging on the directory chooser for a new/existing DICOM database.  Linux is building with no issues (because no tests).  They eventually finish, (see mac above which eventually packaged), but far later than is feasible for a nightly build.</p>
<p>I have forced packaging / extension builds for both platforms, so reports should be coming up on CDash for that.  Windows packaging is failing with this error, which i will work on sorting out today:</p>
<p><code>1&gt;CUSTOMBUILD : error EndUpdateResourceD: /D/P/Slicer-0-build/Slicer-build/Slicer.exe [D:\D\P\Slicer-0-build\Slicer-build\Applications\SlicerApp\SlicerUpdateLauncherIcon.vcxproj]</code></p>
<p>Edit - error was due the open Slicer.exe’s in the background as the tests attempted to run.  Windows package should be up shortly.</p>
<p>Eddit:  Package link isn’t coming up on CDash: <a href="http://slicer.kitware.com/midas3/item/454544" rel="nofollow noopener">http://slicer.kitware.com/midas3/item/454544</a></p>

---

## Post #2 by @adamrankin (2019-08-23 15:01 UTC)

<p>Thanks for all the digging!</p>

---

## Post #3 by @jcfr (2019-08-23 15:40 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="1" data-topic="8146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>show the tests hanging on the directory chooser for a new/existing DICOM database.</p>
</blockquote>
</aside>
<p>Commit <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28452">r28452</a> from <a class="mention" href="/u/cpinter">@cpinter</a> was intended to address this.</p>
<p>It turns out that the popup leading to the timeout is the following:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8d645da060000b6c56bbc7489ae6cdda74328ea.png" alt="image" data-base62-sha1="qn8VMM6RijwKxR5budD7BXqegpc" width="627" height="424"></p>
<p>Last commit updating the source code responsible to display the dialog was <a href="https://github.com/commontk/CTK/commit/313e2f98c" class="inline-onebox">ENH: Allow updating DICOM database into different folder; Allow appli… · commontk/CTK@313e2f9 · GitHub</a></p>

---

## Post #4 by @Sam_Horvath (2019-08-23 16:03 UTC)

<p>Here is where ctkDICOMBrowser pops that dialog:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/acd419d5c6e27c6e13811dd508ab8cf17ec76c7a/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L495" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/acd419d5c6e27c6e13811dd508ab8cf17ec76c7a/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L495" target="_blank" rel="nofollow noopener">commontk/CTK/blob/acd419d5c6e27c6e13811dd508ab8cf17ec76c7a/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L495</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="485" style="counter-reset: li-counter 484 ;">
<li>  QPushButton* createButton = schemaUpdateMsgBox.addButton(tr(" Choose different folder "), QMessageBox::RejectRole);</li>
<li>  schemaUpdateMsgBox.setDefaultButton(updateButton);</li>
<li>  schemaUpdateMsgBox.exec();</li>
<li>  if (schemaUpdateMsgBox.clickedButton() == updateButton)</li>
<li>  {</li>
<li>    updateSchema = true;</li>
<li>  }</li>
<li>}</li>
<li>
</li>
<li>QString dir;</li>
<li class="selected">if (d-&gt;ShemaUpdateAutoCreateDirectory)</li>
<li>{</li>
<li>  // Auto-generate new database folder name</li>
<li>  QString newDatabaseDirPath = this-&gt;databaseDirectory();</li>
<li>  newDatabaseDirPath.append("-");</li>
<li>  newDatabaseDirPath.append(d-&gt;DICOMDatabase-&gt;schemaVersion());</li>
<li>  dir = newDatabaseDirPath;</li>
<li>}</li>
<li>else</li>
<li>{</li>
<li>  // Have user select new database folder</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #5 by @lassoan (2019-08-23 16:11 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I think you have fixed this (or a very similar) error. Could you check this? Thanks!</p>

---

## Post #6 by @cpinter (2019-08-23 16:52 UTC)

<p>The tests passed for me, but maybe I didn’t clear the ini file. I’ll check again.</p>

---

## Post #7 by @jcfr (2019-08-23 18:13 UTC)

<p>I manually removed the files and updated the dashboard scripts to ensure settings files are cleared every day.</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/DashboardScripts/commit/42a2f93caa582a8cea63a1e59566766587034066" target="_blank" rel="nofollow noopener">github.com/Slicer/DashboardScripts</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/jcfr" target="_blank" rel="nofollow noopener">
    <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/Slicer/DashboardScripts/commit/42a2f93caa582a8cea63a1e59566766587034066" target="_blank" rel="nofollow noopener">overload, factory-south-macos: Clean Slicer and SlicerSALT settings</a>
</h4>


<div class="date">
  by <a href="https://github.com/jcfr" target="_blank" rel="nofollow noopener">jcfr</a>
  on <a href="https://github.com/Slicer/DashboardScripts/commit/42a2f93caa582a8cea63a1e59566766587034066" target="_blank" rel="nofollow noopener">06:12PM - 23 Aug 19 UTC</a>
</div>

<div class="github-commit-stats">
  changed <strong>2 files</strong>
  with <strong>17 additions</strong>
  and <strong>0 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #8 by @Sam_Horvath (2019-08-26 13:58 UTC)

<p>Tests still timing out (whole test suite taking &gt;20hrs):</p>
<p><a href="http://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=1677416" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=1677416</a></p>

---

## Post #9 by @jcfr (2019-08-27 21:56 UTC)

<p>This should hopefully be fixed by <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28464" rel="nofollow noopener">r28464</a></p>

---

## Post #10 by @jcfr (2019-08-28 13:33 UTC)

<p>Looking at today dashboard, I confirm the issue is fixed.</p>

---

## Post #11 by @cpinter (2019-08-28 16:09 UTC)

<p>Thanks a lot! Sorry I didn’t get to it sooner; working on refactoring the model hierarchies, and the way hierarchy visibilities are handled. You’ll see a PR soon <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #12 by @jcfr (2019-09-06 11:51 UTC)

<p>The workaround I added is incomplete and not working.</p>
<p>I think a proper fix would to initialize <code>ShemaUpdateAutoCreateDirectory</code> using settings like it is already done <a href="https://github.com/commontk/CTK/blob/20a9195338ad3b84402fc7058f9d049189280912/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L993-L999" rel="nofollow noopener">here</a> for <code>schemaUpdateOption</code>. This would allow us to initialize the settings once without having to set the dicom browser property each time a browser is instantiated …</p>
<p>Failing to do so end up triggering the showing of <a href="https://github.com/commontk/CTK/blob/20a9195338ad3b84402fc7058f9d049189280912/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L531-L537" rel="nofollow noopener">this dialog</a> asking the user to <code>Choose existing database / Select empty folder for new DICOM database</code>.</p>
<p>Will be waiting today’s dashboard to complete to have a better idea of the test triggering a timeout</p>

---

## Post #13 by @lassoan (2019-09-09 18:55 UTC)

<p>It seems that there are still problems with the factory. There is no Windows package today; certain extensions are not available for yesterday (e.g, SlicerJupyter is missing).</p>

---

## Post #14 by @jcfr (2019-09-09 19:19 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Could you look into improving ctkDICOMBrowser by adding a settings for ShemaUpdateAutoCreateDirectory ?</p>

---

## Post #15 by @cpinter (2019-09-09 20:05 UTC)

<p>Yes I will take a look at this tomorrow.</p>

---

## Post #16 by @cpinter (2019-09-10 12:28 UTC)

<p>I created a PR: <a href="https://github.com/commontk/CTK/pull/884" rel="nofollow noopener">https://github.com/commontk/CTK/pull/884</a></p>
<p>One question that I have is what should be the default. I changed the default to true, so that the tests pass with a clean settings. In this case we’ll need to commit a fix in Slicer that changes this flag to false if Slicer is not in testing mode (DICOMWidgets.py:100)</p>

---

## Post #17 by @lassoan (2019-09-10 13:24 UTC)

<p>Thank you <a class="mention" href="/u/cpinter">@cpinter</a>. I find selecting an appropriate parent folder and creating a new empty folder is not very easy, so it would be great if we would do this for the users automatically by default (but have the option of setting a custom folder location and having the option of starting with a clean database or a copy of the old one).</p>
<p>Is it expected that database update is initiated immediately when Slicer is started (and not when you go to the DICOM module)?</p>

---

## Post #18 by @cpinter (2019-09-10 13:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="8146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is it expected that database update is initiated immediately when Slicer is started (and not when you go to the DICOM module)?</p>
</blockquote>
</aside>
<p>It only happens when the user opens the DICOM browser.</p>

---

## Post #19 by @jamesobutler (2019-09-10 13:52 UTC)

<p>I can confirm that I opened a recent Slicer nightly and it automatically made a SlicerDicomDatabase folder in my user documents location. I did not open the DICOM browser, but it must’ve instantiated an object on load.</p>

---

## Post #20 by @cpinter (2019-09-10 13:53 UTC)

<p>I see. To me this is unexpected. I will investigate why this happens. Thanks!</p>

---

## Post #21 by @cpinter (2019-09-10 14:51 UTC)

<p>This is why the ctkDICOMBrowser is created on startup:<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/d4aa634aa7b3e7f616d3c19a4e7dbe98c3ad0165#diff-3a9e489b30ef8fd9e195974d45857301R115" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
      <a href="https://github.com/lassoan" target="_blank" rel="nofollow noopener">
    <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="thumbnail onebox-avatar" width="90" height="90">
  </a>

<h4>
  <a href="https://github.com/Slicer/Slicer/commit/d4aa634aa7b3e7f616d3c19a4e7dbe98c3ad0165" target="_blank" rel="nofollow noopener">ENH: Create new view to embed DICOM browser in main widget</a>
</h4>

  <pre class="message" style="white-space: normal;">The DICOM browser layout is registered as a single view which spans the whole widget.
Navigating to the DICOM browser module will...</pre>

<div class="date">
  by <a href="https://github.com/lassoan" target="_blank" rel="nofollow noopener">lassoan</a>
  on <a href="https://github.com/Slicer/Slicer/commit/d4aa634aa7b3e7f616d3c19a4e7dbe98c3ad0165" target="_blank" rel="nofollow noopener">04:50PM - 19 Aug 19 UTC</a>
</div>

<div class="github-commit-stats">
  changed <strong>5 files</strong>
  with <strong>310 additions</strong>
  and <strong>27 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The performPostModuleDiscoveryTasks function triggers creating it by calling setDetailsPopup. This is related to the “DICOM browser in the layout” work.</p>

---

## Post #22 by @Sam_Horvath (2019-09-11 12:29 UTC)

<p>CDash is looking good so far today.  Packages are up for all platforms, minimal tests going to timeout.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=9" title=":tada:" class="emoji" alt=":tada:"></p>

---

## Post #23 by @ungi (2019-09-11 20:41 UTC)

<p>Hi. Windows build for extensions seem to be missing. I was looking for SlicerIGT, and the last version I found with a successful Windows build was Sept 5. And even on that day Mac build was missing. Do you know what’s going on, or if anyone is working on a fix?<br>
Thanks,<br>
Tamas</p>

---

## Post #24 by @Sam_Horvath (2019-09-11 20:57 UTC)

<p>This thread details the issues we have been having with the factories over the past week.</p>
<p>For today’s Windows extensions, It appears that the build was interrupted (not a build error issue). I am looking into it.</p>

---
