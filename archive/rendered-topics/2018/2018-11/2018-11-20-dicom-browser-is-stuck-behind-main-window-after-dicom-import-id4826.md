# DICOM browser is stuck behind main window after DICOM import

**Topic ID**: 4826
**Date**: 2018-11-20
**URL**: https://discourse.slicer.org/t/dicom-browser-is-stuck-behind-main-window-after-dicom-import/4826

---

## Post #1 by @mag (2018-11-20 21:49 UTC)

<p>I think the DICOM browser in the new stable release for Mac has a very little issue. When I import a DICOM, after it finishes it closes automatically (before it would stay open and let me load the series). After the browser closes, the DICOM  module keeps working but not the browser button: if I click on it to reopen the browser, nothing happens. However if I go to another module and then come back to DICOM module, the browser button works alright. Is anybody having the same funny behaviour? The nightly built from the 01/11/18 also does the same thing but the previous stable release doesn’t.</p>

---

## Post #2 by @fedorov (2018-11-20 22:21 UTC)

<p>It does not close, it is just “hiding” behind the main window. Try to move around your Slicer main window, then you should be able to find the DICOM Browser window. It is quite annoying and counter-intuitive.</p>

---

## Post #3 by @mag (2018-11-20 22:33 UTC)

<p>Oh wow that’s funny, I would never have noticed, cause it doesn’t even show in the dock  <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=6" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"><br>
Indeed, it’s very annoying…I think I’ll just revert to the old version. Thank you!</p>

---

## Post #4 by @fedorov (2018-11-20 22:34 UTC)

<aside class="quote no-group" data-username="mag" data-post="3" data-topic="4826">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/58f4c7/48.png" class="avatar"> mag:</div>
<blockquote>
<p>I think I’ll just revert to the old version.</p>
</blockquote>
</aside>
<p>Wow! I would never think it is that bad for a user … I don’t know how difficult/feasible it would be to fix this. I thought I raised this issue a while ago, but I cannot find the thread.</p>

---

## Post #5 by @lassoan (2018-11-20 22:39 UTC)

<p>If you only have a single monitor then it is better to automatically hide the DICOM browser window after loading by unchecking “Browser persistent” checkbox. Do you mean that the DICOM browser window is not hidden after loading even if “Browser persistent” is unchecked?</p>

---

## Post #6 by @fedorov (2018-11-20 22:41 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> on mac the DICOM Browser window is hiding behind the main application window <em>after the Import</em> operation. This is not about hiding it after load.</p>

---

## Post #7 by @pieper (2018-11-20 23:20 UTC)

<p>Yes, I saw this today with Sonia too - it seems to be an issue with Qt5 on mac.</p>

---

## Post #8 by @lassoan (2018-11-20 23:21 UTC)

<p>I see, thanks for the clarification. I cannot fix this, as I cannot reproduce this on Windows, but probably the DICOM browser window just need to raised to the top by calling <code>widget.raise_()</code> or something similar.</p>

---

## Post #9 by @jdx-john (2018-11-21 13:55 UTC)

<p>I think this sounds the same issue we’ve seen in our Slicer application <a class="mention" href="/u/lassoan">@lassoan</a>. If so, it was a problem since a year ago for us which pre-dates Qt5?</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>  you looked on our side, did you raise a bug or anything?</p>

---

## Post #10 by @mag (2018-11-21 18:09 UTC)

<p>It’s not bad but the old version has everything I need and does not have this bug so I’d rather use that until I’ve finished importing all my dataset <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #11 by @pieper (2018-11-21 19:24 UTC)

<p>It’s funny I cannot reproduce this with my local build or Slicer 4.10 on my desktop or 4.10 on my laptop mac (running 10.13.6 High Sierra and 10.14 Mojave respectively).</p>
<p>In non-persistent mode the DICOM browser closes after loading.  In persistent mode it stays on top of the slicer app window.</p>

---

## Post #12 by @mag (2018-11-21 20:12 UTC)

