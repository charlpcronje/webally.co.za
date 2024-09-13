# Label
Renders an accessible label associated with controls.

**Install:** `npx  shadcn-svelte@latest add label`

## Preview
```svelte
<script lang="ts">
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>
 
<div>
  <div class="flex items-center space-x-2">
    <Checkbox id="terms" />
    <Label for="terms">Accept terms and conditions</Label>
  </div>
</div>
```

## Usage
```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label";
</script>
 
<Label for="email">Your email address</Label>
```