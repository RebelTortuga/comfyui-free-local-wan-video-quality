# Detailed Options Guide

This guide explains the supplied workflow. Change one setting at a time and compare outputs using the same input image and seed. Save a copy before changing connections.

## Image and prompts

- **Input image:** choose the image you want edited or animated. No example photograph is bundled.
- **Positive prompt:** describe the edit or motion you want. Be specific about what should change.
- **Negative prompt:** describe unwanted features. Its influence depends on the model and guidance settings.
- **Prompt history:** positive and negative fields start blank. The history node can save and reuse prompt pairs; local history files are not included.

## Generation controls

| Control | Meaning | Practical effect |
| --- | --- | --- |
| Seed | Starting random state | Keep it fixed for comparisons; identical seeds do not guarantee identical results across hardware or software changes. |
| Steps | Sampling iterations | More steps usually take longer; more is not automatically better. |
| CFG | Prompt guidance strength | Higher values can strengthen prompt influence but may introduce artifacts. |
| Denoise | Amount of regeneration | Lower values tend to preserve more of the encoded input; behavior depends on the model and conditioning. |
| Sampler / scheduler | Sampling method and noise schedule | Keep supplied defaults for your first result. |
| Dimensions | Image or video size | Larger dimensions usually require more memory and time. |

## Supplied sampler settings

| Node | Steps | CFG | Sampler | Scheduler | Denoise |
| --- | --- | --- | --- | --- | --- |
| 3 | 30 | 5 | uni_pc | simple | 1 |

## Workflow-specific controls and behavior

1. Load a reference image and write the desired motion in the prompt-history node; prompts start blank.
2. Inspect PREPARED REFERENCE. Center cropping can remove parts of the head or hands.
3. Run with the supplied 480 × 768, 201-frame settings. At 24 fps, the nominal duration is 8.38 seconds.
4. Find the saved video under ComfyUI's output/video directory.

The graph uses 30 steps, CFG 5, uni_pc/simple, fixed seed 123456789 and tiled VAE decoding. Resolution, frame count, and available memory affect performance; no minimum VRAM or render time is certified here. For a quick trial, change BOTH image resize and latent dimensions to 480 × 768, set 49 frames and 16 steps. Use frame counts of the form 4n+1. For landscape, update both dimension pairs together.

The embedded shared note describes several presets; the actual settings above are authoritative. Higher-resolution execution has not been verified in this packaging session.


## Video controls

- **Frame count:** length in frames; nominal seconds equals frame count divided by fps. Use a count of the form 4n+1.
- **Frame rate:** playback speed in frames per second; the supplied value is 24.
- **Resize and latent dimensions:** keep these two dimension pairs matched.
- **Center crop:** fills the requested aspect ratio while preserving proportions, but can crop the subject.
- **Tiled VAE decode:** decodes in chunks to reduce decoding memory pressure; it does not guarantee the entire generation will fit.
- **SaveVideo:** writes the video using the supplied output prefix under ComfyUI's output directory.

## Verification limits

Graph references were checked. These settings are documented from the uploaded JSON; GPU rendering, timings, and minimum VRAM were not verified during packaging.