<p>I’ve just tried again on my work desktop (running 10.13.6 High Sierra) and after importing a new DICOM series the browser hides behind the main window independently on whether persistent mode is selected or not. This happens with Slicer 4.11.0-2018-11-0, Slicer 4.10.0 and Slicer 4.9.0-2018-10-16 but not in Slicer 4.8.1-stable. I don’t know about the latest nightly because I would need admin approval to install it and can not do it right now.</p>
<p>But that’s ok, when I raised the issue I thought the browser button was stuck, I hadn’t realized the browser was just hidden (sorry for that, I could have looked better). That’s not a big issue, I’ll just do all the imports at once or use the old version to avoid playing hide and seek with the DICOM browser.</p>

---

## Post #13 by @pieper (2018-11-21 23:09 UTC)

<p>I see - yes, this happens when the directory import is complete, not on loading the data (sorry, read the issue wrong).  It’s probably because the confirm dialog is parented to the main app window so main window is raised when the dialog is closed.  Probably the directory selector and the confirm dialog should be parented to the dicom browser window instead.</p>

---

## Post #14 by @lassoan (2018-11-23 04:01 UTC)

<p>We’ve been testing this <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> and found that the problem may be the use of modal popups. These popups are quite annoying anyway, so we are thinking about replacing them by widgets in the DICOM browser window.</p>
<p>We could move the progress bar from a popup to the bottom of the DICOM browser window and disable the rest of the window. We could probably even run indexing in a background thread (SQLite allows concurrent database access from multiple threads) and so indexing would not block the GUI. The result popup could be replaced by a textbox/button showing summary and by clicking on it we could show more detailed information.</p>

---

## Post #15 by @Sunderlandkyl (2018-11-23 05:34 UTC)

<p>Here is a quick mockup of the proposed layout:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b06d1a8fae74929b1b31d37518e66be48d9dd878.png" data-download-href="/uploads/short-url/paJMT3pfew3SzmRtkzRsdlSkOSY.png?dl=1" title="DicomProgressBarv01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b06d1a8fae74929b1b31d37518e66be48d9dd878.png" alt="DicomProgressBarv01" data-base62-sha1="paJMT3pfew3SzmRtkzRsdlSkOSY" width="650" height="500" data-dominant-color="F2F0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DicomProgressBarv01</span><span class="informations">803×617 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The label beside the progress bar would provide a broad indication of the current operation/status (import in progress, import completed, etc.). Clicking the details button would provide the user with additional info (Number of patients imported, verbose error messages, etc.)</p>
<p>Any feedback or thoughts?</p>

---

## Post #16 by @lassoan (2018-11-23 12:14 UTC)

<p>Thank you, this looks good to me!</p>
<p>We also need a Cancel button. It could be next to the progress bar or in the details window (that is shown when Details button is clicked). Probably the details window would be a better place because in the future we could add a cancel button for each task (and tasks could include network tasks, such as push/pull images to/from a server).</p>

---

## Post #17 by @pieper (2018-11-23 12:50 UTC)

<p>Note that we tried threading the indexing in the past and had some mystery crashes.</p>
<p>I’m sure it’s solvable, but probably best to fix the model dialog issue first and then do threading as a separate experiment.</p>
<p>As the <a href="http://www.sqlite.org/faq.html#q6">SQLite FAQ says</a>:</p>
<blockquote>
<p>“Threads are evil. Avoid them.”</p>
</blockquote>
<p>See this issue for more background:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/commontk/CTK/issues/292">
  <header class="source">

      <a href="https://github.com/commontk/CTK/issues/292" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/issues/292" target="_blank" rel="noopener">ctkDICOMIndexer and multiple threads</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2013-01-16" data-time="20:54:09" data-timezone="UTC">08:54PM - 16 Jan 13 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2013-01-17" data-time="19:25:37" data-timezone="UTC">07:25PM - 17 Jan 13 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          DICOM
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">In the summer of 2012 we started using the QtConcurrent [1] approach in the inde<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">xer for multithreading [2].  While this seems to work fine in the ctkDICOM test application, when importing large data in slicer we get random crashes like [3] and [4].

It seems that Qt does not support accessing one database connection from multiple threads [5] which is what we do when each functor is using the same ctkDICOMDatabase instance.  The Qt documentation suggests looking at the particular db interface for further guidance.

