# Slicer Docker images

**Topic ID**: 508
**Date**: 2017-06-15
**URL**: https://discourse.slicer.org/t/slicer-docker-images/508

---

## Post #1 by @jcfr (2017-06-15 15:46 UTC)

<p>Hi,</p>
<p>Just to document that Slicer docker images are now rebuilt every night. This allow to keep working the CircleCI test checking that PR and commits pushed to Slicer code base are not breaking the built.</p>
<p>See <a href="https://github.com/thewtex/SlicerDocker" class="inline-onebox">GitHub - Slicer/SlicerDocker: Build, package, test, and run 3D Slicer and Slicer Extensions in Docker.</a></p>
<p>Scripts driving the build of the docker images, push to dockerhub and update of the repository currently lives on <code>metroplex.kitware</code> Linux build machine. I will publish them when I am back from travelling mid July.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2218dc89d668c736e106e7656701359db4db5da6.png" alt="image" data-base62-sha1="4RDuXWUam0T83fmwD6hCK6MEHTE" width="482" height="414"></p>
<p>Thanks<br>
Jc</p>

---

## Post #2 by @fedorov (2017-12-27 23:42 UTC)

<p>I don’t know if this is expected, but I noticed that “official” slicer docker images take very very long time to start, when used for the purpose of running CLIs:</p>
<pre><code class="lang-auto">docker run -ti slicer/slicer-build /usr/src/Slicer-build/Slicer-build/Slicer \
  --launch RobustStatisticsSegmenter --help

0.02s user 0.02s system 0% cpu 1:53.94 total
</code></pre>
<p>Same CLI run using a docker that downloads and unpacks Slicer binary takes orders of magnitude less time:</p>
<pre><code class="lang-auto">docker run -ti fedorov/slicerdockers:4.8.1 /opt/slicer/Slicer \
  --launch  RobustStatisticsSegmenter --help

0.01s user 0.01s system 1% cpu 1.312 total
</code></pre>
<p>Maybe it makes sense to add an “official” Slicer docker image that uses unpacked binary for the users that want to use Slicer functionality from docker, not for building/testing Slicer extensions.</p>

---

## Post #3 by @jcfr (2017-12-28 08:44 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="2" data-topic="508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Maybe it makes sense to add an “official” Slicer docker image that uses unpacked binary for the users that want to use Slicer functionality from docker, not for building/testing Slicer extensions.</p>
</blockquote>
</aside>
<p>Agreed. That would be a very useful addition.</p>
<p>(Currently, the docker files are hosted on <a href="https://github.com/thewtex/SlicerDocker" class="inline-onebox">GitHub - Slicer/SlicerDocker: Build, package, test, and run 3D Slicer and Slicer Extensions in Docker.</a> during the project week, we will transfer the repository to the Slicer GitHub organization. )</p>
<p>In the mean time, do not hesitate to fork that repo.</p>
<p>Also worth noting that the scripts used to rebuild and publish the docker images on a daily basis are stored at <a href="https://github.com/Slicer/SlicerDockerUpdate" class="inline-onebox">GitHub - Slicer/SlicerDockerUpdate: Helper scripts allowing to automatically re-build and publish Slicer docker images</a></p>

---

## Post #4 by @tbillah (2019-08-28 18:47 UTC)

<p>Where is the dockerfile for this image?</p>
<p><a href="https://hub.docker.com/r/slicer/buildenv-qt5-centos7" class="onebox" target="_blank" rel="nofollow noopener">https://hub.docker.com/r/slicer/buildenv-qt5-centos7</a></p>

---

## Post #5 by @unnmdnwb3 (2019-08-29 11:20 UTC)

<p>Hi <a class="mention" href="/u/tbillah">@tbillah</a>, you can find the Dockerfile for the image on the <a href="https://github.com/Slicer/SlicerBuildEnvironment/blob/master/Docker/qt5-centos7/Dockerfile" rel="nofollow noopener">SlicerBuildEnvironment</a>!</p>

---
