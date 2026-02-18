# Trying to load .nii file generated with Nipype

**Topic ID**: 6611
**Date**: 2019-04-26
**URL**: https://discourse.slicer.org/t/trying-to-load-nii-file-generated-with-nipype/6611

---

## Post #1 by @quentinfrancois0 (2019-04-26 02:25 UTC)

<p>Dear all,</p>
<p>I’m new on Slicer after some work with Nipype. I would like to display the results of my work which is a registration between a T1 and a Scan of the same patient on Slicer. Nipype workflow generates a .nii file. I tried to import it with the Add data function of Slicer and when I press the OK button of the window nothing happens, no message in the bottom box. I looked for research ideas on internet but I found nothing. I’m sorry but I don’t have any information about the import error. I see nothing in the bottom console of Slicer.</p>
<p>Could you help me with research ideas to solve the problem ? Search in the header of .nii ? Specific generation of .nii with Nipype ?</p>
<p>Thanks in advance for your help</p>
<p>Quentin</p>

---

## Post #2 by @lassoan (2019-04-26 12:56 UTC)

<p>Is there any error in the application log? If not, then you need to share an example file so that we can investigate the problem.</p>

---

## Post #3 by @quentinfrancois0 (2019-04-26 14:44 UTC)

<p>I just found the log of the error. It is weird that I can display the file with matplotlib in python through Nipype and that Slicer says the file does not exist. Please see below :</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /Users/quentinfrancois/Documents/Robeaut�/brain_imaging/results/registrationT1Scan/result.0.nii does not exist.</p>
<p>Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(0x7fa6150ec7e0) returned failure for request: vtkInformation (0x600001400240)<br>
Debug: Off<br>
Modified Time: 2787208<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /Users/quentinfrancois/Documents/Robeaut�/brain_imaging/results/registrationT1Scan/result.0.nii does not exist.</p>
<p>Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries(0x7fa6150e9070) returned failure for request: vtkInformation (0x6000017fce40)<br>
Debug: Off<br>
Modified Time: 2788701<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file /Users/quentinfrancois/Documents/Robeaut�/brain_imaging/results/registrationT1Scan/result.0.nii does not exist.</p>
<p>Algorithm vtkITKArchetypeImageSeriesScalarReader(0x7fa6150e6c50) returned failure for request: vtkInformation (0x6000017fee00)<br>
Debug: Off<br>
Modified Time: 2789484<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0</p>
<p>ReadData: This is not a nrrd file</p>
<p>ReadData: Cannot read file as a volume of type DiffusionTensorVolume[fullName = /Users/quentinfrancois/Documents/Robeaut�/brain_imaging/results/registrationT1Scan/result.0.nii]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 0 files.<br>
File reader used the archetype file name of /Users/quentinfrancois/Documents/Robeaut�/brain_imaging/results/registrationT1Scan/result.0.nii []<br>
FileNotFoundError</p>
<p>ReadData: This is not a nrrd file</p>
<p>ReadData: Failed to instantiate a file reader</p>
<p>ReadData: Cannot read file as a volume of type Volume[fullName = /Users/quentinfrancois/Documents/Robeaut�/brain_imaging/results/registrationT1Scan/result.0.nii]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 0 files.<br>
File reader used the archetype file name of /Users/quentinfrancois/Documents/Robeaut�/brain_imaging/results/registrationT1Scan/result.0.nii []<br>
FileNotFoundError</p>
<p>Quentin FRANCOIS</p>
<p><a href="mailto:quentinfrancois0@gmail.com">quentinfrancois0@gmail.com</a></p>

---

## Post #4 by @lassoan (2019-04-26 15:15 UTC)

<p>You need to save the file in a path that does not contain special characters.</p>

---

## Post #5 by @quentinfrancois0 (2019-05-02 15:34 UTC)

<p>Dear Andras,</p>
<p>It was so easy. Sorry for the basic question.</p>
<p>Thanks for your help, it worked directly !</p>
<p>Quentin FRANCOIS</p>
<p><a href="mailto:quentinfrancois0@gmail.com">quentinfrancois0@gmail.com</a></p>

---
