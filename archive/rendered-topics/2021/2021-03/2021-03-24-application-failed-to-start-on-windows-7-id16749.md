# Application failed to start on Windows 7

**Topic ID**: 16749
**Date**: 2021-03-24
**URL**: https://discourse.slicer.org/t/application-failed-to-start-on-windows-7/16749

---

## Post #1 by @gabba78 (2021-03-24 10:59 UTC)

<p>Hi, I get 0xc000007b error on Windows 7 machines.<br>
Apparently something is wrong with DirectX</p>

---

## Post #2 by @lassoan (2021-03-24 13:34 UTC)

<p>Windows 7 is not supported (Microsoft dropped support for it long time ago). We have not made any breaking changes intentionally, but we don’t test impact of changes on these old systems. It is not very likely that you can get help from the community to troubleshoot this, so if running Slicer on Windows7 is a priority for you and you cannot resolve the problem yourself then you may contract <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#commercial-partners">commercial partners</a> to investigate the issue.</p>
<p>I would recommend to upgrade the operating system on your computer (and if you have a computer older than 5 years then the hardware as well). If you cannot upgrade immediately then you may use Slicer on a hosted cloud computer (such as this <a href="https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master?filepath=SlicerWeb.ipynb">free 3D Slicer hosting by Binder</a>).</p>

---

## Post #3 by @gabba78 (2021-03-24 17:29 UTC)

<p>Thanks Andras, luckily is just one workstation left with Win7 so I can easily work on another one.<br>
If I manage to fix it by myself I will post it here asap.</p>

---
