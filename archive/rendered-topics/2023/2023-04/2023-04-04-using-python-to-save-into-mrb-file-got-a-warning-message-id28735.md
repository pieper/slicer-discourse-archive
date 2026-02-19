---
topic_id: 28735
title: "Using Python To Save Into Mrb File Got A Warning Message"
date: 2023-04-04
url: https://discourse.slicer.org/t/28735
---

# Using python to save into .mrb file, got a warning message

**Topic ID**: 28735
**Date**: 2023-04-04
**URL**: https://discourse.slicer.org/t/using-python-to-save-into-mrb-file-got-a-warning-message/28735

---

## Post #1 by @derekcbr (2023-04-04 03:09 UTC)

<p>output_file = os.path.join(file_dir, “test.mrb”)<br>
licer.util.saveScene(output_file)<br>
I got the warnings from Slicer:[Qt] class QList&lt;class qSlicerFileWriter *&gt; __cdecl qSlicerCoreIOManagerPrivate::writers(const class QString &amp;,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLScene *) const warning: Unable to find node with ID “” in the given scene.<br>
How to solve this problem? Thanks a lot!</p>

---

## Post #2 by @pieper (2023-04-04 20:28 UTC)

<p>Try with incremental amounts of data in the scene.  First empty, then with sample data, etc. and see what steps lead to a scene that leads to the error and let us know.</p>

---

## Post #3 by @derekcbr (2023-04-05 14:09 UTC)

<p>Thank you for the message. First empty and then with sample data, I still got the same warnings. Thanks!</p>

---

## Post #4 by @pieper (2023-04-05 14:17 UTC)

<p>Thanks for the report.  I see that warning too, testing with my local build on mac.  But at least for me <code>slicer.util.loadScene</code> reads back the file as expected so I think you can ignore the warning.</p>
<p>It would be good if you could file an issue on github for this and ideally someone with a debug build can step through and figure out why this is being triggered.</p>

---

## Post #5 by @derekcbr (2023-04-05 23:13 UTC)

<p>Alright! Thank you for the message!</p>

---
