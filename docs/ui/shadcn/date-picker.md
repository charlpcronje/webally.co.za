# Date Picker
A date picker component with range and presets.

## Install
```
The Date Picker is built using a composition of the `<Popover />` and either the `<Calendar />` or `<RangeCalendar />` components.

See installations instructions for the Popover, Calendar, and Range Calendar components.

```svelte
<script lang="ts">
 import CalendarIcon from "lucide-svelte/icons/calendar";
 import {
  DateFormatter,
  type DateValue,
  getLocalTimeZone
 } from "@internationalized/date";
 import { cn } from "$lib/utils.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import { Calendar } from "$lib/components/ui/calendar/index.js";
 import * as Popover from "$lib/components/ui/popover/index.js";
 
 const df = new DateFormatter("en-US", {
  dateStyle: "long"
 });
 
 let value: DateValue | undefined = undefined;
</script>
 
<Popover.Root>
 <Popover.Trigger asChild let:builder>
  <Button
   variant="outline"
   class={cn(
    "w-[280px] justify-start text-left font-normal",
    !value && "text-muted-foreground"
   )}
   builders={[builder]}
  >
   <CalendarIcon class="mr-2 h-4 w-4" />
   {value ? df.format(value.toDate(getLocalTimeZone())) : "Pick a date"}
  </Button>
 </Popover.Trigger>
 <Popover.Content class="w-auto p-0">
  <Calendar bind:value initialFocus />
 </Popover.Content>
</Popover.Root>
```

Here is the formatted version of your code snippets:

---

### **Examples**

#### **Date Picker**

**Preview**

---

**Code:**

```html
<script lang="ts">
  import CalendarIcon from "lucide-svelte/icons/calendar";
  import { DateFormatter, type DateValue, getLocalTimeZone } from "@internationalized/date";
  import { cn } from "$lib/utils.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";

  const df = new DateFormatter("en-US", { dateStyle: "long" });

  let value: DateValue | undefined = undefined;
</script>

<Popover.Root>
  <Popover.Trigger asChild let:builder>
    <Button
      variant="outline"
      class={cn(
        "w-[280px] justify-start text-left font-normal",
        !value && "text-muted-foreground"
      )}
      builders={[builder]}
    >
      <CalendarIcon class="mr-2 h-4 w-4" />
      {value ? df.format(value.toDate(getLocalTimeZone())) : "Pick a date"}
    </Button>
  </Popover.Trigger>
  <Popover.Content class="w-auto p-0">
    <Calendar bind:value initialFocus />
  </Popover.Content>
</Popover.Root>
```

---

#### **Date Range Picker**

**Preview**

---

**Code:**

```html
<script lang="ts">
  import CalendarIcon from "lucide-svelte/icons/calendar";
  import type { DateRange } from "bits-ui";
  import { CalendarDate, DateFormatter, type DateValue, getLocalTimeZone } from "@internationalized/date";
  import { cn } from "$lib/utils.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { RangeCalendar } from "$lib/components/ui/range-calendar/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";

  const df = new DateFormatter("en-US", { dateStyle: "medium" });

  let value: DateRange | undefined = {
    start: new CalendarDate(2022, 1, 20),
    end: new CalendarDate(2022, 1, 20).add({ days: 20 })
  };

  let startValue: DateValue | undefined = undefined;
</script>

