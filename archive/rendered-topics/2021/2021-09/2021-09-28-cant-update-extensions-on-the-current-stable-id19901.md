# Can't update extensions on the current stable

**Topic ID**: 19901
**Date**: 2021-09-28
**URL**: https://discourse.slicer.org/t/cant-update-extensions-on-the-current-stable/19901

---

## Post #1 by @muratmaga (2021-09-28 19:19 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>I am using the “check for updates” in the latest stable, which doesn’t find any changes (I don’t know the other extension I had, but there was one for SlicerMorph last night). Attached are warnings and a final error in the log.</p>
<p>FYI, I can install any “new” extension from the extension manager (e.g., just install Bone Reconstruction Planner) on this computer and the same stable version.</p>
<pre><code class="lang-auto">A cookie associated with a cross-site resource at http://www.nitrc.org/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032.
"Received response to query {9c5a549e-3afb-4ee0-a8fa-966df8ade5f2} with no associated request?"
"Received response to query {b042c777-fad1-43da-9468-78cb5cc1f46f} with no associated request?"
"update check for IntensitySegmenter complete: 'ace1890' available, 'ace1890' installed"
"Received response to query {6a373e30-d955-4c64-8550-3a4aeff4eee5} with no associated request?"
"update check for Autoscroll complete: 'dbfdb54' available, 'dbfdb54' installed"
"update check for BoneTextureExtension complete: '43f2f52' available, '43f2f52' installed"
"Received response to query {c20f8a7e-f65b-47ff-afdc-9a4b9a4cc1b5} with no associated request?"
"Received response to query {96b5c840-84b6-4c02-b42e-73079d6f6dd7} with no associated request?"
"Received response to query {506ed8d0-4710-41ff-8255-0bee80dc12c2} with no associated request?"
"Received response to query {c2ec7bff-7870-451c-b01a-60c407116b5a} with no associated request?"
"Received response to query {730c9573-0901-4e74-94e8-e9974862661c} with no associated request?"
"update check for SlicerMorph complete: 'f70c039' available, 'f70c039' installed"
"Received response to query {51ca5a1e-543c-487b-bef3-20ecf9666b70} with no associated request?"
Uncaught SyntaxError: missing ) after argument list
Uncaught SyntaxError: missing ) after argument list
Uncaught SyntaxError: missing ) after argument list
Uncaught SyntaxError: missing ) after argument list
</code></pre>

---

## Post #2 by @lassoan (2021-09-28 20:27 UTC)

<p>Probably this just has not been implemented and may not worth the effort for the next few weeks (the next stable version will use the new girder API). I would recommend to submit an issue to the issue tracker to ensure we discuss this before we cut the new stable release.</p>

---

## Post #3 by @muratmaga (2021-09-28 23:11 UTC)

<p>Here is the link to the GH issue</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5908">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5908" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5908" target="_blank" rel="noopener nofollow ugc">Extension updates not found in stable version</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-28" data-time="20:59:35" data-timezone="UTC">08:59PM - 28 Sep 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener nofollow ugc">
          <img alt="muratmaga" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As described in https://discourse.slicer.org/t/cant-update-extensions-on-the-cur<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rent-stable/19901

extension manager in the current stable does not find/install any updates for install extensions. If a new stable based on the new infrastructure will be out soon, then it is not very concerning. But it still needs to be checked.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
