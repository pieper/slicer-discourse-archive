# DCMQI extension: New linking error

**Topic ID**: 966
**Date**: 2017-08-29
**URL**: https://discourse.slicer.org/t/dcmqi-extension-new-linking-error/966

---

## Post #1 by @fedorov (2017-08-29 15:18 UTC)

<p>It looks like some of the commits done yesterday introduced a new linking error for one of our extensions:</p>
<p>/usr/bin/ld: cannot find -lITKFactoryRegistration</p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1087743" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1087743</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> we really need to finalize the set of binaries for the MICCAI tutorial on Sept 10, so this is quite urgent for us. Would it be possible to wait for a day or so until we have Slicer binaries for 3 platforms and all extensions we need, before moving on with all the VTK/Qt5 related upgrades?</p>

---

## Post #2 by @jcfr (2017-08-29 15:20 UTC)

<p>Nightly was fixed last night in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26314">r26314</a></p>
<p>Regarding, error reported <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1087743">here</a>. I have been working on fixing the extensions, I will have a look at this one.</p>

---

## Post #3 by @fedorov (2017-08-29 15:23 UTC)

<p>Thank you. It’s something new, I don’t recall seeing it before.</p>

---

## Post #4 by @jcfr (2017-08-29 22:10 UTC)

<p>Hi <a class="mention" href="/u/fedorov">@fedorov</a>,</p>
<p>I suspect the link error is due to the Slicer core build error that already been fixed.</p>
<p>Otherwise, here are three PRs fixing various issues with the DCMQI extensions.</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/QIICR/dcmqi/pull/298" target="_blank">github.com/QIICR/dcmqi</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/QIICR/dcmqi/pull/298" target="_blank">Fix setting of cxx standard</a>
    </h4>

    <div class="branches">
      <code>QIICR:master</code> ← <code>jcfr:fix-setting-of-cxx-standard</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2017-08-29" data-time="21:45:02" data-timezone="UTC">09:45PM - 29 Aug 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="3 commits changed 5 files with 37 additions and 4 deletions">
        <a href="https://github.com/QIICR/dcmqi/pull/298/files" target="_blank">
          <span class="added">+37</span>
          <span class="removed">-4</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/QIICR/dcmqi/pull/299" target="_blank">github.com/QIICR/dcmqi</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/QIICR/dcmqi/pull/299" target="_blank">Fix warnings</a>
    </h4>

    <div class="branches">
      <code>QIICR:master</code> ← <code>jcfr:fix-warnings</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2017-08-29" data-time="21:54:58" data-timezone="UTC">09:54PM - 29 Aug 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="2 commits changed 4 files with 22 additions and 21 deletions">
        <a href="https://github.com/QIICR/dcmqi/pull/299/files" target="_blank">
          <span class="added">+22</span>
          <span class="removed">-21</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/QIICR/dcmqi/pull/300" target="_blank">github.com/QIICR/dcmqi</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/QIICR/dcmqi/pull/300" target="_blank">cmake: Fix forcebuild step</a>
    </h4>

    <div class="branches">
      <code>QIICR:master</code> ← <code>jcfr:fix-forcebuild-step</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2017-08-29" data-time="22:08:00" data-timezone="UTC">10:08PM - 29 Aug 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 2 additions and 2 deletions">
        <a href="https://github.com/QIICR/dcmqi/pull/300/files" target="_blank">
          <span class="added">+2</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @fedorov (2017-08-30 01:15 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a>! Fingers crossed for the dashboard tomorrow!</p>

---

## Post #6 by @jcfr (2017-08-30 11:34 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>,  look like DCMQI was successfully build and packages on windows and linux. See <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-08-30&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=DCMQI">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2017-08-30&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=DCMQI</a></p>
<p>Still waiting on macOS</p>

---

## Post #7 by @fedorov (2017-08-30 19:55 UTC)

<p>Thanks, I am checking it all now.</p>
<p>Unfortunately, there was a new error in Slicer core, so I again have to wait for the next nightly … For now I will replace the affected file manually, and see if everything else is working as expected - I see <a class="mention" href="/u/lassoan">@lassoan</a> commit that mentions a problem in DataProbe.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:\Program Files\Slicer 4.7.0-2017-08-29\lib\Slicer-4.7\qt-scripted-modules\DataProbeLib\SliceViewAnnotations.py", line 432, in updateViewAnnotations
    self.makeAnnotationText(caller)
  File "C:\Program Files\Slicer 4.7.0-2017-08-29\lib\Slicer-4.7\qt-scripted-modules\DataProbeLib\SliceViewAnnotations.py", line 610, in makeAnnotationText
    self.makeDicomAnnotation(uid,None,sliceViewName)
  File "C:\Program Files\Slicer 4.7.0-2017-08-29\lib\Slicer-4.7\qt-scripted-modules\DataProbeLib\SliceViewAnnotations.py", line 715, in makeDicomAnnotation
    dicomDic = self.extractDICOMValues(uid)
  File "C:\Program Files\Slicer 4.7.0-2017-08-29\lib\Slicer-4.7\qt-scripted-modules\DataProbeLib\SliceViewAnnotations.py", line 856, in extractDICOMValues
    self.extractedDICOMValuesCache.pop_item(last=False)
AttributeError: 'OrderedDict' object has no attribute 'pop_item'
</code></pre>

---

## Post #8 by @lassoan (2017-08-30 20:08 UTC)

<p>Yes, I’ve committed a fix for this error already. Tomorrow’s nightly build should not have this error.</p>

---

## Post #9 by @fedorov (2017-08-30 22:16 UTC)

<p>The current error doesn’t see to affect the functionality of the relevant part of the workflow that we need for the tutorial, so I might just use the today’s set of items, to make things easier.</p>

---

## Post #10 by @lassoan (2017-08-30 23:18 UTC)

<p>I think the only effect of the error is that slice view annotations (patient name, etc. in the corner of slice views) are not displayed.</p>

---
