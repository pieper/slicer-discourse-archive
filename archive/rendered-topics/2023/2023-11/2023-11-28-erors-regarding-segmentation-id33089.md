# Erors regarding segmentation

**Topic ID**: 33089
**Date**: 2023-11-28
**URL**: https://discourse.slicer.org/t/erors-regarding-segmentation/33089

---

## Post #1 by @segmentator (2023-11-28 15:17 UTC)

<p>Hello,</p>
<p>My PC does the segmantation in about 75 seconds, but then I get multiple errors during extraction of features. Also, this error doesn’t happen in another PC that I tried.</p>
<p>Here is the log:</p>
<pre><code class="lang-auto">Requirement already satisfied: pillow&lt;10.1 in c:\users\ali doruk\appdata\local\slicer.org\slicer 5.6.0\lib\python\lib\site-packages (10.0.1)
WARNING: There was an error checking the latest version of pip.
C:/Users/Ali Doruk/AppData/Local/slicer.org/Slicer 5.6.0/slicer.org/Extensions-32390/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:880: UserWarning: 'has_cuda' is deprecated, please use 'torch.backends.cuda.is_built()'
  cuda = torch.cuda if torch.has_cuda and torch.cuda.is_available() else None
.......[VTK] RadiomicsCLI standard error:
[VTK] [2023-11-28 10:45:04] I: radiomics.script: Starting PyRadiomics (version: v3.1.0)
[VTK] [2023-11-28 10:45:04] I: radiomics.script: Processing input...
[VTK] [2023-11-28 10:45:04] E: radiomics.script: Error extracting features!
[VTK] Traceback (most recent call last):
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 135, in run
[VTK]     results = self._processCases(caseGenerator)
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 233, in _processCases
[VTK]     setting_overrides = self._parseOverrides()
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353, in _parseOverrides
[VTK]     settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1105, in safe_load
[VTK]     error_deprecation('safe_load', 'load', arg="typ='safe', pure=True")
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1037, in error_deprecation
[VTK]     raise AttributeError(s)
[VTK] AttributeError: 
[VTK] "safe_load()" has been removed, use
[VTK] 
[VTK]   yaml = YAML(typ='safe', pure=True)
[VTK]   yaml.load(...)
[VTK] 
[VTK] instead of file "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353
[VTK] 
[VTK]       settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
[VTK] 
[VTK] 
.Done
[2023-11-28 10:45:04] I: radiomics.script: Starting PyRadiomics (version: v3.1.0)
[2023-11-28 10:45:04] I: radiomics.script: Processing input...
[2023-11-28 10:45:04] E: radiomics.script: Error extracting features!
Traceback (most recent call last):
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 135, in run
    results = self._processCases(caseGenerator)
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 233, in _processCases
    setting_overrides = self._parseOverrides()
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353, in _parseOverrides
    settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1105, in safe_load
    error_deprecation('safe_load', 'load', arg="typ='safe', pure=True")
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1037, in error_deprecation
    raise AttributeError(s)
AttributeError: 
"safe_load()" has been removed, use

  yaml = YAML(typ='safe', pure=True)
  yaml.load(...)

instead of file "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353

      settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']



..[VTK] RadiomicsCLI standard error:
[VTK] [2023-11-28 10:45:07] I: radiomics.script: Starting PyRadiomics (version: v3.1.0)
[VTK] [2023-11-28 10:45:07] I: radiomics.script: Processing input...
[VTK] [2023-11-28 10:45:07] E: radiomics.script: Error extracting features!
[VTK] Traceback (most recent call last):
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 135, in run
[VTK]     results = self._processCases(caseGenerator)
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 233, in _processCases
[VTK]     setting_overrides = self._parseOverrides()
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353, in _parseOverrides
[VTK]     settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1105, in safe_load
[VTK]     error_deprecation('safe_load', 'load', arg="typ='safe', pure=True")
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1037, in error_deprecation
[VTK]     raise AttributeError(s)
[VTK] AttributeError: 
[VTK] "safe_load()" has been removed, use
[VTK] 
[VTK]   yaml = YAML(typ='safe', pure=True)
[VTK]   yaml.load(...)
[VTK] 
[VTK] instead of file "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353
[VTK] 
[VTK]       settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
[VTK] 
[VTK] 
..Done
[2023-11-28 10:45:07] I: radiomics.script: Starting PyRadiomics (version: v3.1.0)
[2023-11-28 10:45:07] I: radiomics.script: Processing input...
[2023-11-28 10:45:07] E: radiomics.script: Error extracting features!
Traceback (most recent call last):
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 135, in run
    results = self._processCases(caseGenerator)
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 233, in _processCases
    setting_overrides = self._parseOverrides()
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353, in _parseOverrides
    settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1105, in safe_load
    error_deprecation('safe_load', 'load', arg="typ='safe', pure=True")
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1037, in error_deprecation
    raise AttributeError(s)
