<!-- rebeltortuga-banner:start -->
<p align="center"><img src="https://raw.githubusercontent.com/RebelTortuga/RebelTortuga/main/assets/RebelTortuga-Neon-Watermarked.webp" alt="RebelTortuga neon turtle watermarked banner" width="100%"></p>

<p align="center">
<a href="https://rebeltortuga.github.io/">Website</a> · <a href="https://github.com/RebelTortuga">GitHub</a> · <a href="https://www.twitch.tv/rebeltortuga">Twitch</a> · <a href="https://www.youtube.com/channel/UCpMIirV8w5RfVd9TpKpA2pQ">YouTube</a> · <a href="https://www.patreon.com/cw/RebelTortuga">Patreon</a> · <a href="https://ko-fi.com/rebeltortuga">Ko-fi</a>
</p>

<!-- rebeltortuga-banner:end -->

# Free Local Wan Video — Quality

**Workflow by:** RebelTortuga  
**Platform:** Local ComfyUI; prepared for a Windows setup, including Stability Matrix  
**Cost:** Free to use. No payment, paid API, subscription, or generation credits are required by this workflow.

**A note from RebelTortuga:** I put this workflow together to animate a reference image using free, local AI, with the source image and motion prompts close together and the main generation settings easy to find. I’m sharing it free with the community. Suggestions, new feature ideas, and constructive feedback are welcome.

Wan 2.2 image-to-video generation at 480 × 768, with 201 frames at 24 fps.

This is an independent community workflow, not an official product of the ComfyUI or model developers. Model weights and custom nodes are installed separately. You need suitable hardware, storage, and electricity; paid cloud hosting is not required. Results and performance depend on your setup.

## Free Local AI — No Paid Service Required

**Price: $0 for this workflow.** It runs image/video inference on your own computer with locally installed models. The provided graph has **no paid API calls, subscription requirement, credit balance, or required account with a hosted generator**.

- Download and import the included `workflow.json` at no charge.
- Install ComfyUI, the listed free custom nodes, and compatible local model files separately.
- You need a capable GPU, disk space, and electricity; model and component licenses still apply.
- Optional third-party hosting or services are **not part of this workflow** and may charge fees.

## Workflow preview (illustration)

![ComfyUI workflow layout preview](assets/workflow-preview.png)

*Layout diagram rendered from this repository's `workflow.json`; not a live ComfyUI screenshot.*

## Clean Slate Controller

