

function createElement(el, props = {}) {
  const $el = document.createElement(el);
  console.log(props);
  Object.keys(props).forEach((prop) => {
    console.log(props);
    $el[prop] = props[prop];
  });
  return $el;
}

function createTextElement(text = '') {
  const $text = document.createTextNode(text);
  return $text;
}

export {
  createElement,
  createTextElement,
};
