# Is there an issue with Linux builds currently?

**Topic ID**: 43743
**Date**: 2025-07-16
**URL**: https://discourse.slicer.org/t/is-there-an-issue-with-linux-builds-currently/43743

---

## Post #1 by @chir.set (2025-07-16 15:13 UTC)

<p>Hello,</p>
<p>There are no Linux builds for Slicer preview and no extensions since a few days.</p>
<p>Slicer clean-built today (<code>e1881207</code>) on Arch runs (<code>--ignore-slicerrc</code>) suspiciously with the following in stdout:</p>
<pre><code class="lang-auto">QFont::fromString: Invalid description 'Noto Sans,11,-1,5,400,0,0,0,0,0,0,0,0,0,0,1'
Traceback (most recent call last):
  File "&lt;string&gt;", line 5, in &lt;module&gt;
  File "&lt;string&gt;", line 212, in &lt;module&gt;
  File "&lt;string&gt;", line 177, in __init__
AttributeError: module 'qt' has no attribute 'QTimer'
Traceback (most recent call last):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/CropVolumeSequence.py", line 24, in __init__
    ScriptedLoadableModule.__init__(self, parent)
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/ScriptedLoadableModule.py", line 41, in __init__
    parent.icon = qt.QIcon(iconPath)
                  ^^^^^^^^
AttributeError: module 'qt' has no attribute 'QIcon'
qSlicerPythonCppAPI::instantiateClass  - [ "CropVolumeSequence" ] - Failed to instantiate scripted pythonqt class "CropVolumeSequence" 0x55a11b00b450
Fail to instantiate module  "CropVolumeSequence"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOM.py", line 12, in &lt;module&gt;
    import DICOMLib
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/__init__.py", line 1, in &lt;module&gt;
    from .DICOMProcesses import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 39, in &lt;module&gt;
    class DICOMProcess:
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 85, in DICOMProcess
    def start(self, cmd: str, args: list[str]) -&gt; qt.QProcess:
                                                  ^^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QProcess'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOM.py"  as module "DICOM" !
Fail to instantiate module  "DICOM"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMEnhancedUSVolumePlugin.py", line 5, in &lt;module&gt;
    from DICOMLib import DICOMPlugin
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/__init__.py", line 1, in &lt;module&gt;
    from .DICOMProcesses import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 39, in &lt;module&gt;
    class DICOMProcess:
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 85, in DICOMProcess
    def start(self, cmd: str, args: list[str]) -&gt; qt.QProcess:
                                                  ^^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QProcess'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMEnhancedUSVolumePlugin.py"  as module "DICOMEnhancedUSVolumePlugin" !
Fail to instantiate module  "DICOMEnhancedUSVolumePlugin"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMGeAbusPlugin.py", line 11, in &lt;module&gt;
    from DICOMLib import DICOMPlugin
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/__init__.py", line 1, in &lt;module&gt;
    from .DICOMProcesses import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 39, in &lt;module&gt;
    class DICOMProcess:
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 85, in DICOMProcess
    def start(self, cmd: str, args: list[str]) -&gt; qt.QProcess:
                                                  ^^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QProcess'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMGeAbusPlugin.py"  as module "DICOMGeAbusPlugin" !
Fail to instantiate module  "DICOMGeAbusPlugin"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMImageSequencePlugin.py", line 9, in &lt;module&gt;
    from DICOMLib import DICOMPlugin
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/__init__.py", line 1, in &lt;module&gt;
    from .DICOMProcesses import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 39, in &lt;module&gt;
    class DICOMProcess:
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 85, in DICOMProcess
    def start(self, cmd: str, args: list[str]) -&gt; qt.QProcess:
                                                  ^^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QProcess'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMImageSequencePlugin.py"  as module "DICOMImageSequencePlugin" !
Fail to instantiate module  "DICOMImageSequencePlugin"
Traceback (most recent call last):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMPatcher.py", line 24, in __init__
    ScriptedLoadableModule.__init__(self, parent)
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/ScriptedLoadableModule.py", line 41, in __init__
    parent.icon = qt.QIcon(iconPath)
                  ^^^^^^^^
