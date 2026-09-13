# Blender-to-Unreal-Environment-Generator
Blender-to-Unreal procedural environment generation pipeline using Instanced Static Meshes (ISM), CSV-driven scene reconstruction, automated collision setup, and optimized low-poly assets for scalable real-time rendering.

A procedural environment generation pipeline for Unreal Engine that reconstructs large-scale real-world scenes using a combination of manually created and AI-generated assets. The workflow leverages Blender for scene assembly, collision setup, and instance management, while Unreal Engine uses Instanced Static Meshes (ISM) and Data Tables to generate optimized environments from exported transformation data.

The system includes a custom Blender export script that converts instance transforms into CSV files, which are imported into Unreal Engine and processed through Blueprint Construction Scripts. This approach significantly reduces draw calls, memory consumption, and manual level-design effort while maintaining real-time rendering performance. Additional optimizations include collision automation, modular asset workflows, baked low-poly assets, and texture memory optimization through controlled texture resolutions and UV organization.

Key Features:
• Blender-to-Unreal procedural environment workflow
• Instanced Static Mesh (ISM) based rendering optimization
• CSV-driven scene reconstruction
• Automated collision generation using Unreal naming conventions
• Support for modular and scalable environments
• Low-poly asset optimization with baked high-detail textures
• Real-time performance-focused rendering pipeline
• Hybrid use of manually created and AI-generated assets
