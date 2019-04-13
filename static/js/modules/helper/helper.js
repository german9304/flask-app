
/**
 *
 * @param {string} el element to create
 * @param {object} props properties from object
 */
function createElement(el, props = {}) {
  const $el = document.createElement(el);
  Object.keys(props).forEach((prop) => {
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
