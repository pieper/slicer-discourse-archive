# Create plane on 3D model - problem with landmarks

**Topic ID**: 40796
**Date**: 2024-12-19
**URL**: https://discourse.slicer.org/t/create-plane-on-3d-model-problem-with-landmarks/40796

---

## Post #1 by @Konstantin (2024-12-19 04:52 UTC)

<p>Good Day. I want to create a plane on the 3D model of the calcaneus. I installed the module “Angle planes”. According to the guide, I click the “add landmark” button and try to manually place landmarks. But instead, landmarks are created on the surface of the model automatically in large quantities (20-30). At first, I thought that the problem was specifically in the program on my computer and installed the 3D slicer on my laptop. But the same thing happens there. Please help me solve the problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dbc2c59137dc119c47341dff60da8154a8d0920.png" data-download-href="/uploads/short-url/8O8hFvE0Rmj0QzRdkPwp2DubzNe.png?dl=1" title="3D SLICER" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dbc2c59137dc119c47341dff60da8154a8d0920_2_690x376.png" alt="3D SLICER" data-base62-sha1="8O8hFvE0Rmj0QzRdkPwp2DubzNe" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dbc2c59137dc119c47341dff60da8154a8d0920_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dbc2c59137dc119c47341dff60da8154a8d0920_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3dbc2c59137dc119c47341dff60da8154a8d0920_2_1380x752.png 2x" data-dominant-color="C2C3D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D SLICER</span><span class="informations">1898×1035 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-12-19 05:09 UTC)

<p>I don’t think the AnglePlanes extension is maintained. You can submit an issue to its developers at <a href="https://github.com/DCBIA-OrthoLab/AnglePlanes-Extension/issues" class="inline-onebox">Issues · DCBIA-OrthoLab/AnglePlanes-Extension · GitHub</a>.</p>
<p>Fortunately, this extension is almost fully replaced by Markups module.<br>
You can place a “plane” markup on the model directly, using Markups module. Markups module does not provide relative measurements between multiple markups but you can specify any number of automatic relative measurements by a few lines of Python script. For example, you can copy-paste this code snippet to get the angle between plane nodes <code>P</code> and <code>P_1</code>:</p>
<pre data-code-wrap="python"><code class="lang-python">plane1 = getNode("P")
plane2 = getNode("P_1")
angleDeg = vtk.vtkMath.DegreesFromRadians(vtk.vtkMath.AngleBetweenVectors(plane1.GetNormalWorld(), plane2.GetNormalWorld()))
print(f"Angle between planes: {angleDeg:0.1f}")
</code></pre>
<p>A bit more sophisticated script that continuously prints the current angle <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-markup-planes">in ths script repository</a>.</p>

---

## Post #3 by @Konstantin (2024-12-19 05:22 UTC)

<p>Thanks for the answer. I still wanted to automate the process of measuring the angle between planes, because my task is to measure orthopedic angles by four points. Using the command line complicates the process too much.</p>

---

## Post #4 by @Konstantin (2024-12-19 05:44 UTC)

<p>Professor Lasso, сan I transfer the value of the obtained angle between two planes from console to the nodes section?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce719e084df4f548648d7206b850cfc7099bba8a.png" data-download-href="/uploads/short-url/tshMxpy0TNhM4OpcItQmRCpyMMG.png?dl=1" title="3D SLICER 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce719e084df4f548648d7206b850cfc7099bba8a_2_690x377.png" alt="3D SLICER 2" data-base62-sha1="tshMxpy0TNhM4OpcItQmRCpyMMG" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce719e084df4f548648d7206b850cfc7099bba8a_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce719e084df4f548648d7206b850cfc7099bba8a_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce719e084df4f548648d7206b850cfc7099bba8a_2_1380x754.png 2x" data-dominant-color="CCCBDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D SLICER 2</span><span class="informations">1894×1035 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2024-12-19 05:51 UTC)

