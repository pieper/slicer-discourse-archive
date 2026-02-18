# Facing issue while installing python package

**Topic ID**: 38459
**Date**: 2024-09-20
**URL**: https://discourse.slicer.org/t/facing-issue-while-installing-python-package/38459

---

## Post #1 by @maniron (2024-09-20 11:11 UTC)

<p>I have been trying to install one package in slicer and I am facing the following issue</p>
<blockquote>
<p>Building wheels for collected packages: spatial_correlation_sampler<br>
Building wheel for spatial_correlation_sampler (pyproject.toml) … error<br>
error: subprocess-exited-with-error<br>
× Building wheel for spatial_correlation_sampler (pyproject.toml) did not run successfully.<br>
│ exit code: 1<br>
╰─&gt; [19 lines of output]<br>
running bdist_wheel<br>
C:\Users\TestProfile\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\torch\utils\cpp_extension.py:495: UserWarning: Attempted to use ninja as the BuildExtension backend but we could not find ninja… Falling back to using the slow distutils backend.<br>
warnings.warn(msg.format(‘we could not find ninja.’))<br>
running build<br>
running build_py<br>
creating build\lib.win-amd64-cpython-39\spatial_correlation_sampler<br>
copying Correlation_Module\spatial_correlation_sampler\spatial_correlation_sampler.py → build\lib.win-amd64-cpython-39\spatial_correlation_sampler<br>
copying Correlation_Module\spatial_correlation_sampler_<em>init</em>_.py → build\lib.win-amd64-cpython-39\spatial_correlation_sampler<br>
running build_ext<br>
C:\Users\TestProfile\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\torch\utils\cpp_extension.py:414: UserWarning: The detected CUDA version (12.6) has a minor version mismatch with the version that was used to compile PyTorch (12.1). Most likely this shouldn’t be a problem.<br>
warnings.warn(CUDA_MISMATCH_WARN.format(cuda_str_version, torch.version.cuda))<br>
building ‘spatial_correlation_sampler_backend’ extension<br>
creating build\temp.win-amd64-cpython-39\Release\Correlation_Module<br>
“C:\Program Files\Microsoft Visual Studio\2022\Preview\VC\Tools\MSVC\14.42.34321\bin\HostX86\x64\cl.exe” /c /nologo /O2 /W3 /GL /DNDEBUG /MD -DUSE_CUDA “-IC:\Users\TestProfile\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\torch\include” “-IC:\Users\TestProfile\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\torch\include\torch\csrc\api\include” “-IC:\Users\TestProfile\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\torch\include\TH” “-IC:\Users\TestProfile\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\torch\include\THC” “-IC:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.6\include” “-IC:\Users\TestProfile\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\include” “-IC:\Users\TestProfile\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Include” “-IC:\Program Files\Microsoft Visual Studio\2022\Preview\VC\Tools\MSVC\14.42.34321\include” “-IC:\Program Files\Microsoft Visual Studio\2022\Preview\VC\Tools\MSVC\14.42.34321\ATLMFC\include” “-IC:\Program Files\Microsoft Visual Studio\2022\Preview\VC\Auxiliary\VS\include” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\ucrt” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\um” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\shared” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\winrt” “-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22621.0\cppwinrt” “-IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\include\um” /EHsc /TpCorrelation_Module\correlation.cpp /Fobuild\temp.win-amd64-cpython-39\Release\Correlation_Module\correlation.obj /MD /wd4819 /wd4251 /wd4244 /wd4267 /wd4275 /wd4018 /wd4190 /wd4624 /wd4067 /wd4068 /EHsc -std=c++17 -fopenmp -DTORCH_API_INCLUDE_EXTENSION_H -DTORCH_EXTENSION_NAME=spatial_correlation_sampler_backend -D_GLIBCXX_USE_CXX11_ABI=0 /std:c++17<br>
cl : Command line warning D9002 : ignoring unknown option ‘-std=c++17’<br>
cl : Command line warning D9002 : ignoring unknown option ‘-fopenmp’<br>
correlation.cpp<br>
C:\Users\TestProfile\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\torch\include\torch/csrc/python_headers.h(12): fatal error C1083: Cannot open include file: ‘Python.h’: No such file or directory<br>
error: command ‘C:\Program Files\Microsoft Visual Studio\2022\Preview\VC\Tools\MSVC\14.42.34321\bin\HostX86\x64\cl.exe’ failed with exit code 2<br>
[end of output]</p>
</blockquote>
<p>note: This error originates from a subprocess, and is likely not a problem with pip.<br>
ERROR: Failed building wheel for spatial_correlation_sampler<br>
Failed to build spatial_correlation_sampler<br>
ERROR: Could not build wheels for spatial_correlation_sampler, which is required to install pyproject.toml-based projects</p>
<p>[notice] A new release of pip is available: 23.0 → 24.2<br>
[notice] To update, run: python-real.exe -m pip install --upgrade pip<br>
PS C:\Users\TestProfile\AppData\Local\NA-MIC\Slicer 5.2.2\bin&gt; PythonSlicer.exe -m pip install python-dev<br>
ERROR: Could not find a version that satisfies the requirement python-dev (from versions: none)<br>
ERROR: No matching distribution found for python-dev</p>
<p>[notice] A new release of pip is available: 23.0 → 24.2</p>

