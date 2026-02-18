# A warning in Python

**Topic ID**: 19752
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/a-warning-in-python/19752

---

## Post #1 by @4DUS (2021-09-20 00:02 UTC)

<p>Hi,</p>
<p>While opening a *.3dus files in a 3D Slicer, I receive the following warning in the Python Interactor tab:</p>
<p>\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\site-packages\numpy\ctypeslib.py:521: RuntimeWarning: A builtin ctypes object gave a PEP3118 format string that does not match its itemsize, so a best-guess will be made of the data type. Newer versions of python may behave correctly.<br>
return array(obj, copy=False)</p>
<p>The displayed images include a number of black pixels located at different regions of the images.<br>
Can you please explain how can it be fixed?</p>

---

## Post #2 by @lassoan (2021-10-17 23:52 UTC)

<p>How did you acquire the *. 3dus file? What ultrasound system and transducer was used?</p>

---

## Post #3 by @4DUS (2021-10-24 11:59 UTC)

<p>Hello Andras,</p>
<p>Thank you for your response.</p>
<p>The *.3dus file was acquired as a DICOM and its extension was changed to the *.3dus.<br>
The system in use was Vivid S70N and the transducer was a NuVera 4D intracardiac catheter.<br>
A similar acquisition with E95 system hasn’t resulted in an error.</p>

---
