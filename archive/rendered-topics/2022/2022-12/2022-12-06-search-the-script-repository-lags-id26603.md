# Search the script repository lags

**Topic ID**: 26603
**Date**: 2022-12-06
**URL**: https://discourse.slicer.org/t/search-the-script-repository-lags/26603

---

## Post #1 by @rbumm (2022-12-06 12:00 UTC)

<p>Pressing “CTRL + F” on the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">3D Slicer script repository page</a> creates a small, noticeable and somewhat disturbing delay until</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01907d902b540d2247ab37d38d71766a15076559.png" alt="image" data-base62-sha1="dQ2UhdK616cskVBnpq8c2pQKNj" width="349" height="90"></p>
<p>appears. Could we make this show up faster or have a search box on that page?</p>

---

## Post #2 by @rbumm (2022-12-06 13:09 UTC)

<p><a href="https://readthedocs-sphinx-search.readthedocs.io/en/latest/">Sphinx search</a> could be interesting.</p>

---

## Post #3 by @lassoan (2022-12-06 15:24 UTC)

<p>We keep all the code snippets in one page to allow easy search among all, but of course it makes the page large. It is currently about 2.5MB, which may take 10-15 seconds to fully load. You may see some content starting to show up in your browser but you may need to wait for a full download for the find feature to start to work.</p>
<p>If you experience something vastly different timing then you can open developer tools (hit F12) and see details on the Network or Performance tabs.</p>

---
