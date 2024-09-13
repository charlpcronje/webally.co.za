# Carousel
A carousel with motion and swipe built using Embla.

Install: `npx  shadcn-svelte@latest add carousel`
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

#### Examples

- Sizes
```svelte
<script lang="ts">
 import * as Card from "$lib/components/ui/card/index.js";
 import * as Carousel from "$lib/components/ui/carousel/index.js";
</script>
 
<Carousel.Root
 opts={{
  align: "start"
 }}
 class="w-full max-w-sm"
>
 <Carousel.Content>
  {#each Array(5) as _, i (i)}
   <Carousel.Item class="md:basis-1/2 lg:basis-1/3">
    <div class="p-1">
     <Card.Root>
      <Card.Content
       class="flex aspect-square items-center justify-center p-6"
      >
       <span class="text-3xl font-semibold">{i + 1}</span>
      </Card.Content>
     </Card.Root>
    </div>
   </Carousel.Item>
  {/each}
 </Carousel.Content>
 <Carousel.Previous />
 <Carousel.Next />
</Carousel.Root>
```

- **Example:** 
```svelte
<!-- 33% of the carousel width. -->
<Carousel.Root>
 <Carousel.Content>
  <Carousel.Item class="basis-1/3">...</Carousel.Item>
  <Carousel.Item class="basis-1/3">...</Carousel.Item>
  <Carousel.Item class="basis-1/3">...</Carousel.Item>
 </Carousel.Content>
</Carousel.Root>
```

- **Responsive**
```svelte
<!-- 50% on small screens and 33% on larger screens. -->
<Carousel.Root>
 <Carousel.Content>
  <Carousel.Item class="md:basis-1/2 lg:basis-1/3">...</Carousel.Item>
  <Carousel.Item class="md:basis-1/2 lg:basis-1/3">...</Carousel.Item>
  <Carousel.Item class="md:basis-1/2 lg:basis-1/3">...</Carousel.Item>
 </Carousel.Content>
</Carousel.Root>
```

#### Spacing
To set the spacing between the items, we use a `pl-[VALUE]` utility on the `<Carousel.Item />` and a negative `-ml-[VALUE]` on the `<Carousel.Content />`.

```svelte
<script lang="ts">
 import * as Card from "$lib/components/ui/card/index.js";
 import * as Carousel from "$lib/components/ui/carousel/index.js";
</script>
 
<Carousel.Root class="w-full max-w-sm">
 <Carousel.Content class="-ml-1">
  {#each Array(5) as _, i (i)}
   <Carousel.Item class="pl-1 md:basis-1/2 lg:basis-1/3">
    <div class="p-1">
     <Card.Root>
      <Card.Content
       class="flex aspect-square items-center justify-center p-6"
      >
       <span class="text-2xl font-semibold">{i + 1}</span>
      </Card.Content>
     </Card.Root>
    </div>
   </Carousel.Item>
  {/each}
 </Carousel.Content>
 <Carousel.Previous />
 <Carousel.Next />
</Carousel.Root>
```

- **Example:**
```svelte
<Carousel.Root>
 <Carousel.Content class="-ml-4">
  <Carousel.Item class="pl-4">...</Carousel.Item>
  <Carousel.Item class="pl-4">...</Carousel.Item>
  <Carousel.Item class="pl-4">...</Carousel.Item>
 </Carousel.Content>
</Carousel.Root>
```

- **Responsive:**
```svelte
<Carousel.Root>
 <Carousel.Content class="-ml-2 md:-ml-4">
  <Carousel.Item class="pl-2 md:pl-4">...</Carousel.Item>
  <Carousel.Item class="pl-2 md:pl-4">...</Carousel.Item>
  <Carousel.Item class="pl-2 md:pl-4">...</Carousel.Item>
 </Carousel.Content>
</Carousel.Root>
```

#### Orientation
Use the orientation prop to set the orientation of the carousel.

```svelte
<script lang="ts">
 import * as Card from "$lib/components/ui/card/index.js";
 import * as Carousel from "$lib/components/ui/carousel/index.js";
</script>
 
<Carousel.Root
 opts={{
  align: "start"
 }}
 orientation="vertical"
 class="w-full max-w-xs"
>
 <Carousel.Content class="-mt-1 h-[200px]">
  {#each Array(5) as _, i (i)}
   <Carousel.Item class="pt-1 md:basis-1/2">
    <div class="p-1">
     <Card.Root>
      <Card.Content class="flex items-center justify-center p-6">
       <span class="text-3xl font-semibold">{i + 1}</span>
      </Card.Content>
     </Card.Root>
    </div>
   </Carousel.Item>
  {/each}
 </Carousel.Content>
 <Carousel.Previous />
 <Carousel.Next />
</Carousel.Root>
```
```svelte
<Carousel.Root orientation="vertical | horizontal">
  <Carousel.Content>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
    <Carousel.Item>...</Carousel.Item>
  </Carousel.Content>
</Carousel.Root>
```

### Options
You can pass options to the carousel using the opts prop. See the Embla Carousel docs for more information.
```svelte
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