---

## Post #2 by @cpinter (2024-09-20 11:14 UTC)

<p>Does this happen on the latest stable 5.6.2? If yes, how about the latest preview?</p>

---

## Post #3 by @maniron (2024-09-20 11:16 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a> I am using the Slicer 5.2.2 version, as one of the application/plugin developed supports only that specific version</p>
<p>package name : spatial_correlation_sampler</p>
<p>is there a solution for this</p>

---

## Post #4 by @maniron (2024-09-20 11:36 UTC)

<p>Is there a way to install python-dev as when I am looking for a solution for this issue, I am getting suggestion like this</p>

---

## Post #5 by @jamesobutler (2024-09-20 12:11 UTC)

<p>Read the following linked post about methods of installing packages where Whl files are having to be built from source. To summarize, build the Whl in a system install of Python and use the cached Whl file to install in the Slicer Python. A Python package requiring build from source with no Whl files available from PyPI is generally an indication of a Python project with not a lot of support.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6117#issuecomment-1042479854">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6117#issuecomment-1042479854" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">

    <div class="github-icon-container" title="Comment">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
    </div>



  <div class="github-info-container">

      <h4>
        Comment by
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?u=1270f1e4ee0c114f4b1d8508d69582b486ab8b37&amp;v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a> - <a href="https://github.com/Slicer/Slicer/pull/6117#issuecomment-1042479854" target="_blank" rel="noopener nofollow ugc">ENH: add python libs and headers for source package install</a>
      </h4>



    <div class="branches">
      <code>Slicer:master</code> ← <code>fbordignon:python_install_test</code>
    </div>

  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Adding Python header and lib would make things worse for end users:
- Bad: User<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6117" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">s need to install build tools. Instead, if we included pre-built wheels in the extension package (the factory machine can do this) then users would not be forced to install anything else than Slicer.
- Bad: Developers would not realize that they are using a Python package that does not have wheels and so the extension would simply not work for users (it would only work on developer computers, where build tools are installed).

For developers, it would be a mixed bag:
- Good: developers could more easily install packages without wheels. But a developer can build wheel by a workaround: install Python-3.9 and build tools on the computer and then pip install the package; next time when calling pip_install in Slicer, the built wheel is found in the package cache and Slicer installs it (at least on Windows).
- Bad: Developers would not realize that they are considering relying on a low-quality Python package, which would be bad.

There may be differences between platforms. For example, on Linux it is probably much more common to have developer tools installed, most end users are developers, providing compatible wheels is hard, and building components is part of normal life. However, in non-mainstream Linux environments entire Slicer may need to be built from source (and then it does not matter what the Slicer package includes).

