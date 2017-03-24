export default function (name) {
  return function (resolve) {
    require([`@/components/${name}.vue`], resolve)
  }
}
