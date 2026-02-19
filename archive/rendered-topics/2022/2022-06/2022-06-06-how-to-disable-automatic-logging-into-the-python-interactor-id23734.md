---
topic_id: 23734
title: "How To Disable Automatic Logging Into The Python Interactor"
date: 2022-06-06
url: https://discourse.slicer.org/t/23734
---

# How to disable automatic logging into the Python Interactor?

**Topic ID**: 23734
**Date**: 2022-06-06
**URL**: https://discourse.slicer.org/t/how-to-disable-automatic-logging-into-the-python-interactor/23734

---

## Post #1 by @CsatiZoltan (2022-06-06 13:26 UTC)

<p>My intention is to</p>
<ul>
<li>log into a file in great detail and verbose formatting (timestamp, logger name, etc.).</li>
<li>log into the Python Interactor in less verbose mode (less verbose formatting, only higher logging levels, etc.).</li>
</ul>
<p>This can be achieved by defining two handlers in the <em>logging</em> module of Python: a <strong>FileHandler</strong> and a <strong>StreamHandler</strong>. I tested logging into a file; it works as intended outside 3D Slicer. Before adding the possibility of logging into the console, I tried it out in 3D Slicer.</p>
<p>I noticed that my INFO-level messages automatically appear in the Python Interactor, even though I only log into a file. This is not the intended behaviour for me as</p>
<ul>
<li>I don’t want my logs appearing automatically in the Python Interactor.</li>
<li>I will define my own formatting to be shown in the Python Interactor using a <strong>StreamHandler</strong> object.</li>
</ul>
<p>It seems that the logs I send to the file are automatically redirected to the Python Interactor, filtered (DEBUG level messages are not shown for instance) and reformatted (keeps the message only) by Slicer. How can I switch this behaviour off?</p>
<p>I also noted that my logs appear in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog" rel="noopener nofollow ugc"><em>Error Log</em></a> window too (this time, the level is indicated as well). It is less of a problem for me, although, if possible, I would like to switch off the automatic redirection here as well.</p>
<p>What I want to achieve:</p>
<ul>
<li>my logging into a file (using <strong>FileHandler</strong>) is not shown in the Python Interactor (preferably neither in the <em>Error Log</em> window)</li>
<li>my logs with a <strong>StreamHandler</strong> are shown in the Python Interactor.</li>
</ul>

---

## Post #2 by @CsatiZoltan (2022-06-07 16:19 UTC)

<p>In the <em>Error Log</em>, I see that each logging to the file results in two log events in Slicer. It demonstrates that the above-mentioned redirection happens.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d9859683d8498d526afadfc99831b553ab633b5.png" alt="SlicerLog" data-base62-sha1="8MTx0KxGr2GtTxUA3dFjYsxfi7z" width="470" height="57"></p>

---

## Post #3 by @jamesobutler (2022-06-07 16:29 UTC)

<p>Related to some of this double logging I have work-in-progress PRs from awhile ago that I haven’t returned to, but there was a lot of discussion on them on improved logging.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5156">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5156" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5156" target="_blank" rel="noopener nofollow ugc">BUG: Fix duplicate python logging messages in the log for regular users</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:stop-double-logging-2</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-08-30" data-time="22:04:39" data-timezone="UTC">10:04PM - 30 Aug 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="2 commits changed 1 files with 13 additions and 12 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5156/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+13</span>
          <span class="removed">-12</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The motivation of this change is to improve user experience when viewing the Err<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5156" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">or Log Dialog and the slicer log as seen in the Report A Bug Dialog.  When there are, for example, 3 errors and 3 warnings, the user will see 3 errors and 3 warnings.  This is instead of 6 errors and 6 warnings where half were indicated from python and the other half were indicated from the stream.

This proposed change only shows python logging output in the console stream while in Developer Mode. For regular users not in developer mode they will no longer see double python logging (one from python and one from the stream).  

Developers will still have the double logging, but this appears to be desired behavior as they want knowledge of everything from the console stream in addition to everything from the python source.  The following code below indicates a method to prevent the double logging, but as it says, it would remove the line that includes the log file name and line number which is arguably the more important of the double logged messages.
https://github.com/Slicer/Slicer/blob/03113368de2e2afac71ade15ba0058b5e78dc39d/Base/Python/slicer/slicerqt.py#L72-L74