Adding the two files on a single platform sounds easy, but implementation on all platforms, adding tests, and assisting end users and extension developers with Python package build errors (what developer tools to install, how to configure, investigate build errors) could be significant one-time and continuous effort.

Taking everything into consideration, I would lean towards not supporting building Python wheels in an installed Slicer, as the costs and disadvantages seem to outweigh the benefits.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jamesobutler (2024-09-20 12:15 UTC)

<aside class="quote no-group" data-username="maniron" data-post="3" data-topic="38459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ee7513/48.png" class="avatar"> maniron:</div>
<blockquote>
<p>I am using the Slicer 5.2.2 version, as one of the application/plugin developed supports only that specific version</p>
</blockquote>
</aside>
<p>Which code is it? Slicer developers don’t support older versions of Slicer, but can help provide guidance on the latest stable and preview releases of Slicer.</p>

---

## Post #7 by @maniron (2024-09-20 12:15 UTC)

<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a> thanks for responding, I was able to install the same package locally, now how can I do the way you mentioned</p>

---

## Post #8 by @maniron (2024-09-20 12:16 UTC)

<p>I mean the application which was developed by us in using slicer 5.2.2</p>

---

## Post #9 by @jamesobutler (2024-09-20 12:16 UTC)

<p>For the sake of this thread and for others that might run into the problem, can you describe how you got it to install succesfully?</p>

---

## Post #10 by @jamesobutler (2024-09-20 12:16 UTC)

<p>How can we get you to use latest Slicer stable and preview version? Slicer 5.2.2 is quite old. Are there compatibility issues with latest Slicer? Slicer developers can help with that.</p>

---

## Post #11 by @maniron (2024-09-20 12:18 UTC)

<p>I installed that package using pip</p>
<blockquote>
<p>pip install spatial_correlation_sampler</p>
</blockquote>
<p>before installing it I wanted to install torch</p>
<p>so used the below command to install the required torch and later I installed the package it got installed</p>
<blockquote>
<p>pip install torch torchvision torchaudio --index-url <a href="https://download.pytorch.org/whl/cu121" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cu121</a></p>
</blockquote>
<p>I am trying the same thing with SlicerPython.exe , but no luck</p>
<blockquote>
<p>PythonSlicer.exe -m pip install  --trusted-host=<a href="http://pytorch.org" rel="noopener nofollow ugc">pytorch.org</a> --trusted-host=<a href="http://download.pytorch.org" rel="noopener nofollow ugc">download.pytorch.org</a> --trusted-host=<a href="http://files.pytorch.org" rel="noopener nofollow ugc">files.pytorch.org</a> torch torchvision torchaudio --index-url <a href="https://download.pytorch.org/whl/cu121" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cu121</a></p>
</blockquote>
<p>above is the command I used to install torch</p>
<blockquote>
<p>PythonSlicer.exe -m pip install spatial_correlation_sampler</p>
</blockquote>
<p>above command I used to install the package</p>

---

## Post #12 by @maniron (2024-09-20 12:19 UTC)

<p>Is there a way where we can upgrade the python version in slicer, cause in my machine I have python 3.11 and slicer 5.2.2 is having 3.9.10</p>

---

## Post #13 by @jamesobutler (2024-09-20 12:20 UTC)

<p>Updating Slicer’s Python version is a good bit of work that has not yet been completed by the Slicer developers, but the work is tracked at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7060">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7060" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7060" target="_blank" rel="noopener nofollow ugc">Update Python minor version from 3.9 to something newer</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-06-28" data-time="23:39:57" data-timezone="UTC">11:39PM - 28 Jun 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          dependencies
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

