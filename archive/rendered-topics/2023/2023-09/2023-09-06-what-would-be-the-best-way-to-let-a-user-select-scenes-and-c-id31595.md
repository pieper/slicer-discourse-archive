---
topic_id: 31595
title: "What Would Be The Best Way To Let A User Select Scenes And C"
date: 2023-09-06
url: https://discourse.slicer.org/t/31595
---

# What would be the best way to let a user select scenes and channel colours in a microscopy oriented importer?

**Topic ID**: 31595
**Date**: 2023-09-06
**URL**: https://discourse.slicer.org/t/what-would-be-the-best-way-to-let-a-user-select-scenes-and-channel-colours-in-a-microscopy-oriented-importer/31595

---

## Post #1 by @EgorZindy (2023-09-06 15:33 UTC)

<p>Hello everyone.</p>
<p>So for my <a href="https://discourse.slicer.org/t/working-on-a-czi-zeiss-microscopy-image-stack-reader-for-3d-slicer-any-help-or-advice-welcome/30769">CZI importer</a>, there are two things I think need to be user-selectable at import time:</p>
<ul>
<li>A CZI file may contain multiple scenes, and a user may decide which scenes need importing.</li>
<li>The channel colours in the CZI file may not be optimal, so being able to change them during the import phase may also be desirable.</li>
</ul>
<p>My question is, would it be possible to make this selection accessible from the import panel? Maybe via “Show options”?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/127045814462c6fc81825ad7bcf7d27a0d21fd7b.png" data-download-href="/uploads/short-url/2D78n9ugwC6Sw2rACIqFT5xiW1R.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/127045814462c6fc81825ad7bcf7d27a0d21fd7b.png" alt="image" data-base62-sha1="2D78n9ugwC6Sw2rACIqFT5xiW1R" width="690" height="404" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">744×436 7.71 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Or, do I show a custom selection panel as an intermediate step?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5be649e2bebf8ef49538fb9687966e12a7ba9249.png" alt="image" data-base62-sha1="d6YQ8oUBxEKOoblZRHVgXR7puFr" width="402" height="199"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/484e6361c822eb75f9d7edf41a50aa5ede68ad9c.png" alt="image" data-base62-sha1="ajEk4PZnNGUUxwqoFVWaT6w3EW8" width="402" height="199"></p>
<p>Clicking on the “…” button (or pressing Enter) brings up the color picker.</p>
<details><summary>Hidden spaghetti code below</summary>
<p>For now, this is just a small experiment conducted in the Jupyter extension, hence the splits corresponding to my various cells. If you find any of this code useful, feel free to re-use it any way you like, ChatGPT certainly did <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20">.</p>
<pre><code class="lang-python">import slicer
import qt
from qt import Qt
</code></pre>
<p>Here’s the code to select colors in a drop down menu:</p>
<pre><code class="lang-python">class CustomComboBox(qt.QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

    def focusInEvent(self, event):
        # Pass the focus to the parent ComboChanCol
        if self.parent():
            self.parent().setFocus()
                        
class ComboChanCol(qt.QWidget):
    """
    Custom Qt Widget to show a dropdown menu with the channels
    and a button to change the color.

    If no colors are provided, then they are automatically set to a HSV sequence
    that hopefully makes sense.
    """

    def __init__(self, channels, colors=None, *args, **kwargs):
        super(ComboChanCol, self).__init__(*args, **kwargs)
        
        # Create the horizontal layout and combobox
        layout = qt.QHBoxLayout()
        #layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self._comboBox = CustomComboBox() #qt.QComboBox()
        layout.addWidget(self._comboBox)

        # Create the button with three dots
        self._button = qt.QPushButton("...")
        self._button.setFixedHeight(self._comboBox.sizeHint.height())
        
        self._button.setMaximumWidth(30)  # Adjust the width as needed
        layout.addWidget(self._button)
        
        self.setLayout(layout)

        print(channels)
        print(colors)
        if colors is None:
            n = len(channels)
            self._colors = self.generate_colors(n)
        else:
            self._colors = [c if type(c) == qt.QColor else qt.QColor(c) for c in colors]
        
        for c,n in zip(self._colors,channels):
            icon = self.create_solid_color_icon(c)
            self._comboBox.addItem(icon,n)
            
        #Connect the button
        self._button.connect('clicked()', self.on_pick_color)
    
    def keyPressEvent(self, event):
        # Check if the Enter key is pressed and if this widget has focus
        if event.key() == Qt.Key_Return and self.hasFocus():
            self.on_pick_color()
        elif event.key() == qt.Qt.Key_Up or event.key() == qt.Qt.Key_Down:
            # Pass the up and down arrow key events to the QComboBox
            self._comboBox.event(event)
            
    def on_pick_color(self):
        channel_index = self._comboBox.currentIndex
        channel_name = self._comboBox.currentText
        initial_color = self._colors[channel_index]

        color_dialog = qt.QColorDialog(self)
        color_dialog.setCurrentColor(initial_color)
        color_dialog.setWindowTitle('Select Color for '+channel_name)

        # Show the dialog and check the result
        result = color_dialog.exec_()

        if result == qt.QColorDialog.Accepted:
            icon = self.create_solid_color_icon(color_dialog.currentColor)
            self._comboBox.setItemIcon(channel_index, icon)
            self._colors[channel_index] = color_dialog.currentColor

    def generate_colors(self, n):
        colors = []

        for i in range(n):
            hue = i * (360 / n)  # Divide the hue range evenly
            saturation = 255  # Maximum saturation
            value = 255  # Maximum value (brightness)
        
            # Create a QColor with the specified HSV values
            color = qt.QColor.fromHsv(hue, saturation, value)        
            colors.append(color)
    
        return colors
    
    def create_solid_color_icon(self, color, size=8):
        pixmap = qt.QPixmap(size,size)
        pixmap.fill(color)
        return qt.QIcon(pixmap)    

    def get_colors(self,as_hex=False):
        return [c.name() if as_hex else c for c in self._colors]
</code></pre>
<p>Here’s the code for selecting scenes via checkboxes in a drop down menu:</p>
<pre><code class="lang-python">class CheckboxComboBox(qt.QComboBox):
    def __init__(self, items, states=None):
        super().__init__()
        self.setView(qt.QListView())  # Set the view for the drop-down list
        self.activated.connect(self.activated_custom)  # Connect the activated signal to your custom slot

        #check if states is the same size as items
        if states is not None and len(items) != len(states):
            raise ValueError("states and items must have the same length")

        self.item_dict = {}
        self.setModel(qt.QStandardItemModel())

        for i, item in enumerate(items):
            checkbox_item = qt.QStandardItem(item)
            checkbox_item.setCheckable(True)
            if states is not None:
                checkbox_item.setCheckState(
                    qt.Qt.Checked if states[i]
                    else qt.Qt.Unchecked
                )
                    
            self.item_dict[item] = checkbox_item
            self.model().appendRow(checkbox_item)

        self.setView(qt.QListView())  # Set the view for the drop-down list

    def activated_custom(self, index):
        selected_item = self.model().item(index) #.row())
        if selected_item:
            selected_text = selected_item.text()  # Get the selected item text
            if selected_text in self.item_dict:
                checkbox_item = self.item_dict[selected_text]
                print(selected_text, checkbox_item.checkState())
                checkbox_item.setCheckState(
                    qt.Qt.Checked if checkbox_item.checkState() == qt.Qt.Unchecked
                    else qt.Qt.Unchecked
                )

    def get_checked_items(self):
        checked_items = {}
        for item, checkbox_item in self.item_dict.items():
            checked_items[item] = checkbox_item.checkState() == qt.Qt.Checked
        return checked_items
</code></pre>
<p>And here’s a dialog box that shows both with a text window for padding:</p>
<pre><code class="lang-python">class TestWindow(qt.QWidget):
    def __init__(self, parent=None, scenes=[], channels=[], colors=None):
        super(TestWindow, self).__init__(parent)

        parent.resize(400,400)
        parent.setWindowTitle("CZI Scene importer")

        # Create a QDialogButtonBox with OK and Cancel buttons
        buttonBox = qt.QDialogButtonBox()
        okButton = buttonBox.addButton(qt.QDialogButtonBox.Ok)
        cancelButton = buttonBox.addButton(qt.QDialogButtonBox.Cancel)
        
        layout = qt.QFormLayout()

        states = [True] * len(scenes)
        self.combo_bc = CheckboxComboBox(scenes, states)
        self._scenes_dict = self.combo_bc.get_checked_items()
        
        layout.addRow("Scenes :", self.combo_bc)
        
        self.ccc = ComboChanCol(channels, colors)
        self._colors = self.ccc.get_colors()        
        layout.addRow("Colors :", self.ccc)

        big_editor = qt.QTextEdit()
        
        layout.addWidget(big_editor)
        layout.addWidget(buttonBox)        
        parent.setLayout(layout)

        buttonBox.accepted.connect(self.ok_callback)
        buttonBox.rejected.connect(self.cancel_callback)

    def ok_callback(self):
        self._colors = self.ccc.get_colors()
        self._scenes_dict = self.combo_bc.get_checked_items()
        self.parentWidget().accept()

    def cancel_callback(self):
        self.parentWidget().reject()

    def get_colors(self, as_hex=False):
        return [c.name() if as_hex else c for c in self._colors]

    def get_scenes(self):
        return self._scenes_dict

scenes = ["Scene %d"%i for i in range(10)]
channels = ["Channel %d"%i for i in range(5)]
colors = None

messagePopup = qt.QDialog()
tw = TestWindow(messagePopup,scenes,channels,colors)    
print("Before:", tw.get_colors(as_hex=True))

result = messagePopup.exec_()
print("After:", result, tw.get_colors(as_hex=True))

print(tw.get_scenes())
</code></pre>
</details>
<p>The user experience (UX) with these widgets is pretty poor in my opinion, so that’s why I’m asking for potential ideas to streamline the process. Of course, if the user is happy with importing all the scenes and the colours are fine, then it’s just a matter of clicking on OK (or Cancel).</p>
<p>Cheers,<br>
Egor</p>

---

## Post #2 by @pieper (2023-09-06 19:13 UTC)

<p>The options in the Add Data dialog might be able to handle these but it doesn’t seem ideal to me.</p>
<p>It may make more sense to make a dedicated importer module that can pull out the pieces from the CZI file and map them to the corresponding Slicer set of nodes.  I’m kind of assuming here that you don’t want to read the full file into memory if you only want to display a subset of it.</p>

---

## Post #3 by @EgorZindy (2023-09-06 20:08 UTC)

<p>Hi Steve,</p>
<blockquote>
<p>The options in the Add Data dialog might be able to handle these but it doesn’t seem ideal to me.</p>
</blockquote>
<p>I was wondering about this. If I could hook my two drop down menus (scenes, channels) next to each other into the “Show options”, “Options” column, that would be a very good start. Right now, that space is empty:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77cd73f21effa07251abb0f2095d2cf45c2c81ad.png" data-download-href="/uploads/short-url/h5OZZj5cQDICULI4KRQuERWhloh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77cd73f21effa07251abb0f2095d2cf45c2c81ad.png" alt="image" data-base62-sha1="h5OZZj5cQDICULI4KRQuERWhloh" width="690" height="404" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">744×436 7.91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This could go in the empty space (one for each file row):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/991ac47d38d7efcb50f4b92efcb766e1ccf494b9.png" alt="image" data-base62-sha1="lQqoVTSkHP0Fk6YzoEiBFoFhsiB" width="232" height="490"></p>
<blockquote>
<p>It may make more sense to make a dedicated importer module that can pull out the pieces from the CZI file and map them to the corresponding Slicer set of nodes. I’m kind of assuming here that you don’t want to read the full file into memory if you only want to display a subset of it.</p>
</blockquote>
<p>Yes, that’s definitely what I want to do, and at least for the CZI format, I have all the pieces I need to pull individual scenes into Slicer.</p>
<p>However, I’ve just now started to look into building a user interface for my importer, and was wondering exactly how to tackle this.</p>
<p>The only other importer I’ve found with a complex user interface is <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/ImportOsirixROI" rel="noopener nofollow ugc">ImportOsirixROI</a> but in my case, popping a window open whether the user wants to change the import parameters or not doesn’t seem ideal.</p>
<p>I’m really new to this, are there any medical formats with multiple sub images and/or multiple channels or is this more a “microscopy thing”?</p>
<p>So that was the general idea behind my question. Any ideas welcome <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @muratmaga (2023-09-06 20:22 UTC)

<p>Data dialog box is difficult to navigate. I would encourage you to take a look at the image stacks interface of Slicermorph, in which we walk user through a steps of decision making about importing imagestack.</p>
<p>You seem to have a lot of decisions to make and a dedicated interface.will give you more control over them.</p>

---

## Post #5 by @muratmaga (2023-09-06 20:46 UTC)

<p>Here is a screenshot of the interface<br>
          <a href="https://raw.githubusercontent.com/SlicerMorph/Tutorials/main/ImageStacks/ImageStacks1.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://raw.githubusercontent.com/SlicerMorph/Tutorials/main/ImageStacks/ImageStacks1.png" width="" height="">
          </a>
</p>

---

## Post #6 by @EgorZindy (2023-09-06 21:01 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>I also found the <a href="https://www.youtube.com/@slicermorphslicermorph8728/videos" rel="noopener nofollow ugc">Slicermorph YouTube channel</a>, great resource!</p>
<p>The “quality” setting in the screenshot above is a really good idea. I’ll definitely keep it in mind. Not sure in the case of CZI images if it’ll decrease the loading time but I won’t know unless I try.</p>
<p>Cheers,<br>
Egor</p>

---
