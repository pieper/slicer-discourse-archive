# Question About Using SimpleITK for Image Resampling

**Topic ID**: 41703
**Date**: 2025-02-14
**URL**: https://discourse.slicer.org/t/question-about-using-simpleitk-for-image-resampling/41703

---

## Post #1 by @Linjun_Yang (2025-02-14 16:04 UTC)

<p>It’s my first time to ask a question in 3D Slicer forum so please bear with me if I fail to follow some rules. Thanks in advance!</p>
<p>I am trying to use SimpleITK to resample a given CT image saved in Nifti format. The given CT image has been centered at world coordinate of (0, 0, 0) using my previous codes based on SimpleITK. I want to resample the image so that the <strong>resampled image is centered in a new grid defined using a target spacing (e.g., isotropic 1.0mm), size (e.g, 256x256x256)</strong>. <strong>My idea is to use the center of the given image in the world coordinate and half of each three target side length (spacing * size) to calculate the new origin. With the new origin as well as the target size and spacing (and direction matrix), one can define the output image grid</strong>. My code is as follow:</p>
<pre><code class="lang-auto">def is_orthogonal(matrix, tol=1e-6):
    identity = np.eye(matrix.shape[0])
    return np.allclose(matrix @ matrix.T, identity, atol=tol)

def resample_nifti_volume(img, target_spacing=[1.0, 1.0, 1.0], target_shape=(256, 256, 256)):
    data = img.get_fdata()
    affine = img.affine

    # Extract spacing and direction from affine
    spacing = np.sqrt(np.sum(affine[:3, :3] ** 2, axis=0))
    direction = affine[:3, :3] / spacing

    if not is_orthogonal(direction):
        print("Warning: Direction matrix is not orthogonal. Correcting...")
        direction, _ = np.linalg.qr(direction)

    # Convert to SimpleITK image
    sitk_img = sitk.GetImageFromArray(data)
    sitk_img.SetSpacing(spacing)
    sitk_img.SetOrigin(affine[:3, 3])
    sitk_img.SetDirection(direction.flatten())

    original_center = np.dot(affine, np.append(np.array(data.shape) / 2, 1))[:3]
    target_center = (np.array(target_shape) - 1) * np.array(target_spacing) / 2.0
    new_origin = original_center - np.dot(direction, target_center)

    resample = sitk.ResampleImageFilter()
    resample.SetOutputSpacing(target_spacing)
    resample.SetSize(target_shape)
    resample.SetInterpolator(sitk.sitkLinear)
    resample.SetOutputOrigin(new_origin)
    resample.SetOutputDirection(direction.flatten())

    resampled_img = resample.Execute(sitk_img)

    resampled_data = sitk.GetArrayFromImage(resampled_img)
    resampled_affine = np.eye(4)
    resampled_affine[:3, :3] = direction * target_spacing  # Properly scale direction by target spacing
    resampled_affine[:3, 3] = new_origin

    return nib.Nifti1Image(resampled_data, resampled_affine)
</code></pre>
<p>However, I got the following result, visualized using the 3D Slicer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c93189bdbf9fc14a0fec1f99882e39e0851e9e4.png" data-download-href="/uploads/short-url/8DRNC4MIP2PUQP7WXPHw8MV3W6g.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c93189bdbf9fc14a0fec1f99882e39e0851e9e4.png" alt="image" data-base62-sha1="8DRNC4MIP2PUQP7WXPHw8MV3W6g" width="412" height="413"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">412×413 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The desirable result is the one square centered at the image space, while the one using my code is not centered. I checked everything that I could check but have no idea how to fix this. I am pretty sure I should use the identity transform in the resampling image filter.</p>
<p>I hope someone can help me with this. My SimpleITK version is <strong>2.4.1</strong>.</p>
<p>Thanks!</p>

---
