# Path of data added to slicer

**Topic ID**: 30425
**Date**: 2023-07-06
**URL**: https://discourse.slicer.org/t/path-of-data-added-to-slicer/30425

---

## Post #1 by @Kening_Zhang (2023-07-06 08:09 UTC)

<p>Dear developer,<br>
I only find the command about the path of files of DICOM, how can I find the path of data added to slicer, by the way, I also want to know the command of  loaded the generated anatomical tracts into the Slicer.<br>
Here is my code,</p>
<h1><a name="p-97233-h-1" class="anchor" href="#p-97233-h-1" aria-label="Heading link"></a></h1>
<pre><code># Input file selector
#
with It(qt.QLineEdit()) as w:
    self.inputFileSelector = w
    w.setReadOnly(True)
    w.setToolTip("Select input file")

def selectInputFile():
  inputFile = qt.QFileDialog.getOpenFileName(self.parent, "Select input file")
  if inputFile:
    self.inputFileSelector.setText(inputFile)

def executeTractography():
  storageNode = node.GetStorageNode()
  if storageNode is not None: # loaded via drag-drop
    self.inputFileSelector = storageNode.GetFullNameFromFileName()
  
with It(qt.QPushButton("Browse")) as button:
    button.clicked.connect(selectInputFile)

with It(qt.QPushButton("Execute")) as executeButton:
    executeButton.clicked.connect(executeTractography)

layout = qt.QHBoxLayout()
layout.addWidget(self.inputFileSelector)
layout.addWidget(button)
layout.addWidget(executeButton)

parametersFormLayout.addRow("Input File:", layout)
</code></pre>
<p>Best wishes,<br>
Joshua</p>

---

## Post #2 by @rbumm (2023-07-06 13:21 UTC)

<pre><code class="lang-auto">slicer.mrmlScene.GetRootDirectory() # all nodes are saved relative to this path
slicer.app.temporaryPath # write-able folder, you can use this to store any temporary data
slicer.app.slicerHome # Slicer core binary folder
slicer.app.extensionsInstallPath # Slicer extensions folder
slicer.modules.sampledata.path # path of a scripted module (in this example: Sample Data module)
</code></pre>

---

## Post #3 by @pieper (2023-07-06 13:27 UTC)

<p>If the data was loaded from disk or saved to disk it will typically have a storage node.  From there you can get the path.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.util.getNode("MRHead").GetStorageNode().GetFileName()
'/private/tmp/MRHead.nrrd'
</code></pre>

---