<div class="grid gap-2">
  <Popover.Root openFocus>
    <Popover.Trigger asChild let:builder>
      <Button
        variant="outline"
        class={cn(
          "w-[300px] justify-start text-left font-normal",
          !value && "text-muted-foreground"
        )}
        builders={[builder]}
      >
        <CalendarIcon class="mr-2 h-4 w-4" />
        {#if value && value.start}
          {#if value.end}
            {df.format(value.start.toDate(getLocalTimeZone()))} - {df.format(
              value.end.toDate(getLocalTimeZone())
            )}
          {:else}
            {df.format(value.start.toDate(getLocalTimeZone()))}
          {/if}
        {:else if startValue}
          {df.format(startValue.toDate(getLocalTimeZone()))}
        {:else}
          Pick a date
        {/if}
      </Button>
    </Popover.Trigger>
    <Popover.Content class="w-auto p-0" align="start">
      <RangeCalendar
        bind:value
        bind:startValue
        initialFocus
        numberOfMonths={2}
        placeholder={value?.start}
      />
    </Popover.Content>
  </Popover.Root>
</div>
```

---

#### **With Presets**

**Preview**

---

**Code:**

```html
<script lang="ts">
  import CalendarIcon from "lucide-svelte/icons/calendar";
  import { DateFormatter, type DateValue, getLocalTimeZone, today } from "@internationalized/date";
  import { cn } from "$lib/utils.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import * as Select from "$lib/components/ui/select/index.js";

  const df = new DateFormatter("en-US", { dateStyle: "long" });

  let value: DateValue | undefined = undefined;

  const items = [
    { value: 0, label: "Today" },
    { value: 1, label: "Tomorrow" },
    { value: 3, label: "In 3 days" },
    { value: 7, label: "In a week" }
  ];
</script>

<Popover.Root openFocus>
  <Popover.Trigger asChild let:builder>
    <Button
      variant="outline"
      class={cn(
        "w-[280px] justify-start text-left font-normal",
        !value && "text-muted-foreground"
      )}
      builders={[builder]}
    >
      <CalendarIcon class="mr-2 h-4 w-4" />
      {value ? df.format(value.toDate(getLocalTimeZone())) : "Pick a date"}
    </Button>
  </Popover.Trigger>
  <Popover.Content class="flex w-auto flex-col space-y-2 p-2">
    <Select.Root
      {items}
      onSelectedChange={(v) => {
        if (!v) return;
        value = today(getLocalTimeZone()).add({ days: v.value });
      }}
    >
      <Select.Trigger>
        <Select.Value placeholder="Select" />
      </Select.Trigger>
      <Select.Content>
        {#each items as item}
          <Select.Item value={item.value}>{item.label}</Select.Item>
        {/each}
      </Select.Content>
    </Select.Root>
    <div class="rounded-md border">
      <Calendar bind:value />
    </div>
  </Popover.Content>
</Popover.Root>
```

---

#### **Form**

**Preview**

---

**Code:**

```html
<script lang="ts" context="module">
  import { z } from "zod";

  export const formSchema = z.object({
    dob: z
      .string()
      .refine((v) => v, { message: "A date of birth is required." })
  });

  export type FormSchema = typeof formSchema;
</script>

<script lang="ts">
  import CalendarIcon from "lucide-svelte/icons/calendar";
  import {
    CalendarDate,
    DateFormatter,
    type DateValue,
    getLocalTimeZone,
    parseDate,
    today
  } from "@internationalized/date";
  import type { Infer, SuperValidated } from "sveltekit-superforms";
  import SuperDebug, { superForm } from "sveltekit-superforms";
  import { zodClient } from "sveltekit-superforms/adapters";
  import { toast } from "svelte-sonner";
  import { browser } from "$app/environment";
  import { page } from "$app/stores";
  import { cn } from "$lib/utils.js";
  import {
    Button,
    buttonVariants
  } from "$lib/components/ui/button/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import * as Form from "$lib/components/ui/form/index.js";
  let data: SuperValidated<Infer<FormSchema>> = $page.data.datePicker;
  export { data as form };

  const form = superForm(data, {
    validators: zodClient(formSchema),
    taintedMessage: null,
    onUpdated: ({ form: f }) => {
      if (f.valid) {
        toast.success(`You submitted ${JSON.stringify(f.data, null, 2)}`);
      } else {
        toast.error("Please fix the errors in the form.");
      }
    }
  });

  const { form: formData, enhance } = form;

  const df = new DateFormatter("en-US", { dateStyle: "long" });

  let value: DateValue | undefined;

  $: value = $formData.dob ? parseDate($formData.dob) : undefined;

  let placeholder: DateValue = today(getLocalTimeZone());
</script>

<form method="POST" action="/?/datePicker" class="space-y-8" use:enhance>
  <Form.Field {form} name="dob" class="flex flex-col">
    <Form.Control let:attrs>
      <Form.Label>Date of birth</Form.Label>
      <Popover.Root>
        <Popover.Trigger
          {...attrs}
          class={cn(
            buttonVariants({ variant: "outline" }),
            "w-[280px] justify-start pl-4 text-left font-normal",
            !value && "text-muted-foreground"
          )}
        >
          {value ? df.format(value.toDate(getLocalTimeZone())) : "Pick a date"}
          <CalendarIcon class="ml-auto h-4 w-4 opacity-50" />
        </Popover.Trigger>
        <Popover.Content class="w-auto p-0" side="top">
          <Calendar
            {value}
            bind:placeholder
            minValue={new CalendarDate(1900, 1, 1)}
            maxValue={today(getLocalTimeZone())}
            calendarLabel="Date of birth"
            initialFocus
            onValueChange={(v) => {
              if (v) {
                $formData.dob = v.toString();
              } else {
                $formData.dob = "";
              }
            }}
          />
        </Popover.Content>
      </Popover.Root>
      <Form

.Description>
        Your date of birth is used to calculate your age
      </Form.Description>
      <Form.FieldErrors />
      <input hidden value={$formData.dob} name={attrs.name} />
    </Form.Control>
  </Form.Field>
  <Button type="submit">Submit</Button>
  {#if browser}
    <SuperDebug data={$formData} />
  {/if}
</form>
```

---

Let me know if you'd like further assistance!