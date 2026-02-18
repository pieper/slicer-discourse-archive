# How to load an entire entire dicom directory using the widget button on a python code?

**Topic ID**: 3088
**Date**: 2018-06-06
**URL**: https://discourse.slicer.org/t/how-to-load-an-entire-entire-dicom-directory-using-the-widget-button-on-a-python-code/3088

---

## Post #1 by @Rahul_Banerjee (2018-06-06 13:42 UTC)

<p>I could only load individual files using the default slicelet code given on the website and the documentation, would like help as I want to upload an entire dicom directory.</p>

---

## Post #2 by @lassoan (2018-06-06 20:41 UTC)

<p>You can use DICOMLib.DICOMUtils.LoadDICOMFilesToDatabase See complete example here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/5ec342768faff961fd3b236935dfe95d7198b117/Applications/SlicerApp/Testing/Python/SubjectHierarchyGenericSelfTest.py#L165-L184" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5ec342768faff961fd3b236935dfe95d7198b117/Applications/SlicerApp/Testing/Python/SubjectHierarchyGenericSelfTest.py#L165-L184" target="_blank">Slicer/Slicer/blob/5ec342768faff961fd3b236935dfe95d7198b117/Applications/SlicerApp/Testing/Python/SubjectHierarchyGenericSelfTest.py#L165-L184</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="165" style="counter-reset: li-counter 164 ;">
<li>try:</li>
<li>  # Open test database and empty it</li>
<li>  with DICOMUtils.TemporaryDICOMDatabase(self.dicomDatabaseDir) as db:</li>
<li>    self.assertTrue( db.isOpen )</li>
<li>    self.assertEqual( slicer.dicomDatabase, db)</li>
<li>
</li>
<li>    # Download, unzip, import, and load data. Verify loaded nodes.</li>
<li>    loadedNodes = {'vtkMRMLScalarVolumeNode':1}</li>
<li>    with DICOMUtils.LoadDICOMFilesToDatabase( \</li>
<li>        self.dicomZipFileUrl, self.dicomZipFilePath, \</li>
<li>        self.dicomDataDir, self.expectedNumOfFilesInDicomDataDir, \</li>
<li>        {}, loadedNodes) as success:</li>
<li>      self.assertTrue(success)</li>
<li>
</li>
<li>  self.assertEqual( len( slicer.util.getNodes('vtkMRMLSubjectHierarchyNode*') ), 1 )</li>
<li>
</li>
<li>except Exception, e:</li>
<li>  import traceback</li>
<li>  traceback.print_exc()</li>
<li>  self.delayDisplay('Test caused exception!\n' + str(e),self.delayMs*2)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>See also this post: <a href="https://discourse.slicer.org/t/imported-dicom-files-do-not-show-in-the-dicomdatabase/2651">Imported dicom files do not show in the dicomDatabase</a></p>

---

## Post #3 by @Rahul_Banerjee (2018-06-07 05:40 UTC)

<p>How do I get the following segment to load dicom database, instead of the individual files it is loading at present?</p>
<blockquote>
<p>loadDataButton = qt.QPushButton(“Load Data”)<br>
hlayout.addWidget(loadDataButton)<br>
loadDataButton.connect(‘clicked()’, slicer.util.openAddVolumeDialog)</p>
</blockquote>
<p><strong><em>Entire Code:</em></strong></p>
<pre><code>def onModuleSelected(modulename):
  global tabWidget
  scrollArea = qt.QScrollArea(tabWidget)
  scrollArea.setWidget(getattr(slicer.modules, modulename.lower()).widgetRepresentation())
  scrollArea.setHorizontalScrollBarPolicy(qt.Qt.ScrollBarAlwaysOff)
  scrollArea.setWidgetResizable(True)
  tabWidget.addTab(scrollArea, modulename)



import qt
import __main__try:
 



mainWidget = qt.QWidget()
mainWidget.objectName = "qSlicerAppMainWindow"
vlayout = qt.QVBoxLayout()
mainWidget.setLayout(vlayout)


# splitter between "layout" and "bottom frame"
#splitter = qt.QSplitter()
#splitter.orientation = qt.Qt.Vertical
#vlayout = qt.QVBoxLayout()
#vlayout.addWidget(splitter)

# layout
layoutManager = slicer.qMRMLLayoutWidget()
layoutManager.setMRMLScene(slicer.mrmlScene)
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)
vlayout.addWidget(layoutManager)

# Bottom frame: including control buttons and tab widget
bottomFrame = qt.QFrame()
bottomVlayout = qt.QVBoxLayout()
bottomFrame.setLayout(bottomVlayout)
vlayout.addWidget(bottomFrame)

# Horizontal layout: Load Data, Save Data, Module Selector
hlayout = qt.QHBoxLayout()
bottomVlayout.addLayout(hlayout)

loadDataButton = qt.QPushButton("Load Data")
#loadDataButton = Button(root, text="Load Data", command=browsefunc)
#loadDataButton.pack()
hlayout.addWidget(loadDataButton)
#loadDataButton.connect('clicked()', browsefunc)
loadDataButton.connect('clicked()', slicer.util.openAddVolumeDialog)
#loadDataButton.connect('clicked()', slicer.util.loadVolume('/path/of/*'))
#loadDataButton.connect('clicked()',DICOMUtils.LoadDICOMFilesToDatabase)


