# ScreenShot is toooo small when red/yellow/green view too small

**Topic ID**: 23110
**Date**: 2022-04-25
**URL**: https://discourse.slicer.org/t/screenshot-is-toooo-small-when-red-yellow-green-view-too-small/23110

---

## Post #1 by @caiqj1203 (2022-04-25 09:04 UTC)

<p>I resize main window like this .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e5173b2e23e987f70557af071fd299f7d98803b.jpeg" data-download-href="/uploads/short-url/6BKtmEuK8izsvlPlKfJI9b7sMVZ.jpeg?dl=1" title="mw_too_small" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2e5173b2e23e987f70557af071fd299f7d98803b_2_84x500.jpeg" alt="mw_too_small" data-base62-sha1="6BKtmEuK8izsvlPlKfJI9b7sMVZ" width="84" height="500" data-dominant-color="202220"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mw_too_small</span><span class="informations">107×631 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>and I use <code>captureImageFromView</code> function to generate screenshot, the screenshot like this</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89ec8efb766b37b0b8906dc95a01171b062c14bb.jpeg" alt="small_screenshott" data-base62-sha1="jG8eJV9TZJ5jSynCC2b945gdZGz" width="339" height="257"></p>
<p>What can I do to make the size of the screenshot independent of the display window?</p>

---

## Post #2 by @lassoan (2022-04-25 12:38 UTC)

<p>You need to make your main window bigger or undock all the widgets (module panel, Python interactor, etc.) that take up space in your main window. You can also maximize each view and take screenshot one by one, change the main window size to be larger than your screen size (<code>slicer.util.mainWindow().size=qt.QSize(2000,2000)</code>), or <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-slice-view-outside-the-view-layout">create a slice viewer outside the main window</a> and set its size to be very large.</p>

---

## Post #3 by @caiqj1203 (2022-04-26 02:01 UTC)

<p>What if the screen is very small?</p>

---

## Post #4 by @lassoan (2022-04-26 03:10 UTC)

<p>You can adjust your screen resolution in your system settings and/or <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#runtime-environment-variables">adjust the application scaling</a> using environment variables.</p>

---
