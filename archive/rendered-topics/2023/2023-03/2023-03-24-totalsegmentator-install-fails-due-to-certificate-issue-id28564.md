# Totalsegmentator install fails due to certificate issue

**Topic ID**: 28564
**Date**: 2023-03-24
**URL**: https://discourse.slicer.org/t/totalsegmentator-install-fails-due-to-certificate-issue/28564

---

## Post #1 by @muratmaga (2023-03-24 19:56 UTC)

<p>This is mostly an issue on our end. I managed to download the zip archive from our end. Is there a way to manually install this?<br>
<a class="mention" href="/u/rbumm">@rbumm</a></p>
<pre><code class="lang-auto">Collecting https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))': /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))': /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))': /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))': /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))': /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))


[notice] A new release of pip is available: 23.0 -&gt; 23.0.1
[notice] To update, run: python-real.exe -m pip install --upgrade pip
[Python] Failed to compute results.
[Python] Command '['C:/Slicer 5.2.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 255, in onApplyButton
    self.logic.setupPythonRequirements()
  File "C:/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 624, in setupPythonRequirements
    slicer.util.pip_install(self.totalSegmentatorPythonPackageDownloadUrl)
  File "C:\Slicer 5.2.2\bin\Python\slicer\util.py", line 3578, in pip_install
    _executePythonModule('pip', args)
  File "C:\Slicer 5.2.2\bin\Python\slicer\util.py", line 3540, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Slicer 5.2.2\bin\Python\slicer\util.py", line 3509, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Slicer 5.2.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip']' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @rbumm (2023-03-25 06:15 UTC)

<p>No immediate idea - How did you install TotalSegmentator? From the Python Console or through the extension? You are using Linux?</p>

---

## Post #3 by @muratmaga (2023-03-25 06:24 UTC)

<p>İ installed via the extension manager (also putorch too). Pytorch threw a similar certificate error, so i downloaded the wheel and manually installed it. Pytorch works now. This is on windows.</p>

---

## Post #4 by @rbumm (2023-03-25 08:57 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="28564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><code>Could not install packages due to an OSError: HTTPSConnectionPool</code></p>
</blockquote>
</aside>
<p>Could you check <a href="https://stackoverflow.com/questions/55688358/how-to-fix-could-not-install-packages-due-to-an-environmenterror-httpsconnecti">this thread</a>? Are you maybe having issues with firewall settings or antivirus software? Please try to connect to a different network or use a VPN</p>

---

## Post #5 by @jcfr (2023-03-25 17:52 UTC)

<p>I have been discussing similar issue in a different post where I am also providing a small python snippet to help better understand.</p>
<aside class="quote quote-modified" data-post="10" data-topic="28561">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-fails-to-download-custom-sample-data/28561/10">Slicer fails to download custom sample data</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Could you try the following ? 
The snippet is expected to work in both PythonSlicer and a regular python interpreter. 
import sys
import traceback
import urllib.request


def processEvents():
    try:
        import slicer
        slicer.app.processEvents()
    except (AttributeError, ImportError):
        pass

    
def display(text, file=sys.stdout):
    processEvents()
    print(text, flush=True, file=file)

    
def error(text):
    display(text, file=sys.stderr)


for url, expected_success …
  </blockquote>
</aside>

<p>Could you try the python snippet I provide in the following context ?</p>
<ul>
<li>Python console built-in the Slicer application</li>
<li>PythonSlicer python console</li>
<li>Regular python console outside of the Slicer environment</li>
</ul>

---

## Post #6 by @rbumm (2023-03-25 19:46 UTC)

<p>Windows Powershell, same in Slicer 5.2.2</p>
<pre><code class="lang-auto">--------
Checking https://data.kitware.com
Checking https://data.kitware.com - OK
--------
Checking https://www.httpvshttps.com/
Checking https://www.httpvshttps.com/ - OK
--------
Checking https://slicer.org/
Checking https://slicer.org/ - OK
--------
Checking https://expired.badssl.com/
Checking https://expired.badssl.com/ - OK  [Expected &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)&gt;]
--------
Checking https://github.com/
Checking https://github.com/ - OK`
</code></pre>

---

## Post #7 by @lassoan (2023-03-26 02:51 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="28564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<pre><code class="lang-auto">Collecting https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))': /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))': /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))': /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))': /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
  WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)'))': /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip
ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))
</code></pre>
</blockquote>
</aside>
<p>As a workaround, you can download the package using a web browser (from the URL that is shown in the error message) and then then <code>pip install</code> that file.</p>

---

