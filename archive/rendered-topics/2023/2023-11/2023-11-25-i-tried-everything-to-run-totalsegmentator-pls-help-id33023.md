---
topic_id: 33023
title: "I Tried Everything To Run Totalsegmentator Pls Help"
date: 2023-11-25
url: https://discourse.slicer.org/t/33023
---

# I tried everything to run totalsegmentator pls help

**Topic ID**: 33023
**Date**: 2023-11-25
**URL**: https://discourse.slicer.org/t/i-tried-everything-to-run-totalsegmentator-pls-help/33023

---

## Post #1 by @Ahmad_Yahay (2023-11-25 18:01 UTC)

<p>I am having trouble with totalsegmentator, i tried most solution in the fourm but nothing worked. I tried the brevious version with slicer 5.4 and could not make it work, now I tried with slicer 5.5 review and totalsegmentator v2 and still no hope.</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\ahmad\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-22\bin\Python\slicer\util.py”, line 3253, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/ahmad/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-22/slicer.org/Extensions-32352/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 292, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/ahmad/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-22/slicer.org/Extensions-32352/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 967, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/ahmad/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-22/slicer.org/Extensions-32352/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 787, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/ahmad/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-22/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\ahmad\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-22\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/ahmad/AppData/Local/Temp/Slicer/__SlicerTemp__٢٠٢٣-١١-٢٤_٠٦+٠٥+٢٤.٦٥٢/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/ahmad/AppData/Local/Temp/Slicer/__SlicerTemp__٢٠٢٣-١١-٢٤_٠٦+٠٥+٢٤.٦٥٢/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’, ‘–device’, ‘cpu’]’ returned non-zero exit status 1.</p>
<p>I also get this error:<br>
Writing input file to C:/Users/ahmad/AppData/Local/Temp/Slicer/__SlicerTemp__٢٠٢٣-١١-٢٤_٠٦+١٤+٣٩.١٦٥/total-segmentator-input.nii</p>
<p>Creating segmentations with TotalSegmentator AI…</p>
<p>Total Segmentator arguments: [‘-i’, ‘C:/Users/ahmad/AppData/Local/Temp/Slicer/__SlicerTemp__٢٠٢٣-١١-٢٤_٠٦+١٤+٣٩.١٦٥/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/ahmad/AppData/Local/Temp/Slicer/__SlicerTemp__٢٠٢٣-١١-٢٤_٠٦+١٤+٣٩.١٦٥/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’, ‘–device’, ‘cpu’]</p>
<p><strong>ERROR: The input file or directory does not exist.</strong></p>
<p>If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>Using ‘fast’ option: resampling to lower resolution (3mm)<br>
I am using the ct chest sample<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0f0e2c6b53c7afa701204fae254107e21d50bea.png" data-download-href="/uploads/short-url/tOnpnIjYIjU9wcNaIaUzewLH7pE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0f0e2c6b53c7afa701204fae254107e21d50bea.png" alt="image" data-base62-sha1="tOnpnIjYIjU9wcNaIaUzewLH7pE" width="690" height="313" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">802×364 9.04 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-11-25 18:45 UTC)

<p>Most likely the issue is that your regional settings in the operating system make the temporary folder name contain special characters. In the short term, you can fix this by changing your date&amp;time settings in your operating system. We’ll try to change the temporary folder generation in TotalSegmentator later.</p>

---

## Post #3 by @rbumm (2023-11-26 08:57 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  Maybe we could use tempfile,</p>
<p>Me</p>
<p>Is there a better way to create an always working unique temp folder in Python ?</p>
<p>ChatGPT</p>
<p>Creating a universally compatible and unique temporary folder in Python can be done using the <code>tempfile</code> module, which is part of Python’s standard library. The <code>tempfile</code> module is designed to create temporary files and directories in a way that is secure and system-independent. This means it automatically handles the creation of unique directory names and ensures compatibility across different operating systems and file systems.</p>
<p>Here is a simple way to create a unique temporary directory using <code>tempfile</code>:</p>
<p>pythonCopy code</p>
<pre><code class="lang-auto">import tempfile
import os

# Create a new temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print("Temporary directory created at:", temp_dir)
    # You can use the temporary directory here

