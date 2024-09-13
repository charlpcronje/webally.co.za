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
