---
topic_id: 38410
title: "How To Install A Package"
date: 2024-09-17
url: https://discourse.slicer.org/t/38410
---

# How to install a package

**Topic ID**: 38410
**Date**: 2024-09-17
**URL**: https://discourse.slicer.org/t/how-to-install-a-package/38410

---

## Post #1 by @maniron (2024-09-17 12:50 UTC)

<p>I am trying to install a package named spatial_correlation-sampler, but the installation is not going through “error: legacy-install-failure”</p>
<p>I ran PythonSlicer.exe -m pip install spatial_correlation-sampler</p>
<p>ModuleNotFoundError: No module named ‘spatial_correlation_sampler’</p>
<p>I tried installing but facing issue<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ab75fb29a9dbbc81e7f5c74ab2d11a3ee7ba087.png" data-download-href="/uploads/short-url/65SVGhskMAqZAZhwIlbatPumNjp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ab75fb29a9dbbc81e7f5c74ab2d11a3ee7ba087.png" alt="image" data-base62-sha1="65SVGhskMAqZAZhwIlbatPumNjp" width="690" height="77" data-dominant-color="FCF4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">975×109 5.03 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-09-17 14:53 UTC)

<p>in that python window try<br>
<code>pip_install("spatial_correlation_sampler")</code></p>
<p>and you will probbaly see the actual error why it is not installed?</p>

---

## Post #3 by @maniron (2024-09-18 05:04 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="2" data-topic="38410">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>pip_install(“spatial_correlation_sampler”)</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> I am still facing the same issue as mentioned first</p>
<p>“OSError: CUDA_HOME environment variable is not set. Please set it to your CUDA install root.”</p>
<p>But I have set this as env variable</p>

---

## Post #4 by @muratmaga (2024-09-18 15:00 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="2" data-topic="38410">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>pip_install(“spatial_correlation_sampler”)</p>
</blockquote>
</aside>
<p>This is on my mac. It looks like this pywheel requires building from scratch, and it is not finding some of the build packages as far as I can tell. You will need to to dig deeper into the package to find what those are and why they are failing under slicer (or not being installed).</p>
<pre><code class="lang-auto">&gt;&gt;&gt; pip_install("spatial_correlation_sampler")
Collecting spatial_correlation_sampler
  Downloading spatial_correlation_sampler-0.5.0.tar.gz (9.8 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Gettin
&gt;&gt;&gt; g requirements to build wheel: finished with status 'error'
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3887, in pip_install
    _executePythonModule("pip", args)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3848, in _executePythonModule
    logProcessOutput(proc)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 3814, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'spatial_correlation_sampler']' returned non-zero exit status 1.```</code></pre>

---

## Post #5 by @maniron (2024-09-19 04:08 UTC)

<p>Currently I tried installing this package in windows , where the issue is coming, but when I install the same package where I have deployed slicer in ubuntu machine, there the installation didnt have any issue</p>

---