AttributeError: module 'qt' has no attribute 'QIcon'
qSlicerPythonCppAPI::instantiateClass  - [ "DICOMPatcher" ] - Failed to instantiate scripted pythonqt class "DICOMPatcher" 0x55a11b0223f0
Fail to instantiate module  "DICOMPatcher"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 13, in &lt;module&gt;
    from DICOMLib import DICOMPlugin
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/__init__.py", line 1, in &lt;module&gt;
    from .DICOMProcesses import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 39, in &lt;module&gt;
    class DICOMProcess:
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 85, in DICOMProcess
    def start(self, cmd: str, args: list[str]) -&gt; qt.QProcess:
                                                  ^^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QProcess'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMScalarVolumePlugin.py"  as module "DICOMScalarVolumePlugin" !
Fail to instantiate module  "DICOMScalarVolumePlugin"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMSlicerDataBundlePlugin.py", line 8, in &lt;module&gt;
    from DICOMLib import DICOMPlugin
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/__init__.py", line 1, in &lt;module&gt;
    from .DICOMProcesses import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 39, in &lt;module&gt;
    class DICOMProcess:
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 85, in DICOMProcess
    def start(self, cmd: str, args: list[str]) -&gt; qt.QProcess:
                                                  ^^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QProcess'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMSlicerDataBundlePlugin.py"  as module "DICOMSlicerDataBundlePlugin" !
Fail to instantiate module  "DICOMSlicerDataBundlePlugin"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMVolumeSequencePlugin.py", line 9, in &lt;module&gt;
    from DICOMLib import DICOMPlugin
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/__init__.py", line 1, in &lt;module&gt;
    from .DICOMProcesses import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 39, in &lt;module&gt;
    class DICOMProcess:
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 85, in DICOMProcess
    def start(self, cmd: str, args: list[str]) -&gt; qt.QProcess:
                                                  ^^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QProcess'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DICOMVolumeSequencePlugin.py"  as module "DICOMVolumeSequencePlugin" !
Fail to instantiate module  "DICOMVolumeSequencePlugin"
Traceback (most recent call last):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/DataProbe.py", line 41, in __init__
    if not slicer.app.commandOptions().noMainWindow:
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: qSlicerCommandOptions has no attribute named 'noMainWindow'
qSlicerPythonCppAPI::instantiateClass  - [ "DataProbe" ] - Failed to instantiate scripted pythonqt class "DataProbe" 0x55a11b63dc60
Fail to instantiate module  "DataProbe"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/ExtensionWizard.py", line 14, in &lt;module&gt;
    from ExtensionWizardLib import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/ExtensionWizardLib/__init__.py", line 4, in &lt;module&gt;
    from .DirectoryListWidget import DirectoryListWidget
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/ExtensionWizardLib/DirectoryListWidget.py", line 36, in &lt;module&gt;
    class DirectoryListWidget(qt.QWidget):
                              ^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QWidget'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/ExtensionWizard.py"  as module "ExtensionWizard" !
Fail to instantiate module  "ExtensionWizard"
Traceback (most recent call last):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/LandmarkRegistration.py", line 14, in __init__
    ScriptedLoadableModule.__init__(self, parent)
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/ScriptedLoadableModule.py", line 41, in __init__
    parent.icon = qt.QIcon(iconPath)
                  ^^^^^^^^
AttributeError: module 'qt' has no attribute 'QIcon'
qSlicerPythonCppAPI::instantiateClass  - [ "LandmarkRegistration" ] - Failed to instantiate scripted pythonqt class "LandmarkRegistration" 0x55a11b79e340
Fail to instantiate module  "LandmarkRegistration"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 5, in &lt;module&gt;
    import DICOMLib
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/__init__.py", line 1, in &lt;module&gt;
    from .DICOMProcesses import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 39, in &lt;module&gt;
    class DICOMProcess:
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 85, in DICOMProcess
    def start(self, cmd: str, args: list[str]) -&gt; qt.QProcess:
                                                  ^^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QProcess'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/MultiVolumeImporterPlugin.py"  as module "MultiVolumeImporterPlugin" !
