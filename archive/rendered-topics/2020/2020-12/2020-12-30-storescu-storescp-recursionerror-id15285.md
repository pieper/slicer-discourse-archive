# Storescu storescp RecursionError

**Topic ID**: 15285
**Date**: 2020-12-30
**URL**: https://discourse.slicer.org/t/storescu-storescp-recursionerror/15285

---

## Post #1 by @fuentesdt (2020-12-30 04:08 UTC)

<p>Hi, i’m trying to load my dicom into the Slicer dicom listener</p>
<p>storescu -aec storescp localhost 11112 dicomdir/*.dcm</p>
<p>Slicer-4.11.20200930-linux-amd64 on ubuntu 16.04</p>
<p>but am getting this RecursionError below?</p>
<pre><code class="lang-auto">Switch to module:  "Welcome"
Switch to module:  "DICOM"
DICOM C-Store SCP service started at port 11112
"DICOM indexer has successfully processed 1 files [0.01s]"
"DICOM indexer has successfully processed 1 files [0.00s]"
"DICOM indexer has successfully inserted 3 files [0.09s]"
"DICOM indexer has successfully processed 1 files [0.09s]"
"DICOM indexer has successfully inserted 1 files [0.05s]"
"DICOM indexer has successfully processed 1 files [0.05s]"
"DICOM indexer has updated display fields for 0 files [0.12s]"
"DICOM indexer has successfully processed 1 files [0.00s]"
</code></pre>
<p>.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
                                                                                                                       
File "/opt/apps/slicer/Slicer-4.11.20200930-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 325, in readFromStandardOutput                                                                                                                                                "DICOM indexer has updated display fields for 0 files [0.11s]"                                                                                         "DICOM indexer has successfully processed 1 files [0.00s]"                                                                                                 
super(DICOMListener,self).readFromStandardOutput(readLineCallback=self.processStdoutLine)                                                            
File "/opt/apps/slicer/Slicer-4.11.20200930-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMProcesses.py", line 267, in readFromStandardOutput                                                                                                                                                    logging.debug("Output from %s: %s" % (self.__class__.__name__, "\n".join(lines)))                                                                    
File "/opt/apps/slicer/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/logging/__init__.py", line 1912, in debug                               root.debug(msg, *args, **kwargs)                                                                                                                     
File "/opt/apps/slicer/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/logging/__init__.py", line 1296, in debug                               self._log(DEBUG, msg, args, **kwargs)                                                                                                                
File "/opt/apps/slicer/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/logging/__init__.py", line 1443, in _log                                exc_info, func, extra, sinfo)                                                                                                                        
File "/opt/apps/slicer/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/logging/__init__.py", line 1413, in makeRecord                          sinfo)                                                                                                                                               
File "/opt/apps/slicer/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/logging/__init__.py", line 281, in __init__                             self.levelname = getLevelName(level)                                                                                                               
RecursionError: maximum recursion depth exceeded                                                                                                       
"DICOM indexer has successfully inserted 2 files [0.
</code></pre>

---

## Post #2 by @lassoan (2020-12-30 05:02 UTC)

<p>I cannot reproduce the problem on Windows or Linux. Could you do some investigation on your own (the DICOM listener is just a Python file, you can add more logs or comment out code to see what goes wrong)?</p>

---

## Post #3 by @fuentesdt (2020-12-30 14:38 UTC)

<p>thank you for your time trying to reproduce this. Slicer design patterns have been the starting point for all imaging projects. This seems to get further for smaller image transfers. I’m trying to load ~1200 dicom images at a time from a dce study. My .sql database files are also on a network file system. I’ve found that the sql load breaks on some configurations of the network files systems. I’ll try to change to local disk and debug further.</p>

---

## Post #4 by @lassoan (2020-12-30 15:09 UTC)

<p>Yes, indeed Slicer DICOM database must be on a local disk. We don’t know exactly what is wrong with virtual and network drives, but we heard from several users that they had problems with those.</p>

---
