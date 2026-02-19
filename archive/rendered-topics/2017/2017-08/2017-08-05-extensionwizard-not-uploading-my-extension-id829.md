---
topic_id: 829
title: "Extensionwizard Not Uploading My Extension"
date: 2017-08-05
url: https://discourse.slicer.org/t/829
---

# ExtensionWizard not uploading my extension

**Topic ID**: 829
**Date**: 2017-08-05
**URL**: https://discourse.slicer.org/t/extensionwizard-not-uploading-my-extension/829

---

## Post #1 by @moselhy (2017-08-05 08:00 UTC)

<p>Hello,</p>
<p>I am trying to upload <a href="https://github.com/moselhy/PhantomSegmenter" rel="noopener nofollow ugc">this extension</a>, but for some reason I am getting this error about a documentation url… I followed all the instructions <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ExtensionWizard#Contributing_Extensions_to_the_Index" rel="noopener nofollow ugc">here</a> and the --describe option works fine.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80b2759e6f65be68aa767379e4eb58c232cd6a56.png" data-download-href="/uploads/short-url/imvsKW2f1uT6nsOcqS5KLi6YTae.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80b2759e6f65be68aa767379e4eb58c232cd6a56.png" alt="image" data-base62-sha1="imvsKW2f1uT6nsOcqS5KLi6YTae" width="690" height="87" data-dominant-color="151614"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">700×89 5.78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2017-08-05 12:01 UTC)

<p>I’ve never needed command-line interface of ExtensionWizard. You can do all Slicer-specific operations using graphical user interface of ExtensionWizard module. I find pushing files, sending pull requests simpler to do using generic tools (simple git commands) rather than learning ExtensionWizard commands.</p>
<p>Does anybody use ExtensionWizard command-line? For what operations? Maybe we can delete rarely used commands to reduce associated documentation, testing, support, and maintenance work.</p>

---

## Post #3 by @moselhy (2017-08-05 19:52 UTC)

<p>So to upload my extension to the extension manager, do I just have to make an s4ext file and submit a pull request to <a href="https://github.com/Slicer/ExtensionsIndex" rel="nofollow noopener">https://github.com/Slicer/ExtensionsIndex</a>?</p>

---

## Post #4 by @fedorov (2017-08-05 20:33 UTC)

<aside class="quote no-group quote-modified" data-username="moselhy" data-post="3" data-topic="829" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moselhy/48/501_2.png" class="avatar"> moselhy:</div>
<blockquote>
<p>So to upload my extension to the extension manager, do I just have to make an s4ext file and submit a pull request to <a href="https://github.com/Slicer/ExtensionsIndex" class="inline-onebox">GitHub - Slicer/ExtensionsIndex: Slicer extensions index</a>?</p>
</blockquote>
</aside>
<p>Yes! And the s4ext file should be created automatically in the build directory for your extension.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve never needed command-line interface of ExtensionWizard.</p>
</blockquote>
</aside>
<p>Me neither, but as I was looking for the page with the instructions to share with <a class="mention" href="/u/moselhy">@moselhy</a>, I found that <code>slicerExtensionWizard --contribute</code> is mentioned as one of the recommended approaches for contributing extensions, and it definitely looks more attractive than the other option, see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions" class="inline-onebox">Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions - Slicer Wiki</a>.</p>
<p>I can see how the other option mentioned can be confusing to a beginner:</p>
<blockquote>
<p>Fork ExtensionIndex repository (<a href="https://github.com/Slicer/ExtensionsIndex" class="inline-onebox">GitHub - Slicer/ExtensionsIndex: Slicer extensions index</a>), add your extension, and send a pull request</p>
</blockquote>

---

## Post #5 by @lassoan (2017-08-05 23:51 UTC)

<p>I’ve added more specific instructions about how to upload a .s4ext file to the ExtensionIndex to a forked repository and send a pull request (although nowadays most developers use GitHub, so already familiar with the workflow). It is nice that all steps (fork repository, upload file, send pull request) are available directly on the web interface, by a few clicks.</p>

---

## Post #6 by @jcfr (2017-08-07 21:17 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>And the s4ext file should be created automatically in the build directory for your extension.</p>
</blockquote>
</aside>
<p>The good news, is that this is already the case. The description is created in the build directory of every extension</p>
<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I found that slicerExtensionWizard --contribute is mentioned as one of the recommended approaches for contributing extensions, and it definitely looks more attractive than the other option</p>
</blockquote>
</aside>
<p>Our of curiosity and to put things in context, which “other options” are you referring to ? It looks like the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions">wiki page</a> always suggested to use <code>slicerExtensionWizard --contribute</code></p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can do all Slicer-specific operations using graphical user interface of ExtensionWizard module. I find pushing files, sending pull requests simpler to do using generic tools (simple git commands) rather than learning ExtensionWizard commands.</p>
<p>Does anybody use ExtensionWizard command-line? For what operations? Maybe we can delete rarely used commands to reduce associated documentation, testing, support, and maintenance work.</p>
</blockquote>
</aside>
<p>Agreed. Now that few years went by, it may a good time to streamline the process.</p>

