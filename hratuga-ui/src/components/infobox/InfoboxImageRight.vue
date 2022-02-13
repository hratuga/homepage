<template>
  <div class="relative max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:px-8">
      <div class="mt-8 lg:grid lg:grid-cols-2 lg:gap-8">
        <div class="relative lg:row-start-1 lg:col-start-2">
          <div class="relative text-base mx-auto max-w-prose lg:max-w-none">
            <figure>
              <div class="aspect-w-12 aspect-h-7 lg:aspect-none">
                <slot name="img">
                </slot>
              </div> 
            </figure>
          </div>
        </div>
        <div class="mt-8 lg:mt-0">
          <div class="text-base max-w-prose mx-auto lg:max-w-none">
            <div>
              <slot name="content">
                </slot>
            </div>
          </div>
        </div>
      </div>
  </div>
 </template>

<script>
export default {
  name: "InfoboxImageRight"  
}
</script>