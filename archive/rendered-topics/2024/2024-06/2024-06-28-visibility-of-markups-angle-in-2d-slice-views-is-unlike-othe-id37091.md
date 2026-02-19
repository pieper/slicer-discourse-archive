---
topic_id: 37091
title: "Visibility Of Markups Angle In 2D Slice Views Is Unlike Othe"
date: 2024-06-28
url: https://discourse.slicer.org/t/37091
---

# Visibility of markups angle in 2D slice views is unlike other markups

**Topic ID**: 37091
**Date**: 2024-06-28
**URL**: https://discourse.slicer.org/t/visibility-of-markups-angle-in-2d-slice-views-is-unlike-other-markups/37091

---

## Post #1 by @jamesobutler (2024-06-28 21:48 UTC)

<p>Why is that the Markups Angle lines can be seen across multiple slice offsets while other markup types such as Line is only seen in the slice offset drawn? I was confused when I was seeing the lines of the angle without the control points in a slice offset away from where I placed it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e54770d74f6f4bf9bb096ff5a2eee61c2d58b92b.jpeg" data-download-href="/uploads/short-url/wIioUWj6aV7TtHzSAV3BepNPqTp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54770d74f6f4bf9bb096ff5a2eee61c2d58b92b_2_690x370.jpeg" alt="image" data-base62-sha1="wIioUWj6aV7TtHzSAV3BepNPqTp" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54770d74f6f4bf9bb096ff5a2eee61c2d58b92b_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54770d74f6f4bf9bb096ff5a2eee61c2d58b92b_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e54770d74f6f4bf9bb096ff5a2eee61c2d58b92b_2_1380x740.jpeg 2x" data-dominant-color="797677"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1032 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then moving slice offset forward, the markup angle is still visible.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7582a3f09399e52f687e2233405209b5406a938f.jpeg" data-download-href="/uploads/short-url/gLxL6CoOX04hgbdwAT45iaIUMJF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7582a3f09399e52f687e2233405209b5406a938f_2_690x370.jpeg" alt="image" data-base62-sha1="gLxL6CoOX04hgbdwAT45iaIUMJF" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7582a3f09399e52f687e2233405209b5406a938f_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7582a3f09399e52f687e2233405209b5406a938f_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7582a3f09399e52f687e2233405209b5406a938f_2_1380x740.jpeg 2x" data-dominant-color="797777"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1032 96.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2024-07-02 12:41 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> This may be a question best for your expertise related to Markups display.</p>

---

## Post #3 by @Sunderlandkyl (2024-07-02 13:35 UTC)

<p>Thanks, I’ll take a look at it.</p>

---

## Post #4 by @Sunderlandkyl (2024-07-02 15:32 UTC)

<p>PR that makes angles follow the same behavior as line/curve markups:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7832">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7832" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7832" target="_blank" rel="noopener nofollow ugc">ENH: Hide angle markups when the line doesn't intersect with the slice</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>Sunderlandkyl:angle_out_of_plane_visibility</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-07-02" data-time="15:31:45" data-timezone="UTC">03:31PM - 02 Jul 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Sunderlandkyl" target="_blank" rel="noopener nofollow ugc">
            <img alt="Sunderlandkyl" src="https://avatars.githubusercontent.com/u/9222709?v=4" class="onebox-avatar-inline" width="20" height="20">
            Sunderlandkyl
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 8 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7832/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+8</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">For line/curve markup types, the lines are hidden whenever they don't intersect <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7832" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">with the current slice, however the current behavior for angle markups is that they continue to be visible even when they no longer intersect. This commit updates the behavior of angle lines to be consistent with that of the other markup types.

See discussion: https://discourse.slicer.org/t/visibility-of-markups-angle-in-2d-slice-views-is-unlike-other-markups/37091</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
