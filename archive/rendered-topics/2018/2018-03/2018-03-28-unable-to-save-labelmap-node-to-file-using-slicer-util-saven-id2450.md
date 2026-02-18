# Unable to save labelmap node to file using slicer.util.saveNode()

**Topic ID**: 2450
**Date**: 2018-03-28
**URL**: https://discourse.slicer.org/t/unable-to-save-labelmap-node-to-file-using-slicer-util-savenode/2450

---

## Post #1 by @drusmanbashir (2018-03-28 09:45 UTC)

<p>Hi,<br>
I have a node called labelmapVolumeNode:</p>
<p>(MRMLCorePython.vtkMRMLLabelMapVolumeNode)000000001C9821C8</p>
<p>But when i try to save it  i get ‘False’ return:</p>
<p>file_path = os.path.join(os.getcwd(), “temporary.nrrd”)<br>
slicer.util.saveNode(labelmapVolumeNode, file_path)<br>
False</p>
<p>The code works if the node in question is a volume node.</p>
<p>Any tips?<br>
Thanks<br>
Usman.</p>

---

## Post #2 by @drusmanbashir (2018-03-28 09:58 UTC)

<p>I realised the labelMapvolumenode was empty. Code works now</p>

---
