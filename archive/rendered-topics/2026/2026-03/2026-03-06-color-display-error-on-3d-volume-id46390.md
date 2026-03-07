---
topic_id: 46390
title: "Color Display Error On 3D Volume"
date: 2026-03-06
url: https://discourse.slicer.org/t/46390
---

# Color display error on 3D Volume

**Topic ID**: 46390
**Date**: 2026-03-06
**URL**: https://discourse.slicer.org/t/color-display-error-on-3d-volume/46390

---

## Post #1 by @Karuruychi (2026-03-06 10:15 UTC)

<p>Hello everyone</p>
<p>I’m developing an application based on Trame-Slicer, specifically a 3D ROI Cropping feature. Trame-Slicer already supports displaying the ROI box, but when I enable it, my 3D block displays incorrect colors. I’m not sure why; it might be due to a mistake or something missing in my setup code. Please give me your opinion.<br>
Here is my setup code:<br>
```</p>
<pre data-code-wrap="python"><code class="lang-python">def cropVolume(self) -&gt; None:
        if not self.volume_node:
            logging.warning("[Volume] No volume node found for cropping")
            return

        # 1. Get Display node
        display_node = self.slicer_app.volume_rendering.get_vr_display_node(self.volume_node)
        if not display_node:
            logging.warning("[Volume] No VR display node found")
            return

        # 2. Get ROI node and toggle logic
        is_enabled = not display_node.GetCroppingEnabled()
        roi_node = self.slicer_app.volume_rendering.get_cropping_roi_node(self.volume_node)

        self.slicer_app.volume_rendering.set_cropping_enabled(
            self.volume_node, 
            roi_node, 
            is_enabled
        )

        self.slicer_app.volume_rendering.set_cropping_roi_node_visibile(self.volume_node, is_enabled)

        # 3. Update
        self.view3D.render()
        if self.controller:
            self.controller.volume_update()


</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52a6fb1ef7ab967fa583d5257b37efcfa8435a2d.jpeg" data-download-href="/uploads/short-url/bNaUgMXmib95t7WSRZ6ODj0157f.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52a6fb1ef7ab967fa583d5257b37efcfa8435a2d_2_584x500.jpeg" alt="image" data-base62-sha1="bNaUgMXmib95t7WSRZ6ODj0157f" width="584" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52a6fb1ef7ab967fa583d5257b37efcfa8435a2d_2_584x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52a6fb1ef7ab967fa583d5257b37efcfa8435a2d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52a6fb1ef7ab967fa583d5257b37efcfa8435a2d.jpeg 2x" data-dominant-color="5E5758"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">868×742 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @drnoorfatima (2026-03-06 10:25 UTC)

<p><strong>The corrupted colors are a transfer function reset issue.</strong> When cropping is toggled, Trame-Slicer internally touches the display node and wipes your color/opacity mapping.</p>
<p>Quick thing to check first: are you saving the <code>VolumePropertyNode</code> before calling <code>set_cropping_enabled</code>? If not, that is almost certainly your problem. The fix involves reapplying it after the toggle fires.</p>
<p>The full solution also depends on your Trame-Slicer version and how your volume rendering pipeline is initialized, because there are a couple of different ways this can break depending on the setup.<br>
Rather than write a wall of code here that may or may not match your setup, feel free to DM me. I can take a quick look at your full pipeline and point you to the exact fix. Should not take long.</p>

---