saveDataButton = qt.QPushButton("Save Data")
hlayout.addWidget(saveDataButton)
saveDataButton.connect('clicked()', slicer.util.openSaveDataDialog)

moduleSelector = slicer.qSlicerModuleSelectorToolBar()
moduleSelector.setModuleManager(slicer.app.moduleManager())
hlayout.addWidget(moduleSelector)
#moduleSelector.connect('moduleSelected(QString)', onModuleSelected)



# Tab widget
tabWidget = qt.QTabWidget()
bottomVlayout.addWidget(tabWidget)

# Connections
moduleSelector.connect('moduleSelected(QString)', onModuleSelected)

# Initialize
modules = ["volumes", "models", "labelstatistics"]
for module in modules:
  onModuleSelected(module)

#tabWidget.show()
mainWidget.show()
#__main__.tabWidget = tabWidget # Keep track of the widget to avoid its premature destruction


__main__.mainWidget = mainWidget # Keep track of the widget to avoid its premature destruction
</code></pre>

---

## Post #4 by @Rahul_Banerjee (2018-06-07 05:41 UTC)

<p>How do I get the following segment to load dicom database, instead of the individual files it is loading at present?</p>
<blockquote>
<p>loadDataButton = qt.QPushButton(“Load Data”)<br>
hlayout.addWidget(loadDataButton)<br>
loadDataButton.connect(‘clicked()’, slicer.util.openAddVolumeDialog)</p>
</blockquote>
<p><em><strong>Entire Code:</strong></em></p>
<pre><code>def onModuleSelected(modulename):

global tabWidget

scrollArea = qt.QScrollArea(tabWidget)

scrollArea.setWidget(getattr(slicer.modules, modulename.lower()).widgetRepresentation())

scrollArea.setHorizontalScrollBarPolicy(qt.Qt.ScrollBarAlwaysOff)

scrollArea.setWidgetResizable(True)

tabWidget.addTab(scrollArea, modulename)

import qt

import __main__try:

mainWidget = qt.QWidget()

mainWidget.objectName = “qSlicerAppMainWindow”

vlayout = qt.QVBoxLayout()

mainWidget.setLayout(vlayout)

# splitter between “layout” and “bottom frame”
#splitter = qt.QSplitter()

#splitter.orientation = qt.Qt.Vertical

#vlayout = qt.QVBoxLayout()

#vlayout.addWidget(splitter)

# layout
layoutManager = slicer.qMRMLLayoutWidget()

layoutManager.setMRMLScene(slicer.mrmlScene)

layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutOneUp3DView)

vlayout.addWidget(layoutManager)

# Bottom frame: including control buttons and tab widget
bottomFrame = qt.QFrame()

bottomVlayout = qt.QVBoxLayout()

bottomFrame.setLayout(bottomVlayout)

vlayout.addWidget(bottomFrame)

# Horizontal layout: Load Data, Save Data, Module Selector
hlayout = qt.QHBoxLayout()

bottomVlayout.addLayout(hlayout)

loadDataButton = qt.QPushButton(“Load Data”)

#loadDataButton = Button(root, text=“Load Data”, command=browsefunc)

#loadDataButton.pack()

hlayout.addWidget(loadDataButton)

#loadDataButton.connect(‘clicked()’, browsefunc)

loadDataButton.connect(‘clicked()’, slicer.util.openAddVolumeDialog)

#loadDataButton.connect(‘clicked()’, slicer.util.loadVolume(’/path/of/*’))

#loadDataButton.connect(‘clicked()’,DICOMUtils.LoadDICOMFilesToDatabase)

saveDataButton = qt.QPushButton(“Save Data”)

hlayout.addWidget(saveDataButton)

saveDataButton.connect(‘clicked()’, slicer.util.openSaveDataDialog)

moduleSelector = slicer.qSlicerModuleSelectorToolBar()

moduleSelector.setModuleManager(slicer.app.moduleManager())

hlayout.addWidget(moduleSelector)

#moduleSelector.connect(‘moduleSelected(QString)’, onModuleSelected)

# Tab widget
tabWidget = qt.QTabWidget()

bottomVlayout.addWidget(tabWidget)

# Connections
moduleSelector.connect(‘moduleSelected(QString)’, onModuleSelected)

# Initialize
modules = [“volumes”, “models”, “labelstatistics”]

for module in modules:

onModuleSelected(module)

#tabWidget.show()

mainWidget.show()

#**main**.tabWidget = tabWidget # Keep track of the widget to avoid its premature destruction

**main**.mainWidget = mainWidget # Keep track of the widget to avoid its premature destruction
</code></pre>

---

## Post #5 by @lassoan (2018-06-07 14:29 UTC)

<p>Please provide more information. It is not obvious what you would like to do, what do you expect your current code should do, and what happens instead.</p>
<p>The forum is good for discussion but not well suited for code review. If you upload your code to github and send a link to it then there is a better chance that somebody can look at it and give you feeback.</p>

---
