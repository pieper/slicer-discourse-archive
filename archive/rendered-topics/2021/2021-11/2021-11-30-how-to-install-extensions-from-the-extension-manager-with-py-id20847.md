# How to install extensions from the extension manager with PythonSlicer

**Topic ID**: 20847
**Date**: 2021-11-30
**URL**: https://discourse.slicer.org/t/how-to-install-extensions-from-the-extension-manager-with-pythonslicer/20847

---

## Post #1 by @pll_llq (2021-11-30 18:05 UTC)

<p>Hi <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=10" title=":wave:" class="emoji" alt=":wave:"></p>
<p>I’m building a docker container chain for testing purposes and I ran into a problem that I can’t install an extension from the extension manager while building the image.</p>
<p>Normally I would use something similar to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#download-and-install-extension" rel="noopener nofollow ugc">the example in the script repository</a> but the problem is that in PythonSlicer there is no <code>slicer.app</code>.</p>
<p>Can anyone advice how to move forward with this issue?</p>

---

## Post #2 by @pll_llq (2021-11-30 18:07 UTC)

<p>I think I’ve found it.</p>
<p>I’ll try to follow the example set here</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/install.sh">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/install.sh" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/install.sh" target="_blank" rel="noopener nofollow ugc">Slicer/SlicerDocker/blob/master/slicer-notebook/install.sh</a></h4>


    <pre><code class="lang-sh">#!/bin/bash

set -e
set +x

script_dir=$(cd $(dirname $0) || exit 1; pwd)
PROG=$(basename $0)

err() { echo -e &gt;&amp;2 ERROR: $@\\n; }
die() { err $@; exit 1; }

if [ "$#" -ne 1 ]; then
  die "Usage: $PROG /path/to/Slicer-X.Y.Z-linux-amd64/Slicer"
fi

slicer_executable=$1

################################################################################
# Set up headless environment
source $script_dir/start-xorg.sh
</code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/install.sh" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
and create an install script that I will run during container build</p>

---

## Post #3 by @jcfr (2021-12-01 07:24 UTC)

<p>You should find more information here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#install-slicer">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#install-slicer</a></p>

---

## Post #4 by @pll_llq (2021-12-01 07:32 UTC)

<p>Yep. My actual problem was that I was using an older example that referenced the old extension manager api</p>

---
