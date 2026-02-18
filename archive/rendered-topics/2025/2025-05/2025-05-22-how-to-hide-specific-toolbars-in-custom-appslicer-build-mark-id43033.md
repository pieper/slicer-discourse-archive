# How to Hide Specific Toolbars in Custom AppSlicer Build (Markups, Sequence Browser, etc.)

**Topic ID**: 43033
**Date**: 2025-05-22
**URL**: https://discourse.slicer.org/t/how-to-hide-specific-toolbars-in-custom-appslicer-build-markups-sequence-browser-etc/43033

---

## Post #1 by @software (2025-05-22 08:18 UTC)

<p>Hi everyone,</p>
<p>I’ve created a custom <code>NewAppSlicer</code> build using Kitware’s 3D Slicer source. Everything is working great, but I’m running into a UI customization issue.</p>
<p>From the <strong>View &gt; Toolbars</strong> menu, I want to <strong>permanently hide</strong> some specific toolbars in my custom build:</p>
<ul>
<li>Mouse Interaction</li>
<li>Capture/Restore</li>
<li>Crosshair Selection</li>
<li>Extensions</li>
<li>Markups</li>
<li>Sequence Browser<br>
I’ve tried hiding them in <code>qNewSlicerAppMainWindowPrivate::setupUi()</code> using the following:<br>
this-&gt;MouseModeToolBar-&gt;setVisible(false);<br>
this-&gt;CaptureToolBar-&gt;setVisible(false);<br>
this-&gt;ViewToolBar-&gt;setVisible(false);<br>
// … and others<br>
Despite no build errors, after compiling and running the app, <strong>these toolbars still appear</strong> in the toolbar list and show up in the UI.</li>
</ul>
<h3><a name="p-125331-what-ive-tried-1" class="anchor" href="#p-125331-what-ive-tried-1" aria-label="Heading link"></a>What I’ve Tried:</h3>
<ul>
<li>Verified the toolbar object names (e.g., <code>MouseModeToolBar</code>, <code>CaptureToolBar</code>)</li>
<li>Added <code>setVisible(false)</code> calls</li>
<li>Rebuilt from scratch and cleared CMake cache</li>
</ul>
<h3><a name="p-125331-what-i-need-help-with-2" class="anchor" href="#p-125331-what-i-need-help-with-2" aria-label="Heading link"></a>What I Need Help With:</h3>
<ul>
<li>The correct internal object names for toolbars like <strong>Markups</strong>, <strong>Extensions</strong>, and <strong>Sequence Browser</strong></li>
<li>Whether hiding them in <code>setupUi()</code> is the right approach</li>
<li>Any other reliable way to <strong>remove/hide these toolbars</strong> by default so users don’t see or re-enable them</li>
</ul>
<p>I’d really appreciate any tips or code examples from someone who has customized the Slicer UI at this level.</p>
<p>Thanks in advance!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3cebdae5db443e8339dd52195f32c80a327a60f.png" data-download-href="/uploads/short-url/yMOXSjTsmkb8xuFV143NDyVpPqL.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3cebdae5db443e8339dd52195f32c80a327a60f.png" alt="Capture" data-base62-sha1="yMOXSjTsmkb8xuFV143NDyVpPqL" width="561" height="312"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">561×312 23.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
