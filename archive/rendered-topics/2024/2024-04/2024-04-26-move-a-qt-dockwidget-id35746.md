# Move a Qt Dockwidget

**Topic ID**: 35746
**Date**: 2024-04-26
**URL**: https://discourse.slicer.org/t/move-a-qt-dockwidget/35746

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-04-26 13:20 UTC)

<p>Hi to all the community.</p>
<p>The task today is move my DockWidgetArea from here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a84d5cf0347f0ac728087ee510d078d2e9884820.png" data-download-href="/uploads/short-url/o0RXNRxXUV3aGjQ1zj3r22CV2bm.png?dl=1" title="Captura de pantalla 2024-04-26 151712" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a84d5cf0347f0ac728087ee510d078d2e9884820_2_690x452.png" alt="Captura de pantalla 2024-04-26 151712" data-base62-sha1="o0RXNRxXUV3aGjQ1zj3r22CV2bm" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a84d5cf0347f0ac728087ee510d078d2e9884820_2_690x452.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a84d5cf0347f0ac728087ee510d078d2e9884820_2_1035x678.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a84d5cf0347f0ac728087ee510d078d2e9884820.png 2x" data-dominant-color="22211F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-04-26 151712</span><span class="informations">1095×718 34.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>to here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c2e200abfd67e168a1195d751ecda877f22f645.png" data-download-href="/uploads/short-url/aRV6QCfLLB9yU9r2H5B8hYArnIp.png?dl=1" title="Captura de pantalla 2024-04-26 151748" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c2e200abfd67e168a1195d751ecda877f22f645_2_527x500.png" alt="Captura de pantalla 2024-04-26 151748" data-base62-sha1="aRV6QCfLLB9yU9r2H5B8hYArnIp" width="527" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c2e200abfd67e168a1195d751ecda877f22f645_2_527x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c2e200abfd67e168a1195d751ecda877f22f645.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c2e200abfd67e168a1195d751ecda877f22f645.png 2x" data-dominant-color="2D2D2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2024-04-26 151748</span><span class="informations">743×704 30.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>At this moment I’m doing it manually, but I’m sure that specifying the correct configuration it could be made automatically.</p>
<p>My current function is:</p>
<pre><code class="lang-auto">def createDockInterface():
    # Delete the statusBar to have cleaner view:
    slicer.util.mainWindow().setStatusBar(None)
    
    # Create and name the widget:
    dock_widget = qt.QDockWidget("ST Assistant v16")
    dock_widget.setObjectName('SegmentTracerDockWidget')
    
    
    # Add the Welcome text:
    label = qt.QLabel("Welcome to SegmentTracer. Loading and resampling data")
    dock_layout = qt.QVBoxLayout()
    dock_layout.addWidget(label)
    dock_content = qt.QWidget()
    dock_content.setLayout(dock_layout)
    dock_widget.setWidget(dock_content)
    
    # Display the widget in bottom left corner:
    slicer.util.mainWindow().addDockWidget(qt.Qt.LeftDockWidgetArea, dock_widget)   
</code></pre>
<p>Thanks a lot for any help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2024-04-29 13:51 UTC)

<p>Maybe somebody from the Slicer developer community will chime in, but since this is a pure Qt question (not related to how Qt is used in Slicer), you can probably find answer more easily by searching or asking on Qt forums.</p>

---
