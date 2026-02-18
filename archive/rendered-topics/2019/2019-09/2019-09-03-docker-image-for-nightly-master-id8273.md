# Docker image for `nightly-master`

**Topic ID**: 8273
**Date**: 2019-09-03
**URL**: https://discourse.slicer.org/t/docker-image-for-nightly-master/8273

---

## Post #1 by @unnmdnwb3 (2019-09-03 11:11 UTC)

<p>Hello everyone,</p>
<p>We’d like to introduce a new <strong>docker image</strong> <code>unnmdnwb3/slicer3d-nightly</code>, which offers an environment to test extensions for <em>Slicer 4.11.x</em> (which supports <em>Python 3</em> ). The image is based on Slicer’s branch <code>nightly-master</code> (fixed on commit <a href="https://github.com/Slicer/Slicer/commit/6c6c15c05dbe425500ff55c3b5783f09a09e50cd" rel="nofollow noopener">82f0c50</a>) and shares the <a href="https://github.com/Slicer/SlicerBuildEnvironment/#docker-based-environments" rel="nofollow noopener">base-image</a> <code>slicer/buildenv-qt5-centos7</code> with the official Slicer docker images.</p>
<p>For more information, please consult the following sources:</p>
<ul>
<li>
<strong>Github</strong>: <a href="https://github.com/unnmdnwb3/slicer3d-nightly" rel="nofollow noopener">https://github.com/unnmdnwb3/slicer3d-nightly</a>
</li>
<li>
<strong>Dockerhub</strong>: <a href="https://hub.docker.com/r/unnmdnwb3/slicer3d-nightly" rel="nofollow noopener">https://hub.docker.com/r/unnmdnwb3/slicer3d-nightly</a>
</li>
</ul>
<p>Detailed information and the <code>Dockerfile</code> can be found on the repo itself.</p>
<p><em>Please consider leaving feedback (either here or on the repo), so that we can improve and adjust our current solution!</em></p>
<h4>Background</h4>
<p>We’re a team from <a href="http://opendose.org/" rel="nofollow noopener">Opendose</a> working on an extension for Slicer. Our goal is to provide software that complies to high standards regarding <em>reliability</em> and <em>correctness</em>. Thus, <em>testing</em> of our code is a key-stone of our effort. To facilitate contributing and to enhance our software quality, an automated <em>CI-Pipeline</em> has been built, using <em>Gitlab-CI</em> and <em>Docker</em>.</p>
<p>Considering the eventual upgrade to <em>Slicer 5</em> and therefore the associated move to <em>Python 3</em>, we wanted to develop our extension for <em>Slicer 4.11.x</em>, which supports <em>Python 3</em>.</p>
<p>As far as we know, the existing <a href="https://github.com/thewtex/SlicerDocker" rel="nofollow noopener">official docker images</a> are currently focussed on supporting <em>Slicer 4.10.x</em> and are based on the <code>master</code> <a href="https://github.com/Slicer/Slicer" rel="nofollow noopener">branch</a>, which only supports <em>Python 2</em>.</p>
<p>Thus, we created <code>unnmdnwb3/slicer3d-nightly</code>.</p>
<p>We hope that we can support other teams with this image in their efforts to facilitate testing and build robust software. If you have any <em>questions</em>, I’m more than happy to address them!</p>

---

## Post #2 by @jcfr (2019-09-03 13:09 UTC)

<p>This is outstanding. Thanks for working on this <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>As far as we know, the existing <a href="https://github.com/thewtex/SlicerDocker">official docker images</a> are currently focussed on supporting <em>Slicer 4.10.x</em> and are based on the <code>master</code> <a href="https://github.com/Slicer/Slicer">branch</a>, which only supports <em>Python 2</em> .</p>
</blockquote>
<p>To clarify, the <code>slicer/slicer-base</code> image is built and published daily. It is based of the “nightly” master branch and it includes python3 and Qt5.</p>
<p>To support extension testing, i suggest we “resurrect” the <code>slicer/slicer-build</code> image, this should allow testing of both python and c++ based Slicer extension.</p>
<p><a class="mention" href="/u/unnmdnwb3">@unnmdnwb3</a> Is it something you could help with ?</p>
<p>In the mean time, <a class="mention" href="/u/thewtex">@thewtex</a> could you transfer the  <code>SlicerDocker</code> project to the Slicer organization ?</p>

---

## Post #3 by @unnmdnwb3 (2019-09-03 14:14 UTC)

<p>Hi <a class="mention" href="/u/jcfr">@jcfr</a>, thank you for your support and the kind words! Really appreciated! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="8273">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>To clarify, the <code>slicer/slicer-base</code> image is built and published daily. It is based of the “nightly” master branch and it includes python3 and Qt5.</p>
</blockquote>
</aside>
<p>Ah sorry, seems like I messed something up. I’ve tried to get the <em>python</em> version from <code>slicer/slicer-build</code> but always got this back:</p>
<pre data-code-wrap="bash"><code class="lang-bash">/usr/src/Slicer-build/python-install/bin/SlicerPython -c 'import sys; print(sys.version)'
&gt; 2.7.13 (default, Jan 29 2018, 03:09:51) 
</code></pre>
<p>Do you know how I can find the <code>python3</code> executable on this image?<br>
We could then definitely pick the best parts from both images and merge them!</p>
<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="8273">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p><a class="mention" href="/u/unnmdnwb3">@unnmdnwb3</a> Is it something you could help with ?</p>
</blockquote>
</aside>
<p>Yes sure. Is there anything specific, with which I can assist you? Or do  you mean the whole process?</p>

---

## Post #4 by @unnmdnwb3 (2019-09-03 14:15 UTC)

<p>By the way, we’ve also built a <em>CI-Pipeline</em> based on <code>gitlab-ci</code>, using the <code>unnmdnwb3/slicer3d-nightly</code> image. Are you interested in having a template for the <em>CI-CD</em> integrated into <code>SlicerWizard?</code><br>
This would probably only take a small effort.</p>
<p>If you’re interested, I’d propose to integrate a small template for <code>gitlab-ci</code>, <code>circle-ci</code> and <code>travis</code>?</p>

---

## Post #5 by @lassoan (2019-09-04 14:55 UTC)

<aside class="quote no-group" data-username="unnmdnwb3" data-post="4" data-topic="8273">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/unnmdnwb3/48/4527_2.png" class="avatar"> unnmdnwb3:</div>
<blockquote>
<p>If you’re interested, I’d propose to integrate a small template for <code>gitlab-ci</code> , <code>circle-ci</code> and <code>travis</code> ?</p>
</blockquote>
</aside>
<p>Yes, we would be definitely interested. Please send a pull request with your proposed changes to the <a href="https://github.com/Slicer/Slicer">Slicer/Slicer github repository</a>. Extension templates are defined <a href="https://github.com/Slicer/Slicer/tree/master/Utilities/Templates/Extensions">here</a>.</p>

---

## Post #6 by @thewtex (2019-09-23 20:32 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="8273">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>In the mean time, <a class="mention" href="/u/thewtex">@thewtex</a> could you transfer the <code>SlicerDocker</code> project to the Slicer organization ?</p>
</blockquote>
</aside>
<p>Done! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><a href="https://github.com/Slicer/SlicerDocker" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerDocker: Build, package, test, and run 3D Slicer and Slicer Extensions in Docker.</a></p>

---
