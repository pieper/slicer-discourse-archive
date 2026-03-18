---
topic_id: 46478
title: "Extension Server Is Down"
date: 2026-03-17
url: https://discourse.slicer.org/t/46478
---

# Extension server is down

**Topic ID**: 46478
**Date**: 2026-03-17
**URL**: https://discourse.slicer.org/t/extension-server-is-down/46478

---

## Post #1 by @IVarha (2026-03-17 09:21 UTC)

<p>Qt] Update extension information from server failed: timed out while waiting for server response from <a href="https://slicer-packages.kitware.com/api/v1/app/5f4474d0e1d8c75dfc705482/extension" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/app/5f4474d0e1d8c75dfc705482/extension</a></p>
<p>[Qt] “<a href="https://extensions.slicer.org/catalog/All/34045/win" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/34045/win</a>” 1 “Uncaught ReferenceError: app is not defined”</p>
<p>[Qt] Uncaught ReferenceError: app is not defined</p>
<p>[Qt] “<a href="https://extensions.slicer.org/catalog/All/34045/win" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/34045/win</a>” 1 “Uncaught ReferenceError: app is not defined”</p>
<p>[Qt] Uncaught ReferenceError: app is not defined</p>
<p>[Qt] Failed to download extension metadata from server</p>
<p>[Qt] Update extension information from server failed: timed out while waiting for server response from <a href="https://slicer-packages.kitware.com/api/v1/app/5f4474d0e1d8c75dfc705482/extension" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/app/5f4474d0e1d8c75dfc705482/extension</a></p>
<p>[Qt] “<a href="https://extensions.slicer.org/catalog/All/34045/win" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/34045/win</a>” 1 “Uncaught ReferenceError: app is not defined”</p>
<p>[Qt] Uncaught ReferenceError: app is not defined</p>
<p>[Qt] “<a href="https://extensions.slicer.org/catalog/All/34045/win" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/34045/win</a>” 1 “Uncaught ReferenceError: app is not defined”</p>

---

## Post #2 by @cpinter (2026-03-17 10:19 UTC)

<p>I just downloaded an extension package from the server. It seems up to me</p>

---

## Post #3 by @J_R (2026-03-17 10:24 UTC)

<p>Also having issues accessing the extension server.</p>
<p>“Site not found<br>
Looks like you followed a broken link or entered a URL that doesn’t exist on Netlify.</p>
<p>If this is your site, and you weren’t expecting a 404 for this path, please visit Netlify’s “page not found” support guide for troubleshooting tips.</p>
<p>Netlify Internal ID: 01KKXN5NJSNCYFXJDNQEYSNQKM”</p>
<p>Updating existing extensions work but not searching or installing new ones.</p>

---

## Post #4 by @Lesly_Perlaza (2026-03-17 10:54 UTC)

<p>I also have the same issue.</p>

---

## Post #5 by @jamesobutler (2026-03-17 11:20 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/ebrahim">@ebrahim</a> will need to check the Netlify site configuration. Related repo is;</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/KitwareMedical/slicer-extensions-webapp">
  <header class="source">

      <a href="https://github.com/KitwareMedical/slicer-extensions-webapp" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/cf114e2a39c38f1b72f2485bfd53aec2/KitwareMedical/slicer-extensions-webapp" class="thumbnail">

  <h3><a href="https://github.com/KitwareMedical/slicer-extensions-webapp" target="_blank" rel="noopener nofollow ugc">GitHub - KitwareMedical/slicer-extensions-webapp: Source code of the site allowing to browse and...</a></h3>

    <p><span class="github-repo-description">Source code of the site allowing to browse and download Slicer extensions. This site is published at extensions.slicer.org and maintained by @Kitware on behalf of the 3D Slicer community.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Anupam_Singh (2026-03-17 13:00 UTC)

<p>I’m also facing the same issue.</p>
<h1><a name="p-132639-site-not-found-1" class="anchor" href="#p-132639-site-not-found-1" aria-label="Heading link"></a>Site not found</h1>
<p>Looks like you followed a broken link or entered a URL that doesn’t exist on Netlify.</p>
<hr>
<p>If this is your site, and you weren’t expecting a 404 for this path, please visit Netlify’s <strong><a href="https://answers.netlify.com/t/support-guide-i-ve-deployed-my-site-but-i-still-see-page-not-found/125?utm_source=404page&amp;utm_campaign=community_tracking" rel="noopener nofollow ugc">“page not found” support guide</a></strong> for troubleshooting tips.</p>
<p>Netlify Internal ID: <code>01KKXY5ANPTTH1JY26YAZQ1C81</code></p>

