---
topic_id: 2465
title: "Introducing Slicerbuildenvironment Project"
date: 2018-03-29
url: https://discourse.slicer.org/t/2465
---

# Introducing SlicerBuildEnvironment project

**Topic ID**: 2465
**Date**: 2018-03-29
**URL**: https://discourse.slicer.org/t/introducing-slicerbuildenvironment-project/2465

---

## Post #1 by @jcfr (2018-03-29 05:25 UTC)

<h3 id="heading--overview">overview</h3>
<p>To streamline the continuous integration and allow anyone to easily reproduce builds, we created a new project. Currently, it contains only a Docker directory that itself contain a sub-directory for each build environment.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/Slicer/SlicerBuildEnvironment">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerBuildEnvironment" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/5f961b8a5ed50494fa0e6d9821f15a4c/Slicer/SlicerBuildEnvironment" class="thumbnail">

  <h3><a href="https://github.com/Slicer/SlicerBuildEnvironment" target="_blank" rel="noopener">GitHub - Slicer/SlicerBuildEnvironment: A repository of scripts to set up a Slicer build...</a></h3>

    <p><span class="github-repo-description">A repository of scripts to set up a Slicer build environment. </span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<h3><a name="p-10040-table-of-contents-1" class="anchor" href="#p-10040-table-of-contents-1" aria-label="Heading link"></a>table of contents</h3>
<ul>
<li><a href="#heading--overview">overview</a></li>
<li><a href="#heading--docker-terminology">docker terminology</a></li>
<li><a href="#heading--organization">organization</a></li>
<li><a href="#heading--dockbuild">dockbuild</a></li>
<li><a href="#heading--available-build-environment">available build environment</a></li>
<li>step-by-step
<ul>
<li><a href="#heading--step-by-step-1">(1) configure, build and package Slicer</a></li>
<li><a href="#heading--step-by-step-2">(2) configure, build and package a Slicer extension</a></li>
</ul>
</li>
<li><a href="#heading--summary">summary</a></li>
<li><a href="#heading--next">next</a></li>
</ul>
<h3 id="heading--docker-terminology">docker terminology</h3>
<p>For the one who are not familiar with <a href="https://en.wikipedia.org/wiki/Docker_%28software%29">Docker</a>, it is somewhat like a light-weight virtual machine that can start very efficiently.</p>
<p>Before diving into the details of this project, some terminology:</p>
<ul>
<li><code>host</code>: This is your workstation running your preferred operating system.</li>
<li><code>container</code>: This is what is created after starting up a docker image.</li>
<li><code>docker image</code>:  It is pre-generated using a recipe (the <code>Dockerfile</code>) and can be downloaded on the <code>host</code>.</li>
<li><code>docker client</code>: To keep things simple, this is the tool used to run a <code>docker image</code>.</li>
</ul>
<h3 id="heading--organization">organization</h3>
<p>The SlicerBuildEnvironment project has the following organization:</p>
<pre><code class="lang-plaintext">SlicerBuildEnvironment
  |
  |--- Docker
          |--- qt4-centos5
          |          |--- Dockerfile
          |
          |--- qt4-ubuntu1004
          |          |--- Dockerfile
          |
          |--- qt5-centos7
          |          |--- Dockerfile
          |
          |--- Makefile
</code></pre>
<p>Each sub-directory (e.g <code>qt5-centos7</code>) contains a  <code>Dockerfile</code> allowing to generate a <strong>reusable</strong> build environment (or docker image). That build environment includes a version of qt (e.g <code>qt5</code>) and is based on a given operating system (e.g <code>centos5</code>).</p>
<h3 id="heading--dockbuild">dockbuild</h3>
<p>The interesting part is that the recipe associated with each SlicerBuildEnvironment image is only responsible to install (or build) Qt,  the remaining of the tools forming the complete compiling environment are provided by some other base images provided by the <strong>dockbuild</strong> project.</p>
<p><a href="https://github.com/dockbuild/dockbuild#readme">dockbuild</a> is a project responsible to create base docker image that includes a <strong>tested</strong> compiling environment, latest git version, cmake, ninja, python 3 and openssh-client. And also a convenience entrypoint allowing to automatically mount the current working directory into the image.</p>
<p>dockbuild was inspired by <a href="https://github.com/dockcross/dockcross">dockcross</a>, a collection of docker image providing cross-compiling enviroment. It even re-use the same tests and entrypoint script.</p>
<h3 id="heading--available-build-environment">available build environment</h3>
<pre><code class="lang-auto">slicer/buildenv-qt4-ubuntu1004:latest
slicer/buildenv-qt4-centos5:latest
slicer/buildenv-qt5-centos7:latest
</code></pre>
<h3 id="heading--step-by-step-1">step-by-step: (1) configure, build and package Slicer</h3>
<p>The following steps will:</p>
<ul>
<li>download Slicer 4.8.1 source code</li>
<li>download the associated build environment</li>
<li>configure, build and package Slicer</li>
</ul>
<pre><code class="lang-auto">ROOT_DIR=/tmp/Slicer481
mkdir -p $ROOT_DIR

