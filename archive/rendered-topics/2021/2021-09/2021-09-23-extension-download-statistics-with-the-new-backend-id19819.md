# Extension download statistics with the new backend

**Topic ID**: 19819
**Date**: 2021-09-23
**URL**: https://discourse.slicer.org/t/extension-download-statistics-with-the-new-backend/19819

---

## Post #1 by @muratmaga (2021-09-23 05:11 UTC)

<p>I tried to download the extension download statistics using the stable, and got the error below. This used to work, so I assume this is related to change in extension server.</p>
<p>Going forward, what is the plan on obtaining extension stats?</p>
<pre><code class="lang-auto">Switch to module:  "ExtensionStats"
Traceback (most recent call last):
  File "C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 579, in getExtensionSlicerRevisionAndDownloads
    item_rev_downloads[itemid] = [self.getItemById(url, itemid)['download'], slicerrevision]
  File "C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 553, in getItemById
    return self._call_midas_url(url, data)
  File "C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 515, in _call_midas_url
    response_data = response_dict['data']
KeyError: 'data'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 153, in onApplyButton
    release_downloads = self.logic.getExtensionDownloadStats(extensionName)
  File "C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 645, in getExtensionDownloadStats
    rev_downloads = self.getExtensionSlicerRevisionAndDownloads(url, extensionName)
  File "C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/DeveloperToolsForExtensions/lib/Slicer-4.11/qt-scripted-modules/ExtensionStats.py", line 584, in getExtensionSlicerRevisionAndDownloads
    self.setStatus("Retrieving package info {0}/{1} for extension {2} - Error: {3} - ".format(idx+1, len(all_itemids), extensionName, str(e)))
UnboundLocalError: local variable 'e' referenced before assignment
</code></pre>

---

## Post #2 by @muratmaga (2021-09-23 18:23 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a><br>
To add to the report same thing is happening with the preview as well:</p>
<pre><code class="lang-auto">Switch to module:  "ExtensionStats"
Traceback (most recent call last):
  File "C:/Users/amaga/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-20/NA-MIC/Extensions-30230/DeveloperToolsForExtensions/lib/Slicer-4.13/qt-scripted-modules/ExtensionStats.py", line 579, in getExtensionSlicerRevisionAndDownloads
    item_rev_downloads[itemid] = [self.getItemById(url, itemid)['download'], slicerrevision]
  File "C:/Users/amaga/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-20/NA-MIC/Extensions-30230/DeveloperToolsForExtensions/lib/Slicer-4.13/qt-scripted-modules/ExtensionStats.py", line 553, in getItemById
    return self._call_midas_url(url, data)
  File "C:/Users/amaga/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-20/NA-MIC/Extensions-30230/DeveloperToolsForExtensions/lib/Slicer-4.13/qt-scripted-modules/ExtensionStats.py", line 515, in _call_midas_url
    response_data = response_dict['data']
KeyError: 'data'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/amaga/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-20/NA-MIC/Extensions-30230/DeveloperToolsForExtensions/lib/Slicer-4.13/qt-scripted-modules/ExtensionStats.py", line 153, in onApplyButton
    release_downloads = self.logic.getExtensionDownloadStats(extensionName)
  File "C:/Users/amaga/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-20/NA-MIC/Extensions-30230/DeveloperToolsForExtensions/lib/Slicer-4.13/qt-scripted-modules/ExtensionStats.py", line 645, in getExtensionDownloadStats
    rev_downloads = self.getExtensionSlicerRevisionAndDownloads(url, extensionName)
  File "C:/Users/amaga/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-20/NA-MIC/Extensions-30230/DeveloperToolsForExtensions/lib/Slicer-4.13/qt-scripted-modules/ExtensionStats.py", line 584, in getExtensionSlicerRevisionAndDownloads
    self.setStatus("Retrieving package info {0}/{1} for extension {2} - Error: {3} - ".format(idx+1, len(all_itemids), extensionName, str(e)))
UnboundLocalError: local variable 'e' referenced before assignment
</code></pre>

---

## Post #3 by @lassoan (2021-09-24 05:07 UTC)

<p>The Midas server does not exist anymore.</p>
<p>You can get download counts in a single json file from the new extensions server: <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705484" class="inline-onebox">SPKC</a></p>
<p>We also plan to develop a tool to get more detailed statistics from web server logs, which will work retrospectively, so no download statistics information will be lost.</p>

---

## Post #4 by @muratmaga (2021-09-24 05:24 UTC)

<p>Are the numbers in the JSONs counts since the new extension manager? They kind of look low (at least for SlicerMorph).</p>

---

## Post #5 by @muratmaga (2021-10-25 17:27 UTC)

<p>Is there a direct URL to obtain the JSON as a file?</p>
<p>The output cannot be saved, but only copy/pasted.</p>

---

## Post #6 by @lassoan (2021-10-26 03:44 UTC)

<p>I would be interested in this, too. It is quite inconvenient to copy-paste that long text.</p>
<p>Also, it would be important to get a snapshot of the last extension statistics of the old server (that is created by DeveloperToolsForExtensions).</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> can you help with these?</p>

---

## Post #7 by @jcfr (2021-10-26 14:41 UTC)

