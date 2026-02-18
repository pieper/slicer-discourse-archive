# Error running Elastix

**Topic ID**: 33735
**Date**: 2024-01-11
**URL**: https://discourse.slicer.org/t/error-running-elastix/33735

---

## Post #1 by @xiaoshideshun (2024-01-11 16:22 UTC)

<p>There is a bug in the registration module. I don’t know how to deal with it. Please give me some advice.</p>
<details>
<summary>
Original text in Chinese</summary>
<p>配准模块出现bug，不知道如何处理，请各位大佬支个招</p>
</details>
<p>Traceback (most recent call last):<br>
File “D:\Slicer\Slicer 5.2.2\bin\Python\slicer\util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “D:/Slicer/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerElastix/lib/Slicer-5.2/qt-scripted-modules/Elastix.py”, line 241, in onApplyButton<br>
self.logic.registerVolumesUsingParameterNode(self._parameterNode)<br>
File “D:/Slicer/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerElastix/lib/Slicer-5.2/qt-scripted-modules/Elastix.py”, line 518, in registerVolumesUsingParameterNode<br>
self.registerVolumes(<br>
File “D:/Slicer/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerElastix/lib/Slicer-5.2/qt-scripted-modules/Elastix.py”, line 564, in registerVolumes<br>
self.logProcessOutput(elastixProcess)<br>
File “D:/Slicer/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerElastix/lib/Slicer-5.2/qt-scripted-modules/Elastix.py”, line 499, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, “elastix”)<br>
subprocess.CalledProcessError: Command ‘elastix’ returned non-zero exit status 4294967294.</p>

---

## Post #2 by @lassoan (2024-01-11 17:14 UTC)

<p>Thank you for reporting. The issue is already tracked here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/lassoan/SlicerElastix/issues/44">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerElastix/issues/44" target="_blank" rel="noopener">github.com/lassoan/SlicerElastix</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerElastix/issues/44" target="_blank" rel="noopener">Failed to compute results.  Command 'elastix' died with &lt;Signals.SIGABRT: 6&gt;.</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-10-04" data-time="15:14:42" data-timezone="UTC">03:14PM - 04 Oct 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/Ox1deL" target="_blank" rel="noopener">
          <img alt="Ox1deL" src="https://avatars.githubusercontent.com/u/146970394?v=4" class="onebox-avatar-inline" width="20" height="20">
          Ox1deL
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Have this issue on macbook air 15inch M2 (Macos 14.0). Please Help!

Details:
<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">
`Traceback (most recent call last):
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3146, in tryWithErrorDisplay
yield
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 241, in onApplyButton
self.logic.registerVolumesUsingParameterNode(self._parameterNode)
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 518, in registerVolumesUsingParameterNode
self.registerVolumes(
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 564, in registerVolumes
self.logProcessOutput(elastixProcess)
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 499, in logProcessOutput
raise subprocess.CalledProcessError(return_code, “elastix”)
subprocess.CalledProcessError: Command ‘elastix’ died with &lt;Signals.SIGABRT: 6&gt;.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Note for the future: Since we don’t have automatic translation available on this forum yet, if you want to use a different language than English, please use an automatic translation service (there are dozens of free services) and use that text in your post. If you want, in addition to the English translation you can also include the original text like this:</p>
<pre><code class="lang-auto">[details="Original text in Chinese"]
This is the text in your native language. The section will be collapsed by default and readers can click on it to view it.
[/details]
</code></pre>

---
