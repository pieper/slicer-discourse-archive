# Command 'elastix' died with <Signals.SIGABRT: 6>.

**Topic ID**: 32970
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/command-elastix-died-with-signals-sigabrt-6/32970

---

## Post #1 by @Franci (2023-11-22 20:31 UTC)

<p>Hi,</p>
<p>I am using a MacBook and Slicer 5.5.0</p>
<p>First I had many issues to find a version that allowed the SlicerElastix downloading.</p>
<p>Now when I put my inputs brain files and output + specify the active volume and the lookup table + click on “apply”, Elastix it not able to compute the results and send back the following error message :<br>
“Command ‘elastix’ died with &lt;Signals.SIGABRT: 6&gt;.”</p>
<p>details:<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3146, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 241, in onApplyButton<br>
self.logic.registerVolumesUsingParameterNode(self._parameterNode)<br>
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 518, in registerVolumesUsingParameterNode<br>
self.registerVolumes(<br>
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 564, in registerVolumes<br>
self.logProcessOutput(elastixProcess)<br>
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 499, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, “elastix”)<br>
subprocess.CalledProcessError: Command ‘elastix’ died with &lt;Signals.SIGABRT: 6&gt;.</p>
<p>Chat GPT says that it’s an error inside the python script, I don’t know how to access it. And I need this data processing step for my research.</p>
<p>Please if anyone could help with this. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2023-11-22 20:32 UTC)

<p>Have you specified some custom Elastix binaries? Was there any issue with the binaries that are bundled with the extension?</p>

---

## Post #3 by @Franci (2023-11-22 20:42 UTC)

<p>Thank you for the quick answer, I just loaded the “SlicerElastix extension” as it was in the “Install Slicer extensions”, without any custom.</p>

---

## Post #4 by @lassoan (2023-11-23 12:35 UTC)

<p>Could you please try with the latest Slicer Preview Release?</p>

---

## Post #5 by @Franci (2023-11-23 13:19 UTC)

<p>unfortunately, it gave the same error message on Slicer 5.4.0. This is why I tried a more ancien version.</p>

---

## Post #6 by @lassoan (2023-11-23 20:52 UTC)

<p>Could you please try with the latest Slicer Preview Release (Slicer-5.5.x)?</p>

---

## Post #7 by @Franci (2023-11-29 15:46 UTC)

<p>I tried the latest version stable, slicer 5.6.0, it gave me the same error message. Do you thing we can resolve this?</p>

---

## Post #8 by @Andrey_Zhylka (2023-12-28 12:45 UTC)

<p>I have the same issue (also on MacBook). The log window says it cannot find libomp.dylib. I have installed that one using Homebrew, but Slicer is not looking for it in the Homebrew directories but in the extension directory and /usr/lib, /usr/local/lib</p>

---

## Post #9 by @lassoan (2024-01-01 17:55 UTC)

<p>Thank you, this explains it. OpenMP is a pain. You probably have dozens of mostly incompatible variants on your system. Elastix should not try to use that are on your system, because most likely they will not work (because they are probably not the same version as the one used when building Elastix).</p>
<p>A workaround that you can apply immediately is to download Elastix binaries (or build Elastix on your system) and specify that path in the Advanced section of the Elastix module in Slicer.</p>
<p>The root cause of the issue could be fixed by bundling libopenmp.dylib with the SlicerElastix extension or disabling OpenMP when building the extension. Your can monitor the status of the fix here:</p>
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


---
