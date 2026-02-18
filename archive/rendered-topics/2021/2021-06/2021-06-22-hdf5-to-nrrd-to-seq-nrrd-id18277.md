# Hdf5 to NRRD to SEQ.NRRD

**Topic ID**: 18277
**Date**: 2021-06-22
**URL**: https://discourse.slicer.org/t/hdf5-to-nrrd-to-seq-nrrd/18277

---

## Post #1 by @Jamal_K (2021-06-22 18:13 UTC)

<p>I have an hdf5 4D Volume rendering with 1 dimension begin time. I transformed this file using python into an NRRD for Slicer to read it. I then added the ‘seq’ label to the file as mentioned here (<a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/Sequences" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.10/Extensions/Sequences - Slicer Wiki</a>) so that it is a sequence.</p>
<p>When I load this data file into Slicer and set it as a sequence it gives me the following error:<br>
Error: Loading /path/rec07_61982292_uint8_x42y73z304t962_data.nrrd - Failed to read node rec07_61982292_uint8_x42y73z304t962_data_1 (vtkMRMLSequenceNode1) from filename=’/path/rec07_61982292_uint8_x42y73z304t962_data.nrrd’</p>

---

## Post #2 by @lassoan (2021-06-22 23:58 UTC)

<p>Can you copy here the Python code that you used for conversion?<br>
It would also help a lot if you could share an example nrrd file (upload somewhere and post the link here).</p>

---

## Post #3 by @Jamal_K (2021-06-25 21:52 UTC)

<p>The data I have is for a specific patient so given confidentiality, I cannot share it, however here is the code for a file xyz.hdf5, I tried to print as much info as possible. If there anything else I can provide please tell me to.</p>
<pre><code class="lang-auto">#importing
import h5py
import nrrd
import numpy as np

#Read the hdf5 file
f = h5py.File('xyz.hdf5','r')
print('File name is:')
print(f.name)

print('File keys are:')
print(list(f.keys()))
</code></pre>
<p>Out:<br>
File name is:<br>
/<br>
File keys are:<br>
[‘volume’]</p>
<pre><code class="lang-auto">#Slicing file into ndarray
data = f['volume'][:10]
print(data.shape)
</code></pre>
<p>Out:<br>
(10, 42, 73, 304)</p>
<pre><code class="lang-auto">#Copying data to NRRD file (readable by Slicer)
f_nrrd_name = 'xyz.nrrd'
nrrd.write(f_nrrd_name, data, index_order = 'C')
# Read the data back from file
readdata, header = nrrd.read(f_nrrd_name)
print(readdata.shape)
</code></pre>
<p>Out:<br>
(304, 73, 42, 10)</p>

---

## Post #4 by @lassoan (2021-06-25 22:23 UTC)

<p>You can write a valid seq.nrrd file from an <code>img</code> numpy array of size <code>(26, 102, 102, 61)</code> (corresponds to number of volumes, colums, rows, slices):</p>
<pre><code class="lang-python">import nrrd
header = {
    'type': 'int',
    'dimension': 4,
    'space': 'right-anterior-superior',
    'space directions': [[     float('nan'),      float('nan'),      float('nan')], [1.953125, 0.      , 0.      ], [0.      , 1.953125, 0.      ], [0.      , 0.      , 1.953125]],
    'kinds': ['list', 'domain', 'domain', 'domain'],
    'labels': ['frame', '', '', ''], 
    'endian': 'little',
    'encoding': 'raw',
    'space origin': [-137.16099548,  -36.80649948, -309.71899414],
    'measurement frame': [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]],
    'axis 0 index type': 'numeric',
    'axis 0 index values': '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25'
}
nrrd.write("c:/tmp/test.seq.nrrd", img, header)
</code></pre>

---
