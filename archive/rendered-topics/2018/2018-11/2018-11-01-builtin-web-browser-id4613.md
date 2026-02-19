---
topic_id: 4613
title: "Builtin Web Browser"
date: 2018-11-01
url: https://discourse.slicer.org/t/4613
---

# Builtin web browser

**Topic ID**: 4613
**Date**: 2018-11-01
**URL**: https://discourse.slicer.org/t/builtin-web-browser/4613

---

## Post #1 by @muratmaga (2018-11-01 17:34 UTC)

<p>I believe there is a web browser built into Slicer. Is it possible to invoke a URL from a python interactor and popup a window? I want to test if a user can interactively authenticate to a data repository we want to support.</p>

---

## Post #2 by @lassoan (2018-11-01 18:11 UTC)

<p>There is a built-in web browser, so that’s one option. It could be also interesting if you can authenticate using Python libraries (e.g., <a href="https://developers.google.com/api-client-library/python/guide/aaa_oauth">oauth2</a>). What kind of authentication that site uses?</p>

---

## Post #3 by @muratmaga (2018-11-01 18:17 UTC)

<p>To be perfectly honest I do not know what they are currently using. I believe, plan on changing to oauth2 and let users create access tokens to be used with API, but that’s a little ways from now. We also need to render some items from their webpage within Slicer (browse and search items, similar to datastore).</p>
<p>Can you point me to documentation about internal web browser?</p>

---

## Post #4 by @pieper (2018-11-01 18:20 UTC)

<p>In Slicer 4.10 you can do the following from python:</p>
<pre><code class="lang-auto">qt.QDesktopServices.openUrl(qt.QUrl('http://slicer.org'))
</code></pre>
<p>to open your desktop browser at an arbitrary URL, but it’s not connected back to Slicer so there’s no easy way to get the authorization token back from the browser for use in web requests (you could do some kind of cut-and-paste or other manual method).</p>
<p>There is also a built-in browser based on QWebEngine that is used in the ExtensionManager and DataStore.</p>
<pre><code class="lang-auto">w = slicer.qSlicerWebWidget()
w.webView().url = qt.QUrl('http://slicer.org')
w.show()
</code></pre>
<p>The python wrapping is not complete (can’t access javascript contents, such as the token, via python but should be able to via C++.</p>
<p>Search for the Qt docs on QtWebEngine fore more details about what you can do with it.</p>

---

## Post #5 by @muratmaga (2018-11-01 18:48 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>. I did manage to login through the built-in browser. I tried to download a file, and as far as I can tell it did. But any idea where it may have ended up? It couldn’t locate it in the slicer temp directory.</p>

---

## Post #6 by @pieper (2018-11-01 19:26 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="4613">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>But any idea where it may have ended up?</p>
</blockquote>
</aside>
<p>I’m not sure - Qt transitioned to a new web architecture and some things aren’t as easy to use as they used to be.  For example some classes are not exposed in PythonQt and that makes it a bit harder to test.  Hopefully it won’t be too much work to enable but I haven’t looked into the details.</p>
<p>My hope has been to make it pretty seamless to go between the built-in browser and the slicer/python world in order to facilitate the kinds of interactions you are describing, but the web infrastructure switch set that back a bit.  I think it’ll still be possible.</p>

---
