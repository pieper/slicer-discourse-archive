---
topic_id: 25629
title: "Windows Nightly Build Error Pip Install Of Simpleitk Build F"
date: 2022-10-10
url: https://discourse.slicer.org/t/25629
---

# Windows Nightly build error: pip install of SimpleITK build failing

**Topic ID**: 25629
**Date**: 2022-10-10
**URL**: https://discourse.slicer.org/t/windows-nightly-build-error-pip-install-of-simpleitk-build-failing/25629

---

## Post #1 by @jcfr (2022-10-10 19:50 UTC)

<p>Between <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-10-07&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=groupname&amp;compare1=63&amp;value1=Nightly-Packages&amp;field2=buildname&amp;compare2=63&amp;value2=Windows">Oct 7</a> and <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-10-08&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=groupname&amp;compare1=63&amp;value1=Nightly-Packages&amp;field2=buildname&amp;compare2=63&amp;value2=Windows">Oct 8</a>, the installation of SimpleITK from its build tree started to fail.</p>
<p>Notes:</p>
<ul>
<li>The commits <a href="https://github.com/Slicer/Slicer/compare/f898ebd7...60f774">introduced</a> between these two dates are likely unrelated.</li>
<li>The error can <strong>NOT</strong> be reproduced by locally running <code>cmake.exe -P D:\D\P\S-0-build\SimpleITK_install_step.cmake</code>
<ul>
<li>Running from the windows terminal with current drive being either <code>C:</code> or <code>D:</code> does <strong>not</strong> allow to reproduce.</li>
<li>Removing the <code>SimpleITK-*</code> directories from <code>D:\D\P\S-0-build\python-install\Lib\site-packages</code> does <strong>not</strong> allow to reproduce.</li>
</ul>
</li>
</ul>
<p>The associated error (logged into file <code>SimpleITK_install_step_error.txt</code>) is the copied below.</p>
<pre><code class="lang-auto">  DEPRECATION: A future pip version will change local packages to be built in-place without first copying to a temporary directory. We recommend you use --use-feature=in-tree-build to test your packages with this new behavior before it becomes the default.
   pip 21.3 will remove support for this functionality. You can find discussion regarding this at https://github.com/pypa/pip/issues/7555.
    ERROR: Command errored out with exit status 1:
     command: 'D:\D\P\S-0-build\python-install\bin\python.exe' -c 'import io, os, sys, setuptools, tokenize sys.argv[0] = '"'"'C:\\Users\\svc-dashboard\\AppData\\Local\\Temp\\pip-req-build-28m_6mgt\\setup.py'"'"' __file__='"'"'C:\\Users\\svc-dashboard\\AppData\\Local\\Temp\\pip-req-build-28m_6mgt\\setup.py'"'"'f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup setup()'"'"')code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"')f.close()exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base 'C:\Users\svc-dashboard\AppData\Local\Temp\pip-pip-egg-info-r_1drybq'
         cwd: C:\Users\svc-dashboard\AppData\Local\Temp\pip-req-build-28m_6mgt\
    Complete output (11 lines):
    Traceback (most recent call last):
      File "&lt;string&gt;", line 1, in &lt;module&gt;
      File "C:\Users\svc-dashboard\AppData\Local\Temp\pip-req-build-28m_6mgt\setup.py", line 20, in &lt;module&gt;
        doc_files = [to_package_relpath(f) for f in [r'D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python/SimpleITK/docs/LICENSE',r'D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python/SimpleITK/docs/NOTICE',r'D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python/SimpleITK/docs/Readme.md',r'D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python/SimpleITK/docs/ITK-5.3-NOTICE',r'D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python/SimpleITK/docs/ITK-5.3-README.md']]
      File "C:\Users\svc-dashboard\AppData\Local\Temp\pip-req-build-28m_6mgt\setup.py", line 20, in &lt;listcomp&gt;
        doc_files = [to_package_relpath(f) for f in [r'D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python/SimpleITK/docs/LICENSE',r'D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python/SimpleITK/docs/NOTICE',r'D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python/SimpleITK/docs/Readme.md',r'D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python/SimpleITK/docs/ITK-5.3-NOTICE',r'D:/D/P/S-0-build/SimpleITK-build/SimpleITK-build/Wrapping/Python/SimpleITK/docs/ITK-5.3-README.md']]
      File "C:\Users\svc-dashboard\AppData\Local\Temp\pip-req-build-28m_6mgt\setup.py", line 18, in to_package_relpath
        return osp.relpath(filename, osp.join(os.curdir, pkg_name))
      File "D:\D/P/S-0-build/python-install\Lib\ntpath.py", line 703, in relpath
        raise ValueError("path is on mount %r, start on mount %r" % (
    ValueError: path is on mount 'D:', start on mount 'C:'
</code></pre>
<p>Related postings:</p>
<ul>
<li><a href="https://forum.image.sc/t/valueerror-path-is-on-mount-d-start-on-mount-c/69746">https://forum.image.sc/t/valueerror-path-is-on-mount-d-start-on-mount-c/69746</a></li>
<li>Problem was reported back 2021 in <a href="https://github.com/pypa/pip/issues/7625">pypa/pip#7625</a> fixed by pull request <a href="https://github.com/pypa/pip/pull/8062">pypa/pip#8062</a>
</li>
</ul>

---

## Post #2 by @jamesobutler (2022-10-10 21:00 UTC)

<p>The SimpleITK issue occurred on some earlier dates as well.<br>
<a href="https://slicer.cdash.org/viewBuildError.php?buildid=2814131" class="inline-onebox" rel="noopener nofollow ugc">CDash</a> 2022-09-30<br>
<a href="https://slicer.cdash.org/viewBuildError.php?buildid=2816855" class="inline-onebox" rel="noopener nofollow ugc">CDash</a> 2022-10-03</p>
<p><a href="https://github.com/Slicer/Slicer/commit/4d1c98ef8f9623cc4ef175b9dc734e9540bd9f02" class="inline-onebox" rel="noopener nofollow ugc">COMP: Update ITK to post-v5.3rc04 version and SimpleITK to post-v2.2.0 · Slicer/Slicer@4d1c98e · GitHub</a> did include a change to use pip to install SimpleITK rather than using setup.py which was based on corresponding change at <a href="https://github.com/SimpleITK/SimpleITK/commit/3ce91dbcb19b6ad502abbaee03b06ceaa9a9db69" class="inline-onebox" rel="noopener nofollow ugc">Use pip to install SimpleITK · SimpleITK/SimpleITK@3ce91db · GitHub</a>. That would be my best suspicion about why it would’ve started to randomly occur.</p>

---

## Post #3 by @Sam_Horvath (2022-10-10 21:07 UTC)

<p>This has been happening intermittently for a while, I thought I had sorted it out earlier when I fixed the nightly build not being cleaned correctly.</p>
<aside class="quote" data-post="3" data-topic="25376">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-build-error-on-windows-dashboard/25376/3">Slicer build error on Windows dashboard</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Coming back to this, it looks like a number of issues were occurring on the factory machine, most notably that the build directory was not being cleaned before the nightly build, which can cause any number of issues when changing major dependencies.
  </blockquote>
</aside>


---

## Post #4 by @jcfr (2022-10-10 22:17 UTC)

<p>To follow up, the issue has been identified and can be reproduced. Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> for your comments <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Since the SimpleITK external project depends on:</p>
<ul>
<li><code>ITK</code></li>
<li><code>Swig</code></li>
<li>
<code>python-setuptools</code> (itself depending on <code>python-ensurepip</code> and <code>python</code>)</li>
<li><code>python</code></li>
</ul>
<p>reproducing the issue required to:</p>
<ul>
<li>delete the content of <code>D:\D\P\S-0-build\python-install</code>
</li>
<li>open the <code>Slicer.sln</code> and right-click build only onto the <code>python</code>, <code>python-ensurepip</code> and <code>python-setuptools</code> projects</li>
<li>re-run the command <code>cmake.exe -P D:\D\P\S-0-build\SimpleITK_install_step.cmake</code>
</li>
</ul>
<p>Then, the warning mentioning <code>pip 21.3</code> is reported and the error is reproduced.</p>
<p>To address the issue, we need to add <code>python-pip</code> as a dependency to the <code>SimpleITK</code> project.</p>

---

## Post #5 by @jcfr (2022-10-10 22:54 UTC)

<p>The regression should be fixed by <a href="https://github.com/Slicer/Slicer/pull/6576">https://github.com/Slicer/Slicer/pull/6576</a></p>
<p>The plan is to integrate the pull request by 10pm ET so that the upcoming round of nightly is completed with the fix.</p>

---

## Post #6 by @jamesobutler (2022-10-10 23:52 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="25629">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>To address the issue, we need to add <code>python-pip</code> as a dependency to the <code>SimpleITK</code> project.</p>
</blockquote>
</aside>
<p>Good catch! Thanks and sorry I didn’t catch that earlier.</p>

---