## Post #8 by @muratmaga (2023-03-28 16:29 UTC)

<p>This is the output from python console inside the slicer</p>
<pre><code class="lang-auto">Checking https://data.kitware.com
Checking https://data.kitware.com - OK
--------
Checking https://www.httpvshttps.com/
Checking https://www.httpvshttps.com/ - OK
--------
Checking https://slicer.org/
Checking https://slicer.org/ - OK
--------
Checking https://expired.badssl.com/
Checking https://expired.badssl.com/ - OK  [Expected &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)&gt;]
--------
Checking https://github.com/
Checking https://github.com/ - OK
</code></pre>

---

## Post #10 by @muratmaga (2023-03-28 16:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I just retried and pip_install local zip file seemed to work this time.</p>
<p>But i encountered another issue. Upon invoking TotalSegmentator module, module wants to update the installation from original source (even through I installed the exact version). Of course this fails with the same certificate error as the extension based install.</p>

---

## Post #11 by @lassoan (2023-03-28 17:25 UTC)

<p>Please check why the module wants to update. You should be able to see it from the stack trace but if it is not clear then you can attach Visual Studio Code’s debugger and step through the code.</p>

---

## Post #12 by @muratmaga (2023-04-03 21:12 UTC)

<p>This is from the error message if it helps:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:\Slicer 5.2.2\bin\Python\slicer\util.py", line 2967, in tryWithErrorDisplay
    yield
  File "C:/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 255, in onApplyButton
    self.logic.setupPythonRequirements()
  File "C:/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py", line 624, in setupPythonRequirements
    slicer.util.pip_install(self.totalSegmentatorPythonPackageDownloadUrl)
  File "C:\Slicer 5.2.2\bin\Python\slicer\util.py", line 3578, in pip_install
    _executePythonModule('pip', args)
  File "C:\Slicer 5.2.2\bin\Python\slicer\util.py", line 3540, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Slicer 5.2.2\bin\Python\slicer\util.py", line 3509, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Slicer 5.2.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'https://github.com/wasserth/TotalSegmentator/archive/b38eb449ad8652a987878a925203cbfa354e9b85.zip']' returned non-zero exit status 1.
</code></pre>

---

## Post #13 by @lassoan (2023-04-03 21:52 UTC)

<p>The version of TotalSegmentator is identified by the download URL because we need to install it by URL and not by version (because it is rarely updated on PyPI and version numbers of packages not on PyPI are unreliable).</p>
<p>You can disable the mechanism that installs the correct TotalSegmentator version by bypassing this check:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/blob/392c53e9f465dca07f0008495a569d077f5630bd/TotalSegmentator/TotalSegmentator.py#L640">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/392c53e9f465dca07f0008495a569d077f5630bd/TotalSegmentator/TotalSegmentator.py#L640" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/392c53e9f465dca07f0008495a569d077f5630bd/TotalSegmentator/TotalSegmentator.py#L640" target="_blank" rel="noopener">lassoan/SlicerTotalSegmentator/blob/392c53e9f465dca07f0008495a569d077f5630bd/TotalSegmentator/TotalSegmentator.py#L640</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="630" style="counter-reset: li-counter 629 ;">
          <li>    slicer.util.pip_install("matplotlib")</li>
          <li>
          </li>
<li># Install TotalSegmentator segmenter</li>
          <li>
          </li>
<li>needToInstallSegmenter = False</li>
          <li>try:</li>
          <li>    import totalsegmentator</li>
          <li>    if not upgrade:</li>
          <li>        # Check if we need to update TotalSegmentator Python package version</li>
          <li>        downloadUrl = self.installedTotalSegmentatorPythonPackageDownloadUrl()</li>
          <li class="selected">        if downloadUrl and (downloadUrl != self.totalSegmentatorPythonPackageDownloadUrl):</li>
          <li>            # TotalSegmentator have been already installed from GitHub, from a different URL that this module needs</li>
          <li>            if not slicer.util.confirmOkCancelDisplay(</li>
          <li>                f"This module requires TotalSegmentator Python package update.",</li>
          <li>                detailedText=f"Currently installed: {downloadUrl}\n\nRequired: {self.totalSegmentatorPythonPackageDownloadUrl}"):</li>
          <li>              raise ValueError('TotalSegmentator update was cancelled.')</li>
          <li>            upgrade = True</li>
          <li>except ModuleNotFoundError as e:</li>
          <li>    needToInstallSegmenter = True</li>
          <li>
          </li>
<li>if needToInstallSegmenter or upgrade:</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This will allow you to move a bit further.</p>

---
