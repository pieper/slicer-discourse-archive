# How to download markups as sample data

**Topic ID**: 36029
**Date**: 2024-05-09
**URL**: https://discourse.slicer.org/t/how-to-download-markups-as-sample-data/36029

---

## Post #1 by @DavidM (2024-05-09 15:32 UTC)

<p>Hi,</p>
<p>I am trying to create tests for a module I’m developing and as part of the test I’m using sampledata. I’m unable to download and import markup fiducial files (mrk.json) but have no issues with stl or vtp files. My code is below. I’m not sure what loadFileType should be set to, maybe this is the issue? I also run into the same problem if I try to read vtu files. Is there a documented way to import markup files as sampledata? Thank you for any help</p>
<pre><code class="lang-auto">def registerSampleData():

    import SampleData
    iconsPath = os.path.join(os.path.dirname(__file__), 'Resources/Icons')
    
    # load demo data    
    SampleData.SampleDataLogic.registerCustomSampleDataSource(
        category="Heart",
        sampleName='RCA',
        uris='https://github.com/dmolony3/SlicerFractionalMyocardialMass/releases/download/SampleData/RCA.mrk.json',
        fileNames='RCA.mrk.json',
        nodeNames='RCA',
        loadFileType='MarkupsFile',
        )
    SampleData.SampleDataLogic.registerCustomSampleDataSource(
        category="Heart",
        sampleName='RCA_surface',
        uris='https://github.com/dmolony3/SlicerFractionalMyocardialMass/releases/download/SampleData/RCA_surface.vtp',
        fileNames='RCA_surface.vtp',
        nodeNames='RCA_surface',
        loadFileType='ModelFile',
        )

class FMMTest(ScriptedLoadableModuleTest):
    """
    This is the test case for your scripted module.
    Uses ScriptedLoadableModuleTest base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def setUp(self):
        """ Do whatever is needed to reset the state - typically a scene clear will be enough.
        """
        slicer.mrmlScene.Clear()

    def runTest(self):
        """Run as few or as many tests as needed here.
        """
        self.setUp()
        self.test_FMM()

    def test_FMM(self):

        import SampleData
        registerSampleData()
        RCA = SampleData.downloadSample('RCA')
        self.delayDisplay('Loaded RCA markup')
        LCA = SampleData.downloadSample('LCA')
        self.delayDisplay('Loaded LCA markup')
        RCA_surface = SampleData.downloadSample('RCA_surface')
        self.delayDisplay('Loaded RCA surface')
        LCA_surface = SampleData.downloadSample('LCA_surface')
        self.delayDisplay('Loaded LCA surface')
        myocardium_surface = SampleData.downloadSample('myocardium_surface')
        self.delayDisplay('Loaded myocardium surface')
        myocardium_volume = SampleData.downloadSample('myocardium_volume')
        self.delayDisplay('Loaded myocardium volume')
        
        outputTable = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTableNode', 'FMM')
        outputMesh = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode', 'Myocardium')

        # Test the module logic
        logic = FMMLogic()

        inputMMARMarkup = None
        self.delayDisplay('Processing starts.')
        outputTable, outputMesh = logic.segmentMesh(myocardium_surface, LCA, RCA, inputMMARMarkup, outputTable, outputMesh) # 3D
        
        self.delayDisplay('Processing ends.')

        self.delayDisplay('Test passed')
</code></pre>

---

## Post #2 by @muratmaga (2024-05-09 18:03 UTC)

<p>You should be able to load markups directly into the scene. See this example (note that in this specific case loadFile is set to FALSE)</p>
<pre><code class="lang-auto">    SampleData.SampleDataLogic.registerCustomSampleDataSource(
      sampleName='Mouse Skull Reference Model',
      category='SlicerMorph',
      uris=['https://github.com/SlicerMorph/SampleData/blob/master/4074_skull.vtk?raw=true', 'https://raw.githubusercontent.com/SlicerMorph/SampleData/master/4074_S_lm1.fcsv?raw=true'],
      checksums=[None, None],
      loadFiles=[False, False],
      fileNames=['4074_skull.vtk','4074_S_lm1.fcsv'],
      nodeNames=['4074_skull', '4074_S_lm1'],
      thumbnailFileName=os.path.join(iconsPath, 'mouse3D.png'),
      loadFileType=['ModelFile','MarkupsFile'],
      customDownloader=self.downloadSampleDataInFolder,
)
</code></pre>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/131a0c6bea14e41ee0ae0b2eb5bae4d055ceafea/SlicerMorphSampleData/SlicerMorphSampleData.py#L69">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/131a0c6bea14e41ee0ae0b2eb5bae4d055ceafea/SlicerMorphSampleData/SlicerMorphSampleData.py#L69" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/131a0c6bea14e41ee0ae0b2eb5bae4d055ceafea/SlicerMorphSampleData/SlicerMorphSampleData.py#L69" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/131a0c6bea14e41ee0ae0b2eb5bae4d055ceafea/SlicerMorphSampleData/SlicerMorphSampleData.py#L69</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="59" style="counter-reset: li-counter 58 ;">
          <li>      sampleName='Mouse Skull Landmarks Only',</li>
          <li>      category='SlicerMorph',</li>
          <li>      uris='https://github.com/SlicerMorph/SampleData/blob/master/mouse_skull_LMs.zip?raw=true',</li>
          <li>      checksums=None,</li>
          <li>      loadFiles=False,</li>
          <li>      fileNames='mouse_skull_LMs.zip',</li>
          <li>      thumbnailFileName=os.path.join(iconsPath, 'pointcloud.png'),</li>
          <li>      loadFileType='ZipFile',</li>
          <li>      customDownloader=self.downloadSampleDataInFolder,</li>
          <li>)</li>
          <li class="selected">    SampleData.SampleDataLogic.registerCustomSampleDataSource(</li>
          <li>      sampleName='Mouse Skull Reference Model',</li>
          <li>      category='SlicerMorph',</li>
          <li>      uris=['https://github.com/SlicerMorph/SampleData/blob/master/4074_skull.vtk?raw=true', 'https://raw.githubusercontent.com/SlicerMorph/SampleData/master/4074_S_lm1.fcsv?raw=true'],</li>
          <li>      checksums=[None, None],</li>
          <li>      loadFiles=[False, False],</li>
          <li>      fileNames=['4074_skull.vtk','4074_S_lm1.fcsv'],</li>
          <li>      nodeNames=['4074_skull', '4074_S_lm1'],</li>
          <li>      thumbnailFileName=os.path.join(iconsPath, 'mouse3D.png'),</li>
          <li>      loadFileType=['ModelFile','MarkupsFile'],</li>
          <li>      customDownloader=self.downloadSampleDataInFolder,</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @DavidM (2024-05-10 01:30 UTC)

<p>Thanks for providing this example. I’m struggling a little bit to understand how to implement this. I need to set loadFiles to True? Do I then make an instance of the class and is there a method I should call to load the data?</p>
<p>Thanks for any additional help</p>

---