AttributeError: 
"safe_load()" has been removed, use

  yaml = YAML(typ='safe', pure=True)
  yaml.load(...)

instead of file "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353

      settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']



..[VTK] RadiomicsCLI standard error:
[VTK] [2023-11-28 10:45:10] I: radiomics.script: Starting PyRadiomics (version: v3.1.0)
[VTK] [2023-11-28 10:45:10] I: radiomics.script: Processing input...
[VTK] [2023-11-28 10:45:10] E: radiomics.script: Error extracting features!
[VTK] Traceback (most recent call last):
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 135, in run
[VTK]     results = self._processCases(caseGenerator)
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 233, in _processCases
[VTK]     setting_overrides = self._parseOverrides()
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353, in _parseOverrides
[VTK]     settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1105, in safe_load
[VTK]     error_deprecation('safe_load', 'load', arg="typ='safe', pure=True")
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1037, in error_deprecation
[VTK]     raise AttributeError(s)
[VTK] AttributeError: 
[VTK] "safe_load()" has been removed, use
[VTK] 
[VTK]   yaml = YAML(typ='safe', pure=True)
[VTK]   yaml.load(...)
[VTK] 
[VTK] instead of file "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353
[VTK] 
[VTK]       settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
[VTK] 
[VTK] 
.Done
[2023-11-28 10:45:10] I: radiomics.script: Starting PyRadiomics (version: v3.1.0)
[2023-11-28 10:45:10] I: radiomics.script: Processing input...
[2023-11-28 10:45:10] E: radiomics.script: Error extracting features!
Traceback (most recent call last):
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 135, in run
    results = self._processCases(caseGenerator)
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 233, in _processCases
    setting_overrides = self._parseOverrides()
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353, in _parseOverrides
    settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1105, in safe_load
    error_deprecation('safe_load', 'load', arg="typ='safe', pure=True")
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1037, in error_deprecation
    raise AttributeError(s)
AttributeError: 
"safe_load()" has been removed, use

  yaml = YAML(typ='safe', pure=True)
  yaml.load(...)

instead of file "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353

      settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']



..[VTK] RadiomicsCLI standard error:
[VTK] [2023-11-28 10:45:12] I: radiomics.script: Starting PyRadiomics (version: v3.1.0)
[VTK] [2023-11-28 10:45:12] I: radiomics.script: Processing input...
[VTK] [2023-11-28 10:45:12] E: radiomics.script: Error extracting features!
[VTK] Traceback (most recent call last):
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 135, in run
[VTK]     results = self._processCases(caseGenerator)
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 233, in _processCases
[VTK]     setting_overrides = self._parseOverrides()
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353, in _parseOverrides
[VTK]     settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1105, in safe_load
[VTK]     error_deprecation('safe_load', 'load', arg="typ='safe', pure=True")
[VTK]   File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1037, in error_deprecation
[VTK]     raise AttributeError(s)
[VTK] AttributeError: 
[VTK] "safe_load()" has been removed, use
[VTK] 
[VTK]   yaml = YAML(typ='safe', pure=True)
[VTK]   yaml.load(...)
[VTK] 
[VTK] instead of file "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353
[VTK] 
[VTK]       settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
[VTK] 
[VTK] 
..Done
[2023-11-28 10:45:12] I: radiomics.script: Starting PyRadiomics (version: v3.1.0)
[2023-11-28 10:45:12] I: radiomics.script: Processing input...
[2023-11-28 10:45:12] E: radiomics.script: Error extracting features!
Traceback (most recent call last):
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 135, in run
    results = self._processCases(caseGenerator)
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 233, in _processCases
    setting_overrides = self._parseOverrides()
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353, in _parseOverrides
    settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1105, in safe_load
    error_deprecation('safe_load', 'load', arg="typ='safe', pure=True")
  File "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py", line 1037, in error_deprecation
    raise AttributeError(s)
AttributeError: 
"safe_load()" has been removed, use

  yaml = YAML(typ='safe', pure=True)
  yaml.load(...)

instead of file "C:\Users\Ali Doruk\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts\__init__.py", line 353

      settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']

</code></pre>

---
