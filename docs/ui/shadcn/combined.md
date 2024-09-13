# File Analysis Report

This document contains an analysis of the project files.

| No.   | File                                 | Lines    | Words    | AI Tokens |
| ----- | ------------------------------------ | -------- | -------- | --------- |
|  1    | ./progress.md                        | 77       | 235      | 432       |
|  2    | ./label.md                           | 28       | 65       | 143       |
|  3    | ./hover-card.md                      | 42       | 83       | 155       |
|  4    | ./dropdown-menu.md                   | 186      | 391      | 1021      |
|  5    | ./drawer.md                          | 101      | 278      | 684       |
|  6    | ./dialog.md                          | 96       | 255      | 463       |
|  7    | ./context-menu.md                    | 45       | 93       | 186       |
|  8    | ./pagination.md                      | 64       | 124      | 263       |
|  9    | ./command.md                         | 143      | 341      | 814       |
|  10   | ./checkbox.md                        | 262      | 676      | 1438      |
|  11   | ./carousel.md                        | 252      | 529      | 1205      |
|  12   | ./breadcrumb.md                      | 109      | 226      | 433       |
|  13   | ./popover.md                         | 45       | 90       | 175       |
|  14   | ./alert-dialog.md                    | 52       | 112      | 217       |
|  15   | ./accordion.md                       | 44       | 95       | 193       |
|  16   | ./card.md                            | 68       | 131      | 270       |
|  17   | ./menubar.md                         | 109      | 185      | 537       |
|  18   | ./combobox.md                        | 151      | 368      | 720       |
|  19   | ./calendar.md                        | 65       | 217      | 351       |
|  20   | ./button.md                          | 153      | 218      | 465       |
|  21   | ./badge.md                           | 88       | 146      | 295       |
|  22   | ./avatar.md                          | 40       | 78       | 156       |
|  23   | ./aspect-ratio.md                    | 41       | 83       | 171       |
|  24   | ./alert.md                           | 55       | 93       | 179       |
|  25   | ./input.md                           | 93       | 128      | 259       |
|  26   | ./collapsible.md                     | 43       | 92       | 167       |
|  27   | ./scroll-area.md                     | 63       | 174      | 322       |
|  28   | ./toggle.md                          | 92       | 127      | 268       |
|  29   | ./range-calendar.md                  | 36       | 98       | 177       |
|  30   | ./radio-group.md                     | 129      | 363      | 836       |
|  31   | ./form.md                            | 215      | 726      | 1255      |
|  32   | ./select.md                          | 80       | 197      | 448       |
|  33   | ./separator.md                       | 35       | 76       | 181       |
|  34   | ./sheet.md                           | 110      | 324      | 749       |
|  35   | ./skeleton.md                        | 28       | 68       | 152       |
|  36   | ./slider.md                          | 20       | 55       | 127       |
|  37   | ./sonner.md                          | 57       | 225      | 374       |
|  38   | ./switch.md                          | 118      | 293      | 634       |
|  39   | ./table.md                           | 105      | 181      | 537       |
|  40   | ./tabs.md                            | 84       | 202      | 535       |
|  41   | ./textarea.md                        | 150      | 408      | 852       |
|       | Total                                | 3774     | 8849     | 18839     |


## Total Counts Across All Files. Tokenizer Used: NLTK's Punkt Tokenizer
- Total Lines: 3774
- Total Words: 8849
- Total AI Tokens: 18839

## File: progress.md
```md
# Progress

```html
<script lang="ts">
  import { Progress } from "bits-ui";
  import { onMount } from "svelte";
 
  let value = 13;
  onMount(() => {
    const timer = setTimeout(() => (value = 66), 500);
    return () => clearTimeout(timer);
  });
</script>
 
<Progress.Root
  {value}
  max={100}
  class="relative h-[15px] w-[60%] overflow-hidden rounded-full bg-dark-10 shadow-mini-inset"
>
  <div
    class="h-full w-full flex-1 rounded-full bg-foreground shadow-mini-inset transition-all duration-1000 ease-in-out"
    style={`transform: translateX(-${
      100 - (100 * (value ?? 0)) / (100 ?? 1)
    }%)`}
  />
</Progress.Root>
```

---

### **Structure**

```ts
<script lang="ts">
  import { Progress } from "bits-ui";
</script>
 
<Progress.Root />
```

---

### **API Reference**

#### **Progress.Root**  
The progress bar component.

- **max**: `number`  
  The maximum value of the progress bar. Used to calculate the percentage of the progress bar.  
  _Default: 100_

- **value**: `number`  
  The current value of the progress bar.  
  _Default: 0_

- **onValueChange**: `function`  
  A callback that fires when the value changes.  
  _Default: undefined_

- **asChild**: `boolean`  
  Whether to use render delegation with this component or not.  
  _Default: false_

- **el**: `HTMLDivElement`  
  The underlying DOM element being rendered. You can bind to this to programmatically interact with the element.  
  _Default: undefined_

---

### **Data Attributes**

- **data-value**: The current value of the progress bar.
- **data-max**: The maximum value of the progress bar.
- **data-state**: Enum representing the current state of the progress bar.
- **data-progress-root**: Present on the root element.

Let me know if you need any additional information!
```

## File: label.md
```md
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
```

## File: hover-card.md
```md
# Hover Card
For sighted users to preview content available behind a link.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="hover-card-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="hover-card" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as HoverCard from "$lib/components/ui/hover-card";
</script>

<HoverCard.Root>
  <HoverCard.Trigger>Hover</HoverCard.Trigger>
  <HoverCard.Content>
    SvelteKit - Web development, streamlined
  </HoverCard.Content>
</HoverCard.Root>
```

```

## File: dropdown-menu.md
```md
# Dropdown Menu
Displays a menu to the user — such as a set of actions or functions — triggered by a button.

```svelte
<script lang="ts">
 import CirclePlus from "lucide-svelte/icons/circle-plus";
 import Cloud from "lucide-svelte/icons/cloud";
 import CreditCard from "lucide-svelte/icons/credit-card";
 import Github from "lucide-svelte/icons/github";
 import Keyboard from "lucide-svelte/icons/keyboard";
 import LifeBuoy from "lucide-svelte/icons/life-buoy";
 import LogOut from "lucide-svelte/icons/log-out";
 import Mail from "lucide-svelte/icons/mail";
 import MessageSquare from "lucide-svelte/icons/message-square";
 import Plus from "lucide-svelte/icons/plus";
 import Settings from "lucide-svelte/icons/settings";
 import User from "lucide-svelte/icons/user";
 import UserPlus from "lucide-svelte/icons/user-plus";
 import Users from "lucide-svelte/icons/users";
 
 import { Button } from "$lib/components/ui/button/index.js";
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
</script>
 
<DropdownMenu.Root>
 <DropdownMenu.Trigger asChild let:builder>
  <Button builders={[builder]} variant="outline">Open</Button>
 </DropdownMenu.Trigger>
 <DropdownMenu.Content class="w-56">
  <DropdownMenu.Label>My Account</DropdownMenu.Label>
  <DropdownMenu.Separator />
  <DropdownMenu.Group>
   <DropdownMenu.Item>
    <User class="mr-2 h-4 w-4" />
    <span>Profile</span>
    <DropdownMenu.Shortcut>⇧⌘P</DropdownMenu.Shortcut>
   </DropdownMenu.Item>
   <DropdownMenu.Item>
    <CreditCard class="mr-2 h-4 w-4" />
    <span>Billing</span>
    <DropdownMenu.Shortcut>⌘B</DropdownMenu.Shortcut>
   </DropdownMenu.Item>
   <DropdownMenu.Item>
    <Settings class="mr-2 h-4 w-4" />
    <span>Settings</span>
    <DropdownMenu.Shortcut>⌘S</DropdownMenu.Shortcut>
   </DropdownMenu.Item>
   <DropdownMenu.Item>
    <Keyboard class="mr-2 h-4 w-4" />
    <span>Keyboard shortcuts</span>
    <DropdownMenu.Shortcut>⌘K</DropdownMenu.Shortcut>
   </DropdownMenu.Item>
  </DropdownMenu.Group>
  <DropdownMenu.Separator />
  <DropdownMenu.Group>
   <DropdownMenu.Item>
    <Users class="mr-2 h-4 w-4" />
    <span>Team</span>
   </DropdownMenu.Item>
   <DropdownMenu.Sub>
    <DropdownMenu.SubTrigger>
     <UserPlus class="mr-2 h-4 w-4" />
     <span>Invite users</span>
    </DropdownMenu.SubTrigger>
    <DropdownMenu.SubContent>
     <DropdownMenu.Item>
      <Mail class="mr-2 h-4 w-4" />
      <span>Email</span>
     </DropdownMenu.Item>
     <DropdownMenu.Item>
      <MessageSquare class="mr-2 h-4 w-4" />
      <span>Message</span>
     </DropdownMenu.Item>
     <DropdownMenu.Item>
      <CirclePlus class="mr-2 h-4 w-4" />
      <span>More...</span>
     </DropdownMenu.Item>
    </DropdownMenu.SubContent>
   </DropdownMenu.Sub>
   <DropdownMenu.Item>
    <Plus class="mr-2 h-4 w-4" />
    <span>New Team</span>
    <DropdownMenu.Shortcut>⌘+T</DropdownMenu.Shortcut>
   </DropdownMenu.Item>
  </DropdownMenu.Group>
  <DropdownMenu.Separator />
  <DropdownMenu.Item>
   <Github class="mr-2 h-4 w-4" />
   <span>GitHub</span>
  </DropdownMenu.Item>
  <DropdownMenu.Item>
   <LifeBuoy class="mr-2 h-4 w-4" />
   <span>Support</span>
  </DropdownMenu.Item>
  <DropdownMenu.Item>
   <Cloud class="mr-2 h-4 w-4" />
   <span>API</span>
  </DropdownMenu.Item>
  <DropdownMenu.Separator />
  <DropdownMenu.Item>
   <LogOut class="mr-2 h-4 w-4" />
   <span>Log out</span>
   <DropdownMenu.Shortcut>⇧⌘Q</DropdownMenu.Shortcut>
  </DropdownMenu.Item>
 </DropdownMenu.Content>
</DropdownMenu.Root>
```

**Install:** `npx shadcn-svelte@latest add dropdown-menu`

