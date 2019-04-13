
/**
 *
 * @param {string} url url to fetch from network
 * @param {object} options defines http options
 */
async function get(url, options = {}) {
  const data = await fetch(url, {
    method: 'GET',
    ...options,
  });
  return data.json();
}

/**
 *
 * @param {*} url url to fetch from network
 * @param {*} options defines http options
 */
async function post(url, options = {}) {
  const data = await fetch(url, {
    method: 'POST',
    ...options,
  });
  return data.json();
}


export {
  get, post,
};