Fail to instantiate module  "MultiVolumeImporterPlugin"
Traceback (most recent call last):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SampleData.py", line 102, in __init__
    if not slicer.app.commandOptions().noMainWindow:
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: qSlicerCommandOptions has no attribute named 'noMainWindow'
qSlicerPythonCppAPI::instantiateClass  - [ "SampleData" ] - Failed to instantiate scripted pythonqt class "SampleData" 0x55a11b8fa740
Fail to instantiate module  "SampleData"
Traceback (most recent call last):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/ScreenCapture.py", line 25, in __init__
    ScriptedLoadableModule.__init__(self, parent)
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/ScriptedLoadableModule.py", line 41, in __init__
    parent.icon = qt.QIcon(iconPath)
                  ^^^^^^^^
AttributeError: module 'qt' has no attribute 'QIcon'
qSlicerPythonCppAPI::instantiateClass  - [ "ScreenCapture" ] - Failed to instantiate scripted pythonqt class "ScreenCapture" 0x55a11b891f80
Fail to instantiate module  "ScreenCapture"
Traceback (most recent call last):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SegmentEditor.py", line 13, in __init__
    ScriptedLoadableModule.__init__(self, parent)
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/ScriptedLoadableModule.py", line 41, in __init__
    parent.icon = qt.QIcon(iconPath)
                  ^^^^^^^^
AttributeError: module 'qt' has no attribute 'QIcon'
qSlicerPythonCppAPI::instantiateClass  - [ "SegmentEditor" ] - Failed to instantiate scripted pythonqt class "SegmentEditor" 0x55a11b925d60
Fail to instantiate module  "SegmentEditor"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SegmentStatistics.py", line 281, in &lt;module&gt;
    class SegmentStatisticsParameterEditorDialog(qt.QDialog):
                                                 ^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QDialog'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SegmentStatistics.py"  as module "SegmentStatistics" !
Fail to instantiate module  "SegmentStatistics"
Traceback (most recent call last):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SimpleFilters.py", line 69, in __init__
    parent.icon = qt.QIcon("%s/ITK.png" % self.ICON_DIR)
                  ^^^^^^^^
AttributeError: module 'qt' has no attribute 'QIcon'
qSlicerPythonCppAPI::instantiateClass  - [ "SimpleFilters" ] - Failed to instantiate scripted pythonqt class "SimpleFilters" 0x55a11b97fdc0
Fail to instantiate module  "SimpleFilters"
Traceback (most recent call last):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/SurfaceToolbox.py", line 18, in __init__
    ScriptedLoadableModule.__init__(self, parent)
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/ScriptedLoadableModule.py", line 41, in __init__
    parent.icon = qt.QIcon(iconPath)
                  ^^^^^^^^
