---
topic_id: 25678
title: "Ai Segmentation With Lung Ct Analyzer Error"
date: 2022-10-13
url: https://discourse.slicer.org/t/25678
---

# AI segmentation with lung CT analyzer error

**Topic ID**: 25678
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/ai-segmentation-with-lung-ct-analyzer-error/25678

---

## Post #1 by @MMdeB (2022-10-13 11:44 UTC)

<p>Hi, I’ve been trying to use the Lung CT Analyzer extension with the AI segmentation ‘lung mask’, but I cannot get it to work. First, an error occurred that ‘torch was not present’, but I solved this by installing PyTorch extension in slicer (and then install pytorch via this module). However, afterwards I still get an error when I try to segment the lung.</p>
<p>First, when I press apply, I get a warning:</p>
<blockquote>
<p>pytorch CUDA is not found on your system. The AI processing will last 3-10 minutes. Do you want to continue?</p>
</blockquote>
<p>If I press OK, I will get the following error:</p>
<blockquote>
<p>Failed to compute results: Command ‘[‘C:/Users/mmdeboer/AppData/Local/NA-MIC/Slicer 5.0.3/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘git+https://github.com/JoHof/lungmask’]’ returned non-zero exit status 1.</p>
</blockquote>
<p>What do I have to do to solve this error? Thanks in advance!</p>

---

## Post #2 by @rbumm (2022-10-13 11:59 UTC)

<aside class="quote no-group quote-modified" data-username="MMdeB" data-post="1" data-topic="25678" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mmdeb/48/16912_2.png" class="avatar"> MMdeB:</div>
<blockquote>
<p>First, when I press apply, I get a warning:</p>
<blockquote>
<p>pytorch CUDA is not found on your system. The AI processing will last 3-10 minutes. Do you want to continue?</p>
</blockquote>
</blockquote>
</aside>
<p>What GPU do you have in use?<br>
Message 1 is normal if you have no GPU or a GPU that does not support CUDA. CUDA needs an Nvidia GPU.</p>
<aside class="quote no-group quote-modified" data-username="MMdeB" data-post="1" data-topic="25678" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mmdeb/48/16912_2.png" class="avatar"> MMdeB:</div>
<blockquote>
<p>If I press OK, I will get the following error:</p>
<blockquote>
<p>Failed to compute results: Command ‘[‘C:/Users/mmdeboer/AppData/Local/NA-MIC/Slicer 5.0.3/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘git+https://github.com/JoHof/lungmask’]’ returned non-zero exit status 1.</p>
</blockquote>
<p>What do I have to do to solve this error? Thanks in advance!</p>
</blockquote>
</aside>
<p>This is strange.<br>
Could you restart Slicer and paste</p>
<pre><code class="lang-auto">slicer.util.pip_install("git+https://github.com/JoHof/lungmask")
</code></pre>
<p>into the Python Interactor, press return, and post the result?<br>
Thank you.</p>

---

## Post #3 by @Filipe_Pagaimo (2023-02-15 00:30 UTC)

<p>Hi, I am facing a similar problem. My laptop has a NVDIA GeForce RTX 3050 Ti.</p>
<p>When pasting the suggested line on the Python console:</p>
<blockquote>
<p>slicer.util.pip_install(“git+https://github.com/JoHof/lungmask”)</p>
</blockquote>
<p>I get the message:</p>
<blockquote>
<p>Collecting git+https://github.com/JoHof/lungmask<br>
Cloning <a href="https://github.com/JoHof/lungmask" class="inline-onebox" rel="noopener nofollow ugc">GitHub - JoHof/lungmask: Automated lung segmentation in CT</a> to c:\users\pagai\appdata\local\temp\pip-req-build-y_ut0tcq<br>
ERROR: Error [WinError 2] The system cannot find the file specified while executing command git version<br>
ERROR: Cannot find command ‘git’ - do you have ‘git’ installed and in your PATH?</p>
<p>[notice] A new release of pip available: 22.3 → 23.0<br>
[notice] To update, run: python-real.exe -m pip install --upgrade pip</p>
</blockquote>
<p>Thank you</p>

---

## Post #4 by @lassoan (2023-02-15 05:10 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="2" data-topic="25678">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p><code>slicer.util.pip_install("git+https://github.com/JoHof/lungmask")</code></p>
</blockquote>
</aside>
<p><a class="mention" href="/u/rbumm">@rbumm</a> It is important to note that users don’t have git installed on their system. You can install git relatively easily on Windows (see complete implementation <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/5cc78d783b64fda32d32a2b96d4499b0d2533863">here</a>), but I don’t think there is no easy/standard solution that works on all linux and macOS configurations. It is easier to install from the zip file that github provides (as shown <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/1eb9aa7df8f07fac6f080ea4c6f59b6ccd4d75a6#diff-25cf74003570e77f7e900eb7a84476163d86e68f055332dbca69ed0293f03a92R519">here</a>) because then you don’t need git at all.</p>
<p>Note that the disadvantage of using git+https or git .zip format is that if the URL does not change (e.g., because you use the latest main version) then pip will just use the latest cached version. Therefore, instead of using a branch name, I would recommend to use a specific git hash, as it is done <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/d9b4f6e7a2eae05d099836aa8d314a59df066262#diff-25cf74003570e77f7e900eb7a84476163d86e68f055332dbca69ed0293f03a92R301">here</a>.</p>
<p>All these issues are solved if the maintainer uploads a package to PyPI. If the maintainer of this package does not do it then you may enter an issue in the repository’s bugtracker to request this.</p>

---

## Post #5 by @rbumm (2023-02-15 08:23 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>, very helpful.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25678">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>All these issues are solved if the maintainer uploads a package to PyPI. If the maintainer of this package does not do it then you may enter an issue in the repository’s bug tracker to request this.</p>
</blockquote>
</aside>
<p>How are these issues solved then? Will <code> slicer.util.pip_install()</code>  recognize the latest version?</p>
<p>Sidenote: <code>slicer.util.pip_uninstall()</code>  only works in 5.2.1 if you do a <code>slicer.util.restart()</code> afterward.</p>

---

## Post #6 by @lassoan (2023-02-15 15:05 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="25678">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>How are these issues solved then? Will <code> slicer.util.pip_install()</code> recognize the latest version?</p>
</blockquote>
</aside>
<p>pip handles download, install, versioning, resolving version requirements, etc. <code>pip_install</code> will install the package according to the requirements that you specify. If you don’t specify any requirement then it just makes sure that some version of the package is installed. If you specify <code>--upgrade</code> then it’ll install the latest one. If you specify a version range then it’ll choose a version in that range.</p>
<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="25678">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Sidenote: <code>slicer.util.pip_uninstall()</code> only works in 5.2.1 if you do a <code>slicer.util.restart()</code> afterward.</p>
</blockquote>
</aside>
<p>Yes, if a Python package is already loaded then installing a new version will not change anything, as the Python scripts from the previous version are already loaded.</p>
<p>Note that <code>pip_uninstall</code> may fail if the Python package is in use and it contains shared libraries (DLLs). If you want to make uninstallation work, you would need to quit Slicer and run <code>PythonSlicer -m pip uninstall ...</code>, but often uninstalling while Slicer is running and then restarting is enough (and it is much easier to do than running some Python scripts outside Slicer). If Python package uninstallation was commonly needed then we could implement some mechanism to do it at Slicer application startup (before initializing Python, by launching the external PythonSlicer interpreter).</p>

---

## Post #7 by @Johan_Diaz_Tovar (2023-12-09 09:23 UTC)

<p>Hello everyone, I recently updated 3D slicer to the version 5.60 and when I’m trying to use the Lung CT Segmenter extension (which it was working before) I’m getting this error:</p>
<p>Failed to compute results: module ‘torch.backends’ has no attribute ‘mps’</p>
<p>I already checked the updates for PyTorch and the lungmask library, I even installed the version where it was working before (5.40) but even doing that it is not working and giving me the same error, what do you thinkg I can do…</p>
<p>I’m using 3D slicer in a Mac</p>

---

## Post #8 by @rbumm (2023-12-09 18:01 UTC)

<p>Please report this error on the <a href="https://github.com/JoHof/lungmask">lungmask GitHub</a>  under issues. Can not reproduce that on a PC. The last version of lungmask obviously “adds support for mps (apple metal)”. If the problem can not be solved by the developer we will switch to an earlier version of lungmask.</p>

---

## Post #9 by @Johan_Diaz_Tovar (2023-12-10 19:59 UTC)

<p>I reported there, thanks!</p>
<p>The version of Lungmask currently being used in my 3D slicer is the 0.2.18</p>

---

## Post #10 by @rbumm (2023-12-11 10:03 UTC)

<p>Can you try to use the Pytorch extension and install Pytorch in CPU mode ? Do you still get the error then ?</p>

---

## Post #11 by @rbumm (2023-12-11 16:52 UTC)

<p>You could always install an earlier version of lungmask from the Python console:</p>
<pre><code class="lang-auto">slicer.util.pip_uninstall("lungmask")
slicer.util.pip_install("https://github.com/JoHof/lungmask/archive/18cfc8967501dc84c844d17594b711c0a8e4711b.zip")
# restart slicer

</code></pre>
<p>This will install lungmask 0.2.17</p>

---

## Post #12 by @Johan_Diaz_Tovar (2023-12-11 18:47 UTC)

<p>Yes, I tried this before, it was set as automatic, I used the CPU mode same error</p>

---

## Post #13 by @Johan_Diaz_Tovar (2023-12-11 19:02 UTC)

<p>Thank you so much!<br>
It defenitly solved the error, going back to the last version works</p>

---

## Post #14 by @Daniel_Lo (2024-09-25 05:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c8e84c821206408d0cdb5478685b3141c69d962.jpeg" data-download-href="/uploads/short-url/fukUwsm3G5OGeghDJUgZShOiWRQ.jpeg?dl=1" title="Screenshot 2024-09-25 at 13.28.21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c8e84c821206408d0cdb5478685b3141c69d962_2_690x364.jpeg" alt="Screenshot 2024-09-25 at 13.28.21" data-base62-sha1="fukUwsm3G5OGeghDJUgZShOiWRQ" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c8e84c821206408d0cdb5478685b3141c69d962_2_690x364.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c8e84c821206408d0cdb5478685b3141c69d962_2_1035x546.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c8e84c821206408d0cdb5478685b3141c69d962_2_1380x728.jpeg 2x" data-dominant-color="AFAEB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-09-25 at 13.28.21</span><span class="informations">1920×1013 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>this happened when i used AI segmentation for Lung CT segmenter</p>

---