As I learne<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">d while working on #7046, the latest versions of python packages such as `numpy` and `scipy` now have a python minimum of 3.9 which is the version currently used by Slicer (3.9.10). Per [NEP29 drop schedule](https://numpy.org/neps/nep-0029-deprecation_policy.html#drop-schedule), Python 3.9 support will begin to be dropped by major python packages beginning April 5th, 2024. However, NEP29 has now been superseded by [SPEC 0](https://scientific-python.org/specs/spec-0000/) where the [drop schedule](https://scientific-python.org/specs/spec-0000/#drop-schedule) states to drop Python 3.9 support in new releases starting in 2023 Q4 (marking the end of 3 years of support). Writing up this issue is to stay ahead of the deprecation curve so that Slicer does not get into a situation of not being able to use the latest versions of major python packages.

## To answer the question: Is the newer version of Python supported by the open source community?
When Slicer was updated from 3.6.7 to 3.9.10 in https://github.com/Slicer/Slicer/commit/34e48e8aef5dad19ec8a955d6f48a1940846e3f3:
It was January 25th, 2022 and the "[python readiness](https://pyreadiness.org/)" for Python 3.9 was that [64.7%](https://github.com/di/pyreadiness/blob/50d28f9bcf62edf5f42e237082f1a3c93f8be3e1/docs/3.9/index.html#L69) of the most popular python packages had explicit support for 3.9 as stated on pypi.org.

|Date | Python 3.9 | Python 3.10 | Python 3.11 | Python 3.12|
|------|-------------|--------------|---------------|--------------|
|June 28th, 2023|[78.6%](https://github.com/di/pyreadiness/blob/a7f95961c5615d5eb336ad646fe3d1aae8cf8c55/docs/3.9/index.html#L95)|[72.8%](https://github.com/di/pyreadiness/blob/a7f95961c5615d5eb336ad646fe3d1aae8cf8c55/docs/3.10/index.html#L95)|[51.7%](https://github.com/di/pyreadiness/blob/a7f95961c5615d5eb336ad646fe3d1aae8cf8c55/docs/3.11/index.html#L95)||
|August 24th, 2023|[80.8%](https://github.com/di/pyreadiness/blob/949c860148e24c6976ff8de76435e663e610d2da/docs/3.9/index.html#L95)|[76.4%](https://github.com/di/pyreadiness/blob/949c860148e24c6976ff8de76435e663e610d2da/docs/3.10/index.html#L95)|[60.6%](https://github.com/di/pyreadiness/blob/949c860148e24c6976ff8de76435e663e610d2da/docs/3.11/index.html#L95)||
|October 28th, 2023|[80.0%](https://github.com/di/pyreadiness/blob/bad9df0eafc04ebf06bbd01ff97be2235a96e841/docs/3.9/index.html#L95)|[76.1%](https://github.com/di/pyreadiness/blob/bad9df0eafc04ebf06bbd01ff97be2235a96e841/docs/3.10/index.html#L95)|[64.4%](https://github.com/di/pyreadiness/blob/bad9df0eafc04ebf06bbd01ff97be2235a96e841/docs/3.11/index.html#L95)||
|December 20th, 2023|[80.8%](https://github.com/di/pyreadiness/blob/b8ab80f82fcc088aa44b3ad9ed26151c70f301cb/docs/3.9/index.html#L95)|[76.9%](https://github.com/di/pyreadiness/blob/b8ab80f82fcc088aa44b3ad9ed26151c70f301cb/docs/3.10/index.html#L95)|[67.5%](https://github.com/di/pyreadiness/blob/b8ab80f82fcc088aa44b3ad9ed26151c70f301cb/docs/3.11/index.html#L95)||
|March 4th, 2024|[82.8%](https://github.com/di/pyreadiness/blob/764e4520b314c28658f099299b3c7670280ffeb5/docs/3.9/index.html#L95)|[78.9%](https://github.com/di/pyreadiness/blob/764e4520b314c28658f099299b3c7670280ffeb5/docs/3.10/index.html#L95)|[69.7%](https://github.com/di/pyreadiness/blob/764e4520b314c28658f099299b3c7670280ffeb5/docs/3.11/index.html#L95)|[48.6%](https://github.com/di/pyreadiness/blob/764e4520b314c28658f099299b3c7670280ffeb5/docs/3.12/index.html#L95)|
|May 17th, 2024|[80.8%](https://github.com/di/pyreadiness/blob/bfe7422e412f0305b6762dcefa4849a8bb05384e/docs/3.9/index.html#L95)|[77.5%](https://github.com/di/pyreadiness/blob/bfe7422e412f0305b6762dcefa4849a8bb05384e/docs/3.10/index.html#L95)|[71.1%](https://github.com/di/pyreadiness/blob/bfe7422e412f0305b6762dcefa4849a8bb05384e/docs/3.11/index.html#L95)|[55.0%](https://github.com/di/pyreadiness/blob/bfe7422e412f0305b6762dcefa4849a8bb05384e/docs/3.12/index.html#L95)|
|August 14th, 2024|[82.8%](https://github.com/di/pyreadiness/blob/a3467a9865e6326f2accb218c43ea9a187a8e39a/docs/3.9/index.html#L95)|[80.8%](https://github.com/di/pyreadiness/blob/a3467a9865e6326f2accb218c43ea9a187a8e39a/docs/3.10/index.html#L95)|[74.7%](https://github.com/di/pyreadiness/blob/a3467a9865e6326f2accb218c43ea9a187a8e39a/docs/3.11/index.html#L95)|[62.2%](https://github.com/di/pyreadiness/blob/a3467a9865e6326f2accb218c43ea9a187a8e39a/docs/3.12/index.html#L95)|

## Describe the solution you'd like

- Update Slicer's Python from 3.9 to 3.10. 

Based on Slicer's previous update to Python 3.9 at 64.7% readiness and Python 3.10 at a higher readiness than that, this means Slicer can consider Python 3.10 ready to update to pending Python 3.10 support at:
- https://github.com/python-cmake-buildsystem/python-cmake-buildsystem
- https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/281

## Describe alternatives you've considered

- Update Slicer's Python from 3.9 to 3.12. This should be considered especially if the python-readiness for Python 3.12 (https://pyreadiness.org/3.12/) has increased when a developer begins to execute on this update.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Slicer 5.2.2 will definitely not ever be updated to support a newer python version.</p>

---

## Post #14 by @maniron (2024-09-20 12:21 UTC)

<p>Hmm got it but atleast if I could be able to install this package it would be more helpful</p>

---

## Post #15 by @maniron (2024-09-20 12:23 UTC)

<aside class="quote no-group" data-username="maniron" data-post="1" data-topic="38459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ee7513/48.png" class="avatar"> maniron:</div>
<blockquote>
<p>fatal error C1083: Cannot open include file: ‘Python.h’: No such file or directory</p>
</blockquote>
</aside>
<p>For this error I placed all the required header files in the python include folder , now this error is not coming but I am getting the link error</p>
<p>LINK : warning LNK4044: unrecognized option ‘/lgomp’; ignored<br>
LINK : fatal error LNK1104: cannot open file ‘python39.lib’<br>
error: command ‘C:\Program Files\Microsoft Visual Studio\2022\Preview\VC\Tools\MSVC\14.42.34321\bin\HostX86\x64\link.exe’ failed with exit code 1104</p>

---

## Post #16 by @maniron (2024-09-20 12:25 UTC)

<p>Can you help me with this, so that I will try this way and see whether I have a solution for the issue</p>

---

## Post #17 by @muratmaga (2024-09-20 16:06 UTC)

<p>Others might chime in but i think you will have to build both Slicer and this python package from source using the same build tools to avoid that problem.</p>
<p>I thought things worked in ubuntu, maybe focus on working on that?</p>

---

## Post #18 by @muratmaga (2024-09-20 16:21 UTC)

<p>Also, why are you trying with 5.2.2? Did you try with the latest stable?</p>

---

## Post #19 by @maniron (2024-09-23 05:38 UTC)

<p>I am actually consuming one of the plugin which is developed with this version of Slicer and making changes to it . Thats the main reason I using this version. Tried with latest version of slicer but the plugin is not working</p>

---
