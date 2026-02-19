---
topic_id: 38468
title: "Adding An Icon To A Ctkcheckablepushbutton Is Difficult"
date: 2024-09-21
url: https://discourse.slicer.org/t/38468
---

# Adding an icon to a ctkCheckablePushButton is difficult

**Topic ID**: 38468
**Date**: 2024-09-21
**URL**: https://discourse.slicer.org/t/adding-an-icon-to-a-ctkcheckablepushbutton-is-difficult/38468

---

## Post #1 by @mau_igna_06 (2024-09-21 14:42 UTC)

<p>Does someone know why I cannot get the right side icon to not render over the text?</p>
<pre><code class="lang-auto">class CustomCheckablePushButton(ctk.ctkCheckablePushButton):
    def __init__(self, text="", parent=None):
        super().__init__(parent)
        
        # Create main layout
        self._mainLayout = qt.QHBoxLayout(self)
        self._mainLayout.setContentsMargins(8, 8, 8, 8)
        self._mainLayout.setSpacing(12)  # Increased spacing between text and icon
        
        # Create a widget to hold the text
        self.textLabel = qt.QLabel(text)
        self.textLabel.setWordWrap(True)  # Allow text to wrap
        self.textLabel.setAlignment(qt.Qt.AlignLeft | qt.Qt.AlignVCenter)
        
        # Create a widget to hold the icon
        self.iconLabel = qt.QLabel()
        self.iconLabel.setAlignment(qt.Qt.AlignCenter)
        
        # Add widgets to main layout
        self._mainLayout.addWidget(self.textLabel, 1)  # Text widget takes up remaining space
        self._mainLayout.addWidget(self.iconLabel, 0)  # Icon widget doesn't expand
        
        # Store the right icon and its size
        self._rightIcon = qt.QIcon()
        self._rightIconSize = qt.QSize(32, 32)  # Default size 32x32
        
        # Set size policy to allow horizontal expansion
        self.setSizePolicy(qt.QSizePolicy.Expanding, qt.QSizePolicy.Preferred)

    def setText(self, text):
        self.textLabel.setText(text)
        self.updateGeometry()

    def text(self):
        return self.textLabel.text()

    def setRightIcon(self, icon):
        self._rightIcon = icon
        self._updateRightIcon()

    def setRightIconSize(self, size):
        self._rightIconSize = size
        self._updateRightIcon()

    def _updateRightIcon(self):
        if self._rightIcon.isNull():
            self.iconLabel.hide()
        else:
            pixmap = self._rightIcon.pixmap(self._rightIconSize)
            self.iconLabel.setPixmap(pixmap)
            self.iconLabel.setFixedSize(self._rightIconSize)
            self.iconLabel.show()
        self.updateGeometry()

    def sizeHint(self):
        textWidth = self.textLabel.sizeHint().width()
        iconWidth = self._rightIconSize.width() if not self._rightIcon.isNull() else 0
        width = textWidth + iconWidth + self._mainLayout.spacing() + self._mainLayout.contentsMargins().left() + self._mainLayout.contentsMargins().right()
        height = max(self.textLabel.sizeHint().height(), self._rightIconSize.height()) + self._mainLayout.contentsMargins().top() + self._mainLayout.contentsMargins().bottom()
        return qt.QSize(width, height)

    def minimumSizeHint(self):
        return self.sizeHint()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjustSize()  # Ensure the button resizes to fit content
</code></pre>
<p>Here is my example use case:</p>
<pre><code class="lang-auto">mybutton = CustomCheckablePushButton()
mybutton.text = (
    "Update\nvisualization"
)

updatePlanningIconPath = os.path.join(DOWNLOADPATH,'update_48.jpg')

mybutton.setRightIcon(qt.QIcon(updatePlanningIconPath))
mybutton.setRightIconSize(qt.QSize(32, 32))
</code></pre>
<p>Here is a screenshot of how it renders:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8231853ec78b8ff9c4803d378389ca6d43404f3f.png" alt="image" data-base62-sha1="izKar0GKixNaENYj7qDEhLiMM6b" width="137" height="52"></p>
<p>Here is the icon:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://fonts.google.com/icons?selected=Material%2BSymbols%2BOutlined:update:FILL@0%3Bwght@600%3BGRAD@0%3Bopsz@48&amp;icon.query=update&amp;icon.size=48&amp;icon.color=%23000000">
  <header class="source">
      <img src="https://www.gstatic.com/images/icons/material/apps/fonts/1x/catalog/v5/favicon.svg" class="site-icon" width="16" height="16">

      <a href="https://fonts.google.com/icons?selected=Material%2BSymbols%2BOutlined:update:FILL@0%3Bwght@600%3BGRAD@0%3Bopsz@48&amp;icon.query=update&amp;icon.size=48&amp;icon.color=%23000000" target="_blank" rel="noopener nofollow ugc">Google Fonts</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/361;"><img src="https://www.gstatic.com/images/icons/material/apps/fonts/1x/material-symbols/material_symbols.jpg" class="thumbnail" width="690" height="393"></div>

<h3><a href="https://fonts.google.com/icons?selected=Material%2BSymbols%2BOutlined:update:FILL@0%3Bwght@600%3BGRAD@0%3Bopsz@48&amp;icon.query=update&amp;icon.size=48&amp;icon.color=%23000000" target="_blank" rel="noopener nofollow ugc">Material Symbols and Icons - Google Fonts</a></h3>

  <p>Material Symbols are our newest icons consolidating over 2,500 glyphs in a single font file with a wide range of design variants.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope you can help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @mau_igna_06 (2024-09-21 21:52 UTC)

<p>This was useful enough for me:</p>
<pre><code class="lang-auto">class checkablePushButtonWithIcon(ctk.ctkCheckablePushButton):
    def __init__(self, text="", icon=qt.QIcon(), parent=None):
        super().__init__(parent)
        self.text = text
        #
        self._mainLayout = qt.QHBoxLayout(self)
        self._mainLayout.setContentsMargins(0, 0, 0, 0)
        #self._mainLayout.setSpacing(15)
        #self._mainLayout.setSpacing(300)
        #
        self.icon = icon
        self._iconSize = qt.QSize(36, 36)
        pixmap = self.icon.pixmap(self._iconSize)
        self._iconLabel = qt.QLabel()
        self._iconLabel.setAlignment(qt.Qt.AlignCenter)
        self._iconLabel.setPixmap(pixmap)
        self._iconLabel.setFixedSize(self._iconSize)
        self._mainLayout.addSpacing(self.sizeHint.width())
        self._mainLayout.addWidget(self._iconLabel)
        self.setMinimumWidth(self.sizeHint.width() + self._iconSize.width())
        self.setSizePolicy(qt.QSizePolicy.Maximum, qt.QSizePolicy.Fixed)


</code></pre>

---
