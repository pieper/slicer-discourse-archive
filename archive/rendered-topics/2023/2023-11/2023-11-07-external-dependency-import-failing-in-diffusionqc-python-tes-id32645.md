# External dependency import failing in DiffusionQC Python test

**Topic ID**: 32645
**Date**: 2023-11-07
**URL**: https://discourse.slicer.org/t/external-dependency-import-failing-in-diffusionqc-python-test/32645

---

## Post #1 by @jhlegarreta (2023-11-07 16:55 UTC)

<p>Hi,<br>
I’ve noticed that the <code>DiffusionQC</code> extension module’s test has been failing for a while:<br>
<a href="https://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=3202379" class="inline-onebox" rel="noopener nofollow ugc">CDash</a></p>
<p>also mentioned in:<br>
<a href="https://github.com/pnlbwh/SlicerDiffusionQC/pull/47#issuecomment-1111096502" class="inline-onebox" rel="noopener nofollow ugc">Fix import errors by lassoan · Pull Request #47 · pnlbwh/SlicerDiffusionQC · GitHub</a></p>
<p>And this happens despite <code>plumbum</code> being specified in the <code>setup.py</code> in the <code>install_requires</code> dependencies:<br>
<a href="https://github.com/pnlbwh/SlicerDiffusionQC/blob/cc785145b301c8b8797099ec1527aceb4b90679a/diffusionqclib/setup.py#L16" rel="noopener nofollow ugc">https://github.com/pnlbwh/SlicerDiffusionQC/blob/cc785145b301c8b8797099ec1527aceb4b90679a/diffusionqclib/setup.py#L16</a></p>
<p>I’ve also seen that <a class="mention" href="/u/jcfr">@jcfr</a> did a PR a long time ago:<br>
<a href="https://github.com/pnlbwh/SlicerDiffusionQC/pulls" class="inline-onebox" rel="noopener nofollow ugc">Pull requests · pnlbwh/SlicerDiffusionQC · GitHub</a></p>
<p>I haven’t got merge rights, so I cannot do much about it. It’d probably address the config issues of the module, but the test issue is probably unrelated.</p>
<p>So concerning the test, is there something that the extension Python code is missing?</p>
<p>Thanks.</p>

---
