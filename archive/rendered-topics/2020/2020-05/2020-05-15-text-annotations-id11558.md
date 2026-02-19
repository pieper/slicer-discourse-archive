---
topic_id: 11558
title: "Text Annotations"
date: 2020-05-15
url: https://discourse.slicer.org/t/11558
---

# Text annotations

**Topic ID**: 11558
**Date**: 2020-05-15
**URL**: https://discourse.slicer.org/t/text-annotations/11558

---

## Post #1 by @joachim (2020-05-15 13:47 UTC)

<p>I would like to add notes to my project. I thought this feature could be found in the <em>Annotation</em> module, but I haven’t found anything in Slicer, so I guess this is a feature request.</p>
<p>Plain text will work, but it would also be nice if I could make use of Markdown: either just syntax highlighting (like in vim) or “rendered” Markdown.</p>
<p>What do you think? Currently, I use a <code>readme.md</code> file in my project’s folder but this will not be included if I make a <code>.mrb</code> bundle of my project.</p>

---

## Post #2 by @pieper (2020-05-15 14:36 UTC)

<p>Hi - the latest nightlies have a Texts module for this.  Multiple Text nodes can be saved with the scene.  Let us know if that works for you.  It’s just text now, but could be extended.  HTML would be easy, markdown would be a little more work.  Happy to provide advice if anyone wants to do the work.</p>

---

## Post #3 by @joachim (2020-05-15 16:36 UTC)

<p>Very nice!</p>
<p>I don’t think editing HTML is practical for the end user. Markdown could however be. Qt seems to have <a href="https://doc.qt.io/qt-5/qtwidgets-richtext-syntaxhighlighter-example.html" rel="nofollow noopener">functionality for syntax highlighting</a>. I use Markdown when I write notes since Vim does syntax highlighting automatically. This makes my notes clear.</p>
<p>Rendering markdown may be overkill. However, a quick look at Github shows a MIT-licensed library <a href="https://github.com/sevenjay/cpp-markdown" rel="nofollow noopener">cpp-markdown</a> for markdown to HTML. There is also a newer header-only, MIT-licensed library called <a href="https://github.com/progsource/maddy" rel="nofollow noopener">maddy</a>. But this library relies on C++14.</p>
<p><strong>PS:</strong> Will Slicer start to use/allow C++14? C++14 makes C++ much more effective!</p>

---

## Post #4 by @pieper (2020-05-15 17:08 UTC)

<p>So far we are just requiring C++11 and it’s not clear when we can move that forward.  I’d actually like C++17 someday too.</p>
<p>Adding markdown via C++ would be the most general of course, but if we wanted to shortcut things adding python markdown would be relatively easier to implement.  A webengine implementation would also be an option.</p>

---

## Post #5 by @joachim (2020-05-15 18:31 UTC)

<p>So Slicer allows C++11? That is something I can live with (I mixed C++11 with C++14). C++11 is the new language, C++14 is mainly a bugfix of C++11, and C++17 is mainly a bugfix of C++14. I too can enjoy C++17 since it has some STL-functions I’ve been missing in C++14.</p>
<p>I don’t think it is productive to make the <em>Texts</em> module very advanced. Implementing the Qt syntax highlighting could however be a nice way for me to get into Slicer development.</p>

---

## Post #6 by @pieper (2020-05-15 18:47 UTC)

<p>Yes, C++11 is a requirement now, so any new Slicer code can definitely use it.</p>
<p>I did a quick search and didn’t find an existing C++ markdown example, but as I suspected there is a <a href="https://doc.qt.io/qt-5/qtwebengine-webenginewidgets-markdowneditor-example.html">webengine-based</a> version.</p>

---

## Post #7 by @joachim (2020-05-15 19:30 UTC)

<p>I have some suggestions to improve the current <em>Texts</em> module:</p>
<ul>
<li>Use monospaced font. In this way you can make tables etc. This will also let your notes stand out compared to the application font for a better user experience.</li>
<li>It should be possible to just type in your notes directly without clicking the <em>Edit</em> button. And remove the <em>Save</em> and <em>Cancel</em> buttons. I didn’t see those buttons, so when I tried to Clone the text node in Data view, the text was not copied.</li>
</ul>
<p>Where should I put my suggestions? As an <em>Issue</em> at <a href="https://github.com/Slicer/Slicer/issues" rel="nofollow noopener">https://github.com/Slicer/Slicer</a>?</p>

---

## Post #8 by @pieper (2020-05-15 19:47 UTC)

<p>Yes, a github issue would be the place to start and the exact behavior can be refined there and in a corresponding pull request with an implementation.  The changes you suggest sound reasonable to me, but I don’t use the Text module myself so I’m sure others have opinions.  Thanks for jumping in on this <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #9 by @lassoan (2020-05-15 20:51 UTC)

<p>Markdown is actually very easy now, as you can use markdown in <a href="https://doc.qt.io/qt-5/qtextedit.html#markdown-prop">QTextEdit</a>. You can also get the markdown rendering as html to be displayed elsewhere in the application where only html is accepted. To get all these, we need to update our Qt version to 5.14.</p>

---

## Post #10 by @jamesobutler (2020-05-15 21:03 UTC)

<p>The last version of Qt5, <a href="https://wiki.qt.io/Qt_5.15_Release" rel="nofollow noopener">Qt 5.15</a> is scheduled for release in a few days on Tuesday.  Might make sense to get all platform versions updated to that instead of my previous attempts to get them all to Qt 5.12.</p>

