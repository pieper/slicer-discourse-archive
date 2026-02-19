---
topic_id: 13536
title: "Simpleitk Tries To Write Python Wrapped Files Into A Default"
date: 2020-09-18
url: https://discourse.slicer.org/t/13536
---

# SimpleITK tries to write Python wrapped files into a default folder that needs root privileges

**Topic ID**: 13536
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/simpleitk-tries-to-write-python-wrapped-files-into-a-default-folder-that-needs-root-privileges/13536

---

## Post #1 by @myousefi2016 (2020-09-18 07:01 UTC)

<p>I’m trying to bake Slicer 4.11 from the source and use my system installed Python 3.6. This is my cmake command:</p>
<pre><code class="lang-auto">cmake -DCMAKE_INSTALL_PREFIX=/scratch1/yousefi/Slicer-Install/ -DSlicer_USE_SYSTEM_python=ON -DSlicer_USE_SYSTEM_OpenSSL=ON -G Ninja ../Slicer
</code></pre>
<p>It just compiles fine until installing step of SimpleITK that shows this error:</p>
<pre><code class="lang-auto">[351/362] Performing install step for 'SimpleITK'
-- SimpleITK: Removing 'install' log files
-- SimpleITK: SimpleITK_WORKING_DIR: /scratch1/yousefi/Slicer-SuperBuild-Debug/SimpleITK-build/SimpleITK-build/Wrapping/Python
-- SimpleITK: /bin/python3.6;setup.py;install
-- SimpleITK: Errors detected - See below.
running install

error: can't create or remove files in install directory

The following error occurred while trying to add or remove files in the
installation directory:

    [Errno 2] No such file or directory: '/usr/local/lib64/python3.6/site-packages/test-easy-install-3462044.write-test'

The installation directory you specified (via --install-dir, --prefix, or
the distutils default setting) was:

    /usr/local/lib64/python3.6/site-packages/

This directory does not currently exist.  Please create it and try again, or
choose a different installation directory (using the -d or --install-dir
option).


CMake Error at /scratch1/yousefi/Slicer/CMake/ExternalProjectForNonCMakeProject.cmake:104 (message):
  SimpleITK: install step failed with exit code '1'.

  Outputs also captured in
  /scratch1/yousefi/Slicer-SuperBuild-Debug/SimpleITK_install_step_output.txt
  and
  /scratch1/yousefi/Slicer-SuperBuild-Debug/SimpleITK_install_step_error.txt.


  Setting env.  variable EP_EXECUTE_DISABLE_CAPTURE_OUTPUTS to 1 allows to
  disable file capture.

Call Stack (most recent call first):
  /scratch1/yousefi/Slicer-SuperBuild-Debug/SimpleITK_install_step.cmake:3 (ExternalProject_Execute)


FAILED: SimpleITK-prefix/src/SimpleITK-stamp/SimpleITK-install 
cd /scratch1/yousefi/Slicer-SuperBuild-Debug/SimpleITK-build &amp;&amp; /scratch1/yousefi/cmake-3.18.2-Linux-x86_64/bin/cmake -P /scratch1/yousefi/Slicer-SuperBuild-Debug/SimpleITK_install_step.cmake &amp;&amp; /scratch1/yousefi/cmake-3.18.2-Linux-x86_64/bin/cmake -E touch /scratch1/yousefi/Slicer-SuperBuild-Debug/SimpleITK-prefix/src/SimpleITK-stamp/SimpleITK-install
ninja: build stopped: subcommand failed.
</code></pre>
<p>It seems that it tries to write some files into the <code>/usr/local/lib64/python3.6/site-packages/</code> which I don’t have the privilege to write. In fact, I’m not an admin in our cluster. Any idea how to fix it?</p>

---

## Post #2 by @Alex_Vergara (2020-09-18 07:10 UTC)

<p>There is no benefits in using your own system python. None at all. Try using the bundled python inside slicer.</p>

---

## Post #3 by @pieper (2020-09-18 12:02 UTC)

<p>If you don’t specifically need it you can turn off SimpleITK.</p>

---

## Post #4 by @myousefi2016 (2020-09-18 12:06 UTC)

<p>Ideed I use SimpleITK in my workflow and I don’t want to turn it off. So it seems building Slicer against system Python is pointless but it would be much easier other than baking all the Python bindings from source when they are installed already.</p>

---

## Post #5 by @lassoan (2020-09-18 12:22 UTC)

<p>Probably the reason why <a class="mention" href="/u/myousefi2016">@myousefi2016</a> has been considering using system Python is to solve the Python environment mixup issues discussed in: <a href="https://discourse.slicer.org/t/im-getting-not-a-useful-error-when-i-try-to-start-slicer-jupyter-kernel-how-to-debug/13530/7" class="inline-onebox">I'm getting not a useful error when I try to start Slicer Jupyter kernel, how to debug?</a></p>

---

## Post #6 by @myousefi2016 (2020-09-18 12:55 UTC)

<p>I can resolve this issue possibly by modifying the cmake file to point it into a local directory probably by adding a —prefix at the end of the python install setup.py command but it would be really awkward I think. I really appreciate if there would be a better workaround for this.</p>

---

## Post #7 by @lassoan (2020-09-18 14:27 UTC)

<p>I think the root cause of all issues is that <a href="https://github.com/Slicer/SlicerJupyter/issues/39">wsgi package is missing from Slicer’s Python</a>. Therefore, users must use an external Python environment to launch jupyter-notebook server. However, Slicer cannot be launched from this Python environment, due to some conflicts in site packages.</p>
<p>Instead of trying to solve the issue with conflicting site packages (for that we would need <a class="mention" href="/u/jcfr">@jcfr</a>’s help), I had a look at this wsgi package issue and I’ve managed to fix it!! - see <a href="https://github.com/Slicer/Slicer/pull/5190">https://github.com/Slicer/Slicer/pull/5190</a></p>
<p>Once this small change is integrated (probably by tomorrow), it will be possible to run Jupyter notebook server in Slicer’s Python environment, so there will be no more site package conflicts, so no need to use system Python.</p>

---

## Post #8 by @myousefi2016 (2020-09-18 14:30 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for your help! Will this PR be included in the binary preview release tomorrow? So there is no need to bake Slicer from source?</p>

---

## Post #9 by @lassoan (2020-09-18 14:32 UTC)

<aside class="quote no-group" data-username="myousefi2016" data-post="8" data-topic="13536">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/myousefi2016/48/7602_2.png" class="avatar"> myousefi2016:</div>
<blockquote>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for your help! Will this PR be included in the binary preview release tomorrow?</p>
</blockquote>
</aside>
<p>Yes, unless Jc has any objection (which is not likely).</p>

---

## Post #10 by @myousefi2016 (2020-09-18 14:35 UTC)

<p>Thank you so much! I’m looking to use that and hopefully, my problem will be solved.</p>

---
