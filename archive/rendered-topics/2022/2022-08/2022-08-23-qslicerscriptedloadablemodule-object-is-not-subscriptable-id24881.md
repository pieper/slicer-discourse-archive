---
topic_id: 24881
title: "Qslicerscriptedloadablemodule Object Is Not Subscriptable"
date: 2022-08-23
url: https://discourse.slicer.org/t/24881
---

# 'qSlicerScriptedLoadableModule' object is not subscriptable

**Topic ID**: 24881
**Date**: 2022-08-23
**URL**: https://discourse.slicer.org/t/qslicerscriptedloadablemodule-object-is-not-subscriptable/24881

---

## Post #1 by @Doodads (2022-08-23 10:21 UTC)

<p>Hi all,</p>
<p>The following error was printed in the python interactor upon start-up after I added a custom module path to Slicer.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "~/CreateMesh/CreateMesh.py", line 43, in __init__
    self.smoothN = meshparams["smoothNumberOfIterations"]
TypeError: 'qSlicerScriptedLoadableModule' object is not subscriptable
TypeError: module() argument 'name' must be str, not qSlicerScriptedLoadableModule
</code></pre>
<p>Does anyone know what is the reason for this error? Below is a snippet of the custom module. Many thanks!</p>
<pre><code class="lang-auto">import numpy as np
import copy
import logging
import vtk, qt, slicer
from slicer.ScriptedLoadableModule import *
from ExtractCenterline import ExtractCenterlineLogic


class CreateMesh:

    def __init__(self, meshparams={}):
          self.modelNodes = None
          self.imageNodes = None
          self.centerlines = None
          self.surface = None
          self.surfacePolyData = None
          self.mesh = None
          self.prevCenterlines = None
          self.prevSurface = None
          self.prevMesh = None
          self.meshErrorsMarkupsNode = None
          self.endPointsMarkupsNode = None
          self.inputSurfaceForCenterline = None
          self.networkPolyData = None
          self.networkModelNode = None
          self.networkCurveNode = None
          self.networkPropertiesTableNode = None
          self.centerlineModelNode = None
          self.centerlineCurveNode = None
          self.centerlinePropertiesTableNode = None
          self.voronoiDiagramModelNode = None
          self.clMaker = ExtractCenterlineLogic()
          self.meshMaker = CreateMeshLogic()

          self.smoothN = meshparams["smoothNumberOfIterations"]
</code></pre>

---
