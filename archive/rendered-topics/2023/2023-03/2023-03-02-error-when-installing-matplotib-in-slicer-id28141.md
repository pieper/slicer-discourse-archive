# Error when installing matplotib in Slicer

**Topic ID**: 28141
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/error-when-installing-matplotib-in-slicer/28141

---

## Post #1 by @hapkx (2023-03-02 12:25 UTC)

<p>I’m trying to install matplotlib package in python-interactor in Slicer 5.0.2 with the following commands:</p>
<pre><code class="lang-auto">from slicer.util import pip_install
pip_install("matplotlib")
import matplotlib.pyplot as plt
</code></pre>
<p>I get the following error:</p>
<pre><code class="lang-auto">WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/matplotlib/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/matplotlib/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/matplotlib/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/matplotlib/
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/matplotlib/
Could not fetch URL https://pypi.org/simple/matplotlib/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/matplotlib/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
ERROR: Could not find a version that satisfies the requirement matplotlib (from versions: none)
ERROR: No matching distribution found for matplotlib
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
Traceback (most recent call last):
  File "D:/DESKTOP/ex/module3/module3.py", line 480, in readPic
    pip_install("matplotlib")
  File "E:\Slicer 5.0.2\bin\Python\slicer\util.py", line 3431, in pip_install
    _executePythonModule('pip', args)
  File "E:\Slicer 5.0.2\bin\Python\slicer\util.py", line 3394, in _executePythonModule
    logProcessOutput(proc)
  File "E:\Slicer 5.0.2\bin\Python\slicer\util.py", line 3363, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['E:/Slicer 5.0.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'matplotlib']' returned non-zero exit status 1.
...
</code></pre>
<p>as shown in the picture:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/493dc4a91f365eeaf6e24861fbacd398c4863df8.png" data-download-href="/uploads/short-url/arVbYkdBATVfESTpbhLMzJOBXsI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/493dc4a91f365eeaf6e24861fbacd398c4863df8.png" alt="image" data-base62-sha1="arVbYkdBATVfESTpbhLMzJOBXsI" width="690" height="271" data-dominant-color="F2EEEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1340×528 50.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-03-02 12:31 UTC)

<p>There seems to be an SSL error. There could be many reasons. Using the current Slicer version (5.2.2) may fix the problem. Let us know if the problem occurs in current Slicer version, too.</p>

---

## Post #3 by @hapkx (2023-03-02 14:26 UTC)

<p>Yes, it still occurs…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a37b2c9209568a721677f52b94351e1d1bfaa8ff.png" data-download-href="/uploads/short-url/nkdJ4whQgzZCRSi2hyKH9YlwpoX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a37b2c9209568a721677f52b94351e1d1bfaa8ff.png" alt="image" data-base62-sha1="nkdJ4whQgzZCRSi2hyKH9YlwpoX" width="690" height="259" data-dominant-color="F3EFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1397×525 50.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @cpinter (2023-03-02 16:27 UTC)

<p>I encountered something very similar when I started a clean build of a Slicer custom app. This was the original error:</p>
<pre><code class="lang-auto">  Performing install step for 'python-pip'
  CMake Error at E:/t/tR/slicersources-build/python-pip-prefix/src/python-pip-stamp/python-pip-install-Release.cmake:49 (message):
    Command failed: 1
     'E:/t/tR/python-install/bin/PythonSlicer.exe' '-m' 'pip' 'install' '--require-hashes' '-r' 'E:/t/tR/python-pip-requirements.txt'
    See also
      E:/t/tR/slicersources-build/python-pip-prefix/src/python-pip-stamp/python-pip-install-*.log 
