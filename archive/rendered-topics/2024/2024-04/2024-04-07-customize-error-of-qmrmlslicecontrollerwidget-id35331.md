---
topic_id: 35331
title: "Customize Error Of Qmrmlslicecontrollerwidget"
date: 2024-04-07
url: https://discourse.slicer.org/t/35331
---

# Customize error of qMRMLSliceControllerWidget

**Topic ID**: 35331
**Date**: 2024-04-07
**URL**: https://discourse.slicer.org/t/customize-error-of-qmrmlslicecontrollerwidget/35331

---

## Post #1 by @park (2024-04-07 09:56 UTC)

<p>Hi all,</p>
<p>I would like to customize of qMRMLSliceControllerWidget</p>
<p>My code is like this (there is no error), but it is not work well.<br>
Especially, the QLabel is not change and the maximize Button is not hide</p>
<p>Can I get a solution for this?</p>
<pre><code class="lang-auto">for viewColor in ["Red", "Green", "Yellow"]:
  widgets2D = layoutManager.sliceWidget(viewColor).findChild("qMRMLSliceControllerWidget")
      
  sliderWidget = widgets2D.findChild("qMRMLSliderWidget")
  sliderWidget.setVisible(False)

  buttons2D = widgets2D.findChildren('QToolButton')

  for button in buttons2D:
    button.setVisible(False)

  viewLabel = widgets2D.findChild("QLabel", "ViewLabel")

    
  if viewColor == "Red":
    viewLabel.setText("Axial")  

  if viewColor == "Green":
    viewLabel.setText("Coronal")

  if viewColor == "Yellow":
    viewLabel.setText("Saggital")

  font = qt.QFont()
  font.setPointSize(12)
  font.setBold(True)
  viewLabel.setFont(font)

  viewLabel.setAlignment(qt.Qt.AlignLeft)
</code></pre>

---

## Post #2 by @qiqi5210 (2024-04-07 12:58 UTC)

<pre><code class="lang-auto">layoutManager=slicer.app.layoutManager()
for viewColor in ["Red", "Green", "Yellow"]:
  widgets2D = layoutManager.sliceWidget(viewColor).findChild("qMRMLSliceControllerWidget")
      
  sliderWidget = widgets2D.findChild("qMRMLSliderWidget")
  sliderWidget.setVisible(False)

  buttons2D=slicer.util.findChild(widgets2D, 'MaximizeViewButton')


  buttons2D.hide()
</code></pre>

---

## Post #3 by @park (2024-04-08 07:43 UTC)

<p>Using this code, it disappears like in the video and then reappears.</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
twoDwidget = layoutManager.sliceWidget("Red")
twoDwidgetBar = twoDwidget.findChild("qMRMLSliceControllerWidget")
button = twoDwidgetBar.findChild("QToolButton", "MaximizeViewButton")
button.hide()
</code></pre>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6a3b0e970ffe37c94bf8994ccb73bcdc2c2b0a4.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e977f559b0b0b83eb9682cc4f989f7b38c286b6b.png">
  </div><p></p>

---

## Post #4 by @lassoan (2024-04-08 17:19 UTC)

<p>Maximize/restore button state is managed by the widget, so you won’t be able to permanently change visibility by low-level under-the-hood manipulations. Instead, you can hide the entire qMRMLViewControllerBar or implement a flag that allows disabling of the maximize/restore feature.</p>

---

## Post #5 by @park (2024-04-09 03:53 UTC)

<p>I got a soultion about it</p>
<pre><code class="lang-auto">for controllerBar in slicer.util.mainWindow().findChildren("qMRMLViewControllerBar"):
    controllerBar.showMaximizeViewButton = False
</code></pre>

---

## Post #6 by @lassoan (2024-04-09 16:26 UTC)

<p>You may still be able to maximize the view by using the right-click menu or double-click on the view. That may show the maximize button again.</p>

---

## Post #7 by @park (2024-04-12 02:00 UTC)

<p>I think it works well. It dose not appear again.</p>

---
