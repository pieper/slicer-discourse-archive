# The Add Data button is not working properly

**Topic ID**: 44557
**Date**: 2025-09-23
**URL**: https://discourse.slicer.org/t/the-add-data-button-is-not-working-properly/44557

---

## Post #1 by @Victor_Wayne (2025-09-23 08:45 UTC)

<p>So, when I click the Add Data button, it opens the file dialog box and I am able to load MRIs perfectly. But if I close the file dialog box without loading any MRML or MRI files and then try to open it again the file dialog box just goes full black and nothing is showing. The title bar of that window and the close button is working perfectly fine but it is not showing any files or folders to load. Just a black window. How can I fix it? Thanks for you help.</p>
<p>(P.S This is problem exists in both pre-built slicer and the slicer I built)</p>

---

## Post #2 by @jamesobutler (2025-09-23 10:59 UTC)

<p>I assume you are using Linux? This has seemingly only come up on that platform. It has something that has been noticed and there is hope that switching to a newer Qt version will resolve it. That should hopefully happen soon. For now you can track the progress at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8579">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8579" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8579" target="_blank" rel="noopener nofollow ugc">Add Data dialog turns black after closing with window “X” on Red Hat Linux</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-07-16" data-time="16:05:39" data-timezone="UTC">04:05PM - 16 Jul 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/amillercompotech" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/208820852?v=4" class="onebox-avatar-inline" width="20" height="20">
          amillercompotech
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

When using 3D Slicer 5.8.1 on a Linux server, I encounter an issue w<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">here the “Add Data” dialog becomes non-functional (black screen) after closing it with the window’s “X” button instead of using **OK** or **Cancel**.

## Steps to reproduce

1. Open 3D Slicer  
2. Click the Add Data icon  
3. Close the dialog using the window manager’s “X” button (see gif)  
4. Attempt to open **Add Data** again.  

## Notes
- This issue only occurs on Linux.
- I could not reproduce it on Windows 11.

## Environment
- **3D Slicer version:** 5.8.1
- **OS:** Red Hat Enterprise Linux (RHEL 9.5)

![Image](https://github.com/user-attachments/assets/026ef675-3497-4d59-b641-9a309c4edd47)

![Image](https://github.com/user-attachments/assets/4f5cfe7b-c289-4678-8942-36c0c0d013a5)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Suhaim (2025-11-28 05:28 UTC)

<p>Hi <a class="mention" href="/u/jamesobutler">@jamesobutler</a>,<br>
Could you suggest how to temporarily remove the “X“ icon of that DataDialog window?<br>
I found the UI file for the widget at, <code>Base/QTGUI/Resources/UI/qSlicerDataDialog.ui.</code>The UI file doesn’t have the “X” icon and seems to populated in the dialog window by some other code.</p>
<p>Could you help with identifying what part of the code to modify for users facing this problem so that there is a temporary fix until the issue is solved in the core repo? I have built Slicer from source, so I don’t mind sub-classing the core Slicer widget or even modifying the Slicer widget on my machine.<br>
Thanks!</p>
<p>PS :</p>
<p>My environment details : -</p>
<p>Slicer version: 5.10.0<br>
Operating system: Ubuntu 22.04<br>
Desktop environment: ubuntu:GNOME<br>
Session type: x11<br>
GPU hardware: Mesa Intel® UHD Graphics (TGL GT1)</p>

---

## Post #4 by @Suhaim (2025-11-28 06:32 UTC)

<p>Hi everyone,<br>
I was able to do the temporary fix I asked for, I edited the following function :-<br>
<code>bool qSlicerDataDialog::exec(const qSlicerIO::IOProperties&amp; readerProperties)</code></p>
<p>All one needs to do is use <code>QWidget::setWindowFlags()</code></p>
<p>Inside <code>qSlicerDataDialog::exec</code> of the core slicer widget, I added one more bit-wise operation- <code>&amp; ~Qt::WindowCloseButtonHint</code> to all <code>QWidget::setWindowFlags()</code> calls inside the function. This removes the close icon(“x“ icon)</p>
<p>I think sub-classing the core widget and overriding said function would be a better approach.</p>

---
