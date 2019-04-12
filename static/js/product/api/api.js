
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
  const jsonData = await data.json();
  return jsonData;
}

/**
 *
 * @param {*} url url to fetch from network
 * @param {*} options defines http options
 */
async function post(url, options = {}) {
  const data = fetch(url, {
    method: 'POST',
    ...options,
  });
  const jsonData = data.json();
  return jsonData;
}


export {
  get, post,
};
