# Plugins
It's possible to extend Embla carousel with additional features using plugins. The complete list of official plugins can be found here.

Installation
All official plugins are separate NPM packages. They're all prefixed with embla-carousel followed by its unique plugin name. For example, the Autoplay plugin is installed like so:

## Installation
```
npm install embla-carousel-autoplay --save
```

## Usage
The Embla Carousel constructor accepts an array of plugins. Each plugin might have its own options, methods and events.

### Adding a plugin
The constructor plugin array is the default way of providing plugins to Embla Carousel. In the following example, the Autoplay plugin is added to the carousel:

```js
import EmblaCarousel from 'embla-carousel'
import Autoplay from 'embla-carousel-autoplay'

const emblaNode = document.querySelector('.embla')
const embla = EmblaCarousel(emblaNode, { loop: true }, [Autoplay()])
```

Note for Svelte: Note that it's possible to change plugins passed to the Embla Carousel constructor after initialization with the reInit method.

### Constructor options
```js
import EmblaCarousel from 'embla-carousel'
import Autoplay from 'embla-carousel-autoplay'

const emblaNode = document.querySelector('.embla')
const embla = EmblaCarousel(emblaNode, { loop: true }, [
  Autoplay({ delay: 4000 })
])
```
- **Note Svelte:** Make sure to assign global options before initializing any carousel and only assign it once. Re-assigning global options might lead to confusing code and unexpected behaviour.


```js
import EmblaCarousel from 'embla-carousel'
import Autoplay from 'embla-carousel-autoplay'

const emblaNode = document.querySelector('.embla')
const embla = EmblaCarousel(emblaNode, { loop: true }, [Autoplay()])
```
Note that it's possible to change plugins passed to the Embla Carousel constructor after initialization with the reInit method.

### Constructor options
Plugins have their own specific options which is the first argument of the plugin constructor. This allows for configuring the plugin to your liking:

```js
import EmblaCarousel from 'embla-carousel'
import Autoplay from 'embla-carousel-autoplay'

const emblaNode = document.querySelector('.embla')
const embla = EmblaCarousel(emblaNode, { loop: true }, [
  Autoplay({ delay: 4000 })
])
```

### Global options
All official plugins allows you to set global options that will be applied to all instances. This allows for overriding the default plugin options with your own:

```js
import EmblaCarousel from 'embla-carousel'
import Autoplay from 'embla-carousel-autoplay'

Autoplay.globalOptions = { delay: 4000 }

const emblaNode = document.querySelector('.embla')
const embla = EmblaCarousel(emblaNode, { loop: true }, [Autoplay()])
```

### Adding event listeners
Some plugins fire their own events. Plugin events are structured as follows `<plugin-name>:eventname`. Adding and removing plugin event listeners is done the same way as native Embla events. Here's an example where an event is added to the autoplay plugin:

```js
import EmblaCarousel from 'embla-carousel'
import Autoplay from 'embla-carousel-autoplay'

const emblaNode = document.querySelector('.embla')
const emblaApi = EmblaCarousel(emblaNode, { loop: true }, [Autoplay()])

function logPluginEvent(emblaApi, eventName) {
  console.log(`Autoplay just triggered ${eventName}!`)
}

emblaApi.on('autoplay:stop', logPluginEvent)
```

### TypeScript
The `EmblaPluginType` is obtained directly from the core package `embla-carousel` and used like so:

```js
import EmblaCarousel, { EmblaPluginType } from 'embla-carousel'
import Autoplay from 'embla-carousel-autoplay'

const emblaNode = document.querySelector('.embla')
const plugins: EmblaPluginType[] = [Autoplay()]
const emblaApi = EmblaCarousel(emblaNode, { loop: true }, plugins)
```





