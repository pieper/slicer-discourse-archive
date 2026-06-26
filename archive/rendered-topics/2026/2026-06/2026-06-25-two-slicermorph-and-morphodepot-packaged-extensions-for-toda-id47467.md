---
topic_id: 47467
title: "Two SlicerMorph and MorphoDepot packaged extensions for todays Stable 5.12 build"
date: 2026-06-25
url: https://discourse.slicer.org/t/47467
last_bumped: 2026-06-25T19:14:04.067Z
---

# Two SlicerMorph and MorphoDepot packaged extensions for todays Stable 5.12 build

**Topic ID**: 47467
**Date**: 2026-06-25
**URL**: https://discourse.slicer.org/t/two-slicermorph-and-morphodepot-packaged-extensions-for-todays-stable-5-12-build/47467

---

## Post #1 by @muratmaga (2026-06-25 19:14 UTC)

<p>On a clean Slicer 5.12.0 (revision <strong>34621</strong>) Linux install, installing <strong>SlicerMorph</strong> or <strong>MorphoDepot</strong> via the Extensions Manager (<code>installExtensionFromServer</code>) fails with <em>“Failed to retrieve metadata for … extension”</em>. The other extensions install fine.</p>
<p><strong>Root cause.</strong> Both extension <em>items</em> on slicer-packages currently hold <strong>two build files</strong> for r34621 (a stale build + the current one). The Extensions Manager fetches <code>/api/v1/item/{id}/files</code> and <strong>explicitly rejects any item that does not have exactly one file</strong> — see <code>qSlicerExtensionsManagerModelPrivate::downloadExtensionByName</code> in <a href="https://github.com/Slicer/Slicer/blob/v5.12.0/Base/QTCore/qSlicerExtensionsManagerModel.cxx#L1576" rel="noopener nofollow ugc">Base/QTCore/qSlicerExtensionsManagerModel.cxx (v5.12.0)</a>:</p>
<pre><code class="lang-auto">// GET /api/v1/item/{item_id}/files
if      (results.isEmpty())     return nullptr;      // 0 files
else if (results.count() == 1)  { file_id = ...; }   // exactly 1 -&gt; OK
else                            return nullptr;      // &gt;1 file -&gt; "not expected", bail

</code></pre>
<p>so <code>count()==2</code> → <code>nullptr</code> → “Failed to retrieve metadata.”</p>
<p><strong>Reproduce (public read API):</strong></p>
<pre><code class="lang-auto">BASE=https://slicer-packages.kitware.com/api/v1
APP=5f4474d0e1d8c75dfc705482      # Slicer app id

# Manager resolves the extension item for r34621:
curl -s "$BASE/app/$APP/extension?baseName=SlicerMorph&amp;app_revision=34621&amp;os=linux&amp;arch=amd64&amp;limit=1" | jq -r '.[0]._id'
#   -&gt; 6a3c00dc3e1fb85a58476a8b

# ...then GETs its files and requires exactly one. This returns TWO:
curl -s "$BASE/item/6a3c00dc3e1fb85a58476a8b/files" | jq -r '.[] | "\(._id)  \(.name)  created=\(.created)"'
#   6a3c00dd3e1fb85a58476a92  34621-linux-amd64-SlicerMorph-gite870ab7-2026-06-17.tar.gz  created=2026-06-24T16:07:57Z   (stale)
#   6a3d17c23e1fb85a58482b87  34621-linux-amd64-SlicerMorph-gitfb97f10-2026-06-25.tar.gz  created=2026-06-25T11:57:54Z   (current)

# MorphoDepot has the same problem (item 6a3beaff3e1fb85a5847514a):
curl -s "$BASE/item/6a3beaff3e1fb85a5847514a/files" | jq -r '.[] | "\(._id)  \(.name)  created=\(.created)"'
#   6a3d02233e1fb85a584817c2  34621-linux-amd64-MorphoDepot-git0a72a7b-2026-06-25.tar.gz  created=2026-06-25T10:25:39Z   (current)
#   6a3beb013e1fb85a58475152  34621-linux-amd64-MorphoDepot-git5567e0d-2026-06-24.tar.gz  created=2026-06-24T14:34:40Z   (stale)
</code></pre>
<p>Can someone remove the stale older file from each item so each has exactly one (<code>count()==1</code>):</p>
<ul>
<li>SlicerMorph item <code>6a3c00dc3e1fb85a58476a8b</code> → delete file <code>6a3c00dd3e1fb85a58476a92</code> (<code>gite870ab7</code>, 2026-06-17)</li>
<li>MorphoDepot item <code>6a3beaff3e1fb85a5847514a</code> → delete file <code>6a3beb013e1fb85a58475152</code> (<code>git5567e0d</code>, 2026-06-24)</li>
</ul>

---
