## Command
Fast, composable, unstyled command menu for Svelte.
Install: `npx shadcn-svelte@latest add command`

### Usage
```svelte
<script lang="ts">
 import * as Command from "$lib/components/ui/command";
</script>
 
<Command.Root>
 <Command.Input placeholder="Type a command or search..." />
 <Command.List>
  <Command.Empty>No results found.</Command.Empty>
  <Command.Group heading="Suggestions">
   <Command.Item>Calendar</Command.Item>
   <Command.Item>Search Emoji</Command.Item>
   <Command.Item>Calculator</Command.Item>
  </Command.Group>
  <Command.Separator />
  <Command.Group heading="Settings">
   <Command.Item>Profile</Command.Item>
   <Command.Item>Billing</Command.Item>
   <Command.Item>Settings</Command.Item>
  </Command.Group>
 </Command.List>
</Command.Root>
```

#### Examples
#### Dialog
```svelte
<script lang="ts">
 import Calculator from "lucide-svelte/icons/calculator";
 import Calendar from "lucide-svelte/icons/calendar";
 import CreditCard from "lucide-svelte/icons/credit-card";
 import Settings from "lucide-svelte/icons/settings";
 import Smile from "lucide-svelte/icons/smile";
 import User from "lucide-svelte/icons/user";
 import { onMount } from "svelte";
 import * as Command from "$lib/components/ui/command/index.js";
 
 let open = false;
 
 onMount(() => {
  function handleKeydown(e: KeyboardEvent) {
   if (e.key === "j" && (e.metaKey || e.ctrlKey)) {
    e.preventDefault();
    open = !open;
   }
  }
 
  document.addEventListener("keydown", handleKeydown);
  return () => {
   document.removeEventListener("keydown", handleKeydown);
  };
 });
</script>
 
<p class="text-muted-foreground text-sm">
 Press
 <kbd
  class="bg-muted text-muted-foreground pointer-events-none inline-flex h-5 select-none items-center gap-1 rounded border px-1.5 font-mono text-[10px] font-medium opacity-100"
 >
  <span class="text-xs">⌘</span>J
 </kbd>
</p>
<Command.Dialog bind:open>
 <Command.Input placeholder="Type a command or search..." />
 <Command.List>
  <Command.Empty>No results found.</Command.Empty>
  <Command.Group heading="Suggestions">
   <Command.Item>
    <Calendar class="mr-2 h-4 w-4" />
    <span>Calendar</span>
   </Command.Item>
   <Command.Item>
    <Smile class="mr-2 h-4 w-4" />
    <span>Search Emoji</span>
   </Command.Item>
   <Command.Item>
    <Calculator class="mr-2 h-4 w-4" />
    <span>Calculator</span>
   </Command.Item>
  </Command.Group>
  <Command.Separator />
  <Command.Group heading="Settings">
   <Command.Item>
    <User class="mr-2 h-4 w-4" />
    <span>Profile</span>
    <Command.Shortcut>⌘P</Command.Shortcut>
   </Command.Item>
   <Command.Item>
    <CreditCard class="mr-2 h-4 w-4" />
    <span>Billing</span>
    <Command.Shortcut>⌘B</Command.Shortcut>
   </Command.Item>
   <Command.Item>
    <Settings class="mr-2 h-4 w-4" />
    <span>Settings</span>
    <Command.Shortcut>⌘S</Command.Shortcut>
   </Command.Item>
  </Command.Group>
 </Command.List>
</Command.Dialog>
```

To show the command menu in a dialog, use the `<Command.Dialog />` component instead of `<Command.Root />`. It accepts props for both the `<Dialog.Root />` and `<Command.Root />` components.
```svelte
<script lang="ts">
 import * as Command from "$lib/components/ui/command";
 import { onMount } from "svelte";
 
 let open = false;
 
 onMount(() => {
  function handleKeydown(e: KeyboardEvent) {
   if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
    e.preventDefault();
    open = !open;
   }
  }
 
  document.addEventListener("keydown", handleKeydown);
 
  return () => {
   document.removeEventListener("keydown", handleKeydown);
  };
 });
</script>
 
<Command.Dialog bind:open>
 <Command.Input placeholder="Type a command or search..." />
 <Command.List>
  <Command.Empty>No results found.</Command.Empty>
  <Command.Group heading="Suggestions">
   <Command.Item>Calendar</Command.Item>
   <Command.Item>Search Emoji</Command.Item>
   <Command.Item>Calculator</Command.Item>
  </Command.Group>
 </Command.List>
</Command.Dialog>
```