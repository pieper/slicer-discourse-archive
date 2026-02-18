#  I can't segment the model

**Topic ID**: 31289
**Date**: 2023-08-22
**URL**: https://discourse.slicer.org/t/i-cant-segment-the-model/31289

---

## Post #1 by @JOSE_LUIS_CORRAL_PUM (2023-08-22 14:25 UTC)

<p>Operating system: Windows 10<br>
Procesador	AMD Ryzen 5 7600X 6-Core Processor                4.70 GHz<br>
RAM instalada	32,0 GB (31,1 GB usable)<br>
Tipo de sistema	Sistema operativo de 64 bits, procesador basado en x64</p>
<p>Slicer version:5.4.0 r31938 / 311cb26</p>
<p>Expected behavior: Total segmentation<br>
Actual behavior: Nothing segments me after the process.<br>
I need help please</p>
<p>This text appears in the console<br>
Processing started</p>
<p>Writing input file to C:/Users/azken/AppData/Local/Temp/Slicer/__SlicerTemp__2023-08-22_10+45+43.576/total-segmentator-input.nii</p>
<p>Creating segmentations with TotalSegmentator AI…</p>
<p>Total Segmentator arguments: [‘-i’, ‘C:/Users/azken/AppData/Local/Temp/Slicer/__SlicerTemp__2023-08-22_10+45+43.576/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/azken/AppData/Local/Temp/Slicer/__SlicerTemp__2023-08-22_10+45+43.576/segmentation’, ‘–ml’, ‘–task’, ‘total’]</p>
<p>C:\Users\azken\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator:5: DeprecationWarning: pkg_resources is deprecated as an API. See <a href="https://setuptools.pypa.io/en/latest/pkg_resources.html" class="inline-onebox" rel="noopener nofollow ugc">Package Discovery and Resource Access using pkg_resources - setuptools 68.1.2.post20230818 documentation</a></p>
<p>from pkg_resources import require</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>preprocessing C:\Users\azken\AppData\Local\Temp\nnunet_tmp_bjfhqiz5\s01.nii.gz</p>
<p>using preprocessor GenericPreprocessor</p>
<p>before crop: (1, 109, 77, 77) after crop: (1, 109, 77, 77) spacing: [1.5 1.5 1.5]</p>
<p>no resampling necessary</p>
<p>no resampling necessary</p>
<p>before: {‘spacing’: array([1.5, 1.5, 1.5]), ‘spacing_transposed’: array([1.5, 1.5, 1.5]), ‘data.shape (data is transposed)’: (1, 109, 77, 77)}</p>
<p>after: {‘spacing’: array([1.5, 1.5, 1.5]), ‘data.shape (data is resampled)’: (1, 109, 77, 77)}</p>
<p>(1, 109, 77, 77)</p>
<p>This worker has ended successfully, no errors to report</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>force_separate_z: None interpolation order: 0</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>preprocessing C:\Users\azken\AppData\Local\Temp\nnunet_tmp_bjfhqiz5\s01.nii.gz</p>
<p>using preprocessor GenericPreprocessor</p>
<p>before crop: (1, 109, 77, 77) after crop: (1, 109, 77, 77) spacing: [1.5 1.5 1.5]</p>
<p>no resampling necessary</p>
<p>no resampling necessary</p>
<p>before: {‘spacing’: array([1.5, 1.5, 1.5]), ‘spacing_transposed’: array([1.5, 1.5, 1.5]), ‘data.shape (data is transposed)’: (1, 109, 77, 77)}</p>
<p>after: {‘spacing’: array([1.5, 1.5, 1.5]), ‘data.shape (data is resampled)’: (1, 109, 77, 77)}</p>
<p>(1, 109, 77, 77)</p>
<p>This worker has ended successfully, no errors to report</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>force_separate_z: None interpolation order: 0</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>preprocessing C:\Users\azken\AppData\Local\Temp\nnunet_tmp_bjfhqiz5\s01.nii.gz</p>
<p>using preprocessor GenericPreprocessor</p>
<p>before crop: (1, 109, 77, 77) after crop: (1, 109, 77, 77) spacing: [1.5 1.5 1.5]</p>
<p>no resampling necessary</p>
<p>no resampling necessary</p>
<p>before: {‘spacing’: array([1.5, 1.5, 1.5]), ‘spacing_transposed’: array([1.5, 1.5, 1.5]), ‘data.shape (data is transposed)’: (1, 109, 77, 77)}</p>
<p>after: {‘spacing’: array([1.5, 1.5, 1.5]), ‘data.shape (data is resampled)’: (1, 109, 77, 77)}</p>
<p>(1, 109, 77, 77)</p>
<p>This worker has ended successfully, no errors to report</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>force_separate_z: None interpolation order: 0</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>preprocessing C:\Users\azken\AppData\Local\Temp\nnunet_tmp_bjfhqiz5\s01.nii.gz</p>
<p>using preprocessor GenericPreprocessor</p>
<p>before crop: (1, 109, 77, 77) after crop: (1, 109, 77, 77) spacing: [1.5 1.5 1.5]</p>
<p>no resampling necessary</p>
<p>no resampling necessary</p>
<p>before: {‘spacing’: array([1.5, 1.5, 1.5]), ‘spacing_transposed’: array([1.5, 1.5, 1.5]), ‘data.shape (data is transposed)’: (1, 109, 77, 77)}</p>
<p>after: {‘spacing’: array([1.5, 1.5, 1.5]), ‘data.shape (data is resampled)’: (1, 109, 77, 77)}</p>
<p>(1, 109, 77, 77)</p>
<p>This worker has ended successfully, no errors to report</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>force_separate_z: None interpolation order: 0</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>preprocessing C:\Users\azken\AppData\Local\Temp\nnunet_tmp_bjfhqiz5\s01.nii.gz</p>
<p>using preprocessor GenericPreprocessor</p>
<p>before crop: (1, 109, 77, 77) after crop: (1, 109, 77, 77) spacing: [1.5 1.5 1.5]</p>
<p>no resampling necessary</p>
<p>no resampling necessary</p>
<p>before: {‘spacing’: array([1.5, 1.5, 1.5]), ‘spacing_transposed’: array([1.5, 1.5, 1.5]), ‘data.shape (data is transposed)’: (1, 109, 77, 77)}</p>
<p>after: {‘spacing’: array([1.5, 1.5, 1.5]), ‘data.shape (data is resampled)’: (1, 109, 77, 77)}</p>
<p>(1, 109, 77, 77)</p>
<p>This worker has ended successfully, no errors to report</p>
<p>Please cite the following paper when using nnUNet:</p>
<p>Isensee, F., Jaeger, P.F., Kohl, S.A.A. et al. “nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation.” Nat Methods (2020). <a href="https://doi.org/10.1038/s41592-020-01008-z" class="inline-onebox" rel="noopener nofollow ugc">nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation | Nature Methods</a></p>
<p>If you have questions or suggestions, feel free to open an issue at <a href="https://github.com/MIC-DKFZ/nnUNet" class="inline-onebox" rel="noopener nofollow ugc">GitHub - MIC-DKFZ/nnUNet</a></p>
<p>force_separate_z: None interpolation order: 0</p>
<p>If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" class="inline-onebox" rel="noopener nofollow ugc">[2208.05868] TotalSegmentator: robust segmentation of 104 anatomical structures in CT images</a></p>
<p>Resampling…</p>
<p>Resampled in 0.92s</p>
<p>Predicting part 1 of 5 …</p>
<p>Predicting part 2 of 5 …</p>
<p>Predicting part 3 of 5 …</p>
<p>Predicting part 4 of 5 …</p>
<p>Predicting part 5 of 5 …</p>
<p>Predicted in 21.36s</p>
<p>Resampling…</p>
<p>Saving segmentations…</p>
<p>Saved in 0.17s</p>
<p>Importing segmentation results…</p>
<p>Cleaning up temporary folder…</p>
<p>Processing completed in 26.22 seconds</p>
<p>Processing finished.</p>

---
