---
topic_id: 176
title: "Loading Volume From Dat File Format"
date: 2017-04-23
url: https://discourse.slicer.org/t/176
---

# Loading volume from .dat file format

**Topic ID**: 176
**Date**: 2017-04-23
**URL**: https://discourse.slicer.org/t/loading-volume-from-dat-file-format/176

---

## Post #1 by @lassoan (2017-04-23 11:05 UTC)

<p>(question moved from slicer-users)</p>
<p>Can I load the .dat datasets <a href="https://www.cg.tuwien.ac.at/research/vis/datasets">https://www.cg.tuwien.ac.at/research/vis/datasets</a> in 3d slicer ? Or can I convert it to some other format supported by 3d slicer?</p>

---

## Post #2 by @lassoan (2017-04-23 11:27 UTC)

<p>The simplest is to create a text file in that describes the image in one of the standard formats, for example <a href="http://teem.sourceforge.net/nrrd/format.html">NRRD</a>.</p>
<p>For example, to load the <a href="https://www.cg.tuwien.ac.at/research/publications/2005/dataset-stagbeetle/">Stag beetle</a> data set, create a text file named <code>stagbeetle.nhdr</code> in the same directory as the .vol file with the following content:</p>
<pre><code>NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: unsigned short
dimension: 3
space: left-posterior-superior
sizes: 832 832 494
space directions: (1,0,0) (0,1,0) (0,0,1)
kinds: domain domain domain
endian: little
encoding: raw
space origin: (0,0,0)
byte skip: 6
data file: stagbeetle832x832x494.dat
</code></pre>
<p>To load the data set in Slicer, drag-and-drop the .nhdr file into the Slicer application window.</p>

---
