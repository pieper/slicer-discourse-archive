# Slicer is freezing on macOS when clicking on "Import DICOM files"

**Topic ID**: 18624
**Date**: 2021-07-11
**URL**: https://discourse.slicer.org/t/slicer-is-freezing-on-macos-when-clicking-on-import-dicom-files/18624

---

## Post #1 by @mohammed_alshakhas (2021-07-11 09:49 UTC)

<p>version 2021.07.08 on mac M1</p>
<p>once I press load Dicom , slicer freezes and nothing can be done. interestingly, when I try to force turn off, I don’t get ( not responding ) next to the app showing a freeze.</p>
<p>older versions worked fine till this</p>
<p>if i don’t try to load dicom it works fine</p>

---

## Post #2 by @pieper (2021-07-11 14:39 UTC)

<p>Thanks for reporting - perhaps this is due to the M1 chip.  Try loading different data or if it’s unique to the data try the same data on a different machine and let us know.</p>

---

## Post #3 by @mohammed_alshakhas (2021-07-11 17:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11a49ff417c9ecd533a09afdaa2f83e0b0a4b644.png" data-download-href="/uploads/short-url/2w4P5CNZrXWIBO9RJQoWCE0knVW.png?dl=1" title="Screen Shot 2021-07-11 at 20.51.59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11a49ff417c9ecd533a09afdaa2f83e0b0a4b644_2_690x219.png" alt="Screen Shot 2021-07-11 at 20.51.59" data-base62-sha1="2w4P5CNZrXWIBO9RJQoWCE0knVW" width="690" height="219" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11a49ff417c9ecd533a09afdaa2f83e0b0a4b644_2_690x219.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11a49ff417c9ecd533a09afdaa2f83e0b0a4b644_2_1035x328.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11a49ff417c9ecd533a09afdaa2f83e0b0a4b644.png 2x" data-dominant-color="3B3B3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-07-11 at 20.51.59</span><span class="informations">1144×364 63.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>im sorry i meant trying to import data , so  once i click on import dicom it freezes</p>

---

## Post #4 by @lassoan (2021-07-12 04:25 UTC)

<p>I think it is due to the recent change in the file selector popup (when you press “Import DICOM files”). As a workaround, you can drag-and-drop the DICOM folder to the application window.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> could you test the “Import DICOM files” button on macOS?</p>

---

## Post #5 by @pieper (2021-07-12 15:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="18624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> could you test the “Import DICOM files” button on macOS?</p>
</blockquote>
</aside>
<p>Yes, I see the behavior too on my mac build.  This is a pretty serious issue - do you know the fix?</p>

---

## Post #6 by @lassoan (2021-07-12 15:09 UTC)

<p>Yes, it is a very serious issue, especially because it impacts those who are new to Slicer and don’t know they can just drag-and-drop the images. I guess the file dialog options in CTK are set incorrectly (maybe it does not appear or appears in some invisible place?) see changes in these commits:</p>
<ul>
<li><a href="https://github.com/commontk/CTK/commit/c4f1eeead234022e74de978126e3a54f648880e5" class="inline-onebox">ENH: Update ctkFileDialog to use native dialog by default · commontk/CTK@c4f1eee · GitHub</a></li>
<li><a href="https://github.com/commontk/CTK/commit/5532a5a7ec07fada320cda43b831515d702a1c6f" class="inline-onebox">BUG: Fix crash instantiating ctkDICOMBrowser · commontk/CTK@5532a5a · GitHub</a></li>
</ul>

---

## Post #7 by @jamesobutler (2021-07-12 15:54 UTC)

<p>Is this specific to the “Import DICOM files” button or is it a problem for all Qt native file dialog usage on macOS?</p>
<pre><code class="lang-python">file_dialog = qt.QFileDialog()
file_dialog.getExistingDirectory()
</code></pre>
<p>Qt 5.15 can set the target platform to 10.13, 10.14, and 10.15 (see <a href="https://doc-snapshots.qt.io/qt5-5.15/supported-platforms.html" rel="noopener nofollow ugc">here</a>).  With the move to macOS 11 with M1 support maybe there are issues?</p>

---

## Post #8 by @lassoan (2021-07-12 17:29 UTC)

<p>The native dialogs work fine, but this is a non-native dialog (has the “import” checkbox). Probably we should just switch to the native dialog and add the import/copy checkbox to the DICOM browser settings. I’ve added an issue to keep track the status of this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5739">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5739" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5739" target="_blank" rel="noopener">Slicer hangs on macOS if user clicks on "Import DICOM files" button</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-07-12" data-time="17:25:00" data-timezone="UTC">05:25PM - 12 Jul 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          priority:urgent
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">On macOS if user clicks on "Import DICOM files" button in DICOM module then the <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">folder selector popup does not get displayed.

