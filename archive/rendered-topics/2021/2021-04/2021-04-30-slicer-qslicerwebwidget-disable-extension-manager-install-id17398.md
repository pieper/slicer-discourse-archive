---
topic_id: 17398
title: "Slicer Qslicerwebwidget Disable Extension Manager Install"
date: 2021-04-30
url: https://discourse.slicer.org/t/17398
---

# slicer.qSlicerWebWidget() disable extension manager install

**Topic ID**: 17398
**Date**: 2021-04-30
**URL**: https://discourse.slicer.org/t/slicer-qslicerwebwidget-disable-extension-manager-install/17398

---

## Post #1 by @fbordignon (2021-04-30 18:16 UTC)

<p>Hello everyone, if I instantiate a webwidget before launching the extensions manager, I cannot install extensions anymore. Steps to reproduce.</p>
<ol>
<li>Python console:</li>
</ol>
<blockquote>
<p>slicer.qSlicerWebWidget()</p>
</blockquote>
<ol start="2">
<li>Open the extension manager for the <strong>first time</strong></li>
<li>The extensions buttons only show the Download option.</li>
</ol>

---

## Post #2 by @lassoan (2021-05-07 14:02 UTC)

<p>Thanks for reporting. We have encountered this issue before but <a href="https://github.com/Slicer/Slicer/issues/4602">thought it was due to the DataStore module</a>, so it did not get much attention.</p>
<p>I’ve submitted a new bug report for this to ensure it has more visibility:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5632" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5632" target="_blank" rel="noopener">Instantiating a slicer.qSlicerWebWidget() breaks extensions manager</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-05-07" data-time="14:00:20" data-timezone="UTC">02:00PM - 07 May 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">if I instantiate a webwidget before launching the extensions manager, I cannot i<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nstall extensions anymore. Steps to reproduce.

Python console:
```python
slicer.qSlicerWebWidget()
```

Open the extension manager for the first time
The extensions buttons only show the Download option.

(reported on discourse.slicer.org: https://discourse.slicer.org/t/slicer-qslicerwebwidget-disable-extension-manager-install/17398)

This issue has been first reported in https://github.com/Slicer/Slicer/issues/4602. It was thought to be a side effect of the DataStore module initialization, but as it turns out, the problem is at lower level.

## Steps to reproduce

- Start Slicer
- instantiate a web widget by `slicer.qSlicerWebWidget()`
- open extensions manager =&gt; "Download" buttons are displayed instead of "Install"

![image](https://user-images.githubusercontent.com/307929/117460816-e8856980-af1a-11eb-9233-fbe1b6e38765.png)

## Environment
- Slicer version: Slicer-4.11.20210226
- Operating system: Windows</span></p>
  </div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/pieper">@pieper</a> I think you have worked on this part of the code in the past, could you have a look at?</p>

---

## Post #3 by @pieper (2021-05-07 14:09 UTC)

<p>Let’s see what happens with the new extension manager implementation.  If it’s still an issue we can dig in deeper.  I added a comment in the github issue about a possible cause.</p>

---
