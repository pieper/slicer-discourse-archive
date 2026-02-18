# 3D slicer not loading images

**Topic ID**: 45211
**Date**: 2025-11-24
**URL**: https://discourse.slicer.org/t/3d-slicer-not-loading-images/45211

---

## Post #1 by @amberlgilbert (2025-11-24 15:30 UTC)

<p>Previously, when loading images this was working, however now the images are not opening and loading, the error displayed is shown below:</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>
<p>[Qt] SQL failed:</p>
<p>[Qt] SELECT Filename FROM Images WHERE SeriesInstanceUID=?</p>
<p>[Qt] Error:</p>
<p>[Qt] database disk image is malformed Unable to fetch row</p>

---

## Post #2 by @cpinter (2025-11-24 15:33 UTC)

<p>Maybe the contents of the database have been moved or deleted? At this point I’d create a new database and import the data again.</p>

---