<p>GUI used to be simpler. However, for this kind of custom measurement tasks, I think using scripting is now simpler and more efficient.</p>
<p>The most important thing that you might not know that for simple tasks like this, you don’t need to write program code anymore. Instead, you can ask any AI chatbot (ChatGPT, Microsoft Copilot, etc. all know 3D Slicer well) and it does everything for you.</p>
<p>For example, I used the free <a href="https://copilot.microsoft.com/">Microsoft Copilot</a>. I asked:</p>
<blockquote>
<p>Generate a code snippet that I can copy into 3D Slicer that measures the angle between planes <code>"P"</code> and <code>"P_1"</code> and displays the value in a popup window. Run this measurement when I hit “Ctrl-A”.</p>
</blockquote>
<p>It generated code that worked perfectly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4635339364c1f44ca79e0941b1be0f8dd06b6966.png" data-download-href="/uploads/short-url/a15pcMmPV9XqrkjkWEUBTBfynv8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4635339364c1f44ca79e0941b1be0f8dd06b6966_2_363x500.png" alt="image" data-base62-sha1="a15pcMmPV9XqrkjkWEUBTBfynv8" width="363" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4635339364c1f44ca79e0941b1be0f8dd06b6966_2_363x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4635339364c1f44ca79e0941b1be0f8dd06b6966_2_544x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/4635339364c1f44ca79e0941b1be0f8dd06b6966_2_726x1000.png 2x" data-dominant-color="1D212D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1290×1776 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<details>
<summary>
Code snippet generated by Microsoft Copilot</summary>
<pre><code class="lang-auto">import slicer
from qt import QKeySequence, QShortcut, QMessageBox

def measure_angle_between_planes():
    # Get the plane nodes
    plane1 = slicer.mrmlScene.GetFirstNodeByName('P')
    plane2 = slicer.mrmlScene.GetFirstNodeByName('P_1')
    
    if not plane1 or not plane2:
        QMessageBox.warning(slicer.util.mainWindow(), 'Error', 'One or both planes not found.')
        return

    # Get the normal vectors of the planes
    normal1 = [0, 0, 0]
    normal2 = [0, 0, 0]
    plane1.GetNormal(normal1)
    plane2.GetNormal(normal2)

    # Calculate the angle between the normals
    import numpy as np
    dot_product = np.dot(normal1, normal2)
    norm1 = np.linalg.norm(normal1)
    norm2 = np.linalg.norm(normal2)
    angle_radians = np.arccos(dot_product / (norm1 * norm2))
    angle_degrees = np.degrees(angle_radians)

    # Display the angle in a popup window
    QMessageBox.information(slicer.util.mainWindow(), 'Angle Between Planes', f'The angle between the planes is: {angle_degrees:.2f} degrees')

# Create a shortcut for Ctrl-A to run the measurement
shortcut = QShortcut(QKeySequence("Ctrl+A"), slicer.util.mainWindow())
shortcut.activated.connect(measure_angle_between_planes)
</code></pre>
</details>
<p>I copy-pasted  this code to the Python console, then placed two planes, then hit <code>Ctrl-A</code>, and it showed the angle value in a popup window, as I asked.</p>
<p>If you don’t want to copy-paste this code each time you start Slicer, you can put it in the <code>Application startup script</code> (you can get the location of this file from the application menu → Edit → Application settings → General → Application startup script).</p>
<p>The beauty of this is that you don’t rely on any developer to do anything for you, you don’t need to know any programming (other than maybe basic syntax and basic math so that you can verify that the values are computed exactly the way you want it). If you want to write the results to a file instead of seeing it in a popup, you just tell the AI chatbot to do that. If you also want to make other measurements, such as measure distance between some points and the plane, etc., just tell it.</p>
<p>For example, you want to see the angle value in the node name? Let’s ask for it:</p>
<blockquote>
<p>Modify the code so that it writes the angle value into the name of the second plane node.</p>
</blockquote>
<p>Copilot generated an updated code snippet in 3 seconds, which again works flawlessly (I just changed the shortcut to <code>Ctrl-Q</code> because if you set the same keyboard shortcut to do two different things then it will become ambiguous and so it will be disabled).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80857ef88f82c92bfa751345becb38d6622664a1.png" data-download-href="/uploads/short-url/ikX83RekCTHBVa0DT2fI0G1muRP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80857ef88f82c92bfa751345becb38d6622664a1_2_355x500.png" alt="image" data-base62-sha1="ikX83RekCTHBVa0DT2fI0G1muRP" width="355" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80857ef88f82c92bfa751345becb38d6622664a1_2_355x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80857ef88f82c92bfa751345becb38d6622664a1_2_532x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80857ef88f82c92bfa751345becb38d6622664a1_2_710x1000.png 2x" data-dominant-color="1C202C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1277×1796 281 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<details>
<summary>
Code snippet generated by Microsoft Copilot</summary>
<pre data-code-wrap="python"><code class="lang-python">import slicer
from qt import QKeySequence, QShortcut, QMessageBox