### Developer Mode:
```
[DEBUG][Qt] 27.08.2020 22:56:22 [] (unknown:0) - Switch to module:  "ScreenCapture"
[INFO][Python] 27.08.2020 22:56:25 [Python] (C:/Users/james/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-26/bin/../lib/Slicer-4.11/qt-scripted-modules/ScreenCapture.py:805) - Write C:\Users\james\Documents\SlicerCapture\image_00004.png
[INFO][Stream] 27.08.2020 22:56:25 [] (unknown:0) - Write C:\Users\james\Documents\SlicerCapture\image_00004.png
```
![image](https://user-images.githubusercontent.com/15837524/91516864-8a4bb580-e8ba-11ea-9903-aee2ff855633.png)

### Regular Users:
```
[DEBUG][Qt] 27.08.2020 23:13:22 [] (unknown:0) - Switch to module:  "ScreenCapture"
[INFO][Python] 27.08.2020 23:13:25 [Python] (C:/Users/james/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-26/bin/../lib/Slicer-4.11/qt-scripted-modules/ScreenCapture.py:805) - Write C:\Users\james\Documents\SlicerCapture\image_00005.png
```
![image](https://user-images.githubusercontent.com/15837524/91517194-3ee5d700-e8bb-11ea-8de5-20def1018c60.png)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5176">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5176" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5176" target="_blank" rel="noopener nofollow ugc">Logging improvements</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:logging-improvements</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-09-06" data-time="22:14:06" data-timezone="UTC">10:14PM - 06 Sep 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="7 commits changed 12 files with 150 additions and 74 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5176/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+150</span>
          <span class="removed">-74</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This would supersede https://github.com/Slicer/Slicer/pull/5156 and the changes <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5176" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">proposed here are based on discussions from that PR.

Requires changes in https://github.com/commontk/CTK/pull/928 where there are changes such as:

- a console mode button which allows viewing the log not in table format, but just simple text format. This is supported by selecting all fields when hiding the table. When hiding the table you can still use the filter buttons to view all errors in the simple text format as well.
- supporting colored text in the description column and full description fields. Warning (orange), Error and Critical (red)

- The ctkErrorLogWidget table view option is shown by default instead of the "Console Mode" option being in the checked state.

![image](https://user-images.githubusercontent.com/15837524/92498868-259d2e80-f1c9-11ea-9966-eeac289763c9.png)

- The error log toolbutton in the status bar now has an icon that reflects the highest logged level state since viewing the log widget.
- The error log can now be docked just like the python console and is by default in the bottom area.  There is a grabber tool between the python console and error log that allows resizing the two if both are shown.
- logging is no longer shown in the python console, but in the log messages area.  If someone wants to add a consoleInfoHandler again, they can add that in code.
- ~~The log text in the ErrorReport Dialog area is no longer editable. I've made it read-only as I don't think it was intended to be editable there.~~ See 7e6a62dccd1b1f17fdb0b8e2946a75286af6d71b
- The log table and log description error are both scrolled to the bottom upon showing the error log. It also scrolls upon adding of a new entry.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @CsatiZoltan (2022-06-08 10:17 UTC)

<p>Thank you for the PR links, good to see that I am not the only one annoyed by the double logging. Is this improvement still on the table for a future Slicer release?</p>

---

## Post #5 by @jamesobutler (2022-06-08 11:58 UTC)

<p>Yeah improvement in that area is still possible, but it’s not currently in a specific Slicer GitHub milestone. For that specific work I did it in my personal free time so when I have some more of it I may pick it back up again.</p>

---

## Post #6 by @jamesobutler (2022-10-28 21:19 UTC)

<p>To follow up on this thread, please see the following thread for an update about python logging</p>
<aside class="quote quote-modified" data-post="1" data-topic="25739">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-feature-python-console-displays-more-log-messages/25739">New feature: Python console displays more log messages</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Until now, the Python console only displayed Python outputs and Python log messages. Therefore, if a Python command executed a VTK method and that VTK method logged an error or warning, it was not immediately visible for the developer (the developer had to notice the change in the log icon, click on it, and scroll down to see the new message). 
In latest Slicer Preview Release (Slicer 5.1.0-2022-10-15 and later), the Python console displays log messages from all sources - Python, Qt, VTK, ITK. 
F…
  </blockquote>
</aside>


---