The sqlite faq is unambiguous about their opinion of threads [6].  ;)  Although they do say that threading could work in some situations [7].

It seems the safest thing is to remove the thread code and go back to something in the main event loop, perhaps with a timer so that the GUI remains responsive.

[1] http://doc.qt.digia.com/qt/qtconcurrentfilter.html

[2] https://github.com/commontk/CTK/commit/8daad7583115e59df90e43cd77fb0a9d665f657e

[3] http://na-mic.org/Bug/view.php?id=2839

[4] http://na-mic.org/Bug/view.php?id=2871

[5] http://qt-project.org/doc/qt-4.8/threads-modules.html#threads-and-the-sql-module

[6] http://www.sqlite.org/faq.html#q6

[7] http://www.sqlite.org/threadsafe.html</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #18 by @lassoan (2018-11-23 16:39 UTC)

<p>Background indexing will be done in a separate development step for sure.</p>
<p>If threading is not stable then we may do it in a separate process, in a CLI module. We already have all the necessary asynchronous execution features in place for CLIs (progress reporting, canceling, job queuing, etc.), so we would not need to develop new infrastructure.</p>

---

## Post #19 by @lassoan (2018-11-23 16:43 UTC)

<p>By the way, it seems that you’ve tried to use the same database connection in multiple threads, which I think is not allowed by default.</p>
<p>We could also change the indexer to collect all data in memory in a worker thread, and after every 50-100 files update the database from the main thread.</p>

---

## Post #20 by @Sunderlandkyl (2018-11-23 20:08 UTC)

<p>I’ve actually discovered something interesting.</p>
<ul>
<li>If you create a ctkDICOMBrowser from the python interactor, then import <strong>will not</strong> cause the issue</li>
<li>If you create a DICOM browser through DICOMWidget.py, then the browser <strong>will</strong> have the issue</li>
</ul>
<p>In that case, it seems to me that it might not be caused by the modal popups, but is instead caused by the rewiring of the browser widget that takes place in DICOMWidget.py.</p>
<p>To get a better idea of what’s going on, can someone explain to me why this widget reorganization is neccesary in DICOMDetailsBase.setup(): <a href="https://github.com/Slicer/Slicer/blob/8d765eab6445c277346f4c7248d9441dca4559dc/Modules/Scripted/DICOMLib/DICOMWidgets.py#L127-L343" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/8d765eab6445c277346f4c7248d9441dca4559dc/Modules/Scripted/DICOMLib/DICOMWidgets.py#L127-L343</a></p>

---

## Post #21 by @pieper (2018-11-24 19:06 UTC)

<p>I’d say that’s a bunch of legacy code and I’m sure there’s a better design - probably the whole widget could be made simpler to maintain and more usable if you are up for it.</p>

---

## Post #22 by @lassoan (2018-11-24 20:14 UTC)

<p>Development of DICOM module had been hindered by having widgets in CTK and therefore need to agree with MITK folks on design (and for example a few years ago they did not agree to store derived values in the database, only standard DICOM fields).</p>
<p>Since only Slicer developers contributed to the DICOM browser in the last few years and probably this will not change in the near future, I think we should be able to make changes that we need. If CTK users have the capability to update their applications according to non-backward compatible changes in CTK DICOM infrastructure then we can do the rework in CTK. If CTK users preferred keeping things as they are now, then we would need to fork CTK DICOM features in Slicer core. <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> how do you think we should manage this? How could we start a discussion with CTK community - by posting an issue on github?</p>

---

## Post #23 by @pieper (2018-11-24 20:50 UTC)

<p>Yes, if we are ready to take on a redesign of the widget we should contact Marco (he plans to be at project week in Las Palmas so we can coordinate there and/or before/after).  If it turns out we don’t have the same goals we can diverge and put a new browser either in CTK or Slicer directly.  We only need to share as much infrastructure as actually makes sense for our projects (which should only benefit - if it hinders we don’t need to do it).</p>

---

## Post #24 by @Sunderlandkyl (2018-12-05 20:12 UTC)