---

## Post #7 by @fedorov (2017-08-07 22:07 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Our of curiosity and to put things in context, which “other options” are you referring to ?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a> there were (and still are, after <a class="mention" href="/u/lassoan">@lassoan</a> edits) two options listed on the wiki: make a pull request manually, or use slicerExtensionWizard to automatically make a pull request with --contribute.</p>

---

## Post #8 by @jcfr (2017-08-07 22:40 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="7" data-topic="829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>two options listed on the wiki:</p>
</blockquote>
</aside>
<p>I see.</p>
<p>There are indeed two pages linked of the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Extension">extension How-tos</a>:</p>
<ol>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Contribute_Extension_Description_File_using_Extension_Wizard">Contribute Extension Description File using Extension Wizard</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Contribute_Extension_Description_File">Manually contributing an extension description file</a></li>
</ol>
<p>That said, the main point of entry <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions">Create Slicer Extension</a> linked of the build instructions found on the main page (and also in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/StartHere">new member check list</a>) only mention the extension wizard approach.  If you think that would help reduce confusion (if any), we could remove that second page ?</p>

---

## Post #9 by @fedorov (2017-08-08 01:50 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="8" data-topic="829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>That said, the main point of entry Create Slicer Extension linked of the build instructions found on the main page (and also in the new member check list) only mention the extension wizard approach.</p>
</blockquote>
</aside>
<p>I must be missing something - it actually mentions both approaches.</p>
<p>From <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions:">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions:</a></p>
<p>"If you consider your extension is ready for distribution, contribute it to the ExtensionsIndex:</p>
<ul>
<li>Fork ExtensionIndex repository on GitHub by clicking Fork button on <a href="https://github.com/Slicer/ExtensionsIndex" class="inline-onebox">GitHub - Slicer/ExtensionsIndex: Slicer extensions index</a> page</li>
<li>Add your .s4ext file to your forked repository: it can be done using a git client or simply by clicking Upload files button</li>
<li>Create a pull request: by clicking Create pull request button</li>
<li>Note: the Extension Wizard can automate this by the following command:"</li>
</ul>

---

## Post #10 by @jcfr (2017-08-08 02:45 UTC)

<p>I missed that. The initial version was only mentioning the extension wizard. See <a href="https://www.slicer.org/w/index.php?title=Documentation/Nightly/Developers/Tutorials/BuildTestPackageDistributeExtensions&amp;oldid=47405">here</a></p>
<p>Then, in  Nov 2016, <a class="mention" href="/u/lassoan">@lassoan</a> improved the page explaining that both approaches were possible. See <a href="https://www.slicer.org/w/index.php?title=Documentation%2FNightly%2FDevelopers%2FTutorials%2FBuildTestPackageDistributeExtensions&amp;type=revision&amp;diff=47413&amp;oldid=47405">here</a>  and more recently updated adding details about s4ext. See <a href="https://www.slicer.org/w/index.php?title=Documentation%2FNightly%2FDevelopers%2FTutorials%2FBuildTestPackageDistributeExtensions&amp;type=revision&amp;diff=53944&amp;oldid=53437">here</a></p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> Would you suggest to remove the mention of pull request ? Or should we change the text to something like:</p>
<aside class="quote no-group">
<blockquote>
<p>If you consider your extension is ready for distribution, contribute it to the ExtensionsIndex using the Extension Wizard:</p>
<pre><code class="lang-auto">$ bin/slicerExtensionWizard --contribute ~/Slicer-MyExtension/
</code></pre>
<p>User having a working knowledge of git can also manually contribute the description file following these steps:</p>
<ol>
<li>Fork ExtensionIndex repository on GitHub by clicking Fork button on <a href="https://github.com/Slicer/ExtensionsIndex" class="inline-onebox">GitHub - Slicer/ExtensionsIndex: Slicer extensions index</a> page</li>
<li>Add your .s4ext file to your forked repository: it can be done using a git client or simply by clicking Upload files button</li>
<li>Create a pull request: by clicking Create pull request button</li>
</ol>
</blockquote>
</aside>

---

## Post #11 by @lassoan (2017-08-08 12:01 UTC)

<p>I feel that the world has changed a lot in the last few years. Git and GitHub has become mainstream, so forking, branchinc, modifying files, and sending pull request are the norm. ExtensionWizard’s commands shorten the command line but they are non-standard and hide what happens internally, making things look more complex than they really are.</p>
<p>We can keep the scripts as they are and documentation will be generated for it automatically, but I don’t think we should advertise them on the wiki at all.</p>

