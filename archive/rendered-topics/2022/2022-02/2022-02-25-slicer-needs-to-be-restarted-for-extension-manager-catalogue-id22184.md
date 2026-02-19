---
topic_id: 22184
title: "Slicer Needs To Be Restarted For Extension Manager Catalogue"
date: 2022-02-25
url: https://discourse.slicer.org/t/22184
---

# Slicer needs to be restarted for extension manager catalogue to be updated

**Topic ID**: 22184
**Date**: 2022-02-25
**URL**: https://discourse.slicer.org/t/slicer-needs-to-be-restarted-for-extension-manager-catalogue-to-be-updated/22184

---

## Post #1 by @muratmaga (2022-02-25 17:54 UTC)

<p>I am not sure if it is a big deal, but there is corner case. Today, I was tying to install a new extension on today’s preview on linux. It showed only 20 extension. I thought maybe the extensions are still building, and I waited a while search my extension. It still showed 20. Only after I restarted the slicer and ran the extension manager newly build extensions showed up in the manager.</p>
<p>Again, it is probably a corner case, but if it is possible to it would be nice to have a mechanism to force update the catalog from the manager.</p>

---

## Post #2 by @jamesobutler (2022-02-25 20:06 UTC)

<p>The latest preview was restarted around 8am EST following the finalization of a <a href="https://github.com/Slicer/Slicer/pull/5978" rel="noopener nofollow ugc">VTK upgrade</a>. So that explains why you at least observed the issue of not all extensions being available compared to normal during your work day in the PST time zone.</p>
<p>The Extensions Manager contains a web browser so it is showing a static page that doesn’t auto-refresh. The “Search…” field I believe is just filtering the static page and not making a new query. If you right-click on the webpage area there is an option available to refresh the page which I believe should’ve provided you the same force refresh as you did by closing Slicer, reopening Slicer and opening the Extensions Manager again. Just closing the Extensions Manager closes just the Window so reopening it is not making a new query. It locally caches all the metadata to improve performance when reopening the Extensions Manager window (re <a href="https://github.com/Slicer/Slicer/commit/bae8472f4d5b3ac6ee51ffd54731747972dbaf07" class="inline-onebox" rel="noopener nofollow ugc">ENH: Improve extension manager startup time and progress reporting · Slicer/Slicer@bae8472 · GitHub</a>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21110acc9bed629ce45e96ca392e25ae5a98149d.jpeg" data-download-href="/uploads/short-url/4IwgGWGV2aQzdHVEqGGRXavUZuR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21110acc9bed629ce45e96ca392e25ae5a98149d_2_690x365.jpeg" alt="image" data-base62-sha1="4IwgGWGV2aQzdHVEqGGRXavUZuR" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21110acc9bed629ce45e96ca392e25ae5a98149d_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21110acc9bed629ce45e96ca392e25ae5a98149d_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21110acc9bed629ce45e96ca392e25ae5a98149d_2_1380x730.jpeg 2x" data-dominant-color="E1E1E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1016 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
