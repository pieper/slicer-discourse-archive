---
topic_id: 3203
title: "Rotation Of A Ct Image Around The Rt Isocenter In Python"
date: 2018-06-16
url: https://discourse.slicer.org/t/3203
---

# Rotation of a CT image around the RT isocenter, in python

**Topic ID**: 3203
**Date**: 2018-06-16
**URL**: https://discourse.slicer.org/t/rotation-of-a-ct-image-around-the-rt-isocenter-in-python/3203

---

## Post #1 by @gdenunzio (2018-06-16 06:50 UTC)

<p>Hi all,<br>
I am a 3D Slicer beginner, so please bear with me…</p>
<p>I have a CT image (in DICOM series format) used for radiation treatment planning. I wish to<br>
read it, apply to it an arbitrary 3D rotation around the isocenter, then resave it as a DICOM series (to read it back into the TPS).<br>
I wish to do it by python scripting (because I’ll have many different rotations to explore, so I want to automate the procedure).<br>
I am learning by doing, because at present I don’t have much time to fully understand the software before starting coding.</p>
<p>By reading what I coud find in the Forum and in the documentation, I understood how to:</p>
<ol>
<li>
<p>prepare things:</p>
<p>import argparse, sys, shutil, os, logging<br>
import vtk, qt, ctk, slicer<br>
import DICOMLib<br>
from DICOMLib import DICOMUtils</p>
</li>
<li>
<p>parse the command line:</p>
<p>def main(argv):<br>
print(‘STARTING!’)<br>
try:<br>
parser = argparse.ArgumentParser(description=“to be done”)<br>
parser.add_argument("-i", “–input-folder”, dest=“input_folder”, metavar=“PATH”,<br>
default="-", required=True, help=“Folder of input DICOM files (can contain sub-folders)”)<br>
parser.add_argument("-o", “–output-folder”, dest=“output_folder”, metavar=“PATH”,<br>
default=".", help=“Folder to save converted datasets”)<br>
args = parser.parse_args(argv)<br>
if args.input_folder == “-”:<br>
print(‘Please specify input DICOM study folder!’)<br>
if args.output_folder == “.”:<br>
print(‘Current directory is selected as output folder (default). To change it, please specify --output-folder’)</p>
</li>
<li>
<p>read the dicom series:</p>
<p>logging.info("Import DICOM data from " + args.input_folder)<br>
DICOMUtils.openTemporaryDatabase()<br>
DICOMUtils.importDicom(args.input_folder)<br>
logging.info(“Load first patient into Slicer”)<br>
patient = slicer.dicomDatabase.patients()[0]<br>
DICOMUtils.loadPatientByUID(patient)</p>
</li>
<li>
<p>Save as nnrd, which is not what I need, but it was at least a test that I was correctly reading the image and filling the right Slicer structures…</p>
<p>node_key = ‘vtkMRMLScalarVolumeNode*’<br>
sv_nodes = slicer.util.getNodes(node_key)<br>
logging.info(“Save image volumes nodes to directory %s: %s” % (args.output_folder, ‘,’.join(sv_nodes.keys())))<br>
for imageNode in sv_nodes.values():<br>
# Clean up file name and set path<br>
fileName = imageNode.GetName() + ‘.nrrd’<br>
charsRoRemove = [’!’, ‘?’, ‘:’, ‘;’]<br>
fileName = fileName.translate(None, ‘’.join(charsRoRemove))<br>
fileName = fileName.replace(’ ‘, ‘_’)<br>
filePath = args.output_folder + ‘/’ + fileName<br>
logging.info(’  Saving image ’ + imageNode.GetName() + ‘\n    to file &lt;’ + filePath + ‘&gt;’)<br>
# Save to file<br>
success = slicer.util.saveNode(imageNode, filePath)<br>
if not success:<br>
logging.error('Failed to save image volume: ’ + filePath)</p>
</li>
<li>
<p>Get out:</p>
</li>
</ol>
<p>except Exception, e:<br>
print e<br>
sys.exit()<br>
return</p>
<ol start="6">
<li>
<p>Prepare “main” execution:</p>
<p>if <strong>name</strong> == “<strong>main</strong>”:<br>
main(sys.argv[1:])</p>
</li>
</ol>
<p>My questions are:</p>
<ol>
<li>
<p>How do I apply the rotation transform?</p>
</li>
<li>
<p>I imagine I can apply a chain of transforms, so I can translate the image so that the isocenter is in the axis origin, then rotate, than translate back: how to do it?</p>
</li>
<li>
<p>How do I save the result as a DICOM series, by using the input DICOM series as a model (as to voxel/slice dimensions, and all the other relevant DICOM fields)?</p>
</li>
</ol>
<p>Any hint, code snippets, link to relevant material, is really welcome.<br>
Thank you very much.<br>
Giorgio<br>
PS sorry, after many tries, I am not succeeding in correctly formatting the code snippets… preformatted text does not give the desired result…  indentation has totally gone…</p>

---

## Post #2 by @gdenunzio (2018-06-16 14:06 UTC)

<p>Beginning to see something.<br>
I applied some transformations this way:</p>
<pre><code>vTransform = vtk.vtkTransform()
vTransform.Translate(-0.88, 35.4, 5.65)  # translate by -isocenter
vTransform.Scale(1,1,1)
vTransform.RotateX(30)  # The angle is in degrees
vTransform.Translate(0.88, -35.4, -5.65)
imageNode.ApplyTransform(vTransform)
</code></pre>
<p>Now I have to interpret what I am seing, and check if this is what I am looking for…<br>
Any help or comment are still very very welcome…!<br>
Best<br>
Giorgio</p>

---

## Post #3 by @Tiberiu (2023-06-13 09:31 UTC)

<p>Hi,<br>
I need to do the same as you. Do you know how to save the transformed scan? When I save the nrrd file for multiple rotations I get the same (presumably original) scan.</p>

---

## Post #4 by @ma1282029525 (2023-06-14 06:02 UTC)

<p>The rotation operation you performed only involves visual effects, while the actual DICOM image does not undergo any transformation. In ITK, this requires resampling to complete</p>

---

## Post #5 by @KHhh (2023-10-24 17:28 UTC)

<p>Hey! I have been doing the same thing but instead of coding it using 3D slicer, I rotated the DCOM file using simpleITK, saved it as a nifti and have been using 3D slicer to view/ check my rotation was accurate. I think it works</p>

---

## Post #6 by @gdenunzio (2023-10-24 17:37 UTC)

<p>Dear friends, before all thanks for your kind replies! Because of the long time elapsed, I had not realized that you had kindly replied! So excuse me and again thanks! I do not even remember if I solved somehow or if I gave up or used other tools (e.g. matlab). That said, thanks for your effort!   Giorgio</p>

---