</code></pre>
<p>In the log file there was something like this:</p>
<pre><code class="lang-auto">  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)'))': /packages/15/d8/dd071918c040f50fa1cf80da16423af51ff8ce4a0f2399b7bf8de45ac3d9/nose-1.3.7-py3-none-any.whl
  WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)'))': /packages/15/d8/dd071918c040f50fa1cf80da16423af51ff8ce4a0f2399b7bf8de45ac3d9/nose-1.3.7-py3-none-any.whl
  WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)'))': /packages/15/d8/dd071918c040f50fa1cf80da16423af51ff8ce4a0f2399b7bf8de45ac3d9/nose-1.3.7-py3-none-any.whl
  WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)'))': /packages/15/d8/dd071918c040f50fa1cf80da16423af51ff8ce4a0f2399b7bf8de45ac3d9/nose-1.3.7-py3-none-any.whl
  WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)'))': /packages/15/d8/dd071918c040f50fa1cf80da16423af51ff8ce4a0f2399b7bf8de45ac3d9/nose-1.3.7-py3-none-any.whl
ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Max retries exceeded with url: /packages/15/d8/dd071918c040f50fa1cf80da16423af51ff8ce4a0f2399b7bf8de45ac3d9/nose-1.3.7-py3-none-any.whl (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)')))

WARNING: You are using pip version 22.0.3; however, version 23.0.1 is available.
You should consider upgrading via the 'E:\dt\dR\python-install\bin\python.exe -m pip install --upgrade pip' command.
</code></pre>
<p>First it happened with <code>python-setuptools</code> then <code>python-pip</code>, without changing anything. In the latter case it complained about pip version so I copied over the pip to site-packages from another, formerly successful build and then the build continued, but the same type of error happened with <code>python-numpy</code>, so I figured the problem is more central. Then I tried building another custom app, and the problem was the same, although that custom app was built successfully before. I think something may have changed in the infrastructure in the past 5-10 days.</p>
<p>Next I’m building a Slicer on the same machine, and will start both a custom app and a Slicer build on another machine on another network to try to pinpoint the issue, but I thought it’d be useful to share this info now in case it helps.</p>

---

## Post #5 by @hapkx (2023-03-02 16:40 UTC)

<p>Thanks for sharing <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=12" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20">. Let’s wait for a solution.</p>

---

## Post #6 by @lassoan (2023-03-03 06:13 UTC)

<p>Try to disable third-party antivirus software if you have any (see <a href="https://stackoverflow.com/questions/61990284/pip-install-fails-with-connection-error-ssl-problem">here</a>). It might also worth trying <a href="https://marin-kitagawa.devlifematter.org/answer/error-when-use-pipwarning-retrying-retry-total=4-connect=none-read=none-redirect=none-status=none-after-connection-broken-by-readtimeouterror-httpscon-9508">this</a>.</p>

---

## Post #7 by @cpinter (2023-03-03 11:01 UTC)

<p>I built regular Slicer (latest commit) and it failed the same way. At the same time on a different computer/network the build succeeded. It is a home computer so there should be no network limitations but evidently there is something. Thanks for the suggestions <a class="mention" href="/u/lassoan">@lassoan</a> I’ll look into those.</p>

---

## Post #8 by @cpinter (2023-03-03 12:00 UTC)

<p>I didn’t have any 3rd party antivirus, but trying the second link worked (in the sense that pip installing matplotlib as mentioned first in this topic succeeded).</p>
<p>In summary, the file <code>c:\Windows\System32\Drivers\etc\hosts</code> had to be opened with a text editor started as administrator, then these two lines added to the end:</p>
<pre><code class="lang-auto">151.101.0.223 pypi.org
151.101.1.63 files.pythonhosted.org
</code></pre>
<p>I’m building Slicer and the custom apps to confirm that everything works.</p>
<p>I’m a bit puzzled, because I didn’t install any relevant-looking application lately, nor have I made changes in firewall or other network settings, didn’t change internet providers etc, so all in all there have been no changes. Still, using pip worked perfectly before, and suddenly this problem started occurring. It would be interesting to know what caused it. But it’s great that it seems to be working now (pending the builds), thanks a lot <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---

