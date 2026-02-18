# Release: OpenDose4D, (need help to finish integration)

**Topic ID**: 10744
**Date**: 2020-03-19
**URL**: https://discourse.slicer.org/t/release-opendose4d-need-help-to-finish-integration/10744

---

## Post #1 by @Alex_Vergara (2020-03-19 14:31 UTC)

<p>Hello</p>
<p>The OpenDose collaboration is proud to announce its first open beta release of the module opendose4d to perform dosimetry calculations in molecular radiotherapy procedures. The code is publicly available at <a href="https://gitlab.com/opendose/opendose4d" rel="nofollow noopener">gitlab</a>.<br>
We need some help to complete Slicer integration, the code already has its own unit testing ready, so every functionality is tested to run.<br>
We already have some alpha testers for the raw code that has proven to be very useful catching bugs. We need also some beta testers that evaluates further the code.<br>
The module expects a multipoint SPECT/CT or multipoint PET/CT, non dynamic. It also is able to proceed with at least one CT, although is not optimal (registration depends now from user).</p>
<p>Regards<br>
<a href="https://www.opendose.org" rel="nofollow noopener">The OpenDose Collaboration</a></p>

---

## Post #2 by @lassoan (2020-03-19 14:52 UTC)

<p>Sounds great. Please send a pull request to ExtensionsIndex that adds your .s4ext file (found in your build folder).</p>

---

## Post #3 by @Alex_Vergara (2020-03-19 15:01 UTC)

<p>I am searching the build folder, but I think you are referring to a c++ build folder for c++ loadable extensions. This whole extension is purely python, there is no build folder.</p>

---

## Post #4 by @jamesobutler (2020-03-19 15:09 UTC)

<p>Do you have plans to make it available through Slicer’s Extension Manager?  Typically I only report bugs/issue bug fixes for extensions that are built by the Slicer organization and report their testing results at <a href="http://slicer.cdash.org/index.php?project=SlicerPreview" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview</a></p>

---

## Post #5 by @Alex_Vergara (2020-03-19 15:10 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="10744">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Do you have plans to make it available through Slicer’s Extension Manager?</p>
</blockquote>
</aside>
<p>yes, that’s the plan</p>

---

## Post #6 by @lassoan (2020-03-19 15:20 UTC)

<p>Even if you only have Python scripted modules, it is useful if you can build your extension, as it allows you to test automatic testing and package creation. It also creates the s4ext file, but you can also easily handcraft an s4ext file (there are many examples in the <a href="https://github.com/Slicer/ExtensionsIndex">ExtensionsIndex repository</a>.</p>

---

## Post #7 by @Alex_Vergara (2020-03-19 15:29 UTC)

<p>I have created a s4ext file</p>
<pre><code class="lang-auto">#
# First token of each non-comment line is the keyword and the rest of the line
# (including spaces) is the value.
# - the value can be blank
#

# This is source code manager (i.e. svn)
scm git
scmurl git://gitlab.com/opendose/OpenDose4D.git
scmrevision develop

# list dependencies
# - These should be names of other modules that have .s4ext files
# - The dependencies will be built first
depends SlicerElastix

# Inner build directory (default is ".")
build_subdirectory .

# homepage
homepage http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/OpenDose4D

# Firstname1 Lastname1 ([SubOrg1, ]Org1), Firstname2 Lastname2 ([SubOrg2, ]Org2)
# For example: Jane Roe (Superware), John Doe (Lab1, Nowhere), Joe Bloggs (Noware)
contributors Alex Vergara Gil (INSERM, France), Janick Rueegger (KSA, Switzerland)

# Match category in the xml description of the module (where it shows up in Modules menu)
category Nuclear Medicine

# url to icon (png, size 128x128 pixels)
iconurl https://gitlab.com/opendose/opendose4d/-/blob/develop/Dosimetry4D/Resources/Icons/Dosimetry4D.png

# Give people an idea what to expect from this code
#  - Is it just a test or something you stand behind?
status stable

# One line stating what the module does
description This module implements the full 3D Dosimetry for molecular radiotherapy on multiple time points.

# Space separated list of urls
screenshoturls

# 0 or 1: Define if the extension should be enabled after its installation.
enabled 1
</code></pre>

---

## Post #8 by @jcfr (2020-03-19 16:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="10744">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it is useful if you can build your extension</p>
</blockquote>
</aside>
<p>Looks like this is already the case, see <a href="https://gitlab.com/opendose/opendose4d/-/blob/develop/CMakeLists.txt" class="inline-onebox">CMakeLists.txt · develop · OpenDose / SlicerOpenDose3D · GitLab</a></p>

---

## Post #9 by @Alex_Vergara (2020-03-19 16:16 UTC)

<p>Probably I am missing something</p>

---

## Post #10 by @lassoan (2020-03-19 16:30 UTC)

<p>The s4ext file has a couple of mistakes (wrong URLs, not ideal branch name), but we can sort these out in the pull request, where there is a comprehensive checklist. So, please send the pull request with this s4ext file and we’ll complete the review there.</p>

---

## Post #11 by @Alex_Vergara (2020-03-19 16:42 UTC)

<p><a href="https://github.com/Slicer/ExtensionsIndex/pull/1689" rel="nofollow noopener">done</a></p>

---
