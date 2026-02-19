---
topic_id: 29823
title: "Matlab Variable To 3D Slicer"
date: 2023-06-04
url: https://discourse.slicer.org/t/29823
---

# MATLAB variable to 3D slicer

**Topic ID**: 29823
**Date**: 2023-06-04
**URL**: https://discourse.slicer.org/t/matlab-variable-to-3d-slicer/29823

---

## Post #1 by @Sbeta (2023-06-04 12:48 UTC)

<p>I am a new learner. I have processed the 3D PET image variable in .mat format and I want to download it as a volume in the 3D slicer for registration with CT. How to do that while keeping the same voxel size of 3D PET? Thanks</p>

---

## Post #2 by @lassoan (2023-06-04 12:58 UTC)

<p>You can use a standard 3D image file format that stores the image geometry (origin, spacing, axis directions). You can use this nrrd writer: <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m" class="inline-onebox">SlicerMatlabBridge/nrrdwrite.m at master · PerkLab/SlicerMatlabBridge · GitHub</a></p>

---

## Post #3 by @Sbeta (2023-06-14 03:50 UTC)

<p>Thank you for that, but I tried to convert them into .dcm by the below code. However, when loading the processed PET image ‘convolvedPET’, 3D slicer shows the scalar range (14.65 to 4.761x 10^7)  in Matlab for convolvedPET.mat has range (4.3x10^-5 tp 684). Please let me the problem or may be I am not aware of something.<br>
Here is the code,</p>
<pre><code class="lang-auto"> %% Section 1 PET original image in DICOM
folderPath = 'PET';
filePattern = fullfile(folderPath, 'IMG-0001-*.dcm');
dcmFiles = dir(filePattern);
numSlices = numel(dcmFiles);
PET = zeros(256, 256, numSlices);
metadataArray = cell(numSlices, 1); % Array to store metadata
for i = 1:numSlices
    fileName = fullfile(folderPath, dcmFiles(i).name);
    info = dicominfo(fileName);
    PET(:, :, i) = dicomread(info);
    metadataArray{i} = info; % Save metadata in the array
end
PET=double(PET); 
 **PET was resized and convolved to get a processed PET image named  'convolvedPET'** 
%% write dicom files and save in a folder 
outputFolderPath = 'Processed_PET';
if ~isfolder(outputFolderPath)
    mkdir(outputFolderPath);
end
% dicom write 
for i = 1:numSlices
    % Retrieve the processed data for the current slice
    processedData = convolvedPET(:, :, i);
   
    % Retrieve the metadata for the current slice
  originalMetadata = metadataArray{i};
   
    % Update the rows and columns in the metadata
    originalMetadata.Rows = size(processedData, 1);
   originalMetadata.Columns = size(processedData, 2);
   
    % Update the pixel spacing in the metadata (assuming the new spacing is 3.0 mm)
   originalMetadata.PixelSpacing = [3.0, 3.0];
   
    % Save the processed data with the updated metadata
    outputFileName = fullfile(outputFolderPath, ['processed_', dcmFiles(i).name]);
    dicomwrite(processedData, outputFileName, originalMetadata,'CreateMode','copy');
end
</code></pre>

---

## Post #4 by @Sbeta (2023-10-27 01:56 UTC)

<p>Thank you. I used that, but when I get the image in the 3D slicer its orientation changes. Please advise on dealing with this</p>

---

## Post #5 by @lassoan (2023-10-27 03:42 UTC)

<p>In files, the world coordinate system is LPS; while internally in Slicer the world coordinate system is RAS. However, this should not cause any problems, as Slicer converts everything from LPS to RAS coordinate system (images, models, transforms, etc.) when reading data from file.</p>

---
