# Elastix fails to build

**Topic ID**: 11077
**Date**: 2020-04-11
**URL**: https://discourse.slicer.org/t/elastix-fails-to-build/11077

---

## Post #1 by @Alex_Vergara (2020-04-11 12:16 UTC)

<p>As seen here <a href="http://slicer.cdash.org/buildSummary.php?buildid=1880612" rel="noopener nofollow ugc">http://slicer.cdash.org/buildSummary.php?buildid=1880612</a></p>
<p>Elastix is failing to build.</p>
<p>I can follow the current errors up to 13/03/2020 build. I see nobody has reported this</p>

---

## Post #2 by @jamesobutler (2020-04-11 14:22 UTC)

<p>This would be because Slicer updated ITK from 5.1rc01 to 5.1rc03. It looks like <a href="https://github.com/lassoan/SlicerElastix" rel="nofollow noopener">SlicerElastix</a> had to be updated when going to 5.1rc01 and use a fork of Elastix because as of Jan 30th it hadn’t been updated to be compatible with that latest ITK. However it appears there has been many commits to <a href="https://github.com/SuperElastix/elastix" rel="nofollow noopener">Elastix</a> since then so I would guess it might be compatible with latest ITK now.</p>
<p>Can you try updating SlicerElastix to use the upstream Elastix at the latest commit and then building the extension to see if those changes work before issuing a PR to SlicerElastix?</p>

---

## Post #3 by @lassoan (2020-04-13 01:33 UTC)

<p>Thanks for reporting. I’ve pushed a fix, please reopen <a href="https://github.com/lassoan/SlicerElastix/issues/27">https://github.com/lassoan/SlicerElastix/issues/27</a> if you find that there are errors on the dashboard tomorrow.</p>

---

## Post #4 by @Alex_Vergara (2020-04-13 13:57 UTC)

<p>Still a lot of errors on build <a href="http://slicer.cdash.org/buildSummary.php?buildid=1882415" rel="nofollow noopener">http://slicer.cdash.org/buildSummary.php?buildid=1882415</a></p>

---

## Post #5 by @lassoan (2020-04-13 15:43 UTC)

<p>Thanks for letting me know. Build is fine in Windows and Linux; only the Mac build is problematic. I’ve attempted a fix, hopefully it’ll work. Please check again tomorrow.</p>

---