<p>After discussing this with <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/lassoan">@lassoan</a>, there is another way that we could organize the DICOM browser.</p>
<p>The DICOM browser widget could be opened in the central widget like is done in <strong><a href="https://github.com/jcfr/ShapePopulationViewer" rel="noopener nofollow ugc">ShapePopulationViewer</a></strong>, ex:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01c24311c5b150729fcf2cdb5e743427cf0b9d89.png" data-download-href="/uploads/short-url/fyGh5mYHqryGOvENMGiFq4O3wd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01c24311c5b150729fcf2cdb5e743427cf0b9d89_2_690x416.png" alt="image" data-base62-sha1="fyGh5mYHqryGOvENMGiFq4O3wd" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01c24311c5b150729fcf2cdb5e743427cf0b9d89_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01c24311c5b150729fcf2cdb5e743427cf0b9d89_2_1035x624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01c24311c5b150729fcf2cdb5e743427cf0b9d89_2_1380x832.png 2x" data-dominant-color="EFF0F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1160 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>We could still provide the option to use the pop-up window for applications/users that would prefer it.</p>
<p>In the longer term, it would be useful if we could re-organize and simplify the DICOM widget to minimize the modifications that are required in Slicer. Are there any modules that rely on the current structure of the DICOM popup?</p>

---

## Post #25 by @lassoan (2018-12-05 20:27 UTC)

<p>This is just a mockup to show where the browser would appear (in the view layout, as a one-up view). The final GUI will be improved - we can move menu actions at the top to the module panel on the left, etc.</p>

---

## Post #26 by @fedorov (2018-12-05 20:39 UTC)

<p>Overall, I very much like this approach. I do not know if anyone really needs to have DICOM browser in a separate window - I never use that functionality, and I am 100% sure no one likes the bug that triggered this conversation.</p>
<p>At some point <a class="mention" href="/u/che85">@che85</a> experimented with something like this in a context of a custom modile, and he ran into some issues, but I don’t recall the details now. Christian, can you comment, if you remember?</p>
<blockquote>
<p>Are there any modules that rely on the current structure of the DICOM popup?</p>
</blockquote>
<p>I don’t know if this is the right way to do things, but in some cases logic of the module is accessed via the popup widget, eg see <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/RSNAVisTutorial.py#L315-L323" class="inline-onebox">Slicer/Applications/SlicerApp/Testing/Python/RSNAVisTutorial.py at main · Slicer/Slicer · GitHub</a>. It is not exactly a dependency on the structure that you asked about, but probably something to be considered. I don’t know why this is the way logic of the module is accessed.</p>

---

## Post #27 by @ihnorton (2018-12-05 21:37 UTC)

<p>I’m not sure how the ShapePopulationViewer looks (not available for 4.10 on Mac), but is the idea to make the DICOM browser shown as a tab? (and allow switching back to the 3D view tab?). That sounds nice.</p>
<p>On the topic of the modal dialog, I think this issue is related (and several others attached to it): <a href="https://issues.slicer.org/view.php?id=1792" rel="nofollow noopener">https://issues.slicer.org/view.php?id=1792</a></p>

---

## Post #28 by @lassoan (2018-12-05 21:53 UTC)

<p>The DICOM browser will be shown in the view layout. We would add a one-up layout with the DICOM browser, but we could add define layouts that have slice and other usual views.</p>
<p>Switch using tabs: we could add a list of recent and/or favorite view layouts and switch between them using tabs or toolbar buttons.</p>

---

## Post #29 by @cpinter (2018-12-05 22:25 UTC)