# After the 'with' block, the temporary directory and all its contents are automatically deleted
print("Temporary directory and all its contents have been deleted")
</code></pre>
<p>This code snippet uses the <code>TemporaryDirectory()</code> function within a context manager (<code>with</code> statement). The temporary directory is automatically created and is guaranteed to be unique. The <code>with</code> statement ensures that the directory is cleaned up (deleted) when you are done with it, which is a good practice when dealing with temporary files and directories.</p>
<p>This method is recommended because it is secure, avoids conflicts, and is compatible with all operating systems where Python runs. It eliminates the need for manual handling of file paths, including issues related to character sets or naming conventions.</p>

---

## Post #4 by @Ahmad_Yahay (2023-11-27 05:13 UTC)

<p>So I tried to change the regional setting and that did not work.  Now I installed slicer and total segmentator on another PC that has English as system language so the special charecters will not be generated. However. I still can not run it. This is what I get:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\Ahmad\AppData\Local\slicer.org\Slicer 5.4.0\bin\Python\slicer\util.py”, line 3146, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/Ahmad/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 271, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/Ahmad/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 785, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/Ahmad/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 614, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/Ahmad/AppData/Local/slicer.org/Slicer 5.4.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\Ahmad\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/Ahmad/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-27_08+03+30.287/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Ahmad/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-27_08+03+30.287/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 2.</p>
<p>Also this note:<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/Ahmad/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-27_08+03+30.287/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Ahmad/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-27_08+03+30.287/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
C:\Users\Ahmad\AppData\Local\slicer.org\Slicer 5.4.0\bin.\python-real.exe: can’t open file ‘C:\Users\Ahmad\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator.exe’: [Errno 2] No such file or directory</p>
<p>I installed pytorch the cpu version since the gpu does not have 7 GB of memory although its Nvidia. and run the the process in fast mode</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af143d1f76be216704ad293a1d0793dcf0d5cf04.png" alt="2023-11-27 (2)" data-base62-sha1="oYOUXnVsV4TCmNwi8TfrjwvMbSk" width="446" height="106"></p>

---

## Post #5 by @lassoan (2023-11-27 06:23 UTC)

<p>OK, this is much better! It seems that the remaining issue is this:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/issues/49">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/49" target="_blank" rel="noopener">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/49" target="_blank" rel="noopener">TotalSegmentator.exe': [Errno 2] No such file or directory</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-11-24" data-time="15:40:33" data-timezone="UTC">03:40PM - 24 Nov 23 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2023-11-27" data-time="05:45:52" data-timezone="UTC">05:45AM - 27 Nov 23 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/Hurmean" target="_blank" rel="noopener">
          <img alt="Hurmean" src="https://avatars.githubusercontent.com/u/12394658?v=4" class="onebox-avatar-inline" width="20" height="20">
          Hurmean
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When I use TotalSegmentator, I encounter the following issues
![1700839166689](<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">https://github.com/lassoan/SlicerTotalSegmentator/assets/12394658/0d9a3ca6-12f7-416c-a8c1-8fb1f2bf6767)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The simplest solution would be to upgrade to Slicer-5.6.</p>
<p>We’ll fix TotalSegmentator on Arabic comptuers soon - see progress here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7430">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7430" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7430" target="_blank" rel="noopener">BUG: Fix temporary folder containing special characters</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-arabic-numerals</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-11-27" data-time="06:22:28" data-timezone="UTC">06:22AM - 27 Nov 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 4 files with 22 additions and 5 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7430/files" target="_blank" rel="noopener">
            <span class="added">+22</span>
            <span class="removed">-5</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">qt.QDateTime().currentDateTime().toString(...) may use Arabic numerals on an ope<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7430" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rating system set to Arabic language. Always specify en-US locale when using when using date in file/folder names to avoid having to work with paths that may contain unicode characters.

Fixes problem originally reported at:
https://discourse.slicer.org/t/i-tried-everything-to-run-totalsegmentator-pls-help/33023/3</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Ahmad_Yahay (2023-11-28 05:19 UTC)

<p>Great thank you working fine now. Thanks for your help.</p>

---
