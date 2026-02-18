# Total Segmentor Lung Basic BUG report on Version 5.2.2 while working perfectly on 5.2.1

**Topic ID**: 28238
**Date**: 2023-03-08
**URL**: https://discourse.slicer.org/t/total-segmentor-lung-basic-bug-report-on-version-5-2-2-while-working-perfectly-on-5-2-1/28238

---

## Post #1 by @Khaldoun (2023-03-08 20:04 UTC)

<p>Operating system:: Windows 10 Professionnel<br>
Intel(R) Core™ i5-10505 CPU @ 3.20GHz   3.19 GHz<br>
16Go RAM<br>
Slicer version:5.2.2<br>
Expected behavior:Should be working as well as on version 5.2.1 installed on the same computer using the fast method as there is no CUDA and no GPU intalled<br>
Actual behavior:: Bug report with 5.2.2 giving this followinf message:<br>
Failed to compute results: Command ‘[‘C:/Users/g-tnn5319433pc/AppData/Local/NA-MIC/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\g-tnn5319433pc\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/g-tnn5319433pc/AppData/Local/Temp/Slicer/__SlicerTemp__2023-03-08_20+56+50.090/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/g-tnn5319433pc/AppData/Local/Temp/Slicer/__SlicerTemp__2023-03-08_20+56+50.090/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 2.</p>
<p>thank you very much for your kind help<br>
Khaldoun</p>

---

## Post #2 by @rbumm (2023-03-08 20:57 UTC)

<p>You must install SlicerPytotch first and install Pytorch.<br>
Then Restart.<br>
The Use TotalSegmentator extension with itself installs TotalsSegmentator and sometimes finish with such an error message.<br>
Restart Slicer, and run TS a second time, that usually fixes it.</p>

---

## Post #3 by @jamesobutler (2023-03-08 23:42 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> When you install the Slicer TotalSegmentor extension, doesn’t it automatically install the Slicer PyTorch extension dependency?</p>
<p>What situations require the user to manually do the process to install PyTorch?</p>

---

## Post #4 by @rbumm (2023-03-09 06:59 UTC)

<p>You are right, this step is done automatically.</p>
<p>If I just install a TS extension in a fresh 3D Slicer 5.2.2, load a dataset and press “Apply” I still get</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39e0f1c01fa94130c5a5cd96f7c014d1cc075842.png" alt="image" data-base62-sha1="8g19ISzJyNeQ8AtBBxDpl5tea6C" width="576" height="265"></p>
<p>upon the first try.</p>
<p>Any second run or a run after a 3D Slicer restart will succeed.</p>

---

## Post #5 by @jamesobutler (2023-03-13 21:33 UTC)

<p>I am observing an error with the TotalSegmentor (like what is shown in the above image) install due to SlicerTotalSegmentor pointing to an older TotalSegmentor version.</p>
<p>A TotalSegmentor dependency incorrectly specified to install <code>sklearn</code> from PyPI instead of <code>scikit-learn</code>, and TotalSegmentor <a href="https://github.com/wasserth/TotalSegmentator/blob/b38eb449ad8652a987878a925203cbfa354e9b85/CHANGELOG.md" rel="noopener nofollow ugc">updated</a> the dependency with a fix.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/jamesobutler/SlicerTotalSegmentator/commit/d9b4f6e7a2eae05d099836aa8d314a59df066262">
  <header class="source">

      <a href="https://github.com/jamesobutler/SlicerTotalSegmentator/commit/d9b4f6e7a2eae05d099836aa8d314a59df066262" target="_blank" rel="noopener nofollow ugc">github.com/jamesobutler/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/jamesobutler/SlicerTotalSegmentator/commit/d9b4f6e7a2eae05d099836aa8d314a59df066262" target="_blank" rel="noopener nofollow ugc">ENH: Install specific TotalSegmentator Python package version</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-01-16" data-time="20:33:14" data-timezone="UTC">08:33PM - 16 Jan 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/rbumm" target="_blank" rel="noopener nofollow ugc">
          <img alt="rbumm" src="https://avatars.githubusercontent.com/u/18140094?v=4" class="onebox-avatar-inline" width="20" height="20">
          rbumm
        </a>
      </div>

      <div class="lines" title="changed 3 files with 44 additions and 11 deletions">
        <a href="https://github.com/jamesobutler/SlicerTotalSegmentator/commit/d9b4f6e7a2eae05d099836aa8d314a59df066262" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+44</span>
          <span class="removed">-11</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Until now, there was an option to install latest TotalSegmentator Python package<span class="show-more-container"><a href="https://github.com/jamesobutler/SlicerTotalSegmentator/commit/d9b4f6e7a2eae05d099836aa8d314a59df066262" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> from GitHub.
However, since the download URL was always the same, pip always used the same existing package in the cache (did not retrieve the latest content of the URL).
There were also issues with options and behavior changing significantly between TotalSegmentator Python package versions, so updating the package separately from the Slicer module appeared to be risky.

Therefore, behavior of the module is now changed so that the required TotalSegmentator Python package version (defined by download URL) is specified in the module logic constructor. When segmentation is started then the package version is checked and the package is updated if needed.

An option for forced reinstallation was kept for troubleshooting and restoration of corrupted installations.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p><a class="mention" href="/u/rbumm">@rbumm</a> <a class="mention" href="/u/lassoan">@lassoan</a> Is there a specific need to continue using TotalSegmentor as of <a href="https://github.com/wasserth/TotalSegmentator/commit/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a" rel="noopener nofollow ugc">ecf84f9</a>? Would it be possible to upgrade this to the <code>v1.5.3</code> tag which appears to contain the <code>sklearn</code> fix?</p>

---

## Post #6 by @lassoan (2023-03-13 21:57 UTC)

<p>The current version already contains the sklearn fix (that allowed thousands of users successfully using TotalSegmentator). That said, if you tested this new hash and everything seems to work then there is no problem with updating the git hash. Please submit a pull request! Thank you.</p>
<p>I don’t trust the git tag, as it can be moved to a different version and pip will not notice it. So, please use a git hash (you can add the git label as a comment).</p>

---

## Post #7 by @jamesobutler (2023-03-13 22:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="28238">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The current version already contains the sklearn fix (that allowed thousands of users successfully using TotalSegmentator).</p>
</blockquote>
</aside>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/blob/fe5c538c8afee20f822c7a3e3075ff90fe9b1893/TotalSegmentator/TotalSegmentator.py#L301">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/fe5c538c8afee20f822c7a3e3075ff90fe9b1893/TotalSegmentator/TotalSegmentator.py#L301" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/fe5c538c8afee20f822c7a3e3075ff90fe9b1893/TotalSegmentator/TotalSegmentator.py#L301" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerTotalSegmentator/blob/fe5c538c8afee20f822c7a3e3075ff90fe9b1893/TotalSegmentator/TotalSegmentator.py#L301</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="291" style="counter-reset: li-counter 290 ;">
          <li>"""</li>
          <li></li>
          <li>def __init__(self):</li>
          <li>    """</li>
          <li>    Called when the logic class is instantiated. Can be used for initializing member variables.</li>
          <li>    """</li>
          <li>    from collections import OrderedDict</li>
          <li></li>
          <li>    ScriptedLoadableModuleLogic.__init__(self)</li>
          <li></li>
          <li class="selected">    self.totalSegmentatorPythonPackageDownloadUrl = "https://github.com/wasserth/TotalSegmentator/archive/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a.zip"</li>
          <li></li>
          <li>    self.logCallback = None</li>
          <li>    self.clearOutputFolder = True</li>
          <li>    self.useStandardSegmentNames = True</li>
          <li></li>
          <li>    self.tasks = OrderedDict()</li>
          <li>    self.tasks['total'] = {'label': 'total', 'supportsFast': True, 'supportsMultiLabel': True}</li>
          <li>    self.tasks['lung_vessels'] = {'label': 'lung vessels', 'requiresPreSegmentation': True}</li>
          <li>    self.tasks['cerebral_bleed'] = {'label': 'cerebral bleed', 'requiresPreSegmentation': True, 'supportsMultiLabel': True}</li>
          <li>    self.tasks['hip_implant'] = {'label': 'hip implant', 'requiresPreSegmentation': True, 'supportsMultiLabel': True}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>^This hash of TotalSegmentor produced an exit error code 1 associated with trying to install the sklearn from PyPI instead of scikit-learn. I did not previously have TotalSegmentor installed in Slicer 5.2.2.</p>

---

## Post #8 by @jamesobutler (2023-03-13 23:55 UTC)

<p>With the currently used TotalSegmentor at <a href="https://github.com/wasserth/TotalSegmentator/commit/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a" rel="noopener nofollow ugc">ecf84f9</a> it specifies a hard version requirement of a dependency that then specifies <code>sklearn</code> instead of <code>scikit-learn</code>. This dependency at nnunet-customized==1.2 includes the fix, but pip —upgrade is not going to make that upgrade since a specific version of this dependency is stated as being required. Maybe this exit code for <code>sklearn</code> doesn’t stop TotalSegmentor from working, but does show as an exit code on first running TotalSegmentor when it gets installed.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/wasserth/TotalSegmentator/blob/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a/setup.py#L27">
  <header class="source">

      <a href="https://github.com/wasserth/TotalSegmentator/blob/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a/setup.py#L27" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/wasserth/TotalSegmentator/blob/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a/setup.py#L27" target="_blank" rel="noopener nofollow ugc">wasserth/TotalSegmentator/blob/ecf84f9e59b84dddb447e2b13542f58c29ee4c6a/setup.py#L27</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="17" style="counter-reset: li-counter 16 ;">
          <li>    # https://github.com/SimpleITK/SimpleITK/issues/1433</li>
          <li>    'SimpleITK',</li>
          <li>    'nibabel&gt;=2.3.0',</li>
          <li>    'tqdm&gt;=4.45.0',</li>
          <li>    'p_tqdm',</li>
          <li>    'xvfbwrapper',</li>
          <li>    'fury',</li>
          <li>    'batchgenerators==0.21',</li>
          <li>    # This does not work if want to upload to pypi</li>
          <li>    # 'nnunet @ git+https://github.com/wasserth/nnUNet_cust@working_2022_03_18#egg=nnUNet'</li>
          <li class="selected">    'nnunet-customized==1.1',</li>
          <li>    'requests'</li>
          <li>],</li>
          <li>zip_safe=False,</li>
          <li>classifiers=[</li>
          <li>    'Intended Audience :: Science/Research',</li>
          <li>    'Programming Language :: Python',</li>
          <li>    'Topic :: Scientific/Engineering',</li>
          <li>    'Operating System :: Unix',</li>
          <li>    'Operating System :: MacOS'</li>
          <li>],</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Xref <a href="https://github.com/wasserth/TotalSegmentator/issues/72" class="inline-onebox" rel="noopener nofollow ugc">Update nnunet-customized to use scikit-learn instead of sklearn · Issue #72 · wasserth/TotalSegmentator · GitHub</a></p>

---

## Post #9 by @lassoan (2023-03-14 14:57 UTC)

<p>Thanks for the investigation. Yes, probably scikit-learn is actually not needed (similarly as matplotlib and other dependencies are not used either).</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> Created a PR to update to TotalSegmentator Python package and it has been merged.</p>

---

## Post #10 by @jamesobutler (2023-03-14 16:52 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="4" data-topic="28238">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>If I just install a TS extension in a fresh 3D Slicer 5.2.2, load a dataset and press “Apply” I still get</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39e0f1c01fa94130c5a5cd96f7c014d1cc075842.png" alt="image" data-base62-sha1="8g19ISzJyNeQ8AtBBxDpl5tea6C" width="576" height="265"></p>
<p>upon the first try.</p>
<p>Any second run or a run after a 3D Slicer restart will succeed.</p>
</blockquote>
</aside>
<p>I’ve written up the following issue report about errors installing TotalSegmentor python dependencies that results in TotalSegmentor not running the first time. Upon restarting Slicer, it will detect that the TotalSegmentor python package is present and will proceed normally.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/issues/17">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/17" target="_blank" rel="noopener nofollow ugc">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/17" target="_blank" rel="noopener nofollow ugc">SlicerTotalSegmentor fails on initial apply</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-03-14" data-time="16:15:22" data-timezone="UTC">04:15PM - 14 Mar 23 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2023-04-05" data-time="03:37:27" data-timezone="UTC">03:37AM - 05 Apr 23 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I'm currently using Slicer 5.2.2, have SlicerPyTorch installed and pointing to S<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">licerTotalSegmentor as of https://github.com/lassoan/SlicerTotalSegmentator/commit/493fa5bcbb75267e21ec086f95d0eb01ec1562a5.

I start Slicer fresh, and when I go into TotalSegmentor and press apply, it appropriate warns that PyTorch needs to be downloaded and installed and then it installs the TotalSegmentor package. However I observe that the install process uninstall `scipy` 1.9.2 that is included as part of Slicer 5.2.2 and it installs `scipy` 1.9.1. This produces an exit code that results in TotalSegmentor not running. Is it expected for the uninstall/install of `scipy` to be successful in Slicer? If I close Slicer, reopen and then press "Apply" in TotalSegmentor then it is successful.

Is access denied because the `scipy` package is in-use as it has been [imported in Slicer on startup](https://github.com/Slicer/Slicer/blob/fb46bd16846dc7c7a69c398aef0fc3baf533905e/Base/Python/slicer/__init__.py#L68-L69)? 
```
ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: 'C:\\Users\\butlej30383\\AppData\\Local\\NA-MIC\\Slicer 5.2.2\\lib\\Python\\Lib\\site-packages\\~cipy\\_lib\\_ccallback_c.cp39-win_amd64.pyd'
Consider using the `--user` option or check the permissions.
```

![image](https://user-images.githubusercontent.com/15837524/225063222-ddf680f7-0caf-4d1e-bf2d-2e652e463fc6.png)

Additional FYI: The latest `torch 2.0.0` was downloaded and installed here.
&lt;details&gt;
  &lt;summary&gt;See full pip output here&lt;/summary&gt;
Python 3.9.10 (main, Feb 22 2023, 01:07:37) [MSC v.1930 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
Collecting light-the-torch&gt;=0.5
  Downloading light_the_torch-0.7.1-py3-none-any.whl (14 kB)
Requirement already satisfied: pip&lt;23.1,&gt;=22.3 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from light-the-torch&gt;=0.5) (23.0)
Installing collected packages: light-the-torch
  WARNING: The script ltt.exe is installed in 'C:\Users\butlej30383\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed light-the-torch-0.7.1

[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python-real.exe -m pip install --upgrade pip
Collecting torch
  Downloading https://download.pytorch.org/whl/cu118/torch-2.0.0%2Bcu118-cp39-cp39-win_amd64.whl (2611.4 MB)
     ---------------------------------------- 2.6/2.6 GB 1.7 MB/s eta 0:00:00
Collecting jinja2
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     -------------------------------------- 133.1/133.1 kB 1.6 MB/s eta 0:00:00
Collecting typing-extensions
  Downloading typing_extensions-4.5.0-py3-none-any.whl (27 kB)
Collecting filelock
  Downloading filelock-3.9.1-py3-none-any.whl (9.7 kB)
Collecting networkx
  Downloading networkx-3.0-py3-none-any.whl (2.0 MB)
     ---------------------------------------- 2.0/2.0 MB 10.0 MB/s eta 0:00:00
Collecting sympy
  Downloading sympy-1.11.1-py3-none-any.whl (6.5 MB)
     ---------------------------------------- 6.5/6.5 MB 29.5 MB/s eta 0:00:00
Collecting MarkupSafe&gt;=2.0
  Downloading MarkupSafe-2.1.2-cp39-cp39-win_amd64.whl (16 kB)
Collecting mpmath&gt;=0.19
  Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
     ------------------------------------- 536.2/536.2 kB 32.9 MB/s eta 0:00:00
Installing collected packages: mpmath, typing-extensions, sympy, networkx, MarkupSafe, filelock, jinja2, torch
  WARNING: The script isympy.exe is installed in 'C:\Users\butlej30383\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts convert-caffe2-to-onnx.exe, convert-onnx-to-caffe2.exe and torchrun.exe are installed in 'C:\Users\butlej30383\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed MarkupSafe-2.1.2 filelock-3.9.1 jinja2-3.1.2 mpmath-1.3.0 networkx-3.0 sympy-1.11.1 torch-2.0.0+cu118 typing-extensions-4.5.0

[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python-real.exe -m pip install --upgrade pip
Collecting matplotlib
  Downloading matplotlib-3.7.1-cp39-cp39-win_amd64.whl (7.6 MB)
     ---------------------------------------- 7.6/7.6 MB 18.8 MB/s eta 0:00:00
Collecting python-dateutil&gt;=2.7
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     -------------------------------------- 247.7/247.7 kB 7.7 MB/s eta 0:00:00
Collecting kiwisolver&gt;=1.0.1
  Downloading kiwisolver-1.4.4-cp39-cp39-win_amd64.whl (55 kB)
     ---------------------------------------- 55.4/55.4 kB 1.5 MB/s eta 0:00:00
Collecting fonttools&gt;=4.22.0
  Downloading fonttools-4.39.0-py3-none-any.whl (1.0 MB)
     ---------------------------------------- 1.0/1.0 MB 12.7 MB/s eta 0:00:00
Collecting cycler&gt;=0.10
  Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
Requirement already satisfied: pillow&gt;=6.2.0 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from matplotlib) (9.4.0)
Requirement already satisfied: pyparsing&gt;=2.3.1 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from matplotlib) (3.0.9)
Requirement already satisfied: packaging&gt;=20.0 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from matplotlib) (23.0)
Collecting importlib-resources&gt;=3.2.0
  Downloading importlib_resources-5.12.0-py3-none-any.whl (36 kB)
Requirement already satisfied: numpy&gt;=1.20 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from matplotlib) (1.23.4)
Collecting contourpy&gt;=1.0.1
  Downloading contourpy-1.0.7-cp39-cp39-win_amd64.whl (160 kB)
     -------------------------------------- 160.2/160.2 kB 3.2 MB/s eta 0:00:00
Collecting zipp&gt;=3.1.0
  Downloading zipp-3.15.0-py3-none-any.whl (6.8 kB)
Requirement already satisfied: six&gt;=1.5 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from python-dateutil&gt;=2.7-&gt;matplotlib) (1.16.0)
Installing collected packages: zipp, python-dateutil, kiwisolver, fonttools, cycler, contourpy, importlib-resources, matplotlib
  WARNING: The scripts fonttools.exe, pyftmerge.exe, pyftsubset.exe and ttx.exe are installed in 'C:\Users\butlej30383\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed contourpy-1.0.7 cycler-0.11.0 fonttools-4.39.0 importlib-resources-5.12.0 kiwisolver-1.4.4 matplotlib-3.7.1 python-dateutil-2.8.2 zipp-3.15.0

[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python-real.exe -m pip install --upgrade pip
Collecting https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  Downloading https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
     - 5.5 MB 16.0 MB/s 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: numpy in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from TotalSegmentator==1.5.3) (1.23.4)
Collecting psutil
  Downloading psutil-5.9.4-cp36-abi3-win_amd64.whl (252 kB)
     -------------------------------------- 252.5/252.5 kB 2.6 MB/s eta 0:00:00
Requirement already satisfied: SimpleITK in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from TotalSegmentator==1.5.3) (2.2.0rc2.dev368)
Collecting nibabel&gt;=2.3.0
  Downloading nibabel-5.0.1-py3-none-any.whl (3.3 MB)
     ---------------------------------------- 3.3/3.3 MB 17.4 MB/s eta 0:00:00
Collecting tqdm&gt;=4.45.0
  Downloading tqdm-4.65.0-py3-none-any.whl (77 kB)
     ---------------------------------------- 77.1/77.1 kB ? eta 0:00:00
Collecting p_tqdm
  Downloading p_tqdm-1.4.0.tar.gz (5.2 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting xvfbwrapper
  Downloading xvfbwrapper-0.2.9.tar.gz (5.6 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting fury
  Downloading fury-0.8.0-py3-none-any.whl (349 kB)
     ------------------------------------- 349.2/349.2 kB 22.6 MB/s eta 0:00:00
Collecting batchgenerators==0.21
  Downloading batchgenerators-0.21-py3-none-any.whl (74 kB)
     ---------------------------------------- 74.7/74.7 kB ? eta 0:00:00
Collecting nnunet-customized==1.2
  Downloading nnunet_customized-1.2-py3-none-any.whl (474 kB)
     ------------------------------------- 474.0/474.0 kB 29.0 MB/s eta 0:00:00
Requirement already satisfied: requests in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from TotalSegmentator==1.5.3) (2.28.2)
Requirement already satisfied: scipy in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from batchgenerators==0.21-&gt;TotalSegmentator==1.5.3) (1.9.2)
Collecting future
  Downloading future-0.18.3.tar.gz (840 kB)
     ------------------------------------- 840.9/840.9 kB 51.9 MB/s eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting scikit-learn
  Downloading scikit_learn-1.2.2-cp39-cp39-win_amd64.whl (8.4 MB)
     ---------------------------------------- 8.4/8.4 MB 38.2 MB/s eta 0:00:00
Collecting scikit-image
  Downloading scikit_image-0.20.0-cp39-cp39-win_amd64.whl (23.9 MB)
     --------------------------------------- 23.9/23.9 MB 28.4 MB/s eta 0:00:00
Collecting threadpoolctl
  Downloading threadpoolctl-3.1.0-py3-none-any.whl (14 kB)
Requirement already satisfied: pillow&gt;=7.1.2 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from batchgenerators==0.21-&gt;TotalSegmentator==1.5.3) (9.4.0)
Collecting unittest2
  Downloading unittest2-1.1.0-py2.py3-none-any.whl (96 kB)
     ---------------------------------------- 96.4/96.4 kB ? eta 0:00:00
Collecting dicom2nifti
  Downloading dicom2nifti-2.4.8-py3-none-any.whl (43 kB)
     ---------------------------------------- 43.6/43.6 kB ? eta 0:00:00
Collecting pandas
  Downloading pandas-1.5.3-cp39-cp39-win_amd64.whl (10.9 MB)
     --------------------------------------- 10.9/10.9 MB 54.4 MB/s eta 0:00:00
Collecting tifffile
  Downloading tifffile-2023.2.28-py3-none-any.whl (216 kB)
     ------------------------------------- 216.4/216.4 kB 12.9 MB/s eta 0:00:00
Collecting medpy
  Downloading MedPy-0.4.0.tar.gz (151 kB)
     ---------------------------------------- 151.8/151.8 kB ? eta 0:00:00
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: torch&gt;=1.6.0a in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from nnunet-customized==1.2-&gt;TotalSegmentator==1.5.3) (2.0.0+cu118)
Requirement already satisfied: packaging&gt;=17 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from nibabel&gt;=2.3.0-&gt;TotalSegmentator==1.5.3) (23.0)
Requirement already satisfied: setuptools in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from nibabel&gt;=2.3.0-&gt;TotalSegmentator==1.5.3) (67.0.0)
Collecting colorama
  Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Requirement already satisfied: vtk&gt;=9.1.0 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from fury-&gt;TotalSegmentator==1.5.3) (9.1.20220125)
Collecting pathos&gt;=0.2.5
  Downloading pathos-0.3.0-py3-none-any.whl (79 kB)
     ---------------------------------------- 79.8/79.8 kB ? eta 0:00:00
Requirement already satisfied: six&gt;=1.13.0 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from p_tqdm-&gt;TotalSegmentator==1.5.3) (1.16.0)
Requirement already satisfied: idna&lt;4,&gt;=2.5 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from requests-&gt;TotalSegmentator==1.5.3) (3.4)
Requirement already satisfied: certifi&gt;=2017.4.17 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from requests-&gt;TotalSegmentator==1.5.3) (2022.12.7)
Requirement already satisfied: charset-normalizer&lt;4,&gt;=2 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from requests-&gt;TotalSegmentator==1.5.3) (3.0.1)
Requirement already satisfied: urllib3&lt;1.27,&gt;=1.21.1 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from requests-&gt;TotalSegmentator==1.5.3) (1.26.14)
Collecting multiprocess&gt;=0.70.14
  Downloading multiprocess-0.70.14-py39-none-any.whl (132 kB)
     ---------------------------------------- 132.9/132.9 kB ? eta 0:00:00
Collecting ppft&gt;=1.7.6.6
  Downloading ppft-1.7.6.6-py3-none-any.whl (52 kB)
     ---------------------------------------- 52.8/52.8 kB ? eta 0:00:00
Collecting dill&gt;=0.3.6
  Downloading dill-0.3.6-py3-none-any.whl (110 kB)
     ---------------------------------------- 110.5/110.5 kB ? eta 0:00:00
Collecting pox&gt;=0.3.2
  Downloading pox-0.3.2-py3-none-any.whl (29 kB)
Collecting lazy_loader&gt;=0.1
  Downloading lazy_loader-0.1-py3-none-any.whl (8.6 kB)
Collecting PyWavelets&gt;=1.1.1
  Downloading PyWavelets-1.4.1-cp39-cp39-win_amd64.whl (4.2 MB)
     ---------------------------------------- 4.2/4.2 MB 38.2 MB/s eta 0:00:00
Requirement already satisfied: networkx&gt;=2.8 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from scikit-image-&gt;batchgenerators==0.21-&gt;TotalSegmentator==1.5.3) (3.0)
Collecting scipy
  Downloading scipy-1.9.1-cp39-cp39-win_amd64.whl (38.6 MB)
     --------------------------------------- 38.6/38.6 MB 40.9 MB/s eta 0:00:00
Collecting imageio&gt;=2.4.1
  Downloading imageio-2.26.0-py3-none-any.whl (3.4 MB)
     ---------------------------------------- 3.4/3.4 MB 30.8 MB/s eta 0:00:00
Requirement already satisfied: typing-extensions in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from torch&gt;=1.6.0a-&gt;nnunet-customized==1.2-&gt;TotalSegmentator==1.5.3) (4.5.0)
Requirement already satisfied: sympy in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from torch&gt;=1.6.0a-&gt;nnunet-customized==1.2-&gt;TotalSegmentator==1.5.3) (1.11.1)
Requirement already satisfied: jinja2 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from torch&gt;=1.6.0a-&gt;nnunet-customized==1.2-&gt;TotalSegmentator==1.5.3) (3.1.2)
Requirement already satisfied: filelock in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from torch&gt;=1.6.0a-&gt;nnunet-customized==1.2-&gt;TotalSegmentator==1.5.3) (3.9.1)
Collecting python-gdcm
  Downloading python_gdcm-3.0.21-cp39-cp39-win_amd64.whl (27.2 MB)
     --------------------------------------- 27.2/27.2 MB 36.4 MB/s eta 0:00:00
Requirement already satisfied: pydicom&gt;=2.2.0 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from dicom2nifti-&gt;nnunet-customized==1.2-&gt;TotalSegmentator==1.5.3) (2.3.1)
Requirement already satisfied: python-dateutil&gt;=2.8.1 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from pandas-&gt;nnunet-customized==1.2-&gt;TotalSegmentator==1.5.3) (2.8.2)
Collecting pytz&gt;=2020.1
  Downloading pytz-2022.7.1-py2.py3-none-any.whl (499 kB)
     ------------------------------------- 499.4/499.4 kB 15.8 MB/s eta 0:00:00
Collecting joblib&gt;=1.1.1
  Downloading joblib-1.2.0-py3-none-any.whl (297 kB)
     ------------------------------------- 298.0/298.0 kB 18.0 MB/s eta 0:00:00
Collecting argparse
  Downloading argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Collecting traceback2
  Downloading traceback2-1.4.0-py2.py3-none-any.whl (16 kB)
Requirement already satisfied: MarkupSafe&gt;=2.0 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from jinja2-&gt;torch&gt;=1.6.0a-&gt;nnunet-customized==1.2-&gt;TotalSegmentator==1.5.3) (2.1.2)
Requirement already satisfied: mpmath&gt;=0.19 in c:\users\butlej30383\appdata\local\na-mic\slicer 5.2.2\lib\python\lib\site-packages (from sympy-&gt;torch&gt;=1.6.0a-&gt;nnunet-customized==1.2-&gt;TotalSegmentator==1.5.3) (1.3.0)
Collecting linecache2
  Downloading linecache2-1.0.0-py2.py3-none-any.whl (12 kB)
Building wheels for collected packages: TotalSegmentator, p_tqdm, xvfbwrapper, future, medpy
  Building wheel for TotalSegmentator (setup.py): started
  Building wheel for TotalSegmentator (setup.py): finished with status 'done'
  Created wheel for TotalSegmentator: filename=TotalSegmentator-1.5.3-py3-none-any.whl size=40473 sha256=72631d27e92da70d44e97e4309a78d20e685ff9af743f96d7e69538a655f33f7
  Stored in directory: C:\Users\butlej30383\AppData\Local\Temp\pip-ephem-wheel-cache-98sqy9xm\wheels\9f\4f\c3\aa92a6088ded23ae736534c7fd546ac5aec3409f87bbed6852
  Building wheel for p_tqdm (setup.py): started
  Building wheel for p_tqdm (setup.py): finished with status 'done'
  Created wheel for p_tqdm: filename=p_tqdm-1.4.0-py3-none-any.whl size=5411 sha256=fa28bb84f74c368e3ca9f728cac1ce3da2df3fb07f95dcf27cf8d23c317ab512
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\53\8b\76\19cce68cdb3253aee026a593ec9bc772607b85193cf65e1f53
  Building wheel for xvfbwrapper (setup.py): started
  Building wheel for xvfbwrapper (setup.py): finished with status 'done'
  Created wheel for xvfbwrapper: filename=xvfbwrapper-0.2.9-py3-none-any.whl size=5027 sha256=b15a6b7c25585d54d8fb6e75a0c52c862db0ca6335cbbb1f53a9fb4607d54d0d
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\aa\09\0e\c0fa4c721cfb0a003121597a24181add912b7488054d2311ad
  Building wheel for future (setup.py): started
  Building wheel for future (setup.py): finished with status 'done'
  Created wheel for future: filename=future-0.18.3-py3-none-any.whl size=492055 sha256=e5d845853ca1d4176cfadcbc5699dbe1277875648cb957ad91f9787813b5c77a
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\bf\5d\6a\2e53874f7ec4e2bede522385439531fafec8fafe005b5c3d1b
  Building wheel for medpy (setup.py): started
  Building wheel for medpy (setup.py): finished with status 'done'
  Created wheel for medpy: filename=MedPy-0.4.0-py3-none-any.whl size=215911 sha256=47f6a0c552cdc868104caf188bd34e85fbd5fd46a2882b6893bc782b1b948d8c
  Stored in directory: c:\users\butlej30383\appdata\local\pip\cache\wheels\41\46\a2\7c585b78f216a3dd8723dbab5f439822fa5dfbff563757a49e
Successfully built TotalSegmentator p_tqdm xvfbwrapper future medpy
Installing collected packages: xvfbwrapper, pytz, linecache2, argparse, traceback2, tifffile, threadpoolctl, scipy, PyWavelets, python-gdcm, psutil, ppft, pox, nibabel, lazy_loader, joblib, imageio, future, dill, colorama, unittest2, tqdm, scikit-learn, scikit-image, pandas, multiprocess, medpy, fury, dicom2nifti, pathos, batchgenerators, p_tqdm, nnunet-customized, TotalSegmentator
  WARNING: The scripts lsm2bin.exe, tiff2fsspec.exe, tiffcomment.exe and tifffile.exe are installed in 'C:\Users\butlej30383\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  Attempting uninstall: scipy
    Found existing installation: scipy 1.9.2
    Uninstalling scipy-1.9.2:
      Successfully uninstalled scipy-1.9.2
ERROR: Could not install packages due to an OSError: [WinError 5] Access is denied: 'C:\\Users\\butlej30383\\AppData\\Local\\NA-MIC\\Slicer 5.2.2\\lib\\Python\\Lib\\site-packages\\~cipy\\_lib\\_ccallback_c.cp39-win_amd64.pyd'
Consider using the `--user` option or check the permissions.


[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python-real.exe -m pip install --upgrade pip
[Python] Failed to compute results.
[Python] Command '['C:/Users/butlej30383/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/GitHub/SlicerTotalSegmentator/TotalSegmentator/TotalSegmentator.py", line 255, in onApplyButton
    self.logic.setupPythonRequirements()
  File "C:/GitHub/SlicerTotalSegmentator/TotalSegmentator/TotalSegmentator.py", line 624, in setupPythonRequirements
    slicer.util.pip_install(self.totalSegmentatorPythonPackageDownloadUrl)
  File "C:\Users\butlej30383\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py", line 3578, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\butlej30383\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py", line 3540, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\butlej30383\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py", line 3509, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/butlej30383/AppData/Local/NA-MIC/Slicer 5.2.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip']' returned non-zero exit status 1.
&lt;/details&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @rbumm (2023-03-14 19:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> can we not just force a restart after TS installation?</p>

---
