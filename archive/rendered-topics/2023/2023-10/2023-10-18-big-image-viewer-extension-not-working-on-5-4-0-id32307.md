---
topic_id: 32307
title: "Big Image Viewer Extension Not Working On 5 4 0"
date: 2023-10-18
url: https://discourse.slicer.org/t/32307
---

# Big image viewer extension not working on 5.4.0

**Topic ID**: 32307
**Date**: 2023-10-18
**URL**: https://discourse.slicer.org/t/big-image-viewer-extension-not-working-on-5-4-0/32307

---

## Post #1 by @muratmaga (2023-10-18 16:46 UTC)

<p>On linux I am getting an error regarding open-slide python package.</p>
<pre><code class="lang-auto">Collecting openslide-python
  Using cached openslide-python-1.3.1.tar.gz (358 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Requirement already satisfied: Pillow in ./Downloads/Slicer/lib/Python/lib/python3.9/site-packages (from openslide-python) (10.1.0)
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
      creating build/lib.linux-x86_64-cpython-39
      creating build/lib.linux-x86_64-cpython-39/openslide
      copying openslide/__init__.py -&gt; build/lib.linux-x86_64-cpython-39/openslide
      copying openslide/_version.py -&gt; build/lib.linux-x86_64-cpython-39/openslide
      copying openslide/lowlevel.py -&gt; build/lib.linux-x86_64-cpython-39/openslide
      copying openslide/deepzoom.py -&gt; build/lib.linux-x86_64-cpython-39/openslide
      running build_ext
      building 'openslide._convert' extension
      creating build/temp.linux-x86_64-cpython-39
      creating build/temp.linux-x86_64-cpython-39/openslide
      /opt/rh/devtoolset-7/root/usr/bin/gcc -pthread -std=c99 -Wall -Wstrict-prototypes -fno-strict-aliasing -fwrapv -g -fPIC -I/home/maga/Downloads/Slicer/lib/Python/include/python3.9 -c openslide/_convert.c -o build/temp.linux-x86_64-cpython-39/openslide/_convert.o
      error: command '/opt/rh/devtoolset-7/root/usr/bin/gcc' failed: No such file or directory
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for openslide-python
  Running setup.py clean for openslide-python
</code></pre>
<p>It looks like it is trying to build the package.</p>

---

## Post #2 by @pieper (2023-10-18 17:36 UTC)

<p>I’ve had trouble installing openslide before.  In this case it looks like their configuration is not correct because the path to the compiler is wrong.  Better for this to be fixed upstream.</p>

---

## Post #3 by @gaoyi.cn (2023-10-19 01:06 UTC)

<p>I’ll investigate this and report back soon.</p>

---
