# Write vtk file from mha volume input

**Topic ID**: 2684
**Date**: 2018-04-25
**URL**: https://discourse.slicer.org/t/write-vtk-file-from-mha-volume-input/2684

---

## Post #1 by @MGM (2018-04-25 12:45 UTC)

<p>Hi</p>
<p>I have a little question on vtk development</p>
<p>My input file is mha volume</p>
<pre><code>char volume_i[50];
char reader_i[50];
char writerVTK_i[50];
char out_file[50];


      sprintf(volume_i, "\nVolume %d", i);  
        printf("%s : %s \n", volume_i, argv[1]);

        vtkSmartPointer&lt;vtkImageData&gt; volume_i = vtkSmartPointer&lt;vtkImageData&gt;::New();

        sprintf(reader_i, "Reader %d", i); 

        vtkSmartPointer&lt;vtkMetaImageReader&gt; reader_i = vtkSmartPointer&lt;vtkMetaImageReader&gt;::New();

        reader_i-&gt;SetFileName(argv[1]);
        reader_i-&gt;Update();

        volume_i-&gt;DeepCopy(reader_i-&gt;GetOutput());
</code></pre>
<p>I would like to write vtk file as an output.</p>
<p>I tried this code :</p>
<pre><code>vtkSmartPointer&lt;vtkPolyDataWriter&gt; writerVTK_i = vtkSmartPointer&lt;vtkPolyDataWriter&gt;::New();

sprintf(out_file, "%d.vtk", i);  
printf("%s\n", out_file);
writerVTK_i-&gt;SetFileName(out_file);
writerVTK_i-&gt;SetInputConnection(volume_i-&gt;GetOutputPort());
writerVTK_i-&gt;Write();
</code></pre>
<p>Should I use vtkMetaImageWriter ?</p>
<p>Thank you</p>

---
