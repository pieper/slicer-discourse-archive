# Installing openslide-python

**Topic ID**: 24187
**Date**: 2022-07-05
**URL**: https://discourse.slicer.org/t/installing-openslide-python/24187

---

## Post #1 by @smrolfe (2022-07-05 18:42 UTC)

<p>I’m trying to install openslide-python via pip_install to support reading NRRD files with <span class="mention">@MONAI</span>. I am getting the following error with Slicer 5.0.2 on Linux:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; pip_install('openslide-python')
Collecting openslide-python
  Using cached openslide-python-1.2.0.tar.gz (338 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: Pillow in ./lib/Python/lib/python3.9/site-packages (from openslide-python) (9.0.1)
Building wheels for collected packages: openslide-python
  Building wheel for openslide-python (setup.py): started
  Building wheel for openslide-python (setup.py): finished with status 'error'
  error: subprocess-exited-with-error

  � python setup.py bdist_wheel did not run successfully.
  ? exit code: 1
  ??&gt; [16 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build/lib.linux-x86_64-3.9
      creating build/lib.linux-x86_64-3.9/openslide
      copying openslide/__init__.py -&gt; build/lib.linux-x86_64-3.9/openslide
      copying openslide/_version.py -&gt; build/lib.linux-x86_64-3.9/openslide
      copying openslide/lowlevel.py -&gt; build/lib.linux-x86_64-3.9/openslide
      copying openslide/deepzoom.py -&gt; build/lib.linux-x86_64-3.9/openslide
      running build_ext
      building 'openslide._convert' extension
      creating build/temp.linux-x86_64-3.9
      creating build/temp.linux-x86_64-3.9/openslide
      /opt/rh/devtoolset-7/root/usr/bin/gcc -pthread -std=c99 -Wall -Wstrict-prototypes -fno-strict-aliasing -fwrapv -g -fPIC -I/home/sara/Slicer_stable/Slicer-5.0.2-linux-amd64/lib/Python/include/python3.9 -c openslide/_convert.c -o build/temp.linux-x86_64-3.9/openslide/_convert.o
      error: command '/opt/rh/devtoolset-7/root/usr/bin/gcc' failed: No such file or directory
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for openslide-python
  Running setup.py clean for openslide-python
Failed to build openslide-python
Installing collected packages: openslide-python
  Running setup.py install for openslide-python: started
  Running setup.py install for openslide-python: finished with status 'error'
  error: subprocess-exited-with-error

  � Running setup.py install for openslide-python did not run successfully.
  ? exit code: 1
  ??&gt; [18 lines of output]
      running install
      /home/sara/Slicer_stable/Slicer-5.0.2-linux-amd64/lib/Python/lib/python3.9/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
        warnings.warn(
      running build
      running build_py
      creating build
      creating build/lib.linux-x86_64-3.9
      creating build/lib.linux-x86_64-3.9/openslide
      copying openslide/__init__.py -&gt; build/lib.linux-x86_64-3.9/openslide
      copying openslide/_version.py -&gt; build/lib.linux-x86_64-3.9/openslide
      copying openslide/lowlevel.py -&gt; build/lib.linux-x86_64-3.9/openslide
      copying openslide/deepzoom.py -&gt; build/lib.linux-x86_64-3.9/openslide
      running build_ext
      building 'openslide._convert' extension
      creating build/temp.linux-x86_64-3.9
      creating build/temp.linux-x86_64-3.9/openslide
      /opt/rh/devtoolset-7/root/usr/bin/gcc -pthread -std=c99 -Wall -Wstrict-prototypes -fno-strict-aliasing -fwrapv -g -fPIC -I/home/sara/Slicer_stable/Slicer-5.0.2-linux-amd64/lib/Python/include/python3.9 -c openslide/_convert.c -o build/temp.linux-x86_64-3.9/openslide/_convert.o
      error: command '/opt/rh/devtoolset-7/root/usr/bin/gcc' failed: No such file or directory
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: legacy-install-failure

� Encountered error while trying to install package.
??&gt; openslide-python

note: This is an issue with the package mentioned above, not pip.
hint: See above for output from the failure.
WARNING: You are using pip version 22.0.3; however, version 22.1.2 is available.
You should consider upgrading via the '/home/sara/Slicer_stable/Slicer-5.0.2-linux-amd64/bin/./python-real -m pip install --upgrade pip' command.
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/sara/Slicer_stable/Slicer-5.0.2-linux-amd64/bin/Python/slicer/util.py", line 3431, in pip_install
    _executePythonModule('pip', args)
  File "/home/sara/Slicer_stable/Slicer-5.0.2-linux-amd64/bin/Python/slicer/util.py", line 3394, in _executePythonModule
    logProcessOutput(proc)
  File "/home/sara/Slicer_stable/Slicer-5.0.2-linux-amd64/bin/Python/slicer/util.py", line 3363, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/home/sara/Slicer_stable/Slicer-5.0.2-linux-amd64/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'openslide-python']' returned non-zero exit status 1.
</code></pre>
<p>It seems there is a gcc binary it cannot find. This is working on Windows OS with no issues. I would appreciate any advice.</p>

---

## Post #2 by @jamesobutler (2022-07-05 23:39 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="1" data-topic="24187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>This is working on Windows OS with no issues.</p>
</blockquote>
</aside>
<p>It builds the whl from source successfully? Or just not an issue on Windows because it uses the pre-built whl from PyPI?</p>
<p>openslide_python-1.2.0-cp39-cp39-win_amd64.whl</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pypi.org/project/openslide-python/1.2.0/">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.35549fe8.ico" class="site-icon" width="" height="">

      <a href="https://pypi.org/project/openslide-python/1.2.0/" target="_blank" rel="noopener nofollow ugc">PyPI</a>
  </header>

  <article class="onebox-body">
    <img width="" height="" src="https://pypi.org/static/images/twitter.abaf4b19.webp" class="thumbnail">

<h3><a href="https://pypi.org/project/openslide-python/1.2.0/" target="_blank" rel="noopener nofollow ugc">openslide-python</a></h3>

  <p>Python interface to OpenSlide</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jamesobutler (2022-07-06 00:02 UTC)

<p>Are you able to successfully build on Ubuntu in regular python (not Slicer python)?</p>
<p>Some openslide-python issues related to building/whls on Linux.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/openslide/openslide/issues/340">
  <header class="source">

      <a href="https://github.com/openslide/openslide/issues/340" target="_blank" rel="noopener nofollow ugc">github.com/openslide/openslide</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/openslide/openslide/issues/340" target="_blank" rel="noopener nofollow ugc">Unable to install on Ubuntu in Docker environment</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-13" data-time="06:09:30" data-timezone="UTC">06:09AM - 13 Sep 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-09-14" data-time="00:02:48" data-timezone="UTC">12:02AM - 14 Sep 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/kuri54" target="_blank" rel="noopener nofollow ugc">
          <img alt="kuri54" src="https://avatars.githubusercontent.com/u/40049003?v=4" class="onebox-avatar-inline" width="20" height="20">
          kuri54
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Context
**Operating system** : Ubuntu18.04 running on docker
**Platform** :<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> 64-bit x86 
**OpenSlide version**: Latest

## Details
When I try to install openslide-python, I get

&gt; 1. install OpenSlide
&gt; 2. pip install openslide-python

I did so because of the above instructions.

Steps
1. create `openslide `folder
2. ` cd openslide`
3. `wget https://github.com/openslide/openslide/releases/download/v3.4.1/openslide-3.4.1.tar.gz`
4. `tar -xvf openslide-3.4.1.tar.gz`
5. `cd openslide-3.4.1`
6. `./configure`

## Error message
```
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /bin/mkdir -p
checking for gawk... no
checking for mawk... mawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports nested variables... (cached) yes
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking for style of include used by make... GNU
checking for gcc... no
checking for cc... no
checking for cl.exe... no
configure: error: in `/work/openslide-python/openslide-3.4.1':
configure: error: no acceptable C compiler found in $PATH
See `config.log' for more details
```

I get an error at step 6.
Am I doing something wrong?

Can you please tell me the correct installation procedure?

I have also tried the following
**Install with apt-get**
1. `sudo apt-get install openslide-tools`
2. `sudo apt-get install python-openslide`
I could not import openslide with this procedure.

**Install from Local environment with brew**
```
==&gt; Checking for dependents of upgraded formulae...
==&gt; No broken dependents found!
```

I'm very sorry to be so persistent. 
Can you please tell me the correct installation procedure in detail?</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubissue" data-onebox-src="https://github.com/openslide/openslide-python/issues/126">
  <header class="source">

      <a href="https://github.com/openslide/openslide-python/issues/126" target="_blank" rel="noopener nofollow ugc">github.com/openslide/openslide-python</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/openslide/openslide-python/issues/126" target="_blank" rel="noopener nofollow ugc">interest in wheel files?</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-06-04" data-time="02:00:19" data-timezone="UTC">02:00AM - 04 Jun 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/kaczmarj" target="_blank" rel="noopener nofollow ugc">
          <img alt="kaczmarj" src="https://avatars.githubusercontent.com/u/17690870?v=4" class="onebox-avatar-inline" width="20" height="20">
          kaczmarj
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Hello, would the maintainers of this project be interested in building multi-pla<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">tform wheels? At the moment, pypi only includes the sources for `openslide-python`, so users require a compiler. This wouldn't be necessary with pre-compiled wheels.

I would be happy to submit a PR for this. I would plan to use https://github.com/pypa/cibuildwheel (which is maintained by the python packaging authority). Wheels could be built for linux, macos, and windows.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2022-07-06 00:38 UTC)

<p>On Windows, OpenSlide Python package requires manual installation of OpenSlide binaries. I’ve implemented that in <a href="https://github.com/gaoyi/SlicerBigImage/tree/main/BigImageViewer">BigImageViewer extension</a>.</p>
<p>On Linux, you need to <a href="https://github.com/gaoyi/SlicerBigImage#Linux">install libopenslide</a>.</p>
<p>It is all somewhat hacky. It’ll be better to switch to OME-NGFF, a zarr-based big image (and transform, etc) file format.</p>

---

## Post #5 by @smrolfe (2022-07-06 04:37 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="24187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>It builds the whl from source successfully? Or just not an issue on Windows because it uses the pre-built whl from PyPI?</p>
<p>openslide_python-1.2.0-cp39-cp39-win_amd64.whl</p>
</blockquote>
</aside>
<p>Yes, it looks like this is the case.</p>

---

## Post #6 by @smrolfe (2022-07-06 04:43 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, given these OpenSlide build issues, I’m going to switch to another solution.</p>

---

## Post #7 by @lassoan (2022-07-06 13:03 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="6" data-topic="24187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>I’m going to switch to another solution</p>
</blockquote>
</aside>
<p>Keep us updated. Slicer will support the NGFF file format, probably using <a href="https://pypi.org/project/ome-zarr/">ome-zarr</a> Python package. It would be great if you could use this format and experiment with the ome-zarr package.</p>

---

## Post #8 by @pieper (2022-07-06 13:16 UTC)

<p>In case you didn’t see it here’s an example using the ome-zarr package.  It’s pretty nice.</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/pieper/0e7edcf70c844925ea104e07aedbe92a">
  <header class="source">

      <a href="https://gist.github.com/pieper/0e7edcf70c844925ea104e07aedbe92a" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/pieper/0e7edcf70c844925ea104e07aedbe92a" target="_blank" rel="noopener">https://gist.github.com/pieper/0e7edcf70c844925ea104e07aedbe92a</a></h4>

  <h5>ngff.py</h5>
  <pre><code class="Python">"""

Display zarr from s3 buckets for example data from here:
https://www.openmicroscopy.org/2020/11/04/zarr-data.html

exec(open("/Users/pieper/idc/ngff.py").read())

see also: /Volumes/GoogleDrive/My\ Drive/hacks/sardana.py
https://gist.github.com/pieper/10ee6add544633f4c75dbb293ef087bc
</code></pre>
    This file has been truncated. <a href="https://gist.github.com/pieper/0e7edcf70c844925ea104e07aedbe92a" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @muratmaga (2022-07-06 17:49 UTC)

<p>I though one of the benefits of the zarr was the support of the image pyramids. This imported file only seemed to display one of the resolution levels (as far as I can tell)?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e6978fc598c9d4bedf57f35832f76cab1392ca5.png" data-download-href="/uploads/short-url/fKKuJG2aUNa5J9IIxoJO5mdKtCt.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e6978fc598c9d4bedf57f35832f76cab1392ca5_2_681x500.png" alt="image" data-base62-sha1="fKKuJG2aUNa5J9IIxoJO5mdKtCt" width="681" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e6978fc598c9d4bedf57f35832f76cab1392ca5_2_681x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e6978fc598c9d4bedf57f35832f76cab1392ca5_2_1021x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e6978fc598c9d4bedf57f35832f76cab1392ca5_2_1362x1000.png 2x" data-dominant-color="A5A5AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1795×1317 402 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @pieper (2022-07-07 20:15 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="24187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>This imported file only seemed to display one of the resolution levels</p>
</blockquote>
</aside>
<p>Yes - the example is a bit arbitrary.  The original dataset is multi-channel, 3D+T, and pyramid encoded and I just picked a particular resolution/timepoint/channel to display.  All the other options can be exposed as we see fit, such as extracting a high-res subvolume and mapping any three channels to RGB (or a more complex mapping).  The ome-zarr library supports all these options and we need to figure out a good interface for that.</p>

---