---

## Post #11 by @pieper (2020-05-15 21:14 UTC)

<p>That makes sense.  My windows build is using 5.14 with no problems (that I’ve seen so far anyway)</p>

---

## Post #12 by @Sam_Horvath (2020-05-15 21:18 UTC)

<p>I will start next week the process of updating the factories (this has been on my plate for a while).  The Linux build will take the longest, as I am not sure how the changes to the Qt installer (i.e. requiring an account) will affect the generation of the docker image we use to build.</p>
<p>For Windows, this will also require switching to VS 2017 on the factory.</p>

---

## Post #13 by @joachim (2020-05-15 21:33 UTC)

<p>Do you think markdown notes is a nice feature? I would like it.</p>
<p>The markdown feature in Qt 5.14 for <code>QTextEdit</code> seems to be a converter to and from Markdown which is possible since <code>QTextEdit</code> can contain rich text (?). Therefore it will be easy to “render” markdown formatted text. I’m not sure if you can edit markdown text in the <code>QTextEdit</code>. If not, I think an editor with Markdown syntax highlighting is more important than rendering, if the <em>Texts</em> module should mainly be used to write own notes. Notes are something you write on the fly.</p>

---

## Post #14 by @lassoan (2020-05-16 04:00 UTC)

<aside class="quote no-group" data-username="joachim" data-post="13" data-topic="11558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> joachim:</div>
<blockquote>
<p>Therefore it will be easy to “render” markdown formatted text. I’m not sure if you can edit markdown text in the <code>QTextEdit</code> .</p>
</blockquote>
</aside>
<p>Yes, you can edit markdown in QTextEdit, because it is plain, unformatted text. When editing is finished then the text is set as markdown text in QTextEdit, which renders it with nice formatting.</p>

---

## Post #15 by @joachim (2020-05-16 14:13 UTC)

<p>OK!</p>
<p>BTW, I built Slicer for the first time yesterday. It built like a charm on macOS with <a href="https://brew.sh/" rel="nofollow noopener">Homebrew</a> (I had some small problems in the beginning; the wiki page should be updated). Not many software projects builds and runs that smoothly. I look forward to learn more.</p>

---

## Post #16 by @pieper (2020-05-16 14:39 UTC)

<p>It would be great if we could migrate all the build instructions from the wiki to the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html">git repository and readthedocs</a>.  We don’t even have a placeholder for that yet, but any PRs would be most welcome.</p>

---

## Post #17 by @lassoan (2020-05-16 16:08 UTC)

<p>Added a ticket to track this task:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4924" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4924" target="_blank">Migrate Slicer build instructions to git</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-05-16" data-time="16:06:26" data-timezone="UTC">04:06PM - 16 May 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Build instructions are very tightly linked to the source code, so it should be stored in the repository.</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:documentation</span>
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:enhancement</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #18 by @lassoan (2020-05-21 19:00 UTC)

<p>FYI, Slicer now uses Qt-5.14.1, so markdown editing and display is available! It works very nicely.</p>
<p>For example, create a textbox:</p>
<pre data-code-wrap="python"><code class="lang-python">t=qt.QTextEdit()
t.show()
</code></pre>
<p>Type some markdown text into it:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1ba27b20e9daf92da25e6a0871d6aecfe22d8cf0.png" alt="image" data-base62-sha1="3Wt0lr8NrBRtz3685mEp91rJVO8" width="514" height="430"></p>
<p>Then run this code to render it as markdown (you can also do some limited WYSIWYG editing, but the behavior is not so obvious, as not all formatting can be translated back to markdown; so I would disable editing):</p>
<pre data-code-wrap="python"><code class="lang-python">t.setMarkdown(t.toPlainText())
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0473c2d191a8a3b4219734cc263c4ce412b5959a.png" alt="image" data-base62-sha1="DnVsf8RmPH9MD0I3eNlGtIBxh0" width="514" height="430"></p>
<p>Run this to switch back to plain text editing:</p>
<pre data-code-wrap="python"><code class="lang-python">t.setPlainText(t.markdown)
</code></pre>
<p>We could add a <code>Format</code> attribute to text node, which could be set to plain text, html, or markdown. Editing would probably always happen in plain text mode, but when you finished editing then rich text could be displayed.</p>
<p><a class="mention" href="/u/joachim">@joachim</a> would you be interested in giving a try and implement this?</p>

---

## Post #19 by @Sam_Horvath (2020-05-21 21:45 UTC)

<p>Only the Windows factory has been switched to 5.14.2.  The other factories are pending, but require more work (macOS factory needs an OS update, and we need to regenerate the docker images for Linux)</p>

---

## Post #20 by @joachim (2020-05-22 21:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>: I tested <code>QTextEdit</code> with markdown and it works very nice. It could be a nice feature. I suggest having a format selector in <code>qMRMLTextWidget</code> (plain, HTML, markdown) at the bottom. And the <code>QTextEdit</code> is only editable if plain format is selected, i.e. selecting markdown or HTML gives a read-only visual appearance. A <code>Format</code> attribute is nice then.</p>
<p>I would love to give this a try later, since I don’t have too much time right now. It is a nice exercise and opportunity for me to get into Slicer coding, however.</p>

---
