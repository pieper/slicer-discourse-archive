# Error when TotalSegmentator trying to install required Python packages: `SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))`

**Topic ID**: 34539
**Date**: 2024-02-26
**URL**: https://discourse.slicer.org/t/error-when-totalsegmentator-trying-to-install-required-python-packages-sslerror-ssleoferror-8-eof-occurred-in-violation-of-protocol-ssl-c-1129/34539

---

## Post #1 by @rnvwnvvir (2024-02-26 11:42 UTC)

<p>Hello,my slicer is 3.6.1.The following error occurs when using TotalSegmentator. Restart is unuseful.Thanks for your help.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae8d1ffb75b6b8b2ed84f25bede032ff517be608.png" alt="联想截图_20240223163912" data-base62-sha1="oU9rc5gVqszi6aP64uIuunnREkE" width="632" height="232"></p>

---

## Post #2 by @lassoan (2024-02-26 15:53 UTC)

<p>If the error does not go away after restarting Slicer, it means that there is some trouble with installing the required Python packages in your Slicer application. You can find more details in the application log that will help you resolving the problem. For example, if you find that you are running out of disk space while trying to install a package then you need to make more free space on your disk.</p>

---

## Post #3 by @jamesobutler (2024-02-26 16:38 UTC)

<p>Having uninstalled Slicer 5.6.1 and deleted the entire directory:<br>
%LOCALAPPDATA%/slicer.org/Slicer 5.6.1</p>
<p>Then deleting my entire python pip cache at:<br>
%LOCALAPPDATA%/pip</p>
<p>Then deleting my TotalSegmentator cache at:<br>
%USERPROFILE%/.totalsegmentator</p>
<p>I reinstalled Slicer 5.6.1, installed the TotalSegmentator Slicer extension and then re-ran TotalSegmentator on the CTChest sample data set, I was successful running TotalSegmentator:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1467d0070bc15a29ef8abe9155a8ba63424109fa.png" data-download-href="/uploads/short-url/2UvXWK6p4C9ErbjWYpI35Jat1O2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1467d0070bc15a29ef8abe9155a8ba63424109fa_2_690x373.png" alt="image" data-base62-sha1="2UvXWK6p4C9ErbjWYpI35Jat1O2" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1467d0070bc15a29ef8abe9155a8ba63424109fa_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1467d0070bc15a29ef8abe9155a8ba63424109fa_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/1467d0070bc15a29ef8abe9155a8ba63424109fa_2_1380x746.png 2x" data-dominant-color="A3A1A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/rnvwnvvir">@rnvwnvvir</a> If you follow the same steps as I did below, you should be able to observe similar success.</p>

---

## Post #4 by @rnvwnvvir (2024-02-27 02:06 UTC)

<p>Thank you, James Butler.I have uninstalled Slicer 5.6.1 and delete all files about slicer 5.6.1.Trying to reinstall the Slicer.But the problem still exist.Below is its error log.I don’t know what the problem is.</p>
<p>Python 3.9.10 (main, Dec 12 2023, 02:25:18) [MSC v.1935 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/pandas/<br>
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/pandas/<br>
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/pandas/<br>
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/pandas/<br>
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/pandas/<br>
Could not fetch URL <a href="https://pypi.org/simple/pandas/:" rel="noopener nofollow ugc">https://pypi.org/simple/pandas/:</a> There was a problem confirming the ssl certificate: HTTPSConnectionPool(host=‘<a href="http://pypi.org" rel="noopener nofollow ugc">pypi.org</a>’, port=443): Max retries exceeded with url: /simple/pandas/ (Caused by SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))) - skipping<br>
ERROR: Could not find a version that satisfies the requirement pandas (from versions: none)<br>
ERROR: No matching distribution found for pandas<br>
Traceback (most recent call last):<br>
File “D:/LeStoreDownload/3dslicer/Slicer 5.6.1/slicer.org/Extensions-32438/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 665, in setupPythonRequirements<br>
import pandas<br>
ModuleNotFoundError: No module named ‘pandas’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “D:/LeStoreDownload/3dslicer/Slicer 5.6.1/slicer.org/Extensions-32438/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 268, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “D:/LeStoreDownload/3dslicer/Slicer 5.6.1/slicer.org/Extensions-32438/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 667, in setupPythonRequirements<br>
slicer.util.pip_install(“pandas”)<br>
File “D:\LeStoreDownload\3dslicer\Slicer 5.6.1\bin\Python\slicer\util.py”, line 3887, in pip_install<br>
_executePythonModule(“pip”, args)<br>
File “D:\LeStoreDownload\3dslicer\Slicer 5.6.1\bin\Python\slicer\util.py”, line 3848, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “D:\LeStoreDownload\3dslicer\Slicer 5.6.1\bin\Python\slicer\util.py”, line 3814, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘D:/LeStoreDownload/3dslicer/Slicer 5.6.1/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pandas’]’ returned non-zero exit status 1.</p>