<p>This is how ShapePopulationViewer looks:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/831b409e713ed9c603f2535834dbd9fce3a5b7d7.png" data-download-href="/uploads/short-url/iHOW4xkUU4kOQ8XJi546DjJiqs7.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831b409e713ed9c603f2535834dbd9fce3a5b7d7_2_690x382.png" alt="image" data-base62-sha1="iHOW4xkUU4kOQ8XJi546DjJiqs7" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831b409e713ed9c603f2535834dbd9fce3a5b7d7_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831b409e713ed9c603f2535834dbd9fce3a5b7d7_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/831b409e713ed9c603f2535834dbd9fce3a5b7d7_2_1380x764.png 2x" data-dominant-color="F9FAF8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1584×879 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The idea is that it defines a custom layout containing a custom widget. When entering the module, it remembers the current layout and switches to the custom one. When leaving the module, then it restores the previous layout. It’s nice because it fits into the layout logic without any hacking, and I also like module selection controlling it.</p>
<p>For the DICOM module, we could now have something meaningful in the module panel such as image preview, database directory selector, etc. If the user clicks the DCM button then it switches to the module as currently but the layout would be replaced by the DICOM browser custom layout. Then when the user wants to do something, they need to switch to another module, in which case they get back the viewers. We could also automatically switch to the Data module after successful loading to make the new data appear in both the data tree and the viewers.</p>

---

## Post #30 by @ihnorton (2018-12-06 03:05 UTC)

<p>I see. Thanks for the explanations. DICOM browsing is a very temporal/temporary interaction, so I think requiring to change layouts every time (even automatically) might feel heavy or inconsistent with the rest of the UI. Whereas the ShapePopulationViewer is still using the “main” area for data viewing (+some extra controls).</p>

---

## Post #31 by @che85 (2018-12-06 03:12 UTC)

<p>I am pretty sure that we fixed that in QuantitativeReporting but we never added the DICOM browser back into the module.</p>

---

## Post #32 by @che85 (2018-12-06 03:20 UTC)

<p>In QuantitativeReporting we added it directly in the module widget</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QuantitativeReporting.py#L176-L179">
  <header class="source">

      <a href="https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QuantitativeReporting.py#L176-L179" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QuantitativeReporting.py#L176-L179" target="_blank" rel="noopener nofollow ugc">QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QuantitativeReporting.py#L176-L179</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="176" style="counter-reset: li-counter 175 ;">
          <li>def enableReportButtons(self, enabled):</li>
          <li>  self.saveReportButton.enabled = enabled</li>
          <li>  self.completeReportButton.enabled = enabled</li>
          <li>  self.exportToHTMLButton.enabled = enabled</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and</p>
<p><a href="https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QRCustomizations/CustomDICOMDetailsWidget.py" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QRCustomizations/CustomDICOMDetailsWidget.py</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/254a2916503f3ba6c468fba8d345480455275a7c.png" data-download-href="/uploads/short-url/5jSynDWNWmL702E5DD1lYhj2Th2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/254a2916503f3ba6c468fba8d345480455275a7c_2_690x410.png" alt="image" data-base62-sha1="5jSynDWNWmL702E5DD1lYhj2Th2" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/254a2916503f3ba6c468fba8d345480455275a7c_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/254a2916503f3ba6c468fba8d345480455275a7c_2_1035x615.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/254a2916503f3ba6c468fba8d345480455275a7c_2_1380x820.png 2x" data-dominant-color="7E7E84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">4064×2418 776 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7181347f75099ad99d20cf33b757393922ab8abc.png" data-download-href="/uploads/short-url/gc6M27I7yYPoFtTzKMHRnRLDTY0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7181347f75099ad99d20cf33b757393922ab8abc_2_690x410.png" alt="image" data-base62-sha1="gc6M27I7yYPoFtTzKMHRnRLDTY0" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7181347f75099ad99d20cf33b757393922ab8abc_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7181347f75099ad99d20cf33b757393922ab8abc_2_1035x615.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7181347f75099ad99d20cf33b757393922ab8abc_2_1380x820.png 2x" data-dominant-color="F9F8F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">4064×2418 697 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So it’s a tab that once clicked hides the slice viewers and uses the whole width of the Slicer window. Once data is loaded the user can return to the previous step where the slice viewers and the module widget width should get restored to its original state.</p>
<p>NOTE: I think there was an issue with resizing the width of the module widget after trying to restore the original state.</p>

---

## Post #33 by @lassoan (2018-12-06 03:58 UTC)

