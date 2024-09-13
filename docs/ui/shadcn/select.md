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