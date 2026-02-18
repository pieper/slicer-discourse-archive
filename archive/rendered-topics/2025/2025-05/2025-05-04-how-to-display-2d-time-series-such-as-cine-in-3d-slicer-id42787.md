# how to display 2D time series such as Cine in 3D Slicer

**Topic ID**: 42787
**Date**: 2025-05-04
**URL**: https://discourse.slicer.org/t/how-to-display-2d-time-series-such-as-cine-in-3d-slicer/42787

---

## Post #1 by @Wei_Sun (2025-05-04 18:12 UTC)

<p>Hi There,</p>
<p>Is there a way to display 2D time series such as cine in 3D Slicer? I converted one 2D time series with 30 images into nii.gz but can only display one image in 3D Slicer.</p>
<p>Thanks,<br>
Wei</p>

---

## Post #2 by @ungi (2025-05-05 15:24 UTC)

<p>Hi, the Sequences module was developed for time series. I’ve been using it for time series of 2D ultrasound successfully. There is not a lot of support for importing different file formats as sequences, so if you have a video file, you may need to implement the importing process. And once you have the data in Slicer, it’s easiest to just save it as a Slicer scene. But some DICOM format time series already load as sequences, so it’s worth trying before you implement your own importer code.</p>

---

## Post #3 by @Deep_Learning (2025-05-05 19:34 UTC)

<p>you might need to save each timepoint  as seperate nii.gz’s to load it into a sequence.</p>

---

## Post #4 by @Wei_Sun (2025-05-06 03:35 UTC)

<p>I tried it but it did not work for my data. Thank you for your suggestion!</p>

---

## Post #5 by @cpinter (2025-05-06 11:32 UTC)

<p>To be able to load a time series directly to Slicer, a specially formatted NRRD is needed, see the CTP Cardio file for example (you can load it using the Sample Data module and the file will be in <code>c:\Users\[You]\AppData\Local\slicer.org\Slicer\cache\SlicerIO</code></p>
<p>However, the best would probably be what <a class="mention" href="/u/ungi">@ungi</a> suggests. You can make a sequence from a set of images with a bit of scripting. This is a script I created to read in a set of transforms into a sequence. You need to modify it just a bit to load the images into a sequence.</p>
<pre><code class="lang-auto"># Create a sequence node
sequenceNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceNode", "GridTransforms")
sequenceNode.SetIndexName("time")
sequenceNode.SetIndexUnit("")
# Get all transform files in the directory
transformFiles = glob.glob(f"{transformFilesPath}/Transform_*.h5")
transformFiles.sort()  # Sort to ensure correct order

# Process each file
for frameIndex, filePath in enumerate(transformFiles):
  # Load the grid transform from HDF5
  transformNode = slicer.util.loadTransform(filePath)
  if transformNode is None:
    print(f"Failed to load transform from {filePath}")
    continue
  # Add the transform node to the sequence
  sequenceNode.SetDataNodeAtValue(transformNode, str(frameIndex))
  slicer.mrmlScene.RemoveNode(transformNode)

# Create a sequence browser node
browserNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSequenceBrowserNode", "GridTransformsBrowser")
browserNode.AddSynchronizedSequenceNode(sequenceNode.GetID())
</code></pre>

---
