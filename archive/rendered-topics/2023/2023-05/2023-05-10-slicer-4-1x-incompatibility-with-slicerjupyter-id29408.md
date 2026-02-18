# Slicer 4.1x incompatibility with SlicerJupyter

**Topic ID**: 29408
**Date**: 2023-05-10
**URL**: https://discourse.slicer.org/t/slicer-4-1x-incompatibility-with-slicerjupyter/29408

---

## Post #1 by @edwardwang1 (2023-05-10 23:32 UTC)

<p>Hi all,</p>
<p>I have been using successfully using SlicerJupyter to process imaging data for the last year. Recently, my hard drive was wiped, and I have been unable to replicate my workflow. I have a couple of questions/issues:</p>
<ol>
<li>I believe that my working version of Slicer was 4.13. However, I am unable to find it in the previous releases <a href="https://www.slicer.org/wiki/Release_Details" rel="noopener nofollow ugc">page</a>. The SlicerJupyter Github <a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md" rel="noopener nofollow ugc">readme</a> still references 4.13. Does anyone know where I can find a download to this?</li>
<li>To stay consistent with my previous work, I want to continue using Slicer 4.1x instead of Slicer 5.x. Therefore, I tried to use Slicer 4.11 (I tried both the 2020 and 2021 version). I tried to use the Extension Manager to install SlicerJupyter (and that seemed to work initially). However, after trying to start the JupyterServer, I got an error while the package pywinpty was installing (see below). I did not have this issue previously. Following this <a href="https://discourse.slicer.org/t/downloading-extensions-for-older-releases/19256">thread</a> I tried installing the extension from the package specific to my slicer version, but I ran into the same issue with needing Rust. Interestingly, this was not an issue for slicer 5+.</li>
</ol>
<pre><code class="lang-auto"> Cargo, the Rust package manager, is not installed or is not on PATH.
    This package requires Rust and Cargo to compile extensions. Install it through
    the system's package manager or via https://rustup.rs/
</code></pre>
<ol start="3">
<li>I have tested this on two separate machines (both Windows 10), and I have the same issue. Both machines are connected to a hospital network.</li>
</ol>
<p>Thanks for the help,<br>
Edward</p>

---

## Post #2 by @lassoan (2023-05-11 00:02 UTC)

<aside class="quote no-group" data-username="edwardwang1" data-post="1" data-topic="29408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/858c86/48.png" class="avatar"> edwardwang1:</div>
<blockquote>
<p>I am unable to find it in the previous releases <a href="https://www.slicer.org/wiki/Release_Details">page</a>.</p>
</blockquote>
</aside>
<p>The easiest is to go back in time by specifying a date in the download page url. For example: <strong><a href="https://download.slicer.org/?date=20210530">https://download.slicer.org/?date=20210530</a></strong></p>
<p>See more information <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_older_release_of_Slicer_.3F">here</a>.</p>
<aside class="quote no-group" data-username="edwardwang1" data-post="1" data-topic="29408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/858c86/48.png" class="avatar"> edwardwang1:</div>
<blockquote>
<p>However, after trying to start the JupyterServer, I got an error while the package pywinpty was installing (see below). I did not have this issue previously.</p>
</blockquote>
</aside>
<p>It is very hard to reproduce a computing environment from several years ago. For example, it would be impossible for you to get Windows7 or an old version of Windows10 now,… Python removed all binary releases older than 3.7 and you would need to rebuild from source if you need it, etc. You cannot get any support for software versions that were replaced several years ago (unless you pay the high price of private support).</p>
<p>If you haven’t saved your computing environment into a docker container or virtual machine image then it is probably better investment of your time if you update your environment to use current software versions. Then, if you want to ensure that this environment remains available for you for several years then you can save this environment in a container or virtual machine image.</p>
<p>About the specific issues you are encountering: Unfortunately, we cannot help you investigating this, because spending time with investigating Slicer 4.x problems (that would maybe help 10 people) would directly take time away from supporting/developing Slicer-5.2 (that would help about 5000-10000 people). If you upgrade to current Slicer version and you encounter problems then we can help with that.</p>

---

## Post #3 by @edwardwang1 (2023-05-11 00:50 UTC)

<p>Hi Andras,</p>
<p>I appreciate the quick response. Lesson learned about keeping a backup of my environment. I will try using the date in the link as you say, and if it doesn’t work I will update my functions for Slicer 5.</p>

---