---

## Post #12 by @fedorov (2017-08-08 13:06 UTC)

<p>I agree with Andras. Slilcer ExtensionWizard is a “one off” thing that developers need to take effort to remember how to use, and it doesn’t always work. Working with git and GitHub is an essential skill that every open source developer should be motivated to learn. I certainly hope that developers contributing extension to Slicer are familiar with the basics of GitHub, such as how to make a PR!</p>

---

## Post #13 by @moselhy (2017-08-08 14:53 UTC)

<p>Thank you for the clarification. See <a href="https://github.com/Slicer/ExtensionsIndex/pull/1444" rel="nofollow noopener">this pull request</a>.</p>
<p><code>Yes! And the s4ext file should be created automatically in the build directory for your extension.</code></p>
<p>I had to generate the description file using the bin/slicerExtensionWizard --describe command and save the output into the .s4ext file, because I couldn’t find the s4ext file in my build directory. Is this a bug or am I doing something wrong?</p>

---

## Post #14 by @fedorov (2017-08-08 15:32 UTC)

<aside class="quote no-group" data-username="moselhy" data-post="13" data-topic="829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moselhy/48/501_2.png" class="avatar"> moselhy:</div>
<blockquote>
<p>I had to generate the description file using the bin/slicerExtensionWizard --describe command and save the output into the .s4ext file, because I couldn’t find the s4ext file in my build directory. Is this a bug or am I doing something wrong?</p>
</blockquote>
</aside>
<p>I don’t know. I personally never used the auto-generated s4ext.</p>

---

## Post #15 by @jcfr (2017-08-08 15:39 UTC)

<aside class="quote no-group" data-username="moselhy" data-post="13" data-topic="829">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moselhy/48/501_2.png" class="avatar"> moselhy:</div>
<blockquote>
<p>Yes! And the s4ext file should be created automatically in the build directory for your extension.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/moselhy">@moselhy</a> You can find it in the build tree. For example:</p>
<pre><code class="lang-auto">$ git clone https://github.com/moselhy/SequenceRegistration
$ mkdir SequenceRegistration-build
$ cd SequenceRegistration-build/
$ cmake -DCMAKE_BUILD_TYPE:STRING=Release -DSlicer_DIR:PATH=/home/jcfr/Projects/Slicer-2-build/Slicer-build/ ../SequenceRegistration

$ make -j6
[...]
-- Configuring Scripted module: Elastix4D
-- Extension description has been written to: /tmp/SequenceRegistration-build/SequenceRegistration.s4ext   &lt;------------
[...]
-- Build files have been written to: /tmp/SequenceRegistration-build

$ pwd
/tmp/SequenceRegistration-build

$ ls *.s4ext
SequenceRegistration.s4ext
</code></pre>
<p>You should also see the following message reported when configuring:</p>
<pre><code class="lang-auto">Extension description has been written to: /tmp/SequenceRegistration-build/SequenceRegistration.s4ext
</code></pre>
<p>Content of the generated file:</p>
<pre><code class="lang-auto">$ cat SequenceRegistration.s4ext
[...]
# This is source code manager (i.e. svn)
scm git
scmurl https://github.com/moselhy/SequenceRegistration
scmrevision 39fe467

# list dependencies
# - These should be names of other modules that have .s4ext files
# - The dependencies will be built first
depends Sequence SlicerElastix

# Inner build directory (default is ".")
build_subdirectory .

# homepage
homepage https://github.com/moselhy/SequenceRegistration

# Firstname1 Lastname1 ([SubOrg1, ]Org1), Firstname2 Lastname2 ([SubOrg2, ]Org2)
# For example: Jane Roe (Superware), John Doe (Lab1, Nowhere), Joe Bloggs (Noware)
contributors Mohamed Moselhy (Western University), Andras Lasso (PerkLab, Queen's University)

# Match category in the xml description of the module (where it shows up in Modules menu)
category Registration

# url to icon (png, size 128x128 pixels)
iconurl https://raw.githubusercontent.com/moselhy/SequenceRegistration/master/Elastix4D/Resources/Icons/Elastix4D.png

# Give people an idea what to expect from this code
#  - Is it just a test or something you stand behind?
status 

# One line stating what the module does
description This will register a multi-volume sequence using Elastix.

# Space separated list of urls
screenshoturls https://raw.githubusercontent.com/moselhy/SequenceRegistration/master/screenshot.png

# 0 or 1: Define if the extension should be enabled after its installation.
enabled 1
</code></pre>

---

## Post #16 by @moselhy (2017-08-09 15:11 UTC)

<p>Thank you, it makes sense now</p>

---
