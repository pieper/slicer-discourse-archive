---
topic_id: 8148
title: "Dicom Browser Layout"
date: 2019-08-23
url: https://discourse.slicer.org/t/8148
---

# DICOM Browser Layout

**Topic ID**: 8148
**Date**: 2019-08-23
**URL**: https://discourse.slicer.org/t/dicom-browser-layout/8148

---

## Post #1 by @Sunderlandkyl (2019-08-23 16:40 UTC)

<p>The latest nightly builds on all platforms include an updated DICOM browser that is  embedded within a layout, rather than as a popup window.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bb2c65c01b78aa2638b639211d2345b7e6dfd2e.png" data-download-href="/uploads/short-url/fmK6Z6feURlvNV7VLs4tUsjnlyC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bb2c65c01b78aa2638b639211d2345b7e6dfd2e_2_690x416.png" alt="image" data-base62-sha1="fmK6Z6feURlvNV7VLs4tUsjnlyC" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bb2c65c01b78aa2638b639211d2345b7e6dfd2e_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bb2c65c01b78aa2638b639211d2345b7e6dfd2e_2_1035x624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6bb2c65c01b78aa2638b639211d2345b7e6dfd2e_2_1380x832.png 2x" data-dominant-color="F0F5F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1160 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To show the dicom browser within a module:<br>
<code>slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutDicomBrowserView)</code></p>
<p>If anybody has any feedback or encounters any issues with the new DICOM browser layout, it would be great if you could post them here.</p>
<p>Thanks,<br>
Kyle</p>

---

## Post #2 by @jumbojing (2021-11-15 02:29 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a><br>
How to auto-hide browser window, when use <code> slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutDicomBrowserView)</code> in python.<br>
like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b08d10bc40189f5aa6a3dc5c4685e01e0baa1671.png" data-download-href="/uploads/short-url/pbQgun4gAj5cd742xxik8TZSGat.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b08d10bc40189f5aa6a3dc5c4685e01e0baa1671_2_690x323.png" alt="image" data-base62-sha1="pbQgun4gAj5cd742xxik8TZSGat" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b08d10bc40189f5aa6a3dc5c4685e01e0baa1671_2_690x323.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b08d10bc40189f5aa6a3dc5c4685e01e0baa1671_2_1035x484.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b08d10bc40189f5aa6a3dc5c4685e01e0baa1671.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1070×502 45.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e139a6ea05deb0992e360f1cbd91ff023fa3d17.png" alt="image" data-base62-sha1="20wGqFoyMdKkIgIrL7tUwysZu4f" width="173" height="80"></p>

---

## Post #3 by @jumbojing (2021-11-15 02:42 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <span class="mention">@pieperThanks</span> <a class="mention" href="/u/chir.set">@chir.set</a>@Sunderlandkyl</p>

---

## Post #4 by @Sunderlandkyl (2021-11-15 15:35 UTC)

<p>It should automatically switch back to the previous layout when something is loaded.<br>
Have you encountered any issues with this?</p>

---

## Post #5 by @jumbojing (2021-11-15 19:47 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a><br>
Yes, the previous layout has automatically switch, but the side bar  still couldn’t switch back…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e96150e9f370aa03bc95f8d9cac85f064c18a848.jpeg" data-download-href="/uploads/short-url/xizKsqWnyx798G0yl0GwMZxjJMs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e96150e9f370aa03bc95f8d9cac85f064c18a848_2_690x422.jpeg" alt="image" data-base62-sha1="xizKsqWnyx798G0yl0GwMZxjJMs" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e96150e9f370aa03bc95f8d9cac85f064c18a848_2_690x422.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e96150e9f370aa03bc95f8d9cac85f064c18a848_2_1035x633.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e96150e9f370aa03bc95f8d9cac85f064c18a848_2_1380x844.jpeg 2x" data-dominant-color="3F444A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1647×1009 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have to reopen my moudle to switch. I need not the side bar. I found the <strong>Auto-hide browser window</strong> checkbox in ‘DICOM database settings’  layout. How to “Auto-hide browser window” with python.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e139a6ea05deb0992e360f1cbd91ff023fa3d17.png" alt="image" data-base62-sha1="20wGqFoyMdKkIgIrL7tUwysZu4f" width="173" height="80"></p>

---

## Post #6 by @Sunderlandkyl (2021-11-15 20:05 UTC)

<p>You can use this function to change the browser persistence setting from Python:<br>
<code>slicer.modules.dicom.widgetRepresentation().self().browserWidget.setBrowserPersistence(True)</code></p>

---

## Post #7 by @jumbojing (2021-11-15 20:32 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="6" data-topic="8148">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>slicer.modules.dicom.widgetRepresentation().self().browserWidget.setBrowserPersistence(True)</p>
</blockquote>
</aside>
<pre><code class="lang-auto">slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutDicomBrowserView)
slicer.modules.dicom.widgetRepresentation().self().browserWidget.setBrowserPersistence(False)
</code></pre>
<p>I use above code, but open the Slicer, the first time “load DICOM”, the sidebar appears, and then “load DICOM”, the sidebar will not appear…Why?</p>

---

## Post #8 by @jumbojing (2021-11-15 21:00 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/602375f7aeef86ce7dc1cfe23d6b5b75b42f9305.gif" alt="ScreenFlow" data-base62-sha1="dItOjMRNnR4Gw2nPXUwy1yNpkH3" width="420" height="298" class="animated"></p>
<p>Open the Slicer, the first time “load DICOM”, the sidebar appears, and then “load DICOM”, the sidebar will not appear…</p>
<p>打开Slicer,第一次“load DICOM”, 侧边栏出现, 此后再“load DICOM”,侧边栏就不会出现了…</p>

---

## Post #10 by @Sunderlandkyl (2021-11-15 21:21 UTC)

<p>Using a freshly started Slicer, running the following code in the python interactor does not cause the DICOM module to appear in the sidebar (tested on Windows &amp; Linux):</p>
<pre><code class="lang-auto">slicer.modules.dicom.widgetRepresentation().self()
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutDicomBrowserView)
slicer.modules.dicom.widgetRepresentation().self().browserWidget.setBrowserPersistence(False)
</code></pre>
<p>Can you provide an example that can be run in the Python interactor that will cause the issue?</p>
<p>Otherwise, you may be able to debug the issue by placing a breakpoint in slicer.util.selectModule() and check the call stack to see where the module is changed.</p>

---

## Post #11 by @jumbojing (2021-11-15 21:47 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a><br>
Thinks, my code use <code>slicer.util.selectModule("DICOM")</code>, I delete it.</p>
<pre><code class="lang-auto">  def showDICOMBrowser(self):
    if slicer.modules.DICOMInstance.browserWidget is None:
      # slicer.util.selectModule('DICOM')
      slicer.util.selectModule('PedicleTrianglePlaner')
    # Make the DICOM browser disappear after loading data
    slicer.modules.dicom.widgetRepresentation().self()
    slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutDicomBrowserView)
    slicer.modules.dicom.widgetRepresentation().self().browserWidget.setBrowserPersistence(False)
</code></pre>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Problem solved, thank you, teacher!<br>
问题解决,谢谢老师</p>

---