## Environment
- Slicer version: Slicer-4.13.0-2021-07-11
- Operating system: macOS only (tested on Intel)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Regardless of removing all non-native file selectors in Slicer, we should fix the non-native dialog in CTK.</p>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> do you have access to a mac? Can you investigate/fix this?</p>

---

## Post #9 by @jamesobutler (2021-07-12 17:35 UTC)

<p>The “Import DICOM files” button is using a native file dialog as of the change to native file dialog usage. See <a href="https://github.com/commontk/CTK/pull/977" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix crash instantiating ctkDICOMBrowser by jamesobutler · Pull Request #977 · commontk/CTK · GitHub</a>. This is a snippet of the native dialog being used.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7732b1fbb60dfe4a0fe1fb1a5fd4d099c331084.png" data-download-href="/uploads/short-url/uJXp0K2uwmq1QNqbygJzkoBk6dm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7732b1fbb60dfe4a0fe1fb1a5fd4d099c331084.png" alt="image" data-base62-sha1="uJXp0K2uwmq1QNqbygJzkoBk6dm" width="690" height="178" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">939×243 15.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I do not have access to a mac to investigate this.</p>

---

## Post #10 by @lassoan (2021-07-12 17:53 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="9" data-topic="18624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The “Import DICOM files” button is using a native file dialog as of the change to native file dialog usage.</p>
</blockquote>
</aside>
<p>I see, yes, it is indeed a native dialog.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Could you investigate? There are a number of special flags set (bottomWidget, ApplicationModel, …) that may cause trouble.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L375-L382">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L375-L382" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L375-L382" target="_blank" rel="noopener">commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L375-L382</a></h4>



    <pre class="onebox"><code class="lang-cpp">
      <ol class="start lines" start="375" style="counter-reset: li-counter 374 ;">
          <li></li>
          <li>// Default values</li>
          <li>importDirectoryModeComboBox-&gt;setCurrentIndex(</li>
          <li>    importDirectoryModeComboBox-&gt;findData(static_cast&lt;int&gt;(q-&gt;importDirectoryMode())));</li>
          <li></li>
          <li>//Initialize import widget</li>
          <li>this-&gt;ImportDialog = new ctkFileDialog();</li>
          <li>this-&gt;ImportDialog-&gt;setBottomWidget(importDirectoryBottomWidget);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @pieper (2021-07-12 18:46 UTC)

<p>Okay, I’ll have a look.</p>

---

## Post #12 by @pieper (2021-07-13 20:03 UTC)

<p>This seems to be a bug related to Qt and macOS getting confused about multiple screens.  <a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a> do you also have two screens on your mac?</p>
<p>It seems the location of the dialog can be off-screen so the application appears to hang because there’s a modal dialog you cannot see.  It appears this can happen when the dialog position is calculated based on the main window location on one screen but is displayed on the other screen and ends up being off-screen.</p>
<p>There are similar problems with menus and tooltips popping up in the wrong locations too.  When I get time I’ll check if there is an updated Qt version that might address this.</p>
<p>On my build I can get around this apparent hang by commenting out line 382 here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L382">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L382" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L382" target="_blank" rel="noopener">commontk/CTK/blob/master/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L382</a></h4>



  <pre class="onebox">    <code class="lang-cpp">
      <ol class="start lines" start="372" style="counter-reset: li-counter 371 ;">
          <li>      importDirectoryModeComboBox-&gt;findData(q-&gt;importDirectoryMode()));</li>
          <li>
          </li>
<li>//Initialize import widget</li>
          <li>this-&gt;ImportDialog = new ctkFileDialog();</li>
          <li>this-&gt;ImportDialog-&gt;setBottomWidget(importDirectoryBottomWidget);</li>
          <li>this-&gt;ImportDialog-&gt;setFileMode(QFileDialog::Directory);</li>
          <li>// XXX Method setSelectionMode must be called after setFileMode</li>
          <li>this-&gt;ImportDialog-&gt;setSelectionMode(QAbstractItemView::ExtendedSelection);</li>
          <li>this-&gt;ImportDialog-&gt;setLabelText(QFileDialog::Accept,"Import");</li>
          <li>this-&gt;ImportDialog-&gt;setWindowTitle("Import DICOM files from directory ...");</li>
          <li class="selected">this-&gt;ImportDialog-&gt;setWindowModality(Qt::ApplicationModal);</li>
          <li>
          </li>
