# Sheet
Extends the Dialog component to display content that complements the main content of the screen.
Install: `npx shadcn-svelte@latest add sheet`

```svelte
<script lang="ts">
 import * as Sheet from "$lib/components/ui/sheet/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import { Input } from "$lib/components/ui/input/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
</script>
 
<Sheet.Root>
 <Sheet.Trigger asChild let:builder>
  <Button builders={[builder]} variant="outline">Open</Button>
 </Sheet.Trigger>
 <Sheet.Content side="right">
  <Sheet.Header>
   <Sheet.Title>Edit profile</Sheet.Title>
   <Sheet.Description>
    Make changes to your profile here. Click save when you're done.
   </Sheet.Description>
  </Sheet.Header>
  <div class="grid gap-4 py-4">
   <div class="grid grid-cols-4 items-center gap-4">
    <Label for="name" class="text-right">Name</Label>
    <Input id="name" value="Pedro Duarte" class="col-span-3" />
   </div>
   <div class="grid grid-cols-4 items-center gap-4">
    <Label for="username" class="text-right">Username</Label>
    <Input id="username" value="@peduarte" class="col-span-3" />
   </div>
  </div>
  <Sheet.Footer>
   <Sheet.Close asChild let:builder>
    <Button builders={[builder]} type="submit">Save changes</Button>
   </Sheet.Close>
  </Sheet.Footer>
 </Sheet.Content>
</Sheet.Root>
```

## Usage
```svelte
<script lang="ts">
 import * as Sheet from "$lib/components/ui/sheet";
</script>
 
<Sheet.Root>
 <Sheet.Trigger>Open</Sheet.Trigger>
 <Sheet.Content>
  <Sheet.Header>
   <Sheet.Title>Are you sure absolutely sure?</Sheet.Title>
   <Sheet.Description>
    This action cannot be undone. This will permanently delete your account
    and remove your data from our servers.
   </Sheet.Description>
  </Sheet.Header>
 </Sheet.Content>
</Sheet.Root>
```

## Examples

## Side
Pass the side property to `<SheetContent />` to indicate the edge of the screen where the component will appear. The values can be top, right, bottom or left.

```svelte
<script lang="ts">
 import * as Sheet from "$lib/components/ui/sheet/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import { Input } from "$lib/components/ui/input/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
 
 const SHEET_SIDES = ["top", "right", "bottom", "left"] as const;
</script>
 
<div class="grid grid-cols-2 gap-2">
 {#each SHEET_SIDES as side, _ (side)}
  <Sheet.Root>
   <Sheet.Trigger asChild let:builder>
    <Button builders={[builder]} variant="outline">{side}</Button>
   </Sheet.Trigger>
   <Sheet.Content {side}>
    <Sheet.Header>
     <Sheet.Title>Edit profile</Sheet.Title>
     <Sheet.Description>
      Make changes to your profile here. Click save when you're done.
     </Sheet.Description>
    </Sheet.Header>
    <div class="grid gap-4 py-4">
     <div class="grid grid-cols-4 items-center gap-4">
      <Label for="name" class="text-right">Name</Label>
      <Input id="name" value="Pedro Duarte" class="col-span-3" />
     </div>
     <div class="grid grid-cols-4 items-center gap-4">
      <Label for="username" class="text-right">Username</Label>
      <Input id="username" value="@peduarte" class="col-span-3" />
     </div>
    </div>
    <Sheet.Footer>
     <Sheet.Close asChild let:builder>
      <Button builders={[builder]} type="submit">Save changes</Button>
     </Sheet.Close>
    </Sheet.Footer>
   </Sheet.Content>
  </Sheet.Root>
 {/each}
</div>
```