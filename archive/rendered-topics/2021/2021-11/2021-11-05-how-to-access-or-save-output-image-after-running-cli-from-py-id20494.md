---
topic_id: 20494
title: "How To Access Or Save Output Image After Running Cli From Py"
date: 2021-11-05
url: https://discourse.slicer.org/t/20494
---

# How to access or save output image after running CLI from Python

**Topic ID**: 20494
**Date**: 2021-11-05
**URL**: https://discourse.slicer.org/t/how-to-access-or-save-output-image-after-running-cli-from-python/20494

---

## Post #1 by @gnketiah (2021-11-05 03:27 UTC)

<p>I have created or run a CLI from Python to calculate T1 mapping as follows.</p>
<pre><code class="lang-python">cliNode = slicer.cli.runSync(slicer.modules.t1mapping, None, parameters)
</code></pre>
<p>Detailed script:</p>
<pre><code class="lang-python">def t1mapping(parameters = {}):
    '''Code for running the pkmoddeling module with input parameters 
    specified in the dict'''
    # adding an alias to the module
    t1mapping = slicer.modules.t1mapping
    # creating a CLI node
    cliNode = slicer.cli.runSync(slicer.modules.t1mapping, None, parameters)
    if cliNode.GetStatus() &amp; cliNode.ErrorsMask:
        # error
        errorText = cliNode.GetErrorText()
        slicer.mrmlScene.RemoveNode(cliNode)
        raise ValueError("CLI execution failed: " + errorText)
    return cliNode


def getIputVolume(inputdir,outputdir):
    DicomFolders=os.listdir(inputdir)
    for index,DicomFolder in enumerate(DicomFolders):
        fullPath = os.path.join(inputdir,DicomFolder)
        fileNames = os.listdir(fullPath)
        for index,fileName in enumerate(fileNames):
            fileNames[index]=os.path.join(inputdir,DicomFolder,fileName)
            
    db = slicer.dicomDatabase
    plugin = slicer.modules.dicomPlugins['MultiVolumeImporterPlugin']()
    if plugin:
        loadables = plugin.examine([fileNames])
    if len(loadables) == 0:
        print('plugin failed to interpret this series')
    else:
        patientID = db.fileValue(loadables[0].files[0],'0010,0020')
        outputPath = os.path.join(outputdir, patientID +  ".nrrd") 
        print (outputPath)
        volume = plugin.load(loadables[0])
        slicer.util.saveNode(volume,outputPath) # saves the loaded image
 
    return  volume,  os.path.join(outputdir, patientID + "_T1map.nrrd") 

# get input volume and output path
inputImageVolume, outputFileName= getIputVolume(inputdir,outputdir)

# Parameters share for all patients in loop
defaultParameters = {'modelName': 'VFA'} 

# list containing parameterdict for each run of the code.
parameters = copy.copy(defaultParameters)
parameters['imageName'] = inputImageVolume 
parameters['T1MapFileName'] = outputFileName

# do actual stuff here  
t1mapping(parameters = parameters)
</code></pre>
<p>All parameters were set correctly and it runs without error (form cliNode.GetErrorText()). My question is how to access or save the calculated or resulting image from cliNode . I would prefer to it save as .nrrd or .mhd file.</p>
<p>I specified the full path in the parameters dict: e.g. parameters[‘T1MapFileName’] = ‘some_path.nrrd’.<br>
But there is no output file or image.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-11-05 15:55 UTC)

<p><code>parameters['imageName']</code> and <code>parameters['T1MapFileName']</code> must be set to a valid MRML volume node object or MRML node ID. You need to create a new volume node for storing the output. See example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-run-a-cli-module-from-python">here</a>.</p>
<p>Once the CLI execution is completed, you can save the volume node to file using <code>saveNode</code> function. See example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file">here</a>.</p>

---

## Post #3 by @gnketiah (2021-11-15 09:39 UTC)

<p>Thanks for the guidance</p>

---
