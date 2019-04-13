import { createElement } from './helper/helper';

const spinner = createElement('div', { className: 'spinner' });
spinner.innerHTML = `
  <p> loading ... </p>
`;

export default spinner;