---

## Post #5 by @rnvwnvvir (2024-02-27 02:08 UTC)

<p>Thank you, Andras Lasso.Re-running will still cause problems.The error log is as follows.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b7551edcea87e9de13cdad36d07a3f5791a4700.png" data-download-href="/uploads/short-url/1DmBLJ933OMtlY8zm8MVTWdmONW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b7551edcea87e9de13cdad36d07a3f5791a4700_2_690x356.png" alt="image" data-base62-sha1="1DmBLJ933OMtlY8zm8MVTWdmONW" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b7551edcea87e9de13cdad36d07a3f5791a4700_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b7551edcea87e9de13cdad36d07a3f5791a4700_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b7551edcea87e9de13cdad36d07a3f5791a4700_2_1380x712.png 2x" data-dominant-color="D9D5D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×993 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2024-02-27 03:53 UTC)

<p>It seems that your internet connection is failing. How do you connect to the internet?</p>

---

## Post #7 by @jamesobutler (2024-02-27 03:58 UTC)

<p>This may be related to the issue of ZScaler getting in the way. <a class="mention" href="/u/rnvwnvvir">@rnvwnvvir</a> does your computer have ZScaler running when this happens? I have observed a similar error trying to download PyTorch when I’m at home and using my corporate laptop which forces ZScaler to be running. When I’m physically at my workplace and on the corporate network ZScaler doesn’t run and there is no issue. When I’m home it doesn’t allow me to turn ZScaler off as I have to enter in special credentials which I don’t have to do that action.</p>
<aside class="quote quote-modified" data-post="22" data-topic="33809">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/sandbox-module-cannot-be-downloaded-via-extension-manager-today/33809/22">Sandbox module cannot be downloaded via extension manager today?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Great detective work! I think this explains the all the issues that you have been experiencing. 
It seems that ZScaler implements a man-in-the-middle attack on all external network communications. According <a href="https://geekingfrog.com/blog/post/corporate-man-in-the-middle" rel="noopener nofollow ugc">this blog post</a> ZScaler does not generate generally trustable certificates, just some temporary throwaway ones. The ZScaler agent running on the user’s computer receives these temporary certificates and regularly replaces them on the system. 
I’m very surprised that hospitals go this far and d…
  </blockquote>
</aside>


---

## Post #9 by @shar486 (2024-04-16 07:10 UTC)

<p>Hello, did you find the solution? I had the same problem, and it didn’t help to use the methods discussed above. I think it’s because we lack pandas packs, but I don’t know where to install them.</p>

---

## Post #10 by @rnvwnvvir (2024-04-22 09:31 UTC)

<p>Sorry,I don’t solve the problem</p>

---

## Post #11 by @zhang_zhixiong (2024-09-23 03:52 UTC)

<p>I had the same problem. Did you solve it?</p>

---

## Post #12 by @lassoan (2024-09-23 04:36 UTC)

<p>Most likely these errors are caused by your IT administrators monitoring and restricting your internet access, therefore it is mainly their responsibility to help you with resolving any side effects, such as applications not being able to download additional plugins or data.</p>
<p>There are two main workarounds:</p>
<ul>
<li>Option A: Download all required components (Slicer extension packages, AI models) manually, using your web browser. This works, because IT administrators in corporate and hospital environments usually set up monitoring and filtering of all your internet traffic via your web browser, therefore they usually allow access to more sites for your web browser than for other applications (such as 3D Slicer).</li>
<li>Option B: Run Slicer on a computer with less restricted internet access and install all the extensions you need. Once all the components are downloaded, Slicer will not need internet access, so you will be able to run the AI tool on any computer. You can even transfer the installed Slicer to any other computer (the Slicer installation folder is portable between computers, no installation is needed).</li>
</ul>

---