def measure_angle_between_planes():
    # Get the plane nodes
    plane1 = slicer.mrmlScene.GetFirstNodeByName('P')
    plane2 = slicer.mrmlScene.GetFirstNodeByName('P_1')
    
    if not plane1 or not plane2:
        QMessageBox.warning(slicer.util.mainWindow(), 'Error', 'One or both planes not found.')
        return

    # Get the normal vectors of the planes
    normal1 = [0, 0, 0]
    normal2 = [0, 0, 0]
    plane1.GetNormal(normal1)
    plane2.GetNormal(normal2)

    # Calculate the angle between the normals
    import numpy as np
    dot_product = np.dot(normal1, normal2)
    norm1 = np.linalg.norm(normal1)
    norm2 = np.linalg.norm(normal2)
    angle_radians = np.arccos(dot_product / (norm1 * norm2))
    angle_degrees = np.degrees(angle_radians)

    # Write the angle value into the name of the second plane node
    plane2.SetName(f'P_1 (Angle: {angle_degrees:.2f} degrees)')

    # Display the angle in a popup window
    QMessageBox.information(slicer.util.mainWindow(), 'Angle Between Planes', f'The angle between the planes is: {angle_degrees:.2f} degrees')

# Create a shortcut for Ctrl-A to run the measurement
shortcut = QShortcut(QKeySequence("Ctrl+A"), slicer.util.mainWindow())
shortcut.activated.connect(measure_angle_between_planes)
</code></pre>
</details>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7af59451bbff9ff377f590d06d640b40f3d09017.png" data-download-href="/uploads/short-url/hxKoYg6cxAtiYXZR4PgKG21uEBx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7af59451bbff9ff377f590d06d640b40f3d09017_2_667x500.png" alt="image" data-base62-sha1="hxKoYg6cxAtiYXZR4PgKG21uEBx" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7af59451bbff9ff377f590d06d640b40f3d09017_2_667x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7af59451bbff9ff377f590d06d640b40f3d09017_2_1000x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7af59451bbff9ff377f590d06d640b40f3d09017_2_1334x1000.png 2x" data-dominant-color="50505D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1978×1482 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Konstantin (2024-12-19 05:59 UTC)

<p>Professor Lasso, thank you for your detailed answer!</p>

---

## Post #7 by @lassoan (2024-12-19 06:08 UTC)

<p>Please let us know how it all worked for you.</p>
<p>If we get positive feedback from you and other users then we may build in an AI assistant directly into Slicer. It would automate the steps that I described above: it would guide users through the process and would do all the copy-pasting of code snippets to the Python console and startup script.</p>

---

## Post #8 by @Konstantin (2024-12-21 07:46 UTC)

<p>Hello, Professor Lasso. I used your advice and encountered new difficulties:</p>
<ol>
<li>You can use the script to automatically measure the angle between two planes by writing the angle value into the plane name only once. If I want to measure this angle again, nothing will work (because the plane name changes by writing a number).</li>
<li>Is it possible to make it so that each measurement is written directly into the name of the “angle” in the “node”? For example, I measure the angle in the sagittal plane between the tibia (plane “P”) and talus (plane "P_1) and write this value into angle “A”. When measuring the angle in the sagittal plane between the tibia (plane “P”)  and calcaneus (plane “P_2”) , the resulting value is written into angle “A_1”. This would be very convenient.<br>
Thank you in advance for your answer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd9278862e77d392da3ec7e78bc3939c505730b7.png" data-download-href="/uploads/short-url/tkzH0uXDVn6hVOyHbgAdkaiiA1p.png?dl=1" title="3D SLICER" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd9278862e77d392da3ec7e78bc3939c505730b7_2_690x374.png" alt="3D SLICER" data-base62-sha1="tkzH0uXDVn6hVOyHbgAdkaiiA1p" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd9278862e77d392da3ec7e78bc3939c505730b7_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd9278862e77d392da3ec7e78bc3939c505730b7_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd9278862e77d392da3ec7e78bc3939c505730b7_2_1380x748.png 2x" data-dominant-color="CFD0E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D SLICER</span><span class="informations">1913×1039 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>

---

## Post #9 by @Konstantin (2024-12-22 06:29 UTC)

<p>I tried adding a command with the help of AI (ChatGPT) to make the results leak into the “angle”, but this script does not work. An error occurs that the program does not understand what an “angle” is.</p>

---
