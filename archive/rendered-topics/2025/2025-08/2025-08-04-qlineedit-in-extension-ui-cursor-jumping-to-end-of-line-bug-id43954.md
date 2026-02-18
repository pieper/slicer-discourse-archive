# QLineEdit in extension UI: Cursor jumping to end of line (bug?)

**Topic ID**: 43954
**Date**: 2025-08-04
**URL**: https://discourse.slicer.org/t/qlineedit-in-extension-ui-cursor-jumping-to-end-of-line-bug/43954

---

## Post #1 by @shai-ikko (2025-08-04 12:50 UTC)

<p>Hi,</p>
<p>I’ve been writing some Slicer extensions using the Extension Wizard &amp; Qt Designer, and it’s been mostly working very well. But I’m seeing a funny behavior, which I think is a bug.</p>
<p>I have extensions which use simple text fields – defined as a <code>QLineEdit</code> using the Qt Designer, and connected to the parameter node using the <code>SlicerParameterName</code> dynamic property (on the widget), which is handled by the <code>@parameterNodeWrapper</code> decorator on the Parameter Node class. I’ve compared my extension’s setup code with one created fresh by the Wizard, and AFAICT I’m not doing anything special, and not dropping any important initialization.</p>
<p>But the text lines behave as described <a href="https://stackoverflow.com/questions/15801259/qlineedit-cursor-moves-to-end-after-textchanged-or-commitdata" rel="noopener nofollow ugc">here</a> – whenever a user types a character in the middle of the field, the cursor jumps to the end.</p>
<p>I suspect this is caused by not-careful-enough code in the GUI connection – it looks like the callback created for updating parameters from the GUI (in <code>parameterNodeWrapper.wrapper._makeGuiToParamCallback()</code> updates the parameter node, but then this updates the GUI back. I suppose this is useful in some cases. But if this is done for text fields, we probably need to restore the cursor position as described in the answers to the StackOverflow question cited above.</p>
<p>Have others also run into this?</p>
<p>[Edit: Related, of course, <a href="http://github.com/Slicer/Slicer/issues/7308" class="inline-onebox" rel="noopener nofollow ugc">Parameter node wrapper GUI connectors are missing for many widgets · Issue #7308 · Slicer/Slicer · GitHub</a> – but that lists <code>QLineEdit</code> as “supported”, which it mostly is]</p>

---

## Post #2 by @pieper (2025-08-04 14:28 UTC)

<p>Yes, probably the text is being set again as part of the update.  Saving and restoring the cursor position makes sense, or it could check if the value of the text is the same as what it’s trying to set and skip the update.  It would make sense to add this to the wrapper code.</p>

---

## Post #3 by @mau_igna_06 (2025-08-04 22:31 UTC)

<p>What about this signal?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://doc.qt.io/qt-6/qlineedit.html#editingFinished">
  <header class="source">
      <img src="https://d33sqmjvzgs8hq.cloudfront.net/wp-content/themes/oneqt/assets/images/favicon.ico.gzip" class="site-icon" alt="" width="" height="">

      <a href="https://doc.qt.io/qt-6/qlineedit.html#editingFinished" target="_blank" rel="noopener nofollow ugc">doc.qt.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://doc.qt.io/qt-6/qlineedit.html#editingFinished" target="_blank" rel="noopener nofollow ugc">QLineEdit Class | Qt Widgets | Qt 6.9.1</a></h3>

  <p>The QLineEdit widget is a one-line text editor.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>HIH</p>

---

## Post #4 by @shai-ikko (2025-08-05 13:52 UTC)

<p>I’ve been able to find some cases where it does work as intended, so there’s probably something a bit more involved going on. I will report more as I find out more.</p>

---

## Post #5 by @shai-ikko (2025-08-05 15:40 UTC)

<p>No, scratch that. Those other cases were in an extension-in-development which had a broken field, and that field broke the connection to the parameter – so the cursor wasn’t jumping because the parameter wasn’t updated.</p>
<p>I see I am able to fix the bug by changing, in class <code>QLineEditToStrConnector</code>,</p>
<pre><code class="lang-auto">    def write(self, value: str) -&gt; None:
        self._widget.text = value
</code></pre>
<p>to</p>
<pre><code class="lang-auto">    def write(self, value: str) -&gt; None:
        # Writing the text of a QLineEdit moves the cursor to the end
        # We tolerate that if the value is actually changing
        if value != self._widget.text:
            self._widget.text = value

</code></pre>
<p>(this is one of the options suggested by <a class="mention" href="/u/pieper">@pieper</a> IIUC)</p>
<p>I will post an issue and a PR for this. Thanks for your help!</p>

---

## Post #6 by @pieper (2025-08-05 15:59 UTC)

<p>Yes, that looks good <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @shai-ikko (2025-08-05 16:42 UTC)

<p>Just for closure, <a href="https://github.com/Slicer/Slicer/issues/8620" class="inline-onebox" rel="noopener nofollow ugc">GitHub · Where software is built</a> and <a href="https://github.com/Slicer/Slicer/pull/8621" class="inline-onebox" rel="noopener nofollow ugc">BUG: Avoid cursor jump on edit in extension LineEdit by shai-ikko · Pull Request #8621 · Slicer/Slicer · GitHub</a></p>
<p>Thanks again!</p>

---
