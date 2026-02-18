# Unable to download extensions from the extensions manager

**Topic ID**: 20618
**Date**: 2021-11-15
**URL**: https://discourse.slicer.org/t/unable-to-download-extensions-from-the-extensions-manager/20618

---

## Post #1 by @nforwood (2021-11-15 02:33 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.11.20210226<br>
Expected behavior: Download works<br>
Actual behavior: Get an error “Error retrieving extension metadata: 60ae226cae4540bf6a89da9d ({303b7c63-e615-43d7-9232-688ef5bec7c9}: 5: Operation canceled)”…</p>
<p>I can’t seem to download any extension from the extension manager. I just get the error above. I also can’t manually download the extensions from the website. I am in a corporate network but usually this hasn’t bean a problem for other applictions.</p>

---

## Post #2 by @lassoan (2021-11-15 21:57 UTC)

<p>The extension server was replaced and too aggressive corporate network/proxy are expected to cause more issues than before. You may find this discussion helpful:</p>
<aside class="quote" data-post="36" data-topic="19361">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-extension-manager-and-issues-with-corporate-certificates/19361/36">New extension manager and issues with corporate certificates</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can open the local machine certificate manager by hitting the windows key and typing certlm.msc. You can then find the self-signed certificate and disable all uses, restart the computer, and see if wget in python still works. 
You can also <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/README.md#debuggingtools-extension-for-3d-slicer">run wget step by step in a Python debugger</a> to see what certificates it is using and from where it gets them.
  </blockquote>
</aside>

<p>We have an other ongoing investigation of problems downloading behind netskope proxy. Is that what your corporate network uses, too?</p>

---

## Post #3 by @muratmaga (2021-11-15 23:22 UTC)

<p><a class="mention" href="/u/nforwood">@nforwood</a> we are behind a corporate firewall and use self-signed certificates. As indicated in the discussion linked, importing certificates into slicer.crt solves part of the equation. but even then we had a lot of issues (e.g., pip_install’s didn’t work because firewall ended up blocking). So you might have to work with your IT department to find a solution (exceptions, firewall rule changes for specific ITs etc) that will work with your particular situation.</p>

---
