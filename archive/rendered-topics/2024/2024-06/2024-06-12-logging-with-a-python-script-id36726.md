# Logging with a python script

**Topic ID**: 36726
**Date**: 2024-06-12
**URL**: https://discourse.slicer.org/t/logging-with-a-python-script/36726

---

## Post #1 by @RomanStriker (2024-06-12 14:59 UTC)

<p>I am trying to log the output of a python script to a file and the console. The code works fine when run in a normal python env but with slicer it does not log anything. The code is as follows.</p>
<pre><code class="lang-auto">import sys
import argparse
import logging

if __name__ == '__main__':
    # create args object
    args = argparse.Namespace(
        dataset_dir="test",
        log_file="debug.log"
    )

    fileHandler = logging.FileHandler(args.log_file, mode='a')
    consoleHandler = logging.StreamHandler(sys.stdout)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[fileHandler, consoleHandler ]
    )

    # print the arguments
    for arg in vars(args):
        logging.info(f"{arg}: {getattr(args, arg)}")

    logging.info('Starting the process...')
</code></pre>
<p>Normal output:</p>
<pre data-code-wrap="bash"><code class="lang-bash">python /home/user/test.py
2024-06-12 16:56:56,652 - INFO - dataset_dir: test
2024-06-12 16:56:56,652 - INFO - log_file: debug.log
2024-06-12 16:56:56,652 - INFO - Starting the process...
</code></pre>
<p>Slicer output:</p>
<pre data-code-wrap="bash"><code class="lang-bash">./Slicer --python-script /home/user/test.py
Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython
Failed to load vtkSlicerCrossSectionAnalysisModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython
  Error(s):
    CLI executable: /home/user/Slicer-5.6.2/slicer.org/Extensions-32448/SlicerVMTK/lib/Slicer-5.6/qt-loadable-modules/vtkvmtk.py
    The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.
Fail to instantiate module  "vtkvmtk"
The following modules failed to be instantiated:
   vtkvmtk
Switch to module:  "Welcome"
</code></pre>
<p>Do I need to add something extra for slicer?</p>

---
