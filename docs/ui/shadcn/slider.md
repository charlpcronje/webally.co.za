# Slider
An input where the user selects a value from within a given range.
**Install**: `npx shadcn-svelte@latest add slider`

```svelte
<script lang="ts">
 import { Slider } from "$lib/components/ui/slider/index.js";
</script>
 
<Slider value={[50]} max={100} step={1} class="max-w-[70%]" />
```

## Usage
```svelte
<script lang="ts">
 import { Slider } from "$lib/components/ui/slider";
</script>
 
<Slider value={[33]} max={100} step={1} />
```