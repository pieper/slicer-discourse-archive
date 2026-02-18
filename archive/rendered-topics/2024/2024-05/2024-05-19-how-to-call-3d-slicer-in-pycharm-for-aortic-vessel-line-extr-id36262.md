#  How to call 3D slicer in pycharm for aortic vessel line extraction and vessel straightening. 

**Topic ID**: 36262
**Date**: 2024-05-19
**URL**: https://discourse.slicer.org/t/how-to-call-3d-slicer-in-pycharm-for-aortic-vessel-line-extraction-and-vessel-straightening/36262

---

## Post #1 by @yml-bit (2024-05-19 14:22 UTC)

<p>I am currently encountering challenges integrating 3D Slicer into my Python workflow within PyCharm for the automated analysis of a large dataset of aortic images. Specifically, I possess a collection of 3D aortic scans (1.nii.gz) alongside their corresponding segmentation masks (2.nii.gz), and my objective is to leverage 3D Slicer’s capabilities for automated vessel centerline extraction and CPR (Curved Planar Reformation) straightening on these datasets.</p>
<p>While manual utilization of 3D Slicer through its graphical user interface (GUI) has proven insightful, I’ve encountered an operational bottleneck: the interactive determination of the centerline’s starting point, a process that is impractical for high-volume, automated processing. This interactive requirement hinders the scalability and efficiency of my workflow, particularly when dealing with a large batch of images.</p>
<p>Given this scenario, I am eager to explore the possibility of programmatically invoking 3D Slicer’s functionalities directly from within my Python scripts executed in PyCharm. My aim is to feed in the starting points for the centerline, which would be algorithmically determined beforehand, thereby bypassing the need for manual intervention and streamlining the entire process.</p>
<p>I am reaching out to seek your expert guidance on how best to achieve this integration. Any advice, code snippets, or pointers towards relevant documentation or examples that could facilitate the seamless interaction between Python and 3D Slicer for my specific purposes would be immensely appreciated. Your assistance would significantly enhance the automation level of my project and accelerate the research process.</p>
<p>Thank you very much in advance for your time and expertise. I look forward to your valuable insights.</p>
<p>Best regards,</p>

---

## Post #2 by @lassoan (2024-05-20 03:31 UTC)

<p>It is great that VMTK in Slicer works well for you. It should be no problem at all to run your Python scripts in 3D Slicer’s Python environment from PyCharm to automate any processing.</p>
<p>If you want to use Slicer modules then you’ll need to launch the Slicer executable: <code>Slicer.exe --python-script path/to/myscript.py</code></p>
<p>For step-by-step debugging in PyCharm you can use the <a href="https://github.com/SlicerRt/SlicerDebuggingTools?tab=readme-ov-file#debuggingtools-extension-for-3d-slicer">DebuggingTools extension</a>.</p>

---
