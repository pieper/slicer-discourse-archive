# Script repository links should show anchor text rather than generic text

**Topic ID**: 31723
**Date**: 2023-09-14
**URL**: https://discourse.slicer.org/t/script-repository-links-should-show-anchor-text-rather-than-generic-text/31723

---

## Post #1 by @mikebind (2023-09-14 17:58 UTC)

<p>When attempting to help users with questions on this forum, I often provide links to helpful example code on the script repository page.  That page helpfully has html anchors at each heading, so I can provide url links to exactly the part of the page which is going to be relevant.  However, the text which shows up on discourse is always “Script -repository – 3D Slicer documentation”, regardless of which part of the script repository page the link will actually take a user to. Here is an example:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>.  That link will take you directly to the “Customize view layout” script example, while this one will take you to the section on the subject hierarchy node: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>.  It is not helpful that these two links look the same.  Having the raw url in these cases would be much more helpful<br>
<code>https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy</code> vs <code>https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout</code><br>
Even better would be if the discourse text showed “Script repository — 3D Slicer documentation: subject hierarchy”, for example.  I don’t know if there is a way to make that easily happen in discourse, but if so, I would like to request turning that feature on. This would be helpful for links throughout the Slicer documentation, where you can link to any header, but is mostly not that big of a deal because the pages are not usually very long.  The script repository is different because it is very large and the content is so varied, so it is much more helpful to link directly to one place on it and make it clear that the link is going to be relevant.</p>

---

## Post #2 by @lassoan (2023-09-15 02:15 UTC)

<p>Automatic rewriting of unformatted link text is a Discourse feature. It might be possible to customize or improve it - you can ask about it on <a href="https://meta.discourse.org/categories" class="inline-onebox">Categories - Discourse Meta</a></p>
<p>What I usually do when I don’t like the automatically generated link text is I use markdown formatting.</p>
<p>The easiest is to use automatic link (angle brackets). For example:</p>
<pre><code class="lang-txt">&lt;https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy&gt;
</code></pre>
<p>Creates this link:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy</a></p>
<p>For custom link text, you can select the URL and hit Ctrl-K (it uses the inline link formatting: <code>[custom link text](url)</code>). For example:</p>
<pre><code class="lang-txt">[subject hierarchy](https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy) 
</code></pre>
<p>Creates this link:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy">subject hierarchy</a></p>

---

## Post #3 by @mikebind (2023-09-15 15:27 UTC)

<p>Thanks, I didn’t know about the angle brackets option for links. I did know about the custom link text option, but can never remember which type of brackets go with which element and which order they go in, so I inevitably get them wrong the first couple times, and it’s onerous enough that I end up avoiding it if I am trying to be quick.  I did not know about the Ctrl-K shortcut for this feature, and will probably end up using that all the time now.  It would still be marginally nicer if the discourse automatic link test included the anchor text, but this solution will work well enough for me that I’ll mark this solved.</p>

---
