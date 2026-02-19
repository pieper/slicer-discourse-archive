---
topic_id: 1205
title: "Document Modules Using Mkdocs"
date: 2017-10-10
url: https://discourse.slicer.org/t/1205
---

# Document modules using mkdocs

**Topic ID**: 1205
**Date**: 2017-10-10
**URL**: https://discourse.slicer.org/t/document-modules-using-mkdocs/1205

---

## Post #1 by @Lorensen (2017-10-10 23:25 UTC)

<p>Have you looked at mkdocs? <a href="http://www.mkdocs.org/" rel="nofollow noopener">http://www.mkdocs.org/</a></p>
<p>Is generates a static website that is very fast. I’ve been using it for the<br>
VTKExamples: <a href="https://lorensen.github.io/VTKExamples/site/" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/</a></p>
<p>It does have hooks for a google custom search engine, google analytics.<br>
Also several look feel’s. I chose the material look<br>
<a href="http://squidfunk.github.io/mkdocs-material/" rel="nofollow noopener">http://squidfunk.github.io/mkdocs-material/</a> .  It is built using<br>
Google’s Material<br>
Design <a href="https://material.io/guidelines/material-design/" rel="nofollow noopener">https://material.io/guidelines/material-design/</a> guidelines.</p>
<p>I use github pages to host the source repository and the static site. I<br>
admit I had special requirements since the bulk of the VTKExamples site is<br>
source code.</p>
<p>I did not look at readthedocs.</p>
<p>Bill</p>

---

## Post #2 by @Lorensen (2017-10-10 23:29 UTC)

<p>Here’s  a talk I gave at Kitware recently…</p>
<p><a href="https://github.com/lorensen/VTKExamples/blob/master/src/Artifacts/VTKExamplesStatus2017.pdf" class="onebox" target="_blank" rel="nofollow noopener">https://github.com/lorensen/VTKExamples/blob/master/src/Artifacts/VTKExamplesStatus2017.pdf</a></p>

---

## Post #3 by @lassoan (2017-10-12 15:28 UTC)

<p>Using MkDocs for Slicer core documentation:<br>
My understanding is that MkDocs uses Markdown as input format. We’ve been considering Markdown for Slicer core documentation but it seemed that “standard” Markdown was too limited and we did not want to choose a certain flavor, that is only understood by a single software. RestructedText with Sphinx generator seemed a more powerful and standardized option. We’ve created a couple of pages (see for example here: <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a>) and it works OK, but we’ll see how it holds up when we add more content.</p>
<p>Using MkDocs for extension documentation:<br>
Historically (when there were no easily available free hosting available) extensions were documented on the slicer wiki, but this does not make much sense anymore. Typically, when we receive request to add a new extension, it comes without any documentation. As a minimum, we ask people to write a short description and tutorial in the <a href="http://readme.md">readme.md</a> file in their github repository - which is probably the simplest possible thing to do. There is no need to set up any extra generator for documentation, as github’s basic rendering is acceptable.</p>
<p><a class="mention" href="/u/lorensen">@Lorensen</a> How do you think mkdocs could fit into the picture? How it could be used for improving what we have now?</p>

---

## Post #4 by @Lorensen (2017-10-12 16:02 UTC)

<p>rst is certainly more powerful (and complicated) than markdown. rst is more suited to “technical writers” than markdown which is quite simple, yet limited. For the main Slicer documentation I can see how rst is the right choice. The Slicer core team is sophisticated and can do a great job with rst/Sphinx.  In my case, for VTKExamples, markdown is a better fit since 90% of the site is generated automatically from source code and simple markdown.</p>

---

## Post #5 by @fedorov (2017-10-12 20:21 UTC)

<p>Another platform that uses Markdown is GitBook, we use it to document some of our extensions, eg <a href="https://qiicr.gitbooks.io/dcmqi-guide/content/">https://qiicr.gitbooks.io/dcmqi-guide/content/</a></p>
<p>The added benefit of GitBook is that it provides a rich text editor in-browser, and supports collaborative development via change requests and questions, which means non-technical users can contribute changes to the content, or ask questions about the content, without ever having to learn what git is. For the full disclosure - we have not reached a point when we get content from arbitrary users, but it is possible…</p>

---

## Post #6 by @jcfr (2017-10-12 20:35 UTC)

<p>Here is a comparison of MediaWiki, and GitHub+GitBook<br>
See <a href="https://www.slicer.org/wiki/Documentation/Labs/DocumentationImprovments#New_Platform:_Comparison" class="inline-onebox">Documentation/Labs/DocumentationImprovments - Slicer Wiki</a></p>
<blockquote>
<p>GitBook … reached a point when we get content from arbitrary users</p>
</blockquote>
<p>I was able to contact GitBook team but they didn’t follow up when I asked about getting free access for Slicer users.</p>

---

## Post #7 by @Lorensen (2017-10-12 23:19 UTC)

<p>A nice feature of mkdocs, since it generates a static site, a user can<br>
preview the entire website before committing changes with a browser<br>
using</p>
<p>python -m SimpleHTTPServer</p>
<p>For example, you can work disconnected from the internet (on a plane,<br>
in New Hampshire, on the Mass Pike, etc.)</p>

---

## Post #8 by @jcfr (2017-10-13 19:42 UTC)

<p>Being able to generate the extension locally is important, both sphinx and mkdocs support this.</p>
<p>With sphinx, you can simply open the generated <code>index.html</code></p>

---

## Post #9 by @fedorov (2018-10-29 20:30 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="1205">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Another platform that uses Markdown is GitBook, we use it to document some of our extensions, eg <a href="https://qiicr.gitbooks.io/dcmqi-guide/content/">https://qiicr.gitbooks.io/dcmqi-guide/content/ </a></p>
</blockquote>
</aside>
<p>I retract my suggestion for considering GitBook at all. In the recent upgrade of the system, GitBook made (in my view) an unfortunate decision to move to a proprietary format for content markup, without providing any documentation or any way to edit the content directly as text. The only way to edit content is via their own web-based editor. This works quite well as long as you use the features that work, but it is easy to get stuck once one deviates from that, or encounters a bug (of which there are many). After all the hopes I had for GitBook, I have to say it did not live to (my) expectations. ReadTheDocs is a better choice.</p>

---