The workflow includes the [RebelTortuga Clean Slate Controller](https://github.com/RebelTortuga/comfyui-clean-slate). Its `image_1`, `positive`, and `negative` inputs are connected to the source image and the corresponding Prompt History outputs. Five buttons clear the image, either prompt, both prompts, or all three. Prompt History remains enabled and stores history locally on each user's own machine; no previous prompt entries or images are bundled.
## Start here

1. Install/update [ComfyUI](https://github.com/Comfy-Org/ComfyUI) locally, either directly or through [Stability Matrix](https://github.com/LykosAI/StabilityMatrix).
2. Install the custom nodes listed in [Dependencies](DEPENDENCIES.md). Use the Python environment belonging to that ComfyUI installation for each extension's requirements.
3. Download the models listed below. Keep their upstream names or reselect renamed files in the loaders.
4. Restart ComfyUI, refresh the browser, and drag `workflow.json` onto the canvas. This is a UI workflow, not an API-format prompt.
5. Follow the workflow steps below. No API key or paid service is required by this graph.

## Requirements

- A working local ComfyUI installation with support for the exact node types in `DEPENDENCIES.md`.
- The listed custom nodes and model files; they are not included in this ZIP.
- Sufficient GPU/system memory and disk space for the selected models and settings. A hardware minimum has not been verified.
- Internet access for initial downloads. The supplied graph uses local inference rather than a paid API.
- Python is needed for ComfyUI; the optional validation script uses the Python standard library. Git is optional when downloading ZIP packages.

## Models

| Loader selection / filename | Location under ComfyUI | Source / instructions |
|---|---|---|
| `wan2.2_ti2v_5B_fp16.safetensors` | `models/diffusion_models` | https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_ti2v_5B_fp16.safetensors |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `models/text_encoders` | https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors |
| `wan2.2_vae.safetensors` | `models/vae` | https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan2.2_vae.safetensors |

## Using the workflow

1. Load a reference image and write the desired motion in the prompt-history node; prompts start blank.
2. Inspect PREPARED REFERENCE. Center cropping can remove parts of the head or hands.
3. Run with the supplied 480 × 768, 201-frame settings. At 24 fps, the nominal duration is 8.38 seconds.
4. Find the saved video under ComfyUI's output/video directory.

The graph uses 30 steps, CFG 5, uni_pc/simple, fixed seed 123456789 and tiled VAE decoding. Resolution, frame count, and available memory affect performance; no minimum VRAM or render time is certified here. For a quick trial, change BOTH image resize and latent dimensions to 480 × 768, set 49 frames and 16 steps. Use frame counts of the form 4n+1. For landscape, update both dimension pairs together.

The embedded shared note describes several presets; the actual settings above are authoritative. Higher-resolution execution has not been verified in this packaging session.

## Prompt history and blank defaults

Positive and negative prompt fields and the input-image selection start blank. Prompt pairs are saved to a relative `user/prompt_history/` JSON path. History is not bundled. Ensure the directory is writable and use the history node's edit mode for a new prompt. Saved history may contain private text; do not commit it.

If `SelectPromptPairHistory` is unavailable, install/update the exact PromptHistory extension in Dependencies. A free fallback is to remove that node in a copy and enter positive/negative text directly into the two text-encoding nodes, disconnecting their prompt-string inputs first. This fallback changes the graph and is not the supplied default.

## Troubleshooting

- **Red/missing nodes:** compare exact node type names in `DEPENDENCIES.md`; different SAM2 or similarly named extension packages are not interchangeable.
- **Missing model:** verify its folder, refresh model lists and select the installed filename in the loader.
- **Out of memory:** reduce image dimensions/frame count as applicable; close other GPU applications. Quantization/tiled decoding do not guarantee a particular GPU will fit.
- **Blank/incorrect result:** check prompts, loaded image, masks, switch mode and selected models.
- **Dependency installation:** follow each upstream README; avoid installing packages into an unrelated global Python.

## Validation and provenance

The workflow is derived from the actual Clean Slate JSON uploaded by the author. Source image and active prompts are blank. Prompt History retains its local save/recall configuration. Two source graphs needed a corrected negative-prompt link; all generation settings are preserved. `SOURCE.json` records the uploaded filename, checksum and changes.

Run `python scripts/validate_workflow.py` to check graph references. Structural checks passed during packaging. No GPU inference, clean-machine installation, visual output quality, or complete dependency-version compatibility was tested here. Exported core node version metadata is not a certified minimum ComfyUI version.

## Frequently asked questions

**Do I need a video to begin?** No. This is an image-to-video workflow: load a still reference image and describe the intended movement.

**Why is rendering slow or out of memory?** Video generation is resource-intensive. Reduce frame count or resolution and close other GPU applications; no specific minimum GPU configuration is guaranteed.

**Why did the subject drift or the crop change?** Inspect **PREPARED REFERENCE** for cropping, and try a shorter sequence or simpler motion instructions.

**Where are the model files?** Models are not packaged in the ZIP. Follow the model table and `DEPENDENCIES.md` for paths and extensions.

## 🔗 Related Free RebelTortuga Projects

Explore other free tools and workflows:

- [comfyui-clean-slate](https://github.com/RebelTortuga/comfyui-clean-slate)
- [comfyui-free-local-qwen-image-edit](https://github.com/RebelTortuga/comfyui-free-local-qwen-image-edit)
- [comfyui-free-local-sdxl-inpainting](https://github.com/RebelTortuga/comfyui-free-local-sdxl-inpainting)
- [comfyui-free-local-wan-video-high-resolution](https://github.com/RebelTortuga/comfyui-free-local-wan-video-high-resolution)

[Browse all RebelTortuga projects](https://github.com/RebelTortuga)

## 🐢 Support RebelTortuga

These workflows are free to download and use. Donations are always optional and do not unlock features.

**[☕ Help this turtle get a new shell on Ko-fi!](https://ko-fi.com/rebeltortuga)**

Contributions help me explore AI, improve workflows, and share free tools. Bug reports and useful suggestions are equally welcome.

## Credits and licensing

The workflow JSON, preview and original documentation in this repository are released under the [MIT License](LICENSE) by RebelTortuga. Model weights, ComfyUI, custom nodes and third-party components are **not included** and retain their own separate licenses and attribution requirements. Review those terms before downloading, redistributing or using them commercially.


## Documentation and help

- **README.md** — start here, requirements, model files, use, and troubleshooting.
- **OPTIONS-README.md** — a plain-language guide to prompts, settings, and the workflow's main stages.
- **DEPENDENCIES.md** — custom-node sources and the exact node types used.
- **CHANGELOG.md** — changes to this repository package.
- **SOURCE.json** — source filename and checksum.

## Feedback and suggestions

Use this repository's GitHub Issues page for bug reports, improvements, and feature requests. Include the workflow name, ComfyUI version, GPU/VRAM, relevant error text, and what you expected to happen. Review logs and screenshots for personal information before sharing them.


## Clean template defaults

Images and active positive/negative prompts start blank. Prompt History auto-save and recall remain enabled; the history JSON files themselves are **not** bundled. The preview PNG is included at `assets/workflow-preview.png`.

---

<!-- BEGIN REBELTORTUGA SAFETY -->
## Privacy & Software Safety

Read the [project safety guidance](SAFETY.md) before use. It covers local workflows, dependencies, saved files, and security warnings. See [SECURITY.md](SECURITY.md) for vulnerability reporting and the [license](LICENSE) for terms.

[Privacy & Software Safety](https://rebeltortuga.github.io/privacy-software-safety.html) · [Project Licenses](https://rebeltortuga.github.io/project-licenses.html)

Do not upload passwords, access tokens, browser profiles, private backups, or unredacted diagnostic reports to public issues.
<!-- END REBELTORTUGA SAFETY -->

<!-- rebeltortuga-official-links:start -->
## Official RebelTortuga links

- 🌐 [Website](https://rebeltortuga.github.io/)
- <img src="https://cdn.simpleicons.org/github/FFFFFF" width="17" height="17" alt=""> [GitHub](https://github.com/RebelTortuga)
- <img src="https://cdn.simpleicons.org/twitch/9146FF" width="17" height="17" alt=""> [Twitch](https://www.twitch.tv/rebeltortuga)
- <img src="https://cdn.simpleicons.org/youtube/FF0033" width="17" height="17" alt=""> [YouTube](https://www.youtube.com/channel/UCpMIirV8w5RfVd9TpKpA2pQ)
- <img src="https://cdn.simpleicons.org/patreon/FF424D" width="17" height="17" alt=""> [Patreon](https://www.patreon.com/cw/RebelTortuga)
- <img src="https://cdn.simpleicons.org/kofi/FF5E5B" width="17" height="17" alt=""> [Ko-fi](https://ko-fi.com/rebeltortuga)
<!-- rebeltortuga-official-links:end -->

## Official Project Guide

[View the comfyui-free-local-wan-video-quality project guide](https://rebeltortuga.github.io/projects/comfyui-free-local-wan-video-quality.html)
