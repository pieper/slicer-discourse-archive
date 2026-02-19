---
topic_id: 42962
title: "Ctk Axis Widget In 3Drendering"
date: 2025-05-16
url: https://discourse.slicer.org/t/42962
---

# CTK axis widget in 3Drendering

**Topic ID**: 42962
**Date**: 2025-05-16
**URL**: https://discourse.slicer.org/t/ctk-axis-widget-in-3drendering/42962

---

## Post #1 by @Pierre_Bour (2025-05-16 12:07 UTC)

<p>Dear all,<br>
I am working on a code to add a ctk widget in the 3D rendering in the upper right corner.<br>
I have currently something working but I was wondering if there is something more elegant that what I have done.</p>
<pre><code class="lang-auto">    # Get the 3D view widget
    threeDWidget = slicer.app.layoutManager().threeDWidget(0)
    threeDView = threeDWidget.threeDView()
    viewNode = threeDView.mrmlViewNode()

    # In the axes widget the order of labels is: +X, -X, +Z, -Z, +Y, -Y
    # and in the view node axis labels order is: -X, +X, -Y, +Y, -Z, +Z.
    axesLabels = [
       viewNode.GetAxisLabel(1),  # +X
       viewNode.GetAxisLabel(0),  # -X
       viewNode.GetAxisLabel(5),  # +Z
       viewNode.GetAxisLabel(4),  # -Z
       viewNode.GetAxisLabel(3),  # +Y
       viewNode.GetAxisLabel(2),  # -Y
    ]

    # Create the axes widget
    self.axesWidget = ctk.ctkAxesWidget()
    self.axesWidget.setFixedSize(100, 100)

    # Set the labels on the axes widget
    self.axesWidget.setAxesLabels(axesLabels)
    self.axesWidget.setAutoReset(True)

    # Set connections
    self.axesWidget.currentAxisChanged.connect(self.lookFromAxis)

    layout = qt.QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(self.axesWidget)

    # Add axes widget and make the background transparent
    self.overlay = qt.QWidget(threeDView)
    self.overlay.setFixedSize(100, 100)
    self.overlay.setLayout(layout)
    self.overlay.setAttribute(qt.Qt.WA_TranslucentBackground, True)
    self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 128);")

    self.overlay.installEventFilter(self)

</code></pre>
<p>the event filter play this fucntion</p>
<pre><code class="lang-auto">  #------------------------------------------------------------------------------
  def updateAxesWidgetPosition(self):
    """
    Update the position of the axes widget in the 3D view.
    """
    layoutManager = slicer.app.layoutManager()
    if layoutManager is None:
      return

    threeDView = layoutManager.threeDWidget(0).threeDView()

    # Get size of the 3D view widget
    threeDViewSize = threeDView.size

    # Compute position for top-right corner
    popupWidth = self.overlay.width
    x = threeDViewSize.width() - popupWidth
    y = 0

    self.overlay.move(x, y)
</code></pre>
<p>Thank you very much for you help and advice,</p>
<p>Pierre</p>

---
