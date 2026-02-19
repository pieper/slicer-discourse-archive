---
topic_id: 34788
title: "Wayland Vtk Glew Could Not Be Initialized Unknown Error"
date: 2024-03-08
url: https://discourse.slicer.org/t/34788
---

# Wayland: [VTK] GLEW could not be initialized: Unknown error

**Topic ID**: 34788
**Date**: 2024-03-08
**URL**: https://discourse.slicer.org/t/wayland-vtk-glew-could-not-be-initialized-unknown-error/34788

---

## Post #1 by @chir.set (2024-03-08 19:01 UTC)

<p>Hi all,</p>
<p>KDE on Arch Linux is now at version 6 and uses Wayland by default. X11 is still available but support seems decreased, and it will probably stop some day.</p>
<p>The problem with Slicer is the appearance of this message on every MRML event, even in an empty scene, <em>in Python console</em> and in stdout. The flooded Python console becomes hard to use, whether for running code or reading other messages.</p>
<p><code>[VTK] GLEW could not be initialized: Unknown error</code></p>
<p>I rebuilt Slicer and extensions in vain regarding the appearance of this message. GLEW is installed on the build machine and the runtime machine. (By the way, I don’t know what it does, what it is).</p>
<p>I wish to know if there’s a way to prevent this message from showing in Python console. Is there a VTK configuration parameter to set? Some system changes to do? As a last ‘solution’, I’ll try to search this message in the source files of VTK, simply remove it and adapt the SuperBuild cmake file.</p>
<p>Thanks and regards.</p>

---

## Post #2 by @pieper (2024-03-08 20:58 UTC)

<p>Yes, trying to debug this at the VTK level is probably the right thing to do, but it may not be easy.  Probably Slicer / VTK are not the only programs that have issues with Wayland so I’d suggest sticking with X11 for now.  Eventually maybe Vulkan, Wayland, and other new things will be preferable but the transition is likely to take a while.</p>

---

## Post #3 by @chir.set (2024-03-08 21:24 UTC)

<p>Thanks for your reply.</p>
<p>Meanwhile, I found a nice workaround <a href="https://github.com/Slicer/Slicer/issues/7282#issuecomment-1827541418" rel="noopener nofollow ugc">here</a>.</p>
<pre><code class="lang-auto"># Use either or both
# export XDG_SESSION_TYPE=""
export QT_QPA_PLATFORM="xcb"
</code></pre>
<p>The view controllers are badly located also under KDE6/Wayland.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8660140db7989c93c3a420acde23ab986b48ab07.png" data-download-href="/uploads/short-url/jaJPkx0HI8CQMo88hJNoxDxI4g7.png?dl=1" title="View_Controllers_Wayland_KDE6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/8660140db7989c93c3a420acde23ab986b48ab07_2_690x318.png" alt="View_Controllers_Wayland_KDE6" data-base62-sha1="jaJPkx0HI8CQMo88hJNoxDxI4g7" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/8660140db7989c93c3a420acde23ab986b48ab07_2_690x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/8660140db7989c93c3a420acde23ab986b48ab07_2_1035x477.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8660140db7989c93c3a420acde23ab986b48ab07.png 2x" data-dominant-color="13130E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">View_Controllers_Wayland_KDE6</span><span class="informations">1182×546 40.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ll report other issues as they are discovered.</p>
<p>But the above workaround resolves everything up to now.</p>

---