cd ${ROOT_DIR}

# Download sources
svn co http://svn.slicer.org/Slicer4/branches/Slicer-4-8 Slicer -r 26813

# Download corresponding build environment and generate convenience script
docker run --rm slicer/buildenv-qt4-ubuntu1004 &gt; ~/bin/slicer-buildenv-qt4-ubuntu1004
chmod u+x ~/bin/slicer-buildenv-qt4-ubuntu1004

# Configure Slicer
slicer-buildenv-qt4-ubuntu1004 cmake \
  -BSlicer-build -HSlicer \
  -GNinja \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF \
  -DSlicer_BUILD_CLI:BOOL=OFF \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -DBUILD_TESTING:BOOL=OFF

# Build Slicer
slicer-buildenv-qt4-ubuntu1004 cmake --build Slicer-build

# Package Slicer
slicer-buildenv-qt4-ubuntu1004 cmake --build Slicer-build\Slicer-build --target package
</code></pre>
<h3 id="heading--step-by-step-2">step-by-step: (2) configure, build and package a Slicer extension</h3>
<p>The following steps will:</p>
<ul>
<li>download an extension source code</li>
<li>configure, build and package the extension using the build generated above</li>
</ul>
<pre><code class="lang-auto">ROOT_DIR=/tmp/Slicer481

cd ${ROOT_DIR}

EXTENSION_NAME=ImageMaker

# Download extension source
git clone git://github.com/finetjul/ImageMaker ${EXTENSION_NAME}

# Configure the extension
slicer-buildenv-qt4-ubuntu1004 cmake \
  -B${EXTENSION_NAME}-build -H${EXTENSION_NAME} \
  -GNinja \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DSlicer_DIR:PATH=/work/Slicer-build/Slicer-build


# Hint: /work is the working directory in the image, it corresponds to 
#       the directory from which the script `slicer-buildenv-qt4-ubuntu1004` is called.


# Build the extension
slicer-buildenv-qt4-ubuntu1004 cmake --build ${EXTENSION_NAME}-build

# Package the extension
slicer-buildenv-qt4-ubuntu1004 cmake --build ${EXTENSION_NAME}-build --target package
</code></pre>
<h3 id="heading--summary">summary</h3>
<p>We presented a collection of Linux based build environment allowing to reproduce build of Slicer, Slicer extension or literally any other project with similar requirements.</p>
<p>This build environment requires to have docker installed and can be used on Linux, macOS or Windows host.</p>
<h3 id="heading--next">next</h3>
<p>In follow-up posts, we will:</p>
<ul>
<li>explain how to run the tests</li>
<li>describe the <code>slicer/slicer-base</code> docker images used for continous integration</li>
<li>introduce the <code>slicer/slicer</code> image (it will be available shortly, and will be a light weight images including Slicer binaries)</li>
</ul>
<p>In the future, we also plan to add windows docker images, and/or vagrant cookbook to create Windows virtual machines.</p>

---

## Post #2 by @lassoan (2018-03-29 13:11 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a>, this is great! It could be useful to have this nice overview in the SlicerBuildEnvironment documentation pages, too.</p>

---

## Post #3 by @jcfr (2018-03-30 03:56 UTC)

<p>Thanks for the feedback.</p>
<p>The project README has been updated.</p>

---