## Post #9 by @cpinter (2023-03-03 14:40 UTC)

<p><a class="mention" href="/u/hapkx">@hapkx</a> I marked Andras’ suggestion solution because it helped me, but please confirm it works for you as well, since this topic is coming from your side.</p>

---

## Post #10 by @hapkx (2023-03-03 18:11 UTC)

<p>The second one works! Thank you! <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=12" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"></p>

---

## Post #11 by @lassoan (2023-03-04 03:16 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> I’m just curious, do you have optical fiber connection to your internet service provider? Does disabling “TCP and UDP Checksum Offload for IPv6” (or TCP/IPv6 protocol completely) fixes the issue as well?</p>
<p><em>From <a href="https://www.reddit.com/r/Fios/comments/xo55n4/verizon_just_activated_ipv6_turning_off_ipv6_tcp/">https://www.reddit.com/r/Fios/comments/xo55n4/verizon_just_activated_ipv6_turning_off_ipv6_tcp/</a> :</em></p>
<ol>
<li>Open the “Network Connections” page of the Windows Control Panel.</li>
<li>Open the “Properties” dialog of the NIC.</li>
<li>Select “Configure…” to open the NIC’s configuration.</li>
<li>Navigate to the Advanced tab and disable “TCP and UDP Checksum Offload for IPv6”.</li>
</ol>

---

## Post #12 by @cpinter (2023-03-06 15:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="28141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>do you have optical fiber connection to your internet service provider?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="28141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does disabling “TCP and UDP Checksum Offload for IPv6” (or TCP/IPv6 protocol completely) fixes the issue as well?</p>
</blockquote>
</aside>
<p>Well, maybe I need some help. My Windows is set to English, but it was originally Spanish, and some parts are apparently not converted to English. Here’s the page in question:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aedd241198e3179effa16729044a4db4e980bad7.png" alt="image" data-base62-sha1="oWUS46VjCQOAIrXgIFEfG3lifpJ" width="400" height="455"></p>
<p>I guess the checksum offload is the one selected. But there are five of them, and Windows doesn’t let me resize this window and there are no tooltips either to see the end of these strings. I don’t want to just disable all of them because I don’t want to potentially break something.</p>
<p>Can you please check on your machine what are these four exactly? Maybe then we can guess the order of these and I can disable just the TCP and UDP ones.</p>

---

## Post #13 by @cpinter (2023-03-06 15:17 UTC)

<p>Well considering what could break I gave it a go anyway. I disabled all five, and it did not fix the issue.</p>

---

## Post #14 by @lassoan (2023-03-06 16:02 UTC)

<p>Here is my network interface properties list:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd7ff6040e18f9a38a65fc78ca1e7741cc2c24ae.png" data-download-href="/uploads/short-url/r2ooCq3xf0OOSbf8qAaEVwrfJHo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd7ff6040e18f9a38a65fc78ca1e7741cc2c24ae.png" alt="image" data-base62-sha1="r2ooCq3xf0OOSbf8qAaEVwrfJHo" width="431" height="500" data-dominant-color="EEF0F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">595×689 17.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a73ab87e3e79d177f461da525b00bb0be095edbc.png" data-download-href="/uploads/short-url/nRnxQX91WslvkGpiQCP02JQ62jG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a73ab87e3e79d177f461da525b00bb0be095edbc.png" alt="image" data-base62-sha1="nRnxQX91WslvkGpiQCP02JQ62jG" width="431" height="500" data-dominant-color="F1F1F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">595×689 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can try temporarily disabling TCP/IPv6 to see if it makes a difference, just for testing.</p>

---

## Post #15 by @cpinter (2023-03-07 10:24 UTC)

<p>OK I’ll try to disable IPv6 when appropriate. <a class="mention" href="/u/hapkx">@hapkx</a> if you’d like to help out you could try this one.</p>

---
