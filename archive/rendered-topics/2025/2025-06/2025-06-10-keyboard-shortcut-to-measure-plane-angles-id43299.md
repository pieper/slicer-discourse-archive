# Keyboard shortcut to measure plane angles?

**Topic ID**: 43299
**Date**: 2025-06-10
**URL**: https://discourse.slicer.org/t/keyboard-shortcut-to-measure-plane-angles/43299

---

## Post #1 by @ben.rodwell (2025-06-10 22:54 UTC)

<p>I’m trying to make a keyboard shortcut to use the “Measure angle between two markup planes” script in the script repository so that I can quickly measure the angles between planes without having to copy and past the code into the python console every time. I’ve put the code below into my .slicerrc.py file but it does not seem to be working right now. The same script works when I paste it into the console but I cannot make the keyboard shortcut work. Does anyone know what I have done wrong?</p>
<pre><code class="lang-auto">planeNodeNames = ["P", "P_1"]

# Print angles between slice nodes
def ShowAngle(unused1=None, unused2=None):
  planeNormalVectors = []
  for planeNodeName in planeNodeNames:
    planeNode = slicer.util.getFirstNodeByClassByName("vtkMRMLMarkupsPlaneNode", planeNodeName)
    planeNormalVector = [0.0, 0.0, 0.0]
    planeNode.GetNormalWorld(planeNormalVector)
    planeNormalVectors.append(planeNormalVector)
  angleRad = vtk.vtkMath.AngleBetweenVectors(planeNormalVectors[0], planeNormalVectors[1])
  angleDeg = vtk.vtkMath.DegreesFromRadians(angleRad)
  print("Angle between planes {0} and {1} = {2:0.3f}".format(planeNodeNames[0], planeNodeNames[1], angleDeg))

# Observe plane node changes
for planeNodeName in planeNodeNames:
  planeNode = slicer.util.getFirstNodeByClassByName("vtkMRMLMarkupsPlaneNode", planeNodeName)
  planeNode.AddObserver(slicer.vtkMRMLMarkupsPlaneNode.PointModifiedEvent, ShowAngle)

# Print current angle
ShowAngle()


shortcuts = [
  ("Ctrl+d", lambda: ShowAngle())
  ]

for (shortcutKey, callback) in shortcuts:
  shortcut = qt.QShortcut(slicer.util.mainWindow())
  shortcut.setKey(qt.QKeySequence(shortcutKey))
  shortcut.connect( "activated()", callback)

</code></pre>

---
