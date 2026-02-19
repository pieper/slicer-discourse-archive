---
topic_id: 37089
title: "Build Extension That Depends On Other Extensions"
date: 2024-06-28
url: https://discourse.slicer.org/t/37089
---

# Build extension that depends on other extensions

**Topic ID**: 37089
**Date**: 2024-06-28
**URL**: https://discourse.slicer.org/t/build-extension-that-depends-on-other-extensions/37089

---

## Post #1 by @mau_igna_06 (2024-06-28 16:52 UTC)

<p>While the build documentation of Slicer is complete, I found it hard to build an extension that depends on other extensions and I had to come up on how to do it myself. So here is my code for that:</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mauigna06/4cb485da9358a6b58d6ecfc91c1b78cc">
  <header class="source">

      <a href="https://gist.github.com/mauigna06/4cb485da9358a6b58d6ecfc91c1b78cc" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mauigna06/4cb485da9358a6b58d6ecfc91c1b78cc" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/mauigna06/4cb485da9358a6b58d6ecfc91c1b78cc</a></h4>

  <h5>build_extension_with_dependencies.sh</h5>
  <pre><code class="Shell"># copypaste this code in the console
#
# set variables
export SLICER_CODE_PATH=/home/$USER/Slicers/Slicer
export SLICER_SUPERBUILD_PATH=/home/$USER/Slicers/SlicerR
export SLICER_BUILD_PATH=$SLICER_SUPERBUILD_PATH/Slicer-build
export BRP_AND_OTHER_EXTENSIONS_CODE=/media/$USER/Nuevo_vol/Lin/Documents/Github
export BRP_AND_OTHER_EXTENSIONS_BUILD=/home/$USER/SExtentions
export BRP_BUILD=$BRP_AND_OTHER_EXTENSIONS_BUILD/BRPR
export NUMBER_OF_SLICER_COMPILATION_JOBS=2</code></pre>
   This file has been truncated. <a href="https://gist.github.com/mauigna06/4cb485da9358a6b58d6ecfc91c1b78cc" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I still don’t know to use the alternative SuperBuild method to do this but I’d like to learn about it because I think it should be simpler</p>

---

## Post #2 by @chir.set (2024-06-28 17:55 UTC)

<p>This won’t solve your problem.</p>
<p>Slicer’s CMakeLists.txt has these lines:</p>
<pre><code class="lang-auto"># Directories can be set in three ways:
#
# (1) Automatically by specifying the label 'REMOTE_MODULE' when
#     calling 'Slicer_Remote_Add' from SuperBuild.cmake.
#
# (2) Automatically by specifying the label 'REMOTE_EXTENSION' when
#     calling 'Slicer_Remote_Add' from SuperBuild.cmake.
#
# (3) Explicitly by configuring the project using the following syntax:
#  cmake -DSlicer_EXTENSION_SOURCE_DIRS:STRING=/path/to/ExtensionA;/path/to/ExtensionB /path/to/source/Slicer
</code></pre>
<p>I understand that <span class="hashtag-raw">#3</span> is what you would need. It could be as simple as adding the Slicer_EXTENSION_SOURCE_DIRS variable to your command line that configures Slicer. But the " /path/to/source/Slicer" part is confusing. It’s doubtful that it refers to an executable, and it’s not in the form of a ‘-D’ cmake parameter.</p>
<p>Never tried that, just discovered that Slicer can build extensions and modules while being built itself.</p>
<p>Your method is mine also: build everything separately.</p>

---

## Post #3 by @chir.set (2024-06-28 18:36 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="2" data-topic="37089">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>But the " /path/to/source/Slicer" part is confusing.</p>
</blockquote>
</aside>
<p>Shame on me, it’s just the path to Slicer sources <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/crazy_face.png?v=12" title=":crazy_face:" class="emoji" alt=":crazy_face:" loading="lazy" width="20" height="20"></p>

---