<p>The two main options seems to be A. switching layouts, B. temporarily hide the central widget (view layout). I don’t really see any advantages option B. but there seems to be a couple of disadvantages:</p>
<ul>
<li>Not having a central widget may not be a valid application main window layout in Qt (<a href="https://stackoverflow.com/questions/3531031/qmainwindow-with-only-qdockwidgets-and-no-central-widget" rel="nofollow noopener">https://stackoverflow.com/questions/3531031/qmainwindow-with-only-qdockwidgets-and-no-central-widget</a>)</li>
<li>We could not show the DICOM browser while in another module (while if the DICOM browser is in the view layout then the user could switch to that layout and back - without exiting from the current module)</li>
<li>We would lose 3-4 lines across the whole screen due to the Slicer logo if we  just extended the module panel to full window width.</li>
<li>In the long term, we’ll probably allow creating view layouts more dynamically (similarly to ParaView) and will support multiple monitors. If we manage DICOM browser outside of the view layout then the DICOM module will not benefit from this infrastructure.</li>
<li>We cannot easily have combined view layouts (e.g., show a DICOM browser with a slice or 3D view). I don’t know how useful this would be now, but maybe when we have dynamic/multi-monitor support then this will be more important.</li>
</ul>

---

## Post #35 by @cpinter (2018-12-06 15:17 UTC)

<p>[Update: I’m not sure where did <a class="mention" href="/u/fedorov">@fedorov</a>’s comment go about the browser in the module panel but this was an answer to that]</p>
<p>I like this too, except that then where do the options go that are currently occupying this space? Also we’re losing the opportunity to improve the module panel to include actually useful supplementary information like thumbnails etc.</p>

---

## Post #37 by @fedorov (2018-12-06 15:57 UTC)

<p>Sorry for the mishap …</p>
<p>Here’s the proposed mockup again</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/387ba22676b20d50bf87b6209f38a6906dcc6120.png" data-download-href="/uploads/short-url/83FCxKaryHtbeQGkyuzadTLVFcc.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387ba22676b20d50bf87b6209f38a6906dcc6120_2_689x386.png" alt="image" data-base62-sha1="83FCxKaryHtbeQGkyuzadTLVFcc" width="689" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387ba22676b20d50bf87b6209f38a6906dcc6120_2_689x386.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387ba22676b20d50bf87b6209f38a6906dcc6120_2_1033x579.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/387ba22676b20d50bf87b6209f38a6906dcc6120.png 2x" data-dominant-color="A3A5B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1308×733 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="cpinter" data-post="35" data-topic="4826">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>where do the options go that are currently occupying this space?</p>
</blockquote>
</aside>
<p>If you are talking about the content below, I would say they can easily go into some log or advanced view. I personally never use the “Recent activity” list, and start listener is a quite advanced option.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b919257fc9f95c5271d09fcaf5612d614443df7.png" data-download-href="/uploads/short-url/flAYsyt0YCYavatNLRpYHQgLBQ3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b919257fc9f95c5271d09fcaf5612d614443df7_2_462x500.png" alt="image" data-base62-sha1="flAYsyt0YCYavatNLRpYHQgLBQ3" width="462" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b919257fc9f95c5271d09fcaf5612d614443df7_2_462x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b919257fc9f95c5271d09fcaf5612d614443df7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b919257fc9f95c5271d09fcaf5612d614443df7.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">655×708 60.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="cpinter" data-post="35" data-topic="4826">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Also we’re losing the opportunity to improve the module panel to include actually useful supplementary information like thumbnails etc.</p>
</blockquote>
</aside>
<p>Not losing, just making it available only in the full view. I am just thinking about the 80/20 rule. In my experience, the abbreviated view would address most of the uses of the DICOM module. Just my 2c. It would be great if other users share their perspective so we try to get a more representative sample.</p>

---

## Post #38 by @Sunderlandkyl (2018-12-13 23:44 UTC)

<p>I’ve created a pull request that integrates the DICOM browser into a new view and layout.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/1061">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/1061" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/1061" target="_blank" rel="noopener nofollow ugc">resolution of Slices in 3D view is suboptimal</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:37:00" data-timezone="UTC">10:37PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:37:00" data-timezone="UTC">10:37PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener nofollow ugc">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=1061). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I’d appreciate everyone’s thoughts/comments.</p>

---
