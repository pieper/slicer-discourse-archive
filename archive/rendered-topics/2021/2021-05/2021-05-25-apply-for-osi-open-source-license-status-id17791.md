# Apply for OSI open source license status

**Topic ID**: 17791
**Date**: 2021-05-25
**URL**: https://discourse.slicer.org/t/apply-for-osi-open-source-license-status/17791

---

## Post #1 by @Christian_Kleineidam (2021-05-25 13:25 UTC)

<p>OSI is generally used as a registry for which licenses are real open source licenses. The 3D Slicer license currently isn’t listed with OSI. <a href="https://opensource.org/approval" class="inline-onebox" rel="noopener nofollow ugc">The License Review Process | Open Source Initiative</a> provides an easy way to register new licenses and get them into the registry.</p>

---

## Post #2 by @pieper (2021-05-25 19:26 UTC)

<p>Thanks for raising this.  You are right, it’s probably worth going through that process, since people do sometimes ask why the Slicer license is not in the registry.  When this has come up before the feeling was that the OSI discouraged people from using non-standard licenses so we thought it would be rejected and that applying was not worth the effort.  However the page you linked looks pretty reasonable and maybe they will now appreciate the reasons Slicer’s license includes a few protections that aren’t present in some simpler licenses while still being a very permissive open license.</p>

---

## Post #3 by @lassoan (2021-05-25 20:35 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> would you try to submit the Slicer License for approval? It seems that the review is free and you just need to send the license to a mailing list. I guess the Slicer License would be “Legacy Approval” submission type with “Non-reusable licenses” proliferation category.</p>

---

## Post #4 by @pieper (2021-05-25 21:00 UTC)

<p>Okay, makes sense.  Let me loop in Ron since he and I worked with the BWH lawyers to draft the license in the first place.  I agree it belongs in the “non-reusable” category since it is written with BWH hard-coded in the language and it’s not possible for someone to just drop it into their own project even if they like the provisions.</p>

---

## Post #5 by @pieper (2022-01-31 18:54 UTC)

<p>As a follow up, I engaged the OSI group on this topic and <a href="http://lists.opensource.org/pipermail/license-review_lists.opensource.org/2021-June/thread.html#5166">after some back and forth</a> we determined that the Slicer clauses requiring that user comply with local laws and regulations make the Slicer license incompatible with OSI, although it was not a unanimous decision.</p>
<p>When the license was written several people, including myself, determined it is proper not to encourage people to make illegal medical products.  Of course if they are willing to make illegal medical products they are probably also willing to violate the Slicer license, so in the end I consider it a moot point.</p>
<p>In the end we decided to provide more context about licensing considerations to the documentation:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5658/files">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5658/files" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5658" target="_blank" rel="noopener">DOC: Add text about licensing context</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>Slicer:doc-add-license-context</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-05-27" data-time="19:16:50" data-timezone="UTC">07:16PM - 27 May 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 26 additions and 1 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5658/files" target="_blank" rel="noopener">
          <span class="added">+26</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Per suggestion from @jcfr.</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