## Usage
```svelte
<script lang="ts">
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
</script>
 
<DropdownMenu.Root>
 <DropdownMenu.Trigger>Open</DropdownMenu.Trigger>
 <DropdownMenu.Content>
  <DropdownMenu.Group>
   <DropdownMenu.Label>My Account</DropdownMenu.Label>
   <DropdownMenu.Separator />
   <DropdownMenu.Item>Profile</DropdownMenu.Item>
   <DropdownMenu.Item>Billing</DropdownMenu.Item>
   <DropdownMenu.Item>Team</DropdownMenu.Item>
   <DropdownMenu.Item>Subscription</DropdownMenu.Item>
  </DropdownMenu.Group>
 </DropdownMenu.Content>
</DropdownMenu.Root>
```

### Checkboxes
```svelte
<script lang="ts">
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 
 let showStatusBar = true;
 let showActivityBar = false;
 let showPanel = false;
</script>
 
<DropdownMenu.Root>
 <DropdownMenu.Trigger asChild let:builder>
  <Button variant="outline" builders={[builder]}>Open</Button>
 </DropdownMenu.Trigger>
 <DropdownMenu.Content class="w-56">
  <DropdownMenu.Label>Appearance</DropdownMenu.Label>
  <DropdownMenu.Separator />
  <DropdownMenu.CheckboxItem bind:checked={showStatusBar}>
   Status Bar
  </DropdownMenu.CheckboxItem>
  <DropdownMenu.CheckboxItem bind:checked={showActivityBar} disabled>
   Activity Bar
  </DropdownMenu.CheckboxItem>
  <DropdownMenu.CheckboxItem bind:checked={showPanel}
   >Panel</DropdownMenu.CheckboxItem
  >
 </DropdownMenu.Content>
</DropdownMenu.Root>
```

### Radio Group
```svelte
<script lang="ts">
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 
 let position = "bottom";
</script>
 
<DropdownMenu.Root>
 <DropdownMenu.Trigger asChild let:builder>
  <Button variant="outline" builders={[builder]}>Open</Button>
 </DropdownMenu.Trigger>
 <DropdownMenu.Content class="w-56">
  <DropdownMenu.Label>Panel Position</DropdownMenu.Label>
  <DropdownMenu.Separator />
  <DropdownMenu.RadioGroup bind:value={position}>
   <DropdownMenu.RadioItem value="top">Top</DropdownMenu.RadioItem>
   <DropdownMenu.RadioItem value="bottom">Bottom</DropdownMenu.RadioItem>
   <DropdownMenu.RadioItem value="right">Right</DropdownMenu.RadioItem>
  </DropdownMenu.RadioGroup>
 </DropdownMenu.Content>
</DropdownMenu.Root>
```
```

## File: drawer.md
```md
# Drawer
A drawer component for Svelte.

## About
Drawer is built on top of Vaul Svelte, which is a Svelte port of Vaul by Emil Kowalski.

**Install:** `npx  shadcn-svelte@latest add drawer`

```svelte
<script lang="ts">
 import * as Drawer from "$lib/components/ui/drawer";
</script>
 
<Drawer.Root>
 <Drawer.Trigger>Open</Drawer.Trigger>
 <Drawer.Content>
  <Drawer.Header>
   <Drawer.Title>Are you sure absolutely sure?</Drawer.Title>
   <Drawer.Description>This action cannot be undone.</Drawer.Description>
  </Drawer.Header>
  <Drawer.Footer>
   <Button>Submit</Button>
   <Drawer.Close>Cancel</Drawer.Close>
  </Drawer.Footer>
 </Drawer.Content>
</Drawer.Root>
```

### Examples
#### Responsive Dialog
You can combine the Dialog and Drawer components to create a responsive dialog. This renders a Dialog on desktop and a Drawer on mobile.`
```svelte
<script lang="ts">
 import { mediaQuery } from "svelte-legos";
 import * as Dialog from "$lib/components/ui/dialog/index.js";
 import * as Drawer from "$lib/components/ui/drawer/index.js";
 import { Input } from "$lib/components/ui/input/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 
 let open = false;
 const isDesktop = mediaQuery("(min-width: 768px)");
</script>
 
