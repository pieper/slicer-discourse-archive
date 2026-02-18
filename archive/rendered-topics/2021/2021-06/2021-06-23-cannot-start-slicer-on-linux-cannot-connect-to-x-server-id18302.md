# Cannot start Slicer on LInux - cannot connect to X server

**Topic ID**: 18302
**Date**: 2021-06-23
**URL**: https://discourse.slicer.org/t/cannot-start-slicer-on-linux-cannot-connect-to-x-server/18302

---

## Post #1 by @Fabio_Geraci (2021-06-23 14:23 UTC)

<p>this is my output</p>
<pre><code class="lang-auto">~/Slicer-4.11.20210226-linux-amd64/Slicer
Slicer: cannot connect to X server 192.168.0.1
fec0:0:0:ffff::1
fec0:0:0:ffff::2:0
</code></pre>

---

## Post #2 by @Fabio_Geraci (2021-06-23 19:44 UTC)

<p>I am running a jupyter notebook, where slicer is invoked to show images, the very first tutorial. In my bashrc i have</p>
<pre><code class="lang-auto">#
export SITK_SHOW_COMMAND=${HOME}/Slicer-4.11.20210226-linux-amd64/Slicer
export PATH="$PATH:${HOME}/Slicer-4.11.20200930-linux-amd64"
# 
#export DISPLAY=localhost:1.0
#
</code></pre>
<p>an i run jupyter notebook from MobaXterm, with the following error:</p>
<pre><code class="lang-auto">QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-fabiog'
Switch to module:  "Welcome"
The X11 connection broke: I/O error (code 1)
Slicer: Fatal IO error: client killed
XIO:  fatal IO error 0 (Success) on X server "localhost:10.0"
      after 1361 requests (1361 known processed) with 0 events remaining.
free(): invalid pointer
</code></pre>

---

## Post #3 by @lassoan (2021-06-25 02:05 UTC)

<p>The question was already posted here and turned out to be a configuration error on the user’s computer:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5707">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5707" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5707" target="_blank" rel="noopener">3D Slicer fails to open on MobaXterm</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-06-24" data-time="08:53:26" data-timezone="UTC">08:53AM - 24 Jun 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-06-24" data-time="17:35:48" data-timezone="UTC">05:35PM - 24 Jun 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/fabiogeraci" target="_blank" rel="noopener">
          <img alt="fabiogeraci" src="https://avatars.githubusercontent.com/u/19588735?v=4" class="onebox-avatar-inline" width="20" height="20">
          fabiogeraci
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">status:question</span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Good Morning,

My setup: Windows 10 - Ubuntu WSL1 (Welcome to Ubuntu 20.04.2 L<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">TS (GNU/Linux 4.4.0-19041-Microsoft x86_64)) - MobaXterm

In bashrc I have the following lines:
```
#
export SITK_SHOW_COMMAND=${HOME}/Slicer-4.11.20210226-linux-amd64/Slicer
export PATH="$PATH:${HOME}/Slicer-4.11.20200930-linux-amd64"
#
```
Issue: I am trying to launch 3D Slicer from MobaXterm, using:
`~/Slicer-4.11.20210226-linux-amd64/Slicer`
It seems to be working but then I get the following error:
```
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-username'
Switch to module:  "Welcome"
Slicer: Fatal IO error: client killed
The X11 connection broke: I/O error (code 1)
XIO:  fatal IO error 0 (Success) on X server "localhost:10.0"
      after 1362 requests (1362 known processed) with 0 events remaining.
free(): invalid size
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
