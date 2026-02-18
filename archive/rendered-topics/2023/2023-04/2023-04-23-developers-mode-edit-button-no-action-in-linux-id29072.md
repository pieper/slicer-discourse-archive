# Developer's mode edit button no action in Linux

**Topic ID**: 29072
**Date**: 2023-04-23
**URL**: https://discourse.slicer.org/t/developers-mode-edit-button-no-action-in-linux/29072

---

## Post #1 by @muratmaga (2023-04-23 20:38 UTC)

<p>After enabling the developer mode, I expect the edit button would open the source code of the active module in a text editor.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb2df59cc3afbfd5622b9da9c7986f18f827d178.png" data-download-href="/uploads/short-url/zQ2jnZuqpkQoKuc5vJYwnBjNT7y.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2df59cc3afbfd5622b9da9c7986f18f827d178_2_690x88.png" alt="image" data-base62-sha1="zQ2jnZuqpkQoKuc5vJYwnBjNT7y" width="690" height="88" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2df59cc3afbfd5622b9da9c7986f18f827d178_2_690x88.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2df59cc3afbfd5622b9da9c7986f18f827d178_2_1035x132.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2df59cc3afbfd5622b9da9c7986f18f827d178_2_1380x176.png 2x" data-dominant-color="EAEAEA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1436×184 31.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In Linux, this doesn’t seem to do anything, even though there are multiple registered editors available in the system (gedit, Rstudio, etc). At the minimum it should open with vi or something. It also doesnt seem like a user-editable setting under the developer settings in Application Settings menu.</p>

---

## Post #2 by @pieper (2023-04-23 21:15 UTC)

<p>I don’t use that button, but I suspect you can control it with something like <code>export EDITOR=gvim</code>  or similar in the shell before you start Slicer.  This would at least be the old school way of doing it.</p>

---

## Post #3 by @muratmaga (2023-04-23 21:27 UTC)

<p>EDITOR/VISUAL shell variables didn’t seem to have any effect. It is not a big deal. It just helps not to navigate a bunch of folders to take a peek at the code… Works well on Mac.</p>

---

## Post #4 by @pieper (2023-04-23 21:34 UTC)

<p>Here’s the code that we use:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/e14435d3ff7205446ba5eae0e9d50d2dbb7a4148/Base/Python/slicer/ScriptedLoadableModule.py#L226-L228">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/e14435d3ff7205446ba5eae0e9d50d2dbb7a4148/Base/Python/slicer/ScriptedLoadableModule.py#L226-L228" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/e14435d3ff7205446ba5eae0e9d50d2dbb7a4148/Base/Python/slicer/ScriptedLoadableModule.py#L226-L228" target="_blank" rel="noopener">Slicer/Slicer/blob/e14435d3ff7205446ba5eae0e9d50d2dbb7a4148/Base/Python/slicer/ScriptedLoadableModule.py#L226-L228</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="226" style="counter-reset: li-counter 225 ;">
          <li>def onEditSource(self):</li>
          <li>    filePath = slicer.util.modulePath(self.moduleName)</li>
          <li>    qt.QDesktopServices.openUrl(qt.QUrl("file:///" + filePath, qt.QUrl.TolerantMode))</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It looks configurable, but may require some work:</p>
<p><a href="https://doc.qt.io/qt-5/qdesktopservices.html" class="onebox" target="_blank" rel="noopener">https://doc.qt.io/qt-5/qdesktopservices.html</a></p>
<p>Maybe better if we check the return code from the <code>openUrl</code> call and if it fails we put up a dialog box with the file path and a button to copy it to the clipboard.</p>

---