{#if $isDesktop}
 <Dialog.Root bind:open>
  <Dialog.Trigger asChild let:builder>
   <Button variant="outline" builders={[builder]}>Edit Profile</Button>
  </Dialog.Trigger>
  <Dialog.Content class="sm:max-w-[425px]">
   <Dialog.Header>
    <Dialog.Title>Edit profile</Dialog.Title>
    <Dialog.Description>
     Make changes to your profile here. Click save when you're done.
    </Dialog.Description>
   </Dialog.Header>
   <form class="grid items-start gap-4">
    <div class="grid gap-2">
     <Label for="email">Email</Label>
     <Input type="email" id="email" value="shadcn@example.com" />
    </div>
    <div class="grid gap-2">
     <Label for="username">Username</Label>
     <Input id="username" value="@shadcn" />
    </div>
    <Button type="submit">Save changes</Button>
   </form>
  </Dialog.Content>
 </Dialog.Root>
{:else}
 <Drawer.Root bind:open>
  <Drawer.Trigger asChild let:builder>
   <Button variant="outline" builders={[builder]}>Edit Profile</Button>
  </Drawer.Trigger>
  <Drawer.Content>
   <Drawer.Header class="text-left">
    <Drawer.Title>Edit profile</Drawer.Title>
    <Drawer.Description>
     Make changes to your profile here. Click save when you're done.
    </Drawer.Description>
   </Drawer.Header>
   <form class="grid items-start gap-4 px-4">
    <div class="grid gap-2">
     <Label for="email">Email</Label>
     <Input type="email" id="email" value="shadcn@example.com" />
    </div>
    <div class="grid gap-2">
     <Label for="username">Username</Label>
     <Input id="username" value="@shadcn" />
    </div>
    <Button type="submit">Save changes</Button>
   </form>
   <Drawer.Footer class="pt-2">
    <Drawer.Close asChild let:builder>
     <Button variant="outline" builders={[builder]}>Cancel</Button>
    </Drawer.Close>
   </Drawer.Footer>
  </Drawer.Content>
 </Drawer.Root>
{/if}
```
```

## File: dialog.md
```md
# Dialog
A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

## Structure
```svelte
<script lang="ts">
  import { Dialog } from "bits-ui";
</script>
 
<Dialog.Root>
  <Dialog.Trigger />
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content>
      <Dialog.Title />
      <Dialog.Description />
      <Dialog.Close />
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Controlled Usage
If you want to control or be aware of the `open` state of the dialog from outside of the component, you can bind to the `open` prop.
```svelte
<script lang="ts">
  import { Dialog } from "bits-ui";
  let dialogOpen = false;
</script>
 
<button on:click={() => (dialogOpen = true)}>Open Dialog</button>
<Dialog.Root bind:open={dialogOpen}>
  <Dialog.Trigger />
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content>
      <Dialog.Title />
      <Dialog.Description />
      <Dialog.Close />
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

# Dialog - Bits UI

> ## Excerpt
> Headless components for Svelte.

---
Here is your content formatted in Markdown:

# Dialog
A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

## Structure
```svelte
<script lang="ts">
  import { Dialog } from "bits-ui";
</script>

<Dialog.Root>
  <Dialog.Trigger />
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content>
      <Dialog.Title />
      <Dialog.Description />
      <Dialog.Close />
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

### Controlled Usage
If you want to control or be aware of the `open` state of the dialog from outside of the component, you can bind to the `open` prop.
```svelte
<script lang="ts">
  import { Dialog } from "bits-ui";
  let dialogOpen = false;
</script>

<button on:click={() => (dialogOpen = true)}>Open Dialog</button>
<Dialog.Root bind:open={dialogOpen}>
  <Dialog.Trigger />
  <Dialog.Portal>
    <Dialog.Overlay />
    <Dialog.Content>
      <Dialog.Title />
      <Dialog.Description />
      <Dialog.Close />
    </Dialog.Content>
  </Dialog.Portal>
</Dialog.Root>
```

```

## File: context-menu.md
```md
# Context Menu
Displays a menu to the user — such as a set of actions or functions — triggered by right click.

<script>
    import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs'
</script>

<ComponentPreview name="context-menu-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="context-menu" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu";
</script>

<ContextMenu.Root>
  <ContextMenu.Trigger>Right click</ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Item>Profile</ContextMenu.Item>
    <ContextMenu.Item>Billing</ContextMenu.Item>
    <ContextMenu.Item>Team</ContextMenu.Item>
    <ContextMenu.Item>Subscription</ContextMenu.Item>
  </ContextMenu.Content>
</ContextMenu.Root>
```

```

## File: pagination.md
```md
---
title: Pagination
description: Pagination with page navigation, next and previous links.
component: true
source: https://github.com/huntabyte/shadcn-svelte/tree/main/sites/docs/src/lib/registry/default/ui/pagination
bits: https://www.bits-ui.com/docs/components/pagination
---

<script>
    import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="pagination-demo" >

<div />

</ComponentPreview>

## Installation

<PMAddComp name="pagination" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as Pagination from "$lib/components/ui/pagination";
</script>

<Pagination.Root count={100} perPage={10} let:pages let:currentPage>
  <Pagination.Content>
    <Pagination.Item>
      <Pagination.PrevButton />
    </Pagination.Item>
    {#each pages as page (page.key)}
      {#if page.type === "ellipsis"}
        <Pagination.Item>
          <Pagination.Ellipsis />
        </Pagination.Item>
      {:else}
        <Pagination.Item isVisible={currentPage == page.value}>
          <Pagination.Link {page} isActive={currentPage == page.value}>
            {page.value}
          </Pagination.Link>
        </Pagination.Item>
      {/if}
    {/each}
    <Pagination.Item>
      <Pagination.NextButton />
    </Pagination.Item>
  </Pagination.Content>
</Pagination.Root>
```

```

## File: command.md
```md
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
```

## File: checkbox.md
```md
## Checkbox
A control that allows the user to toggle between checked and not checked.
Install: `npx shadcn-svelte@latest add checkbox`

```svelte
<script lang="ts">
 import { Checkbox } from "$lib/components/ui/checkbox/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
 let checked = false;
</script>
 
<div class="flex items-center space-x-2">
 <Checkbox id="terms" bind:checked aria-labelledby="terms-label" />
 <Label
  id="terms-label"
  for="terms"
  class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
 >
  Accept terms and conditions
 </Label>
</div>
```

#### Usage
```svelte
<script lang="ts">
 import { Checkbox } from "$lib/components/ui/checkbox";
</script>
```
```svelte
<Checkbox />
```

#### Examples
```svelte
<script lang="ts">
 import { Checkbox } from "$lib/components/ui/checkbox/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
</script>
 
<div class="items-top flex space-x-2">
 <Checkbox id="terms1" />
 <div class="grid gap-1.5 leading-none">
  <Label
   for="terms1"
   class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
  >
   Accept terms and conditions
  </Label>
  <p class="text-muted-foreground text-sm">
   You agree to our Terms of Service and Privacy Policy.
  </p>
 </div>
</div>
```

#### Disabled
```svelte
<script lang="ts">
 import { Checkbox } from "$lib/components/ui/checkbox/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
</script>
 
<div class="flex items-center space-x-2">
 <Checkbox id="terms" disabled />
 <Label
  for="terms2"
  class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 peer-data-[disabled=true]:cursor-not-allowed peer-data-[disabled=true]:opacity-70"
 >
  Accept terms and conditions
 </Label>
</div>
```

#### Form
```svelte
<script lang="ts" context="module">
 import { z } from "zod";
 export const formSchema = z.object({
  mobile: z.boolean().default(false)
 });
 export type FormSchema = typeof formSchema;
</script>
 
<script lang="ts">
 import SuperDebug, {
  type Infer,
  type SuperValidated,
  superForm
 } from "sveltekit-superforms";
 import { zodClient } from "sveltekit-superforms/adapters";
 import { toast } from "svelte-sonner";
 import { browser } from "$app/environment";
 import { page } from "$app/stores";
 import * as Form from "$lib/components/ui/form/index.js";
 import { Checkbox } from "$lib/components/ui/checkbox/index.js";
 let data: SuperValidated<Infer<FormSchema>> = $page.data.checkboxSingle;
 export { data as form };
 
 const form = superForm(data, {
  validators: zodClient(formSchema),
  onUpdated: ({ form: f }) => {
   if (f.valid) {
    toast.success(`You submitted ${JSON.stringify(f.data, null, 2)}`);
   } else {
    toast.error("Please fix the errors in the form.");
   }
  }
 });
 
 const { form: formData, enhance } = form;
</script>
 
<form action="/?/checkboxSingle" method="POST" class="space-y-6" use:enhance>
 <Form.Field
  {form}
  name="mobile"
  class="flex flex-row items-start space-x-3 space-y-0 rounded-md border p-4"
 >
  <Form.Control let:attrs>
   <Checkbox {...attrs} bind:checked={$formData.mobile} />
   <div class="space-y-1 leading-none">
    <Form.Label>Use different settings for my mobile devices</Form.Label>
    <Form.Description>
     You can manage your mobile notifications in the <a
      href="/examples/forms">mobile settings</a
     > page.
    </Form.Description>
   </div>
   <input name={attrs.name} value={$formData.mobile} hidden />
  </Form.Control>
 </Form.Field>
 <Form.Button>Submit</Form.Button>
 {#if browser}
  <SuperDebug data={$formData} />
 {/if}
</form>
```

```svelte
<script lang="ts" context="module">
 import { z } from "zod";
 
 const items = [
  {
   id: "recents",
   label: "Recents"
  },
  {
   id: "home",
   label: "Home"
  },
  {
   id: "applications",
   label: "Applications"
  },
  {
   id: "desktop",
   label: "Desktop"
  },
  {
   id: "downloads",
   label: "Downloads"
  },
  {
   id: "documents",
   label: "Documents"
  }
 ] as const;
 
 export const formSchema = z.object({
  items: z.array(z.string()).refine((value) => value.some((item) => item), {
   message: "You have to select at least one item."
  })
 });
 export type FormSchema = typeof formSchema;
</script>
 
<script lang="ts">
 import SuperDebug, {
  type Infer,
  type SuperValidated,
  superForm
 } from "sveltekit-superforms";
 import { zodClient } from "sveltekit-superforms/adapters";
 import { toast } from "svelte-sonner";
 import { browser } from "$app/environment";
 import { page } from "$app/stores";
 import * as Form from "$lib/components/ui/form/index.js";
 import { Checkbox } from "$lib/components/ui/checkbox/index.js";
 
 let data: SuperValidated<Infer<FormSchema>> = $page.data.checkboxMultiple;
 export { data as form };
 
 const form = superForm(data, {
  validators: zodClient(formSchema),
  onUpdated: ({ form: f }) => {
   if (f.valid) {
    toast.success(`You submitted ${JSON.stringify(f.data, null, 2)}`);
   } else {
    toast.error("Please fix the errors in the form.");
   }
  }
 });
 
 const { form: formData, enhance } = form;
 
 function addItem(id: string) {
  $formData.items = [...$formData.items, id];
 }
 
 function removeItem(id: string) {
  $formData.items = $formData.items.filter((i) => i !== id);
 }
</script>
 
<form action="/?/checkboxMultiple" method="POST" class="space-y-8" use:enhance>
 <Form.Fieldset {form} name="items" class="space-y-0">
  <div class="mb-4">
   <Form.Legend class="text-base">Sidebar</Form.Legend>
   <Form.Description>
    Select the items you want to display in the sidebar.
   </Form.Description>
  </div>
  <div class="space-y-2">
   {#each items as item}
    {@const checked = $formData.items.includes(item.id)}
    <div class="flex flex-row items-start space-x-3">
     <Form.Control let:attrs>
      <Checkbox
       {...attrs}
       {checked}
       onCheckedChange={(v) => {
        if (v) {
         addItem(item.id);
        } else {
         removeItem(item.id);
        }
       }}
      />
      <Form.Label class="font-normal">
       {item.label}
      </Form.Label>
      <input
       hidden
       type="checkbox"
       name={attrs.name}
       value={item.id}
       {checked}
      />
     </Form.Control>
    </div>
   {/each}
   <Form.FieldErrors />
  </div>
 </Form.Fieldset>
 <Form.Button>Update display</Form.Button>
 {#if browser}
  <SuperDebug data={$formData} />
 {/if}
</form>
```
```

## File: carousel.md
```md
---
title: 
description: 
component: true
source: https://github.com/huntabyte/shadcn-svelte/tree/main/sites/docs/src/lib/registry/default/ui/carousel
bits: https://www.embla-carousel.com/get-started/svelte/
---
# Carousel
A carousel with motion and swipe built using Embla.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="carousel-demo">

<div />

</ComponentPreview>

## About

The carousel component is built using the [Embla Carousel](https://www.embla-carousel.com/get-started/svelte/) library.

## Installation

<PMAddComp name="carousel" />

<ManualInstall>

1. Install `embla-carousel-svelte`:

<PMInstall command="embla-carousel-svelte -D" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as Carousel from "$lib/components/ui/carousel/index.js";
</script>

<Carousel.Root>
  <Carousel.Content>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
  </Carousel.Content>
  <Carousel.Previous />
  <Carousel.Next />
</Carousel.Root>
```

## Examples

### Sizes

To set the size of the items, you can use the `basis` utility class on the `<Carousel.Item />`.

<ComponentPreview name="carousel-size">

<div />

</ComponentPreview>

```svelte title="Example" showLineNumbers {4-6}
<!-- 33% of the carousel width. -->
<Carousel.Root>
  <Carousel.Content>
    <Carousel.Item class="basis-1/3">...</Carousel.Item>
    <Carousel.Item class="basis-1/3">...</Carousel.Item>
    <Carousel.Item class="basis-1/3">...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

```svelte title="Responsive" showLineNumbers {4-6}
<!-- 50% on small screens and 33% on larger screens. -->
<Carousel.Root>
  <Carousel.Content>
    <Carousel.Item class="md:basis-1/2 lg:basis-1/3">...</Carousel.Item>
    <Carousel.Item class="md:basis-1/2 lg:basis-1/3">...</Carousel.Item>
    <Carousel.Item class="md:basis-1/2 lg:basis-1/3">...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

### Spacing

To set the spacing between the items, we use a `pl-[VALUE]` utility on the `<Carousel.Item />` and a negative `-ml-[VALUE]` on the `<Carousel.Content />`.

<ComponentPreview name="carousel-spacing">

<div />

</ComponentPreview>

```svelte title="Example" showLineNumbers /-ml-4/ /pl-4/
<Carousel.Root>
  <Carousel.Content class="-ml-4">
    <Carousel.Item class="pl-4">...</Carousel.Item>
    <Carousel.Item class="pl-4">...</Carousel.Item>
    <Carousel.Item class="pl-4">...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

```svelte title="Responsive" showLineNumbers /-ml-2/ /pl-2/ /md:-ml-4/ /md:pl-4/
<Carousel.Root>
  <Carousel.Content class="-ml-2 md:-ml-4">
    <Carousel.Item class="pl-2 md:pl-4">...</Carousel.Item>
    <Carousel.Item class="pl-2 md:pl-4">...</Carousel.Item>
    <Carousel.Item class="pl-2 md:pl-4">...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

### Orientation

Use the `orientation` prop to set the orientation of the carousel.

<ComponentPreview name="carousel-orientation">

<div />

</ComponentPreview>

```svelte showLineNumbers /vertical | horizontal/
<Carousel.Root orientation="vertical | horizontal">
  <Carousel.Content>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

## Options

You can pass options to the carousel using the `opts` prop. See the [Embla Carousel docs](https://www.embla-carousel.com/api/options/) for more information.

```svelte showLineNumbers {2-5}
<Carousel.Root
  opts={{
    align: "start",
    loop: true,
  }}
>
  <Carousel.Content>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

## API

Use reactive state and the `bind:api` directive to get an instance of the carousel API.

<ComponentPreview name="carousel-api">

<div />

</ComponentPreview>

```svelte showLineNumbers {2,5,18}
<script lang="ts">
  import { type CarouselAPI } from "$lib/components/ui/carousel/context.js";
  import * as Carousel from "$lib/components/ui/carousel/index.js";

  let api: CarouselAPI;
  let count = 0;
  let current = 0;

  $: if (api) {
    count = api.scrollSnapList().length;
    current = api.selectedScrollSnap() + 1;
    api.on("select", () => {
      current = api.selectedScrollSnap() + 1;
    });
  }
</script>

<Carousel.Root bind:api>
  <Carousel.Content>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

## Events

You can listen to events using the api instance from `bind:api`.

```svelte showLineNumbers {2,5,7-11,14}
<script lang="ts">
  import { type CarouselAPI } from "$lib/components/ui/carousel/context.js";
  import * as Carousel from "$lib/components/ui/carousel/index.js";

  let api: CarouselAPI;

  $: if (api) {
    api.on("select", () => {
      // do something on select
    });
  }
</script>

<Carousel.Root bind:api>
  <Carousel.Content>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

## Plugins

You can use the `plugins` prop to add plugins to the carousel.

```svelte showLineNumbers {2,7-11}
<script lang="ts">
  import Autoplay from "embla-carousel-autoplay";
  import * as Carousel from "$lib/components/ui/carousel/index.js";
</script>

<Carousel.Root
  plugins={[
    Autoplay({
      delay: 2000,
    }),
  ]}
>
  <!-- ... -->
</Carousel.Root>
```

<ComponentPreview name="carousel-plugin">

<div />

</ComponentPreview>

See the [Embla Carousel docs](https://www.embla-carousel.com/api/plugins/) for more information on using plugins.

```

## File: breadcrumb.md
```md
# Breadcrumb
Displays the path to the current resource using a hierarchy of links.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp } from '$lib/components/docs';
</script>

<ComponentPreview name="breadcrumb-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="breadcrumb" />

<ManualInstall>

1. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as Breadcrumb from "$lib/components/ui/breadcrumb/index.js";
</script>

<Breadcrumb.Root>
  <Breadcrumb.List>
    <Breadcrumb.Item>
      <Breadcrumb.Link href="/">Home</Breadcrumb.Link>
    </Breadcrumb.Item>
    <Breadcrumb.Separator />
    <Breadcrumb.Item>
      <Breadcrumb.Link href="/components">Components</Breadcrumb.Link>
    </Breadcrumb.Item>
    <Breadcrumb.Separator />
    <Breadcrumb.Item>
      <Breadcrumb.Page>Breadcrumb</Breadcrumb.Page>
    </Breadcrumb.Item>
  </Breadcrumb.List>
</Breadcrumb.Root>
```

## Examples

### Custom separator

Use a custom component in the `<slot>` of `<Breadcrumb.Separator />` to create a custom separator.

<ComponentPreview name="breadcrumb-separator">

<div />

</ComponentPreview>

---

### Dropdown

You can compose `<Breadcrumb.Item />` with a `<DropdownMenu />` to create a dropdown in the breadcrumb.

<ComponentPreview name="breadcrumb-dropdown">

<div />

</ComponentPreview>

---

### Collapsed

We provide a `<Breadcrumb.Ellipsis />` component to show a collapsed state when the breadcrumb is too long.

<ComponentPreview name="breadcrumb-ellipsis">

<div />

</ComponentPreview>

---

### Link component

To use a custom link component from your routing library, you can use the `asChild` prop on `<Breadcrumb.Link />`.

<ComponentPreview name="breadcrumb-link">

<div />

</ComponentPreview>

---

### Responsive

Here's an example of a responsive breadcrumb that composes `<Breadcrumb.Item />` with `<Breadcrumb.Ellipsis />`, `<DropdownMenu />`, and `<Drawer />`.

It displays a dropdown on desktop and a drawer on mobile.

<ComponentPreview name="breadcrumb-responsive">

<div />

</ComponentPreview>

```

## File: popover.md
```md
---
title: Popover
description: Displays rich content in a portal, triggered by a button.
component: true
source: https://github.com/huntabyte/shadcn-svelte/tree/main/sites/docs/src/lib/registry/default/ui/popover
bits: https://www.bits-ui.com/docs/components/popover
---

<script>
  import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="popover-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="popover" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as Popover from "$lib/components/ui/popover";
</script>

<Popover.Root>
  <Popover.Trigger>Open</Popover.Trigger>
  <Popover.Content>Place content for the popover here.</Popover.Content>
</Popover.Root>
```

```

## File: alert-dialog.md
```md
# Alert Dialog
A modal dialog that interrupts the user with important content and expects a response.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="alert-dialog-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="alert-dialog" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as AlertDialog from "$lib/components/ui/alert-dialog";
</script>

<AlertDialog.Root>
  <AlertDialog.Trigger>Open</AlertDialog.Trigger>
  <AlertDialog.Content>
    <AlertDialog.Header>
      <AlertDialog.Title>Are you absolutely sure?</AlertDialog.Title>
      <AlertDialog.Description>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </AlertDialog.Description>
    </AlertDialog.Header>
    <AlertDialog.Footer>
      <AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
      <AlertDialog.Action>Continue</AlertDialog.Action>
    </AlertDialog.Footer>
  </AlertDialog.Content>
</AlertDialog.Root>
```

```

## File: accordion.md
```md
# Accordion
A vertically stacked set of interactive headings that each reveal a section of content.

<script>
    import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="accordion-demo" class="[&_[data-melt-accordion]]:sm:max-w-[70%]">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="accordion" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as Accordion from "$lib/components/ui/accordion";
</script>

<Accordion.Root>
  <Accordion.Item value="item-1">
    <Accordion.Trigger>Is it accessible?</Accordion.Trigger>
    <Accordion.Content>
      Yes. It adheres to the WAI-ARIA design pattern.
    </Accordion.Content>
  </Accordion.Item>
</Accordion.Root>
```

```

## File: card.md
```md
# Card
Displays a card with header, content, and footer.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp } from '$lib/components/docs';
</script>

<ComponentPreview name="card-with-form">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="card" />

<ManualInstall>

1. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as Card from "$lib/components/ui/card";
</script>

<Card.Root>
  <Card.Header>
    <Card.Title>Card Title</Card.Title>
    <Card.Description>Card Description</Card.Description>
  </Card.Header>
  <Card.Content>
    <p>Card Content</p>
  </Card.Content>
  <Card.Footer>
    <p>Card Footer</p>
  </Card.Footer>
</Card.Root>
```

### Modify the heading level

By default, the `<Card.Title>` component renders an `<h3>` element. You can change this by passing a `tag` prop to the component.

For example:

```svelte
<Card.Title tag="h1">This will render an H1</Card.Title>
```

...

```svelte
<Card.Title tag="h6">This will render an H6</Card.Title>
```

## Examples

<ComponentPreview name="card-demo">

<div />

</ComponentPreview>

```

## File: menubar.md
```md
## Menubar
A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands.

**Install:** npx shadcn-svelte@latest add menubar

```svelte
<script lang="ts">
  import * as Menubar from "$lib/components/ui/menubar/index.js";
 
  let bookmarks = false;
  let fullUrls = true;
 
  const profileRadioValue = "benoit";
</script>
 
<Menubar.Root>
  <Menubar.Menu>
    <Menubar.Trigger>File</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Item>
        New Tab <Menubar.Shortcut>⌘T</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Item>
        New Window <Menubar.Shortcut>⌘N</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Item>New Incognito Window</Menubar.Item>
      <Menubar.Separator />
      <Menubar.Sub>
        <Menubar.SubTrigger>Share</Menubar.SubTrigger>
        <Menubar.SubContent>
          <Menubar.Item>Email link</Menubar.Item>
          <Menubar.Item>Messages</Menubar.Item>
          <Menubar.Item>Notes</Menubar.Item>
        </Menubar.SubContent>
      </Menubar.Sub>
      <Menubar.Separator />
      <Menubar.Item>
        Print... <Menubar.Shortcut>⌘P</Menubar.Shortcut>
      </Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
  
  <Menubar.Menu>
    <Menubar.Trigger>Edit</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Item>
        Undo <Menubar.Shortcut>⌘Z</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Item>
        Redo <Menubar.Shortcut>⇧⌘Z</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Separator />
      <Menubar.Sub>
        <Menubar.SubTrigger>Find</Menubar.SubTrigger>
        <Menubar.SubContent>
          <Menubar.Item>Search the web</Menubar.Item>
          <Menubar.Separator />
          <Menubar.Item>Find...</Menubar.Item>
          <Menubar.Item>Find Next</Menubar.Item>
          <Menubar.Item>Find Previous</Menubar.Item>
        </Menubar.SubContent>
      </Menubar.Sub>
      <Menubar.Separator />
      <Menubar.Item>Cut</Menubar.Item>
      <Menubar.Item>Copy</Menubar.Item>
      <Menubar.Item>Paste</Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
  
  <Menubar.Menu>
    <Menubar.Trigger>View</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.CheckboxItem bind:checked={bookmarks}>
        Always Show Bookmarks Bar
      </Menubar.CheckboxItem>
      <Menubar.CheckboxItem bind:checked={fullUrls}>
        Always Show Full URLs
      </Menubar.CheckboxItem>
      <Menubar.Separator />
      <Menubar.Item inset>
        Reload <Menubar.Shortcut>⌘R</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Item inset>
        Force Reload <Menubar.Shortcut>⇧⌘R</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Separator />
      <Menubar.Item inset>Toggle Fullscreen</Menubar.Item>
      <Menubar.Separator />
      <Menubar.Item inset>Hide Sidebar</Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
  
  <Menubar.Menu>
    <Menubar.Trigger>Profiles</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.RadioGroup value={profileRadioValue}>
        <Menubar.RadioItem value="andy">Andy</Menubar.RadioItem>
        <Menubar.RadioItem value="benoit">Benoit</Menubar.RadioItem>
        <Menubar.RadioItem value="Luis">Luis</Menubar.RadioItem>
      </Menubar.RadioGroup>
      <Menubar.Separator />
      <Menubar.Item inset>Edit...</Menubar.Item>
      <Menubar.Separator />
      <Menubar.Item inset>Add Profile...</Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
</Menubar.Root>
```

```

## File: combobox.md
```md
# Combobox
Autocomplete input and command palette with a list of suggestions.

<script>
  import { ComponentPreview, ManualInstall, Callout } from '$lib/components/docs';
</script>

<ComponentPreview name="combobox-demo">

<div />

</ComponentPreview>

## Installation

The Combobox is built using a composition of the `<Popover />` and the `<Command />` components.

See installation instructions for the [Popover](/docs/components/popover#installation) and the [Command](/docs/components/command#installation) components.

## Usage

```svelte
<script lang="ts">
  import Check from "lucide-svelte/icons/check";
  import ChevronsUpDown from "lucide-svelte/icons/chevrons-up-down";
  import * as Command from "$lib/registry/default/ui/command/index.js";
  import * as Popover from "$lib/registry/default/ui/popover/index.js";
  import { Button } from "$lib/registry/default/ui/button/index.js";
  import { cn } from "$lib/utils.js";
  import { tick } from "svelte";

  const frameworks = [
    {
      value: "sveltekit",
      label: "SvelteKit",
    },
    {
      value: "next.js",
      label: "Next.js",
    },
    {
      value: "nuxt.js",
      label: "Nuxt.js",
    },
    {
      value: "remix",
      label: "Remix",
    },
    {
      value: "astro",
      label: "Astro",
    },
  ];

  let open = false;
  let value = "";

  $: selectedValue =
    frameworks.find((f) => f.value === value)?.label ??
    "Select a framework...";

  // We want to refocus the trigger button when the user selects
  // an item from the list so users can continue navigating the
  // rest of the form with the keyboard.
  function closeAndFocusTrigger(triggerId: string) {
    open = false;
    tick().then(() => {
      document.getElementById(triggerId)?.focus();
    });
  }
</script>

<Popover.Root bind:open let:ids>
  <Popover.Trigger asChild let:builder>
    <Button
      builders={[builder]}
      variant="outline"
      role="combobox"
      aria-expanded={open}
      class="w-[200px] justify-between"
    >
      {selectedValue}
      <ChevronsUpDown class="ml-2 h-4 w-4 shrink-0 opacity-50" />
    </Button>
  </Popover.Trigger>
  <Popover.Content class="w-[200px] p-0">
    <Command.Root>
      <Command.Input placeholder="Search framework..." />
      <Command.Empty>No framework found.</Command.Empty>
      <Command.Group>
        {#each frameworks as framework}
          <Command.Item
            value={framework.value}
            onSelect={(currentValue) => {
              value = currentValue;
              closeAndFocusTrigger(ids.trigger);
            }}
          >
            <Check
              class={cn(
                "mr-2 h-4 w-4",
                value !== framework.value && "text-transparent"
              )}
            />
            {framework.label}
          </Command.Item>
        {/each}
      </Command.Group>
    </Command.Root>
  </Popover.Content>
</Popover.Root>
```

## Examples

### Combobox

<ComponentPreview name="combobox-demo">

<div />

</ComponentPreview>

### Popover

<ComponentPreview name="combobox-popover">

<div />

</ComponentPreview>

### Dropdown menu

<ComponentPreview name="combobox-dropdown-menu">

<div />

</ComponentPreview>

### Form

Since the Combobox is built using the `<Popover />` and the `<Command />` components, we need to use the `<Form.Control />` component. `<Form.Control />` enables us to apply the right `aria-*` attributes to non-standard form elements, and adds a hidden input to ensure the form is submitted with the correct value.

Note: You must be on version `0.5.0` or higher of `formsnap` for this to work correctly.

<ComponentPreview name="combobox-form">

<div />

</ComponentPreview>

```

## File: calendar.md
```md
# Calendar
A calendar component that allows users to select dates.

<script>
    import { ComponentPreview, ManualInstall, Callout, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="calendar-demo">

<div />

</ComponentPreview>

## About

The `<Calendar />` component is built on top of the [Bits Calendar](https://www.bits-ui.com/docs/components/calendar) component, which uses the [@internationalized/date](https://react-spectrum.adobe.com/internationalized/date/index.html) package to handle dates.

If you're looking for a range calendar, check out the [Range Calendar](/docs/components/range-calendar) component.

## Installation

<PMAddComp name="calendar" />

<ManualInstall>

1. Install `bits-ui` and `@internationalized/date`:

<PMInstall command="bits-ui @internationalized/date" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Date Picker

You can use the `<Calendar />` component to build a date picker. See the [Date Picker](/docs/components/date-picker) page for more information.

## Examples

### Form

<ComponentPreview name="date-picker-demo">

<div />

</ComponentPreview>

## Advanced Customization

The `<Calendar />` component can be combined with other components to create a more complex calendar.

<Callout>
    By default, we export the combined Calendar component as <code>Calendar</code> as there are quite a few pieces that need to be combined to create it. We're modifying that component in the examples below.
</Callout>

### Month & Year Selects

Here's an example of how you could create a calendar with month and year select dropdowns instead of the previous and next buttons.

<ComponentPreview name="calendar-with-selects">

<div />

</ComponentPreview>

```

## File: button.md
```md
# Button
Displays a button or a component that looks like a button.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="button-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="button" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button";
</script>
```

```svelte
<Button variant="outline">Button</Button>
```

### Link

You can convert the `<button>` into an `<a>` element by simply passing an `href` as a prop.

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button";
</script>

<Button href="/dashboard">Dashboard</Button>
```

Alternatively, you can use the `buttonVariants` helper to create a link that looks like a button.

```svelte
<script lang="ts">
  import { buttonVariants } from "$lib/components/ui/button";
</script>

<a href="/dashboard" class={buttonVariants({ variant: "outline" })}>
  Dashboard
</a>
```

## Examples

### Primary

<ComponentPreview name="button-demo">

<div />

</ComponentPreview>

---

### Secondary

<ComponentPreview name="button-secondary">

<div />

</ComponentPreview>

---

### Destructive

<ComponentPreview name="button-destructive">

<div />

</ComponentPreview>

---

### Outline

<ComponentPreview name="button-outline">

<div />

</ComponentPreview>

---

### Ghost

<ComponentPreview name="button-ghost">

<div />

</ComponentPreview>

---

### Link

<ComponentPreview name="button-link">

<div />

</ComponentPreview>

---

### With Icon

<ComponentPreview name="button-with-icon">

<div />

</ComponentPreview>

---

### Icon

<ComponentPreview name="button-icon">

<div />

</ComponentPreview>

---

### Loading

<ComponentPreview name="button-loading">

<div />

</ComponentPreview>

```

## File: badge.md
```md
# Badge
Displays a badge or a component that looks like a badge.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp } from '$lib/components/docs';
  import { BadgeDemo, BadgeDestructive, BadgeOutline, BadgeSecondary } from '$lib/registry/default/example'
</script>

<ComponentPreview name="badge-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="badge" />

<ManualInstall>

1. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import { Badge } from "$lib/components/ui/badge";
</script>
```

```svelte
<Badge variant="outline">Badge</Badge>
```

### Link

You can use the `badgeVariants` helper to create a link that looks like a badge.

```svelte
<script lang="ts">
  import { badgeVariants } from "$lib/components/ui/badge";
</script>

<a href="/dashboard" class={badgeVariants({ variant: "outline" })}>Badge</a>
```

## Examples

### Default

<ComponentPreview name="badge-demo">

<div />

</ComponentPreview>

---

### Secondary

<ComponentPreview name="badge-secondary">

<div />

</ComponentPreview>

---

### Outline

<ComponentPreview name="badge-outline">

<div />

</ComponentPreview>

---

### Destructive

<ComponentPreview name="badge-destructive">

<div />

</ComponentPreview>

```

## File: avatar.md
```md
# Avatar
An image element with a fallback for representing the user.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="avatar-demo">

<div/>

</ComponentPreview>

## Installation

<PMAddComp name="avatar" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as Avatar from "$lib/components/ui/avatar";
</script>

<Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
</Avatar.Root>
```

```

## File: aspect-ratio.md
```md
# Aspect Ratio
Displays content within a desired ratio.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="aspect-ratio-demo">

<div/>

</ComponentPreview>

## Installation

<PMAddComp name="aspect-ratio" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import { AspectRatio } from "$lib/components/ui/aspect-ratio";
</script>

<div class="w-[450px]">
  <AspectRatio ratio={16 / 9} class="bg-muted">
    <img src="..." alt="..." class="rounded-md object-cover" />
  </AspectRatio>
</div>
```

```

## File: alert.md
```md
# Alert
Displays a callout for user attention.
<script>
  import { ComponentPreview, ManualInstall, PMAddComp } from '$lib/components/docs';
</script>

<ComponentPreview name="alert-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="alert" />

<ManualInstall>

1. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as Alert from "$lib/components/ui/alert";
</script>

<Alert.Root>
  <Alert.Title>Heads up!</Alert.Title>
  <Alert.Description>
    You can add components to your app using the cli.
  </Alert.Description>
</Alert.Root>
```

## Examples

### Default

<ComponentPreview name="alert-demo">

<div />

</ComponentPreview>

### Destructive

<ComponentPreview name="alert-destructive">

<div />

</ComponentPreview>

```

## File: input.md
```md
# Input
Displays a form input field or a component that looks like an input field.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp} from '$lib/components/docs';

  export let form;
</script>

<ComponentPreview name="input-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="input" />

<ManualInstall>

1. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import { Input } from "$lib/components/ui/input";
</script>

<Input />
```

## Examples

### Default

<ComponentPreview name="input-demo">

<div />

</ComponentPreview>

### Disabled

<ComponentPreview name="input-disabled">

<div />

</ComponentPreview>

### With Label

<ComponentPreview name="input-with-label">

<div />

</ComponentPreview>

### With Text

<ComponentPreview name="input-with-text">

<div />

</ComponentPreview>

### With Button

<ComponentPreview name="input-with-button">

<div />

</ComponentPreview>

### File

<ComponentPreview name="input-file">

<div />

</ComponentPreview>

### Form

<ComponentPreview name="form-demo" {form}>

<div />

</ComponentPreview>

```

## File: collapsible.md
```md
# Collapsible
An interactive component which expands/collapses a panel.

<script>
  import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="collapsible-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="collapsible" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import * as Collapsible from "$lib/components/ui/collapsible";
</script>

<Collapsible.Root>
  <Collapsible.Trigger>Can I use this in my project?</Collapsible.Trigger>
  <Collapsible.Content>
    Yes. Free to use for personal and commercial projects. No attribution
    required.
  </Collapsible.Content>
</Collapsible.Root>
```

```

## File: scroll-area.md
```md
# Scroll Area

```svelte
<script lang="ts">
  import { ScrollArea } from "bits-ui";
</script>
 
<div
  class="max-w-[250px] rounded-[10px] border border-dark-10 bg-background-alt px-2 py-4 shadow-card"
>
  <ScrollArea.Root class="relative h-[205px] px-4">
    <ScrollArea.Viewport class="h-full w-full">
      <ScrollArea.Content>
        <h4
          class="mb-4 mt-2 text-[20px] font-semibold leading-none tracking-[-0.01em] text-foreground"
        >
          Scroll Area
        </h4>
        <p class="text-sm leading-5 text-foreground-alt">
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dignissimos
          impedit rem, repellat deserunt ducimus quasi nisi voluptatem cumque
          aliquid esse ea deleniti eveniet incidunt! Deserunt minus laborum
          accusamus iusto dolorum. Lorem ipsum dolor sit, amet consectetur
          adipisicing elit. Blanditiis officiis error minima eos fugit voluptate
          excepturi eveniet dolore et, ratione impedit consequuntur dolorem hic
          quae corrupti autem? Dolorem, sit voluptatum.
        </p>
      </ScrollArea.Content>
    </ScrollArea.Viewport>
    <ScrollArea.Scrollbar
      orientation="vertical"
      class="flex h-full w-2.5 touch-none select-none rounded-full border-l border-l-transparent p-px transition-all hover:w-3 hover:bg-dark-10"
    >
      <ScrollArea.Thumb
        class="relative flex-1 rounded-full bg-muted-foreground opacity-40 transition-opacity hover:opacity-100"
      />
    </ScrollArea.Scrollbar>
    <ScrollArea.Corner />
  </ScrollArea.Root>
</div>
```

## Structure
```svelte
<script lang="ts">
  import { ScrollArea } from "$lib/index.js";
</script>
 
<ScrollArea.Root>
  <ScrollArea.Viewport>
    <ScrollArea.Content>
      <!-- ... -->
    </ScrollArea.Content>
  </ScrollArea.Viewport>
  <ScrollArea.Scrollbar orientation="vertical">
    <ScrollArea.Thumb />
  </ScrollArea.Scrollbar>
  <ScrollArea.Scrollbar orientation="horizontal">
    <ScrollArea.Thumb />
  </ScrollArea.Scrollbar>
  <ScrollArea.Corner />
</ScrollArea.Root>
```
```

## File: toggle.md
```md
---
title: Toggle
description: A two-state button that can be either on or off.
component: true
source: https://github.com/huntabyte/shadcn-svelte/tree/main/sites/docs/src/lib/registry/default/ui/toggle
bits: https://www.bits-ui.com/docs/components/toggle
---

<script>
  import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="toggle-demo">

<div />

</ComponentPreview>

## Installation

<PMAddComp name="toggle" />

<ManualInstall>

1. Install `bits-ui`:

<PMInstall command="bits-ui" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

## Usage

```svelte
<script lang="ts">
  import { Toggle } from "$lib/components/ui/toggle";
</script>

<Toggle>Toggle</Toggle>
```

## Examples

### Default

<ComponentPreview name="toggle-demo">

<div />

</ComponentPreview>

### Outline

<ComponentPreview name="toggle-outline">

<div />

</ComponentPreview>

### With Text

<ComponentPreview name="toggle-with-text">

<div />

</ComponentPreview>

### Small

<ComponentPreview name="toggle-sm">

<div />

</ComponentPreview>

### Large

<ComponentPreview name="toggle-lg">

<div />

</ComponentPreview>

### Disabled

<ComponentPreview name="toggle-disabled">

<div />

</ComponentPreview>

```

## File: range-calendar.md
```md
---
title: Range Calendar
description: A calendar component that allows users to select a range of dates.
component: true
source: https://github.com/huntabyte/shadcn-svelte/tree/main/sites/docs/src/lib/registry/default/ui/range-calendar
bits: https://www.bits-ui.com/docs/components/range-calendar
---

<script>
    import { ComponentPreview, ManualInstall, PMAddComp, PMInstall } from '$lib/components/docs';
</script>

<ComponentPreview name="range-calendar-demo">

<div />

</ComponentPreview>

## About

The `<RangeCalendar />` component is built on top of the [Bits Range Calendar](https://www.bits-ui.com/docs/components/range-calendar) component, which uses the [@internationalized/date](https://react-spectrum.adobe.com/internationalized/date/index.html) package to handle dates.

## Installation

<PMAddComp name="range-calendar" />

<ManualInstall>

1. Install `bits-ui` and `@internationalized/date`:

<PMInstall command="bits-ui @internationalized/date" />

2. Copy and paste the component source files linked at the top of this page into your project.

</ManualInstall>

```

## File: radio-group.md
```md
# Radio Group
A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.

**Install:** `npx shadcn-svelte@latest add radio-group`

## Preview
```svelte
<script lang="ts">
 import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
</script>
 
<RadioGroup.Root value="comfortable">
 <div class="flex items-center space-x-2">
  <RadioGroup.Item value="default" id="r1" />
  <Label for="r1">Default</Label>
 </div>
 <div class="flex items-center space-x-2">
  <RadioGroup.Item value="comfortable" id="r2" />
  <Label for="r2">Comfortable</Label>
 </div>
 <div class="flex items-center space-x-2">
  <RadioGroup.Item value="compact" id="r3" />
  <Label for="r3">Compact</Label>
 </div>
 <RadioGroup.Input name="spacing" />
</RadioGroup.Root>
```

## Usage
```svelte
<script lang="ts">
 import { Label } from "$lib/components/ui/label";
 import * as RadioGroup from "$lib/components/ui/radio-group";
</script>
 
<RadioGroup.Root value="option-one">
 <div class="flex items-center space-x-2">
  <RadioGroup.Item value="option-one" id="option-one" />
  <Label for="option-one">Option One</Label>
 </div>
 <div class="flex items-center space-x-2">
  <RadioGroup.Item value="option-two" id="option-two" />
  <Label for="option-two">Option Two</Label>
 </div>
</RadioGroup.Root>
```

## Examples
```svelte
<script lang="ts" context="module">
 import { z } from "zod";
 
 export const formSchema = z.object({
  type: z.enum(["all", "mentions", "none"], {
   required_error: "You need to select a notification type"
  })
 });
 export type FormSchema = typeof formSchema;
</script>
 
<script lang="ts">
 import SuperDebug, {
  type Infer,
  type SuperValidated,
  superForm
 } from "sveltekit-superforms";
 import { zodClient } from "sveltekit-superforms/adapters";
 import { toast } from "svelte-sonner";
 import { browser } from "$app/environment";
 import { page } from "$app/stores";
 import * as Form from "$lib/components/ui/form/index.js";
 import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
 
 let data: SuperValidated<Infer<FormSchema>> = $page.data.radioGroup;
 export { data as form };
 
 const form = superForm(data, {
  validators: zodClient(formSchema),
  onUpdated: ({ form: f }) => {
   if (f.valid) {
    toast.success(`You submitted ${JSON.stringify(f.data, null, 2)}`);
   } else {
    toast.error("Please fix the errors in the form.");
   }
  }
 });
 
 const { form: formData, enhance } = form;
</script>
 
<form method="POST" action="/?/radioGroup" class="w-2/3 space-y-6" use:enhance>
 <Form.Fieldset {form} name="type" class="space-y-3">
  <Form.Legend>Notify me about...</Form.Legend>
  <RadioGroup.Root
   bind:value={$formData.type}
   class="flex flex-col space-y-1"
  >
   <div class="flex items-center space-x-3 space-y-0">
    <Form.Control let:attrs>
     <RadioGroup.Item value="all" {...attrs} />
     <Form.Label class="font-normal">All new messages</Form.Label>
    </Form.Control>
   </div>
   <div class="flex items-center space-x-3 space-y-0">
    <Form.Control let:attrs>
     <RadioGroup.Item value="mentions" {...attrs} />
     <Form.Label class="font-normal"
      >Direction messages and mentions</Form.Label
     >
    </Form.Control>
   </div>
   <div class="flex items-center space-x-3 space-y-0">
    <Form.Control let:attrs>
     <RadioGroup.Item value="none" {...attrs} />
     <Form.Label class="font-normal">Nothing</Form.Label>
    </Form.Control>
   </div>
   <RadioGroup.Input name="type" />
  </RadioGroup.Root>
  <Form.FieldErrors />
 </Form.Fieldset>
 <Form.Button>Submit</Form.Button>
 {#if browser}
  <SuperDebug data={$formData} />
 {/if}
</form>
```

```

## File: form.md
```md
# Formsnap & Superforms  
Building forms with Formsnap, Superforms, & Zod.

Forms are tricky. They are one of the most common things you'll build in a web application, but also one of the most complex.

Well-designed HTML forms are:
- Well-structured and semantically correct.
- Easy to use and navigate (keyboard).
- Accessible with ARIA attributes and proper labels.
- Supported by client- and server-side validation.
- Well-styled and consistent with the rest of the application.

In this guide, we will take a look at building forms with **Formsnap**, **SvelteKit-Superforms**, and **Zod**.

---

## Features

The form components offered by `shadcn-svelte` are wrappers around **Formsnap** and **SvelteKit-Superforms** which provide a few benefits:

- Composable components for building forms.
- Form field components for scoping form state.
- Form validation using Zod or any other validation library supported by Superforms.
- Applies the correct ARIA attributes to form fields based on their states.
- Enables you to easily use components like `Select`, `RadioGroup`, `Switch`, `Checkbox`, and other form components with Formsnap.

If you're unfamiliar with **Superforms** & **Formsnap**, check out their documentation first, as this guide assumes you have a basic understanding of how they work together.

---

## Anatomy

```html
<form>
  <Form.Field>
    <Form.Control>
      <Form.Label />
      <!-- Any Form input component -->
    </Form.Control>
    <Form.Description />
    <Form.FieldErrors />
  </Form.Field>
</form>
```

### Example

```html
<form method="POST" use:enhance>
  <Form.Field {form} name="email">
    <Form.Control let:attrs>
      <Form.Label>Email</Form.Label>
      <Input {...attrs} bind:value={$formData.email} />
    </Form.Control>
    <Form.Description />
    <Form.FieldErrors />
  </Form.Field>
</form>
```

---

## Installation

```bash
npx shadcn-svelte@latest add form
```

Select package manager: `npm`

---

## Usage

### 1. Create a Form Schema

Define the shape of your form using a **Zod** schema. We’ll define it in a file called `schema.ts` in the same directory as our page component.

```ts
// src/routes/settings/schema.ts
import { z } from "zod";

export const formSchema = z.object({
  username: z.string().min(2).max(50),
});

export type FormSchema = typeof formSchema;
```

### 2. Return the Form from the Route's Load Function

```ts
// src/routes/settings/+page.server.ts
import type { PageServerLoad } from "./$types.js";
import { superValidate } from "sveltekit-superforms";
import { formSchema } from "./schema";
import { zod } from "sveltekit-superforms/adapters";

export const load: PageServerLoad = async () => {
  return {
    form: await superValidate(zod(formSchema)),
  };
};
```

### 3. Create a Form Component

In this example, we'll pass the form returned from the load function as a prop to this component.

```svelte
<!-- src/routes/settings/settings-form.svelte -->
<script lang="ts">
  import * as Form from "$lib/components/ui/form";
  import { Input } from "$lib/components/ui/input";
  import { formSchema, type FormSchema } from "./schema";
  import {
    type SuperValidated,
    type Infer,
    superForm,
  } from "sveltekit-superforms";
  import { zodClient } from "sveltekit-superforms/adapters";

  export let data: SuperValidated<Infer<FormSchema>>;

  const form = superForm(data, {
    validators: zodClient(formSchema),
  });

  const { form: formData, enhance } = form;
</script>

<form method="POST" use:enhance>
  <Form.Field {form} name="username">
    <Form.Control let:attrs>
      <Form.Label>Username</Form.Label>
      <Input {...attrs} bind:value={$formData.username} />
    </Form.Control>
    <Form.Description>This is your public display name.</Form.Description>
    <Form.FieldErrors />
  </Form.Field>
  <Form.Button>Submit</Form.Button>
</form>
```

The name, id, and all accessibility attributes are applied to the input by spreading the `attrs` object from the `Form.Control` component. The `Form.Label` will automatically associate with the input using the `for` attribute.

### 4. Create a Page Component

Pass the form data from the load function to the form component.

```svelte
<!-- src/routes/settings/+page.svelte -->
<script lang="ts">
  import type { PageData } from "./$types.js";
  import SettingsForm from "./settings-form.svelte";
  export let data: PageData;
</script>

<SettingsForm data={data.form} />
```

### 5. Create an Action to Handle Form Submission

```ts
// src/routes/settings/+page.server.ts
import type { PageServerLoad, Actions } from "./$types.js";
import { fail } from "@sveltejs/kit";
import { superValidate } from "sveltekit-superforms";
import { zod } from "sveltekit-superforms/adapters";
import { formSchema } from "./schema";

export const load: PageServerLoad = async () => {
  return {
    form: await superValidate(zod(formSchema)),
  };
};

export const actions: Actions = {
  default: async (event) => {
    const form = await superValidate(event, zod(formSchema));
    if (!form.valid) {
      return fail(400, { form });
    }
    return { form };
  },
};
```

---

## Done

That's it! You now have a fully accessible form that is type-safe with client- and server-side validation.

### Example Form

```html
<form method="POST" use:enhance>
  <Form.Field {form} name="username">
    <Form.Control let:attrs>
      <Form.Label>Username</Form.Label>
      <Input {...attrs} bind:value={$formData.username} />
    </Form.Control>
    <Form.Description>This is your public display name.</Form.Description>
    <Form.FieldErrors />
  </Form.Field>
  <Form.Button>Submit</Form.Button>
</form>
```

---

## Next Steps

Be sure to check out the **Formsnap** and **Superforms** documentation for more information on how to use them effectively.
```

## File: select.md
```md
# Select
Displays a list of options for the user to pick from—triggered by a button.

### **Preview**
```svelte
<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
 
  const fruits = [
    { value: "apple", label: "Apple" },
    { value: "banana", label: "Banana" },
    { value: "blueberry", label: "Blueberry" },
    { value: "grapes", label: "Grapes" },
    { value: "pineapple", label: "Pineapple" }
  ];
</script>
 
<Select.Root portal={null}>
  <Select.Trigger class="w-[180px]">
    <Select.Value placeholder="Select a fruit" />
  </Select.Trigger>
  <Select.Content>
    <Select.Group>
      <Select.Label>Fruits</Select.Label>
      {#each fruits as fruit}
        <Select.Item value={fruit.value} label={fruit.label}>
          {fruit.label}
        </Select.Item>
      {/each}
    </Select.Group>
  </Select.Content>
  <Select.Input name="favoriteFruit" />
</Select.Root>
```

### **Installation**
```bash
npx shadcn-svelte@latest add select
```

- **Package manager:** `npm`

### **Manual Installation**

### **Usage**
```svelte
<script lang="ts">
  import * as Select from "$lib/components/ui/select";
</script>
 
<Select.Root>
  <Select.Trigger class="w-[180px]">
    <Select.Value placeholder="Theme" />
  </Select.Trigger>
  <Select.Content>
    <Select.Item value="light">Light</Select.Item>
    <Select.Item value="dark">Dark</Select.Item>
    <Select.Item value="system">System</Select.Item>
  </Select.Content>
</Select.Root>
```

### **Examples**
#### **Form**
For more advanced usage and to learn how to implement multiple `Select` components in a form, check out the Bits UI Select Recipe on Formsnap.

### **Preview**
```svelte
<!-- Style: Default -->
<Email>
  Select a verified email to display.
  You can manage email addresses in your email settings.
</Email>
Submit

200
{
  email: ""
}
```
```

## File: separator.md
```md
# Separator
Visually or semantically separates content.
Install: `npx shadcn-svelte@latest add separator`

```svelte
<script lang="ts">
  import { Separator } from "$lib/components/ui/separator/index.js";
</script>
 
<div>
  <div class="space-y-1">
    <h4 class="text-sm font-medium leading-none">Radix Primitives</h4>
    <p class="text-muted-foreground text-sm">
      An open-source UI component library.
    </p>
  </div>
  <Separator class="my-4" />
  <div class="flex h-5 items-center space-x-4 text-sm">
    <div>Blog</div>
    <Separator orientation="vertical" />
    <div>Docs</div>
    <Separator orientation="vertical" />
    <div>Source</div>
  </div>
</div>
```

## Usage
```svelte
<script lang="ts">
 import { Separator } from "$lib/components/ui/separator";
</script>
 
<Separator />
```
```

## File: sheet.md
```md
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
```

## File: skeleton.md
```md
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
```

## File: slider.md
```md
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
```

## File: sonner.md
```md
# Sonner
An opinionated toast component for Svelte.
**Install:** `npx shadcn-svelte@latest add sonner`

```svelte
<script lang="ts">
 import { toast } from "svelte-sonner";
 import { Button } from "$lib/components/ui/button/index.js";
</script>
 
<Button
 variant="outline"
 on:click={() =>
  toast.success("Event has been created", {
   description: "Sunday, December 03, 2023 at 9:00 AM",
   action: {
    label: "Undo",
    onClick: () => console.info("Undo")
   }
  })}
>
 Show Toast
</Button>
```

### Setup theme support
```svelte
By default, Sonner will use the user's system preferences to determine whether to show the light or dark theme. To get around this, you can either pass in a custom theme prop to the component, or simply use mode-watcher which you can hardcode to dark or light mode should you wish.

You can learn more about setting up Dark Mode support here.

If you wish to opt out of Dark Mode support, you can uninstall mode-watcher and remove the theme prop from the component after installing via CLI, or manually install the component and don't include mode-watcher
```

### Add the Toaster component:
Note: Make sure you are adding the import from the path "$lib/components/ui/sonner" not "svelte-sonner".

#### +layout.svelte`
```svelte
<script lang="ts">
 import { Toaster } from "$lib/components/ui/sonner";
</script>
 
<Toaster />
 
<slot />
```

### Usage
```svelte
<script lang="ts">
 import { toast } from "svelte-sonner";
 import { Button } from "$lib/components/ui/button";
</script>
 
<Button on:click={() => toast("Hello world")}>Show toast</Button>
```
```

## File: switch.md
```md
# Switch
A control that allows the user to toggle between checked and not checked.
**Install:** `npx shadcn-svelte@latest add switch`

```svelte
<script lang="ts">
 import { Label } from "$lib/components/ui/label/index.js";
 import { Switch } from "$lib/components/ui/switch/index.js";
</script>
 
<div class="flex items-center space-x-2">
 <Switch id="airplane-mode" />
 <Label for="airplane-mode">Airplane Mode</Label>
</div>
```

### Usage
```svelte
<script lang="ts">
 import { Switch } from "$lib/components/ui/switch";
</script>
 
<Switch />`
```

### Examples

```svelte
<script lang="ts" context="module">
 import { z } from "zod";
 export const formSchema = z.object({
  marketing_emails: z.boolean().default(false).optional(),
  security_emails: z.boolean().default(true)
 });
 export type FormSchema = typeof formSchema;
</script>
 
<script lang="ts">
 import SuperDebug, {
  type Infer,
  type SuperValidated,
  superForm
 } from "sveltekit-superforms";
 import { zodClient } from "sveltekit-superforms/adapters";
 import { toast } from "svelte-sonner";
 import { browser } from "$app/environment";
 import { page } from "$app/stores";
 import * as Form from "$lib/components/ui/form/index.js";
 import { Switch } from "$lib/components/ui/switch/index.js";
 let data: SuperValidated<Infer<FormSchema>> = $page.data.switch;
 export { data as form };
 
 const form = superForm(data, {
  validators: zodClient(formSchema),
  onUpdated: ({ form: f }) => {
   if (f.valid) {
    toast.success(`You submitted ${JSON.stringify(f.data, null, 2)}`);
   } else {
    toast.error("Please fix the errors in the form.");
   }
  }
 });
 
 const { form: formData, enhance } = form;
</script>
 
<form method="POST" action="/?/switch" class="w-full space-y-6" use:enhance>
 <fieldset>
  <legend class="mb-4 text-lg font-medium"> Email Notifications </legend>
  <div class="space-y-4">
   <Form.Field
    {form}
    name="marketing_emails"
    class="flex flex-row items-center justify-between rounded-lg border p-4"
   >
    <Form.Control let:attrs>
     <div class="space-y-0.5">
      <Form.Label>Marketing emails</Form.Label>
      <Form.Description>
       Receive emails about new products, features, and more.
      </Form.Description>
     </div>
     <Switch
      includeInput
      {...attrs}
      bind:checked={$formData.marketing_emails}
     />
    </Form.Control>
   </Form.Field>
   <Form.Field
    {form}
    name="security_emails"
    class="flex flex-row items-center justify-between rounded-lg border p-4"
   >
    <Form.Control let:attrs>
     <div class="space-y-0.5">
      <Form.Label>Security emails</Form.Label>
      <Form.Description>
       Receive emails about your account security.
      </Form.Description>
     </div>
     <Switch
      {...attrs}
      aria-readonly
      disabled
      includeInput
      bind:checked={$formData.security_emails}
     />
    </Form.Control>
   </Form.Field>
  </div>
 </fieldset>
 <Form.Button>Submit</Form.Button>
 {#if browser}
  <SuperDebug data={$formData} />
 {/if}
</form>
```
```

## File: table.md
```md
# Table
A responsive table component.
**Install:** `npx shadcn-svelte@latest add table`

```svelte
<script lang="ts">
 import * as Table from "$lib/components/ui/table/index.js";
 
 const invoices = [
  {
   invoice: "INV001",
   paymentStatus: "Paid",
   totalAmount: "$250.00",
   paymentMethod: "Credit Card"
  },
  {
   invoice: "INV002",
   paymentStatus: "Pending",
   totalAmount: "$150.00",
   paymentMethod: "PayPal"
  },
  {
   invoice: "INV003",
   paymentStatus: "Unpaid",
   totalAmount: "$350.00",
   paymentMethod: "Bank Transfer"
  },
  {
   invoice: "INV004",
   paymentStatus: "Paid",
   totalAmount: "$450.00",
   paymentMethod: "Credit Card"
  },
  {
   invoice: "INV005",
   paymentStatus: "Paid",
   totalAmount: "$550.00",
   paymentMethod: "PayPal"
  },
  {
   invoice: "INV006",
   paymentStatus: "Pending",
   totalAmount: "$200.00",
   paymentMethod: "Bank Transfer"
  },
  {
   invoice: "INV007",
   paymentStatus: "Unpaid",
   totalAmount: "$300.00",
   paymentMethod: "Credit Card"
  }
 ];
</script>
 
<Table.Root>
 <Table.Caption>A list of your recent invoices.</Table.Caption>
 <Table.Header>
  <Table.Row>
   <Table.Head class="w-[100px]">Invoice</Table.Head>
   <Table.Head>Status</Table.Head>
   <Table.Head>Method</Table.Head>
   <Table.Head class="text-right">Amount</Table.Head>
  </Table.Row>
 </Table.Header>
 <Table.Body>
  {#each invoices as invoice, i (i)}
   <Table.Row>
    <Table.Cell class="font-medium">{invoice.invoice}</Table.Cell>
    <Table.Cell>{invoice.paymentStatus}</Table.Cell>
    <Table.Cell>{invoice.paymentMethod}</Table.Cell>
    <Table.Cell class="text-right">{invoice.totalAmount}</Table.Cell>
   </Table.Row>
  {/each}
 </Table.Body>
</Table.Root>
```

## Usage
```svelte
<script lang="ts">
 import * as Table from "$lib/components/ui/table";
</script>
```
```svelte
<Table.Root>
 <Table.Caption>A list of your recent invoices.</Table.Caption>
 <Table.Header>
  <Table.Row>
   <Table.Head class="w-[100px]">Invoice</Table.Head>
   <Table.Head>Status</Table.Head>
   <Table.Head>Method</Table.Head>
   <Table.Head class="text-right">Amount</Table.Head>
  </Table.Row>
 </Table.Header>
 <Table.Body>
  <Table.Row>
   <Table.Cell class="font-medium">INV001</Table.Cell>
   <Table.Cell>Paid</Table.Cell>
   <Table.Cell>Credit Card</Table.Cell>
   <Table.Cell class="text-right">$250.00</Table.Cell>
  </Table.Row>
 </Table.Body>
</Table.Root>
```

```

## File: tabs.md
```md
# Tabs
A set of layered sections of content—known as tab panels—that are displayed one at a time.
**Install:** `npx shadcn-svelte@latest add tabs`

```svelte
<script lang="ts">
 import * as Tabs from "$lib/components/ui/tabs/index.js";
 import * as Card from "$lib/components/ui/card/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import { Input } from "$lib/components/ui/input/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
</script>
 
<Tabs.Root value="account" class="w-[400px]">
 <Tabs.List class="grid w-full grid-cols-2">
  <Tabs.Trigger value="account">Account</Tabs.Trigger>
  <Tabs.Trigger value="password">Password</Tabs.Trigger>
 </Tabs.List>
 <Tabs.Content value="account">
  <Card.Root>
   <Card.Header>
    <Card.Title>Account</Card.Title>
    <Card.Description>
     Make changes to your account here. Click save when you're done.
    </Card.Description>
   </Card.Header>
   <Card.Content class="space-y-2">
    <div class="space-y-1">
     <Label for="name">Name</Label>
     <Input id="name" value="Pedro Duarte" />
    </div>
    <div class="space-y-1">
     <Label for="username">Username</Label>
     <Input id="username" value="@peduarte" />
    </div>
   </Card.Content>
   <Card.Footer>
    <Button>Save changes</Button>
   </Card.Footer>
  </Card.Root>
 </Tabs.Content>
 <Tabs.Content value="password">
  <Card.Root>
   <Card.Header>
    <Card.Title>Password</Card.Title>
    <Card.Description>
     Change your password here. After saving, you'll be logged out.
    </Card.Description>
   </Card.Header>
   <Card.Content class="space-y-2">
    <div class="space-y-1">
     <Label for="current">Current password</Label>
     <Input id="current" type="password" />
    </div>
    <div class="space-y-1">
     <Label for="new">New password</Label>
     <Input id="new" type="password" />
    </div>
   </Card.Content>
   <Card.Footer>
    <Button>Save password</Button>
   </Card.Footer>
  </Card.Root>
 </Tabs.Content>
</Tabs.Root>
```

## Usage
```svelte
<script lang="ts">
 import * as Tabs from "$lib/components/ui/tabs";
</script>
 
<Tabs.Root value="account" class="w-[400px]">
 <Tabs.List>
  <Tabs.Trigger value="account">Account</Tabs.Trigger>
  <Tabs.Trigger value="password">Password</Tabs.Trigger>
 </Tabs.List>
 <Tabs.Content value="account">
  Make changes to your account here.
 </Tabs.Content>
 <Tabs.Content value="password">Change your password here.</Tabs.Content>
</Tabs.Root>
```
```

## File: textarea.md
```md
# Textarea
Displays a form textarea or a component that looks like a textarea.
Install: `npx shadcn-svelte@latest add textarea`

```svelte
<script lang="ts">
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<Textarea placeholder="Type your message here." />
```

## Usage
```svelte
<script lang="ts">
 import { Textarea } from "$lib/components/ui/textarea";
</script>
```
```svelte
<Textarea />
```

## Examples
```svelte
<script lang="ts">
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<Textarea placeholder="Type your message here." />
```

### Disabled
```svelte
<script lang="ts">
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<Textarea disabled placeholder="Type your message here." />
```

### With Label
```svelte
<script lang="ts">
 import { Label } from "$lib/components/ui/label/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<div class="grid w-full gap-1.5">
 <Label for="message">Your message</Label>
 <Textarea placeholder="Type your message here." id="message" />
</div>
```

### With Text
```svelte
<script lang="ts">
 import { Label } from "$lib/components/ui/label/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<div class="grid w-full gap-1.5">
 <Label for="message-2">Your Message</Label>
 <Textarea placeholder="Type your message here." id="message-2" />
 <p class="text-muted-foreground text-sm">
  Your message will be copied to the support team.
 </p>
</div>
```

### With Button
```svelte
<script lang="ts">
 import { Button } from "$lib/components/ui/button/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
</script>
 
<div class="grid w-full gap-2">
 <Textarea placeholder="Type your message here." />
 <Button>Send message</Button>
</div>
```

### Form`
``svelte
<script lang="ts" context="module">
 import { z } from "zod";
 export const formSchema = z.object({
  bio: z
   .string()
   .min(10, "Bio must be at least 10 characters.")
   .max(160, "Bio must be at most 160 characters.")
 });
 export type FormSchema = typeof formSchema;
</script>
 
<script lang="ts">
 import SuperDebug, {
  type Infer,
  type SuperValidated,
  superForm
 } from "sveltekit-superforms";
 import { zodClient } from "sveltekit-superforms/adapters";
 import { toast } from "svelte-sonner";
 import { browser } from "$app/environment";
 import { page } from "$app/stores";
 import * as Form from "$lib/components/ui/form/index.js";
 import { Textarea } from "$lib/components/ui/textarea/index.js";
 
 let data: SuperValidated<Infer<FormSchema>> = $page.data.textarea;
 export { data as form };
 
 const form = superForm(data, {
  validators: zodClient(formSchema),
  onUpdated: ({ form: f }) => {
   if (f.valid) {
    toast.success(`You submitted ${JSON.stringify(f.data, null, 2)}`);
   } else {
    toast.error("Please fix the errors in the form.");
   }
  }
 });
 
 const { form: formData, enhance } = form;
</script>
 
<form method="POST" action="/?/textarea" class="w-2/3 space-y-6" use:enhance>
 <Form.Field {form} name="bio">
  <Form.Control let:attrs>
   <Form.Label>Bio</Form.Label>
   <Textarea
    {...attrs}
    placeholder="Tell us a little bit about yourself"
    class="resize-none"
    bind:value={$formData.bio}
   />
   <Form.Description>
    You can <span>@mention</span> other users and organizations.
   </Form.Description>
  </Form.Control>
  <Form.FieldErrors />
 </Form.Field>
 <Form.Button>Submit</Form.Button>
 {#if browser}
  <SuperDebug data={$formData} />
 {/if}
</form>
```

 
<Textarea placeholder="Type your message here." />
```


