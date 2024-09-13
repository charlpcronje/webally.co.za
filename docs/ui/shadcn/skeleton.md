# Skeleton
Use to show a placeholder while content is loading.

```svelte
<script lang="ts">
 import { Skeleton } from "$lib/components/ui/skeleton/index.js";
</script>
 
<div class="flex items-center space-x-4">
 <Skeleton class="h-12 w-12 rounded-full" />
 <div class="space-y-2">
  <Skeleton class="h-4 w-[250px]" />
  <Skeleton class="h-4 w-[200px]" />
 </div>
</div>
```

Install: `npx shadcn-svelte@latest add skeleton`

## Usage
```svelte
<script lang="ts">
 import { Skeleton } from "$lib/components/ui/skeleton";
</script>
```
```svelte
<Skeleton class="h-[20px] w-[100px] rounded-full" />
```