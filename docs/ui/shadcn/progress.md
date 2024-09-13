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