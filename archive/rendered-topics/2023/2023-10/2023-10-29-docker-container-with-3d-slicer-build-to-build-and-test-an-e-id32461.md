# Docker container with 3D Slicer build to build and test an extension

**Topic ID**: 32461
**Date**: 2023-10-29
**URL**: https://discourse.slicer.org/t/docker-container-with-3d-slicer-build-to-build-and-test-an-extension/32461

---

## Post #1 by @jhlegarreta (2023-10-29 21:03 UTC)

<p>Hi,<br>
related to <a href="https://discourse.slicer.org/t/adding-a-ci-build-to-a-slicer-extension/30857" class="inline-onebox">Adding a CI build to a Slicer extension</a>, I am willing to add an additional GitHub Actions workflow to check building and testing an extension this time using a Slicer Docker image, so that I can know early if a change to the extension fails (Slicer taking above 3 hours to build).</p>
<p>I have done several attempts here, so far unsuccessfully:<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/6679889770/job/18152413938?pr=192" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add Docker-assisted build, test GHA workflow · SlicerDMRI/SlicerDMRI@b030e77 · GitHub</a></p>
<p>I am pulling the nightly <code>slicer/slicer-base:latest</code> image.</p>
<p>And I am using the step below in my GHA workflow file to try to build the extension against it:</p>
<pre><code class="lang-auto">Slicer_DIR=/usr/src/Slicer-build/Slicer-build

EXTENSION_NAME=SlicerDMRI
EXTENSION_SOURCE_DIR=${{ github.workspace }}/$EXTENSION_NAME
EXTENSION_BUILD_DIR=${{ github.workspace }}/$EXTENSION_NAME-build

docker run \
  --rm \
  -v $EXTENSION_SOURCE_DIR:/usr/src/slicerdmri \
  -v $EXTENSION_BUILD_DIR:/usr/src/slicerdmri-build \
Slicer-build
  slicer/slicer-base \
  cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE:STRING=$BUILD_TYPE \
    -DSlicer_DIR:PATH=$Slicer_DIR \
    -S /usr/src/slicerdmri \
    -B /usr/src/slicerdmri-build
</code></pre>
<p>It looks like I am not giving it the right Slicer build directory or I am not mapping it correctly to the Docker volume:</p>
<pre><code class="lang-auto">-- Configuring incomplete, errors occurred!
CMake Error at CMakeLists.txt:22 (find_package):
  By not providing "FindSlicer.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Slicer", but
  CMake did not find one.

  Could not find a package configuration file provided by "Slicer" with any
  of the following names:

    SlicerConfig.cmake
    slicer-config.cmake
</code></pre>
<p><a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/6679889770/job/18152413938?pr=192#step:5:33" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add Docker-assisted build, test GHA workflow · SlicerDMRI/SlicerDMRI@b030e77 · GitHub</a></p>
<p>IIUC, I am giving it the same directory as I do in my regular GHA workflow build that compiles Slicer:<br>
<a href="https://github.com/SlicerDMRI/SlicerDMRI/actions/runs/6684590637/job/18162009288#step:7:2" class="inline-onebox" rel="noopener nofollow ugc">Merge pull request #194 from jhlegarreta/FixSprintfWarnings · SlicerDMRI/SlicerDMRI@f95c613 · GitHub</a></p>
<p>Locally,</p>
<pre><code class="lang-auto">docker run --rm  slicer/slicer-base find . -name "SlicerConfig.cmake" -type f
</code></pre>
<p>or</p>
<pre><code class="lang-auto">docker run --rm  slicer/slicer-base find . -name "slicer-config.cmake" -type f
</code></pre>
<p>dot not provide any answer.</p>
<p>And</p>
<pre><code class="lang-auto">docker run --rm  slicer/slicer-base ls ./Slicer-build
</code></pre>
<p>does not show a meaningful directory structure (<code>Slicer-build/share/Slicer-5.5/Slicer.crt</code>) for this purpose.</p>
<p>Locally, if I do</p>
<pre><code class="lang-auto">docker run --rm 
  -v /bld/slicer:/usr/src/Slicer-build/slicer-build \
  -v /src/slicerdmri:/usr/src/slicerdmri \
  -v /bld/slicerdmri:/usr/src/slicerdmri-build \
  slicer/slicer-base \
  cmake -GNinja -DCMAKE_BUILD_TYPE:STRING=Debug \
  -DSlicer_DIR:PATH=$Slicer_DIR \
  -S /usr/src/slicerdmri \
  -B /usr/src/slicerdmri-build
</code></pre>
<p>I get an CMake error:</p>
<pre><code class="lang-auto">CMake Error:
The current CMakeCache.txt directory
/usr/src/slicerdmri-build/CMakeCache.txt
is different than the directory
/bld/slicerdmri where CMakeCache.txt was created.
This may result in binaries being created in the wrong place.
If you are not sure, reedit the CMakeCache.txt
CMake Error:
The source "/usr/src/slicerdmri/CMakeLists.txt"
does not match the source
"/src/slicerdmri/CMakeLists.txt"
used to generate cache.
Re-run cmake with a different source directory.
</code></pre>
<p>So,</p>
<ul>
<li>Can this be done, i.e. does <code>slicer/slicer-base:latest</code> contain a Slicer that is already built? If not, do such images exist (PS: I have already gone through <a href="https://github.com/Slicer/SlicerDocker/blob/main/unmaintained-images.rst" rel="noopener nofollow ugc">this note</a>).</li>
<li>I do not find a nightly build of the image used <a href="https://gitlab.com/opendose/opendose3d/-/blob/develop/.gitlab-ci.yml?ref_type=heads" rel="noopener nofollow ugc">by the OpenDose3D extension</a> mentioned in <a href="https://discourse.slicer.org/t/adding-a-ci-build-to-a-slicer-extension/30857/24" class="inline-onebox">Adding a CI build to a Slicer extension - #24 by lassoan</a>, Dokcer only hosting <a href="https://hub.docker.com/u/bishopwolf" rel="noopener nofollow ugc">these possibly related images</a>, none being large enough to host a Slicer build, and not being updated nightly.</li>
<li>What am I missing?</li>
</ul>
<p>Thanks.</p>

---