<li>this-&gt;MetadataDialog = new ctkDICOMMetadataDialog();</li>
          <li>this-&gt;MetadataDialog-&gt;setObjectName("DICOMMetadata");</li>
          <li>this-&gt;MetadataDialog-&gt;setWindowTitle("DICOM File Metadata");</li>
          <li>
          </li>
<li>//connect signal and slots</li>
          <li>q-&gt;connect(this-&gt;ImportDialog, SIGNAL(filesSelected(QStringList)),</li>
          <li>        q,SLOT(onImportDirectoriesSelected(QStringList)));</li>
          <li>
          </li>
<li>q-&gt;connect(importDirectoryModeComboBox, SIGNAL(currentIndexChanged(int)),</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>With even with that change, there is something odd going on with the dialogs from the dicom module.  if I start Slicer on one screen, then drag the app to another, then invoke one of the dicom dialogs (either import or query-retrieve) it will show up on the screen where Slicer was started.  Other dialogs, like the load and save dialogs follow Slicer to the new screen.  I don’t see any obvious reason why some dialogs would appear on one screen and some on the other.  The import dialog is native and the query retrieve dialog is a QDialog.</p>
<p>So other than removing that one line and waiting for a better Qt fix I’m not sure what more can be done right now.</p>
<p>Depending on how this bug manifests it may be a workaround to remove your settings file like this <code>rm -rf ~/.config/www.na-mic.org/</code>.</p>

---

## Post #13 by @lassoan (2021-07-13 21:40 UTC)

<p>I’ve tried it on a mac that has not been connected to an external screen for years and removed the entire <code>~/.config/www.na-mic.org/</code> folder and the issue is the same.</p>
<p>Maybe the issue is that the dialog is not displayed using <code>exec</code> or <code>open</code> but it just got shown and raised:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/CTK/blob/e485a3fcecdffc2b40aaafbdbf9f470edf403354/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L762-L768">
  <header class="source">

      <a href="https://github.com/commontk/CTK/blob/e485a3fcecdffc2b40aaafbdbf9f470edf403354/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L762-L768" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/e485a3fcecdffc2b40aaafbdbf9f470edf403354/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L762-L768" target="_blank" rel="noopener">commontk/CTK/blob/e485a3fcecdffc2b40aaafbdbf9f470edf403354/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L762-L768</a></h4>



  <pre class="onebox">    <code class="lang-cpp">
      <ol class="start lines" start="762" style="counter-reset: li-counter 761 ;">
          <li>void ctkDICOMBrowser::openImportDialog()</li>
          <li>{</li>
          <li>  Q_D(ctkDICOMBrowser);</li>
          <li>
          </li>
<li>  d-&gt;ImportDialog-&gt;show();</li>
          <li>  d-&gt;ImportDialog-&gt;raise();</li>
          <li>}</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/pieper">@pieper</a> could you try if using <code>exec</code> or <code>open</code> to show the dialog fixes the problem?</p>

---

## Post #14 by @jamesobutler (2021-07-14 00:31 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Are you using Qt 5.15.2? From my memory I think we updated the factory macOS builds from 5.15.1 to 5.15.2 to resolve some issues with tool tips and menus and stuff.</p>
<p>This also reminds me as part of the new upcoming Slicer release all platforms should use the same Qt version which is currently not the case. <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #15 by @mohammed_alshakhas (2021-07-14 08:43 UTC)

<p>i do have multiple screen and i check on the other screen cause im familiar with that issue in other software .<br>
to make i sure i don’t have that  i do right click and `" show all windows"  and that will show me if im missing the dialogue box.</p>
<p>thought about it and unfortunately did find any dialogue box on other screen.</p>
<p>i do have however other times where slicer by itself swipe to to other blank screen which is extremely ANNOYING</p>

---

## Post #16 by @pieper (2021-07-14 14:24 UTC)

<p>Agreed, there are some bugs in the Qt / macOS integration in terms of screens and spaces.  The splash screen doesn’t show up right, the screen geometry is not saved/restored right, the dialogs and tooltips and even menus show up in the wrong places.  I’ve gotten a bit used to them but I agree they are <em>annoying</em>.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="14" data-topic="18624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Are you using Qt 5.15.2?</p>
</blockquote>
</aside>
<p>Yes, I use qt 5.15.2 from homebrew.</p>
<p>According to <a href="https://www.qt.io/blog/qt-roadmap-for-2021">the Qt roadmap</a> 1.15.3 will be commercial-only and there won’t be a 6.2 with all the features we need until around September and it’s not clear if this will solve these issues or maybe introduce new ones.  And of course macOS may introduce new features that break behavior.</p>
<p>I know it’s not realistic for everyone but I actually use my mac for general work but about half the time I’m using Slicer on a remote desktop to a linux VM where everything works nicely.</p>

---

## Post #17 by @lassoan (2021-07-14 20:57 UTC)

<aside class="quote no-group" data-username="pieper" data-post="16" data-topic="18624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I know it’s not realistic for everyone but I actually use my mac for general work but about half the time I’m using Slicer on a remote desktop to a linux VM where everything works nicely.</p>
</blockquote>
</aside>
<p>I would add that everything works well on Windows, too.</p>
<p>It seems that macOS keeps breaking things more quickly than Qt developers would be able/care to fix. And this is just the window management. It will take even more effort to maintain compatibility with macOS over the coming years due to deprecation of OpenGL and Intel CPUs. Also, Apple is not participating in other standardization efforts, such as OpenXR for virtual/augmented reality. Overall, Apple seem to want to seize complete control at all level, which is really good for them and allows them to do some optimizations and simplifications in their hardware and software stack, but it makes their products increasingly problematic platforms for open, cross-platform applications.</p>

---

## Post #18 by @muratmaga (2021-07-14 21:19 UTC)

<p>Any idea what the breakdown of download is for Windows/Mac/Linux ? I know it is a crude approximation of actual usage by platform. But at least it would give some indication…</p>

---

## Post #19 by @pieper (2021-07-14 21:21 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="18" data-topic="18624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Any idea what the breakdown of download is for Windows/Mac/Linux ?</p>
</blockquote>
</aside>
<p><a href="https://download.slicer.org/download-stats/" class="onebox" target="_blank" rel="noopener">https://download.slicer.org/download-stats/</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1b013c165311b6c48562ddd2fcff373ba5e3841.png" alt="image" data-base62-sha1="n4m7dcKoIsXGwzLmxjuAD76Lol3" width="324" height="160"></p>
<p>We certainly don’t want to give up on mac, but the points Andras makes are valid.</p>

---

## Post #20 by @mohammed_alshakhas (2021-07-15 17:38 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>  <a class="mention" href="/u/muratmaga">@muratmaga</a> for an average user like me who depends macos environment, it is semi impossible to shift for windows . i gave up the idea of many softwares for this reason ,<br>
plus<br>
with mac im using much less powerful machines than i would need with windows  .  im writing from my 10 years old mac machine which i use for slicer without any issues .<br>
id say that if it wasn’t mac compatible i  would have lost the chance to work on slicer<br>
i love slicer and i hope that continue using on macOS .</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00ecdf0a94f526b84672140d352eb7c18b012fff.png" alt="Screen Shot 2021-07-15 at 20.31.03" data-base62-sha1="8buEbc0vVqKRvknXdpkJ7Q3Ont" width="571" height="308"></p>

---

## Post #21 by @pieper (2021-07-15 18:08 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks for the <code>exec()</code> suggestion, it seems to work.  See <a href="https://github.com/commontk/CTK/pull/983">this PR</a>.</p>
<p><a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a> It’s great that a 10 year old mac is still working well for you.  It’s also much appreciated that you took the time to report this issue so we could address it.  It happens that I’m the only Slicer core developer who uses a mac for my day to day work and I didn’t happen to see the issue.</p>
<p>On the bigger picture of supporting Apple in the future, we’ll certainly try but there could very well be issues that are out of our control.</p>

---

## Post #22 by @hherhold (2021-07-15 18:27 UTC)

<p>Just to echo <a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a> here, I’m Mac-based as well for all my slicer work. I would very much like to see slicer continue as a full cross-platform application. While I’ve only been able to contribute by fixing a small bug here or there, I’ll try to help out where I can.</p>

---

## Post #23 by @lassoan (2021-07-15 19:12 UTC)

<p>Slicer will not be an outlier. If Apple makes open-source/cross-platform 3D application development practically impossible then not just Slicer but a whole lot of other applications will disappear from Apple devices, so many people will have to switch to Windows or Linux. But this is highly unlikely to happen. Apple will try to push everyone towards adopting their proprietary technologies, but just not that hard to make developers leave their platforms in large numbers.</p>
<p>Most probably cross-platform software will be just a bit more glitchy and more limited on macOS compared to other platforms, and you may not have access to features, such as GPU-accelerated processing and deep learning, augmented/virtual reality, etc. for a few years. I would expect then bridging toolkits will appear that can translate open interfaces to proprietary Apple technology and/or Apple will start support some open interfaces.</p>

---
