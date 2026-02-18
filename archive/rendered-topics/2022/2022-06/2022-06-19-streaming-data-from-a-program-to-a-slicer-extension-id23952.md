# Streaming data from a program to a Slicer extension

**Topic ID**: 23952
**Date**: 2022-06-19
**URL**: https://discourse.slicer.org/t/streaming-data-from-a-program-to-a-slicer-extension/23952

---

## Post #1 by @koeglfryderyk (2022-06-19 23:05 UTC)

<p>I have a Python program that detects hand coordinates in a video stream.</p>
<p>I’m trying to send those coordinates continuously to my Slicer Python extension so I can display the hand in Slicer.</p>
<p>I think I’m half-way there. I can update the hand model in Slicer by repeatedly pressing a button. This is what I currently have:</p>
<ol>
<li>The python program continuously sends data using <code>from multiprocessing.connection import Client</code>, it looks more or less like this:<pre><code class="lang-auto">with Client(('localhost', 5038)) as c:
    msg = np.reshape(all_fings_world[:, 0:3], (63, 1)).tobytes()
    c.send(msg)
</code></pre>
</li>
<li>In Slicer, in my extension I created a button that when clicked executes code that looks more or less like this:<pre><code class="lang-auto">try:
    self.serv = Listener(('', 5038))
    client = self.serv.accept()
    self.message = client.recv()
    self.update_hand()
except Exception as e:
    print(e)
</code></pre>
</li>
</ol>
<p>What I’m missing is to not have to keep clicking this button to update the hand in Slicer. Is there a way to make Slicer execute some code in a loop in the ‘background’ so that Slicer can still be used? I tried creating a thread to run this code, but this didn’t do anything. And just putting everything in a <code>while True</code> freezes Slicer.</p>

---

## Post #2 by @errollgarner (2022-06-20 01:02 UTC)

<p>You can use OpenIGTLink to send and receive the points:<br>
In your python program, you can use the python implementation of OpenIGTLink (<a href="https://github.com/lassoan/pyigtl" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/pyigtl: Python implementation of OpenIGTLink</a>) to send and on the Slicer side you can use the OpenIGTLinkIF module to receive the data.<br>
OpenIGTLink natively supports streaming points. You can find the protocol specifications here: <a href="https://github.com/openigtlink/OpenIGTLink/blob/release-3.0/Documents/Protocol/point.md" class="inline-onebox" rel="noopener nofollow ugc">OpenIGTLink/point.md at release-3.0 · openigtlink/OpenIGTLink · GitHub</a></p>

---

## Post #3 by @pieper (2022-06-20 19:56 UTC)

<p>OpenIGTLink is a good option.  Another option would be to use the new <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html?highlight=webserver#data-access">WebServer</a> to control the scene.  It is also integrated in the Slicer event loop so it handles updates asynchronously.</p>
<p>Or if you want to stick with something lower level like you are currently doing you could use a <code>QSocketNotifier</code> like is done <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/WebServer/WebServer.py#L487">in the WebServer code</a> so that you get a Qt signal when the socket has data ready to read.</p>

---

## Post #4 by @muratmaga (2022-06-21 01:55 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="23952">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>ould be to use the new <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html?highlight=webserver#data-access">WebServer</a> to control the scene</p>
</blockquote>
</aside>
<p>Is this in latest stable? I am not seeing a module called webserver.</p>

---

## Post #5 by @jamesobutler (2022-06-21 03:27 UTC)

<p>WebServer was integrated into Slicer on May 11th or about a week after the Slicer 5.0.2 release. Therefore it is only available in Slicer Preview builds since then.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/bdc1ee03893e957ba360a5988e4ed93cc275637a">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/bdc1ee03893e957ba360a5988e4ed93cc275637a" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/bdc1ee03893e957ba360a5988e4ed93cc275637a" target="_blank" rel="noopener nofollow ugc">ENH: add WebServer module (#5999)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-05-12" data-time="01:57:44" data-timezone="UTC">01:57AM - 12 May 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener nofollow ugc">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="changed 19 files with 3151 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/bdc1ee03893e957ba360a5988e4ed93cc275637a" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+3151</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">* ENH: add WebServer module

Code imported from Steve Pieper's developments.
<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/bdc1ee03893e957ba360a5988e4ed93cc275637a" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">
https://github.com/pieper/SlicerWeb

* DOC: add WebServer documentation page

* DOC: add note about web server access

* ENH: Improve WebServer module

- Moved out request handlers to separate files.
- Allow registration of custom request handlers.
- Iterate through registered request handlers and let that one process the request that returned the highest confidence.
- Save default handler and logging options in application settings.
- Start/stop the server when a start/stop button is pressed (not start when opening the WebServer module GUI).
- Updated Slicer icon.
- Updated module icon (API icon from Google Material Icon Set)
- Added `sampleData` command to allow easy testing and demoing of the API
- Added `gui` command to switch between full application/viewers only, switch viewer layout
- Added `screenshot` command to get screenshot of the application main window

* DOC: Update webserver.md

* ENH: web server fixes

* add entry on demo page to reset view to four up with controls
* change "got it" messages to more meaningful feedback
* add extra tooltip hints on usage
* fix logic of local connection button

* DOC: add web server security suggestion

* STYLE: fix codespell findings

https://github.com/Slicer/Slicer/actions/runs/2254569488

* ENH: add exception handler for web requests

This puts the stack trace in the log and prevents
any bad request handlers from leaving the network connection
dangling.

* BUG: fix dicomweb in Web Server module

A newer version of pydicom is required to fix a bug
in json serialization of a pydicom multivalue class.

Also fix a warning from bad uri syntax.

* BUG: fix DICOMweb endpoint for OHIF

* Implements study level query and metadata.
* Adds offset and limits to study listing
* Adds documentation on using with OHIF

Co-authored-by: Andras Lasso &lt;lasso@queensu.ca&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
