---
topic_id: 29821
title: "About Creating Customslicer"
date: 2023-06-04
url: https://discourse.slicer.org/t/29821
---

# About creating Customslicer

**Topic ID**: 29821
**Date**: 2023-06-04
**URL**: https://discourse.slicer.org/t/about-creating-customslicer/29821

---

## Post #1 by @dsa934 (2023-06-04 06:08 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Hi slicer users,</p>
<p>So far, I’ve been using it by developing a Python module and adding it as a module extension to Slicer.</p>
<p>However, if you use it like this, it doesn’t matter if you add a new function, but it seems to be a problem when you try to modify an existing function.</p>
<p>Therefore, I want to create a custom slicer.<br>
(e.g. ‘slicerCat’,  <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/#step1" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/#step1</a>)</p>
<p>This post seems out of date. Are there any other resources I should refer to to implement CustomSlicer?</p>
<p>EDIT:<br>
Q1.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44e7613bf02cabdebc224ef8e683881cbc684442.png" alt="image" data-base62-sha1="9Pycd9yJR5T0jHVykrLDO98GpIC" width="435" height="43"><br>
It seemed to say that if you do not modify the git tag, it will connect to the latest version, but there is a problem. Where do I get the git tag hash values for each slicer version?</p>
<p>Q2.<br>
What is the difference between directly building the slicer 5.2.1 code in ‘<a href="https://github.com/Slicer/Slicer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a>’ and using CustomSlicer?</p>

---

## Post #2 by @lassoan (2023-06-04 20:20 UTC)

<p>Using the custom application template has the advantage that you can do lots of customizations without modifying anything in Slicer core. Since you don’t modify Slicer core source files, you can keep getting Slicer core updates without worrying having merge conflicts.</p>
<p>The instructions should be still up-to-date. But if you find anything outdated then let us know. Where did you get that git hash from that is in your screenshot?</p>
<p>You can find Slicer git tags and hashes in <a href="https://github.com/Slicer/Slicer/tree/5.2.2">github</a>. If you want to use Slicer-5.2.2 as the basis of your custom application then you can use <code>5.2.2</code> tag as <code>GIT_TAG</code>.</p>

---

## Post #3 by @dsa934 (2023-06-04 23:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="29821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Using the custom application template has the advantage that you can do lots of customizations without modifying anything in Slicer core. Since you don’t modify Slicer core source files, you can keep getting Slicer core updates without worrying having merge conflicts.</p>
</blockquote>
</aside>
<p>Excellent, If so, is it possible to override functions such as the basic save function of slicer?<br>
For example, is it possible to modify the save function that exists in slicer so that it does not operate unless certain conditions are met?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="29821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The instructions should be still up-to-date. But if you find anything outdated then let us know. Where did you get that git hash from that is in your screenshot?</p>
</blockquote>
</aside>
<pre><code class="lang-auto">pip install cookiecutter jinja2-github
cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate
</code></pre>
<p>The tag value of CmakeList.txt created when the above command was used was used as it is.</p>
<p>Looking for CustomSlicer, it seems to be divided into c++ and python versions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269d729210a3326cb9377cdd11c4029b34db0e25.png" data-download-href="/uploads/short-url/5vBtmOQCZbEGwVEq7tuQgKZzR9H.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269d729210a3326cb9377cdd11c4029b34db0e25.png" alt="image" data-base62-sha1="5vBtmOQCZbEGwVEq7tuQgKZzR9H" width="690" height="490" data-dominant-color="BCBDDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1008×716 40.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I make a c++ version of customslicer, if I make it based on version 5.2.2, can I use the python module in this customslicer? (Can I use python console in c++ custom slicer like normal slicer 5.2.2 above?)</p>

---

## Post #4 by @jcfr (2023-06-04 23:32 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="3" data-topic="29821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>When I make a c++ version of customslicer, if I make it based on version 5.2.2, can I use the python module in this customslicer?</p>
</blockquote>
</aside>
<p>Yes.</p>
<p>Scripted modules can be integrated in custom application built of both <a href="https://github.com/Slicer/Slicer/tree/v5.2.2">Slicer@v5.2.2</a> and the latest version <a href="https://github.com/Slicer/Slicer/tree/main">Slicer@main</a></p>

---

## Post #5 by @dsa934 (2023-06-04 23:40 UTC)

<p>In summary, if you use a custom slicer, you can use the existing method of adding modules(using extension wizard), and you can perform actions such as GUI and basic function overriding without touching the core.</p>
<p>All that’s left is for me to get this build done. Thank you both.</p>

---

## Post #6 by @dsa934 (2023-06-05 00:36 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1d249ae48b8a5e295ef6c1571ccdc18997f3e21.png" data-download-href="/uploads/short-url/rECGRBl7yCNN1oAhYwIWu3pzhdv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1d249ae48b8a5e295ef6c1571ccdc18997f3e21.png" alt="image" data-base62-sha1="rECGRBl7yCNN1oAhYwIWu3pzhdv" width="690" height="61" data-dominant-color="292829"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">695×62 2.08 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">pip install cookiecutter jinja2-github
cookiecutter gh:KitwareMedical/SlicerCustomAppTemplate
</code></pre>
<p>Both ‘v5.2.2’ and ‘5.2.2’ do not work, but if the prompt input that appears when entering the above command is incorrect, does it not work?</p>
<p>Should the git tag have a value like ‘afdkljasflanvsaldslak5safd’ and not ‘5.2.2’?</p>

---

## Post #7 by @jamesobutler (2023-06-05 00:44 UTC)

<p><code>v5.2.2</code> is a valid <code>GIT_TAG</code> for <a>https://github.com/Slicer/Slicer</a> and should successfully check out the source as long as you have a valid internet connection for it to download the source.</p>
<p>What is your value for <code>GIT_REPOSITORY</code> on the line just above <code>GIT_TAG</code>?</p>

---

## Post #8 by @dsa934 (2023-06-05 00:45 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44a37638a36b90191266af2c5c338f87ca3b58aa.png" alt="image" data-base62-sha1="9NcGmy5cAp5LgM0ucjR2xAoX7Si" width="653" height="132"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abba5262688288655846fe0cd37e28d230aee51f.png" alt="image" data-base62-sha1="ovaQ5jxSgU7E1D0i8JzwXYhp7z1" width="284" height="197"></p>
<p>Could it be a problem if I put the settings wrong above? I don’t understand why this doesn’t work</p>

---

## Post #9 by @jcfr (2023-06-05 03:44 UTC)

<pre><code class="lang-diff">    GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/Slicer/Slicer
-    GIT_TAG        '5.2.2'
+    GIT_TAG        "v5.2.2"
    GIT_PROGRESS   1
</code></pre>
<p>See <a href="https://github.com/Slicer/Slicer/tree/v5.2.2">https://github.com/Slicer/Slicer/tree/v5.2.2</a></p>
<p>Single quotes are not supported as a way to delimit a string, there will be part of string.</p>
<p>For reference, see <a href="https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#quoted-argument">https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#quoted-argument</a></p>
<p>To illustrate:</p>
<pre><code class="lang-bash">$ cat /tmp/test.cmake
set(tag_1 'v5.2.2')
message("tag_1 [${tag_1}]")

set(tag_2 "v5.2.2")
message("tag_2 [${tag_2}]")
</code></pre>
<pre><code class="lang-bash">$ cmake -P /tmp/test.cmake
tag_1 ['v5.2.2']
tag_2 [v5.2.2]
</code></pre>

---

## Post #11 by @dsa934 (2023-06-05 04:56 UTC)

<p>I think I saw that something said that the directory creation could not be done because the file name was too long.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69d83bdb072eb74ef19c440b1c34f5e89355d6b1.png" data-download-href="/uploads/short-url/f6lpClcen3AzlpxjfcMgv8BPuw1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69d83bdb072eb74ef19c440b1c34f5e89355d6b1.png" alt="image" data-base62-sha1="f6lpClcen3AzlpxjfcMgv8BPuw1" width="690" height="39" data-dominant-color="323233"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1330×77 2.31 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could this be a git tag issue? Could it be a file path issue? (It seems that the path is not in local…)</p>

---

## Post #12 by @jcfr (2023-06-05 05:53 UTC)

<blockquote>
<p>Could it be a file path issue?</p>
</blockquote>
<p>Based on the reported message, this is most likely the problem.</p>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#set-up-source-and-build-folders">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#set-up-source-and-build-folders</a></p>
<blockquote>
<p>Could this be a git tag issue?</p>
</blockquote>
<p>I don’t think so. Per explanation above, the tag <code>v5.2.2</code> is valid.</p>
<p>For future reference, this git-based screencast demonstrates the complete process:</p>
<ul>
<li>create project using cookiecutter</li>
<li>update <code>CMakeLists.txt</code> setting <code>v5.2.2</code></li>
<li>configure</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e184213800f16e65f1e2f3ad7bd19a2be07e733c.gif" alt="SlicerCustomAppTemplate-x2.5-min" data-base62-sha1="wb0w5uyoJzUzuoIFL80wlrwBZU0" width="690" height="422" class="animated"></p>

---

## Post #13 by @dsa934 (2023-06-05 06:11 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c66dabfaadd20efd07a0bba229a66d588113bb2.png" data-download-href="/uploads/short-url/8Cl0NMaMOMhUjHSVLpoKNwv4wFQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c66dabfaadd20efd07a0bba229a66d588113bb2.png" alt="image" data-base62-sha1="8Cl0NMaMOMhUjHSVLpoKNwv4wFQ" width="690" height="207" data-dominant-color="2B2A2B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1300×390 25.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I think you’re right, the git_tag problem seems to have been passed.</p>
<p>But another road was restricted, so I have two questions.</p>
<p>Q1. Does the project name (currently: Cslicer) always have to be one letter?</p>
<p>Q2. When I cloned and built the normal 3d slicer, I asked for qt 5.15 or higher. Is SlicerCat the same?</p>
<p>edit :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a17a3facccdf893fc39413588366fbd29d326417.png" alt="image" data-base62-sha1="n2uMWBvFq6mlD3oOu5yH453foxx" width="400" height="101"></p>
<p>Isn’t this length limit too tight?</p>
<p>The path to build is automatically specified, but how do I solve the problem that the length is limited?</p>

---

## Post #14 by @dsa934 (2023-06-05 06:38 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7123759b9bd808f067f433931b5d117a6758a343.png" alt="image" data-base62-sha1="g8RVnXi8bOfCkQnNqboKifm2ZXl" width="675" height="292"></p>
<p>I followed the material you posted above, but in my case, there is a difference in that I am building through the "VS community " because I am building on the window OS, and can this cause a character limit?</p>
<p>And there is no process to send “git init, git commit msg” in the description of slicerCAT. Is this a necessary process?</p>

---

## Post #15 by @jcfr (2023-06-05 06:46 UTC)

<blockquote>
<p>Q1. Does the project name (currently: Cslicer) always have to be one letter?</p>
</blockquote>
<p>The project name can have multiple letters.</p>
<p>What need to be short is the build and source directories which are independent of the project name.</p>
<p>As described in the documentation, use a short build directory.</p>
<pre data-code-wrap="diff"><code class="lang-diff">- C:/S/out/build
+C:/SR
</code></pre>
<p>Or any other short name (e.g <code>AR</code>, BR<code>, ... where </code>R` stand for Release, or D would stand for Debug …</p>
<blockquote>
<p>When I cloned and built the normal 3d slicer, I asked for qt 5.15 or higher. Is SlicerCat the same?</p>
</blockquote>
<p>To clarify <code>SlicerCat</code> is an example of custom application illustrating a blog post. See explanation <a href="https://github.com/KitwareMedical/SlicerCAT#should-i-use-this-project-to-create-a-new-custom-application-">here</a></p>
<p>Now this is clarified, the requirement of the custom application you are building are based on the version of Slicer are you specifying in <code>GIT_TAG</code>.</p>
<p>It turns out that Slicer <code>v5.2.2</code> and <code>main</code> are both tested and built using Qt 5.15</p>
<blockquote>
<p>I followed the material you posted above, but in my case, there is a difference in that I am building through the "VS community " because I am building on the window OS, and can this cause a character limit?</p>
</blockquote>
<p>Use shorter path then, this is a limitation of windows.</p>
<p>To summarize, these would be all valid pair of source and build directories:</p>
<pre><code class="lang-auto">C:\A
C:\AR

C:\A0
C:\A0R

C:\B
C:\BR

C:\C
C:\CR
...
</code></pre>

---

## Post #16 by @dsa934 (2023-06-05 06:50 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<aside class="quote no-group quote-modified" data-username="dsa934" data-post="13" data-topic="29821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a17a3facccdf893fc39413588366fbd29d326417.png" alt="image" data-base62-sha1="n2uMWBvFq6mlD3oOu5yH453foxx" width="400" height="101"></p>
</blockquote>
</aside>
<p>Even if you set the directory path to ‘C:\S’(i mean one letter), it seems that the build does not work.</p>
<aside class="quote no-group" data-username="jcfr" data-post="15" data-topic="29821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>To clarify <code>SlicerCat</code> is an example of custom application illustrating a blog post. See explanation <a href="https://github.com/KitwareMedical/SlicerCAT#should-i-use-this-project-to-create-a-new-custom-application-" rel="noopener nofollow ugc">here</a></p>
</blockquote>
</aside>
<p>There are one reasons why I am trying to create a CustomSlicer.<br>
It is easy to ‘add a new function’ to the slicer through the ‘extension wizard’, but to ‘overriding an existing function’, the code of the slicer itself must be modified.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="29821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Using the custom application template has the advantage that you can do lots of customizations without modifying anything in Slicer core. Since you don’t modify Slicer core source files, you can keep getting Slicer core updates without worrying having merge conflicts.</p>
</blockquote>
</aside>
<p>Can I use a customslicer to modify the basic functionality of the slicer without modifying the core? (e.g. When saving data, saving is disabled if certain conditions are not satisfied)</p>
<p>It is possible to create a new save function in the form of adding a shortcut, but the intention is to directly modify some of the basic functions of 3d slicer.</p>
<p>If CustomSlicer can’t serve the purpose above, I guess I’ll have to build the slicer itself.</p>

---

## Post #17 by @dsa934 (2023-06-05 12:23 UTC)

<p>…?</p>
<p>I really don’t know what it is</p>
<p>Edit :</p>
<p>1.normal  5.2.1 slicer build (access denied)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d9538b0abf973e54ccfc2f0aac8b3bfeb6015c5.png" data-download-href="/uploads/short-url/1W9UzZvAk9rRYjKuaQhgu5EeLgV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d9538b0abf973e54ccfc2f0aac8b3bfeb6015c5.png" alt="image" data-base62-sha1="1W9UzZvAk9rRYjKuaQhgu5EeLgV" width="690" height="70" data-dominant-color="323233"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1241×126 2.72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
2. SlicerCAT build</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42477e51592225933cef39814cf7cb24cccde157.png" data-download-href="/uploads/short-url/9skGASKY2l1EakadvnvdmPbgaCH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42477e51592225933cef39814cf7cb24cccde157.png" alt="image" data-base62-sha1="9skGASKY2l1EakadvnvdmPbgaCH" width="690" height="66" data-dominant-color="323233"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1523×146 2.71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
3.normal 5.2.2 slicer (access denied)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8e0e743cbf683d7bca77e3b8e0c9fbdcbecbfc2.png" data-download-href="/uploads/short-url/uWAZbzKWVaWuOEihpeBw7wzSe1c.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8e0e743cbf683d7bca77e3b8e0c9fbdcbecbfc2.png" alt="image" data-base62-sha1="uWAZbzKWVaWuOEihpeBw7wzSe1c" width="690" height="151" data-dominant-color="323233"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1338×294 6.08 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji only-emoji" alt=":sob:" loading="lazy" width="20" height="20"></p>

---

## Post #18 by @lassoan (2023-06-05 15:48 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="16" data-topic="29821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>overriding an existing function’, the code of the slicer itself must be modified.</p>
</blockquote>
</aside>
<p>There are lots of mechanisms in Slicer for customizing the behavior without the need to change the Slicer core source code. If you don’t find how to modify any specific behavior without Slicer core modifications then let us know.</p>
<aside class="quote no-group" data-username="dsa934" data-post="16" data-topic="29821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>When saving data, saving is disabled if certain conditions are not satisfied</p>
</blockquote>
</aside>
<p>You can replace the save dialog by your own by registering a custom <code>qSlicerFileDialog</code> for <code>NoFile</code> type (that refers to the scene save dialog).</p>
<p>You can change the behavior an application exit (by default: ask for confirmation and if scene is changed then offer saving) as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#override-application-close-behavior">here</a>.</p>

---

## Post #19 by @dsa934 (2023-06-06 03:33 UTC)

<p>Please confirm if I am misunderstanding the slicer.</p>
<p>New function: Can be implemented by adding a module through ‘extension wizard’</p>
<p>Modification of existing functions: There is a way to customize without modifying the sclier core.</p>
<p>So why does CustomSlicer (SlicerCAT) exist?<br>
Is the purpose of using it to customize the logo, GUI environment, etc. to suit my purpose without simply changing the slicer core?</p>
<p>For example, there are two ways to save work in slicer as far as I know.</p>
<ul>
<li>Click the Save icon.</li>
<li>Shortcut (“Ctrl+s”)</li>
</ul>
<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="29821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can replace the save dialog by your own by registering a custom <code>qSlicerFileDialog</code> for <code>NoFile</code> type (that refers to the scene save dialog).</p>
<p>You can change the behavior an application exit (by default: ask for confirmation and if scene is changed then offer saving) as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#override-application-close-behavior" rel="noopener nofollow ugc">here</a>.</p>
</blockquote>
</aside>
<p>This method seems to be a way to modify the filediaglog that pops up when the ‘SaveIcon’ is clicked.<br>
However, if ‘override’ is applied to a shortcut that has already been designated, it will not be applied.</p>
<p>==============================================</p>
<p>‘Save function modification’ is just an example of a case where an existing function needs to be modified.</p>
<p>I thought it would be simpler to use the ‘Extension Wizard’ if you were adding your own modules(New function ) to the Slicer, and if you were customizing an existing function(save, load dicom, etc … ) , it would be simpler to directly access and modify the implementation part of the function.</p>
<p>I understand that if you are developing in the form of a ‘plugin’ in the current slicer, it will be more convenient to use CustomSlicer in this case because it is difficult to modify the existing function. Did I misunderstand?</p>
<p>Then, the purpose of CustomSlicer is to activate only the functions that the user wants in the slicer to make it light, and for direct modification of existing functions, is there no difference between building and using ‘Slicer’ or ‘CustomSlicer’?</p>

---