AttributeError: module 'qt' has no attribute 'QIcon'
qSlicerPythonCppAPI::instantiateClass  - [ "SurfaceToolbox" ] - Failed to instantiate scripted pythonqt class "SurfaceToolbox" 0x55a11b9b86c0
Fail to instantiate module  "SurfaceToolbox"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;frozen importlib._bootstrap_external&gt;", line 999, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 488, in _call_with_frames_removed
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/VectorToScalarVolume.py", line 12, in &lt;module&gt;
    from slicer.parameterNodeWrapper import parameterNodeWrapper
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/parameterNodeWrapper/__init__.py", line 6, in &lt;module&gt;
    from .guiConnectors import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/parameterNodeWrapper/guiConnectors.py", line 19, in &lt;module&gt;
    from . import parameterPack as pack
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/parameterNodeWrapper/parameterPack.py", line 11, in &lt;module&gt;
    from .serializers import (
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/parameterNodeWrapper/serializers.py", line 424, in &lt;module&gt;
    class QColorSerializer(Serializer):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/parameterNodeWrapper/serializers.py", line 444, in QColorSerializer
    def write(self, parameterNode, name: str, value : qt.QColor) -&gt; None:
                                                      ^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QColor'
loadSourceAsModule - Failed to load file "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/VectorToScalarVolume.py"  as module "VectorToScalarVolume" !
Fail to instantiate module  "VectorToScalarVolume"
Traceback (most recent call last):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/../lib/Slicer-5.9/qt-scripted-modules/WebServer.py", line 30, in __init__
    ScriptedLoadableModule.__init__(self, parent)
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/ScriptedLoadableModule.py", line 41, in __init__
    parent.icon = qt.QIcon(iconPath)
                  ^^^^^^^^
AttributeError: module 'qt' has no attribute 'QIcon'
qSlicerPythonCppAPI::instantiateClass  - [ "WebServer" ] - Failed to instantiate scripted pythonqt class "WebServer" 0x55a11ba5e7c0
Fail to instantiate module  "WebServer"
The following modules failed to be instantiated:
   DICOMEnhancedUSVolumePlugin
   SampleData
   DICOMVolumeSequencePlugin
   DICOMSlicerDataBundlePlugin
   SurfaceToolbox
   CropVolumeSequence
   DICOM
   WebServer
   SegmentEditor
   ScreenCapture
   ExtensionWizard
   LandmarkRegistration
   SimpleFilters
   VectorToScalarVolume
   MultiVolumeImporterPlugin
   SegmentStatistics
   DICOMGeAbusPlugin
   DICOMScalarVolumePlugin
   DataProbe
   DICOMImageSequencePlugin
   DICOMPatcher
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/SubjectHierarchyLib/__init__.py", line 3, in &lt;module&gt;
    from . import parameterNodeWrapper  # Required to ensure parameterNodeWrapper plugins are registered
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/SubjectHierarchyLib/parameterNodeWrapper/__init__.py", line 3, in &lt;module&gt;
    from .guiConnectors import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/SubjectHierarchyLib/parameterNodeWrapper/guiConnectors.py", line 2, in &lt;module&gt;
    from slicer.parameterNodeWrapper import (
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/parameterNodeWrapper/__init__.py", line 6, in &lt;module&gt;
    from .guiConnectors import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/parameterNodeWrapper/guiConnectors.py", line 19, in &lt;module&gt;
    from . import parameterPack as pack
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/parameterNodeWrapper/parameterPack.py", line 11, in &lt;module&gt;
    from .serializers import (
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/parameterNodeWrapper/serializers.py", line 424, in &lt;module&gt;
    class QColorSerializer(Serializer):
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/bin/Python/slicer/parameterNodeWrapper/serializers.py", line 444, in QColorSerializer
    def write(self, parameterNode, name: str, value : qt.QColor) -&gt; None:
                                                      ^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QColor'
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/SegmentEditorEffects/__init__.py", line 16, in &lt;module&gt;
    from .SegmentEditorThresholdEffect import *
  File "/opt/programs/Slicer-5.9.0-2025-07-16-linux-amd64/lib/Slicer-5.9/qt-scripted-modules/SegmentEditorEffects/SegmentEditorThresholdEffect.py", line 995, in &lt;module&gt;
    class HistogramEventFilter(qt.QObject):
                               ^^^^^^^^^^
AttributeError: module 'qt' has no attribute 'QObject'
Switch to module:  "Volumes"
Wayland does not support QWindow::requestActivate()
Switch to module:  ""
Switch to module:  ""
</code></pre>
<p>It’s not usable obviously.</p>
<p>Are there know issues for Linux builds? May we expect ‘business as usual’ soon?</p>
<p>Thank you.</p>

---

## Post #2 by @jamesobutler (2025-07-17 00:25 UTC)

<p>See the following details below. It appears there may be an issue specific to Linux builds that is not being observed for Windows or macOS builds.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8565">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8565" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8565" target="_blank" rel="noopener nofollow ugc">BUG: Revert Python initialization change that breaks PythonQt integration</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>jcfr:revert-pyconfig-init-qt-breakage</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-07-14" data-time="15:13:35" data-timezone="UTC">03:13PM - 14 Jul 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 11 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8565/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1</span>
            <span class="removed">-11</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This reverts commit 3bace0b4b6 ("ENH: Update Python initialization to use PyConf<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8565" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ig API", 2025-07-03)

The commit replaced the deprecated `Py_NoUserSiteDirectory` global flag with `PyConfig`-based initialization (PEP 587). While forward-looking, the change caused Slicer to fail at startup due to broken PythonQt integration. For example, `qt.QTimer` and `qt.QIcon` became unavailable.

Additionally, over 100 Python and C++ tests fail (`ctest`) due to incomplete or incorrect initialization of the embedded interpreter.

Until proper support for `PyConfig` is implemented in coordination with PythonQt, this reverts to using `Py_NoUserSiteDirectory` to restore expected behavior.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @chir.set (2025-07-17 08:26 UTC)

<p>Thanks for the link. After reverting the referenced commit, Slicer builds and runs fine.</p>
<p>(There’s a new issue regarding VMTK and ITK, that’s another headache.)</p>

---

## Post #4 by @jcfr (2025-07-17 18:05 UTC)

<p>Thanks for your patience <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=14" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>
<p>A pull request fixing the python initialization has just been published <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=14" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>
<p>See <a href="https://github.com/Slicer/Slicer/pull/8582">PR#8582</a></p>
<hr>
<p>Fixes regression introduced in:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/commit/7a26aa1b8748f1813d7206a9911c90987d563ad2">7a26aa1</a> (“ENH: Update Python initialization for compatibility with isolated mode”)</li>
<li><a href="https://github.com/Slicer/Slicer/commit/3bace0b4b61a1feaed10bdfd407d6fe0d07948c4">3bace0b</a> (“ENH: Update Python initialization to use PyConfig API”)</li>
</ul>
<p>These changes inadvertently introduced multiple and inconsistent Python initializations by removing the use of deprecated symbols (<code>PySys_SetArgvEx</code>, <code>Py_NoUserSiteDirectory</code>) without fully replicating their intended behavior. As a result, over 100 tests failed (e.g., <code>AttributeError: module 'qt' has no attribute 'QTimer'</code> on Ubuntu) due to Python being initialized both too late and with conflicting settings.</p>
<p>This commit restores correct initialization behavior by:</p>
<ol>
<li>Initializing Python early in <code>qSlicerCorePythonManager</code> using the <code>PyConfig</code> API. Rather than explicitly setting <code>config.isolated = 0</code>, this relies on the default (non-isolated) mode established by <code>Py_InitializeFromConfig</code>, which ensures that environment variables and site directories are respected. Early initialization ensures Python is ready before QApplication starts.</li>
<li>Preventing re-initialization by <code>PythonQt</code> by setting the <code>PythonAlreadyInitialized</code> flag. The previously required clearing of the <code>IgnoreSiteModule</code> flag is no longer necessary, as <code>PythonQt</code> no longer manages initialization.</li>
<li>Moving argument population (<code>PyConfig_SetArgv</code>) and interpreter config update (<code>_PyInterpreterState_SetConfig</code>) into <code>qSlicerCoreApplication::handleCommandLineArguments()</code> to occur after command-line arguments are fully known.</li>
</ol>
<p>This approach ensures consistent interpreter state across embedded Python and PythonQt integration, and aligns with the best practices of the <code>PyConfig</code> API.</p>

---

## Post #5 by @jcfr (2025-07-17 18:07 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="43743">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>There’s a new issue regarding VMTK and ITK, that’s another headache.</p>
</blockquote>
</aside>
<p>Do you have more details about this ?</p>
<p>Also, I suggest you base your build on the linked pull request that should be integrated into <code>main</code> shortly.</p>

---

## Post #6 by @jcfr (2025-07-17 18:14 UTC)

<p>For reference, here is the corresponding VMTK issue:</p>
<ul>
<li><a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/162" class="inline-onebox">VMTK libs build failure · Issue #162 · vmtk/SlicerExtension-VMTK · GitHub</a></li>
</ul>

---

## Post #7 by @chir.set (2025-07-17 18:31 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="43743">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>I suggest you base your build on the linked pull request that should be integrated into <code>main</code> shortly.</p>
</blockquote>
</aside>
<p>Thank you for considering both issues. My last build at <code>407906c367</code> does not yet include PR <a href="https://github.com/Slicer/Slicer/pull/8582" rel="noopener nofollow ugc">8582</a>.</p>
<p>I’ll keep you updated tomorrow.</p>
<p>Regards.</p>

---

## Post #8 by @chir.set (2025-07-18 07:23 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="7" data-topic="43743">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I’ll keep you updated tomorrow.</p>
</blockquote>
</aside>
<p>Unfortunately, Slicer does not start with a usable result when built at 533859698. The VMTK issue (related or not) persists.</p>
<p>Here is a trimmed <code>stdout</code> (too long for the editor) with <code>--ignore-slicerrc</code> from the build tree:</p>
<pre><code class="lang-auto">QFont::fromString: Invalid description 'Noto Sans,11,-1,5,400,0,0,0,0,0,0,0,0,0,0,1'
Traceback (most recent call last):
  File "&lt;string&gt;", line 5, in &lt;module&gt;
  File "&lt;string&gt;", line 12, in &lt;module&gt;
  File "/home/arc/src/Slicer-SuperBuild9/Slicer-build/bin/Python/slicer/__init__.py", line 218, in &lt;module&gt;
    import scipy.linalg  # noqa: F401
    ^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/linalg/__init__.py", line 205, in &lt;module&gt;
    from ._basic import *
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/linalg/_basic.py", line 13, in &lt;module&gt;
    from ._decomp import _asarray_validated
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/linalg/_decomp.py", line 26, in &lt;module&gt;
    from scipy._lib._util import _asarray_validated
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/_lib/_util.py", line 18, in &lt;module&gt;
    from scipy._lib._array_api import array_namespace
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/_lib/_array_api.py", line 17, in &lt;module&gt;
    from scipy._lib.array_api_compat import (
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/_lib/array_api_compat/numpy/__init__.py", line 1, in &lt;module&gt;
    from numpy import *
  File "&lt;frozen importlib._bootstrap&gt;", line 1410, in _handle_fromlist
  File "&lt;frozen importlib._bootstrap&gt;", line 1412, in _handle_fromlist
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/__init__.py", line 352, in __getattr__
    import numpy.testing as testing
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/testing/__init__.py", line 11, in &lt;module&gt;
    from ._private.utils import *
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1393, in &lt;module&gt;
    _SUPPORTS_SVE = check_support_sve()
                    ^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1387, in check_support_sve
    output = subprocess.run(cmd, capture_output=True, text=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/subprocess.py", line 550, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/subprocess.py", line 1209, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/subprocess.py", line 2153, in _communicate
    stdout = self._translate_newlines(stdout,
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/subprocess.py", line 1086, in _translate_newlines
    data = data.decode(encoding, errors)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 12: ordinal not in range(128)
decoding with 'ANSI_X3.4-1968' codec failed
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
NameError: name 'getSlicerRCFileName' is not defined
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/arc/src/Slicer-SuperBuild9/Slicer-build/bin/Python/slicer/__init__.py", line 218, in &lt;module&gt;
    import scipy.linalg  # noqa: F401
    ^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/linalg/__init__.py", line 205, in &lt;module&gt;
    from ._basic import *
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/linalg/_basic.py", line 13, in &lt;module&gt;
    from ._decomp import _asarray_validated
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/linalg/_decomp.py", line 26, in &lt;module&gt;
    from scipy._lib._util import _asarray_validated
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/_lib/_util.py", line 18, in &lt;module&gt;
    from scipy._lib._array_api import array_namespace
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/_lib/_array_api.py", line 17, in &lt;module&gt;
    from scipy._lib.array_api_compat import (
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/_lib/array_api_compat/numpy/__init__.py", line 1, in &lt;module&gt;
    from numpy import *
  File "&lt;frozen importlib._bootstrap&gt;", line 1410, in _handle_fromlist
  File "&lt;frozen importlib._bootstrap&gt;", line 1412, in _handle_fromlist
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/__init__.py", line 352, in __getattr__
    import numpy.testing as testing
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/testing/__init__.py", line 11, in &lt;module&gt;
    from ._private.utils import *
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1393, in &lt;module&gt;
    _SUPPORTS_SVE = check_support_sve()
                    ^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1387, in check_support_sve
    output = subprocess.run(cmd, capture_output=True, text=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/subprocess.py", line 550, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/subprocess.py", line 1209, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/subprocess.py", line 2153, in _communicate
    stdout = self._translate_newlines(stdout,
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/subprocess.py", line 1086, in _translate_newlines
    data = data.decode(encoding, errors)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 12: ordinal not in range(128)
decoding with 'ANSI_X3.4-1968' codec failed
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/arc/src/Slicer-SuperBuild9/Slicer-build/bin/Python/slicer/__init__.py", line 218, in &lt;module&gt;
    import scipy.linalg  # noqa: F401
    ^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/linalg/__init__.py", line 205, in &lt;module&gt;
    from ._basic import *
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/linalg/_basic.py", line 13, in &lt;module&gt;
    from ._decomp import _asarray_validated
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/linalg/_decomp.py", line 26, in &lt;module&gt;
    from scipy._lib._util import _asarray_validated
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/_lib/_util.py", line 18, in &lt;module&gt;
    from scipy._lib._array_api import array_namespace
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/_lib/_array_api.py", line 17, in &lt;module&gt;
    from scipy._lib.array_api_compat import (
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/scipy/_lib/array_api_compat/numpy/__init__.py", line 1, in &lt;module&gt;
    from numpy import *
  File "&lt;frozen importlib._bootstrap&gt;", line 1410, in _handle_fromlist
  File "&lt;frozen importlib._bootstrap&gt;", line 1412, in _handle_fromlist
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/__init__.py", line 352, in __getattr__
    import numpy.testing as testing
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/testing/__init__.py", line 11, in &lt;module&gt;
    from ._private.utils import *
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1393, in &lt;module&gt;
    _SUPPORTS_SVE = check_support_sve()
                    ^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1387, in check_support_sve
    output = subprocess.run(cmd, capture_output=True, text=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/subprocess.py", line 550, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</code></pre>

---

## Post #9 by @chir.set (2025-07-18 13:24 UTC)

<p>Here is the output when starting in <code>C.UTF-8</code> locale:</p>
<pre><code class="lang-auto">QT_QPA_PLATFORM="xcb" LANG=C.UTF-8 LC_ALL=C.UTF-8 src/Slicer-SuperBuild9/Slicer-build/Slicer
QFont::fromString: Invalid description 'Noto Sans,11,-1,5,400,0,0,0,0,0,0,0,0,0,0,1'
Switch to module:  "Volumes"
Loading Slicer RC file [/home/user/.slicerrc.py]
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;string&gt;", line 129, in loadSlicerRCFile
  File "/home/arc/src/Slicer-SuperBuild9/python-install/lib/python3.12/encodings/ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 22744: ordinal not in range(128)
</code></pre>
<p>If I add <code>--ignore-slicerrc</code>:</p>
<pre><code class="lang-auto">QFont::fromString: Invalid description 'Noto Sans,11,-1,5,400,0,0,0,0,0,0,0,0,0,0,1'
Switch to module:  "Volumes"
</code></pre>
<p>(I don’t know yet if Slicer is usable since I’m currently doing that remotely.)</p>

---

## Post #10 by @chir.set (2025-07-18 13:40 UTC)

<p>Further tests:</p>
<p>The default locale of the environment is <code>fr_FR.UTF-8</code>, which is the only locale active in <code>/etc/locale.gen</code>.</p>
<p>The bunch of decode errors before loading <code>.slicerrc.py</code> occur with the default locale in the environment or on the command line.</p>
<p>They do not appear with anything else : <code>{C,en_US,ar_BH,so_SO}.UTF-8</code>. None of these have been generated by <code>locale-gen</code> which is from the <code>glibc</code> package.</p>

---

## Post #11 by @chir.set (2025-07-19 09:51 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="9" data-topic="43743">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>(I don’t know yet if Slicer is usable since I’m currently doing that remotely.)</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a><br>
It’s usable, but like a disabled person.</p>
<p>It must be started with a locale that has not been generated for glibc. Modules are functional, even Python modules, but the rc file fails to load (a major limitation for me).</p>

---

## Post #12 by @jcfr (2025-07-22 05:31 UTC)

<p>Following the upgrade of the Linux build environment, the Preview build should be available for download tomorrow:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/slicer-build-environment-upgraded-to-qt5-almalinux8-gcc14/43802" class="inline-onebox">Slicer Build Environment Upgraded to `qt5-almalinux8-gcc14`</a></li>
</ul>

---

## Post #13 by @chir.set (2025-07-22 07:12 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="12" data-topic="43743">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>the Preview build should be available for download tomorrow:</p>
</blockquote>
</aside>
<p>Great and thanks <a class="mention" href="/u/jcfr">@jcfr</a>.</p>
<p>There’s still one last step <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3870655" rel="noopener nofollow ugc">issue</a> however.</p>

---

## Post #14 by @jcfr (2025-07-22 07:46 UTC)

<p>Root cause has been identified and build environment will be updated later today.</p>

---