<p>Current stats can be retrieved using this REST end point:</p>
<p><a href="https://slicer-packages.kitware.com/api/v1#!/app/app_getDownloadStats">https://slicer-packages.kitware.com/api/v1#!/app/app_getDownloadStats</a></p>
<p>For example:</p>
<pre><code class="lang-auto">https://slicer-packages.kitware.com/api/v1/app/5f4474d0e1d8c75dfc705482/downloadstats
</code></pre>
<p>where <code>5f4474d0e1d8c75dfc705482</code> corresponds to the application id (aka <code>folderId</code> in Girder terminology):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f325f7d6b655f1599ae9dea7bd95a9490c124af.png" data-download-href="/uploads/short-url/mIjQaCooyfdhPqQ9e1s5ciR9JIb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f325f7d6b655f1599ae9dea7bd95a9490c124af_2_690x289.png" alt="image" data-base62-sha1="mIjQaCooyfdhPqQ9e1s5ciR9JIb" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f325f7d6b655f1599ae9dea7bd95a9490c124af_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f325f7d6b655f1599ae9dea7bd95a9490c124af_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f325f7d6b655f1599ae9dea7bd95a9490c124af_2_1380x578.png 2x" data-dominant-color="BEBEBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1850×776 83.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @muratmaga (2021-10-26 18:15 UTC)

<p>Thanks JC. I parsed the output from the link you provided and the numbers are very different from what I used to get out of Extension Download Statistics tool, even though it includes historical revisions (not just the 4.13 revisions) for SlicerMorph.</p>
<p>This is important for us, and I suspect other grant supported projects. Would it be possible to reconcile this with the older statistics?</p>

---

## Post #9 by @lassoan (2021-10-26 19:51 UTC)

<p>I’ve updated the ExtensionStats module in SlicerDeveloperToolsForExtensions:</p>
<ul>
<li>it retrieves download counts from Girder</li>
<li>it loads Midas statistics from a CSV file and adds it to the numbers provided by Girder</li>
</ul>
<p>The Midas statistics is collected in May 2021, therefore we miss about 3 months of downloads. If <a class="mention" href="/u/jcfr">@jcfr</a> can retrieve the latest snapshot from the old server and updates the <a href="https://github.com/Slicer/SlicerDeveloperToolsForExtensions/blob/master/ExtensionStats/Resources/ExtensionsDownloadStats-20210521.csv">Midas csv file</a> then we should have accurate download counts.</p>

---

## Post #10 by @lassoan (2021-10-26 19:55 UTC)

<p>By the way, getting full statistics on all extensions is much faster now. <strong>Using the old server it took 6-8 hours, now it takes about 2 seconds</strong>. The main difference is that the new server stores the statistics as a single file that can be retrieved using one query, while on Midas we had to submit thousands of queries (one for each revision of each extension).</p>

---

## Post #11 by @jcfr (2021-10-27 01:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="19819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If <a class="mention" href="/u/jcfr">@jcfr</a> can retrieve the latest snapshot from the old server and updates the <a href="https://github.com/Slicer/SlicerDeveloperToolsForExtensions/blob/master/ExtensionStats/Resources/ExtensionsDownloadStats-20210521.csv">Midas csv file </a> then we should have accurate download counts.</p>
</blockquote>
</aside>
<p>The script is currently running and I expect  it will complete in  few hours. I will then upload it to <a href="https://github.com/Slicer/SlicerDeveloperToolsForExtensions/tree/master/ExtensionStats/Resources">https://github.com/Slicer/SlicerDeveloperToolsForExtensions/tree/master/ExtensionStats/Resources</a></p>

---

## Post #12 by @jcfr (2021-10-27 16:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="19819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The Midas statistics is collected in May 2021, therefore we miss about 3 months of downloads.</p>
</blockquote>
</aside>
<p>Historical extension download stats have been published.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/SlicerDeveloperToolsForExtensions/pull/18">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerDeveloperToolsForExtensions/pull/18" target="_blank" rel="noopener">github.com/Slicer/SlicerDeveloperToolsForExtensions</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/SlicerDeveloperToolsForExtensions/pull/18" target="_blank" rel="noopener">ENH: Update baseline extension download stats from 2021.05.21 to 2021.10.27</a>
      </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jcfr:update-historical-extensions-download-stats</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-27" data-time="16:30:38" data-timezone="UTC">04:30PM - 27 Oct 21 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener">
            <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="1 commits changed 3 files with 177 additions and 2 deletions">
          <a href="https://github.com/Slicer/SlicerDeveloperToolsForExtensions/pull/18/files" target="_blank" rel="noopener">
            <span class="added">+177</span>
            <span class="removed">-2</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See https://discourse.slicer.org/t/extension-download-statistics-with-the-new-ba<span class="show-more-container"><a href="https://github.com/Slicer/SlicerDeveloperToolsForExtensions/pull/18" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ckend/19819</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #13 by @muratmaga (2021-10-27 17:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="19819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve updated the ExtensionStats module in SlicerDeveloperToolsForExtensions:</p>
</blockquote>
</aside>
<p>I works great and really fast, thank you Andras (and JC as well).</p>
<p>There is a minor issue that table copy doesn’t function</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/murat/AppData/Local/NA-MIC/Slicer 4.13.0-2021-10-26/NA-MIC/Extensions-30334/DeveloperToolsForExtensions/lib/Slicer-4.13/qt-scripted-modules/ExtensionStats.py", line 144, in copyTableToClipboard
    tableText += table.GetColumn(columnIndex).GetValue(rowIndex)
TypeError: must be str, not int
</code></pre>

---

## Post #14 by @lassoan (2021-10-27 21:22 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="19819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>There is a minor issue that table copy doesn’t function</p>
</blockquote>
</aside>
<p>Good catch. I’ve fixed it now.</p>

---