---

## Post #7 by @Matteboo (2026-03-17 13:04 UTC)

<p>I’m getting the same issue too.</p>
<p>Site not found<br>
Looks like you followed a broken link or entered a URL that doesn’t exist on Netlify.</p>
<p>If this is your site, and you weren’t expecting a 404 for this path, please visit Netlify’s “page not found” support guide for troubleshooting tips.</p>
<p>Netlify Internal ID: 01KKXY91PZG2PV48F5ADTAH9DY</p>

---

## Post #8 by @Sam_Horvath (2026-03-17 14:17 UTC)

<p>Workaround:</p>
<p>Download 5.10.0 extensions here: <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/69120522ac7b1c95e7937500" class="inline-onebox">SPKC</a></p>
<p>Download Latest nightly extensions here: <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/69b8e7f70716b743fc035a80" class="inline-onebox">SPKC</a></p>

---

## Post #9 by @Sam_Horvath (2026-03-17 14:22 UTC)

<p>The site should now be back up ( for now.  It is unclear whether this was an issue on Netlify or our side)</p>

---

## Post #10 by @jcfr (2026-03-17 14:51 UTC)

<p>Following up: this has now been addressed. As <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> mentioned, it is still unclear whether this was a temporary glitch or something else.</p>
<hr>
<p>This also provided an opportunity to review the list of projects whose deployment we manage through Netlify.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Project</th>
<th>Preview / Production</th>
<th>Website sources &amp; infrastructure docs</th>
</tr>
</thead>
<tbody>
<tr>
<td>Extensions</td>
<td><a href="https://extensions.slicer.org">https://extensions.slicer.org</a></td>
<td><a href="https://github.com/KitwareMedical/slicer-extensions-webapp">https://github.com/KitwareMedical/slicer-extensions-webapp</a></td>
</tr>
</tbody>
</table>
</div><hr>
<p>The other Slicer sites we deploy with Netlify are primarily used to preview rendering changes in the context of GitHub pull requests. The table below summarizes them:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Project</th>
<th>Preview</th>
<th>Production</th>
<th>Website sources &amp; infrastructure docs</th>
</tr>
</thead>
<tbody>
<tr>
<td>Project Week</td>
<td><a href="https://projectweek-na-mic-org-preview.netlify.app">https://projectweek-na-mic-org-preview.netlify.app</a></td>
<td><a href="https://projectweek.na-mic.org/">https://projectweek.na-mic.org/</a> (GitHub Pages)</td>
<td><a href="https://github.com/NA-MIC/ProjectWeek">https://github.com/NA-MIC/ProjectWeek</a></td>
</tr>
<tr>
<td>Slicer website</td>
<td><a href="https://slicer-org.netlify.app">https://slicer-org.netlify.app</a></td>
<td><a href="https://slicer.org">https://slicer.org</a> (Kitware-hosted)</td>
<td><a href="https://github.com/Slicer/slicer.org#infrastructure">Infrastructure docs</a></td>
</tr>
<tr>
<td>Training</td>
<td><a href="https://training-slicer-org.netlify.app/">https://training-slicer-org.netlify.app/</a></td>
<td><a href="https://training.slicer.org/">https://training.slicer.org/</a> (GitHub Pages)</td>
<td><a href="https://github.com/Slicer/training.slicer.org">https://github.com/Slicer/training.slicer.org</a></td>
</tr>
<tr>
<td>Autoscoper</td>
<td><a href="https://autoscoperm-slicer-org-preview.netlify.app">https://autoscoperm-slicer-org-preview.netlify.app</a></td>
<td><a href="https://autoscoperm.slicer.org/">https://autoscoperm.slicer.org/</a> (GitHub Pages)</td>
<td><a href="https://github.com/BrownBiomechanics/autoscoperm.slicer.org">https://github.com/BrownBiomechanics/autoscoperm.slicer.org</a></td>
</tr>
</tbody>
</table>
</div><h3><a name="p-132650-suggested-next-steps-1" class="anchor" href="#p-132650-suggested-next-steps-1" aria-label="Heading link"></a>Suggested Next Steps</h3>
<p>Considering that the Netlify hosting is currently associated with my personal Netlify account  (starter legacy plan), I suggest to request official support from Netlify through <a href="https://www.netlify.com/legal/open-source-policy" class="inline-onebox">Open Source Plan Policy | Netlify</a>.</p>
<p>This way we will be able to create a org/team and allow multiple admin.</p>

---
