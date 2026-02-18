# Programatically install extensions

**Topic ID**: 19241
**Date**: 2021-08-18
**URL**: https://discourse.slicer.org/t/programatically-install-extensions/19241

---

## Post #1 by @Srijeet_Chatterjee (2021-08-18 01:21 UTC)

<p>Hello everyone,</p>
<p>I am really new to slicer (just a couple of weeks) and a novice programmer. My difficulty is to understand whether it is possible to load the slicer extensions without setting the additional module path manually / via any script. I would prefer to use simple python style (preferably pip) to install an extension. Alternatively, can setting a path in the SlicerLauncerSettings.ini for Python path work? I tried that approach however, I don’t get see the extension in the catalog. Any help in this regard would be highly appreciated! Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @muratmaga (2021-08-18 02:40 UTC)

<p>You may want to look at this approach</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/install.sh">
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


---
