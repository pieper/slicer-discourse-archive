# Loading of MRHead sample data set failed

**Topic ID**: 1716
**Date**: 2017-12-24
**URL**: https://discourse.slicer.org/t/loading-of-mrhead-sample-data-set-failed/1716

---

## Post #1 by @mima (2017-12-24 04:36 UTC)

<p>Hello<br>
I download 3Dslicer when i try to doawnload sample data the give me this answer<br>
Requesting load MRHead from C:/Users/mima/AppData/Local/Temp/Slicer/RemoteIO/MR-head.nrrd…<br>
Load failed!</p>
<p>Can one help me please</p>

---

## Post #2 by @cpinter (2017-12-24 15:15 UTC)

<p>Hi!</p>
<p>Which version of Slicer do you use?<br>
Can you copy any file to that folder? (i.e. is it somehow inaccessible)<br>
Please send us the log: About / Report a bug.</p>

---

## Post #3 by @mima (2017-12-24 19:05 UTC)

<p>Hi<br>
I use 3D slicer 4.6.2</p>

---

## Post #4 by @cpinter (2017-12-27 15:36 UTC)

<p>That version is quite old now, please use 4.8.1.</p>
<p>If the same thing happens with 4.8.1, then please:</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="1716">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Can you copy any file to that folder? (i.e. is it somehow inaccessible)</p>
<p>Please send us the log: About / Report a bug.</p>
</blockquote>
</aside>

---

## Post #5 by @mima (2017-12-31 09:31 UTC)

<p>Hello</p>
<ul>
<li>I try with 4.9.0</li>
<li>Yes i can copy any file to that folder</li>
<li>I send you the log</li>
</ul>

---

## Post #6 by @cpinter (2018-01-03 15:42 UTC)

<p>Thanks for the answers and the log!</p>
<p>It seems that the file was downloaded halfway the first time and is in a corrupt state, that’s why it cannot be loaded. You’ll need to delete the file 'C:/Users/mima/AppData/Local/Temp/Slicer/RemoteIO/MR-head.nrrd’<br>
and try again.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> Should we do this automatically when loading fails like this on a sample dataset?</p>

---

## Post #7 by @lassoan (2018-01-03 15:59 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="1716">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Should we do this automatically when loading fails like this on a sample dataset?</p>
</blockquote>
</aside>
<p>That’s a good idea! Would you take a stab at implementing this?</p>

---

## Post #8 by @cpinter (2018-01-03 16:31 UTC)

<p>OK I’ll give it a go. I implemented similar things recently anyway.</p>

---

## Post #9 by @pieper (2018-01-03 16:43 UTC)

<p>Yes, excellent idea!  Thanks for looking into this.  In other places we have used md5 sum checks as well, but redownloading on failed load sounds simpler.</p>

---

## Post #10 by @che85 (2018-01-03 16:45 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Maybe you should even add some check if the download directory is accessible and if not have a message box telling the user about the issue and maybe let them choose a location where to store sample data?</p>

---

## Post #11 by @cpinter (2018-01-03 17:06 UTC)

<p>Choosing the location might be an overkill, as the temp directory should be writable at all times, but I’ll add the check and the warning.</p>

---

## Post #12 by @pieper (2018-01-03 17:48 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a>  Note that the sample data uses the cache directory which is already settable in the Cache page of the user preferences.  So it is possible that it could be set to an invalid directory.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/e9348fa17ab54267b924959905c3f1576708d551/Modules/Scripted/SampleData/SampleData.py#L291-L295" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/e9348fa17ab54267b924959905c3f1576708d551/Modules/Scripted/SampleData/SampleData.py#L291-L295" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/e9348fa17ab54267b924959905c3f1576708d551/Modules/Scripted/SampleData/SampleData.py#L291-L295</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="291" style="counter-reset: li-counter 290 ;">
<li>def downloadFileIntoCache(self, uri, name):</li>
<li>  """Given a uri and and a filename, download the data into</li>
<li>  a file of the given name in the scene's cache"""</li>
<li>  destFolderPath = slicer.mrmlScene.GetCacheManager().GetRemoteCacheDirectory()</li>
<li>  return self.downloadFile(uri, destFolderPath, name)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #13 by @cpinter (2018-01-04 15:07 UTC)

<p>If Sample Data uses the centrally set cache folder, then I think checking whether it’s writable should not happen in a module, but somewhere more central, like when setting that folder at startup. And because the same goes for DICOM database folder etc, this could be handled the same way for all these folders. Thoughts?</p>

---

## Post #14 by @lassoan (2018-01-04 16:51 UTC)

<p>Fully agree, it should not be checked in  a module.</p>
<p>The DICOM folder is checked when you switch to the DICOM module (not ideal, but in general you import DICOM using the DICOM module, so it is OK). However, temp and cache folder are not checked. This caused problems on some Linux systems, where earlier temp folder was not always initialized to a writeable location, but that problem is now <a href="https://issues.slicer.org/view.php?id=4340">fixed</a>.</p>
<p>It’s not easy to figure out when and how the user should be notified about invalid temp and cache folders and they should happen very rarely, if ever. So, I think it is acceptable to handle this exceptional case by only logging an error and letting the user figure it out from that.</p>

---

## Post #15 by @pieper (2018-01-04 18:08 UTC)

<p>I was thinking the validity of the settings could be checked at application start time.</p>

---

## Post #16 by @cpinter (2018-01-23 20:58 UTC)

<p>For the record, the re-download feature was added in<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/09d9918a828788ba8643f2cbdcc3b5b86ab871e1" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    
<h4>
  <a href="https://github.com/Slicer/Slicer/commit/09d9918a828788ba8643f2cbdcc3b5b86ab871e1" target="_blank" rel="nofollow noopener">ENH: Try to download sample data again after loading fails</a>
</h4>

  <pre class="message" style="white-space: pre-wrap;">Related to https://discourse.slicer.org/t/loading-of-mrhead-sample-data-set-failed/1716

git-svn-id: http://svn.slicer.org/Slicer4/trunk@26858 3bd1e089-480b-0410-8dfb-8563597acbee</pre>

<div class="date">
  by <a href=""></a>
  on <a href="https://github.com/Slicer/Slicer/commit/09d9918a828788ba8643f2cbdcc3b5b86ab871e1" target="_blank" rel="nofollow noopener">08:57PM - 23 Jan 18</a>
</div>

<div class="github-commit-stats">
  changed <strong>1 files</strong>
  with <strong>25 additions</strong>
  and <strong>8 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
