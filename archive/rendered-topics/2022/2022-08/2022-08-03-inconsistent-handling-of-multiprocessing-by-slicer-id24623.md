---
topic_id: 24623
title: "Inconsistent Handling Of Multiprocessing By Slicer"
date: 2022-08-03
url: https://discourse.slicer.org/t/24623
---

# Inconsistent handling of multiprocessing by slicer

**Topic ID**: 24623
**Date**: 2022-08-03
**URL**: https://discourse.slicer.org/t/inconsistent-handling-of-multiprocessing-by-slicer/24623

---

## Post #1 by @dvbower (2022-08-03 16:56 UTC)

<p>On a Windows 10 enterprise computer the following multiprocessing code block evaluates differently for two execution commands.  Executing the script directly with <code>PythonSlicer.exe</code> gives the expected result, i.e., output is reported for both <code>main</code> and <code>fun</code>.  However, executing the script with <code>slicer.exe --python-script [script]</code> only reports output from <code>main</code>, suggesting that <code>fun</code> has not been called, thereby implying a problem with the multiprocessing.  In contrast, on a Mac, both execution approaches (either using python directly, or piping through slicer) return output from both <code>main</code> and <code>fun</code>.</p>
<p>I mostly want to execute the python script using slicer.exe to access the ctk and slicer modules, which I don’t believe I can access from the PythonSlicer.exe python bundle.  Any suggestions are much appreciated.</p>
<pre><code>import sys
import time
from multiprocessing import Process

def fun():

    outfile = open('test_fun.log','w')
    print("Starting fun")
    outfile.write('Starting fun\n')
    time.sleep(2)
    outfile.write('Finishing fun')
    print('Finishing fun')
    outfile.close()

def main():

    p = Process(target=fun)
    p.start()
    p.join()

if __name__ == '__main__':

    print('Starting main')
    outfile = open('test_main.log', 'w')
    main()
    outfile.write('Yes in main()')
    outfile.close()
    print('Finishing main')
    sys.exit(0)
</code></pre>

---

## Post #2 by @pieper (2022-08-03 17:51 UTC)

<p>There could definitely be differences between <code>--python-script</code>, which happens in the slicer application main loop, and running in the <code>PythonSlicer</code> interpreter with regards to <code>multiprocessing</code>.  In the context of the Slicer main loop you might have more luck with <code>QProcess</code> like we use in the <a href="https://github.com/pieper/SlicerParallelProcessing">SlicerParallelProcessing</a> extension.</p>

---

## Post #3 by @dvbower (2022-08-04 08:02 UTC)

<p>Thanks I will check it out.</p>

---
