---
topic_id: 11929
title: "Module Documentation"
date: 2020-06-08
url: https://discourse.slicer.org/t/11929
---

# Module documentation

**Topic ID**: 11929
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/module-documentation/11929

---

## Post #1 by @drouin-simon (2020-06-08 16:04 UTC)

<p>I would like to know what is the current preferred way to write documentation for a Slicer scripted module?</p>
<p>This page suggest writing a wiki page:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/DocumentExtension#Documentation_for_a_scripted_module" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/DocumentExtension#Documentation_for_a_scripted_module</a></p>
<p>We have requested an account here to do so, but no answer:</p>
<p><a href="https://www.slicer.org/wiki/Special:RequestAccount" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Special:RequestAccount</a></p>
<p>Also, I would like to know how to proceed for a new module. Our module is not quite ready yet for publication, but we would like to build the documentation as we go. Is there a way to keep the wiki page private until we publish the module?</p>

---

## Post #2 by @lassoan (2020-06-08 17:48 UTC)

<p>The world has changed since that wiki page was created (at that time github did not exist, it was not trivial to get free hosting, render documentation, etc.). I’ll update it.</p>
<p>We are moving software documentation to the source code repository both for Slicer core and for extensions.</p>
<p>For simple documentation, you can put everything in the top-level README.md file in the repository and rely on Github’s default rendering. For more comprehensive documentation you can add more files, use github pages or readthedocs for rendering pages.</p>

---

## Post #3 by @muratmaga (2020-08-31 16:29 UTC)

<p>I am also on this boat.</p>
<p>Do you have any guidelines about creating the documentation. I found this, <a href="https://discourse.slicer.org/t/document-modules-on-readthedocs/330/18" class="inline-onebox">Document modules on readthedocs</a>  but there isn’t much in it. I am not familiar with readthedocs and how it is pulled from GH. It would be great if someone can point out some Slicer specific examples.</p>
<p>Also, wiki was clunky and while ugly, it had a consistent style across modules. Is the current plan each project doing their own style etc…</p>

---

## Post #4 by @jcfr (2020-08-31 17:40 UTC)

<blockquote>
<p>some Slicer specific examples.</p>
</blockquote>
<p>See <a href="https://github.com/Slicer/Slicer/tree/master/Docs/user_guide/modules" class="inline-onebox">Slicer/Docs/user_guide/modules at main · Slicer/Slicer · GitHub</a></p>

---

## Post #5 by @muratmaga (2020-08-31 17:44 UTC)

<p>Thanks jc. Is there any other documentaiton about how to link these to readdocs?</p>

---

## Post #6 by @lassoan (2020-08-31 17:47 UTC)

<p>I would recommend to start with writing markdown files in Github. Whatever you write, will be usable in readthedocs, too, without any formatting change.</p>
<p>If you end up having dozens of pages of documentation then you can think about how to organize the information better. But I’m not even sure that it is a good approach, as users don’t tend to read lengthy documentation either. Creating more self-explaining modules (using tooltips, wizards, etc.), tutorials (text, slide, or video based), Jupyter notebooks, etc. might be a better time investment than more thorough reference manual.</p>
<p>Read-the-docs is interesting because it is widely used in Python developer community, offers nice navigation between pages, and allows generating documentation using Python (for example, instead of creating screenshots manually, you can run Python code snippets and embed resulting data into the documentation).</p>
<p>We don’t have a good example for an extension with read-the-docs documentation but would be happy to work this out with you (use SlicerMorph as a pilot, then update the extension template based on what we learn).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="11929">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Also, wiki was clunky and while ugly, it had a consistent style across modules. Is the current plan each project doing their own style etc…</p>
</blockquote>
</aside>
<p>I like consistency a lot, but I’m afraid it would be hard to enforce it now. Centralized documentation was a good fit when most Slicer development was paid from a center grant. It was also a decade when software development was not as distributed as now (people still used SVN instead of git, Matlab’s centrally managed toolboxes were the norm instead of Python packages provided by hundreds of thousands of developers, etc.).</p>
<p>We could make the Slicer extension manager something similar to the <a href="https://pypi.org/">Python Package Index (PyPI)</a> - showing structured metadata and a custom “Project description” page (often the same as the main README.md file of the project).</p>

---

## Post #7 by @muratmaga (2020-08-31 18:03 UTC)

<p>THanks. We have plenty of markdown for our modules (on our workshop folders) that we can rework into module documentation.</p>

---
